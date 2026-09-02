# Changelog

## [1.1.0] - 2026-09-02

Restructured from a findings checklist into a gated procedure, and corrected four citation
defects. The research base in 1.0.0 was real and the feature families were the right ones;
what was missing was the layer that decides *when a flag is a finding* and *when to stop*.

### Fixed

Citation defects, all found by checking every cited figure against the paper's Table 16.
**Every individual number in 1.0.0 was accurate.** The errors were in what they were
attached to.

- **The headline statistic was wrong.** 1.0.0 opened with "30 structural features that
  distinguish AI from human writing with 93% detection accuracy." Per Table 2, 93.2%
  macro-F1 belongs to the **257-feature** narrative model. The **30 core features reach
  84.8%** — slightly below style-only features (85.8%) and well below raw-text baselines
  (TF-IDF+XGBoost 99.7%, ModernBERT 99.9%). 1.0.0 attributed the full model's performance to
  the subset it actually taught, in its first paragraph. Also, macro-F1 is not accuracy.
- **"Stable even after aggressive style editing" was unsourced and undersold.** The real
  result (§4.2) is stronger and worth citing precisely: after LAMP span-level artifact
  rewriting on 278 Gemini stories, the narrative model still detects them at 93.9% macro-F1
  versus 95.5% unedited, a 1.6-point drop. This is the finding that justifies a structural
  skill separate from `humanizer`, and it belongs in the skill by name.
- **One evidence row was mislabeled.** 1.0.0 listed "Linear opening (begins at the beginning)
  | AI 2.33 | Human 2.12 | −0.20". The Table 16 feature at those values is **Opening Spatial
  Grounding** — how much the opening grounds the reader in physical space. A spatial feature
  was reproduced as a temporal claim. The temporal guidance survives on the four genuine
  Temporal complexity features; that row never supported it.
- **Wrong table cited.** 1.0.0 cited "Core features (Table 15)" for the whole 30-feature
  taxonomy. Table 15 is the 13 human-characterizing features; Table 14 is the 20
  AI-characterizing features; Table 16 carries the means and gaps the skill reproduces. The
  20 + 13 = 33 rows cover 30 distinct features because Reference Explicitness, Subplot
  Integration, and Dominant Emotional Expression each appear on both sides.
- **Version.** Cited v4; current is v6 (revised 10 Aug 2026). Also now noted as published at
  COLM 2026 rather than as a preprint.

### Added

- **Step 1 register triage** with a hard stop for technical docs, runbooks, process
  instructions, data reporting, legal, and RFP answers, and a per-register cluster
  allow-list. 1.0.0's Long-Form Mode covered "essays, case studies, thought leadership" and
  instructed "apply the full checklist," so a customer case study was eligible for subplots,
  moral ambiguity, a nonlinear opening, and a resolution outside the protagonist's control.
  Register, not length, now selects the mode.
- **Gate-plus-corroborator scan.** A cluster fires only when its highest-gap feature is
  AI-side *and* at least one corroborator agrees. 1.0.0 said "flag each pattern present,"
  which ignores that these are population base rates: 57% of *published human* stories have
  no subplots, 52% state the theme narratorially, 46% resolve on protagonist choice. Single
  features are near-worthless evidence about one document.
- **Step 3 threshold.** 0–1 clusters → no interventions; 2–3 → up to 2; 4+ → up to 3. Hard
  cap of 3 per pass. 1.0.0 had no threshold, so the audit produced a findings list on every
  run, and its intervention counts disagreed with themselves (Step 5 said 3–5, Use Case 2
  said top 3). "Zero interventions is a real answer" is now stated twice.
- **Step 5 guardrail — "keep the piece, drop the intervention."** Four checks: coherence,
  truth, whether the point survived, whether the author would recognize it. Structural
  analogue of `farnsworth-rhetoric`'s claim check.
- **Truth constraint on cluster C1.** In non-fiction you may only leave unresolved what is
  actually unresolved and only externalize a resolution that was actually external. You
  cannot invent an open thread in a case study; if the fact isn't known, the intervention is
  flagged for the author rather than executed. 1.0.0 had no truth constraint anywhere.
- **"What this optimizes, and what it doesn't."** States the objective function: these
  features come from a detection study, matching the human distribution is a proxy rather
  than the goal, and an intervention that moves the distribution while making the piece
  worse has failed. 1.0.0 instructed "break one causal link — let something happen that
  doesn't follow logically" with one sentence of counterweight in Common Issues.
- **Closed-option feature questions** from Tables 14 and 15, replacing prose heuristics.
  Scoring "Dominant Emotional Expression → explicit labels / embodied metaphors / behavioral
  cues / ambiguous" is reproducible across runs; scoring "look for characters' hearts
  clenching" is not. Full option sets in `references/features.md`.
- **Forbidden constructions table** mapping each move to the `humanizer` pattern its default
  form violates, with a replacement.
- **A worked example.** 1.0.0 had none — no demonstration of input → scan → intervention for
  a skill whose deliverable is a prioritized intervention list, and an Output Format section
  describing a shape it never showed. The example is thought leadership, fires 7 clusters,
  takes 3, and itemizes what was declined by cap, by register, and by truth constraint.
- **Scale key.** 1.0.0 presented percentages, 1–5 Likert means, and ordinal means in
  identically formatted tables under the column header "rate," and told the agent to report
  "the human/AI rate gap" — which yields "+0.28" for a 28-point percentage gap. Units are now
  mandatory in output, and `references/features.md` documents the ambiguity in the two Reader
  engagement features, where Table 16 prints 0.67/0.39 and 0.28/0.07 as ordinal means while
  the paper's own prose states the same comparisons as 67%/39% and 28%/7%.
- **Corpus provenance.** Human stories come from **Books3 short-story anthologies** —
  published literary fiction — at **~5,000 words each**. 1.0.0 stated neither, then applied
  the results to 300-word status updates without hedging. The extrapolation is now declared
  as judgment in one place and bounded in the register table.
- **The eight missing core features**, now all present as corroborators. Two matter:
  **Dialogue-to-Narration Proportion** (+0.24 — "more dialogue relative to narration" is a
  cheap concrete intervention and was absent) and **Dominant Emotional Expression → explicit
  labels** (29% human vs 8% AI — the positive instruction cluster B's fix needs, where 1.0.0
  gave only the negative). Also **Depth of Interior Access**, which is the "character
  interiority" the description advertises and 1.0.0's body never mentioned.
- **`references/features.md`** and this changelog.
- `source-check` named as a downstream dependency of cluster F: naming a real source means
  the claim about it has to be right.

### Changed

- **Intervention order reworked**, and split by mode. Long-form: A → B → F → D → E → C → G.
  Short-form and case study: A → B → F → E. 1.0.0 ranked temporal complexity first as "the
  most impactful structural move"; its four gaps are the smallest in the table (all ≤0.34 on
  a 1–5 scale), it is the most invasive intervention available, and it is out of scope for
  every non-fiction register. Thematic restraint now leads because it is a pure deletion with
  the largest cluster behind it and improves the piece on any standard.
- **1.0.0's priority list was inverted for its own short-form mode.** It ranked temporal
  complexity #1 and resolution mode #3, both of which short-form skips, and reader address
  last while calling it "often high impact for professional writing" — in a mode where it is
  one of only three in-scope signals. Each mode now has its own order.
- **Cluster C split into C1 and C2 by cost.** C1 (partial or external resolution, one
  unresolved thread) is available in non-fiction under the truth constraint. C2 (break a
  causal link, introduce a character mid-action, add a subplot) is fiction and personal essay
  only. 1.0.0 offered all of them at every length.
- **Intertextual reference moved into short-form scope.** 1.0.0 excluded it as not applying
  "at short-form length." Naming a specific work is a one-clause change that works at any
  length, and at +23pp it is the best value-per-effort move in the taxonomy. Declared as
  judgment, since nothing in the corpus is short.
- **Emotional-expression fix now carries the "show, don't tell" warning explicitly.** The
  evidence says human authors name feelings more than three times as often as AI. That
  contradicts standard craft advice, so the instruction now says so and says to apply it
  once rather than everywhere.
- Description tightened: "subplot architecture" and "character interiority" replaced with
  "resolution mode, emotional expression, intertextual reference," which is what the skill
  operates on. Hard-stop registers added to the "Do NOT use for" clause.

### Verified

- All 22 statistics in 1.0.0 checked against Table 16 of arXiv:2604.03136v6, extracted from
  the author-hosted PDF. Every figure accurate; the four defects above were attribution and
  labelling, not arithmetic.
- Feature-count arithmetic reconciled: Table 14 (20) + Table 15 (13) = 33 rows over 30
  distinct features, with three features double-listed. Matches the paper's "30 core
  features."
- Cross-skill collision with `humanizer` #17 confirmed and fixed. 1.0.0's model direct-address
  intervention was *"you'll understand why this matters in a moment"* — a forward-reference
  announcement, which is what #17 exists to delete ("LLMs announce what they're about to do
  instead of doing it"; watch list includes "you might be wondering," "here's what you need
  to know"). Since the declared pipeline runs `humanizer` after this skill, `humanizer` would
  have stripped the intervention this skill had just made. Replaced with a second-person
  claim or an aside, with the anti-pattern named.
- Checked and cleared: cluster F's "name a specific work" does **not** conflict with
  `humanizer` #4 (vague attributions and notability name-dropping). #4 targets unnamed
  authorities and inflated source counts; its own corrected examples add named specifics. The
  two skills agree. #4 is cited in the forbidden-constructions table as the failure mode to
  avoid when executing F, not as a conflict.

### Untested

- **No eval run.** 1.0.0 shipped with no test and 1.1.0 adds none. Needs `skill-builder`
  eval-mode with a clean-context executor.
- **`scripts/scan-ai-tells.py` cannot cover this skill.** These features are structural and
  not regex-detectable, unlike `humanizer`'s lexical patterns. Grading needs an LLM with a
  rubric built from the response-option sets in `references/features.md`. The negative cases
  are the ones that matter: a case study, an explainer, and a status update should each
  produce zero interventions.
- **The threshold table is calibrated by argument, not measurement.** 0–1 / 2–3 / 4+ maps to
  0 / 2 / 3 interventions on the reasoning that base rates make single features weak. No run
  has established that a piece firing 2 clusters reads differently from one firing 4.
- **The gate-versus-corroborator assignment is a judgment call.** Highest-gap feature per
  cluster becomes the gate. For cluster C the gate merges two features (agency in resolution,
  mode of resolution) because neither alone captures it.
- **Whether an LLM scores the closed-option questions consistently is unmeasured.** That is
  the central bet of this version.
- **The register allow-list is unevidenced** and is the change most likely to be wrong,
  because no register in the table except fiction appears in the corpus.

## [1.0.0] - 2026-06-03

### Added

- Initial release. AI-elevated and human-elevated pattern checklists drawn from StoryScope's
  core feature taxonomy, organized into thematic over-determination, sensory and emotional
  performativity, structural streamlining, temporal complexity, moral ambiguity, reader
  address, intertextual reference, and location/subplot variety.
- Long-form and short-form modes, five-step scanning process, five-item intervention priority
  list, three output formats, workflow position, common issues.
