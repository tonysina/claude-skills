# Changelog

## [1.1.0] - 2026-09-02

Restructured from a reference document into an executable procedure. The figure
knowledge in 1.0.0 was sound; what was missing was the operational layer that decides
*when* to apply a figure and *when to stop*.

### Added

- **Antithesis** — 1.0.0 declared "contrast creates impact" as its master principle but
  shipped no figure for contrast. Added with a swap test to detect manufactured contrast.
- **Hypophora** — ask-then-answer. Highest-yield figure for executive summaries and
  business writing, absent from 1.0.0.
- **Erotema** — rhetorical question, with an honest note that hypophora is usually better.
- **Figure budget** with hard caps by length and register (SKILL.md Step 1). 1.0.0 said
  "use sparingly," which is an adverb, not a constraint. Over-application was the skill's
  dominant failure mode.
- **Per-figure trigger conditions.** In 1.0.0 only chiasmus had them; the other eight
  figures had no condition governing when to apply them, so the model applied them
  because they were on the list. Every figure now has a detectable trigger, and "don't
  hunt for triggers" is stated explicitly in Common issues.
- **Forbidden constructions table** mapping each default-mode construction to the
  humanizer pattern number it violates, with a replacement for each.
- **Claim check guardrail.** Figures compress and compression eats qualifiers. Four-point
  check for hedges becoming promises, vanished qualifiers, dropped numbers, and lost
  attributions — with instructions to keep the claim and drop the figure when they
  conflict.
- **Ear test.** Farnsworth's method is auditory; 1.0.0 said "the ear detects differences"
  and gave no auditory procedure. Now: stress on the final syllable, closing clause in
  one breath.
- **Triage step** with a register table, including a hard stop for technical, legal,
  process, and data writing.
- **Mode-bound output formats** per use case, replacing 1.0.0's "brief note on techniques
  applied (if helpful for learning)", which left output shape to the model and varied
  run to run.
- **Common issues** section, including "zero figures is a real answer."
- **`references/figures.md`** — extended catalog organized by Farnsworth's families:
  symploce, anadiplosis, epizeuxis, asyndeton, polysyndeton, praeteritio, litotes,
  strategic passive, direct address. Includes a table of figures deliberately excluded
  and why.
- **`beyond-obvious` chaining** for single-line work, to counter the tendency to apply the
  first figure that fits.
- This changelog.

### Changed

- **"Rule of three" replaced by isocolon** with a mandatory load-bearing test. This was a
  direct contradiction with `humanizer`: humanizer pattern #7 is titled "Rule of three"
  and instructs removal of decorative triads, while 1.0.0 Technique 8 instructed adding
  them. Resolved by distinguishing load-bearing parallel members (each carries
  information the others don't — keep) from decorative triads (members interchangeable —
  humanizer strips them).
- **Chiasmus split from antimetabole.** 1.0.0 labeled the Kennedy line as chiasmus and
  told the model to "produce A-B-B-A" with no word-identity constraint, which yields
  structural mush. Antimetabole (same words reversed) is now the default because it is
  mechanically verifiable; chiasmus is a fallback. The three trigger tests from 1.0.0 —
  the strongest piece of engineering in that version — are preserved verbatim.
- **Saxon diction reclassified as free.** 1.0.0 presented Saxon default, Saxon finish, and
  say-it-twice as three of nine "techniques," making 33% of the skill one idea and
  implying diction work consumed the same attention budget as a figure. Diction removes
  ornament rather than adding it, so it is now unbudgeted and applied everywhere.
- **Workflow position made bidirectional.** `human-narrative` declared the pipeline
  (human-narrative → humanizer → farnsworth-rhetoric); 1.0.0 said nothing back. Now
  declared, with an explicit note on what to do if humanizer is re-run afterward.
- **Description gained a "Do NOT use for" clause.** 1.0.0 was the only skill in the
  writing set without one, and its triggers ("make this persuasive," "key message")
  collided with `strategic-persuasion-writing` and `good-presentations` with no
  disambiguation. Also added triggers: "make this land," "sharpen this line," "this
  ending is flat," "tagline," "farnsworth".
- Anaphora cap tightened to one run per piece and prohibited under 300 words. Epistrophe
  prohibited from sharing a paragraph with anaphora.

### Fixed

- **The Full Example.** 1.0.0's flagship output ("...we will not just compete. We will
  lead.") contained a negative parallelism (humanizer #6), two anaphora runs, a generic
  positive closer (humanizer #15), and an em dash — and it upgraded the source's hedged
  "an opportunity to enhance our competitive positioning" into the unqualified promise
  "we will lead." The skill's most-anchored-on artifact was a specimen of what the
  adjacent skill exists to delete. It is now retained as a labeled **overcooked
  counter-example**, with the budget violations and the claim inflation itemized, beside
  a compliant rewrite.
- **Technique 1 contradicted itself.** The instruction said "mix for contrast — use
  Latinate to set up Saxon"; the example directly below performed neither mixing nor
  contrast, only plain-language deletion. Rewritten as a nominalization-to-verb move with
  the contrast claim removed.
- **"Put simply:" removed** from the say-it-twice example. It belongs to humanizer's
  didactic-filler list (#14). Restated as: juxtapose the two sentences with no transition,
  and the anti-pattern is now named.
- **Churchill's active-voice line labeled as hypothetical.** It is Farnsworth's own
  teaching foil, not a line Churchill wrote. 1.0.0 presented it unlabeled beside the real
  quotation, where an agent could quote it as genuine.
- Anadiplosis carries a warning that the figure asserts causation structurally and will
  lie on the author's behalf if the chain is merely correlational.

### Verified

- Quotation accuracy checked against sources: Holmes (*United States v. Schwimmer*, 1929
  dissent), Lincoln ("House Divided," 1858), Gettysburg Address, Kennedy inaugural,
  Churchill ("so much owed," 20 August 1940; "we shall fight," 4 June 1940), Franklin,
  Caesar. All genuine, condensed where noted in SKILL.md.

### Smoke tested

Deterministic scan (`scripts/scan-ai-tells.py`) over 5 synthetic cases plus a positive
control. The scan reads humanizer's flag lists live from its SKILL.md, so it cannot drift
out of sync with the skill it is reconciling against.

- All 5 outputs: 0 hard violations. Budget tiers `<300` and `300–600` exercised.
- The three negative cases — technical runbook, already-good prose, status update —
  correctly produced zero figures. Over-application is this skill's dominant failure
  mode, so restraint cases are more than half the test set.
- Regression confirmed: v1.0.0's own Full Example output scores 3 hard violations against
  v1.1.0's rules (negative parallelism, generic positive closer, and an anaphora run in a
  36-word piece).
- humanizer flag reduction on the exec-summary case: 2 flags in, 0 out.
- Note for future runs: the positive control returned *clean* on the scan's first
  execution, missing all three known violations. Two scan bugs caused it — humanizer
  states pattern #6 as templates with `X`/`Y` placeholders that cannot be literal-matched,
  and the anaphora detector did not skip leading conjunctions, so `But if we commit / if
  we collaborate / if we follow through` read as a run of 2. A third bug produced a false
  positive (`here is a` matching inside "There is also"). Without the control, the run
  would have reported a confident false pass. Always score the control first.

### Untested

- **Executor bias.** The smoke test was authored and executed in the same context as the
  skill, so it shows that these outputs comply — not that the skill teaches a fresh agent
  to comply. Needs `skill-builder` eval-mode with a clean-context executor subagent.
- **The `>600` word budget tier is unexercised** (1 figure per 150 words, cap 6). It is
  the only tier expressed as a rate rather than a flat cap, so it is the most likely of
  the three to be miscalibrated.
- **Claim drift is unmeasured.** The scan cannot check it, and it is the guardrail with
  the least evidence behind it. Needs the LLM grader.
- Antithesis and hypophora are not regex-detectable, so scanned figure counts are a floor
  rather than a total. `#15 generic positive conclusions` is an open category in
  humanizer, so only listed literals are caught.
- Cases are synthetic. A real corpus should be drawn from live collateral.

## [1.0.0] - 2026-02-19

### Added

- Initial release. Nine techniques from Ward Farnsworth's *Classical English Rhetoric* and
  *Classical English Style*: Saxon vs. Latinate diction, Saxon finish, say it twice,
  anaphora, epistrophe, mixed anaphora/epistrophe, chiasmus, rule of three, strategic
  passive voice.
- Master principle (contrast), application guide by context, quick revision checklist,
  worked example.
