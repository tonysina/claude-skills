#!/usr/bin/env python3
"""Aggregate grading.json files from an eval run into one Markdown table.

usage: tests/evals/aggregate.py tests/evals/runs/<date> [--md out.md]

Run layout: <date>/<skill>/e<id>-<arm>/grading.json, where arm is with, without,
or old (the previous committed version of the skill).
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

root = Path(sys.argv[1])
out = None
if "--md" in sys.argv:
    out = Path(sys.argv[sys.argv.index("--md") + 1])

rows = []
for g in sorted(root.glob("*/e*-*/grading.json")):
    skill = g.parent.parent.name
    eid, arm = g.parent.name.split("-", 1)
    meta = json.load(open(g.parent / "eval_metadata.json"))
    d = json.load(open(g))
    s = d["summary"]
    fails = [e["text"][:70] for e in d["expectations"] if not e["passed"]]
    rows.append((skill, int(eid[1:]), meta["name"], arm, s["passed"], s["total"], s["pass_rate"], fails))

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
