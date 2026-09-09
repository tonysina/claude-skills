#!/usr/bin/env python3
"""Extract the text an executor delivered to the user from its result.md.

usage: tests/evals/extract-delivered.py <result.md> [-o out.txt]

Executors write result.md as delivered-text plus commentary explaining the
changes. The commentary quotes the original, so scanning the whole file counts
the executor's *citations* of a pattern as *commissions* of it. In the
2026-09-08 run every grader had to neutralise that by hand, and one noted that a
grader trusting the raw scan would have passed an arm that removed half the
source's em dashes.

Convention: the delivered text sits between the first two `---` fences. Falls
back to the whole file, and says so on stderr, when no fenced region is found.
"""
import sys
from pathlib import Path

args = [a for a in sys.argv[1:] if a != "-o"]
if not args:
    sys.exit(__doc__)
src = Path(args[0])
out = Path(args[1]) if len(args) > 1 else None

lines = src.read_text(encoding="utf-8").splitlines()
fences = [i for i, l in enumerate(lines) if l.strip() == "---"]

if len(fences) >= 2:
    body = "\n".join(lines[fences[0] + 1:fences[1]]).strip()
else:
    body = "\n".join(lines).strip()
    print(f"{src.name}: no fenced delivered region; using whole file. "
          f"Scan results include commentary and are not evidence of committed patterns.",
          file=sys.stderr)

if out:
    out.write_text(body + "\n", encoding="utf-8")
else:
    print(body)
