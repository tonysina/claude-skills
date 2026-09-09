#!/usr/bin/env python3
"""Aggregate grading.json files from an eval run into one Markdown table.

usage: tests/evals/aggregate.py tests/evals/runs/<date> [--md out.md]
       tests/evals/aggregate.py tests/evals/runs/<date> --variance [--md out.md]

Run layout: <date>/<skill>/e<id>-<arm>/grading.json, where arm is with, without,
or old (the previous committed version of the skill).

--variance treats the arms as repeat runs of one configuration rather than as
different configurations, and reports spread instead of a single mean. Use it on a
run whose arms are r1, r2, r3 -- the same skill version executed three times.

Why spread and not just a mean: a pass rate from one run is a point estimate with
no error bar, so a later number that moves cannot be told apart from noise. #4 was
opened because humanizer 0.94 -> 0.88 was triaged as a regression on single runs of
each. Per eval it reports min/max and the pass/total of each run, because an eval
that swings is the thing worth finding; per skill it reports the mean of the
per-run suite rates, the population stdev over those runs, and the range.

stdev over three runs is a weak estimate and is printed for ordering, not for
inference. The per-eval range is the more honest signal at this sample size.
"""
import json
import statistics
import sys
from collections import defaultdict
from pathlib import Path

root = Path(sys.argv[1])
out = None
if "--md" in sys.argv:
    out = Path(sys.argv[sys.argv.index("--md") + 1])

variance = "--variance" in sys.argv

rows = []
for g in sorted(root.glob("*/e*-*/grading.json")):
    skill = g.parent.parent.name
    eid, arm = g.parent.name.split("-", 1)
    meta = json.load(open(g.parent / "eval_metadata.json"))
    d = json.load(open(g))
    s = d["summary"]
    fails = [e["text"][:70] for e in d["expectations"] if not e["passed"]]
    rows.append((skill, int(eid[1:]), meta["name"], arm, s["passed"], s["total"], s["pass_rate"], fails))

def variance_report(rows):
    """Per-eval spread across runs, then per-skill mean/stdev/range over run rates."""
    out = []
    by_eval = defaultdict(dict)
    names = {}
    for skill, eid, name, arm, p, t, r, fails in rows:
        by_eval[(skill, eid)][arm] = (p, t, r)
        names[(skill, eid)] = name
    arms = sorted({a for v in by_eval.values() for a in v})

    out += [f"## Per eval, across {len(arms)} runs", ""]
    hdr = "| Skill | Eval | " + " | ".join(arms) + " | mean | min | max | range |"
    out += [hdr, "|" + "---|" * (len(arms) + 6)]
    for (skill, eid), per in sorted(by_eval.items()):
        rs = [per[a][2] for a in arms if a in per]
        if not rs:
            continue
        cells = []
        for a in arms:
            if a in per:
                p, t, r = per[a]
                cells.append(f"{p}/{t} ({r:.2f})")
            else:
                cells.append("-")
        spread = max(rs) - min(rs)
        mark = " **" if spread >= 0.25 else " "
        out.append(f"| {skill} | {eid} {names[(skill, eid)]} | " + " | ".join(cells)
                   + f" | {sum(rs) / len(rs):.2f} | {min(rs):.2f} | {max(rs):.2f} |"
                   + f"{mark}{spread:.2f}{mark.strip()} |")
    out += ["", "`**` marks an eval whose pass rate moved by 0.25 or more between "
            "identical runs.", ""]

    # per-skill: the suite rate for each run, then spread over those
    out += ["## Per skill, over run-level suite pass rates", ""]
    out += ["| Skill | Evals | " + " | ".join(arms) + " | mean | stdev | min | max | range |",
            "|" + "---|" * (len(arms) + 7)]
    by_skill = defaultdict(lambda: defaultdict(list))
    for skill, eid, name, arm, p, t, r, fails in rows:
        by_skill[skill][arm].append(r)
    for skill, per_arm in sorted(by_skill.items()):
        run_rates = [sum(v) / len(v) for a, v in sorted(per_arm.items())]
        cells = [f"{sum(per_arm[a]) / len(per_arm[a]):.2f}" if a in per_arm else "-"
                 for a in arms]
        n_evals = max(len(v) for v in per_arm.values())
        sd = statistics.pstdev(run_rates) if len(run_rates) > 1 else 0.0
        out.append(f"| {skill} | {n_evals} | " + " | ".join(cells)
                   + f" | {sum(run_rates) / len(run_rates):.2f} | {sd:.3f} |"
                   + f" {min(run_rates):.2f} | {max(run_rates):.2f} |"
                   + f" {max(run_rates) - min(run_rates):.2f} |")
    out += ["", "stdev is the population stdev over the run-level suite rates. At "
            "three runs it orders the skills; it does not support inference. The "
            "per-eval range above is the more honest signal.", ""]
    return out


if variance:
    text = "\n".join(variance_report(rows))
    print(text)
    if out:
        out.write_text(text + "\n", encoding="utf-8")
    sys.exit(0)

lines = ["| Skill | Eval | Arm | Passed | Rate | Failed expectations |", "|---|---|---|---|---|---|"]
for skill, eid, name, arm, p, t, r, fails in rows:
    lines.append(f"| {skill} | {eid} {name} | {arm} | {p}/{t} | {r:.2f} | {'; '.join(fails) or '-'} |")

lines += ["", "| Skill | Arm | Evals | Mean pass rate |", "|---|---|---|---|"]
agg = defaultdict(list)
for skill, eid, name, arm, p, t, r, fails in rows:
    agg[(skill, arm)].append(r)
for (skill, arm), rs in sorted(agg.items()):
    lines.append(f"| {skill} | {arm} | {len(rs)} | {sum(rs) / len(rs):.2f} |")

text = "\n".join(lines)
print(text)
if out:
    out.write_text(text + "\n", encoding="utf-8")
