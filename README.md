# Claude Skills

A collection of 12 custom skills for Claude — covering writing, thinking, research, and AI design.

Skills extend Claude with specialized behaviors invoked via slash commands (e.g. `/humanizer`, `/split-pdf`). Most skills are pure prompting and work in both Claude Code and claude.ai. A few require Claude Code-specific tools (file system, shell) and won't work on claude.ai.

---

## Installation

### Claude Code (recommended)

```bash
# Clone the repo
git clone https://github.com/tonysina/claude-skills.git

# Copy one or more skill folders into Claude's skills directory
cp -r claude-skills/skills/humanizer ~/.claude/skills/
cp -r claude-skills/skills/split-pdf ~/.claude/skills/

# Restart Claude Code — skills are available immediately
```

Invoke with a slash command: `/humanizer`, `/split-pdf`, etc.

### claude.ai web

1. Download the `.skill` file from `dist/` (e.g. [`humanizer.skill`](dist/humanizer.skill))
2. Go to [claude.ai](https://claude.ai) → open any Project
3. Click **"+"** → **"Upload a skill"** → select the `.skill` file
4. Enable it via **Settings → Customize → Skills**

---

## Skills

| Skill | Description | Claude Code | claude.ai | Download |
|-------|-------------|:-----------:|:---------:|----------|
| [and-or-planner](skills/and-or-planner/) | Autonomous AND/OR task planner — breaks complex tasks into conjunctive and alternative subtasks before execution | ✅ | ⚠️ | [.skill](dist/and-or-planner.skill) |
| [beyond-obvious](skills/beyond-obvious/) | Generates diverse options beyond predictable defaults using verbalized sampling | ✅ | ✅ | [.skill](dist/beyond-obvious.skill) |
| [beyond-the-summary](skills/beyond-the-summary/) | Extracts non-obvious insights, tensions, and actionable implications from documents | ✅ | ✅ | [.skill](dist/beyond-the-summary.skill) |
| [farnsworth-rhetoric](skills/farnsworth-rhetoric/) | Applies classical rhetorical techniques to make writing more memorable and persuasive | ✅ | ✅ | [.skill](dist/farnsworth-rhetoric.skill) |
| [good-presentations](skills/good-presentations/) | Creates persuasive, rhetorically structured presentations using the Rhetoric of Decks framework | ✅ | ✅ | [.skill](dist/good-presentations.skill) |
| [humanizer](skills/humanizer/) | Removes AI writing patterns from text to make it sound more natural and human-written | ✅ | ✅ | [.skill](dist/humanizer.skill) |
| [intelligence-flow-architecture](skills/intelligence-flow-architecture/) | Designs how humans and AI collaborate in products, workflows, and processes | ✅ | ✅ | [.skill](dist/intelligence-flow-architecture.skill) |
| [markdown-fetch](skills/markdown-fetch/) | Fetches web content as clean markdown, reducing token usage by up to 80% | ✅ | ⚠️ | [.skill](dist/markdown-fetch.skill) |
| [skill-builder](skills/skill-builder/) | Creates and improves skills — turns conversations or existing prompts into reusable skills | ✅ | ✅ | [.skill](dist/skill-builder.skill) |
| [split-pdf](skills/split-pdf/) | Downloads, splits, and deeply reads PDFs — producing structured notes for implementation and content | ✅ | ❌ | [.skill](dist/split-pdf.skill) |
| [start-with-why](skills/start-with-why/) | Creates inspiring content using Simon Sinek's Golden Circle (WHY → HOW → WHAT) | ✅ | ✅ | [.skill](dist/start-with-why.skill) |
| [strategic-persuasion-writing](skills/strategic-persuasion-writing/) | Generates persuasive language scripts using advanced behavioral influence models (FATE, PCP, Six-Axis) | ✅ | ✅ | [.skill](dist/strategic-persuasion-writing.skill) |

✅ Full support · ⚠️ Partial (some features require Claude Code tools) · ❌ Claude Code only

---

## Building Your Own Skills

See [`docs/skill-creation-best-practices/`](docs/skill-creation-best-practices/) for guides on writing, structuring, and packaging your own skills.

Start with [`The-Complete-Guide-to-Building-Skills-for-Claude.md`](docs/skill-creation-best-practices/The-Complete-Guide-to-Building-Skills-for-Claude.md).

---

## License

MIT
