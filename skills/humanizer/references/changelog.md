# Changelog

## [1.3.1] - 2026-09-02

Patches from the first clean-context eval (`tests/evals/runs/2026-09-02/REPORT.md`). No
pattern content or watch-list changes; the calibration in 1.3.0 still applies.

### Fixed

- **Residue does not prove authorship.** The eval's residue run wrote "sources Gemini was
  reading when it drafted the paragraph." The rule that residue proves a chatbot touched
  the citation, not that it wrote the prose, was only in `extended-patterns.md`. Now in
  SKILL.md under "What residue proves," with two additions the executors volunteered on
  their own: name the model the marker belongs to, and warn the user when stripped markers
  were the text's only sourcing.
- **"Humanize this" on clean text.** The executor asked whether returning the paragraph
  unchanged was acceptable for an explicit rewrite request; the answer was inferable from
  three sections and stated in none. "Full rewrite" now says: clean scan, return unchanged,
  say so. Also states that "Edit with constraints" wins when a constraint co-occurs.
- **`VAGUE-ATTRIB` with no source to name.** The fix said "name a source"; the eval's
  rewrite kept the unsourced claim with a note underneath because none existed. Added the
  fallback: delete it, or mark it inline. Swapping it for an unsourced specific-sounding
  claim is named as the wrong move.

### Added

- **Review-and-flag opens with a verdict.** Both eval arms invented a verdict line because
  the use case did not ask for one. Now it does, with confidence stated. Also states that
  a one-clause fix per finding is fine and a rewritten paragraph is not, which is the line
  the no-skill baseline crossed.
- **`INFLATION` non-exhaustiveness note.** The eval's rewrite caught "seamless," which is
  not on the list. The note says unlisted promotional adjectives count when they cluster
  with listed ones, and that the scan cannot see them. Kept as prose rather than watch-list
  entries so the calibrated lists stay source-faithful and the scan's flag set unchanged.

## [1.3.0] - 2026-09-02

Gave the patterns stable IDs, measured the finding threshold instead of arguing it, closed
five gaps against the source, and repaired three defects the skill had shipped with. The
pattern catalog in 1.2.0 was sound and tracked its source more faithfully than the other
two writing skills tracked theirs; what was missing was a handle other skills could
reference without breaking, and a number that says when a hit is a finding.

### Fixed

- **Self-violation.** `AI-VOCAB` said, in the skill's own voice, "Studies have shown these
  words appear far more frequently…" while `VAGUE-ATTRIB` flags "studies have shown
  (without citation)." The source has the citations; the skill had dropped them and kept
  the construction it tells you to delete. Restored: Juzek and Ward (ACL Findings 2025),
  Kobak et al. (*Science Advances* 2025), Geng and Trotta (ACL Findings 2025). Scanning
  the skill's own prose with `scripts/scan-ai-tells.py` now returns 0 hits; under 1.2.0 it
  returned 1, this one.
- **Wrong boundary year.** 1.2.0 said "post-2023 vs pre-2023." The source says after 2022,
  when LLM chatbots became widely accessible (ChatGPT launched November 2022). Fixed.
- **Copula citation undersold.** 1.2.0 said "one study documented a 10%+ decrease in 'is'
  and 'are' usage in academic writing after 2023." The source (Geng and Trotta, arXiv
  2404.08627) says *during* 2023 with no major change before, and adds the stronger
  result: prompting GPT-3.5 to "revise the following sentence" over 10,000 abstracts
  reproduced the drop. Both now stated. Huang et al. (2026) added for the Wikipedia
  replication.
- **Stale internal cross-reference.** `references/extended-patterns.md` pointed didactic
  disclaimers and section summaries at "pattern 13," which was Fragmented headers. They
  were #14. A pattern had been inserted at some point and the reference file never
  updated. Now references `DIDACTIC` by ID, which cannot go stale the same way.
- **`RULE-OF-3` contradicted its own example.** The pattern said "LLMs overuse groups of
  three" and its corrected output was a triad. The edit was right (it removed the
  decorative triad and kept the one carrying three distinct facts) but the skill never
  said why. Added the load-bearing test, stated as the same test `farnsworth-rhetoric`
  v1.1.0 applies to isocolon, so the two skills now agree on which triads survive from
  both sides. This closes the asymmetry noted in farnsworth's 1.1.0 changelog.
- **Two "filler" flags contradicted the source.** `DIDACTIC` listed "in order to" and "due
  to the fact that" as AI filler. The source's "Signs of human writing" section lists "in
  order to" and "the fact that" as constructions *more common in human text than AI*.
  Removed, with a note in the pattern saying why, and the human-signs list added to
  `extended-patterns.md`.
- **Stale "ineffective indicators" list.** 1.2.0 listed "letter-like writing with
  salutations," which is no longer on the source's list. Replaced with the current list:
  adds mixed casual/formal register, transition words in isolation, unsourced content, and
  correct complex markup.

### Added

- **Stable pattern IDs** (`INFLATION`, `NEG-PARALLEL`, `SIGNPOSTING`, …) with display
  numbers kept for reading order. The ordinal numbers had about 28 external references
  across `farnsworth-rhetoric`, `human-narrative`, and `scripts/scan-ai-tells.py`, and
  inserting a pattern broke all of them silently (see the #13/#14 defect above). All
  external references now use IDs. The quick-reference table at the top of SKILL.md is the
  ID registry.
- **"When a flag is a finding" threshold table.** Density (watch-list hits per 100 words)
  and spread (distinct patterns hit). Under 1 per 100 and 0-1 patterns: within human
  range. 1-2 per 100 or 2 patterns: ambiguous, flag. 2+ per 100 or 3+ patterns: rewrite.
  Constructions and markup residue are findings at any density. See Calibration below.
- **`VAGUE-CONNECT`** (source §"Vague expression of connection or association"): "in
  connection with," "associated with," and kin, used to abstract a relation away instead
  of naming it. New pattern, display #6, in Pass 2.
- **`STYLE-SHIFT`** (source §"Pronounced shift in writing style"): the mixed-authorship
  signal, including English-variety mismatch. New pattern, display #20, in a new Pass 4
  that also holds the voice check, which 1.2.0 called "Pass 4" in the how-to list without
  a section to match.
- **"X rather than Y"** added to `NEG-PARALLEL` as the third named variant (source §3.4;
  particularly common in Grok output).
- **Model-specific residue** in `extended-patterns.md`: Gemini (`[cite: N]`,
  `[span_N](start_span)`), DeepSeek (lenticular brackets with daggers), Perplexity
  (`[attached_file:1]`, `ppl-ai-file-upload`), Grok (`grok_render_citation_card_json`,
  `referrer=grok.com`), Copilot (`utm_source=copilot.com`), and the unattributed
  `:::writing{variant="document"}` block. 1.2.0 covered ChatGPT and Grok only. Residue is
  now the first section of the file because it is the highest-confidence evidence
  available.
- **Heading-structure tells** in `extended-patterns.md`: title heading above content,
  skipped levels, level-1 overuse, headings containing only headings, thematic breaks
  between every section.
- **AI-VOCAB list** brought up to the source: *boasts* (meaning "has"), *bolstered*, *deep
  dive*, *meticulous/meticulously*, *robust* added. Era breakdown (2023 to mid-2024 /
  mid-2024 to mid-2025 / mid-2025 on) and the Grok idiolect note added.
- **NO-COPULA list** brought up to the source: *functions as*, *operates as*,
  *maintains*, *refers to* added, with the source's newer elaborate forms ("ventured into
  politics as a candidate").
- **"Signs of human writing"** section in `extended-patterns.md`, and a "Removing human
  signs" entry in Common issues, so the skill stops a rewrite from polishing human markers
  out.
- **House-style note** explaining that the file writes `--` deliberately: its own prose
  has to pass its own em dash check, and the scan counts the em dash character.
- This changelog.

### Changed

- **How-to list** restructured from six numbered steps that mapped loosely onto four
  passes into four passes that match the four section headers.
- **`ELEGANT-VAR`** marked declining. The source moved it to historical indicators in
  2026 and added the caveat that non-native English writers taught to avoid repetition
  produce it too.
- **`DIDACTIC`** renamed from "Didactic disclaimers and filler" to "Didactic disclaimers
  and section summaries," which is what the source's two historical sections cover.
- **`EM-DASH`** notes that some vendors have tuned em dash use down since it became
  notorious, so absence proves nothing.
- Display numbers 6-19 shifted by one to make room for `VAGUE-CONNECT` at #6. This is
  the first renumbering, and the reason the IDs exist.

### Calibration

The threshold table is measured, not argued. Corpus, built from the source page itself:

- **Positives:** 84 blocks (11,972 words) of the page's own quoted examples, each one
  editor-confirmed AI text. Extracted from the page's wikitext (`{{cot}}` blocks,
  blockquotes, and the AI side of `{{textdiff}}` pairs), markup stripped.
- **Human set 1:** 10 blocks (2,200 words) of the page's own editorial prose, written by
  Wikipedia editors, with the watch-list boxes and quoted examples removed.
- **Human set 2:** 50 blocks (7,487 words) from nine Wikipedia articles at their last
  revision before 2021, on the same subjects as the AI examples (Somali cuisine, Korattur,
  Los Angeles Art Association, Gillingham, Huey Lewis and the News, …). The source's own
  rule: text older than November 2022 cannot be AI.

Scanned with `scripts/scan-ai-tells.py` reading this version's watch lists, meta-quotation
filter on.

| Set | Blocks | Median density | p90 | Max | Max patterns |
|---|---|---|---|---|---|
| AI examples | 84 | 0.1 | 3.8 | 10.8 | 5 |
| Human editorial | 10 | 0.0 | 0.6 | 0.7 | 1 |
| Human pre-2021 | 50 | 0.0 | 0.4 | 1.6 | 2 |

Rule performance (true positive rate on AI blocks / false positive rate on human blocks):
density ≥ 2.0 with ≥ 1 pattern, 0.30 / 0.00; density ≥ 1.0 with ≥ 2 patterns,
0.21 / 0.03; ≥ 3 patterns at any density, 0.11 / 0.00. Two human blocks reached
2 patterns (`INFLATION` + `NO-COPULA`, via *features* and *serves as*), which is why
`NO-COPULA` now carries a calibration note. No human block contained a construction.

What the numbers say about the word lists: **42 of 84 confirmed-AI blocks scored zero.**
Their tells were markup, negative parallelism, formula sections, or headings, none of
which a word list catches. The lexical scan is precise and not sensitive. That is stated
in the skill so a clean word-list pass is not read as a clean bill.

Bias to note: the positives were chosen by Wikipedia editors as examples of *specific*
patterns, many of them markup, so the zero-hit rate overstates how often real AI prose
evades the word lists. The human sets are encyclopedic register; the thresholds have not
been checked on marketing or business prose.

### Verified

- Every pattern in SKILL.md checked against the live source on 2026-09-02. Every one is
  still there. `ELEGANT-VAR` and `DIDACTIC` have moved to the historical section, now
  reflected.
- Curly-quote claim (ChatGPT and DeepSeek yes, Gemini and Claude no) confirmed.
  `utm_source` vendors confirmed, plus Grok's `referrer=grok.com`.
- Cross-skill coupling: after the ID change, every reference in `farnsworth-rhetoric`
  (SKILL.md and changelog), `human-narrative` (SKILL.md and changelog), and
  `scripts/scan-ai-tells.py` was updated to IDs in the same commit. A grep for `#[0-9]+`
  next to "humanizer" across the branch returns only historical changelog lines that now
  carry the ID alongside the number they had at the time.
- `scripts/scan-ai-tells.py` regression: with the 1.2.0 watch lists, all nine farnsworth
  fixtures return identical counts before and after the meta-quotation filter and ID
  labels. With the 1.3.0 lists, the exec-summary *input* gains two hits ("associated
  with" is now `VAGUE-CONNECT`); its expected output still scans clean.

### Evaluated

Clean-context eval, 2026-09-02, four cases, `with` / `without` / `old` arms, one run per
configuration (`tests/evals/runs/2026-09-02/REPORT.md`). With-skill pass rate 0.95 (26 of
27 expectations) against 0.53 with no skill. The fresh executor applied the density table as
written ("0.7 per 100, in one pattern, inside the human range") and declined to rewrite;
left "in order to," "there is a," "very," and "the fact that" alone and said why; named
Gemini from the residue list. The one failure: the residue run wrote "when it drafted the
paragraph," claiming authorship the residue does not prove. That rule is in
`extended-patterns.md` and not in SKILL.md; candidate patch recorded in the report. The
v1.2.0 arm passed the known-human case with the same verdict, so no delta is measurable
on that case from the threshold table alone. The known-human fixture's filename leaked the
answer to all arms; corrected for the next run.

### Untested
- **Thresholds on non-encyclopedic prose.** Both human sets are Wikipedia register. A
  marketing one-pager written by a human may sit above 1.0 per 100 on `INFLATION` words
  alone. The "ambiguous" band exists for this reason, but it has not been checked.
- **`VAGUE-CONNECT` and `STYLE-SHIFT` have no before/after from a real run.** The
  `VAGUE-CONNECT` example is adapted from the source's examples; `STYLE-SHIFT` has no
  example because it is a document-level judgment, not a sentence edit.
- **The load-bearing test is a judgment call** with no measured agreement. Its value is
  that both skills now state the same test, so a disagreement between them is now a bug in
  one place rather than a design conflict.

## [1.2.0] - 2026-06-03

Eighteen patterns, tone awareness, voice calibration from a sample, four use cases,
`references/extended-patterns.md` for markup and citation artifacts. No changelog was kept
before 1.3.0; earlier history is in git.
