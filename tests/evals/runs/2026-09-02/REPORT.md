# Writing-triad eval run — 2026-09-02

First clean-context evaluation of `humanizer` v1.3.0, `farnsworth-rhetoric` v1.1.0, and
`human-narrative` v1.1.0. Until this run, every test of these skills had been authored and
executed in the same context as the skill, so it showed the outputs complied, not that the
skill taught a fresh agent to comply. This run closes that gap for eleven cases.

## Method

- **Executors:** one fresh general-purpose subagent per run, following
  `skill-builder/agents/executor.md`. It received the skill directory path, the user
  prompt, and the input file. It was told not to invoke the Skill tool, not to read other
  skills, and not to run `scripts/scan-ai-tells.py`.
- **Arms:** `with` (current skill), `without` (no skill; told not to load any), and `old`
  (the previous committed version, extracted with `git archive`) on the one case per skill
  most likely to show a regression.
- **Graders:** one subagent per eval, grading every arm of that eval against the same
  expectations, following `skill-builder/agents/grader.md`. Each grader also critiqued the
  eval itself. `scan.txt` beside each run is the deterministic scan of that run's
  `result.md`, given to graders as evidence.
- **One run per configuration.** No variance measurement. Treat single-run deltas of one
  expectation as noise.
- 25 executor runs, 11 graders, 106 graded expectations.

Layout: `<skill>/e<id>-<arm>/` holds `inputs/`, `outputs/result.md` (the user-facing
response), `outputs/user_notes.md`, `outputs/metrics.json`, `transcript.md`, `scan.txt`,
`grading.json`. `results-table.md` is the aggregate. `skills-old/` holds the previous
skill versions used by the `old` arm.

## Results

| Skill | with | without | old (1 eval) |
|---|---|---|---|
| farnsworth-rhetoric | **0.95** (4 evals) | 0.47 | 0.75 |
| human-narrative | **0.88** (3 evals) | 0.56 | 0.60 |
| humanizer | **0.95** (4 evals) | 0.53 | 1.00 |

Per-eval detail is in `results-table.md`. Every eval except human-narrative e2 shows the
skill arm ahead of the no-skill arm. Both regression arms that could show a delta did.

### What the skills demonstrably taught

- **Restraint.** farnsworth e2 (already-good paragraph): the skill arm returned the text
  unchanged with a stated budget; the baseline "strengthened" three sentences and turned
  the author's understated lesson into a categorical maxim. humanizer e4 (human paragraph
  with human markers): the skill arm left "in order to," "there is a," "very," and "the
  fact that" alone and said why; the baseline replaced two of them and added a hedge.
  humanizer e2 (known-human text): the skill arm reported one hit in 135 words, cited the
  calibration range, and declined to rewrite; the baseline volunteered a paragraph rewrite.
- **Hard stops.** farnsworth e1 (runbook): the skill arm did diction only and flagged the
  fixture's undefined exactly-thirty-seconds boundary rather than resolving it; the
  baseline restructured into a checklist and changed the threshold logic; the v1.0.0 arm
  did diction plus one added emphasis sentence, which is the dosage failure v1.1.0 exists
  to prevent.
- **Truth constraint.** human-narrative e1 (case study): the skill arm kept every
  Ridgeline fact; the v1.0.0 arm asserted "maintenance scheduling still runs on
  spreadsheets," a present-state claim the input never makes; the baseline invented five
  characterizations while telling the user "same facts." human-narrative e3 (essay): the
  baseline added three biographical details to a first-person non-fiction essay and
  disclosed it only in its private notes.
- **Vocabulary.** humanizer e1: the skill arm named patterns by stable ID and converted
  the bold inline-header list; the baseline swapped the colons for periods and kept the
  bold lead-ins. humanizer e3: the skill arm named Gemini as the source of `[cite: N]`
  and `[span_2](start_span)`; the baseline hedged between "an AI research tool or a
  document export" and reworded every sentence.
- **Claim check.** farnsworth e4: the skill arm listed the hedges that survived; the
  baseline claimed "nothing was softened" while turning "financial modelling indicates
  ... would offset" into a statement of fact and adding a commitment the source never made.

### With-skill failures (4 of 78 expectations)

| Run | Failed expectation | Verdict |
|---|---|---|
| humanizer e3-with | Does not claim the markers prove authorship | **Skill defect.** Response wrote "sources Gemini was reading when it drafted the paragraph." The rule (residue proves a chatbot touched the citation, not that it wrote the prose) lives in `extended-patterns.md`, not in SKILL.md. Candidate patch below. |
| farnsworth e3-with | No option adds a claim absent from the input | **Skill gap, small.** Treatment 4 (antithesis, "not on a shelf") characterizes the alternative; the executor's own claim check caught it and it shipped the option anyway as non-recommended. The skill runs the claim check but does not say a treatment that fails it is withdrawn. Candidate patch below. |
| human-narrative e1-with | Invents no facts (every name/date in output appears in input) | **Eval defect.** The F intervention (name a specific reference) adds a name and date by construction; the executor added Goldratt, *The Goal* (1984), labeled it, and told the user to run `source-check`. The expectation forbids what expectation 2 permits. Fixed in `evals.json`. |
| human-narrative e3-with | At least one embodied metaphor replaced | **Eval defect.** The skill's cluster B fires at an embodied share of 60% or more; the fixture's share is about 33%, so the skill arm correctly did not fire B. The fixture assumed B would fire. Fixed in `evals.json` (fixture tuning noted; assertion made conditional on B firing). |

### Regression arms

- farnsworth e1-old (v1.0.0): 3/4. Added a one-word emphasis sentence ("If lag is over
  thirty seconds, stop.") to a runbook. v1.1.0's hard stop and dosage rule prevent this;
  the v1.1.0 arm scored 4/4.
- human-narrative e1-old (v1.0.0): 3/5. Applied four structural changes to a case study,
  one of them a resolution-mode move that produced an invented present-state claim.
  v1.1.0's register table, cap of 2, and truth constraint prevent this.
- humanizer e2-old (v1.2.0): 4/4, same verdict as v1.3.0. **No measurable delta on this
  case.** The v1.3.0 arm reported a density ("0.7 per 100, in one pattern") and the v1.2.0
  arm did not, but no expectation measured that. See eval defects.

### Observations that are not graded failures

- **Proportionality on short inputs.** human-narrative e2: the input is a 48-word status
  update. Status updates are in the skill's short-form row (A, B, E, F in scope), not the
  hard-stop row, so the skill arm ran a full cluster scan and produced a 508-word audit
  with a table and corpus percentages before concluding zero interventions. That is
  compliant and correct, and it is also more than the input warrants. The no-skill arm
  reached the same verdict in 270 words. The register allow-list was already flagged in
  the 1.1.0 changelog as the change most likely to be wrong; this is one data point that
  the short-form row needs a length floor or a "report in proportion" rule.
- **Blocked-intervention slot.** human-narrative e3-with: the F intervention was blocked
  by the truth guardrail and the executor "assumed a blocked intervention frees its cap
  slot" and took the next in order. The skill says the intervention loses but not whether
  the slot is reused. Ambiguity worth one sentence.
- **Single-line output shape.** farnsworth e3-with produced both the treatments list and
  the strengthen-mode change note, "since the skill asks for both in different places."
  The Single-line use case should say which.
- **Scan blind spot for eval outputs.** The meta-quotation filter strips blockquotes, and
  executors put rewritten text in blockquotes, so `scan.txt` scored commentary rather than
  output in several runs. For grading, run the scan with `--keep-quotes` or on a flattened
  copy of the rewrite. Noted in `tests/evals/README.md`.

## Eval defects found by the graders, and what changed

The graders' `eval_feedback` sections were the most useful product of the run. Applied to
`tests/evals/*/evals.json` for the next run:

- **humanizer e2's input filename leaked the answer** (`human-2020-gillingham.txt`). All
  three executors noted the filename before reading the text. The verdicts may still be
  right, but the case cannot be trusted to discriminate. Renamed to `sample-b.txt`.
  Example words in the expectation replaced with the words actually present.
- humanizer e1: added a fidelity expectation (no facts not in the source) and the
  inverted "X, not Y" form to the negative-parallelism list.
- humanizer e3: "output text" defined as the cleaned paragraph; sourcing-caveat expectation
  added.
- humanizer e4: "minor edits" defined (punctuation or one word, at most one sentence);
  "pad" rephrased to cover any added word, hedge, or punctuation.
- farnsworth e1: diction defined (word substitution, no added or split sentences); the
  exactly-thirty-seconds boundary made its own expectation.
- farnsworth e3: expectation that a treatment failing the claim check is withdrawn, not
  offered; count and figure-naming split into two expectations.
- farnsworth e4: "Financial modelling indicates" and "should not be interpreted as a
  recommendation" named as hedges; numbers-retained and no-added-commitment expectations.
- human-narrative e1: expectation 4 now permits one labeled outside reference; "facts"
  extended to events, states, and characterizations; "thread not present in the input."
- human-narrative e2: renamed from "hard-stop" to "short-form-proportionality," with an
  expectation on response length relative to input.
- human-narrative e3: truth-preservation expectation added; embodied-metaphor expectation
  made conditional on cluster B firing; fixture note that B sits under the 60% rule.

## Candidate skill patches (not applied in this run)

1. **humanizer, SKILL.md "When a flag is a finding":** add one sentence: residue proves a
   chatbot touched the citation or paragraph it sits in, not that it wrote the surrounding
   prose. Evidence: e3-with wrote "when it drafted the paragraph." Patch level.
2. **farnsworth-rhetoric, Single-line use case:** a treatment that fails the claim check is
   withdrawn, not presented as an option; and state which output shape single-line mode
   uses. Evidence: e3-with. Patch level.
3. **human-narrative, Step 5:** when a guardrail blocks an intervention, the next in order
   takes its slot (or does not; pick one). Evidence: e3-with executor note. Patch level.
4. **human-narrative, Step 1 / Step 3:** on short professional text, clusters E (reader
   address) and F (intertextual reference) fire by construction, since a status update
   never addresses the reader and never names a book. The threshold table then reports
   "some AI-side clustering" on a piece the skill's own prose says should be zero, and the
   executor reconciles it by hand. Either drop E from the short-form row, or state in
   Step 3 that E+F alone do not reach the intervention bar below 600 words, and add a
   "report in proportion to the input" rule. Evidence: e2-with executor notes. Design
   question, not a patch.

### Executor suggestions collected from `user_notes.md`

Smaller items the fresh executors raised while following the skills. Each is in the
named run's `outputs/user_notes.md`.

- **farnsworth description contradicts its body** (e1-with). The frontmatter says "Do
  NOT use for ... process instructions"; the register table handles process text with
  "diction work only." The executor followed the table. Pick one: either the description
  says "process text gets diction only, no figures," or the table row says decline.
- **farnsworth register table has no row for a blog post-mortem** (e2-with). Treated as
  thought leadership; budget was 1 either way. Add "engineering blog, post-mortem" to
  the thought-leadership row.
- **Both farnsworth executors miscounted the 19-word tagline as 22** (e3, grader note).
  The budget arithmetic was wrong but the verdict unchanged. A "count the words" line in
  Step 1 is cheap.
- **humanizer "Full rewrite" should say what to do when the scan is clean** (e4-with).
  "Return the text unchanged" is currently inferable from three separate sections.
- **humanizer has no guidance for `VAGUE-ATTRIB` when no real source exists** (e1-with).
  The fix says "name a source"; the executor kept the claim and flagged it. State the
  fallback: delete the claim or flag it inline.
- **humanizer `INFLATION` list misses marketing adjectives like "seamless"** (e1-with).
  The executor caught it anyway. Consider adding *seamless*, *effortless*, *powerful*
  (figurative) to the watch list, or a note that the list is not exhaustive.
- **humanizer says nothing about warning the user that stripped residue was the only
  sourcing** (e3-with), or whether to name the model in the change summary. Both
  executors volunteered the warning; make it a rule.
- **humanizer review-and-flag mode has no verdict line** (e2-old, e2-with). Both arms
  invented one. Add "open with a one-line verdict and confidence" to the use case.
- **human-narrative Step 5 does not say whether a blocked intervention frees its slot**
  (e3-with). Already patch 3 above.

## Limits

- One run per configuration; no variance.
- The `old` arm was run on one eval per skill, chosen as the likeliest regression.
- The executors and graders are the same model family as the skill authors; the graders
  did not see the arm labels but the run directories name them.
- Two of the eleven cases are compromised for discrimination (humanizer e2 by filename,
  human-narrative e3 by fixture assumption) and are corrected only for the next run.
- The executors could not run the scan script or chained skills (`beyond-obvious`,
  `source-check`, `humanizer` after `human-narrative`), so pipeline behaviour is untested.
