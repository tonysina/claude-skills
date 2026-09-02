#!/usr/bin/env python3
"""Run scan-ai-tells quietly over a labelled corpus and print distributions.

usage: calibrate.py <scan-ai-tells.py> <humanizer SKILL.md> <label>=<dir> [<label>=<dir> ...]
"""
import importlib.util
import statistics
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location("scan", sys.argv[1])
scan = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scan)

flags = scan.load_flags(sys.argv[2])
sets = {}
for arg in sys.argv[3:]:
    label, d = arg.split("=", 1)
    rows = [scan.scan(p, flags, quiet=True) for p in sorted(Path(d).glob("*.txt"))]
    sets[label] = rows


def pct(vals, q):
    vals = sorted(vals)
    if not vals:
        return float("nan")
    k = (len(vals) - 1) * q
    lo, hi = int(k), min(int(k) + 1, len(vals) - 1)
    return vals[lo] + (vals[hi] - vals[lo]) * (k - lo)


for label, rows in sets.items():
    n = len(rows)
    words = sum(r["words"] for r in rows)
    dens = [r["density"] for r in rows]
    pats = [r["patterns"] for r in rows]
    cons = [r["cons"] for r in rows]
    print(f"\n== {label}: {n} blocks, {words} words ==")
    print(f"  density/100w  median {statistics.median(dens):.2f}  "
          f"p25 {pct(dens, .25):.2f}  p75 {pct(dens, .75):.2f}  p90 {pct(dens, .9):.2f}  "
          f"max {max(dens):.2f}  zero-hit blocks {sum(1 for d in dens if d == 0)}")
    print(f"  patterns hit  median {statistics.median(pats):.1f}  "
          f"p25 {pct(pats, .25):.1f}  p75 {pct(pats, .75):.1f}  p90 {pct(pats, .9):.1f}  "
          f"max {max(pats)}")
    print(f"  constructions  blocks with >=1: {sum(1 for c in cons if c)}/{n}")
    from collections import Counter
    c = Counter(pid for r in rows for pid in r["pattern_ids"])
    print("  pattern frequency (blocks):", ", ".join(f"{k}={v}" for k, v in c.most_common()))

# Candidate thresholds: for each rule, precision/recall on pos vs everything else
pos = sets.get("pos", [])
neg = [r for k, rows in sets.items() if k != "pos" for r in rows]
print("\n== threshold candidates (pos = AI examples; neg = all human sets) ==")
print(f"{'rule':<40}{'TPR':>7}{'FPR':>7}")
for d in (0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
    for p in (1, 2, 3, 4):
        rule = lambda r, d=d, p=p: r["density"] >= d and r["patterns"] >= p
        tpr = sum(rule(r) for r in pos) / len(pos)
        fpr = sum(rule(r) for r in neg) / len(neg) if neg else float("nan")
        print(f"{'density>=' + str(d) + ' and patterns>=' + str(p):<40}{tpr:>7.2f}{fpr:>7.2f}")

print("\n== per-block detail, human sets ==")
for k, rows in sets.items():
    if k == "pos":
        continue
    for r in rows:
        print(f"  {k:<10}{r['file']:<40}{r['words']:>6}w  {r['density']:>5.1f}/100  "
              f"{r['patterns']} pats {r['pattern_ids']}")
