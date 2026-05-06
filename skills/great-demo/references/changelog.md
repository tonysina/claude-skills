# Changelog

## [1.0.1] - 2026-05-05

### Changed

- Renamed skill from `great-demo-method` to `great-demo` (slug, frontmatter, H1).
- Modernized dated tech references throughout:
  - "LCD cable" replaced with cable/wireless-cast-agnostic language (`references/delivery.md`).
  - "CD-ROM, DVD" canned-demo media list replaced with current options: screen recordings, interactive demo platforms (Navattic, Storylane, Reprise, Demostack), web walkthroughs (`references/special-cases.md`).
  - Ctrl-Alt-Del reboot anecdote generalized (`references/delivery.md`).
  - "Fluorescent kill switches" → "overhead lighting kill switches" (`assets/infrastructure-checklist.md`).
  - Projection checklist row updated with HDMI, USB-C, DisplayPort, AirPlay, Miracast, Chromecast options (`assets/infrastructure-checklist.md`).
  - "Word doc" / "Word document" references generalized to shared on-screen documents.
  - Stick pointer dropped (rare in 2026); replaced with annotation tools built into presentation/screen-share software (`references/delivery.md`).
- Reframed Remote Demos opening to reflect 2026 reality where remote is default for most B2B software demos rather than a degraded fallback. Preserved underlying engagement-compensation advice (`references/special-cases.md`).
- Added camera-on guidance and notification-discipline guidance to Remote Demo prep checklist (`references/special-cases.md`).

### Fixed

- Removed buzzwords from the skill's own prose that the skill itself flags as credibility-eroders ("seamless," "powerful" used non-instructively). Skill now passes its own buzzword test.

## [1.0.0] - 2026-05-05

### Added

- Initial release. Implements Peter Cohan's Great Demo! method as a product-agnostic skill.
- Mode router in SKILL.md: design, critique, qualify, delivery, special-case, glossary lookup.
- `references/design.md`: full demo-design walkthrough — Outline, Illustration, Situation Slide, Do It, Do It Again, timing, practice, rehearsal.
- `references/critique.md`: 13-item rubric for scoring an existing demo script against the Great Demo! method, with output format and worked example.
- `references/qualify.md`: pre-demo qualification — CBI/Reason/Specific Capability framework, Chain of Pain construction, Delta calculation, workflow mapping, Direct vs. Indirect Research.
- `references/delivery.md`: live-demo techniques — three question types, Not Now List, Q&A handling, language and buzzwords, mouse and pointer use, props, recovering from bugs and crashes, humor, confidence.
- `references/special-cases.md`: trade show (Menu Approach, Handoff), large unqualified groups (To Do List), remote demos (interactivity, preparation, delivery), scripted RFP demos, deployment demos, canned demos, generic demos.
- `references/glossary.md`: definitions of Cohan's terms.
- `assets/demo-information-sheet.md`: blank template for capturing CBI/Reason/Specific Capability per stakeholder, Delta, and meeting objective.
- `assets/situation-slide-template.md`: blank Situation Slide template.
- `assets/meeting-information-sheet.md`: blank meeting logistics and agenda template.
- `assets/infrastructure-checklist.md`: pre-demo hardware, software, network, AV, and facilities checklist organized into Required and Optional categories.

### Scope decisions

- Excludes evaluation management material (Cohan's Chapter 13 — Sequence of Events, success criteria, eval pricing). Different domain; can be built as a separate skill if needed.
- Product-agnostic. No BlueDolphin or other vendor-specific references. Designed to complement vendor-specific demo skills rather than overlap.
