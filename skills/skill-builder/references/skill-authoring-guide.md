# Skill Authoring Guide

Read this before creating, reviewing, or improving any skill. This captures the best practices that produce high-quality, reliable skills.

## Contents

1. [Before You Start](#before-you-start)
2. [Skill Structure](#skill-structure)
3. [Writing the Description](#writing-the-description)
4. [Writing Instructions](#writing-instructions)
5. [Skill Categories and Patterns](#skill-categories-and-patterns)
6. [Common Mistakes](#common-mistakes)
7. [Troubleshooting](#troubleshooting)

---

## Before You Start

Identify 2-3 concrete use cases before writing anything. For each, define what triggers it, what steps are involved, and what success looks like. This grounds every subsequent decision -- the description, the instructions, the test cases. See [Defining Use Cases](#defining-use-cases) for the template.

---

## Skill Structure

A skill is a folder containing:

```
skill-name/
├── SKILL.md          # Required - main instructions
├── scripts/          # Optional - executable code (Python, Bash, etc.)
├── references/       # Optional - documentation loaded as needed
└── assets/           # Optional - templates, fonts, icons used in output
```

### Design Principles

**Composability**: Claude can load multiple skills simultaneously. Your skill should work well alongside others -- don't assume it's the only capability available.

**Portability**: Skills work identically across Claude.ai, Claude Code, and API. Create a skill once and it works across all surfaces, provided the environment supports any dependencies the skill requires.

### Critical Rules

**SKILL.md naming**: Must be exactly `SKILL.md` (case-sensitive). No variations (SKILL.MD, skill.md, etc.).

**Folder naming**: Use kebab-case only.
- `notion-project-setup` -- correct
- `Notion Project Setup` -- wrong (spaces)
- `notion_project_setup` -- wrong (underscores)
- `NotionProjectSetup` -- wrong (capitals)

**No README.md** inside the skill folder. All documentation goes in SKILL.md or references/. (If distributing via GitHub, put the README at the repo level for human users, outside the skill folder.)

**No XML angle brackets** (`< >`) in YAML frontmatter -- security restriction, since frontmatter appears in the system prompt.

**No "claude" or "anthropic"** in the skill name -- reserved.

### Optional YAML Fields

Beyond the required `name` and `description`, these optional fields are available:

- **license**: Use if making the skill open source (e.g., MIT, Apache-2.0)
- **compatibility** (1-500 chars): Environment requirements -- intended product, required system packages, network access needs
- **allowed-tools**: Restrict which tools the skill can access (e.g., `"Bash(python:*) Bash(npm:*) WebFetch"`)
- **metadata**: Custom key-value pairs. `version` is required (start at `1.0.0`). Other suggested fields: author, mcp-server

```yaml
---
name: my-skill
description: What it does and when to use it.
license: MIT
compatibility: Requires network access for API calls
metadata:
  author: Your Name
  version: 1.0.0
  mcp-server: your-server-name
---
```

**Security notes on YAML:** Frontmatter uses safe YAML parsing. Any standard YAML types are allowed (strings, numbers, booleans, lists, objects), as are custom metadata fields and descriptions up to 1024 characters. XML angle brackets and code execution in YAML are forbidden. Skills named with "claude" or "anthropic" prefix are reserved.

### Progressive Disclosure

Skills use three loading levels to minimize token usage:

1. **Metadata (YAML frontmatter)**: Always in context. ~100 words. Provides enough info for Claude to decide when to load the skill.
2. **SKILL.md body**: Loaded when Claude thinks the skill is relevant. Contains full instructions. Keep under 500 lines.
3. **Bundled resources** (references/, scripts/, assets/): Loaded only as needed. Scripts can execute without being loaded into context.

If approaching the 500-line limit, add a layer of hierarchy with clear pointers about where to find more detail.

**Key patterns:**
- Reference files clearly from SKILL.md with guidance on *when* to read each one
- **Keep references one level deep from SKILL.md.** Claude may only partially read files that are referenced from other referenced files (e.g., using `head -100` to preview instead of reading fully). Link all reference files directly from SKILL.md.
- For reference files over 300 lines, include a table of contents at the top
- Organize by domain when a skill supports multiple frameworks (e.g., `references/aws.md`, `references/gcp.md`)

---

## Writing the Description

The description field is how Claude decides whether to load your skill. This is the most important piece to get right.

### Required Structure

```
[What it does] + [When to use it] + [Key capabilities]
```

Must include BOTH what the skill does AND specific trigger conditions. Under 1024 characters. No XML tags.

**Always write in third person.** The description is injected into Claude's system prompt, and inconsistent point-of-view can cause discovery problems. Write "Processes Excel files and generates reports" rather than "I can help you process Excel files" or "You can use this to process Excel files."

### Good Examples

```yaml
# Specific and actionable
description: >
  Analyzes Figma design files and generates developer handoff
  documentation. Use when user uploads .fig files, asks for "design
  specs", "component documentation", or "design-to-code handoff".

# Includes trigger phrases
description: >
  Manages Linear project workflows including sprint planning, task
  creation, and status tracking. Use when user mentions "sprint",
  "Linear tasks", "project planning", or asks to "create tickets".

# Clear value proposition with negative triggers
description: >
  PayFlow payment processing for e-commerce. Handles account creation,
  payment setup, and subscription management. Use when user says
  "onboard new customer", "set up subscription", or "create PayFlow
  account". Do NOT use for general financial queries.
```

### Bad Examples

```yaml
# Too vague -- won't trigger reliably
description: Helps with projects.

# Missing trigger conditions
description: Creates sophisticated multi-page documentation systems.

# Too technical, no user-facing triggers
description: Implements the Project entity model with hierarchical relationships.
```

### Undertriggering vs. Overtriggering

Claude currently tends to **undertrigger** -- it won't load a skill when it should. To counter this, make descriptions slightly "pushy." Include more trigger phrases than you think necessary, and mention even tangential contexts where the skill would help.

If a skill triggers too often, add negative triggers:
```yaml
description: >
  Advanced data analysis for CSV files. Use for statistical modeling,
  regression, clustering. Do NOT use for simple data exploration
  (use data-viz skill instead).
```

To debug triggering, ask Claude: "When would you use the [skill name] skill?" It will quote the description back. Adjust based on what's missing.

---

## Writing Instructions

### Safety: Principle of Lack of Surprise

Skills must not contain malware, exploit code, or content that could compromise system security. A skill's contents should not surprise the user in their intent if described. Don't create misleading skills or skills designed to facilitate unauthorized access, data exfiltration, or malicious activities. Roleplay-style skills ("roleplay as an XYZ") are fine.

### Only Add What Claude Doesn't Know

The context window is a shared resource. Your skill competes for space with the system prompt, conversation history, other skills' metadata, and the user's actual request. Claude is already very capable, so challenge each piece of content: "Does Claude really need this explanation?" If a paragraph restates something Claude already knows (what PDFs are, how libraries work, basic programming concepts), cut it.

### Imperative Form

Prefer commands over descriptions:
```markdown
# Good
Run `python scripts/validate.py --input {filename}` to check format.

# Less good
The validation script can be used to check the format.
```

### Be Specific and Actionable

Every instruction should tell Claude exactly what to do, what to check, and what success looks like.

```markdown
# Good
Run `python scripts/validate.py --input {filename}` to check data format.
If validation fails, common issues include:
- Missing required fields (add them to the CSV)
- Invalid date formats (use YYYY-MM-DD)

# Bad
Validate the data before proceeding.
```

### Explain the Why

LLMs work better when they understand reasoning, not just rules. Instead of rigid directives:

```markdown
# Less effective
ALWAYS check the date format. NEVER skip validation.

# More effective
Check the date format before processing -- downstream scripts expect
YYYY-MM-DD and will silently produce wrong results with other formats.
```

### Match Specificity to Task Fragility

Not every instruction needs the same level of rigidity. Use high freedom (text-based guidance, multiple valid approaches) for tasks like code review where context drives the approach. Use low freedom (exact scripts, no parameters) for fragile operations like database migrations where only one path is safe. Default to the minimum constraint level that produces reliable results.

### Include Error Handling

Document the failures users will actually hit:

```markdown
## Common Issues

### MCP Connection Failed
If you see "Connection refused":
1. Verify MCP server is running: Settings > Extensions
2. Confirm API key is valid
3. Try reconnecting: Settings > Extensions > [Service] > Reconnect
```

For critical validations, bundle a script instead of relying on language instructions. Code is deterministic; language interpretation isn't.

### Use Examples

Show input/output pairs for common scenarios:

```markdown
## Commit message format
**Example 1:**
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

### Reference Bundled Resources Clearly

```markdown
Before writing queries, consult `references/api-patterns.md` for:
- Rate limiting guidance
- Pagination patterns
- Error codes and handling
```

### Define Output Formats Explicitly

```markdown
## Report structure
Use this template:
# [Title]
## Executive summary
## Key findings
## Recommendations
```

### Recommended Instruction Template

Adapt this structure for your skill. Replace bracketed sections with your content:

```markdown
---
name: your-skill
description: [What it does. When to use it.]
---

# Your Skill Name

## Instructions

### Step 1: [First Major Step]
Clear explanation of what happens.

Example:
\`\`\`bash
python scripts/fetch_data.py --project-id PROJECT_ID
Expected output: [describe what success looks like]
\`\`\`

(Add more steps as needed)

## Examples

### Example 1: [common scenario]
User says: "Set up a new marketing campaign"
Actions:
1. Fetch existing campaigns via MCP
2. Create new campaign with provided parameters
Result: Campaign created with confirmation link

(Add more examples as needed)

## Troubleshooting

### Error: [Common error message]
Cause: [Why it happens]
Solution: [How to fix]

(Add more error cases as needed)
```

### Model Performance Notes

If the skill requires thoroughness, add encouragement -- but put it in user prompts rather than SKILL.md when possible, since it's more effective there:

```markdown
# Performance Notes
- Take your time to do this thoroughly
- Quality is more important than speed
- Do not skip validation steps
```

---

## Skill Categories and Patterns

### Defining Use Cases

Before writing anything, define 2-3 concrete use cases. Use this format:

```
Use Case: Project Sprint Planning
Trigger: User says "help me plan this sprint" or "create sprint tasks"
Steps:
1. Fetch current project status from Linear (via MCP)
2. Analyze team velocity and capacity
3. Suggest task prioritization
4. Create tasks in Linear with proper labels and estimates
Result: Fully planned sprint with tasks created
```

Ask yourself: What does the user want to accomplish? What multi-step workflows does this require? Which tools are needed (built-in or MCP)? What domain knowledge should be embedded?

### Why MCP Users Need Skills

If you're building a skill that layers on top of an MCP server, understanding the value prop matters:

Without skills: users connect the MCP but don't know what to do next, each conversation starts from scratch, results vary because everyone prompts differently, and users blame the connector when the real issue is workflow guidance.

With skills: pre-built workflows activate automatically, tool usage is consistent and reliable, best practices are embedded in every interaction, and the learning curve drops significantly.

Think of MCP as the professional kitchen (tools, ingredients, equipment) and skills as the recipes (step-by-step instructions for creating something valuable).

### Choosing Your Approach: Problem-First vs. Tool-First

Most skills lean one direction:

- **Problem-first**: "I need to set up a project workspace" -- the skill orchestrates the right MCP calls in the right sequence. Users describe outcomes; the skill handles the tools.
- **Tool-first**: "I have Notion MCP connected" -- the skill teaches Claude the optimal workflows and best practices. Users have access; the skill provides expertise.

Knowing which framing fits your use case helps you pick the right pattern below.

### Category 1: Document & Asset Creation

For creating consistent, high-quality output (documents, presentations, apps, designs, code).

Key techniques:
- Embedded style guides and brand standards
- Template structures for consistent output
- Quality checklists before finalizing
- Typically no external tools required

### Category 2: Workflow Automation

For multi-step processes that benefit from consistent methodology.

Key techniques:
- Step-by-step workflow with validation gates
- Templates for common structures
- Built-in review and improvement suggestions
- Iterative refinement loops

### Category 3: MCP Enhancement

For workflow guidance layered on top of MCP tool access.

Key techniques:
- Coordinate multiple MCP calls in sequence
- Embed domain expertise that users would otherwise need to specify
- Provide context automatically
- Include error handling for common MCP issues

### Workflow Patterns

**Sequential orchestration**: Multi-step processes in specific order with dependencies between steps, validation at each stage, and rollback instructions.

**Multi-MCP coordination**: Workflows spanning multiple services with clear phase separation, data passing between MCPs, and centralized error handling.

**Iterative refinement**: Output quality improves with iteration. Includes explicit quality criteria, validation scripts, and stopping conditions.

**Context-aware tool selection**: Same outcome, different tools depending on context. Clear decision criteria, fallback options, and transparency about choices.

**Domain-specific intelligence**: Specialized knowledge beyond tool access. Compliance checks before action, comprehensive documentation, and audit trails.

### Structural Patterns

**Router + Sub-skill**: When a skill grows too broad — either approaching the 500-line limit or covering genuinely distinct domains — split it into a lightweight router and focused sub-skills.

**When to use this pattern:**
- A single skill serves 3+ meaningfully different use cases with different instructions, examples, and reference files for each
- SKILL.md is approaching 500 lines and the content isn't padding — it's genuinely necessary
- Users describing the same tool in different ways get inconsistent results because the instructions are trying to do too much

**How it works:**

The router is a thin skill whose only job is intent detection. It reads the user's request, identifies which domain applies, and directs Claude to load the appropriate sub-skill's SKILL.md. It carries no domain-specific instructions of its own.

The sub-skills are full, focused skills. Each has its own SKILL.md, references/, and assets/. Each can be tested, versioned, and improved independently.

```
bluedolphin/                    ← router skill folder
├── SKILL.md                    ← detects intent, routes only
├── bluedolphin-presentations/  ← sub-skill: slide creation
│   ├── SKILL.md
│   └── references/
├── bluedolphin-analysis/       ← sub-skill: EA analysis
│   ├── SKILL.md
│   └── references/
└── bluedolphin-proposals/      ← sub-skill: sales proposals
    ├── SKILL.md
    └── references/
```

**Writing the router description:**

The router's description must be broad enough to catch all the queries that belong to any of its sub-skills. It should name the domains it covers and list the combined trigger phrases across all of them.

```yaml
---
name: bluedolphin
description: >
  BlueDolphin and ValueBlue platform skills covering presentations,
  EA analysis, and sales proposals. Use when user mentions BlueDolphin,
  ValueBlue, enterprise architecture deliverables, transformation
  presentations, or asks to create slides, analyze architecture, or
  draft a proposal. Routes to the appropriate sub-skill based on
  what the user is trying to accomplish.
---
```

**Writing the router body:**

Keep it short. The router's SKILL.md should only contain routing logic — how to read intent and which sub-skill to invoke. No domain content.

```markdown
# BlueDolphin Router

Read the user's request and identify which domain applies:

- **Presentations** (slides, decks, PowerPoint, webinar): Load and follow `bluedolphin-presentations/SKILL.md`
- **EA Analysis** (architecture review, capability mapping, heat maps): Load and follow `bluedolphin-analysis/SKILL.md`
- **Proposals** (sales deck, pitch, business case): Load and follow `bluedolphin-proposals/SKILL.md`

If the request spans multiple domains, ask the user which to tackle first.
Do not attempt to handle the request yourself — always defer to the sub-skill.
```

**Writing sub-skill descriptions:**

Sub-skill descriptions can be narrow since the router is responsible for initial intent detection. Focus on what makes that sub-skill distinct from its siblings, and include a note that it's part of the parent system.

```yaml
---
name: bluedolphin-presentations
description: >
  Creates on-brand BlueDolphin/ValueBlue presentations. Sub-skill of
  the BlueDolphin router. Use directly when the user explicitly asks
  for slides, decks, or PowerPoint. Handles brand compliance, slide
  structure, and speaker notes.
---
```

**What to avoid:**

Don't over-split. Two use cases in one SKILL.md is fine — that's just good organization. The router pattern is for when the sub-domains are large enough that each would be a complete, independently useful skill on its own. If you're splitting to avoid a rewrite, you're splitting too soon.

Don't duplicate content across sub-skills. Shared reference material (brand guidelines, glossary, API patterns) belongs in the router folder as a shared `references/` file, linked from each sub-skill.

---

## Common Mistakes

**Instructions too verbose**: Keep instructions concise. Use short lists and numbered steps. Move detailed reference material to separate files.

**Critical instructions buried**: Put the most important instructions at the top. Use `## Important` or `## Critical` headers. Repeat key points if needed.

**Ambiguous language**:
```markdown
# Bad
Make sure to validate things properly

# Good
Before calling create_project, verify:
- Project name is non-empty
- At least one team member assigned
- Start date is not in the past
```

**Too many skills enabled simultaneously**: If you have 20-50+ skills enabled, consider selective enablement or grouping related capabilities into skill "packs."

**All content loaded at once**: Use progressive disclosure. Move detailed docs to references/, link to them, and keep SKILL.md focused on core instructions.

---

## Troubleshooting

### Skill Won't Upload

**"Could not find SKILL.md"**: File not named exactly SKILL.md. Rename (case-sensitive).

**"Invalid frontmatter"**: YAML formatting issue. Common mistakes:
```yaml
# Wrong - missing delimiters
name: my-skill
description: Does things

# Wrong - unclosed quotes
name: my-skill
description: "Does things

# Correct
---
name: my-skill
description: Does things
---
```

**"Invalid skill name"**: Name has spaces or capitals. Use kebab-case.

### Skill Doesn't Trigger

Revise the description field. Quick checklist:
- Is it too generic?
- Does it include trigger phrases users would actually say?
- Does it mention relevant file types?

### Skill Triggers Too Often

1. Add negative triggers ("Do NOT use for...")
2. Be more specific about scope
3. Clarify the boundary between this skill and related ones

### MCP Connection Issues

1. Verify MCP server is connected (Settings > Extensions)
2. Check authentication (API keys valid, permissions granted, OAuth refreshed)
3. Test MCP independently without the skill ("Use [Service] MCP to fetch my projects")
4. Verify tool names match (case-sensitive)

### Instructions Not Followed

1. Instructions too verbose -- trim and restructure
2. Critical instructions buried -- move to top
3. Ambiguous language -- be specific
4. For critical validations, use scripts instead of language instructions

### Large Context Issues

Symptom: Skill seems slow or responses degraded.

Causes: skill content too large, too many skills enabled simultaneously, all content loaded at once instead of using progressive disclosure.

Solutions:
- Move detailed docs to references/, link instead of inlining, keep SKILL.md under 5,000 words
- If you have 20-50+ skills enabled, evaluate whether all are necessary. Consider selective enablement or grouping related capabilities into skill "packs."
