# StoryScope Core Features — Full Reference

All 30 core features from Russell et al. (2026), *StoryScope: Investigating idiosyncrasies in
AI fiction*, COLM 2026, arXiv:2604.03136v6.

Table 14 lists the 20 AI-characterizing features. Table 15 lists the 13 human-characterizing
features. That sums to 33 rows over 30 distinct features, because **Reference Explicitness**,
**Subplot Integration**, and **Dominant Emotional Expression** each appear on both sides with
a different option value elevated. Table 16 reproduces all of them with means and gaps.

`SKILL.md` uses 22 of the 30 inline as gates and corroborators. The remaining 8 are recorded
here and marked ○.

---

## Reading the scales

Three different scales appear in the same table. Never report a value without its unit.

| Marker | Scale | How to report |
|---|---|---|
| `%` | Prevalence of a specific categorical or binary option | percent; gaps in **percentage points** |
| `L` | 1–5 Likert, value is the mean | "3.94 on a 1–5 scale" |
| `o` | Ordinal, value is the mean over integer codes | state the code range |

**Gap = Human − AI throughout.** Negative gaps are AI-elevated. The AI column averages
across all five models.

> **Scale note on the two Reader engagement features.** Table 16 prints Fourth-Wall
> Permeability as 0.67 / 0.39 and Direct Reader Address as 0.28 / 0.07, both marked as
> ordinal means over integer codes. Table 15 gives the response options as 1–4 for
> fourth-wall permeability and never / occasional asides / frequent-structural for direct
> address, so the codes must be zero-based. The paper's own prose (§4.1) states the same two
> comparisons as "67% vs. 39%" and "28% vs. 7%". The table values and the prose values are
> therefore the same measurement described two ways, and the source does not fully
> disambiguate which presentation is canonical. **Report these as ordinal means with the code
> range, or quote the paper's percentages directly — do not present them as bare decimals,
> which read as Likert scores.**

---

## Table 16 — all 30 core features by theme

### AI-elevated: Thematic over-determination — cluster A

| Feature | Scale | Human | AI | Gap |
|---|---|---|---|---|
| Thematic Explicitness & Moralizing | L | 3.28 | 3.94 | −0.65 |
| Moral / Philosophical Weighting | L | 3.26 | 3.68 | −0.42 |
| Thematic Unity | L | 4.41 | 4.74 | −0.33 |
| Narratorial Thematic Commentary → yes | % | 52% | 77% | −25 |
| Dialogue Function → philosophical debate | % | 34% | 59% | −25 |
| Reference Explicitness → implicit echoes | % | 50% | 72% | −22 |

### AI-elevated: Sensory and embodied performativity — cluster B

| Feature | Scale | Human | AI | Gap |
|---|---|---|---|---|
| Dominant Emotional Expression → embodied | % | 38% | 81% | **−42** |
| Setting as Psychological Mirror | L | 3.58 | 4.07 | −0.49 |
| Environmental & Ecological Emphasis | L | 2.83 | 3.21 | −0.38 |
| Sensory Modalities → olfactory | % | 57% | 82% | −26 |
| Sensory Density | L | 3.66 | 3.93 | −0.26 |
| Depth of Interior Access | L | 3.67 | 3.93 | −0.26 |

−42pp is the largest gap in the taxonomy.

### AI-elevated: Structural streamlining — cluster C

| Feature | Scale | Human | AI | Gap |
|---|---|---|---|---|
| Causal Chain Continuity | L | 3.92 | 4.20 | −0.28 |
| Spatial Granularity Level ○ | o | 2.27 | 2.53 | −0.26 |
| Agency in Resolution → protagonist choice | % | 46% | 69% | −23 |
| Character Introduction → external description | % | 30% | 52% | −22 |
| Subplot Integration → no subplots | % | 57% | 79% | −22 |
| Mode of Resolution → internal understanding | % | 27% | 47% | −21 |
| Pre-Threat Character Investment ○ | L | 2.76 | 2.99 | −0.23 |
| Opening Spatial Grounding ○ | o | 2.12 | 2.33 | −0.20 |

> **Opening Spatial Grounding is a spatial feature, not a temporal one** — how much the
> opening grounds the reader in physical space. v1.0.0 of this skill reproduced this row
> under the label "Linear opening (begins at the beginning)," which is a temporal claim this
> row does not support. The temporal guidance in cluster D rests on the four Temporal
> complexity features below, which do support it.

### Human-elevated: Intertextual richness — cluster F

| Feature | Scale | Human | AI | Gap |
|---|---|---|---|---|
| Intertextual Strategy → explicit named reference | % | 47% | 24% | +23 |
| Reference Explicitness → balanced mix | % | 37% | 16% | +21 |

### Human-elevated: Reader engagement — cluster E

| Feature | Scale | Human | AI | Gap |
|---|---|---|---|---|
| Fourth-Wall Permeability | o | 0.67 | 0.39 | +0.28 |
| Frequency of Direct Reader Address | o | 0.28 | 0.07 | +0.21 |

See the scale note above before reporting either of these.

### Human-elevated: Temporal complexity — cluster D

| Feature | Scale | Human | AI | Gap |
|---|---|---|---|---|
| Depth of Recontextualization After Surprise | L | 3.28 | 2.95 | +0.34 |
| Degree of Chronological Discontinuity | L | 2.40 | 2.12 | +0.28 |
| Nonlinear Framing for Delayed Disclosure | L | 1.96 | 1.68 | +0.28 |
| Anachrony Intensity | L | 2.58 | 2.31 | +0.27 |

Every gap in this cluster is ≤0.34 on a 1–5 scale. The paper's abstract highlights temporal
complexity as a headline human signal, and the effect sizes are the smallest in the table.
Both things are true; `SKILL.md` Step 4 resolves them by ranking D mid-list.

### Human-elevated: Narrative diversity — cluster G

| Feature | Scale | Human | AI | Gap |
|---|---|---|---|---|
| Location Variety Scope | o | 1.34 | 1.08 | +0.26 |
| Dialogue-to-Narration Proportion | L | 2.95 | 2.70 | +0.24 |
| Subplot Integration → thematically parallel | % | 42% | 21% | +22 |
| Moral Polarity Toward Protagonist → ambivalent/mixed | % | 59% | 38% | +21 |
| Dominant Emotional Expression → explicit labels | % | 29% | 8% | +21 |

Table 16 places explicit emotion labels here. Functionally it is the human-side pole of
cluster B's gate, and `SKILL.md` uses it there — the B fix needs the positive instruction
("name the feeling"), not only the negative one ("stop using the body").

---

## Feature questions and response options

From Tables 14 and 15. These are the paper's own operationalizations. Score against the
option set rather than in prose — a closed answer set is what makes an audit reproducible
across runs.

| Feature | Question | Options | Elevated for |
|---|---|---|---|
| Narratorial Thematic Commentary | Does the narrator state the theme? | yes / no | AI: yes |
| Dialogue Function | What work does dialogue do? | philosophical debate / … | AI: debate |
| Thematic Unity | Do all elements serve one theme? | 1–5 | AI: high |
| Thematic Explicitness & Moralizing | How explicitly is the theme stated or moralized? | 1–5 | AI: high |
| Moral / Philosophical Weighting | How heavily does the story foreground moral or philosophical questions? | 1–5 | AI: high |
| Dominant Emotional Expression | How are characters' emotions most commonly conveyed? | explicit labels / embodied metaphors / behavioral cues / ambiguous | AI: embodied · Human: explicit labels |
| Setting as Psychological Mirror | Does setting reflect inner state? | 1–5 | AI: high |
| Sensory Modalities | Which senses are engaged? | multi-select, incl. olfactory | AI: olfactory |
| Sensory Density | How dense is sensory detail? | 1–5 | AI: high |
| Depth of Interior Access | How deep into characters' inner life does narration go? | 1–5 | AI: high |
| Environmental & Ecological Emphasis | How prominent is the natural environment or ecology? | 1–5 | AI: high |
| Agency in Resolution | Whose agency resolves the main event chain? | protagonist choice / … | AI: protagonist choice |
| Mode of Resolution | Is the main event chain resolved through internal acceptance or external action? | resolved externally / resolved internally / unresolved | AI: internally |
| Subplot Integration | How directly do subplots echo the central theme? | no subplots / thematically parallel / contrasting / independent | AI: no subplots · Human: thematically parallel |
| Causal Chain Continuity | Does every event cause the next? | 1–5 | AI: high |
| Character Introduction | How is the character introduced? | external description / in dialogue / in action | AI: external description |
| Pre-Threat Character Investment | How much investment is built before major jeopardy? | 1–5 | AI: high |
| Spatial Granularity Level | How fine-grained is the depiction of physical space? | very_low–high (ord) | AI: high |
| Opening Spatial Grounding | How much does the opening ground the reader in space? | ord | AI: high |
| Intertextual Strategy | What kinds of intertextual engagement does the story employ? | explicit named / retelling / pastiche / myth-religion / self-referential (multi) | Human: explicit named |
| Reference Explicitness | Are intertextual gestures explicit or diffuse? | none / explicit named / implicit echoes / balanced mix | AI: implicit echoes · Human: balanced mix |
| Frequency of Direct Reader Address | How often does the text directly address the reader? | never / occasional asides / frequent-structural | Human: frequent |
| Fourth-Wall Permeability | To what extent does the story break the boundary between story-world and reader? | 1 (no breaking) – 4 (radical violations) | Human: high |
| Degree of Chronological Discontinuity | How often does the narrative jump across time? | 1–5 | Human: high |
| Anachrony Intensity | How heavily does the narrative rely on flashbacks or flash-forwards? | 1 (absent) – 5 (dominant anachronic) | Human: high |
| Nonlinear Framing for Delayed Disclosure | To what extent does the story use time jumps to stage revelations? | 1 (linear) – 5 (heavily fragmented) | Human: high |
| Depth of Recontextualization After Surprise | How extensively does a revelation force reinterpretation of earlier scenes? | 1 (none) – 5 (complete re-reading) | Human: high |
| Moral Polarity Toward Protagonist | Does the narrative frame the protagonist's choices as morally clear or ambiguous? | clearly positive / ambivalent-mixed / clearly negative | Human: ambivalent |
| Dialogue-to-Narration Proportion | What proportion of text is direct dialogue vs narration? | 1 (no dialogue) – 5 (dialogue dominates) | Human: high |
| Location Variety Scope | How many distinct physical locales does the story inhabit? | single – multiworld (ord) | Human: high |

---

## The eight features not used inline

Recorded for completeness. Each is either low-gap, fiction-specific, or has no intervention
that survives the Step 5 guardrail in a professional register.

| Feature | Gap | Why not inline |
|---|---|---|
| Moral / Philosophical Weighting | −0.42 | Used as a cluster A corroborator; second-largest Likert gap in the table |
| Environmental & Ecological Emphasis | −0.38 | Cluster B corroborator; fiction-weighted |
| Depth of Interior Access | −0.26 | Cluster B corroborator. Named in the skill's own description as "character interiority" and omitted from v1.0.0's body entirely |
| Spatial Granularity Level | −0.26 | Cluster C corroborator; no non-fiction intervention |
| Pre-Threat Character Investment | −0.23 | Cluster C corroborator; fiction only |
| Opening Spatial Grounding | −0.20 | Cluster C corroborator; smallest gap in the AI-elevated set, and the row v1.0.0 mislabeled |
| Reference Explicitness → implicit echoes | −22 | Cluster A corroborator; the AI-side pole of cluster F's gate |
| Dialogue-to-Narration Proportion | +0.24 | Cluster G corroborator. "More dialogue relative to narration" is a cheap concrete intervention and was absent from v1.0.0 |

All eight now appear as corroborators in `SKILL.md`. None is a gate.

---

## What the paper does not support

- **Any claim about writing under ~5,000 words.** The corpus is ~5,000-word literary short
  fiction. Short-form guidance in this skill is judgment.
- **Any claim about non-fiction.** No essays, case studies, or business collateral in the
  corpus.
- **Any claim that these features measure quality.** They measure position in narrative
  feature space relative to published fiction and five 2025–2026 LLMs.
- **Per-model targeting from the core set.** The paper reports per-model fingerprints
  (Claude: flat event escalation; GPT: gossip as plot mechanism; Gemini: external character
  description) from a separate 101-feature Core+FP model at 91.1% macro-F1. Those are not in
  the core 30 and are not used here.
- **Stability of the numbers over time.** The AI column averages five models from a single
  generation. Model behavior moves; these gaps will drift.
