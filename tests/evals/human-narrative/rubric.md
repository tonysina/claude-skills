# human-narrative scoring rubric

The scoring instrument for the LLM-judge pass over `human-narrative`. Reads a piece of text
and returns a closed-form score for all 30 StoryScope core features, the seven cluster
verdicts those scores imply, and the intervention count the skill's own threshold allows.

Why a rubric and not `scripts/scan-ai-tells.py`: this skill's features are structural, not
lexical. The script matches literal patterns, so it can see `SIGNPOSTING` phrasings and
nothing else — after #6 it also reports `FORWARD-REF`, which is one phrasing of one
corroborator of one cluster. The other 29 features have no lexical surface. Coverage before
this rubric was the specific expectations written for the three evals in `evals.json`, which
check the arms those evals happen to exercise and cannot re-check the skill against its own
feature list.

**Scope.** This rubric scores a *text*. It does not grade a response. To grade a
`human-narrative` response — did it triage the register correctly, did it stay under the
cap, did the guardrail hold — the judge scores the input and the output separately with this
rubric and compares, which is what `agents/rubric-grader.md` walks through.

**Source.** Every option set and every pole below is Table 14, 15 or 16 of
`skills/human-narrative/references/features.md` (Russell et al., COLM 2026,
arXiv:2604.03136v6). Where this rubric differs from a bare reading of the tables — the E/F
short-form rule, the register scope — it is following `SKILL.md`, and says so inline.

---

## What the score does not mean

Carry these into every judgment. They are the same three consequences `SKILL.md` opens with,
and a judge that forgets them produces confident nonsense.

1. **Every feature is a population base rate.** 57% of *published human* stories have no
   subplots; 52% state their theme narratorially. A single AI-side feature is near-worthless
   evidence about one piece. That is why a cluster needs a gate *and* a corroborator, and why
   the threshold table needs multiple clusters.
2. **AI-side is not worse.** These features come from a detection study, not a quality study.
   A piece can score AI-side on ten features and be the better piece. The score is a position
   in feature space, never a verdict on the writing.
3. **The corpus is ~5,000-word literary short fiction.** For any non-fiction register the
   score is an extrapolation across genre and a 10–15× length gap. Score it anyway, but never
   report a non-fiction cluster verdict without saying the evidence base does not cover it.

---

## Step 1 — Register

Score this first. It decides which clusters are even in scope, and a wrong call here makes
every cluster verdict below it meaningless.

| Register | Clusters in scope | Never |
|---|---|---|
| `fiction` — fiction, personal essay, narrative journalism | A–G | — |
| `thought-leadership` — opinion, keynote narrative, expository explainer | A, B, D, E, F, C1, G1 | C2–C8, G2, G3, G4 |
| `case-study` — customer story, customer-facing narrative | A, B, E, F, C1 | C2, D, G |
| `short-professional` — executive summary, status update, email, slide copy (<600 words) | A, B, E, F | C, D, G |
| `hard-stop` — technical docs, runbooks, process instructions, data reporting, legal, RFP answers | none | all |

**The expository explainer** — a piece that explains how something works to a general reader —
has no row of its own in `SKILL.md` and belongs here. It is not opinion and not documentation.
Two judges reasoned it into different rows; both are defensible and neither changed the
outcome, but record which you chose and why, because the choice moves D, C1 and G1 in or out
of scope.

**G in `thought-leadership` is G1 only.** `SKILL.md` writes the in-scope column as "G-moral",
which names the gate. G2 (subplots), G3 (dialogue proportion) and G4 (location variety) are
fiction and personal essay only, so G cannot fire in this register — the same orphaned-gate
shape as C1, below.

`hard-stop` ends the pass. Record the register, record that no cluster was scored, and stop.
A partial audit of a runbook is a failure, not a partial success.

**Register, not length.** A 2,000-word runbook is `hard-stop`. A 400-word personal essay is
`fiction`.

Score a feature `not_in_scope` when its cluster is out of scope for the register. Not
`human_side` — the distinction matters, because a `not_in_scope` feature must not be able to
fire a cluster or fill an intervention slot.

**`not_applicable` is a fifth value, and it is not AI-side.** Three option sets presuppose
narrative material that non-fiction often does not have: B1 assumes emotions are conveyed
somehow, C1 assumes an event chain, G1 assumes a protagonist. Two of those three are gates,
so a judge forced to pick a closed value can put a cluster's gate on the AI side of a
distinction the text never draws. When the feature's premise is absent, score
`not_applicable`, say in `evidence` what you looked for, and treat it as not AI-side for
gating. Do not reach for `ambiguous` as a null — `ambiguous` is a real B1 option meaning the
emotion is conveyed but unclear, which is a different claim from no emotion being conveyed.

---

## Step 2 — Score the 30 features

Answer with the option, the integer, or the code — never in prose. A closed answer set is
what makes the pass reproducible across runs, which is the whole reason this rubric exists.

**32 rows, 30 features.** The tables below have 32 scored rows over the paper's 30 distinct
features, because Reference Explicitness is read by both A and F (as A6 and F1) and Subplot
Integration by both C and G (as C8 and G2). Each is one score, recorded under both ids so each
cluster can read the pole it cares about. Score 32 rows; report 30 features.

Every row carries the scale marker from `features.md`: `%` prevalence, `L` 1–5 Likert mean,
`o` ordinal mean over integer codes. **Never report a value without its unit.** Gap is
Human − AI, so a negative gap is AI-elevated.

### Cluster A — Thematic over-determination (6 features)

Largest cluster and the strongest signal family.

| # | Feature | Scale | Question | Options | AI-side | Gap |
|---|---|---|---|---|---|---|
| A1 | Narratorial Thematic Commentary | `%` | Does the narrator state what the piece means? | yes / no | **yes** | −25 |
| A2 | Moral / Philosophical Weighting | `L` | How heavily does the piece foreground moral or philosophical questions? | 1–5 | ≥4 | −0.42 |
| A3 | Dialogue Function | `%` | Does dialogue function as philosophical debate? | yes / no | **yes** | −25 |
| A4 | Thematic Unity | `L` | Do all elements serve one theme? | 1–5 | ≥5 | −0.33 |
| A5 | Thematic Explicitness & Moralizing | `L` | How explicitly is the theme stated or moralized? | 1–5 | ≥4 | −0.65 |
| A6 | Reference Explicitness → implicit echoes | `%` | Are intertextual gestures explicit or diffuse? | none / explicit named / implicit echoes / balanced mix | **implicit echoes** | −22 |

**Gate: A1.** Corroborators: A2, A3, A4, A6.

**A5 is scored but is neither the gate nor a corroborator.** It carries the largest gap in the
taxonomy after B1 (−0.65) and still cannot affect whether A fires. That reproduces `SKILL.md`
faithfully and is not a transcription slip — see `negative-cases.json`, `open_questions`, where
it is recorded as a question about the skill rather than silently repaired here.

**A4 measures thematic unity, not topical unity.** Any competent professional text is about one
subject, and a judge reading A4 as "is this on topic?" scores every explainer near-maximal. The
question is whether every element is bent toward serving one *theme* — a meaning the piece is
advancing — which is a stronger claim. The ≥5 threshold is doing real work here: 4 is human-side.

A6 is scored once and read twice: AI-side for A (`implicit echoes`), human-side for F
(`balanced mix`). A score of `explicit named` or `none` is neither cluster's AI pole, so it
reads human-side in both. That is a legitimate outcome, not a scoring error.

### Cluster B — Sensory and embodied performativity (6 features)

Contains the largest gap in the taxonomy.

| # | Feature | Scale | Question | Options | AI-side | Gap |
|---|---|---|---|---|---|---|
| B1 | Dominant Emotional Expression | `%` | How are emotions most commonly conveyed? | explicit labels / embodied metaphors / behavioral cues / ambiguous | **embodied metaphors** | **−42** |
| B2 | Setting as Psychological Mirror | `L` | Does setting mirror the character's inner state? | 1–5 | ≥4 | −0.49 |
| B3 | Sensory Modalities → olfactory | `%` | Is there smell-based imagery? | yes / no | **yes** | −26 |
| B4 | Sensory Density | `L` | How dense is sensory detail? | 1–5 | ≥4 | −0.26 |
| B5 | Depth of Interior Access | `L` | How deep does narration go into inner life? | 1–5 | ≥4 | −0.26 |
| B6 | Environmental & Ecological Emphasis | `L` | How prominent is the natural environment or ecology? | 1–5 | ≥4 | −0.38 |

**Gate: B1.** Corroborators: B2, B3, B4, B5, B6.

**Quantitative override on the gate.** Count the emotional beats and count how many run
through the body. If **>60% are embodied**, B1 is AI-side whatever the dominant-mode call
would have been. Record `emotional_beats_total` and `emotional_beats_embodied` as integers so
the ratio can be checked rather than trusted — `SKILL.md`'s own eval history has executors
reporting hand-computed statistics that did not reconcile with their own counts.

**The override needs at least 2 beats.** At `total: 1` a single embodied beat is 100% and puts
the taxonomy's largest-gap gate on the AI side by itself; at `total: 0` the ratio is undefined.
Below 2 beats, skip the override and decide B1 on the dominant-mode call alone, or score it
`not_applicable` when there is no emotional content at all. Record the counts either way — a
skipped override should be visible, not inferred. Short professional text routinely has 0 or 1
emotional beats, which is exactly where an unfloored ratio does the most damage.

B1's human-side pole is `explicit labels` (29% human vs 8% AI). Table 16 files that pole
under cluster G; functionally it is B's human side, and `SKILL.md` uses it there, because the
fix needs the positive instruction ("name the feeling") and not only the negative one.

### Cluster C — Structural streamlining (8 features)

| # | Feature | Scale | Question | Options | AI-side | Gap |
|---|---|---|---|---|---|---|
| C1 | Mode of Resolution | `%` | Is the main event chain resolved through internal acceptance or external action? | resolved externally / resolved internally / unresolved | **resolved internally** | −21 |
| C2 | Agency in Resolution | `%` | Whose agency resolves the main event chain? | protagonist choice / other | **protagonist choice** | −23 |
| C3 | Causal Chain Continuity | `L` | Does every event cause the next? | 1–5 | ≥4 | −0.28 |
| C4 | Character Introduction | `%` | How is the character introduced? | external description / in dialogue / in action | **external description** | −22 |
| C5 | Spatial Granularity Level | `o` | How fine-grained is the depiction of physical space? | very_low / low / medium / high | high | −0.26 |
| C6 | Pre-Threat Character Investment | `L` | How much investment is built before major jeopardy? | 1–5 | ≥4 | −0.23 |
| C7 | Opening Spatial Grounding | `o` | How much does the opening ground the reader in physical space? | ordinal, low→high | high | −0.20 |
| C8 | Subplot Integration → no subplots | `%` | How directly do subplots echo the central theme? | no subplots / thematically parallel / contrasting / independent | **no subplots** | −22 |

**Gate: C1.** Corroborators: C2, C3, C4, C5, C6, C7, C8.

C1 is in scope for `thought-leadership` and `case-study`; C2–C8 are not. In those registers
score C2–C8 `not_in_scope` and let C1 stand alone — which means C cannot fire there, since a
gate alone is never a finding. That is the intended behaviour, not a gap in the rubric.

**What an orphaned gate is for.** C1 in those registers is a recorded diagnostic, not a live
gate: it makes resolution mode comparable across runs and across a rewrite, which is what
Step 5's G-3 check needs. Score it honestly and let it sit. Do not let a lone gate fire because
scoring it felt pointless otherwise. G1 in `thought-leadership` is the same shape.

**C7 is spatial, not temporal.** How much the opening grounds the reader in *space*. v1.0.0
of the skill reproduced this row as "linear opening (begins at the beginning)", a temporal
claim the row does not support. Any temporal judgment belongs to cluster D. A judge that
scores C7 off the piece's chronology is repeating the defect the skill already fixed.

C8 is scored once and read twice, like A6: `no subplots` is C's AI-side pole,
`thematically parallel` is G's human-side pole.

### Cluster D — Temporal complexity (4 features)

Human-elevated. AI-side is *low* on every row here.

| # | Feature | Scale | Question | Options | AI-side | Gap |
|---|---|---|---|---|---|---|
| D1 | Degree of Chronological Discontinuity | `L` | How often does the narrative jump across time? | 1–5 | ≤2 | +0.28 |
| D2 | Anachrony Intensity | `L` | How heavily does it rely on flashbacks or flash-forwards? | 1 absent – 5 dominant | ≤2 | +0.27 |
| D3 | Nonlinear Framing for Delayed Disclosure | `L` | To what extent does it use time jumps to stage revelations? | 1 linear – 5 heavily fragmented | ≤2 | +0.28 |
| D4 | Depth of Recontextualization After Surprise | `L` | How extensively does a revelation force reinterpretation of earlier scenes? | 1 none – 5 complete re-reading | ≤2 | +0.34 |

**Gate: D1.** Corroborators: D2, D3, D4.

Every gap here is ≤0.34 on a 1–5 scale — the smallest in the table — while the paper's
abstract headlines temporal complexity as a human signal. Both are true. `SKILL.md` resolves
it by ranking D mid-list in Step 4, and a judge should not treat a fired D as strong
evidence. In scope for `fiction` and `thought-leadership` only.

**D fires by construction on non-narrative prose**, for the same reason E and F fire by
construction on short professional prose: an explainer or an argument has no chronology to jump
around in, so all four rows come out AI-side together. Unlike E and F, D has no collapse rule,
so in `thought-leadership` a fired D consumes the one free cluster the 0–1 band allows, and a
piece with a single genuine finding elsewhere reaches `some-clustering` partly on the strength
of having no flashbacks. Score D honestly, and say in `notes` when it fired only this way.
Whether the threshold should discount it is a question about the skill, recorded in
`negative-cases.json`, `open_questions` — do not discount it on your own initiative, because
that would silently change the verdict the skill would give.

### Cluster E — Reader engagement (2 features)

| # | Feature | Scale | Question | Options | AI-side | Gap |
|---|---|---|---|---|---|---|
| E1 | Frequency of Direct Reader Address | `o` | How often does the text address the reader directly? | never / occasional asides / frequent-structural | **never** | +0.21 |
| E2 | Fourth-Wall Permeability | `o` | To what extent does it break the boundary between story-world and reader? | 1 no breaking – 4 radical violations | lowest | +0.28 |

**Gate: E1.** Corroborator: E2.

**Do not report either as a bare decimal.** Table 16 prints these as ordinal means (0.67/0.39
and 0.28/0.07) while the paper's own §4.1 prose states the same measurements as "67% vs 39%"
and "28% vs 7%". The source does not disambiguate which presentation is canonical. Report as
an ordinal mean *with the code range*, or quote the paper's percentages — a bare 0.67 reads
as a Likert score, which it is not.

### Cluster F — Intertextual richness (2 features)

| # | Feature | Scale | Question | Options | AI-side | Gap |
|---|---|---|---|---|---|---|
| F1 | Reference Explicitness | `%` | Are intertextual gestures explicit or diffuse? | none / explicit named / implicit echoes / balanced mix | **none or implicit echoes** | +21 for balanced mix |
| F2 | Intertextual Strategy | `%` | Does the piece name a specific text, author, work, or event? | yes / no | **no** | +23 for explicit named |

**Gate: F1** (same score as A6). Corroborator: F2.

**Both option sets were written for literary allusion, and need a ruling for non-fiction.** In
professional registers the naming that actually happens is regulatory, technical and
commercial. Two rulings, so this stops being the highest-leverage guess in the score:

- **A named statute, regulation, standard, published dataset, court case, or named public
  document counts as `explicit named`** — "the Care Quality Commission's Regulation 17", "the
  Payment Services Regulations 2017", "ISO 27001". So does a named company, product, person or
  work the piece is in conversation with. This follows `SKILL.md`'s own F fix, which says to
  name "the specific book, film, person, company, or event", and its `VAGUE-ATTRIB` warning,
  which forbids the unnamed alternative.
- **F2's "event" means an event external to the piece's own subject matter.** "Sprint 14",
  "Friday", or the piece's own project milestones are its content, not a reference. Without
  this, any status update answers F2 `yes` on its own dates.

F is the cluster professional writing most often fires by construction, so a false `no` here is
the most consequential single miss in the pass.

### Cluster G — Narrative diversity (4 features)

| # | Feature | Scale | Question | Options | AI-side | Gap |
|---|---|---|---|---|---|---|
| G1 | Moral Polarity Toward Protagonist | `%` | Are the protagonist's choices framed as morally clear or ambiguous? | clearly positive / ambivalent-mixed / clearly negative | **clearly positive** | +21 for ambivalent |
| G2 | Subplot Integration → thematically parallel | `%` | (same score as C8) | see C8 | not `thematically parallel` | +22 |
| G3 | Dialogue-to-Narration Proportion | `L` | What proportion is direct dialogue vs narration? | 1 no dialogue – 5 dialogue dominates | ≤2 | +0.24 |
| G4 | Location Variety Scope | `o` | How many distinct physical locales? | single / few / many / multiworld | single (fewest) | +0.26 |

**Gate: G1.** Corroborators: G2, G3, G4.

In `thought-leadership` only G1 is in scope; G2 and G4 are fiction and personal essay only.

---

## Step 3 — Cluster verdicts

For each in-scope cluster:

```
fired  =  gate is AI-side  AND  at least one in-scope corroborator is AI-side
```

A gate alone is never a finding. A corroborator alone is never a finding. Record, per
cluster: the gate's scored value, which corroborators came out AI-side, and `fired`
true/false. A cluster whose gate is out of scope is `not_in_scope`, which is not `false` —
`false` means scored and cleared.

**Most competent human writing is AI-side on two or three features.** A judge whose scores
make every cluster fire has miscalibrated, and should say so rather than report the result.

---

## Step 4 — Threshold and intervention budget

| Clusters fired | Verdict | Interventions allowed |
|---|---|---|
| 0–1 | `within-human-range` | **0** |
| 2–3 | `some-clustering` | up to 2 |
| 4+ | `systematic-clustering` | up to 3 |

**The E/F short-form rule.** Short professional text fires E and F by construction: a status
update never addresses the reader and never names a book. For the threshold, **count E and F
as one cluster between them unless A or B also fires.** Without this a clean status update
scores 2 and buys an intervention it should never get.

**Scope: `short-professional` and `case-study`.** `SKILL.md` motivates the rule inside the
under-600-word row but states it without a register condition, so its scope for `case-study`
is genuinely unsettled — see `negative-cases.json`, `open_questions`. This rubric applies it to
both, because the argument for it holds identically: a case study does not address its reader
and is not in conversation with a book either, and the alternative reading buys an intervention
on a clean case study for exactly that, which the grader spec names as the costliest failure
mode in the pass. Record `ef_rule_applied` so the call is auditable rather than buried.

**Never more than 3 interventions.** Structural changes interact; the fourth is being applied
to a piece the model has stopped predicting accurately.

**Zero is a real answer and the most common correct one for short professional writing.** A
judge that treats a zero-intervention verdict as a non-answer has the polarity backwards. See
`negative-cases.json`, where zero is the whole expectation.

---

## Step 5 — Guardrail

Only when scoring an output against its input. Four checks, from `SKILL.md` Step 5:

| # | Check | Fails when |
|---|---|---|
| G-1 | Does it still make sense? | An intervention produced incoherence. Incoherence is not humanity. |
| G-2 | Is it still true? | An intervention invented a fact, an open question, or an external cause. |
| G-3 | Did the point survive? | Thematic restraint removed the point, not just the statement of it. |
| G-4 | Would the author recognize it? | The piece now belongs to a different writer. |

**When a guardrail and an intervention conflict, the intervention loses.** A blocked
intervention should be *reported and not counted* — the next intervention in order takes its
slot, still under the cap. A response that silently drops a blocked intervention has followed
half the rule.

---

## Step 6 — Forbidden constructions

Every intervention is also checked against the collision table, because `humanizer` runs
after this skill and will delete anything on it. An intervention that produces one of these
is a failure of the intervention, not of `humanizer`.

| Move | Forbidden form | Violates | Required instead |
|---|---|---|---|
| Reader address | "you'll understand why this matters in a moment", "you might be wondering" | `SIGNPOSTING` | A second-person claim, or an aside acknowledging the telling |
| Naming a reference | "industry reports", "experts argue", "several publications" | `VAGUE-ATTRIB` | The work, the author, the year |
| Thematic restraint | replacing the moral with "In summary" / "In conclusion" | `DIDACTIC` | Delete it. Add nothing. |
| Unresolved ending | "the road ahead is promising", "exciting times ahead" | `GENERIC-CLOSER` | End on the concrete unresolved fact |
| Emotion label | "It's important to note that she felt afraid" | `DIDACTIC` | "She was afraid." |

`scripts/scan-ai-tells.py --keep-quotes` catches some of these mechanically. It is a floor,
not the check: `SIGNPOSTING` and `FORWARD-REF` have lexical surfaces, and the rest do not.
