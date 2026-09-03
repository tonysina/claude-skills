# Changelog

## [2.0.0] - 2026-09-03

Audit findings from the persuasion-triad skill review (`skills/persuasion-triad-review`
branch), cross-checked against the primary source, Chase Hughes' *The Behavior Ops
Manual*. Corrects both fabricated content the skill was generating and the audit's own
initial assumption that most of the framework was unsourced — verification against the
actual book showed FATE, PCP, the Six-Axis Model, and the Behavior Compass are real,
faithfully-rendered content from that source; only a handful of specific claims (see
Removed) were not in it.

### Fixed

- **Attribution.** `SKILL.md:52` said "from source material" and never named it. Now
  names *The Behavior Ops Manual* by Chase Hughes in the frontmatter and inline.
- **Fabrication surface.** The authority/social-proof templates in
  `structural-models.md` had unbound brackets with no instruction that they be filled
  from user-supplied fact; `examples.md`'s five outputs all asserted invented,
  verifiable-sounding statistics as fact. Templates now require `[FACT NEEDED: ...]`
  when the user hasn't supplied the claim; two examples now demonstrate that marker
  surviving into a delivered draft.
- **Self-defeating concealment.** The skill instructed marking embedded commands with
  bold, while also requiring techniques be invisible to casual reading — mutually
  unsatisfiable, and the generated examples showed the visible-spam result. Bold-marking
  instruction removed; commands are now placed by sentence position only.
- **Layer-count contradiction.** `SKILL.md:23` said three layers; `structural-models.md`
  said four. The source's own Hierarchy of Influence Factors has four, ranked
  Impulse > Behavioral > Emotion > Thought. Both now say four, in that order.
- **Priority-state count contradiction.** Three different counts appeared across the
  skill (three / max 4 / select 4 / all six ranked). The source states "only 3 of 6 need
  be strongly present" (its own example: Milgram's obedience experiment). All sites now
  say three.
- **Unbounded dosage floors.** Every quantity in the skill was a floor with no ceiling
  ("at least 6-8 techniques," "4-6 times," escalating with stakes). Converted to a
  ceiling table in `SKILL.md` Step 5, and inverted the stakes rule: higher stakes now
  call for more restraint, not more layering.
- **Inoperative ethics clause.** The previous clause forbade "bypassing informed
  consent" while the method is defined as working beneath conscious awareness — a
  contradiction the model couldn't act on. Replaced with a Step 0 scope gate: this
  skill's techniques are adapted from a manual built for interrogation/security
  contexts, and are only in scope where the reader can freely decline. Requests aimed at
  someone who can't (a direct report, a dependent, someone in distress) now get a plain
  message instead of a softer version of the technique — demonstrated in `examples.md`
  Example 2.
- **Frontmatter exclusion not enforced.** "Not for routine business correspondence" was
  stated but never checked. Step 0 now checks it.
- **Demeaning-identity language.** Negative-dissociation examples included insults
  toward anyone who declines ("lazy people," "weak decision-makers"). Removed; kept the
  identity-neutral distancing variants.
- **Blame-shifting and false-consensus patterns.** The PCP Permission phase included
  "it's not your fault" and "everyone in your position would" examples. Replaced with
  patterns that name the real reason for a change rather than manufacturing absolution
  or consensus.

### Removed

- **The 70%+ sensory-density target.** Not in the source — the book says only "adapt
  your language to their mode." Removed; sensory matching now applies where it fits
  naturally.
- **The scarcity/brain-scan claim** ("fear of loss shows up in brain scans... losing
  children or their phone"). Confirmed absent from the source entirely — no "scarcity"
  or "fear of loss" content of any kind in the book. Removed; the surrounding
  urgency-writing techniques are kept as standard craft, not attributed to Hughes.

### Changed

- **Needs Map framing.** "The Need is the wound; the behavior is the self-medication"
  is the source's own framing but is now scoped to internal reasoning only — never to be
  echoed in output-facing text.
- **Neuropeptide mechanism and VAK sensory model.** Both confirmed faithfully sourced to
  the book. Kept, with an added note that these are the source's own explanatory model,
  not independently replicated findings.
