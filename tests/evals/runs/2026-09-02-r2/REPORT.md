# Writing-triad eval re-run — 2026-09-02-r2 (+ r3 verification)

Second clean-context evaluation of the writing triad, run against the four candidate
patches applied earlier the same session (`0d604c7` humanizer 1.3.1, `810507d`
farnsworth-rhetoric 1.1.1, `f0acd86` human-narrative 1.1.1) plus the corrected `evals.json`
files from the first run's grader feedback. Arms are `prev` (the pre-patch version, via
`skills-prev/`) and `with` (the patched version) — no `without` or `old` arm this time; the
question this run answers is "did the patch help," not "does the skill help at all."

## Method

Same executor/grader procedure as `runs/2026-09-02/REPORT.md`. 16 executor runs (11 skills
worth of `prev`/`with` pairs, minus one skill with 3 evals instead of 4), 11 graders, 79
graded expectations. One run per configuration; treat single-expectation deltas as noise.

One executor run (`farnsworth-rhetoric/e3-with`) stalled mid-session on a provider rate
limit before writing its output; it was re-run to completion in the same run directory
before scanning and grading. `superseded/` holds two abandoned Fable-model executor attempts
that predate the opus-5 standardization; not part of the graded set.

## Results

| Skill | prev mean | with mean |
|---|---|---|
| farnsworth-rhetoric | 0.89 (4 evals) | 0.91 (4 evals) |
| human-narrative | 0.83 (3 evals) | 0.92 (3 evals) |
| humanizer | 0.94 (4 evals) | 0.88 (4 evals) ⚠️ |

Per-eval detail in `results-table.md`. farnsworth-rhetoric and human-narrative improved on
the patches under test. humanizer regressed on one eval (below) — the other three are
unaffected and pass 100% on both arms.

### Patches confirmed working

- **farnsworth e3 (tagline-options): 0.57 → 1.00.** This is the direct target of
  `810507d`. The prev arm generated an antithesis treatment its own claim check flagged as
  "the least defensible" and shipped it anyway with a caveat; the with arm withdrew the same
  class of failing candidate into a labeled "Withdrawn candidates" section instead of
  presenting it. Exactly the failure mode the patch exists to close.
- **human-narrative e2 (short-form-proportionality): 0.75 → 1.00.** prev produced a 596-word
  audit with a full cluster table for a 48-word input; with produced a single 110-word
  paragraph with an explicit "leave it" verdict. `f0acd86`'s length-floor guidance held.

### humanizer regression: e1 (ai-heavy-rewrite), 0.75 → 0.50

`0d604c7` added one line to the "Edit with constraints" use case: *"When 'humanize' and a
constraint arrive together, this use case wins."* The eval prompt is "Humanize this... Keep
it professional." "Keep it professional" is a bare register descriptor, not a scope-limiting
constraint — "Full rewrite"'s own Tone awareness section already defaults to professional
register for that kind of text. The new clause had no test for that distinction, so it
routed the prompt into Edit with constraints, which only includes a change summary "on
request." No request was made, so the with-arm response dropped the full change summary and
stable pattern IDs that four of this eval's eight expectations depend on.

Confirmed as the mechanism, not a grading fluke, by diffing `0d604c7` against the previous
committed version and tracing the exact clause.

**Fixed in `0089d3a`** (v1.3.2): narrowed "Edit with constraints" to constraints that limit
*what may change* (structure, length, specific wording or facts to preserve); a bare
register descriptor now stays in Full rewrite with its change summary intact.

**Verified in `runs/2026-09-02-r3/humanizer/e1-with/`** (`6c29196`): re-ran the same eval
against the patched skill. **8/8 (1.00)**, above even the pre-patch prev-arm baseline of
6/8. The executor correctly stayed in Full rewrite and produced a 9-pattern change summary
(`INFLATION`, `NO-COPULA`, `AI-VOCAB`, `VAGUE-ATTRIB`, `NEG-PARALLEL`, `BOLD-LISTS`,
`CHALLENGES-FORMULA`, `DIDACTIC`, `GENERIC-CLOSER`).

One incidental finding from the r3 grading: `scan.txt` reported 3 hard `NEG-PARALLEL`
violations on the r3 output, but they are false positives — the scanner matched illustrative
quotes of the *removed* original text embedded inside the change-summary section, not
anything in the live rewritten prose. Graded on the actual body text instead. Worth revisiting
if `scan-ai-tells.py`'s meta-quotation filter keeps missing change-summary quotation the way
`runs/2026-09-02/REPORT.md` already flagged it missing blockquotes.

### Other with-arm shortfalls (not regressions — pre-existing or reporting gaps)

| Run | Rate | Note |
|---|---|---|
| farnsworth e1-with | 4/5 | Flagged for restructuring beyond word-substitution in a hard-stop register; grader noted the same paragraph-2 sentence-split pattern also appears in `e1-prev`, so this may predate the patch rather than be introduced by it — not confirmed either way. |
| farnsworth e2-with | 5/5 | Passes; scan.txt shows 2 hard violations vs. prev's 1, but the grader judged the extra `NEG-PARALLEL` hit a likely false positive (the skill's own diction checklist prose, not the forbidden construction). |
| farnsworth e4-with | 6/7 | Claim check names 3 of 5 required hedges explicitly; the other two survive in the body but go unmentioned in the check itself — a reporting-completeness gap, not a substance failure. |
| human-narrative e3 (both arms) | 6/8 | Tied. Both arms fail the same two expectations for the same structural reason: the skill's own cluster-priority order caps interventions at 3 and puts the resolution-governing cluster 6th, so it's correctly excluded — the grader flagged this expectation as miscalibrated against the skill's own design, not a defect in either arm. |

### Eval-authoring notes carried forward

Graders again flagged assertions worth tightening for the next run (full text in each
`grading.json`'s `eval_feedback`):

- Several "no change" expectations (farnsworth e2, human-narrative e1's fact-preservation)
  are trivially satisfied whenever the model declines to edit — they don't discriminate
  quality of reasoning when the correct answer is "leave it alone."
- No assertion anywhere checks the accuracy of an executor's own self-reported craft claims
  (farnsworth's "ear test" prosody count, humanizer's "avoided decorative triads" claim) —
  both skills had executors make a specific, checkable claim that scan.txt or manual count
  contradicted, uncaught by any expectation.
- Several runs' transcripts reference `user_notes.md` / `metrics.json` as produced outputs
  that don't exist on disk — a run-artifact completeness gap across several arms, not a
  skill defect.
- `human-narrative e3`'s forward-reference expectation ("Here's the full audit, then the
  rewrite") is a clean catch that `scan-ai-tells.py` misses entirely at 0 flags — a candidate
  for adding to the scan script.

## Limits

- One run per configuration; no variance measurement, same as r1.
- No `without`/`old` arm this round — this run measures patch delta, not skill-vs-baseline
  value (that question was answered in r1).
- r3 covers only the one regressed eval, re-run to confirm the fix; the other three
  humanizer evals were not re-run since the patch was scoped to the use-case
  disambiguation clause they don't exercise.
