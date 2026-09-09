#!/usr/bin/env python3
"""Extract the text an executor delivered to the user from its result.md.

usage: tests/evals/extract-delivered.py <result.md> [-o out.txt]

Executors write result.md as delivered-text plus commentary explaining the
changes. The commentary quotes the original, so scanning the whole file counts
the executor's *citations* of a pattern as *commissions* of it. In the
2026-09-08 run every grader had to neutralise that by hand, and one noted that a
grader trusting the raw scan would have passed an arm that removed half the
source's em dashes.

Two conventions, tried in order:

1. Explicit markers, `---BEGIN DELIVERED---` / `---END DELIVERED---`. Prefer these
   when you control the executor prompt. They are unambiguous.
2. The first two bare `---` fences. Kept for the runs already committed, but it is
   fragile: a `---` horizontal rule *inside* the answer closes the region early and
   silently truncates. That happened on the 2026-09-08-variance human-narrative
   e3-r2 arm, where the capture stopped before the interventions and the rewrite,
   and the arm's scan was measured over a fragment. When a file has more than two
   bare fences, this script now says so on stderr rather than truncating quietly.

Falls back to the whole file, and says so on stderr, when no region is found.
"""
import sys
from pathlib import Path

args = [a for a in sys.argv[1:] if a != "-o"]
if not args:
    sys.exit(__doc__)
src = Path(args[0])
out = Path(args[1]) if len(args) > 1 else None

lines = src.read_text(encoding="utf-8").splitlines()
begin = [i for i, l in enumerate(lines) if l.strip() == "---BEGIN DELIVERED---"]
end = [i for i, l in enumerate(lines) if l.strip() == "---END DELIVERED---"]
fences = [i for i, l in enumerate(lines) if l.strip() == "---"]

if begin and end and end[-1] > begin[0]:
    body = "\n".join(lines[begin[0] + 1:end[-1]]).strip()
elif len(fences) >= 2:
    body = "\n".join(lines[fences[0] + 1:fences[1]]).strip()
    if len(fences) > 2:
        print(f"{src.name}: {len(fences)} bare '---' fences, using the first two. "
              f"If the answer contains a horizontal rule this capture is truncated -- "
              f"check it, or re-run the executor with ---BEGIN/END DELIVERED--- markers.",
              file=sys.stderr)
else:
    body = "\n".join(lines).strip()
    print(f"{src.name}: no fenced delivered region; using whole file. "
          f"Scan results include commentary and are not evidence of committed patterns.",
          file=sys.stderr)

if out:
    out.write_text(body + "\n", encoding="utf-8")
else:
    print(body)
