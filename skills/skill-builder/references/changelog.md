# Changelog — skill-builder

## [1.3.0] - 2026-06-12
### Removed
- Dropped the skills inventory spreadsheet (`tonys-claude-skills.xlsx`)
  requirement from Step 9, the Improve finalization steps, and the quality
  checklist. The per-skill changelog plus the frontmatter version field
  already record each skill's state, so the external spreadsheet was
  redundant. Step 9 renamed from "Update Skills Inventory" to "Update the
  Changelog."

## [1.2.0] - 2026-02-24
### Added
- `references/skill-authoring-guide.md`: New "Structural Patterns" section with Router + Sub-skill pattern, including when to use it, folder structure, router description and body guidance, sub-skill description guidance, and what to avoid (over-splitting, duplicating shared content)

## [1.1.0] - 2026-02-19
### Added
- Step 9 (Update Skills Inventory) added to Create workflow: requires updating `tonys-claude-skills.xlsx` and `references/changelog.md` after every create or improve session
- Version bump instructions added to Improve workflow with explicit 3-step requirement (version → changelog → spreadsheet)
- `references/changelog.md` format defined and required for all skills

### Changed
- Version field elevated from optional/suggested to **required** in frontmatter — enforced in Step 4 with explicit "do not create a skill without it" language
- Quality checklist: version check moved from "After Upload" to "During Development" so it's caught before finalization
- Spreadsheet and changelog update checks added to "After Upload" section of quality checklist
- `skill-authoring-guide.md`: version marked as required, not just suggested

## [1.0.0] - 2026-02-19
### Added
- Initial baseline version assigned as part of bulk versioning across all user skills
