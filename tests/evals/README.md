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
3. Run `scripts/scan-ai-tells.py --keep-quotes` on `outputs/result.md` and save as
   `scan.txt`. Use `--keep-quotes` here: executors put rewritten text in blockquotes, which
   the default meta-quotation filter strips.
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

See `runs/2026-09-02/REPORT.md` for the first run's results and the changes it drove.
