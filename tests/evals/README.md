# Clean-context evals for the writing triad

Eval definitions and run results for `humanizer`, `farnsworth-rhetoric`, and
`human-narrative`. The point of these, as against `tests/cases/`, is that the executor is a
fresh agent that has never seen the skill's authoring context, so a pass means the skill
taught the behaviour rather than the author already knowing it.

```
tests/evals/
  <skill>/evals.json        eval prompts, input files, expectations (skill-builder schema)
  <skill>/files/            input fixtures
  runs/<date>/              one run: per-arm directories, gradings, REPORT.md, results-table.md
  aggregate.py              gradings -> results table

  human-narrative/rubric.md               scoring instrument: all 30 StoryScope features
  human-narrative/agents/rubric-grader.md the LLM-judge pass over that rubric
  human-narrative/negative-cases.json     fixtures whose correct outcome is zero interventions
```

## The human-narrative rubric pass

`scripts/scan-ai-tells.py` cannot cover `human-narrative`: its features are structural, not
lexical. The script matches literal patterns, so of the 30 features it can see one corroborator
of one cluster (`FORWARD-REF`, added in #6) and nothing else. Coverage before the rubric was the
expectations written for the three evals in `human-narrative/evals.json`, which check the arms
those evals happen to exercise and cannot re-check the skill against its own feature list.

`rubric.md` is the instrument: every feature as a closed-form score with its option set, its
scale marker, its AI-side pole and its gap, plus the cluster gate/corroborator logic, the
register table, the Step 3 threshold and the Step 5 guardrails. `agents/rubric-grader.md` is
the judge, in the same shape as `skill-builder`'s `agents/grader.md`. It scores a text; to grade
a response it scores input and output separately and compares.

To run it:

1. Spawn a fresh judge with `agents/rubric-grader.md`, `rubric.md`, the input path, optionally
   the output path, and where to write `rubric-grading.json`.
2. Tell it not to read `negative-cases.json` (it holds the expected answer), not to read
   `skills/human-narrative/` (the rubric is meant to be sufficient on its own), and not to
   invoke the Skill tool.
3. For a negative case, assert `interventions_allowed == 0`.

`negative-cases.json` carries the three zero-intervention fixtures — a case study, an explainer
and a status update — each with the rubric author's own per-cluster scoring and the reason it
clears, so a judge that disagrees produces a reviewable diff rather than a silent pass. A
disagreement on one feature is not a failure; a disagreement that moves
`interventions_allowed` off zero is.

`validate-rubric-grading.py` checks a judge's output structurally: fields present, `side`
inside the vocabulary, no feature scored without evidence, no cluster fired on a gate alone,
the E/F collapse arithmetic, and the verdict and intervention budget following from the
adjusted count. `--negative-cases` also asserts `interventions_allowed == 0`. It cannot tell
you a score is *wrong* — that needs a reader, or a second judge and a diff.

First run, 2026-09-08: three fresh judges, one per fixture, blind to `negative-cases.json` and
to `skills/human-narrative/`. All three reached zero interventions, all three produced
schema-valid output, and every cluster verdict matched. The pass also produced nine rubric
fixes and three new `open_questions` about the skill itself — including one no eval had
caught: **D fires by construction on any non-narrative prose**, the same shape as E and F in
short form, but with no collapse rule, so a `thought-leadership` piece starts one cluster down
on the strength of having no flashbacks.

These matter more than the positive cases. `human-narrative`'s register allow-list is the change
its own changelog flags as most likely to be wrong, because no register in the table except
fiction appears in the StoryScope corpus — so the allow-list is unevidenced everywhere it gets
used most. A false positive on clean professional writing is what costs a user real work.

## Running

Follow `skill-builder` eval mode (`~/.claude/skills/skill-builder/references/eval-mode.md`).
In brief, per eval and per arm:

1. Scaffold `runs/<date>/<skill>/e<id>-<arm>/inputs/` with the fixture and
   `eval_metadata.json` (prompt plus expectations).
2. Spawn a fresh executor subagent with `agents/executor.md`, the skill path (or none for the
   `without` arm, or a `git archive` extract for the `old` arm), the prompt, and the inputs
   directory. Tell it not to invoke the Skill tool, not to read other skills, and not to run
   `scripts/scan-ai-tells.py`. The installed skills are symlinks into this repo, so the
   `without` arm must be told explicitly.
3. Extract the delivered text first, then scan that -- not the whole `result.md`:

   ```
   tests/evals/extract-delivered.py outputs/result.md -o outputs/delivered.txt
   scripts/scan-ai-tells.py --keep-quotes outputs/delivered.txt > scan.txt
   ```

   `--keep-quotes` is right for the delivered text, because executors put rewritten text in
   blockquotes which the default meta-quotation filter strips. It is wrong for the whole
   file: the change summary quotes the patterns it removed, so a raw scan counts citations
   as commissions. On the 2026-09-08 control arm the whole file showed 10 em dashes and the
   delivered text showed 2.

   Since #6 the scan also runs a **pattern-ID commentary filter** in both modes, dropping
   lines that label a quotation with a `humanizer` pattern ID. It is a backstop, not a
   replacement for this step: `extract-delivered.py` falls back to the whole file whenever
   the result has fewer than two `---` fences, which is how the r3 arm's change summary got
   scanned as prose in the first place. Extract first; the filter is what makes the fallback
   survivable. Pass `--keep-summary` to see the unfiltered number.

   The scan also reports `FORWARD-REF` (`human-narrative` cluster E) in its own column,
   deliberately outside density, the distinct-pattern count and the violation total. Do not
   fold it into a humanizer verdict.
4. Spawn one grader subagent per eval with `agents/grader.md`, grading every arm against
   the same expectations, writing `grading.json` per arm.
5. `tests/evals/aggregate.py runs/<date> --md runs/<date>/results-table.md`.

Spawning more than about eight subagents in one turn hits a spawn lock; batch them.

## Rules learned from the 2026-09-02 run

- Fixture filenames must be neutral. `human-2020-gillingham.txt` told every executor the
  answer.
- Expectations must define their thresholds ("minor edits" means punctuation or one word,
  at most one sentence). Graders otherwise invent the cut-off.
- An expectation must not forbid what another permits (the naming-a-reference intervention
  adds a name by construction).
- A fixture built to trip a rule must actually trip it under the skill's own threshold.
- Always include a fidelity expectation. The no-skill baselines invented facts in three of
  eleven cases and told the user "same facts."
- Read the graders' `eval_feedback`. It was the most useful output of the run.

## Rules learned from the 2026-09-08 run

- **Assertions that pass on absence measure nothing.** Four of eval 7's five original
  assertions were satisfied by a response that says "reads human" and stops, so lazy
  restraint and correct restraint scored the same. Every eval whose right answer is
  restraint needs at least one assertion that only a response doing the work can satisfy.
- **A carve-out needs a positive assertion.** "Does not flag X" passes for a response that
  never noticed X. Assert that the response identifies the construction and says it kept it
  deliberately.
- **A fixture must not resemble the skill's own worked example.** Eval 8's input shared its
  subject matter and move sequence with the `UNDER-PUNCT` example in `SKILL.md`, so a pass
  could not distinguish measurement from recall. Eval 9 is the same pattern in an unrelated
  domain; 8 is kept as a regression case only.
- **Assert arithmetic.** Two executors reported hand-computed statistics that did not
  reconcile with their own word counts. Neither changed a verdict and no assertion caught
  either. Un-thresholded patterns rest on hand measurement, so the measurement needs checking.
- **Assert that cited rules are quotable.** A control-arm executor invented a retention rule
  ("one per paragraph is normal punctuation") and stated it to the user as the skill's.
- **Grade the delivered text, not `result.md`.** See step 3.
- A control arm is supposed to fail. Tell the grader so explicitly, or it grades charitably
  and the A/B collapses.

See `runs/2026-09-02/REPORT.md` and `runs/2026-09-08/REPORT.md` for results and the changes
they drove.
