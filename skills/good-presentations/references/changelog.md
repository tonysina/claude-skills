# Changelog

## [1.2.0] - 2026-09-03

Two fixes from the persuasion-triad skill review (`skills/persuasion-triad-review`
branch), shipped together since the version field wasn't bumped between them.

### Fixed

- **Broken hard dependency in Claude Code.** Step 7's only build path was
  `/mnt/skills/public/pptx/SKILL.md`, which exists in the claude.ai/API container but
  not in Claude Code, leaving the skill unable to produce a deck at all in that
  environment. Step 7 now branches on environment: the managed pptx skill on claude.ai,
  or a detect -> install -> fallback sequence (`python-pptx` / `pptxgenjs`) in Claude
  Code, re-deriving the QA checks by hand since there's no QA rules file to read
  outside the managed path. Falls back to a structured outline if no library can be
  installed, rather than improvising unverifiable pptx code.
- **Trigger collision with `start-with-why`.** The bare trigger phrase "thought
  leadership" fired this skill on requests for thought-leadership *prose*, not just
  decks, colliding with `start-with-why`'s identical claim to that territory — neither
  skill's exclusions mentioned the other's medium. Narrowed the trigger to "thought
  leadership deck" / "thought leadership slides" and added "Do NOT use for thought
  leadership prose or articles (use start-with-why)." Also added a reciprocal note for
  sharpening an individual slide title or closing line (use `farnsworth-rhetoric`).
