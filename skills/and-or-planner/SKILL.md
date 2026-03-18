---
name: and-or-planner
description: >
  Autonomous AND/OR task planner. Invoke BEFORE executing any task that meets:
  (Check 1: has multiple required subtasks that ALL must succeed — conjunctive
  requirements) OR (Check 2: has multiple valid approaches where one might fail —
  alternatives), AND (Check 3: involves 3+ discrete steps OR any external
  dependency such as a package, service, or API). Do NOT invoke for simple linear
  tasks — Check 3 alone is not sufficient. Examples that should trigger: setting
  up a database + running migrations + seeding (Check 1 + Check 3); installing
  lodash with underscore as fallback — even just 2 steps (Check 2 + external dep
  clause of Check 3); configuring multiple CI steps that all must pass.
compatibility: Requires Read, Write, Edit, Bash
allowed-tools: Read, Write, Edit, Bash
---

# AND/OR Planner

**Announce at start:** "Using and-or-planner to structure this task before execution."

## What This Does

Before executing a complex task, this skill generates an AND/OR tree that makes the task's structure explicit: AND nodes enforce that all required subtasks complete; OR nodes pre-rank alternative approaches and try them in order on failure. The tree is written to `.and-or-plan.md` and updated live during execution.

This addresses two failure modes:
- **Premature abandonment** — giving up when the first approach fails instead of trying alternatives
- **Incomplete completion** — stopping when some required subtasks succeed instead of all of them

## Step 1: Trigger Check

Run this self-assessment before generating the tree:

1. **Conjunctive check** — does this task require multiple distinct things that ALL must succeed?
2. **Alternative check** — does this task have multiple valid approaches where one might fail?
3. **Complexity floor** — does the task involve 3+ discrete steps OR any external dependency (package, service, API)?

**Fire if: (Check 1 OR Check 2) AND Check 3.**

If the trigger condition is not met, stop here — execute the task normally without a tree.

## Step 2: Generate the Tree

Analyze the task and produce an AND/OR tree. Apply these rules before writing:

**Generation rules:**
1. Root is always an AND node (the overall goal requires all subtasks)
2. OR nodes represent points where multiple approaches exist — score each child 0.0–1.0 by estimated likelihood of success in this codebase context. Highest score = tried first.
3. OR nodes must have ≥2 children. If you produce a single-child OR, collapse it — replace the OR node with its child directly.
4. AND nodes represent groups where all children must complete.
5. ACTION nodes are atomic leaf operations: a single command, file write, or verifiable step.
6. Every node must have a type and status. Every OR child must have a score.

**On generation failure** (malformed tree, file write error): warn — `⚠ AND/OR tree generation failed: [reason]. Falling back to linear execution.` — and proceed without a tree.

## Step 3: Write `.and-or-plan.md`

Check if `.and-or-plan.md` already exists:
- `Status: in_progress` → context reset; skip to Step 5 (Resume)
- `Status: completed` or `Status: failed` → archive it first: move to `.claude/and-or-history/YYYY-MM-DD-[slug].md` (create dir if needed), then overwrite

Write the file at the project root:

```markdown
# AND/OR Plan: [task description]
Generated: [ISO 8601 timestamp]
Status: in_progress

## Tree

- AND: [root goal] [PENDING]
  - OR: [sub-goal] [PENDING]
    - ACTION: [approach 1] (score: 0.9) [PENDING]
    - ACTION: [approach 2] (score: 0.6) [PENDING]
  - AND: [required group] [PENDING]
    - ACTION: [step 1] [PENDING]
    - ACTION: [step 2] [PENDING]
```

**Node statuses:** `PENDING` → `IN_PROGRESS` → `SUCCESS` | `FAILED` | `PRUNED`

`PRUNED` is applied to OR siblings that are never attempted because an earlier sibling succeeded. Do not leave them as `PENDING` — mark them `PRUNED` when the OR node resolves to `SUCCESS`.

Update node statuses in this file throughout execution. The file reflects live state — it's resumable and user-editable.

If a `.gitignore` exists, suggest adding:
```
.and-or-plan.md
.claude/and-or-history/
```

## Step 4: Execute the Tree (DFS)

Traverse depth-first. Update node status to `IN_PROGRESS` when entering, then `SUCCESS` or `FAILED` on completion.

### AND nodes
Execute all children sequentially. Mark `SUCCESS` when all children are `SUCCESS`. If any child reaches `FAILED`, mark the AND node `FAILED` immediately — do not continue remaining children. Propagate failure up to the parent.

### OR nodes
Execute children in descending score order. Mark `SUCCESS` as soon as any child succeeds — do not execute remaining children.

On child failure:
1. Announce (non-blocking, no confirmation needed):
   ```
   ⟳ Approach failed: [child name] — [brief reason]
     Trying next: [next child name] (score: [score])
   ```
2. **Rollback** side effects from the failed child (uninstall packages, revert created files)
   - **If rollback fails:** mark the OR node `FAILED`, surface to user:
     `⚠ Rollback failed for [approach]: [reason]. Cannot safely attempt next branch.`
     Stop — do not attempt remaining OR children from a dirty state.
3. Attempt next child

On child success: mark all remaining unexecuted OR siblings `PRUNED`, then mark the OR node `SUCCESS`. Do not leave untried siblings as `PENDING`.

If all OR children fail: mark OR node `FAILED`, propagate up.

### ACTION nodes
Execute the atomic operation. Verify the outcome. Mark `SUCCESS` or `FAILED`.

## Step 5: File Lifecycle

### On success (root AND reaches SUCCESS)
1. Update file: `Status: completed`
2. Move `.and-or-plan.md` → `.claude/and-or-history/YYYY-MM-DD-[task-slug].md`
   (create `.claude/and-or-history/` if it doesn't exist)

### On failure (all branches exhausted, root FAILED)
1. Update file: `Status: failed`
2. Leave `.and-or-plan.md` in place
3. Surface summary to user:
   ```
   ✗ AND/OR plan failed.

   Tried:
   - [branch 1]: [failure reason]
   - [branch 2]: [failure reason]

   Blocked on: [specific node and reason]
   To resume after editing: change `Status: failed` to `Status: in_progress` in .and-or-plan.md — Claude will detect it on next context start.
   ```

### On context reset (Step 5, Resume)
`.and-or-plan.md` exists with `Status: in_progress` at session start:

1. Announce: `Found in-progress AND/OR plan — resuming from [node name]`
2. Traverse from the last `IN_PROGRESS` node, or the first `PENDING` node if no IN_PROGRESS nodes exist
3. Within AND nodes: skip children already in `SUCCESS` state — do not re-run succeeded work
4. Continue DFS normally from the resume point

## Reference Example

**Task:** "Set up authentication — install JWT library, create middleware, add tests"

**Trigger check:**
- Check 1: Yes — install + middleware + tests must ALL succeed
- Check 2: Yes — jsonwebtoken or jose are both valid
- Check 3: Yes — 3+ steps, external package dependency
- Result: FIRE

**Generated tree:**
```markdown
# AND/OR Plan: Set up authentication
Generated: 2026-03-11T15:00:00Z
Status: in_progress

## Tree

- AND: Set up authentication [IN_PROGRESS]
  - OR: JWT library [PENDING]
    - ACTION: npm install jsonwebtoken (score: 0.9) [PENDING]
    - ACTION: npm install jose (score: 0.6) [PENDING]
  - AND: Middleware [PENDING]
    - ACTION: Create src/middleware/auth.ts [PENDING]
    - ACTION: Register middleware in src/app.ts [PENDING]
  - AND: Tests [PENDING]
    - ACTION: Write unit tests for token generation [PENDING]
    - ACTION: Write integration tests for protected routes [PENDING]
```

**Execution trace:**
1. Enter root AND → IN_PROGRESS
2. Enter OR (JWT library) → IN_PROGRESS
3. Attempt `npm install jsonwebtoken` → fails (peer dep conflict)
4. Announce: `⟳ Approach failed: npm install jsonwebtoken — peer dependency conflict with Node 22. Trying next: npm install jose (score: 0.6)`
5. Rollback: `npm uninstall jsonwebtoken` → succeeds
6. Attempt `npm install jose` → SUCCESS
7. OR node → SUCCESS
8. Enter AND (Middleware) → execute Create auth.ts → SUCCESS → Register middleware → SUCCESS → AND SUCCESS
9. Enter AND (Tests) → execute unit tests → SUCCESS → integration tests → SUCCESS → AND SUCCESS
10. Root AND → SUCCESS
11. Update Status: completed, move file to .claude/and-or-history/

Note: this trace exercises the failure-then-success OR path (first child fails, second succeeds) — both children are attempted, so no PRUNED siblings are produced in this trace. The PRUNED-on-first-success scenario (first child succeeds, remaining siblings marked PRUNED) is covered by the "Correct PRUNED status" scenario in `~/.claude/skills/and-or-planner/VERIFICATION-SCENARIOS.md`, which is the authoritative reference for that behavior.

For all failure-path traces (OR exhaustion, rollback failure, multi-level AND propagation), also treat `VERIFICATION-SCENARIOS.md` as the authoritative reference.
