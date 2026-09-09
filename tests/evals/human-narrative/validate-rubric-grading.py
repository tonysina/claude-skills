#!/usr/bin/env python3
"""Check a rubric-grading.json against the schema in agents/rubric-grader.md.

usage: tests/evals/human-narrative/validate-rubric-grading.py <rubric-grading.json> ...
       ... --negative-cases    also assert interventions_allowed == 0

Structural only. It cannot tell you a score is wrong -- that needs a reader, or a
second judge and a diff. What it does catch is the shape errors that make a run
unusable: a missing field, a side outside the vocabulary, a feature scored with no
evidence behind it, a cluster fired on a gate alone, an intervention budget that
does not follow from the adjusted cluster count.
"""
import json
import sys
from pathlib import Path

TOP = {"input_path", "output_path", "register", "register_hint", "register_agrees",
       "register_reason", "clusters_in_scope", "input_scores", "output_scores",
       "response_checks", "notes", "rubric_feedback"}
FEATURE = {"id", "feature", "scale", "value", "side", "evidence"}
SIDES = {"ai", "human", "neutral", "not_in_scope", "not_applicable"}
SCALES = {"%", "L", "o"}
REGISTERS = {"fiction", "thought-leadership", "case-study", "short-professional", "hard-stop"}
VERDICTS = {"within-human-range", "some-clustering", "systematic-clustering"}
CHECKS = {"register-call", "intervention-count", "intervention-order", "guardrails",
          "forbidden-constructions", "proportionality", "fidelity"}
# 32 rows over 30 distinct features: Reference Explicitness is A6/F1 and Subplot
# Integration is C8/G2, each scored once and read by two clusters.
IDS = ({f"A{n}" for n in range(1, 7)} | {f"B{n}" for n in range(1, 7)}
       | {f"C{n}" for n in range(1, 9)} | {f"D{n}" for n in range(1, 5)}
       | {"E1", "E2", "F1", "F2"} | {f"G{n}" for n in range(1, 5)})
BUDGET = {"within-human-range": 0, "some-clustering": 2, "systematic-clustering": 3}


def check(path, negative=False):
    errs, warns = [], []
    try:
        d = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e:
        return [f"unreadable: {e}"], []

    for k in sorted(TOP - set(d)):
        errs.append(f"missing top-level field: {k}")
    for k in sorted(set(d) - TOP):
        warns.append(f"unexpected top-level field: {k}")
    if d.get("register") not in REGISTERS:
        errs.append(f"register {d.get('register')!r} not one of {sorted(REGISTERS)}")

    if d.get("register") == "hard-stop":
        i = d.get("input_scores") or {}
        if i.get("interventions_allowed") not in (0, None):
            errs.append("hard-stop must allow 0 interventions")
        if i.get("clusters_fired_raw") not in (0, None):
            errs.append("hard-stop must score no clusters")
        return errs, warns

    i = d.get("input_scores")
    if not isinstance(i, dict):
        errs.append("input_scores missing")
        return errs, warns

    feats = i.get("features") or []
    seen = {}
    for f in feats:
        fid = f.get("id", "?")
        for k in sorted(FEATURE - set(f)):
            errs.append(f"{fid}: missing field {k}")
        if fid not in IDS:
            errs.append(f"{fid}: not a rubric feature id")
        if fid in seen:
            errs.append(f"{fid}: scored twice")
        seen[fid] = f
        if f.get("side") not in SIDES:
            errs.append(f"{fid}: side {f.get('side')!r} not one of {sorted(SIDES)}")
        if f.get("scale") not in SCALES:
            warns.append(f"{fid}: scale {f.get('scale')!r} not one of {sorted(SCALES)}")
        if f.get("side") not in ("not_in_scope",) and not str(f.get("evidence") or "").strip():
            errs.append(f"{fid}: scored {f.get('side')} with empty evidence")
    for missing in sorted(IDS - set(seen)):
        errs.append(f"{missing}: not scored at all")

    # B1's override needs its numerator and denominator, not its ratio
    b1 = seen.get("B1", {})
    if b1.get("side") not in ("not_in_scope",):
        tot, emb = i.get("emotional_beats_total"), i.get("emotional_beats_embodied")
        if not isinstance(tot, int) or not isinstance(emb, int):
            errs.append("emotional_beats_total / _embodied must both be integers")
        elif emb > tot:
            errs.append(f"emotional_beats_embodied {emb} > total {tot}")
        elif tot >= 2 and emb / tot > 0.6 and b1.get("side") != "ai":
            errs.append(f"B1 override: {emb}/{tot} embodied is >60% but B1 scored "
                        f"{b1.get('side')}")
        elif tot == 0 and b1.get("side") not in ("not_applicable", "neutral"):
            errs.append(f"B1: 0 emotional beats but scored {b1.get('side')!r} "
                        f"(expected not_applicable)")
        elif tot == 1 and b1.get("side") == "ai" and emb == 1:
            warns.append("B1: scored ai on a single embodied beat; the >60% override "
                         "needs 2 beats, so this must rest on the dominant-mode call")

    fired = []
    for c in i.get("clusters") or []:
        cid = c.get("id", "?")
        if c.get("fired") is True:
            fired.append(cid)
            if not (c.get("corroborators_ai_side") or []):
                errs.append(f"cluster {cid}: fired with no AI-side corroborator "
                            f"(a gate alone is never a finding)")
            if c.get("gate_side") != "ai":
                errs.append(f"cluster {cid}: fired with gate_side "
                            f"{c.get('gate_side')!r}")

    raw, adj = i.get("clusters_fired_raw"), i.get("clusters_fired_adjusted")
    if raw is not None and raw != len(fired):
        errs.append(f"clusters_fired_raw {raw} != {len(fired)} clusters marked fired")
    ef = i.get("ef_rule_applied")
    if isinstance(raw, int) and isinstance(adj, int):
        collapse = set(fired) >= {"E", "F"} and not ({"A", "B"} & set(fired))
        expected = raw - 1 if collapse else raw
        if adj != expected:
            errs.append(f"clusters_fired_adjusted {adj} != {expected} "
                        f"(E/F collapse {'applies' if collapse else 'does not apply'})")
        if ef is not collapse:
            warns.append(f"ef_rule_applied {ef} but E/F collapse "
                         f"{'applies' if collapse else 'does not apply'}")

    v = i.get("verdict")
    if v not in VERDICTS:
        errs.append(f"verdict {v!r} not one of {sorted(VERDICTS)}")
    elif isinstance(adj, int):
        want = ("within-human-range" if adj <= 1
                else "some-clustering" if adj <= 3 else "systematic-clustering")
        if v != want:
            errs.append(f"verdict {v!r} does not follow from {adj} adjusted clusters "
                        f"(expected {want!r})")
    allowed = i.get("interventions_allowed")
    if v in BUDGET and allowed != BUDGET[v]:
        errs.append(f"interventions_allowed {allowed} != {BUDGET[v]} for verdict {v!r}")

    rc = d.get("response_checks")
    if d.get("output_path"):
        if not rc:
            errs.append("output_path given but response_checks is empty")
        else:
            names = {c.get("check") for c in rc}
            for m in sorted(CHECKS - names):
                errs.append(f"response_checks: missing {m}")
            for c in rc:
                if c.get("passed") is False and not str(c.get("evidence") or "").strip():
                    errs.append(f"response_checks {c.get('check')}: failed with no evidence")
    elif rc:
        warns.append("response_checks present for an input-only score")

    if negative and allowed != 0:
        errs.append(f"NEGATIVE CASE: interventions_allowed is {allowed}, expected 0")
    return errs, warns


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    negative = "--negative-cases" in sys.argv
    if not args:
        sys.exit(__doc__)
    bad = 0
    for p in args:
        errs, warns = check(p, negative)
        status = "FAIL" if errs else "ok"
        print(f"[{status}] {p}")
        for e in errs:
            print(f"    ERROR {e}")
        for w in warns:
            print(f"    warn  {w}")
        bad += bool(errs)
    print(f"\n{len(args)} file(s), {bad} failing")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
