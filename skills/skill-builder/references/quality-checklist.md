# Quality Checklist

Run through this checklist before finalizing a skill for upload. You can also use `scripts/quick_validate.py <path>` for automated structural checks.

## Before You Start

- [ ] Identified 2-3 concrete use cases with expected triggers, steps, and results
- [ ] Tools identified (built-in capabilities, MCP, or both)
- [ ] Reviewed example skills for patterns relevant to this use case
- [ ] Planned folder structure (which files go where)

## During Development

- [ ] Folder named in kebab-case (no spaces, underscores, or capitals)
- [ ] SKILL.md file exists with exact spelling (case-sensitive)
- [ ] YAML frontmatter has `---` delimiters on both sides
- [ ] `name` field: kebab-case, matches folder name, no "claude" or "anthropic"
- [ ] `description` field includes WHAT the skill does AND WHEN to use it
- [ ] `description` includes specific trigger phrases users would say
- [ ] No XML angle brackets (< >) anywhere in frontmatter
- [ ] **`metadata: version` is present** — new skills start at `1.0.0`; updated skills have an incremented version. This is required, not optional.
- [ ] Instructions are specific and actionable (not vague)
- [ ] Instructions explain *why* when the reasoning matters
- [ ] Error handling included for common failure modes
- [ ] Examples provided (input/output pairs for common scenarios)
- [ ] References linked clearly with guidance on when to read each one
- [ ] SKILL.md under 500 lines (detailed docs moved to references/)
- [ ] No README.md inside the skill folder

## Before Upload

- [ ] Tested triggering on obvious task descriptions
- [ ] Tested triggering on paraphrased requests (different wording, same intent)
- [ ] Verified skill does NOT trigger on unrelated topics
- [ ] Functional tests pass (valid outputs, API calls succeed, edge cases handled)
- [ ] Tested with all models you plan to use (Haiku may need more guidance; Opus may need less)
- [ ] Tool integration works correctly (if applicable)
- [ ] Compressed as .zip file (if uploading manually)

## After Upload

- [ ] Tested in real conversations with varied prompts
- [ ] Monitored for undertriggering (skill doesn't load when it should)
- [ ] Monitored for overtriggering (skill loads for unrelated queries)
- [ ] Collected user feedback on output quality
- [ ] Iterated on description and instructions based on feedback
- [ ] `references/changelog.md` updated with what changed and why
- [ ] Skills inventory spreadsheet (`tonys-claude-skills.xlsx`) updated — Version and Last Modified fields reflect current state

## Success Criteria (Aspirational Targets)

These are rough benchmarks, not precise thresholds:

**Quantitative:**
- Skill triggers on ~90% of relevant queries (test 10-20 queries)
- Workflow completes within expected tool call count
- Zero failed API calls per workflow run

**Qualitative:**
- Users don't need to prompt Claude about next steps
- Workflows complete without user correction
- Consistent results across sessions
- A new user can accomplish the task on first try with minimal guidance
