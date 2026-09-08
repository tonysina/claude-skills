#!/usr/bin/env python3
"""
Deterministic AI-tell scan for writing-skill output.

Checks text against humanizer's flag patterns and farnsworth-rhetoric's figure
budget. Built to validate that the writing skills in this repo do not contradict
each other -- farnsworth-rhetoric adds rhetorical figures, humanizer strips the
constructions those figures can degrade into, so farnsworth output must survive a
humanizer scan.

Usage:
    scripts/scan-ai-tells.py <target.txt> [target2.txt ...]
    scripts/scan-ai-tells.py --humanizer <path/to/SKILL.md> <target.txt> ...
    scripts/scan-ai-tells.py --keep-quotes <target.txt> ...

The humanizer path defaults to skills/humanizer/SKILL.md in this repo.

ALWAYS INCLUDE A POSITIVE CONTROL -- a text with known violations, scored first. On
this script's first run the control returned clean while missing three known
violations, which would have been reported as a pass for every file in the run. A
scan that reports no findings on everything is indistinguishable from a broken scan.

Meta-quotation filter (default on, disable with --keep-quotes):
  Text that *discusses* a pattern is not text that *uses* it. Before scanning, the
  script removes fenced code, inline code, Markdown blockquotes, humanizer's own
  '**... to watch:**' flag lines, short double-quoted strings, and short
  single-asterisk italic spans (the use/mention convention). Without this,
  scanning humanizer's SKILL.md against itself reported 13 hits, 12 of which were
  the skill quoting a pattern in order to explain it. Known-good answer for that
  file under v1.2.0 is 1 (a real "Studies have shown" self-violation, fixed in
  v1.3.0, after which the answer is 0).

Two flag sources:

  1. AUTO-EXTRACTED from humanizer/SKILL.md '**... to watch:**' lines. These are
     literal word/phrase lists, so they can be matched directly. Extracting them
     live means the scan cannot drift out of sync when humanizer is revised. Each
     flag is tagged with the stable pattern ID of the '### N. ID -- ...' heading
     it sits under, so the report can count distinct patterns hit.

  2. HAND-DERIVED construction cores (CONSTRUCTIONS below). humanizer states some
     patterns as templates with X/Y/Z placeholders (NEG-PARALLEL) or as
     open-ended categories (GENERIC-CLOSER). Placeholders cannot be
     literal-matched, so the invariant core of each template is encoded here as
     a regex. These need updating by hand if humanizer's pattern set changes.
     Labels use humanizer's stable pattern IDs, not display numbers.

Also measures:
  - em dash total and max-per-paragraph (EM-DASH is about proximity, not count)
  - anaphora runs at sentence and clause level, ignoring leading conjunctions
  - word-level and phrase-level triads (isocolon load-bearing test / RULE-OF-3)
  - word count vs farnsworth figure budget
  - flag density per 100 words and distinct patterns hit, which is what
    humanizer's threshold table is calibrated on

Known limits (need the LLM grader, not this script):
  - GENERIC-CLOSER is an open category; only listed literals hit.
  - Antithesis and hypophora are not reliably detectable by regex, so the figure
    count here is a floor, not a total.
  - Claim drift (a hedge becoming a promise, a dropped qualifier) is not checkable
    here at all. That is farnsworth-rhetoric's claim check, and it needs a grader.
"""

import re
import sys
from pathlib import Path

WATCH_HEADERS = (
    "Words to watch:",
    "Key words:",
    "Patterns to watch:",
    "Phrases to watch:",
    "Authority trope phrases:",
    "Notability phrases:",
)

# Hand-derived. Invariant cores of humanizer's placeholder templates.
GAP = r".{1,60}?"
CONSTRUCTIONS = [
    ("NEG-PARALLEL", r"\bit'?s not just\b"),
    ("NEG-PARALLEL", r"\bnot just\b" + GAP + r"\b(?:it'?s|we|they|but)\b"),
    ("NEG-PARALLEL", r"\bnot only\b" + GAP + r"\bbut\b"),
    ("NEG-PARALLEL", r"\bmore than just\b"),
    ("NEG-PARALLEL", r"\bisn'?t just\b"),
    ("NEG-PARALLEL", r"\bit'?s not about\b" + GAP + r"\bit'?s\b"),
    ("NEG-PARALLEL tailing negation", r",\s*no\s+\w+\.\s*$|,\s*no\s+\w+\s*$"),
    ("GENERIC-CLOSER", r"\bwe will lead\b|\bthe future is bright\b"),
]

LEADING_STOPWORDS = {
    "but", "and", "or", "so", "yet", "for", "nor", "then", "thus",
    "the", "a", "an",
}

# '### 3. AI-VOCAB -- AI vocabulary words'  ->  ('3', 'AI-VOCAB')
# Falls back to the number alone for a pre-ID humanizer file.
HEADING_RE = re.compile(r"^###\s+(\d+)\.\s+(?:([A-Z][A-Z0-9-]+)\s+--\s+)?")


def expand_slashes(phrase):
    """'stands/serves as' -> ['stands as', 'serves as']; leaves plain text alone."""
    if "/" not in phrase:
        return [phrase]
    tokens = phrase.split()
    out = [""]
    for tok in tokens:
        if "/" in tok:
            alts = [a for a in tok.split("/") if a]
            out = [f"{o} {a}".strip() for o in out for a in alts]
        else:
            out = [f"{o} {tok}".strip() for o in out]
    return out


def load_flags(humanizer_path):
    """Pull literal flag phrases out of humanizer's '**... to watch:**' lines.

    Returns {flag_lowercase: pattern_id}. Entries containing X/Y/Z placeholders
    are skipped here and handled by CONSTRUCTIONS instead.
    """
    text = Path(humanizer_path).read_text(encoding="utf-8")
    raw = []
    current = "?"
    for line in text.splitlines():
        stripped = line.strip()
        h = HEADING_RE.match(stripped)
        if h:
            current = h.group(2) or f"#{h.group(1)}"
            continue
        if not stripped.startswith("**"):
            continue
        for header in WATCH_HEADERS:
            if header in stripped:
                payload = stripped.split(header, 1)[1].replace("**", "").strip()
                # split on both comma and slash-with-spaces (two conventions in use)
                for chunk in re.split(r",|\s/\s", payload):
                    raw.append((chunk, current))
                break

    flags = {}
    for item, pid in raw:
        item = item.strip().strip('"').strip("'")
        item = item.replace("...", " ").replace("…", " ")
        item = re.sub(r"\[.*?\]", " ", item)
        item = re.sub(r"\(.*?\)", " ", item)
        item = re.sub(r"\s+", " ", item).strip(" .\"'")
        if len(item) < 3:
            continue
        # placeholder templates are handled by CONSTRUCTIONS
        if re.search(r"\b[XYZ]\b", item):
            continue
        for variant in expand_slashes(item):
            variant = variant.strip()
            if len(variant) >= 3:
                flags.setdefault(variant.lower(), pid)
    return flags


def strip_quoted(text):
    """Remove text that quotes or displays a pattern rather than using it.

    Order matters: fenced code first (it may contain quotes and blockquotes),
    then whole lines (blockquotes, flag lists), then inline spans.
    """
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    kept = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith(">"):
            continue
        if s.startswith("**") and any(h in s for h in WATCH_HEADERS):
            continue
        kept.append(line)
    text = "\n".join(kept)
    text = re.sub(r"`[^`\n]*`", " ", text)
    # short quoted strings only; a 200+ char quote is a passage, not a mention
    text = re.sub(r"\"[^\"\n]{1,200}\"", " ", text)
    text = re.sub(r"“[^”\n]{1,200}”", " ", text)
    # single-asterisk italics on a word or short phrase is the use/mention
    # convention (*delve*, *in order to*); bold (**...**) is left alone
    text = re.sub(r"(?<!\*)\*(?!\*)[^*\n]{1,40}\*(?!\*)", " ", text)
    return text


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p.strip() for p in parts if p.strip()]


def clauses(text):
    parts = re.split(r"[,;:]|(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if p.strip()]


def anaphora_key(unit, n=2):
    """First n meaningful words, skipping leading conjunctions and articles.

    Without the skip, 'But if we commit / if we collaborate / if we follow through'
    reads as a run of 2 instead of 3.
    """
    words = re.findall(r"[A-Za-z']+", unit.lower())
    while words and words[0] in LEADING_STOPWORDS:
        words.pop(0)
    return " ".join(words[:n]) if len(words) >= n else None


def find_anaphora(units, min_run=2):
    """Runs of >=min_run consecutive units sharing their anaphora key."""
    runs, current, prev_key = [], [], None
    for unit in units:
        key = anaphora_key(unit)
        if key and key == prev_key:
            current.append(unit)
        else:
            if len(current) >= min_run:
                runs.append((prev_key, list(current)))
            current = [unit] if key else []
        prev_key = key
    if len(current) >= min_run:
        runs.append((prev_key, list(current)))
    return runs


def find_word_triads(text):
    pat = re.compile(
        r"\b([A-Za-z][\w'-]*),\s+([A-Za-z][\w'-]*),\s+(?:and\s+|or\s+)?([A-Za-z][\w'-]*)\b"
    )
    return [m.group(0) for m in pat.finditer(text)]


def find_phrase_triads(text):
    """Three comma-separated segments of 2-6 words sharing a first word."""
    found = []
    for sentence in sentences(text):
        segs = [s.strip() for s in sentence.split(",") if s.strip()]
        run, prev = [], None
        for seg in segs:
            words = re.findall(r"[A-Za-z']+", seg.lower())
            head = words[0] if words else None
            if head and head == prev and 2 <= len(words) <= 6:
                run.append(seg)
            else:
                if len(run) >= 3:
                    found.append(", ".join(run))
                run = [seg] if head and 2 <= len(words) <= 6 else []
            prev = head
        if len(run) >= 3:
            found.append(", ".join(run))
    return found


def budget_for(wordcount):
    if wordcount > 600:
        return min(6, max(1, wordcount // 150)), ">600 words: 1 per 150, cap 6"
    if wordcount >= 300:
        return 3, "300-600 words: 3"
    return 1, "<300 words: 1"


def scan(path, flags, keep_quotes=False, quiet=False):
    raw_text = Path(path).read_text(encoding="utf-8")
    text = raw_text if keep_quotes else strip_quoted(raw_text)
    # Curly apostrophes defeat the it's/isn't regexes. Wikipedia's confirmed-AI
    # examples use them throughout, so without this the constructions check
    # fired on 2 of 84 known-positive blocks.
    text = text.replace("’", "'")
    stripped_words = (len(re.findall(r"[A-Za-z'-]+", raw_text))
                      - len(re.findall(r"[A-Za-z'-]+", text)))
    lower = text.lower()
    wc = len(re.findall(r"[A-Za-z'-]+", text))

    tier_a, tier_b = [], []
    patterns_hit = set()
    for flag, pid in flags.items():
        multiword = " " in flag
        # Word-boundary both ends regardless of length. Without the leading \b,
        # the flag "here is a" matches inside "There is also".
        pattern = re.escape(flag)
        if flag[:1].isalnum():
            pattern = r"\b" + pattern
        if flag[-1:].isalnum():
            pattern = pattern + r"\b"
        hits = len(re.findall(pattern, lower))
        if hits:
            (tier_a if multiword else tier_b).append((flag, hits, pid))
            patterns_hit.add(pid)

    constructions = []
    for label, pattern in CONSTRUCTIONS:
        for m in re.finditer(pattern, lower, re.MULTILINE):
            snippet = re.sub(r"\s+", " ", m.group(0))[:70]
            constructions.append((label, snippet))
            patterns_hit.add(label.split()[0])

    paragraphs = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    dash_total = text.count("—")
    dash_max_para = max((p.count("—") for p in paragraphs), default=0)
    if dash_max_para >= 3:
        patterns_hit.add("EM-DASH")

    sent_runs = find_anaphora(sentences(text))
    clause_runs = find_anaphora(clauses(text))
    strong = [r for r in sent_runs + clause_runs if len(r[1]) >= 3]
    weak = [r for r in sent_runs + clause_runs if len(r[1]) == 2]

    word_triads = find_word_triads(text)
    phrase_triads = find_phrase_triads(text)
    budget, rule = budget_for(wc)

    total_hits = (sum(n for _, n, _ in tier_a) + sum(n for _, n, _ in tier_b)
                  + len(constructions))
    density = (100.0 * total_hits / wc) if wc else 0.0

    verdict_flags = (
        len(constructions)
        + (1 if dash_max_para >= 3 else 0)
        + (max(0, len(strong) - 1))
        + (len(strong) if wc < 300 else 0)
    )

    row = {
        "file": Path(path).name,
        "words": wc,
        "budget": budget,
        "cons": len(constructions),
        "tier_a": sum(n for _, n, _ in tier_a),
        "tier_b": sum(n for _, n, _ in tier_b),
        "dash": dash_max_para,
        "strong": len(strong),
        "weak": len(weak),
        "triads": len(word_triads) + len(phrase_triads),
        "violations": verdict_flags,
        "density": density,
        "patterns": len(patterns_hit),
        "pattern_ids": sorted(patterns_hit),
    }
    if quiet:
        return row

    print(f"\n{'=' * 70}")
    print(f"FILE: {Path(path).name}")
    print(f"{'=' * 70}")
    print(f"  words: {wc}   figure budget: {budget}   ({rule})")
    if not keep_quotes and stripped_words:
        print(f"  meta-quotation filter removed {stripped_words} words "
              f"(code, blockquotes, flag lists, short quoted strings)")

    print(f"\n  [CONSTRUCTIONS] forbidden-table violations: {len(constructions)}")
    for label, snippet in constructions:
        print(f"        FLAG {label}: \"{snippet}\"")
    if not constructions:
        print("        none")

    print(f"\n  [A] humanizer multi-word flags: {len(tier_a)} distinct")
    for flag, n, pid in sorted(tier_a, key=lambda x: -x[1]):
        print(f"        x{n}  \"{flag}\"  [{pid}]")
    if not tier_a:
        print("        none")

    print(f"\n  [B] humanizer single-word flags (needs context): {len(tier_b)} distinct")
    for flag, n, pid in sorted(tier_b, key=lambda x: -x[1]):
        print(f"        x{n}  {flag}  [{pid}]")
    if not tier_b:
        print("        none")

    print(f"\n  em dashes: {dash_total} total, max {dash_max_para} per paragraph")
    if dash_max_para >= 3:
        print("        FLAG humanizer EM-DASH (3+ in proximity)")

    print(f"\n  anaphora: {len(strong)} strong run(s) (>=3), {len(weak)} weak (2)")
    for key, run in strong:
        print(f"        STRONG \"{key}...\" x{len(run)}")
    for key, run in weak:
        print(f"        weak   \"{key}...\" x{len(run)}")
    if len(strong) > 1:
        print(f"        FLAG farnsworth cap: 1 run/piece, found {len(strong)}")
    if strong and wc < 300:
        print("        FLAG farnsworth: no anaphora under 300 words")

    print(f"\n  triads: {len(word_triads)} word-level, {len(phrase_triads)} phrase-level")
    for t in word_triads + phrase_triads:
        print(f"        {t[:70]}")
    if word_triads or phrase_triads:
        print("        -> run isocolon load-bearing test on each")

    print(f"\n  density: {total_hits} flag hits / {wc} words = {density:.1f} per 100"
          f"   distinct patterns: {len(patterns_hit)} {row['pattern_ids']}")
    print(f"\n  HARD VIOLATIONS: {verdict_flags}")
    return row


DEFAULT_HUMANIZER = (
    Path(__file__).resolve().parent.parent / "skills" / "humanizer" / "SKILL.md"
)


def main():
    args = sys.argv[1:]
    humanizer = DEFAULT_HUMANIZER
    keep_quotes = False

    while args and args[0].startswith("--"):
        if args[0] == "--humanizer":
            if len(args) < 2:
                print("--humanizer requires a path\n")
                print(__doc__)
                sys.exit(1)
            humanizer = Path(args[1])
            args = args[2:]
        elif args[0] == "--keep-quotes":
            keep_quotes = True
            args = args[1:]
        else:
            print(f"unknown option {args[0]}\n")
            print(__doc__)
            sys.exit(1)

    if not args:
        print(__doc__)
        sys.exit(1)

    if not humanizer.exists():
        print(f"humanizer SKILL.md not found: {humanizer}")
        print("Pass an explicit path with --humanizer <path>")
        sys.exit(1)

    missing = [p for p in args if not Path(p).exists()]
    if missing:
        for p in missing:
            print(f"target not found: {p}")
        sys.exit(1)

    flags = load_flags(humanizer)
    print(f"Loaded {len(flags)} literal flags from {humanizer.name} "
          f"+ {len(CONSTRUCTIONS)} hand-derived constructions"
          f"{'  (quotes kept)' if keep_quotes else ''}")
    rows = [scan(p, flags, keep_quotes=keep_quotes) for p in args]

    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    hdr = (f"{'file':<28}{'wds':>5}{'bud':>4}{'CONS':>6}{'A':>4}{'B':>4}"
           f"{'dash':>5}{'anaph':>6}{'tri':>4}{'/100':>6}{'pat':>4}{'VIOL':>6}")
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        print(f"{r['file']:<28}{r['words']:>5}{r['budget']:>4}{r['cons']:>6}"
              f"{r['tier_a']:>4}{r['tier_b']:>4}{r['dash']:>5}"
              f"{str(r['strong']) + '/' + str(r['weak']):>6}{r['triads']:>4}"
              f"{r['density']:>6.1f}{r['patterns']:>4}{r['violations']:>6}")


if __name__ == "__main__":
    main()
