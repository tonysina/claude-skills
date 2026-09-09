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
    scripts/scan-ai-tells.py --keep-summary <target.txt> ...

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

Pattern-ID commentary filter (default on, disable with --keep-summary):
  A change summary names the patterns it removed and quotes the text it removed
  them from, so a raw scan counts a citation as a commission. This runs in BOTH
  modes, because the problem is not quoting: the citations sit in ordinary prose
  bullets, and --keep-quotes is what the eval README requires for delivered text
  (executors put rewritten prose in blockquotes), which switches quote filtering
  off exactly when a change summary is present.

  Keyed on humanizer's pattern IDs, not on a heading name -- executors invent the
  heading ('Change summary', '## What changed', '**Change note**', '## What I
  deliberately did not change' all appear across tests/evals/runs/). A block
  naming an all-caps pattern ID is commentary by construction; delivered prose
  does not cite pattern IDs. Case-sensitive, so 'inflation' the word is safe.

  Known-good answer: runs/2026-09-02-r3/humanizer/e1-with delivered text scores 0
  NEG-PARALLEL. Before this filter it scored 3, all three inside the one
  '- `NEG-PARALLEL`: "It's not just a form to fill out..."' bullet, and every
  grader in that run had to neutralise the number by hand.

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
  - forward references (FORWARD-REF), human-narrative cluster E: structural
    announcements pointing the reader to somewhere else in the artifact. Reported
    and counted SEPARATELY from humanizer's constructions, density and distinct-
    pattern count, all of which are calibrated on humanizer's own pattern set --
    folding a second skill's finding into them would move a calibrated number,
    and would break comparison with every scan.txt already committed under
    tests/evals/runs/. humanizer SIGNPOSTING covers the lexical forms and is
    auto-extracted; these are the structural ones it misses. Patterns derive from
    phrases graders caught by hand while the scan reported 0 flags:
    runs/2026-09-02-r2 human-narrative e3-prev ("Here's the full audit, then the
    rewrite", "F is the reason -- see the end") and e3-with ("reasons at the
    bottom", "for the reason below"), plus human-narrative 1.0.0's own
    SIGNPOSTING collision ("you'll understand why this matters in a moment").
  - word count vs farnsworth figure budget
  - flag density per 100 words and distinct patterns hit, which is what
    humanizer's threshold table is calibrated on

Known limits (need the LLM grader, not this script):
  - GENERIC-CLOSER is an open category; only listed literals hit.
  - Antithesis and hypophora are not reliably detectable by regex, so the figure
    count here is a floor, not a total.
  - Claim drift (a hedge becoming a promise, a dropped qualifier) is not checkable
    here at all. That is farnsworth-rhetoric's claim check, and it needs a grader.
  - FORWARD-REF catches phrasings, not the structure itself. An announcement made
    without a deictic word ("The audit comes first. The rewrite is separate.")
    passes. A clean FORWARD-REF count is not evidence against the tell, the same
    caveat UNDER-PUNCT carries; human-narrative's other 29 features are not
    checked here at all and need the LLM grader.
  - The pattern-ID filter is a whole-block drop, so a change summary that also
    contains delivered prose loses that prose from the scan. Extract the
    delivered text first, per tests/evals/README.md, and this does not arise.
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

# human-narrative cluster E. Kept OUT of CONSTRUCTIONS on purpose: humanizer's
# density table and its distinct-pattern count are calibrated on humanizer's own
# pattern set, so folding a second skill's finding into either would move a
# calibrated number. Counted and reported separately; see FORWARD-REF in the
# docstring.
#
# humanizer's SIGNPOSTING watch list already covers the lexical forms ("here's
# what you need to know," "you might be wondering") and is auto-extracted. These
# are the structural forms it misses -- a deictic pointer to somewhere else in
# the artifact. Every pattern below is derived from a phrase a grader caught by
# hand while the scan reported 0, cited by run in the docstring.
FORWARD_REF = [
    # "reasons at the bottom", "for the reason below", "details further down"
    (r"\b(?:reasons?|details?|caveats?|notes?|context|rationale|the rest|more)\b"
     r"[^.\n]{0,30}?\b(?:below|at the bottom|at the end|further down)\b"),
    # "F is the reason -- see the end". Bare "see below" is deliberately absent:
    # in a document with sections it is an ordinary editorial cross-reference,
    # which is how the 2026-09-02 grader ruled on '(see "Not taken")', and it
    # fires on good-presentations/SKILL.md's own option table. No evidenced
    # positive needs it -- "reason below" is caught by the pointer pattern above.
    r"\bsee\s+(?:the end|the bottom|further down)\b",
    # "Here's the full audit, then the rewrite."
    r"\bhere'?s\s+(?:the|what|why|how|my)\b[^.\n]{0,60}?,\s*then\b",
    # "as we'll see", "in what follows", "by the end of this piece"
    r"\bas\s+(?:we|you)'?(?:ll|d)\s+see\b",
    r"\bin what follows\b",
    r"\bwhat follows (?:is|are)\b",
    r"\bby the end of this\b",
    # "more on this below", "I'll come back to that later"
    r"\bmore on (?:this|that|it)\b[^.\n]{0,20}?"
    r"\b(?:below|later|in a (?:moment|second|bit|minute))\b",
    (r"\b(?:i|we)'?(?:ll| will)\s+"
     r"(?:explain|unpack|get to|come back to|return to|cover|walk through)\b"
     r"[^.\n]{0,25}?\b(?:below|later|shortly|in a (?:moment|second|bit|minute))\b"),
    # "first I'll audit, then I'll rewrite"
    r"\bfirst\b[^.\n]{0,40}?,\s*then (?:i|we)'?(?:ll| will)\b",
    # "you'll understand why this matters in a moment" -- 1.0.0's own defect
    r"\byou'?ll (?:understand|see) why\b[^.\n]{0,40}?\bin a (?:moment|second|bit)\b",
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


def load_pattern_ids(humanizer_path):
    """Every stable pattern ID in humanizer's '### N. ID -- ...' headings.

    Read live for the same reason the flag lists are: an ID added, renamed or
    retired in humanizer needs no change here.
    """
    text = Path(humanizer_path).read_text(encoding="utf-8")
    ids = set()
    for line in text.splitlines():
        h = HEADING_RE.match(line.strip())
        if h and h.group(2):
            ids.add(h.group(2))
    return ids


ID_TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\b|\b[A-Z]{4,}\b")
QUOTED_SPAN_RE = re.compile(
    r"\"[^\"\n]{3,}\"|\u201c[^\u201d\n]{3,}\u201d"
    r"|(?<!\*)\*(?!\*)[^*\n]{2,40}\*(?!\*)"
)
LIST_MARKER_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)?")
LIST_ITEM_RE = re.compile(r"^\s*(?:[-*+]\s|\d+[.)]\s|#{1,6}\s|>)")
CITATION_HEAD = 60


def cites_pattern(line, ids):
    """True when a line labels a quotation with a humanizer pattern ID.

    Both halves are needed, and the label has to come first. A change-summary
    bullet names the pattern and then quotes the text it was removed from:

        - `NEG-PARALLEL`: "It's not just a form to fill out; it's ..."
        **Negative parallelism (`NEG-PARALLEL`).** "rapidly evolving ..."

    humanizer's own prose also names IDs, but as a cross-reference at the end of
    a sentence about something else ("... is already listed under `AI-VOCAB`",
    "See `UNDER-PUNCT` and farnsworth-rhetoric/references/figures.md"). Requiring
    the ID inside the first CITATION_HEAD characters, past any list marker, and a
    quoted span somewhere in the line, separates the two: across humanizer's
    SKILL.md this drops nothing, and across tests/evals/runs/ it catches 44 of the
    51 lines that pair an ID with a quotation.

    The 7 it does not catch put the ID after the quotation. They are commentary,
    but they quote no construction the scan matches, so they cost nothing today --
    a looser rule that caught them also swallowed 50 lines of humanizer's own
    prose, which would have gutted the self-check CONTRIBUTING.md documents.
    """
    body = LIST_MARKER_RE.sub("", line, count=1)
    if not (ids & set(ID_TOKEN_RE.findall(body[:CITATION_HEAD]))):
        return False
    return bool(QUOTED_SPAN_RE.search(body))


def strip_pattern_commentary(text, pattern_ids):
    """Drop blocks that label a quotation with a humanizer pattern ID.

    A change summary cites the patterns it removed and quotes the text it removed
    them from, so a raw scan counts the citation as a commission. Blockquote and
    short-quote filtering does not catch it: the citations sit in ordinary prose
    bullets, and --keep-quotes -- which tests/evals/README.md requires for
    delivered text, because executors put rewritten prose in blockquotes --
    switches that filtering off exactly when a change summary is present.

    Keyed on the pattern IDs rather than on a heading name because executors
    invent the heading: 'Change summary', '## What changed', '**Change note**',
    '**What I changed and why**' and '## What I deliberately did not change' all
    appear across tests/evals/runs/. The IDs are the invariant, and they arrive
    live from humanizer's own headings, so this cannot drift when the pattern set
    is revised.

    Matching is case-sensitive on an all-caps token: 'INFLATION' is a citation,
    'inflation' is a word. A bullet's continuation lines go with it, since a
    wrapped bullet holds the rest of the quotation.
    """
    if not pattern_ids:
        return text
    ids = set(pattern_ids)
    kept, dropping = [], False
    for line in text.splitlines():
        if not line.strip():
            dropping = False
            kept.append(line)
            continue
        if cites_pattern(line, ids):
            dropping = True
            continue
        # continuation of a dropped bullet: no new marker of its own
        if dropping and not LIST_ITEM_RE.match(line):
            continue
        dropping = False
        kept.append(line)
    return "\n".join(kept)


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


def scan(path, flags, keep_quotes=False, keep_summary=False, quiet=False,
         pattern_ids=()):
    raw_text = Path(path).read_text(encoding="utf-8")
    # Commentary filter runs FIRST and in both modes. It has to see the raw text:
    # executors write the IDs as `NEG-PARALLEL`, and strip_quoted removes inline
    # code spans, so running it second leaves it nothing to key on in default
    # mode. Change-summary citation is a separate problem from blockquoting, and
    # --keep-quotes -- required for delivered text -- switches quoting off anyway.
    text = raw_text
    if not keep_summary:
        text = strip_pattern_commentary(text, pattern_ids)
    if not keep_quotes:
        text = strip_quoted(text)
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

    # Separate from constructions: not a humanizer pattern, so it stays out of
    # patterns_hit, total_hits, density and the violation count, all of which are
    # calibrated on humanizer's set.
    forward_refs = []
    for pattern in FORWARD_REF:
        for m in re.finditer(pattern, lower):
            forward_refs.append(re.sub(r"\s+", " ", m.group(0))[:70])

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
        "fwd": len(forward_refs),
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

    print(f"\n  forward references (human-narrative cluster E): {len(forward_refs)}")
    for snippet in forward_refs:
        print(f"        FLAG FORWARD-REF: \"{snippet}\"")
    if not forward_refs:
        print("        none")

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
    keep_summary = False

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
        elif args[0] == "--keep-summary":
            keep_summary = True
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
    pattern_ids = load_pattern_ids(humanizer)
    notes = []
    if keep_quotes:
        notes.append("quotes kept")
    if keep_summary:
        notes.append("pattern-ID commentary kept")
    print(f"Loaded {len(flags)} literal flags from {humanizer.name} "
          f"+ {len(CONSTRUCTIONS)} hand-derived constructions "
          f"+ {len(FORWARD_REF)} forward-reference patterns"
          f"{'  (' + ', '.join(notes) + ')' if notes else ''}")
    rows = [scan(p, flags, keep_quotes=keep_quotes, keep_summary=keep_summary,
                 pattern_ids=pattern_ids) for p in args]

    print(f"\n{'=' * 70}")
    print("SUMMARY")
    print(f"{'=' * 70}")
    hdr = (f"{'file':<28}{'wds':>5}{'bud':>4}{'CONS':>6}{'A':>4}{'B':>4}"
           f"{'dash':>5}{'anaph':>6}{'tri':>4}{'fwd':>4}{'/100':>6}{'pat':>4}"
           f"{'VIOL':>6}")
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        print(f"{r['file']:<28}{r['words']:>5}{r['budget']:>4}{r['cons']:>6}"
              f"{r['tier_a']:>4}{r['tier_b']:>4}{r['dash']:>5}"
              f"{str(r['strong']) + '/' + str(r['weak']):>6}{r['triads']:>4}"
              f"{r['fwd']:>4}{r['density']:>6.1f}{r['patterns']:>4}"
              f"{r['violations']:>6}")


if __name__ == "__main__":
    main()
