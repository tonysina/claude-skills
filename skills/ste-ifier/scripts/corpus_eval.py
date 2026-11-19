#!/usr/bin/env python3
"""Score the checker against the example pairs in ASD-STE100 Issue 9 itself.

  python3 corpus_eval.py [--show N] [--dump FILE.json]

Corpus:
  rules  Part 1 and general-recommendation pairs ("Non-STE: / STE:", "Do not write: / WRITE:").
  dict   Dictionary pairs: each non-approved word, its alternative, the non-STE example,
         and the official STE example (printed in capitals, scored in sentence case).
  ok     STE examples of approved words (no pair; used for false alarms only).

Scores:
  recall  rules: the non-STE sentence gets at least one finding.
          dict:  the checker flags the entry's own word in its non-STE sentence.
  false alarms: an official STE sentence gets a hard word finding (not approved in any
          part of speech, not a term) or a structure error.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ste_dict as S  # noqa: E402

UNITS = set("mm cm m km kg g mg l ml kpa psi v a w hz khz mhz s ms min h ft in lb nm °c °f".split())


def sentence_case(t):
    t = t.lower()
    return re.sub(r"(^|[.!?:]\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), t)


def rule_pairs(lines):
    """Pairs from Part 1 (and GR) with the rule they illustrate."""
    body = max(i for i, l in enumerate(lines) if l.strip() == "Part 1 – Writing rules")
    end = max(i for i, l in enumerate(lines) if l.strip() == "Part 2 – Dictionary")
    rule, pairs, cur, mode = None, [], None, None
    for l in lines[body:end]:
        m = re.match(r"^\s*(Rule (\d+\.\d+)|(GR-\d))\s", l)
        if m:
            rule = m.group(2) or m.group(3)
        s = l.strip()
        nm = re.match(r"^(Non-STE|Do not write):\s*(.*)", s)
        sm = re.match(r"^(STE|WRITE):\s*(.*)", s)
        if nm:
            cur = {"rule": rule, "non": nm.group(2), "ste": []}
            pairs.append(cur)
            mode = "non"
        elif sm and cur:
            cur["ste"].append(sm.group(2))
            mode = "ste"
        elif not s or s.startswith("(") or s == "or" or re.match(r"^[A-Z][a-z]+( [a-z]+)*:$", s):
            mode = None if not s or s.startswith("(") else mode
        elif mode == "non" and l.startswith(" " * 10):
            cur["non"] += "\n" + s  # keep line breaks: vertical lists and paragraphs stay separate
        elif mode == "ste" and l.startswith(" " * 10):
            cur["ste"][-1] += "\n" + s
        else:
            mode = None
    return [p for p in pairs if p["non"] and p["ste"]]


def split_region(text):
    """Split a dictionary line's example region into (STE part, non-STE part) by letter case."""
    toks = text.split()
    for i, t in enumerate(toks):
        letters = re.sub(r"[^A-Za-z°]", "", t)
        if not letters or not re.search(r"[a-z]", letters):
            continue
        if t.lower().strip(".,") in UNITS and i and re.search(r"\d", toks[i - 1]):
            continue
        return " ".join(toks[:i]), " ".join(toks[i:])
    return " ".join(toks), ""


def dict_pairs(entries):
    pairs, ok_examples = [], []
    for e in entries:
        lines = [l for l in e["lines"] if l.strip()]
        fields = [(m.start(), m.group()) for m in re.finditer(r"\S+(?: \S+)*", lines[0])]
        if len(fields) < 3:
            continue
        x3 = fields[2][0]
        if e["approved"]:
            ste = " ".join(split_region(l[x3 - 1:])[0] for l in lines)
            if re.search(r"[A-Z]{2}", ste):
                ok_examples.append({"head": e["head"], "ste": ste})
            continue
        cur = None
        for l in lines:
            alt = l[:x3 - 1].strip()
            if l is lines[0]:
                alt = re.split(r"\s{2,}", l.strip())[1] if len(fields) > 1 else ""
            ste, non = split_region(l[x3 - 1:])
            if alt and re.match(r"[A-Z]", alt):
                cur = {"head": e["head"], "pos": e["pos"], "alt": alt, "ste": "", "non": ""}
                pairs.append(cur)
            if cur:
                cur["ste"] += " " + ste
                cur["non"] += " " + non
    out = []
    for p in pairs:
        p["ste"], p["non"] = " ".join(p["ste"].split()), " ".join(p["non"].split())
        if re.search(r"[A-Z]{2}", p["ste"]) and re.search(r"[a-z]", p["non"]):
            out.append(p)
    return out, ok_examples


def hard_findings(res, terms):
    words = [k for k, f in res["words"].items() if S.hard(k, f)]
    errors = [f for f in res["structure"] if f[2] == "error"]
    return words, errors


def main():
    show = int(sys.argv[sys.argv.index("--show") + 1]) if "--show" in sys.argv else 0
    raw = S.text()
    idx = S.index(S.parse(raw))
    terms = {}
    for f in sorted((S.SKILL / "terms").glob("*.md")):
        terms.update(S.parse_terms(f.read_text(), f.name))
    rp = rule_pairs(raw.splitlines())
    dp, ok = dict_pairs(S.parse(raw))
    report = {"rules": [], "dict": [], "ok": []}

    # rules corpus
    miss_by_rule, fa_by_rule, n_by_rule = Counter(), Counter(), Counter()
    for p in rp:
        n = S.analyze(idx, p["non"], terms)
        detected = bool(n["words"] or n["structure"])
        ste = S.analyze(idx, p["ste"][0], terms)
        hw, he = hard_findings(ste, terms)
        n_by_rule[p["rule"]] += 1
        miss_by_rule[p["rule"]] += not detected
        fa_by_rule[p["rule"]] += bool(hw or he)
        report["rules"].append({**p, "detected": detected, "found": sorted(n["words"]) + [f[1] for f in n["structure"]],
                                "false_alarm": hw + [f"{f[1]} {f[3]}" for f in he]})

    # dictionary corpus
    for p in dp:
        n = S.analyze(idx, p["non"], terms)
        hit = any(e["head"] == p["head"] for f in n["words"].values() for e in f["hits"])
        ste = S.analyze(idx, sentence_case(p["ste"]), terms)
        hw, he = hard_findings(ste, terms)
        report["dict"].append({**p, "hit": hit, "found": sorted(n["words"]),
                               "false_alarm": hw + [f"{f[1]} {f[3]}" for f in he]})
    for p in ok:
        ste = S.analyze(idx, sentence_case(p["ste"]), terms)
        hw, he = hard_findings(ste, terms)
        report["ok"].append({**p, "false_alarm": hw + [f"{f[1]} {f[3]}" for f in he]})

    R, D, O = report["rules"], report["dict"], report["ok"]
    pct = lambda a, b: f"{100 * a / b:.1f}%" if b else "n/a"
    print(f"RULE EXAMPLES   {len(R)} pairs")
    print(f"  recall (non-STE sentence flagged)      {pct(sum(r['detected'] for r in R), len(R))}")
    print(f"  false alarms on official STE           {pct(sum(bool(r['false_alarm']) for r in R), len(R))}")
    print("  by rule (pairs / missed / false alarms):")
    print("   " + "  ".join(f"{k}:{n_by_rule[k]}/{miss_by_rule[k]}/{fa_by_rule[k]}"
                            for k in sorted(n_by_rule, key=lambda r: (str(r).startswith("GR"), [int(x) for x in re.findall(r"\d+", str(r))]))))
    print(f"DICTIONARY      {len(D)} pairs, {len(O)} approved-word examples")
    print(f"  recall (entry's own word flagged)      {pct(sum(d['hit'] for d in D), len(D))}")
    print(f"  false alarms on official STE (pairs)   {pct(sum(bool(d['false_alarm']) for d in D), len(D))}")
    print(f"  false alarms on approved-word examples {pct(sum(bool(o['false_alarm']) for o in O), len(O))}")
    fa = Counter(x.split(" ")[0] if " " in x else x for r in D + O + R for x in r["false_alarm"])
    print("  most frequent false alarms: " + ", ".join(f"{k} ({v})" for k, v in fa.most_common(15)))
    if show:
        print("\nMISSED DICTIONARY WORDS (sample)")
        for d in [d for d in D if not d["hit"]][:show]:
            print(f"  {d['head']} ({d['pos']}): {d['non']}")
        print("\nFALSE ALARMS ON OFFICIAL STE (sample)")
        for r in [r for r in D + O + R if r["false_alarm"]][:show]:
            print(f"  {r['false_alarm']}: {(r['ste'] if isinstance(r['ste'], str) else r['ste'][0])[:140]!r}")
        print("\nMISSED RULE EXAMPLES")
        for r in [r for r in R if not r["detected"]][:show]:
            print(f"  [{r['rule']}] {r['non']}")
    if "--dump" in sys.argv:
        Path(sys.argv[sys.argv.index("--dump") + 1]).write_text(json.dumps(report, indent=1))


if __name__ == "__main__":
    main()
