# Improve Mode Reference

Iteratively optimize a skill using the run-grade-compare-analyze loop.

## Setup Phase

### 0. Read output schemas

```bash
Read references/schemas.md  # JSON structures for grading, history, comparison, analysis
```

This tells you the structure of outputs you'll produce and validate.

### 1. Choose workspace location

**Ask the user** where to put the workspace. Suggest `<skill-name>-workspace/` as a sibling to the skill directory. If the workspace ends up inside a git repo, suggest adding it to `.gitignore`.

### 2. Copy skill to v0

```bash
scripts/copy_skill.py <skill-path> <skill-name>-workspace/v0 --iteration 0
```

### 3. Verify or create evals

- Check for existing `evals/evals.json`
- If missing, ask user for 2-3 example tasks and create evals
- Use `scripts/init_json.py evals` to create with correct structure

### 4. Create tasks for baseline

```python
for run in range(3):
    TaskCreate(
        subject=f"Eval baseline, run {run+1}"
    )
```

### 5. Initialize history.json

```bash
scripts/init_json.py history <workspace>/history.json
```

Edit to fill in skill_name. See `references/schemas.md` for full structure.

---

## Iteration Loop

For each iteration (0, 1, 2, ...):

### Step 1: Execute (3 Parallel Runs)

Spawn 3 executor subagents in parallel (or run sequentially without subagents). Update task to `implementing` stage.

```
Read agents/executor.md at: <skill-builder-path>/agents/executor.md

Execute this task:
- Skill path: workspace/v<N>/skill/
- Task: <eval prompt from evals.json>
- Test files: <eval files if any>
- Save transcript to: workspace/v<N>/runs/run-<R>/transcript.md
- Save outputs to: workspace/v<N>/runs/run-<R>/outputs/
```

### Step 2: Grade Assertions

Spawn grader subagents (or grade inline). Update task to `reviewing` stage.

Grading produces structured pass/fail results for tracking pass rates. The grader also extracts claims and reads user_notes to surface issues that expectations might miss.

**Set the grader up for success**: The grader needs to inspect actual outputs, not just read the transcript. If outputs aren't plain text, tell the grader how to read them -- check the skill for inspection tools and pass those as hints.

```
Read agents/grader.md at: <skill-builder-path>/agents/grader.md

Grade these expectations:
- Assertions: <list from evals.json>
- Transcript: workspace/v<N>/runs/run-<R>/transcript.md
- Outputs: workspace/v<N>/runs/run-<R>/outputs/
- Save grading to: workspace/v<N>/runs/run-<R>/grading.json

To inspect output files:
<include inspection hints from the skill, e.g.:>
<"Use python -m markitdown <file> to extract text content">
```

**Review grading.json**: Check `user_notes_summary` for uncertainties flagged by the executor. Check `eval_feedback` -- if the grader flagged lax assertions or missing coverage, update `evals.json` before continuing. Improving evals mid-loop is fine and often necessary.

**Eval quality loop**: If `eval_feedback` has suggestions, tighten assertions and rerun. Keep iterating until `eval_feedback` looks solid. Consult the user but don't block on approval for each round. When picking which eval to use for the quality loop, prefer one where the skill partially succeeds (some expectations pass, some fail) -- this gives the grader the most useful signal.

### Step 3: Blind Compare (If N > 0)

For iterations after baseline, use blind comparison. While grading tracks expectation pass rates, the comparator judges **holistic output quality** using a rubric. Two outputs might both pass all expectations, but one could still be clearly better.

**Blind A/B Protocol:**
1. Randomly assign: 50% chance v<N> is A, 50% chance v<N> is B
2. Record assignment in `workspace/grading/v<N>-vs-best/assignment.json`
3. Comparator sees only "Output A" and "Output B" -- never version names

```
Read agents/comparator.md at: <skill-builder-path>/agents/comparator.md

Blind comparison:
- Eval prompt: <the task that was executed>
- Output A: <path to one version's output>
- Output B: <path to other version's output>
- Assertions: <list from evals.json>

You do NOT know which is old vs new. Judge purely on quality.
```

**Determine winner by majority vote:**
- 2+ comparators prefer A: A wins
- 2+ comparators prefer B: B wins
- Otherwise: TIE

### Step 4: Post-hoc Analysis

After blind comparison, analyze results:

```
Read agents/analyzer.md at: <skill-builder-path>/agents/analyzer.md

Analyze:
- Winner: <A or B>
- Winner skill: workspace/<winner-version>/skill/
- Winner transcript: workspace/<winner-version>/runs/run-1/transcript.md
- Loser skill: workspace/<loser-version>/skill/
- Loser transcript: workspace/<loser-version>/runs/run-1/transcript.md
- Comparison result: <from comparator>
```

### Step 5: Update State

Update task to `completed` stage. Record results:

```python
if new_version wins majority:
    current_best = new_version

history.iterations.append({
    "version": "v<N>",
    "parent": "<previous best>",
    "expectation_pass_rate": 0.85,
    "grading_result": "won" | "lost" | "tie",
    "is_current_best": bool
})
```

### Step 6: Create New Version (If Continuing)

1. Copy current best to new version:
   ```bash
   scripts/copy_skill.py workspace/<current_best>/skill workspace/v<N+1> \
       --parent <current_best> \
       --iteration <N+1>
   ```

2. Apply improvements from analyzer suggestions

3. Create new tasks for next iteration

4. Continue loop or stop if:
   - **Time budget exhausted**: Track elapsed time, stop when approaching limit
   - **Goal achieved**: Target quality level or pass rate reached
   - **Diminishing returns**: No significant improvement in last 2 iterations
   - **User requests stop**: Check for user input between iterations

---

## Final Report

When iterations complete:

1. **Best Version**: Which version performed best (not necessarily the last)
2. **Score Progression**: Assertion pass rates across iterations
3. **Key Improvements**: What changes had the most impact
4. **Recommendation**: Whether to adopt the improved skill

Copy best skill back to main location:
```bash
cp -r workspace/<best_version>/skill/* ./
```

Check for `present_files` tool. If available:
```bash
scripts/package_skill.py <path/to/skill-folder>
```
Direct the user to the `.skill` file. If `present_files` isn't available, skip packaging.

---

## Without Subagents

Improve mode still works but with reduced rigor:

- **Single run per iteration** (not 3) -- variance analysis isn't possible with one run
- **Inline execution**: Read `agents/executor.md` and follow the procedure directly. Then read `agents/grader.md` and grade inline.
- **No blind comparison**: You can't meaningfully blind yourself. Instead, compare outputs by re-reading both versions' results and analyzing differences directly.
- **No separate analyzer**: Do the analysis inline after comparing -- identify what improved, what regressed, and what to try next.
- **Keep everything else**: Version tracking, copy-iterate-grade loop, history.json, stopping criteria all work the same.
- **Acknowledge reduced rigor**: Without independent agents, grading is less rigorous. Results are directional, not definitive.

---

## Workspace Directory Layout

```
parent-directory/
├── skill-name/                      # The skill
│   ├── SKILL.md
│   ├── evals/
│   │   ├── evals.json
│   │   └── files/
│   └── scripts/
│
└── skill-name-workspace/            # Workspace (sibling directory)
    │
    │── [Eval mode]
    ├── eval-0/
    │   ├── with_skill/
    │   │   ├── inputs/              # Staged input files
    │   │   ├── outputs/             # Skill outputs
    │   │   │   ├── transcript.md
    │   │   │   ├── user_notes.md
    │   │   │   ├── metrics.json
    │   │   │   └── [output files]
    │   │   ├── grading.json
    │   │   └── timing.json
    │   └── without_skill/
    │       └── ...
    ├── comparison.json
    ├── summary.json
    │
    │── [Improve mode]
    ├── history.json
    ├── v0/
    │   ├── META.yaml
    │   ├── skill/
    │   └── runs/
    │       ├── run-1/
    │       │   ├── transcript.md
    │       │   ├── user_notes.md
    │       │   ├── outputs/
    │       │   └── grading.json
    │       ├── run-2/
    │       └── run-3/
    ├── v1/
    │   ├── META.yaml
    │   ├── skill/
    │   ├── improvements/
    │   │   └── suggestions.md
    │   └── runs/
    └── grading/
        └── v1-vs-v0/
            ├── assignment.json
            ├── comparison-1.json
            ├── comparison-2.json
            ├── comparison-3.json
            └── analysis.json
    │
    │── [Benchmark mode]
    └── benchmarks/
        └── 2026-01-15T10-30-00/
            ├── benchmark.json
            ├── benchmark.md
            └── runs/
                ├── eval-1/
                │   ├── with_skill/
                │   │   ├── run-1/
                │   │   ├── run-2/
                │   │   └── run-3/
                │   └── without_skill/
                │       ├── run-1/
                │       ├── run-2/
                │       └── run-3/
                └── eval-2/
                    └── ...
```
