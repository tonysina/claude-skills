# Contributing to Claude Skills

Thanks for contributing! This guide explains how to add, test, and build skills.

## Adding a New Skill

### 1. Create the skill directory

```bash
mkdir -p skills/your-skill-name
```

### 2. Write the skill definition

Create `skills/your-skill-name/SKILL.md` with the skill's metadata and prompt:

```markdown
---
name: your-skill-name
description: >
  A concise one-paragraph description of what the skill does.
  Mention when to use it and what it triggers on.
metadata:
  version: 1.0.0
---

# Your Skill Title

[Full skill content and instructions...]
```

**Guidelines:**
- Keep the description under 150 characters — it appears in skill selection UIs
- List trigger phrases in the description (e.g., "Triggers on 'generate', 'create', 'design'")
- Make it clear what kind of input the skill expects
- Reference official docs or frameworks when applicable

### 3. Add reference materials (optional)

If your skill references external frameworks, best practices, or examples, store them in:

```
skills/your-skill-name/
├── SKILL.md
├── references/
│   ├── framework-guide.md
│   └── example.pdf
└── assets/
    └── template.md
```

These files are included in the compiled `.skill` file for offline access.

### 4. Build the .skill file

Run the build script to create the compiled `.skill` file:

```bash
./scripts/build-skills.sh your-skill-name
```

This generates `dist/your-skill-name.skill` — a ZIP archive containing your SKILL.md and any assets/references.

Or build all skills:

```bash
./scripts/build-skills.sh
```

### 5. Update the README

Add your skill to the skills table in alphabetical order:

```markdown
| [your-skill-name](skills/your-skill-name/) | Brief description | ✅/⚠️/❌ | ✅/⚠️/❌ | [.skill](dist/your-skill-name.skill) |
```

**Support levels:**
- ✅ Full support — works in both Claude Code and claude.ai
- ⚠️ Partial — requires Claude Code tools (file system, shell, etc.) for some features
- ❌ Claude Code only — cannot run on claude.ai

### 6. Commit your changes

```bash
git checkout -b add-your-skill-name
git add skills/your-skill-name/ dist/your-skill-name.skill README.md
git commit -m "feat: add your-skill-name skill

[Description of what the skill does and when to use it]

Co-Authored-By: Claude <noreply@anthropic.com>"

git push -u origin add-your-skill-name
```

Then open a pull request.

## Claude Code vs claude.ai

Skills work differently depending on the platform:

| Aspect | Claude Code | claude.ai |
|--------|------------|-----------|
| Installation | Copy skill folder to `~/.claude/skills/` | Upload `.skill` file via Settings → Customize → Skills |
| File access | ✅ Full (read/write) | ❌ None |
| Shell commands | ✅ Full | ❌ None |
| Web requests | ✅ Full | ✅ Limited (no auth headers) |
| Real-time iteration | ✅ Skills reload automatically | ⚠️ Requires re-upload after edits |

**Mark as ⚠️ (Partial) if** your skill:
- Uses file operations (Read, Write, Edit, Glob)
- Runs shell commands (Bash)
- Needs task management (TaskCreate, TaskUpdate)
- Requires git operations

**Mark as ❌ (Claude Code only) if** your skill:
- Depends on shell access for core functionality
- Reads/writes files as its primary purpose
- Requires interactive terminal sessions

## Workflow Tips

### Test your skill locally

1. Copy the skill folder into `~/.claude/skills/`:
   ```bash
   cp -r skills/your-skill-name ~/.claude/skills/
   ```

2. Restart Claude Code (the skill reloads automatically)

3. Invoke it with `/your-skill-name` and iterate

4. Once satisfied, rebuild the `.skill` file:
   ```bash
   ./scripts/build-skills.sh your-skill-name
   ```

### Rebuilding after edits

Any time you modify `SKILL.md` or add/remove files in `assets/` or `references/`, rebuild:

```bash
./scripts/build-skills.sh your-skill-name
```

Then commit both the source and the rebuilt `.skill` file.

### Testing the writing skills

`humanizer`, `farnsworth-rhetoric`, and `human-narrative` share one pipeline and reference each other by `humanizer`'s stable pattern IDs (the table at the top of `skills/humanizer/SKILL.md`). Two test aids exist:

- **`scripts/scan-ai-tells.py`** — deterministic scan. Reads `humanizer`'s watch lists live from its SKILL.md, so word-list edits need no script change; the hand-derived `CONSTRUCTIONS` regexes and ID labels in the script do. Reports flag density, distinct patterns hit, em dash proximity, anaphora runs, triads, and word count against `farnsworth-rhetoric`'s figure budget. Text inside code, blockquotes, watch-list lines, and short quoted strings is ignored by default (`--keep-quotes` to include it), so a document that discusses a pattern is not scored as using it.
- **`tests/cases/`** — smoke-test fixtures. `NN-name-IN.txt` is the input, `NN-name-OUT.txt` is the expected output. Negative cases have byte-identical IN and OUT because the correct output is no change. Not an automated suite.

To re-run:

```bash
# always score the positive control first; a scan that reports clean on everything
# is indistinguishable from a broken scan
./scripts/scan-ai-tells.py tests/cases/00-control-v1.0.0-output.txt tests/cases/*-OUT.txt

# self-check: humanizer's own prose should return 0 hits
./scripts/scan-ai-tells.py skills/humanizer/SKILL.md
```

After editing a `humanizer` pattern, grep the branch for the pattern's ID and check the scan's `CONSTRUCTIONS` table. Never insert, merge, or renumber a pattern without keeping its ID.

### Pull requests

- Keep PRs focused — one skill per PR unless they're tightly related
- Include a test plan: "Tested with `/your-skill-name` on [task description]"
- Ensure the `.skill` file is committed (CI checks this)
- Link to relevant docs, frameworks, or research if applicable

## Build Automation

GitHub Actions automatically:
1. Builds `.skill` files when `skills/` changes
2. Verifies all `.skill` files are present and up-to-date
3. Fails the build if source was modified without rebuilding

This ensures `dist/` is always in sync with `skills/`.

## Questions?

Check the [official skill authoring guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) or review existing skills for examples.
