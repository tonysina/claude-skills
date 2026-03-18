---
name: skill-builder
description: >
  Create new skills, improve existing skills, and measure skill performance.
  Use when users want to create a skill from scratch, turn a conversation into
  a reusable skill, update or optimize an existing skill, run evals to test a
  skill, or benchmark skill performance with variance analysis. Trigger on
  phrases like "build a skill", "make a skill", "create a skill for",
  "turn this into a skill", "improve my skill", "test my skill",
  "evaluate this skill", "skill performance", "skill benchmark",
  or any mention of SKILL.md, skill folders, or skill development workflow.
metadata:
  version: 1.2.0
---

# Skill Builder

Build, test, and improve skills through an iterative workflow.

## Core Workflow

The skill development process:

1. Define what you want the skill to do and roughly how it should do it
2. Write a draft of the skill
3. Create a few test prompts and run Claude-with-access-to-the-skill on them
4. Evaluate the results (automated evals or human review -- both are valid)
5. Rewrite the skill based on evaluation feedback
6. Repeat until satisfied
7. Expand the test set and try again at larger scale

Your job is to figure out where the user is in this process and help them move forward. Maybe they want to start from scratch, or maybe they already have a draft and need the eval/iterate loop. Be flexible -- if the user says "just vibe with me," do that instead of running formal evals.

## Building Blocks

The skill-builder operates on composable building blocks:

| Building Block | Input | Output | Agent |
|-----------|-------|--------|-------|
| **Eval Run** | skill + eval prompt + files | transcript, outputs, metrics | `agents/executor.md` |
| **Grade Expectations** | outputs + expectations | pass/fail per expectation | `agents/grader.md` |
| **Blind Compare** | output A, output B, eval prompt | winner + reasoning | `agents/comparator.md` |
| **Post-hoc Analysis** | winner + skills + transcripts | improvement suggestions | `agents/analyzer.md` |

These blocks combine into four modes:

| Mode | Purpose | Workflow |
|------|---------|----------|
| **Create** | Interactive skill development | Interview > Research > Draft > Run > Refine |
| **Improve** | Iteratively optimize skill | Executor > Grader > Comparator > Analyzer > Apply |
| **Eval** | Test skill performance | Executor > Grader > Results |
| **Benchmark** | Standardized measurement (requires subagents) | 3x runs per config > Aggregate > Analyze |

See `references/mode-diagrams.md` for visual workflow diagrams.

---

## Environment Capabilities

Check whether you can spawn subagents (independent agents that execute tasks in parallel). This determines how modes execute:

- **With subagents**: Delegate to executor, grader, comparator, analyzer agents in parallel when tasks are independent.
- **Without subagents**: Read agent reference files and follow procedures inline, sequentially. Acknowledge reduced rigor since the same context that executes also grades.

---

## Creating a Skill

Before writing anything, read `references/skill-authoring-guide.md` for best practices on structure, descriptions, instructions, and common patterns.

### Step 1: Capture Intent

Start by understanding what the user needs. The current conversation might already contain a workflow to capture (e.g., "turn this into a skill"). If so, extract answers from conversation history first: the tools used, step sequence, corrections the user made, input/output formats observed.

Gather these answers (confirm with user before proceeding):

1. What should this skill enable Claude to do?
2. When should this skill trigger? (specific user phrases and contexts)
3. What's the expected output format?
4. Are there 2-3 concrete use cases this skill should handle?
5. Should we set up test cases? (suggest the appropriate default based on whether outputs are objectively verifiable vs. subjective)

For each use case, define it concretely:

```
Use Case: [Name]
Trigger: User says "[phrase1]" or "[phrase2]"
Steps:
1. [First action]
2. [Second action]
Result: [What success looks like]
```

### Step 2: Interview and Research

Proactively ask about edge cases, input/output formats, example files, success criteria, and dependencies. Check available MCPs for research (docs, similar skills, best practices). Come prepared with context to reduce burden on the user.

### Step 3: Initialize

Run the initialization script:

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

This creates SKILL.md with frontmatter, plus scripts/, references/, and assets/ directories.

### Step 4: Write Frontmatter

The frontmatter is how Claude decides whether to load a skill. This is the single most important part to get right.

```yaml
---
name: skill-name-in-kebab-case
description: >
  [What it does]. [When to use it with specific trigger phrases].
  Use when user mentions [phrase1], [phrase2], [phrase3], or asks
  to [action1] or [action2]. Do NOT use for [negative triggers].
metadata:
  version: 1.0.0
---
```

**Version is required.** Every new skill must include `metadata: version: 1.0.0` in the frontmatter. Do not create a skill without it. This is not optional.

Rules for the `name` field:
- Kebab-case only, no spaces, no capitals
- Must match the folder name
- Cannot contain "claude" or "anthropic" (reserved)

Rules for the `description` field:
- Must include both WHAT and WHEN (trigger conditions)
- Under 1024 characters, no XML angle brackets (< >)
- Include specific phrases users would actually say
- Mention relevant file types if applicable
- Lean slightly "pushy" -- Claude tends to undertrigger, so be generous with trigger conditions
- Add negative triggers if needed to prevent overtriggering

Optional fields: `license`, `compatibility`, `allowed-tools`, `metadata` (author, version, mcp-server). See `references/skill-authoring-guide.md` for details on each.

See `references/skill-authoring-guide.md` for good/bad description examples.

### Step 5: Write Instructions

Write the skill body in Markdown using imperative form. Follow these principles:

**Progressive disclosure**: Keep SKILL.md under 500 lines. Move detailed reference material to `references/` and link clearly with guidance on when to read each file. The three levels are:
1. Metadata (name + description) -- always in context (~100 words)
2. SKILL.md body -- loaded when skill triggers (<500 lines)
3. Bundled resources (references/, scripts/, assets/) -- loaded as needed

**Be specific and actionable**: Tell Claude exactly what to run, what to check, and what success looks like. Prefer code over vague language.

```markdown
# Good
Run `python scripts/validate.py --input {filename}` to check format.
If validation fails, common issues:
- Missing required fields (add them to the CSV)
- Invalid date formats (use YYYY-MM-DD)

# Bad
Validate the data before proceeding.
```

**Explain the why**: Today's LLMs are smart. They have good theory of mind and can go beyond rote instructions when they understand the reasoning. If you find yourself writing ALWAYS or NEVER in all caps or using rigid structures, reframe and explain why the thing matters. That's more effective than shouting.

**Include error handling**: Document common failures and how to recover. For critical validations, consider bundling a script that performs checks programmatically -- code is deterministic; language interpretation isn't.

**Use examples**: Show input/output pairs for the most common scenarios. This grounds Claude's understanding of what "good" looks like.

**No README.md**: All documentation goes in SKILL.md or references/. Don't include README.md, INSTALLATION_GUIDE.md, CHANGELOG.md, or similar files. Skills are for AI agents, not human onboarding.

### Step 6: Validate

Before presenting the skill, run through `references/quality-checklist.md` to catch common issues.

Run the quick validation script:

```bash
scripts/quick_validate.py <path/to/skill-folder>
```

### Step 7: Test

**Pro Tip: Iterate on a single task before expanding.** The most effective skill creators iterate on a single challenging task until Claude succeeds, then extract the winning approach into the skill. This leverages in-context learning and provides faster signal than broad testing. Once you have a working foundation, expand to multiple test cases for coverage.

Skills can be tested at three levels of rigor -- pick what matches your needs:
- **Manual testing in Claude.ai**: Run queries directly and observe behavior. Fast iteration, no setup.
- **Scripted testing in Claude Code**: Automate test cases for repeatable validation across changes.
- **Programmatic testing via skills API**: Build evaluation suites that run systematically against defined test sets.

Come up with 2-3 realistic test prompts -- the kind of thing a real user would say. Share them with the user for confirmation, then run them.

**Always have something cooking.** Every time the user adds an example or input:
1. Immediately start running it -- don't wait for full specification
2. Show outputs in workspace -- tell user: "The output is at X, take a look"
3. Run first tests in main agent loop (not subagent) so user sees the transcript
4. Seeing what Claude does helps the user understand and refine requirements

If the user wants formal evals, create `evals/evals.json`:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's task prompt",
      "expected_output": "Description of expected result",
      "files": [],
      "assertions": [
        "The output includes X",
        "The skill correctly handles Y"
      ]
    }
  ]
}
```

Initialize with `scripts/init_json.py evals evals/evals.json` and validate with `scripts/validate_json.py evals/evals.json`. See `references/schemas.md` for the full schema.

### Step 8: Package and Present

Check whether you have access to the `present_files` tool. If you do:

```bash
scripts/package_skill.py <path/to/skill-folder>
```

Direct the user to the resulting `.skill` file path so they can install it. If you don't have `present_files`, skip this step.

For distribution beyond personal use: host on GitHub with a clear README (at the repo level, not inside the skill folder), include example usage and screenshots, and if the skill enhances an MCP integration, link to it from your MCP documentation. When positioning the skill, focus on outcomes ("set up project workspaces in seconds") rather than implementation details ("folder containing YAML frontmatter").

### Step 9: Update Skills Inventory

After creating or improving any skill, update the user's skills inventory spreadsheet and the skill's changelog. These steps are required, not optional.

**Update the spreadsheet** (`tonys-claude-skills.xlsx`):
- If creating a new skill: add a new row with Skill Name, Description, Triggers, Output, Last Modified (today's date), and Version
- If improving a skill: update the Version and Last Modified fields for that skill's row

**Update the skill changelog** by appending to `references/changelog.md` inside the skill folder (create it if it doesn't exist):

```markdown
## [version] - YYYY-MM-DD
### Changed
- [What was changed and why]

## [previous version] - YYYY-MM-DD
### Added
- [Initial release notes]
```

Use the same semver convention: patch (x.x.1) for small fixes, minor (x.1.0) for new capabilities, major (x.0.0) for rewrites.

---

## Improving a Skill

When the user asks to improve a skill, ask:
1. **Which skill?** Identify the skill to improve.
2. **How much time?** How long can Claude spend iterating?
3. **What's the goal?** Target quality level, specific issues, or general improvement.

Then autonomously iterate using the building blocks (run, grade, compare, analyze). When improvements are finalized, you must:

1. **Increment the version** in the skill's frontmatter metadata. This is required — do not finalize improvements without updating the version. Convention: patch (x.x.1) for small fixes or wording tweaks, minor (x.1.0) for new capabilities or meaningful additions, major (x.0.0) for structural rewrites.
2. **Update `references/changelog.md`** inside the skill folder with what changed and why (create the file if it doesn't exist).
3. **Update the skills inventory spreadsheet** (`tonys-claude-skills.xlsx`) with the new version number and today's date in the Last Modified field.

### Writing Philosophy for Improvements

The authoring guide (`references/skill-authoring-guide.md`) covers general writing principles. During improvements specifically, keep these priorities in mind:

1. **Generalize from feedback.** The goal is skills that work across many prompts, not just the test set. If you're making fiddly, overfitting changes, try branching out with different metaphors or working patterns.

2. **Keep the prompt lean.** Read transcripts, not just outputs -- if the skill makes Claude waste time on unproductive steps, cut the parts causing that.

3. **Understand the user's intent.** If feedback is terse or frustrated, work to understand what they actually need and encode that reasoning into the skill. ALL-CAPS directives are a yellow flag -- reframe with reasoning instead.

### Detailed Iteration Workflow

Read `references/improve-mode.md` for the full setup, iteration loop, comparison protocol, and final report procedures.

Read `references/schemas.md` for JSON output structures used in grading, history, comparison, and analysis.

---

## Eval Mode

Run individual evals to test skill performance and grade expectations.

Read `references/eval-mode.md` and `references/schemas.md` before running evals.

Use Eval mode when:
- Testing a specific eval case
- Comparing with/without skill on a single task
- Quick validation during development

The workflow: Setup > Check Dependencies > Prepare > Execute > Grade > Display Results

Without subagents, execute and grade sequentially. Read the agent reference files (`agents/executor.md`, `agents/grader.md`) and follow procedures directly.

---

## Benchmark Mode

Standardized performance measurement with variance analysis. **Requires subagents.**

Read `references/benchmark-mode.md` and `references/schemas.md` before running benchmarks.

Use Benchmark mode when:
- Understanding overall skill performance
- Comparing across models
- Tracking performance over time
- Validating whether a skill adds value

Key differences from Eval: runs all evals, 3 times each per configuration, always includes no-skill baseline, uses most capable model for analysis.

---

## Workspace Structure

Workspaces are created as sibling directories to the skill being worked on. See `references/improve-mode.md` for the full directory layout including eval, improve, and benchmark structures.

Key output files:
- `transcript.md` - Execution log from executor
- `user_notes.md` - Uncertainties and workarounds flagged by executor
- `metrics.json` - Tool calls, output size, step count
- `grading.json` - Assertion pass/fail, notes, user_notes summary
- `comparison-N.json` - Blind rubric-based comparison
- `history.json` - Version progression with pass rates and winners

---

## Task Tracking

Each eval run becomes a task with stage progression:

```
pending > planning > implementing > reviewing > verifying > completed
          (prep)     (executor)     (grader)    (validate)
```

Create tasks per eval run and update stages as work progresses. For comparison tasks, stages map to: gathering outputs > spawning comparators > tallying votes > handling ties > declaring winner.

---

## Coordinator Responsibilities

1. **Delegate to subagents when available; execute inline otherwise.** In Improve, Eval, and Benchmark modes, use subagents for executor/grader work when possible.
2. **Create mode exception**: Run examples in main loop so user sees the transcript (interactive feedback matters more than consistency).
3. **Use independent grading when possible.** Without subagents, grade inline but acknowledge the limitation.
4. **Track progress with tasks.** Create tasks, update stages, mark complete.
5. **Track best version** -- the best performer, not the latest iteration.
6. **Run multiple times for variance** -- 3 runs per config with subagents; 1 run otherwise.
7. **Parallelize independent work** when subagents are available.
8. **Report results clearly** with evidence and metrics.
9. **Review user_notes** for issues that passed expectations might miss.
10. **Capture execution metrics** in Benchmark mode.
11. **Use most capable model** for analysis.

---

## Delegating Work

**With subagents**: Spawn an independent agent with the reference file instructions. Include the reference file path in the prompt. When tasks are independent (like 3 runs of the same version), spawn all subagents in the same turn for parallelism.

**Without subagents**: Read the agent reference file and follow the procedure directly in your main loop. Execute each step sequentially.

---

## Communicating with the User

The skill-builder attracts users across a wide range of technical familiarity. The power of Claude is inspiring people who have never opened a terminal to start building things, alongside experienced developers. Pay attention to context cues to calibrate your language:

- "evaluation" and "benchmark" are borderline but OK for most users
- "JSON" and "assertion" -- wait for cues that the user knows these terms before using them without explanation
- Briefly explain terms if you're in doubt

When in doubt, err toward clarity over precision. A user who feels respected and understood will iterate further than one who feels talked down to or lost.

---

## Reference Index

| File | When to read |
|------|-------------|
| `references/skill-authoring-guide.md` | Before creating or reviewing any skill |
| `references/quality-checklist.md` | Before finalizing a skill for upload |
| `references/improve-mode.md` | When running Improve mode workflows |
| `references/eval-mode.md` | When running Eval mode |
| `references/benchmark-mode.md` | When running Benchmark mode |
| `references/schemas.md` | When working with JSON output structures |
| `references/mode-diagrams.md` | For visual workflow diagrams |
| `agents/executor.md` | When executing skill runs |
| `agents/grader.md` | When grading expectations |
| `agents/comparator.md` | When doing blind A/B comparisons |
| `agents/analyzer.md` | When analyzing comparison results |
