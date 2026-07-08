#!/usr/bin/env python3
"""
init_workspace.py — Create the timestamped output tree for a source-check run.

Sets up the directory structure the skill writes into, copies the source draft
to input.md so the original is never touched, and prints the workspace path for
the orchestrator to use.

Usage:
    init_workspace.py <draft-file>
    init_workspace.py <draft-file> --base <dir>   # default: alongside the draft

Creates:
    <base>/source_check_<YYYYMMDD_HHMMSS>/
      ├── input.md        # copy of the source draft
      ├── claims/         # split_claims.py writes here
      ├── reports/        # per-agent JSON lands here
      └── (report, corrected, footnotes written by the consolidator)
"""

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description="Initialize a source-check workspace.")
    ap.add_argument("draft", help="Path to the source draft")
    ap.add_argument("--base", help="Where to create the workspace (default: draft's directory)")
    args = ap.parse_args()

    src = Path(args.draft)
    if not src.exists():
        sys.exit(f"error: draft not found: {src}")

    base = Path(args.base) if args.base else src.parent
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    ws = base / f"source_check_{stamp}"

    (ws / "claims").mkdir(parents=True, exist_ok=True)
    (ws / "reports").mkdir(parents=True, exist_ok=True)

    # Never touch the original. Work from a copy.
    shutil.copy2(src, ws / "input.md")

    print(str(ws))
    print(f"  input.md   <- copy of {src.name} (original untouched)", file=sys.stderr)
    print(f"  claims/    <- run split_claims.py --out {ws}/claims", file=sys.stderr)
    print(f"  reports/   <- per-claim agent JSON", file=sys.stderr)


if __name__ == "__main__":
    main()
