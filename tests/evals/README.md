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
```

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
