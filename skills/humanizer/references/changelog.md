# Changelog

## [1.4.1] - 2026-09-08

Closes the item 1.4.0 recorded and deferred (#10). No watch-list or threshold changes.

### Fixed

- **`NEG-PARALLEL`'s reversed variant had no example separating it from comparative
  preference.** "X rather than Y" was listed among the patterns to watch with nothing to
  distinguish a straw rejected pole from a genuine choice between two real outcomes ("I
  would rather wait for the data than publish something that gets revised"). Three
  executors in `tests/evals/runs/2026-09-08/` hit the call independently -- e5-with,
  e5-prev, e7-with -- and all three resolved it correctly by reasoning the skill did not
  supply. Now stated as a deletion test, matching the tests `RULE-OF-3` and "undecided
  connection" already use: cut the "rather than Y" clause, and if the sentence makes the
  same claim without it, Y was a straw pole. A before/after pair and a preference left
  unchanged sit under the test.

  The variant is ungated by the density table, which is why an example was worth a release
  on its own: a false positive there carries a verdict with no threshold to catch it.

### Tests

- `tests/cases/06-decision-note-{IN,OUT}.txt` -- negative case, byte-identical by
  convention. A note whose point is a stated preference; the correct output is no change.
  The scanner has no "rather than" regex, so this fixture is not a scanner regression test:
  it holds the line for the executor reading the pattern list literally, which is the
  failure mode the three eval arms were one judgment away from.

## [1.4.0] - 2026-09-08

Source re-check against the live page on 2026-09-08, plus one pattern from outside it. The
page carries an August 2026 banner saying parts of it relating to the most recent models
need updating -- the source flags its own currency limits, which is the argument for dating
the vocabulary buckets rather than maintaining them as one list.

### Fixed

- **`EM-DASH` was one-directional and is no longer true.** The pattern claimed LLMs use em
  dashes more than human writers, hedged only with "some vendors have tuned this down."
  The July 2026 corpus study found the heuristic has inverted for most models: only one of
  the four frontier models tested exceeds human writers on em dashes, and one sits below
  every human baseline in the study. The folk rule has also changed human behaviour, with
  writers stripping dashes from their own prose to avoid suspicion, so the signal is
  contaminated in both directions. Retitled "Em dash overuse" -> "Em dash frequency", ID
  unchanged. Now scoped to pre-2025 text or co-occurrence with other Pass 2 patterns, and
  says explicitly that dash scarcity proves nothing on its own.

  Per-model variance is the reason the pattern was scoped rather than deleted, and it is
  recorded here rather than in SKILL.md: an executor holding text of unknown origin cannot
  evaluate a per-model rule.

  Upstream had already revised its em dash section and cites the same study; it carries a
  September 2026 banner *proposing* relocation to Historical indicators. The proposal is
  conditional and has not happened, so the pattern stays resident. This release catches up
  to the source rather than diverging from it.
- **Added the spacing discriminator `EM-DASH` never had.** AI-generated em dashes are
  usually surrounded by spaces, against the convention most human dash-users follow. This
  is a form tell rather than a frequency tell, so it survives the reversal above.
- **`three em dashes in a paragraph` was an ungated finding.** Now scoped to pre-2025 text
  in "What the table does not gate." The claim that no human block in the calibration set
  contained one is left intact: that corpus predates the reversal and the statement remains
  true of it.

### Added

- **`UNDER-PUNCT` -- punctuation scarcity.** Display 10, Pass 2. Current models
  under-punctuate, which is the reverse of what this skill and its source both encode: fewer
  commas and semicolons than human writers, parentheses nearly absent, longer sentences, and
  "and" as the most overused word. Two causes given in the source -- longer sentences carry
  fewer internal breaks, and the models do not quote real people, which removes quotation
  marks and attributive commas. That second cause is why the pattern points at
  `VAGUE-ATTRIB`.

  **This is the one pattern in the skill not drawn from the Wikipedia page.** Punctuation
  scarcity does not appear there at all; the only adjacent line runs the other way, that
  humans use commas, parentheses and colons where models use dashes. Source: The Economist,
  "How to spot AI writing," 30 July 2026 -- four frontier models prompted to rewrite
  Economist articles without web access, compared across 55,940 sentences and 1.2m words,
  checked against CNN/NYT/WaPo journalism and 1950-2022 bestseller fiction. Findings are
  published as chart positions only: no effect sizes, no methodology appendix.

  **Baseline caveat.** Economist house style is unusually short-sentenced and heavily
  punctuated for a human baseline, which would widen every gap the study reports. This is
  the main reason the pattern ships **un-thresholded**: there is no published calibration to
  set a number from, and inventing one from a single source with no effect sizes would give
  the threshold table a precision it has not earned.

  Structural rather than lexical, so unlike the vocabulary layer it should not decay as
  model vocabulary churns.
- **Date check in "When a flag is a finding."** The source rules AI use out entirely for
  text written before ChatGPT's public launch on 30 November 2022, and notes that older
  writing sometimes displays these signs by coincidence. The skill had no date check
  anywhere and would run a full scan on a 2015 draft with no cue that the exercise was
  misconceived. Roughly 40 words, and it forecloses a whole class of false positive.
- **`AI-VOCAB` mid-2026 bucket.** The tell shifts from listed words to register:
  polysyllables, rare words, scientific vocabulary, nominalisations, Latinate suffixes over
  Saxon roots. Orwell's "pretentious diction." Literal scanning cannot catch it, so the
  entry routes to `farnsworth-rhetoric`'s Saxon default rather than duplicating the rule.

  **Why the buckets are dated rather than maintained.** Juzek, quoted in the same article,
  attributes vocabulary churn to models being tuned on human feedback and absorbing what
  readers find impressive. A list maintained as current will always lag; a list dated by era
  stays useful for older text as it ages out of currency. That reasoning is here rather than
  in SKILL.md because it is addressed to whoever maintains the list, not to whoever is
  editing a draft.
- **Two `VAGUE-CONNECT` sub-patterns.** *Rotating connectors* (a small repeating set
  carrying every transition in a piece) and *undecided connection* ("and" joining two ideas
  whose relationship was never chosen), with a cut-and-test procedure for the second. Both
  are vague expression of connection, so they extend an existing ID rather than adding two.

  The cut-and-test is adapted from third-party commentary on the study, not from the study
  itself, and is not attributed to The Economist.
- **A drafting principle in Pass 1.** "The common root is the impulse to explain a thing's
  significance instead of stating it." The only guidance in the file usable while drafting
  rather than editing.

### Changed

- **`ELEGANT-VAR` moved to `extended-patterns.md`,** into the Historical indicators section
  that already carried a pointer to it. The pointer now reverses direction. It keeps its
  stable ID and leaves the SKILL.md pattern table entirely rather than staying as a stub:
  nothing outside humanizer references it, verified by grep across the sibling skills and
  the scan script. It has no watch list, so density and spread are unaffected.
- **`DIDACTIC` stays resident, on revised grounds.** The 2026-09-08 check found both of its
  halves demoted to the source's Historical indicators -- "Didactic disclaimers (November
  2022-2024)" and "Section summaries" -- which reverses the reason it was kept resident
  while `ELEGANT-VAR` moved. It stays anyway, for a different reason: `farnsworth-rhetoric`
  and `human-narrative` both reference `DIDACTIC` by ID in their own tables, so it fails the
  external-safety test that cleared `ELEGANT-VAR` to move. Relocating it would mean editing
  two more skills to keep three cross-references resolving. Revisit if those references go.
- **Display numbers.** `UNDER-PUNCT` enters at 10 and `ELEGANT-VAR` leaves, so the
  insertion and the deletion cancel below row 11. `CHALLENGES-FORMULA` moves 10 -> 11 and is
  the only number that changes; rows 12-20 are untouched. Twenty rows before, twenty after.
  Second renumbering since the IDs were introduced.
- **Pass 4 voice check absorbed "Signs of voiceless writing"** from Tone awareness. Same
  diagnostic stated twice, in two places; it now lives where the executor is standing when
  it needs it.
- **Citations compressed to author and year** in `AI-VOCAB` and `NO-COPULA`. Venue names,
  paper titles, the arXiv identifier, the effect size and the 10,000-abstract replication
  detail are evidence, and evidence belongs here. Named attribution is kept rather than
  dropped: this skill flags `VAGUE-ATTRIB`, and 1.3.0 records fixing a self-violation where
  a pattern body said "studies have shown" in the skill's own voice. Author plus year is the
  floor.
- **Calibration derivation moved here.** The paragraph under the threshold table duplicated
  the Calibration section below in less detail. SKILL.md keeps one clause -- that no human
  block scored above 1.6 per 100 -- because it tells the executor how much headroom the
  thresholds have.
- **Deduplication pass.** The register-descriptor ruling stated in both "Full rewrite" and
  "Edit with constraints" now states once with a pointer; "Ambiguous patterns" reduced to
  the pointer and the one thing the density table does not carry; the `NEG-PARALLEL` example
  dropped from "Meaning loss on rewrite," where the pattern's own section already covers it;
  the `INFLATION` regression-to-the-mean mechanism cut to the clause an executor can apply
  to a sentence.

### Not adopted, with reasons

Recorded so the next person diffing against the source does not re-open the argument.

- **Per-model style profiles** ("Differences between LLMs" on the source page). Keyed to a
  variable the executor cannot observe: it holds text of unknown origin, so a per-model
  conditional is unevaluable at runtime. Also dated -- the page's examples are GPT-4o,
  Grok-Beta, Gemini 1.5 and Claude 3.5. Model-specific *markup residue* stays in
  `extended-patterns.md` and is not the same thing: residue is an observable artifact that
  identifies the tool, whereas idiolect requires knowing the model before you can apply it.
- **"Biases in content."** Political bias in model output is a content-integrity question
  about what models say, not a tell for how they say it. Outside what a rewriting skill
  does.
- **Comment-specific indicators.** The page has a full section on AI-generated discussion
  comments with its own sub-page. This skill targets prose -- posts, essays, reports,
  emails -- and comments are a different genre with a different tell profile. Note that the
  em dash tell is reportedly stronger in discussion text, which is now recorded in
  `EM-DASH` itself.
- **Detection-confidence calibration.** The page carries data on detector error rates and
  on humans performing at chance level. "Review and flag" asks for a confidence number with
  no calibration behind it. Deferred: "What residue proves" already governs the claims this
  skill may make, and the skill never invokes a detector. Add only if an eval run shows
  executors producing overconfident verdicts.
- **The `writ` skill's vocabulary list.** Mixes source-derived flags with popular lore
  (*moreover*, *realm*, *leverage*, *holistic*, *game-changer*, "in today's fast-paced
  world"). `AI-VOCAB`'s take-the-list-literally rule exists to prevent exactly that drift.
- **The article's closing advice** ("look for bland, pretentious prose lavished with
  Latinate words") as a standalone rule. It is the same single-feature heuristic the article
  itself spends three paragraphs warning against.
- **Detection-accuracy claims.** The article quotes a vendor's 99.98% figure and
  immediately notes detectors give false positives and no reasons.
- **Recalibrating the density table.** Different corpus, different genre, no published
  numbers, and a human baseline anchored on one publication's house style. The 1.3.0
  calibration is unchanged.

### Patches from the gate run

`tests/evals/runs/2026-09-08/`. Five cases, six arms, all clean-context. Two patches landed
before merge, both found by executors rather than by review.

- **`UNDER-PUNCT` was missing from "What the table does not gate."** Its exemption was
  stated one paragraph earlier, next to the density and spread bullets, but the paragraph
  that actually enumerates table-bypassing findings did not list it. Two executors, on
  unrelated fixtures, independently reported the same consequence: a reader applying the
  table mechanically scores an unpunctuated text at density 0.0, spread 0, and ships it
  unchanged. Both still caught it -- one cited the rate exemption, the other "a clean
  word-list scan is not a clean bill" -- but both had to assemble the ruling from two
  places. Now stated in the paragraph where the decision is made.
- **The scanner caveat was too weak.** `UNDER-PUNCT` said the script "does not compute
  these," which reads as a missing feature rather than a trap. It now says a clean report
  from the script is not evidence against the pattern, because the script scores an
  unpunctuated wall of "and" at zero. Added an instruction to check arithmetic before
  quoting a rate: two executors reported hand-computed statistics that did not reconcile
  with their own word counts. Neither error changed a verdict, but an un-thresholded
  pattern rests entirely on hand measurement, which is the failure mode to watch.

Not patched, recorded instead: `NEG-PARALLEL`'s reversed "X rather than Y" variant has no
example separating it from ordinary comparative preference ("I would rather wait than
publish"). Three executors hit that judgment call and all three resolved it correctly, but
the variant is ungated by the density table, so a false positive there flips a verdict on
its own. Predates 1.4.0 and is out of scope for it. Filed as #10, fixed in 1.4.1.

### Tooling

The audit and brief behind this release both recorded `scripts/scan-ai-tells.py` as missing
and treated its absence as an open question, because they were read against a packaged
`.skill` bundle rather than the repo. The script was at the repo root the whole time, and
as of #9 it ships inside the humanizer and farnsworth-rhetoric packages too, so the three
`scripts/scan-ai-tells.py` references in SKILL.md now resolve for installed users and not
only in-repo. No pattern text was written against tooling that does not exist.

`scripts/scan-ai-tells.py` computes no rate measures -- commas per sentence, sentence
length, parentheses per 1,000 words -- and does not count Latinate suffixes. Both
`UNDER-PUNCT` and the `AI-VOCAB` register note are therefore written as manual reads and
say so in the text, rather than promising tooling that does not exist. The script's
auto-extraction reads `**... to watch:**` lines from SKILL.md; `UNDER-PUNCT` deliberately
uses `**Signals:**` so that "and" is never pulled into the flag set.

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
