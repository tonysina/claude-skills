# Changelog

## [1.1.0] - 2026-09-03

Fixes from the persuasion-triad skill review (`skills/persuasion-triad-review` branch).
No structural changes to the Golden Circle workflow — this skill was the strongest of
the three reviewed on craft; the fixes are attribution, self-consistency, and
cross-references, not a rewrite.

### Fixed

- **Self-violating exclusion vs. own use case.** The description excluded "general
  copywriting" while Use Case 3 is website copy — a model reading the description
  would decline the skill's own worked example. Narrowed to "product or feature copy."
- **Self-violating SEO reference.** The description excluded "SEO content," while the
  LinkedIn-length guidance justified hashtags with "per SEO best practices." Removed
  the SEO justification; hashtags are now capped at three and only on request.
- **Cross-source attribution error.** Everything was attributed to *Start with Why*
  (2009), but the Contribution/Impact WHY-statement template (Step 2a) is from the
  follow-up book, *Find Your Why* (Sinek, Mead & Docker, 2017), and the 5 Whys
  technique is Toyoda's, not Sinek's. Both now correctly attributed.
- **Non-executable quality gate.** The Glance Test instructed "ask a peer to review
  the draft" — an agent has no peer. Rewritten as a self-check the agent runs and
  reports to the user, with a peer read offered as an optional second pass.
- **Duplicated rule.** The WHY/HOW/WHAT no-labels rule was stated in both Step 5 and
  Output Guidelines. Step 5 now points to Output Guidelines instead of restating it.
- **Redundant review step.** Step 7 substantially re-ran Step 4's Celery Test audit.
  Now re-confirms Step 4's audit still holds and checks only the two things Step 4
  doesn't cover (WHY-before-WHAT ordering, sense of belonging).
- **No downstream handoff.** The skill generated prose and stopped, with no mention
  that generated prose should run through `humanizer`, or that a single closing line
  should run through `farnsworth-rhetoric`. Added a Workflow Position section.
- **No back-pointers.** `farnsworth-rhetoric` named this skill in its routing clause;
  this skill named nothing back (zero outbound cross-references). Added a "Do NOT use
  for" clause naming `good-presentations`, `farnsworth-rhetoric`, and
  `strategic-persuasion-writing` for the cases each of them should handle instead.

### Added

- Workflow Position section: downstream pipeline to `humanizer` then
  `farnsworth-rhetoric`, `beyond-obvious` at Step 2a for generating multiple WHY
  candidates instead of committing to the first that passes validation, and an
  explicit exit to `good-presentations` when the request turns out to be slides.

### Cross-repo

- `good-presentations` narrowed its colliding "thought leadership" trigger to
  "thought leadership deck/slides" and added a reciprocal "Do NOT use for thought
  leadership prose (use start-with-why)" clause, resolving the two-way collision on
  requests like "write me thought leadership content."
- `farnsworth-rhetoric`'s routing clause was corrected in the same review — see its
  own changelog.
