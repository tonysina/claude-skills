# Changelog

## [2.0.0] - 2026-11-02

The skill no longer prescribes a demo flow. It keeps the parts of Cohan's
method that diagnose and plan (CBI/Reason/Specific Capability, the Chain of
Pain, the Delta, the Not Now List) and drops the parts that dictate how a
demo is structured and delivered.

### Removed
- Prescribed flow: Situation Slide, Illustration, Do It, Do It Again, the
  recap Summary, and the read-aloud Outline Introduction. Removed from
  `SKILL.md`, `references/design.md`, `references/critique.md`,
  `references/delivery.md`, `references/special-cases.md`,
  `references/qualify.md`, `references/glossary.md` and the assets.
- `assets/situation-slide-template.md`.
- The Cohan timing table (15 to 30 minutes) in `references/design.md`.
- Delivery word-swap table ("show" vs "share", "allow" vs "enable", "but" vs
  "and") and scripted humor, including the reward joke, the "three engineers
  in a car" anecdote and the pile-of-books prop story, in
  `references/delivery.md`.
- Glossary entries for Do It, Do It Again, Illustration, Situation Slide,
  Outline and Introduction, and the "Same content as the Outline" wording in
  the Demonstration Roadmap entry.
- Pointers to the retired `good-presentations` skill.

### Changed
- "Do the last thing first" is now a lens, not a required order. The first
  principle reads: put something that matters to the audience in front of
  them early.
- `references/design.md`: new sections "The Screen Map" (stakeholder, CBI,
  Reason, Specific Capability, screen to show, Delta), "Showing the Path",
  "Questions and Meeting Check" and "Timing". The worked example is rewritten.
- `references/critique.md`: rubric reduced from 13 items to 8 (early
  relevance, capability-to-CBI tie, quantified Delta, buzzwords, question
  handling, file names, keyboard shortcuts, timing). The worked example is
  rewritten.
- Output norms: concrete time estimates per section against the user's
  budget. Over budget, trim depth first, then drop capabilities tied to the
  least important pain.
- Vendor voice routing: this skill builds the plan (CBI mapping, screens,
  time per section) and hands it to the vendor skill to apply voice and
  fact-sourcing when a script is needed.
- Special cases, qualification and the asset checklists now say "screen" or
  "screenshot" where they said Situation Slide or Illustration.

### Kept
- CBI/Reason/Specific Capability mapping, the Chain of Pain, the Delta, the
  Not Now List and To Do List, question handling, mouse discipline, bug and
  crash recovery, the buzzword test, and the file name and keyboard shortcut
  rules.

## [1.0.2] - 2026-09-03

### Added
- Reciprocal routing to vendor-specific voice skills (`SKILL.md`, new "Working
  With a Vendor-Specific Voice Skill" section). Fixes a one-way pointer:
  `references/critique.md` already named `bluedolphin-collateral` for brand-voice
  questions, but only in Critique mode; nothing surfaced that awareness in Design
  mode, where `bluedolphin-collateral`'s own Demo mode now defers to this skill
  for structure. Also removes a live trigger collision on "build a demo" between
  the two skills — they now have explicit, non-overlapping jobs.

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
