#!/usr/bin/env python3
"""
split_claims.py — Extract checkable factual claims from a draft into one file
per claim, so each verification agent receives exactly one claim.

This is a SCAFFOLD splitter. It does sentence-level segmentation and a
heuristic first pass at flagging which sentences look like checkable factual
claims (contain a number, a year, a percentage, a named source, or an
attribution verb). It deliberately errs toward inclusion: a borderline
sentence is written out as a candidate claim rather than dropped, because a
human or a downstream agent discarding a non-claim is cheap, while a missed
claim is the failure this whole skill exists to prevent.

It does NOT decide truth, find sources, or judge argument. That is the
claim agents' job. This only segments and routes.

Usage:
    split_claims.py <draft-file> --out <dir>
    split_claims.py draft.md --out workspace/claims/

Accepts .md, .txt, or any UTF-8 plain text. For PDFs or decks, extract text
first and pass the text file.

Output: one file per candidate claim, named claim_001.txt ... claim_NNN.txt,
plus a manifest.json listing every claim with its source line number.
"""

import argparse
import json
import re
import sys
from pathlib import Path

# Markers that suggest a sentence asserts something checkable.
NUMERIC = re.compile(r"\b\d")                      # any digit
PERCENT = re.compile(r"\d\s?%|\bpercent\b", re.I)
YEAR = re.compile(r"\b(1[89]\d{2}|20\d{2})\b")
MONEY = re.compile(r"[$£€]\s?\d|\b\d+\s?(billion|million|trillion|thousand)\b", re.I)
ATTRIBUTION = re.compile(
    r"\b(according to|reported by|study|survey|report|found that|"
    r"data (from|shows)|research|analysis|census|bureau|institute|"
    r"published|cited|estimates?|figures?)\b",
    re.I,
)
# Sentences that are clearly framing/opinion, not checkable. Down-weight these.
OPINION = re.compile(
    r"\b(i think|i believe|in my view|arguably|should|might|could|"
    r"feels like|seems|the lesson|the point is|what matters)\b",
    re.I,
)


def split_sentences(text: str):
    """Lightweight sentence segmentation. Good enough for prose drafts.
    Keeps the source character offset so we can report line numbers."""
    # Normalize whitespace but keep paragraph breaks as sentence boundaries.
    chunks = re.split(r"(?<=[.!?])\s+|\n{2,}", text)
    sentences = []
    cursor = 0
    for chunk in chunks:
        s = chunk.strip()
        if not s:
            cursor += len(chunk) + 1
            continue
        line_no = text.count("\n", 0, text.find(s, cursor)) + 1 if s in text[cursor:] else text.count("\n", 0, cursor) + 1
        sentences.append((s, line_no))
        cursor += len(chunk) + 1
    return sentences


def looks_checkable(sentence: str) -> bool:
    """Heuristic: does this sentence assert something a source could confirm?
    Inclusive by design — a number, year, money figure, percentage, or an
    attribution phrase flags it. Pure-opinion sentences with no numbers and
    no attribution are excluded."""
    has_signal = any(
        p.search(sentence)
        for p in (NUMERIC, PERCENT, YEAR, MONEY, ATTRIBUTION)
    )
    if not has_signal:
        return False
    # If it's opinion-flavored AND has no hard number, drop it. If it has a
    # number, keep it even if opinion-flavored — "I think revenue hit $4M" is
    # still a checkable claim about $4M.
    if OPINION.search(sentence) and not (NUMERIC.search(sentence) or MONEY.search(sentence)):
        return False
    return True


def main():
    ap = argparse.ArgumentParser(description="Split a draft into one file per checkable claim.")
    ap.add_argument("draft", help="Path to draft (.md/.txt/plain text)")
    ap.add_argument("--out", required=True, help="Output directory for claim files")
    ap.add_argument("--all-sentences", action="store_true",
                    help="Write every sentence, not just heuristic claims "
                         "(use when you'd rather filter downstream)")
    args = ap.parse_args()

    src = Path(args.draft)
    if not src.exists():
        sys.exit(f"error: draft not found: {src}")

    text = src.read_text(encoding="utf-8", errors="replace")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    sentences = split_sentences(text)
    manifest = []
    n = 0
    for sent, line_no in sentences:
        keep = True if args.all_sentences else looks_checkable(sent)
        if not keep:
            continue
        n += 1
        fname = f"claim_{n:03d}.txt"
        (out / fname).write_text(sent + "\n", encoding="utf-8")
        manifest.append({"id": n, "file": fname, "line": line_no, "claim": sent})

    (out / "manifest.json").write_text(
        json.dumps({"source": str(src), "count": n, "claims": manifest}, indent=2),
        encoding="utf-8",
    )

    if n == 0:
        print("No checkable claims detected. If the draft has claims the "
              "heuristic missed, re-run with --all-sentences and filter "
              "downstream.", file=sys.stderr)
    else:
        print(f"Wrote {n} candidate claim(s) to {out}/")
        print(f"Manifest: {out}/manifest.json")
        print("Review the candidates before spawning agents — the splitter is "
              "inclusive on purpose, so drop any non-claims it caught.")


if __name__ == "__main__":
    main()
