# Claude Skills

A collection of custom skills for Claude — covering writing, thinking, research, and AI design.

Skills extend Claude with specialized behaviors invoked via slash commands (e.g. `/humanizer`, `/split-pdf`). Most skills are pure prompting and work in both Claude Code and claude.ai. A few require Claude Code-specific tools (file system, shell) and won't work on claude.ai.

---

## Installation

### On the Web (claude.ai)

1. Download the `.skill` file from `dist/` (e.g. [`humanizer.skill`](dist/humanizer.skill))
2. Go to **Settings → Customize → Skills** → click **"+"** → upload the `.skill` file

### On Claude Code

```bash
# Clone the repo
git clone https://github.com/tonysina/claude-skills.git

# Copy one or more skill folders into Claude's skills directory
cp -r claude-skills/skills/humanizer ~/.claude/skills/
cp -r claude-skills/skills/split-pdf ~/.claude/skills/

# Restart Claude Code — skills are available immediately
```

Invoke with a slash command: `/humanizer`, `/split-pdf`, etc.
---

## Skills

| Skill | Description | Claude Code | claude.ai | Download |
|-------|-------------|:-----------:|:---------:|----------|
| [and-or-planner](skills/and-or-planner/) | Autonomous AND/OR task planner — breaks complex tasks into conjunctive and alternative subtasks before execution | ✅ | ⚠️ | [.skill](dist/and-or-planner.skill) |
| [beyond-obvious](skills/beyond-obvious/) | Generates diverse options beyond predictable defaults using verbalized sampling | ✅ | ✅ | [.skill](dist/beyond-obvious.skill) |
| [beyond-the-summary](skills/beyond-the-summary/) | Extracts non-obvious insights, tensions, and actionable implications from documents | ✅ | ✅ | [.skill](dist/beyond-the-summary.skill) |
| [farnsworth-rhetoric](skills/farnsworth-rhetoric/) | Applies classical rhetorical figures to existing writing under a strict dosage budget — antithesis, isocolon, antimetabole, hypophora, Saxon finish | ✅ | ✅ | [.skill](dist/farnsworth-rhetoric.skill) |
| [great-demo](skills/great-demo/) | Apply Peter Cohan's Great Demo! method to design, critique, and qualify software demonstrations | ✅ | ⚠️ | [.skill](dist/great-demo.skill) |
| [human-narrative](skills/human-narrative/) | Audits narrative structure for AI patterns that survive surface editing — thematic over-explanation, embodied emotion, tidy resolution, linear time | ✅ | ✅ | [.skill](dist/human-narrative.skill) |
| [humanizer](skills/humanizer/) | Removes AI writing patterns from text — 20 source-checked patterns with stable IDs, a measured finding threshold, and model-residue detection | ✅ | ✅ | [.skill](dist/humanizer.skill) |
| [intelligence-flow-architecture](skills/intelligence-flow-architecture/) | Designs how humans and AI collaborate in products, workflows, and processes | ✅ | ✅ | [.skill](dist/intelligence-flow-architecture.skill) |
| [markdown-fetch](skills/markdown-fetch/) | Fetches web content as clean markdown, reducing token usage by up to 80% | ✅ | ⚠️ | [.skill](dist/markdown-fetch.skill) |
| [skill-builder](skills/skill-builder/) | Creates and improves skills — turns conversations or existing prompts into reusable skills | ✅ | ✅ | [.skill](dist/skill-builder.skill) |
| [source-check](skills/source-check/) | Verifies factual claims against primary sources — one isolated agent per claim, consolidated into a report and a corrected draft | ✅ | ⚠️ | [.skill](dist/source-check.skill) |
| [split-pdf](skills/split-pdf/) | Downloads, splits, and deeply reads PDFs — producing structured notes for implementation and content | ✅ | ❌ | [.skill](dist/split-pdf.skill) |
| [start-with-why](skills/start-with-why/) | Creates inspiring content using Simon Sinek's Golden Circle (WHY → HOW → WHAT) | ✅ | ✅ | [.skill](dist/start-with-why.skill) |
| [strategic-persuasion-writing](skills/strategic-persuasion-writing/) | Generates persuasive language scripts using behavioral influence models (FATE, PCP, Six-Axis) from Chase Hughes' The Behavior Ops Manual | ✅ | ✅ | [.skill](dist/strategic-persuasion-writing.skill) |

✅ Full support · ⚠️ Partial (some features require Claude Code tools) · ❌ Claude Code only

---

## Retired skills

### good-presentations (removed November 2026)

This skill built decks around a fixed rhetorical framework: every title a claim, a three-act arc, a Devil's Advocate slide, and a one-sentence closing line. It was retired for these reasons:

- **The prescribed patterns pushed slide copy toward slogans.** A title that must be a claim, a closing that must be one memorable sentence, and a rule to break the pattern once for effect produce the clipped, dramatic style that reads badly when spoken in a live demo.
- **It conflicted with the demo skills.** It said never to open with an agenda, while great-demo reads an outline aloud. It said to close on one sentence with no summary, while great-demo requires a recap of each capability.
- **Nothing was left for it to own.** It excluded brand-specific decks, so BlueDolphin decks never fell under it. The pptx skill already covers the build mechanics, and farnsworth-rhetoric covers sharpening an individual title or closing line.

For deck work, use the pptx skill for mechanics and plan the argument directly. The last version is in git history before the commit that removed it.

---

## Building Your Own Skills

- [Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — official Anthropic docs
- [Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — official Anthropic docs
- [The Complete Guide to Building Skills for Claude](https://gist.github.com/joyrexus/ff71917b4fc0a2cbc84974212da34a4a) — comprehensive community walkthrough

---

## License

MIT
