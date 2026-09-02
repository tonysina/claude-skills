---
name: human-narrative
description: |
  Audit writing for AI-elevated narrative patterns and guide structural rewrites to make
  it read as human-authored. Operates at the scene and story structure level — temporal
  order, thematic restraint, resolution mode, emotional expression, intertextual reference.
  Complements humanizer (surface/lexical) and farnsworth-rhetoric (sentence craft).

  Triggers: "does this read like AI at the structural level", "humanize the narrative",
  "make this story read more human", "audit narrative structure", "this feels too neat/tidy",
  "why does this feel AI-written even after editing", "make this essay less formulaic",
  "this feels over-explained", "the ending is too tidy", "human-narrative"

  Do NOT use for: surface-level AI tells (use humanizer), sentence-level craft
  (use farnsworth-rhetoric), grammar or style-only fixes, technical documentation,
  runbooks, process instructions, data reporting, legal language, or RFP answers.
metadata:
  version: 1.1.1
---

# Human-Narrative: Structural AI Pattern Removal

Audit and rewrite at the narrative structure level — where AI patterns survive surface
editing. Based on the 30 core features from StoryScope (Russell et al., COLM 2026), which
separate AI from human fiction using discourse structure rather than style.

**This skill does not touch sentences.** It diagnoses and rewrites at the scene, section,
and structural level. Run `humanizer` after this skill, `farnsworth-rhetoric` last.

---

## What this optimizes, and what it doesn't

The features come from a **detection** study. They describe where published human fiction
and five LLMs sit differently in narrative space. They do not describe good writing.

Three consequences that govern every step below:

1. **Matching the human distribution is a proxy, not the goal.** An intervention that moves
   a piece toward human structural variance and makes it worse has failed. See Step 5.
2. **Every feature is a population base rate, not a diagnosis.** 57% of *published human*
   stories have no subplots. 52% state their theme narratorially. 46% resolve on the
   protagonist's choice. Any single AI-side feature is near-worthless evidence about one
   piece, which is why Step 2 requires corroboration and Step 3 requires a threshold.
3. **The evidence base is ~5,000-word literary short fiction.** Everything this skill says
   about executive summaries, LinkedIn posts, case studies, and work collateral is
   extrapolation across both genre and a 10–15× length gap. The register table in Step 1
   is where that extrapolation is bounded; it is judgment, not evidence.

---

## Step 1 — Register triage

| Register | Clusters in scope | Never |
|---|---|---|
| Fiction, personal essay, narrative journalism | All (A–G) | — |
| Thought leadership, opinion, keynote narrative | A, B, D, E, F, C1, G-moral | C2, subplots, location variety |
| Case study, customer story, customer-facing narrative | A, B, E, F, C1 | C2, D, G |
| Executive summary, status update, email, slide copy (<600 words) | A, B, E, F | C, D, G |
| Technical docs, runbooks, process instructions, data reporting, legal, RFP answers | **Hard stop.** Do not run. | — |

If the register is a hard stop, say so and stop. Do not produce a partial audit.

**Length is not the mode; register is.** A 2,000-word runbook is still a hard stop. A
400-word personal essay still gets D if the author wants it.

---

## Step 2 — Cluster scan

Seven clusters. For each in-scope cluster, answer the **gate** question, then check
**corroborators**. Answer with the option set given — not with prose.

**A cluster fires only if the gate is AI-side AND at least one corroborator is AI-side.**
A gate alone is not a finding.

Score honestly. Most competent human writing is AI-side on two or three features.

---

### A — Thematic over-determination

Largest cluster (6 features) and the strongest signal family.

**Gate.** *Does the narrator state what the piece means?* → yes / no. **AI-side: yes.**
(77% AI vs 52% human)

**Corroborators.**
- *How heavily does the piece foreground moral or philosophical questions?* 1–5. AI-side: ≥4
- *Does dialogue function as philosophical debate?* → yes / no. AI-side: yes (59% / 34%)
- *Do all elements serve one theme?* 1–5. AI-side: ≥5
- *Are intertextual gestures explicit or diffuse?* AI-side: implicit echoes (72% / 50%)

**Fix.** Delete the thematic statement, or move it earlier where it reads as premise rather
than verdict. Add nothing in its place. If dialogue debates the theme, give the characters
a concrete disagreement and let the theme sit under it.

**Cheapest cluster to fix — it is pure deletion, and the result is better writing by any
standard, not just by distribution match.**

---

### B — Sensory and embodied performativity

Contains the single largest gap in the whole taxonomy (−42pp).

**Gate.** *How are emotions most commonly conveyed?* → explicit labels / embodied metaphors
/ behavioral cues / ambiguous. **AI-side: embodied metaphors** (81% AI vs 38% human).
Human-side: explicit labels (29% human vs 8% AI).

**Quantitative rule.** Count emotional beats. If **>60% run through the body**, the gate
is AI-side regardless of the dominant-mode call.

**Corroborators.**
- *Does setting mirror the character's inner state?* 1–5. AI-side: ≥4 (4.07 / 3.58)
- *Is there smell-based imagery?* → yes / no. AI-side: yes (82% / 57%)
- *Sensory density* 1–5. AI-side: ≥4 (3.93 / 3.66)
- *How deep does narration go into inner life?* 1–5. AI-side: ≥4 (3.93 / 3.67)
- *How prominent is the natural environment?* 1–5. AI-side: ≥4 (3.21 / 2.83)

**Fix.** Convert one embodied passage to a direct emotion label. Let one setting be neutral
or incongruent with the character's state. Do not convert them all — human writing mixes
labels, embodied moments, and behavioral cues; the AI signal is *systematic* reliance on
one mode.

**This fix runs against "show, don't tell." That is what the evidence says: human authors
name feelings more than three times as often as AI does. Apply it once, not everywhere.**

---

### C — Structural streamlining

Split by cost. **C1 is available in non-fiction; C2 is fiction and personal essay only.**

**Gate.** *Is the main event chain resolved through the protagonist's own choice or internal
understanding?* → externally / internally / unresolved. **AI-side: internally.**
(protagonist-choice agency 69% / 46%; internal-understanding resolution 47% / 27%)

**Corroborators.**
- *Do subplots echo the central theme?* → no subplots / thematically parallel / contrasting
  / independent. AI-side: no subplots (79% / 57%)
- *Does every event cause the next?* 1–5. AI-side: ≥4 (4.20 / 3.92)
- *How is the main character introduced?* → external description / in dialogue / in action.
  AI-side: external description (52% / 30%)
- *How much investment is built before major jeopardy?* 1–5. AI-side: ≥3 (2.99 / 2.76)
- *Opening spatial grounding* and *spatial granularity*, ordinal. AI-side: higher
  (2.33 / 2.12 and 2.53 / 2.27)

**C1 fix — all registers except hard stops.** Move the resolution from internal realization
to partial, external, or delayed. Leave one thread unresolved.

> **Truth constraint.** In non-fiction you may only leave unresolved what is *actually*
> unresolved, and you may only externalize a resolution that was *actually* external. You
> cannot invent an open thread in a case study. If you don't know the fact, flag the
> intervention for the author instead of executing it.

**C2 fix — fiction and personal essay only.** Break a causal link. Introduce a character
mid-action rather than by description. Add a subplot.

---

### D — Temporal complexity

The paper's headline human signal. Also the smallest measured gaps in the table — all four
are ≤0.34 on a 1–5 scale — and the most invasive intervention available. Treat the strength
of this cluster as modest and its cost as high.

**Gate.** *How often does the narrative jump across time?* 1–5. **AI-side: ≤2**
(human 2.40 / AI 2.12)

**Corroborators.**
- *Reliance on flashbacks or flash-forwards* 1–5. AI-side: ≤2 (2.58 / 2.31)
- *Time jumps used to stage revelations* 1–5. AI-side: ≤2 (1.96 / 1.68)
- *Does a revelation force reinterpretation of earlier scenes?* 1–5. AI-side: ≤3
  (3.28 / 2.95)

**Fix.** Open at the most charged moment and let the piece work backward from it. Delay one
piece of information that would explain an earlier event. One disruption, not several.

---

### E — Reader engagement

**Gate.** *How often does the text address the reader directly?* → never / occasional asides
/ frequent-structural. **AI-side: never.** (see scale note in `references/features.md`)

**Corroborator.** *Does the text break the boundary between story-world and reader?*
ordinal. AI-side: lowest.

**Fix.** One second-person claim about the reader's own experience, or one aside that
acknowledges the telling.

> **Do not use a forward-reference announcement.** "You'll understand why this matters in a
> moment," "you might be wondering," "here's what you need to know" are `humanizer`
> `SIGNPOSTING`, and `humanizer` runs after this skill and will delete them. Address the
> reader about something, don't announce structure.

---

### F — Intertextual richness

**Gate.** *Are intertextual gestures explicit or diffuse?* → none / explicit named /
implicit echoes / balanced mix. **AI-side: none or implicit echoes** (implicit 72% AI vs
50% human).

**Corroborator.** *Does the piece name a specific text, author, work, or event?* → yes / no.
AI-side: no (explicit named reference 47% human vs 24% AI).

**Fix.** Name the specific book, film, person, company, or event the piece is in
conversation with. Give the author and, where it matters, the year.

**Highest value-per-effort cluster for professional writing.** It is a one-clause change,
it works at any length, and it improves the piece independent of any distribution argument.

> Two constraints. Naming a real source means the claim about it must be right — run
> `source-check` before publishing. And do not substitute "industry reports," "experts
> argue," or "several publications," which is `humanizer` `VAGUE-ATTRIB`.

---

### G — Narrative diversity

**Gate.** *Does the piece frame the protagonist's choices as morally clear or ambiguous?*
→ clearly positive / ambivalent-mixed / clearly negative. **AI-side: clearly positive**
(ambivalent 59% human vs 38% AI).

**Corroborators.**
- *Subplot integration* → AI-side: no subplots; human-side: thematically parallel (42% / 21%)
- *Proportion of direct dialogue vs narration* 1–5. AI-side: ≤2 (2.95 / 2.70)
- *How many distinct locations?* ordinal. AI-side: fewer (1.34 / 1.08)

**Fix.** Find the moral center and complicate it: a character who is right and wrong at
once, a resolution that solves one problem and creates another, one element the piece
declines to editorialize about. Raise the dialogue-to-narration ratio.

The moral-ambiguity fix is available in thought leadership. Subplots and location variety
are fiction and personal essay only.

---

## Step 3 — Threshold

| Clusters fired | Verdict | Interventions |
|---|---|---|
| 0–1 | Reads within human structural range | **None.** Report and stop. |
| 2–3 | Some AI-side clustering | Up to **2** |
| 4+ | Systematic AI-side clustering | Up to **3** |

**Never more than 3 interventions in one pass.** Three well-chosen structural changes
exceed six, and structural changes interact — the fourth is being applied to a piece you
have already stopped modelling accurately.

**Zero fired clusters is a real answer and the most common correct one for short
professional writing.** Say the piece reads within human range and stop. Do not manufacture
findings to fill a report.

**Short professional text fires E and F by construction.** A status update, an email, or
slide copy never addresses the reader and never names a book, so in the under-600-word row
E and F come out AI-side on almost every piece. Together they do not reach the intervention
bar on their own: for the threshold, count E and F as one cluster between them unless A or
B also fires. Then a status update with only E and F scores 1, which is "within human
range," which is the answer the paragraph above already gives.

**Report in proportion to the input.** Under 100 words, a one-paragraph verdict with the
clusters named in a sentence. No table, no corpus percentages.

---

## Step 4 — Intervention order

Ordered by evidence strength × reversibility. Take from the top; stop at the cap.

**Long-form:** A (thematic restraint) → B (emotional rebalance) → F (name the reference) →
D (temporal) → E (reader address) → C (resolution mode) → G (moral ambiguity)

**Short-form and case study:** A → B → F → E

A leads because it is a deletion with the largest cluster behind it. C and G come last
because they are the most invasive and the most register-constrained. D sits mid-list rather
than first: v1.0.0 ranked it first on the strength of the paper's framing, but its measured
gaps are the smallest in the table and it is out of scope for every non-fiction register.

Execute one at a time. After each, state what changed structurally and what it costs the
piece downstream.

---

## Step 5 — Guardrail: keep the piece, drop the intervention

Before accepting any rewrite, check:

1. **Does it still make sense?** "Break one causal link" and "leave a thread unresolved" are
   instructions that can produce incoherence. Incoherence is not humanity.
2. **Is it still true?** No intervention may invent a fact, an open question, or an external
   cause that isn't there. See the truth constraint under C1.
3. **Did the point survive?** Thematic restraint removes the statement of the point, not the
   point. If deleting the moral leaves the reader unable to reconstruct it, the deletion was
   too deep — restore less than you removed.
4. **Would the author recognize it?** Structural changes are large. If the piece now belongs
   to a different writer, stop and hand the finding back.

**When a guardrail and an intervention conflict, the intervention loses.** Report the finding
and say why you didn't act on it. A blocked intervention is reported, not counted: the next
intervention in order takes its slot, still under the Step 3 cap.

---

## Forbidden constructions

Default forms of these moves collide with `humanizer`, which runs after this skill.

| Move | Do not produce | Violates | Use instead |
|---|---|---|---|
| Reader address | "you'll understand why this matters in a moment", "you might be wondering" | `SIGNPOSTING` | A second-person claim, or an aside acknowledging the telling |
| Naming a reference | "industry reports", "experts argue", "several publications" | `VAGUE-ATTRIB` | The work, the author, the year |
| Thematic restraint | replacing the moral with "In summary" / "In conclusion" | `DIDACTIC` | Delete it. Add nothing. |
| Unresolved ending | "the road ahead is promising", "exciting times ahead" | `GENERIC-CLOSER` | End on the concrete unresolved fact |
| Emotion label | "It's important to note that she felt afraid" | `DIDACTIC` | "She was afraid." |

The "Violates" column uses `humanizer`'s stable pattern IDs, not its display numbers.

If `humanizer` runs afterward and deletes something this skill added, `humanizer` is right.
Do not re-add it.

---

## Worked example

Register: thought leadership. Clusters in scope: A, B, D, E, F, C1, G-moral.

**Before** (152 words)

> When our largest client's integration failed three days before their board review, I felt
> my chest tighten. The smell of burnt coffee filled the war room as the team stared at
> dashboards that told us nothing. Outside, rain streaked the windows, matching the mood in
> the room.
>
> We worked through the night. By morning, I understood something I had been avoiding for
> years: our architecture had grown faster than our discipline. That realization changed how
> I lead. The lesson is that technical debt is never really technical — it is a record of
> every decision we deferred. Once I accepted that, the fix became obvious, and we shipped a
> working integration with four hours to spare.

**Scan**

| Cluster | Gate | Corroborators | Fired |
|---|---|---|---|
| A | states the theme: yes | moralizing 4; thematic unity 5 | ✅ |
| B | embodied; 3 of 3 beats through the body | olfactory yes; setting-as-mirror 5 | ✅ |
| C | resolved internally | causal continuity 4 | ✅ |
| D | chronological discontinuity 1 | anachrony 1; delayed disclosure 1 | ✅ |
| E | never addresses the reader | fourth wall lowest | ✅ |
| F | none | no named reference | ✅ |
| G | clearly positive | dialogue-to-narration 1 | ✅ |

7 fired → cap 3. Taking A, B, F in order.

**After** (108 words)

> When our largest client's integration failed three days before their board review, I was
> afraid.
>
> We worked through the night in a room with four dashboards, none of which told us where the
> failure was. By morning we had found it: a retry policy written in 2021 by someone who had
> since left, doing exactly what it was designed to do.
>
> Fred Brooks argued in *The Mythical Man-Month* that conceptual integrity requires a system
> be designed by as few minds as possible. Our integration had eleven.
>
> We shipped with four hours to spare.

**What changed**

- **A.** Deleted "That realization changed how I lead" and "The lesson is that technical debt
  is never really technical." The Brooks paragraph now carries the idea without stating it.
  Gate: yes → no.
- **B.** "I felt my chest tighten" → "I was afraid." Deleted the burnt coffee (olfactory) and
  the rain matching the mood (setting-as-mirror). Embodied share of emotional beats: 3/3 → 0/1.
- **F.** Added Brooks and *The Mythical Man-Month*. Reference explicitness: none → explicit
  named.

**Not taken**

- **C1** was next in order and the cap was reached. "Once I accepted that, the fix became
  obvious" was an internal-understanding resolution; the honest version is that the retry
  policy was never removed, which would end the piece unresolved. **Flagged rather than
  executed, because it depends on a fact the author has and the editor doesn't** (truth
  constraint, C1).
- **D, E, G** fired but fall below the cap. **C2** and G's subplot and location fixes are out
  of scope for this register.

**Watch downstream.** The piece now names a real book, so the Brooks paraphrase has to be
checked against the source before it ships — run `source-check`. And "I was afraid" is now
the only emotional statement in the piece; if a later editing pass softens it, cluster B
returns.

---

## Output format

**Diagnosis only.** The cluster table from Step 2 — gate call, corroborators, fired or not.
Then the Step 3 verdict. For each fired cluster, quote or locate the instance and name the
available intervention. Order by the Step 4 sequence. Offer to execute. Report gaps with
their units (percentage points, or Likert means on a 1–5 scale); never a bare decimal.

**Full audit + rewrite.** Cluster table, verdict, then interventions one at a time up to the
cap. After each: what changed, what it cost, what to watch. Close with what you did not take
and why — cap, register, or guardrail. Don't polish sentences; that's `humanizer`'s job.

**Targeted intervention.** Score the named cluster only. Execute if it fires and the register
allows. Note downstream effects.

---

## Workflow position

```
Long-form:   human-narrative → humanizer → farnsworth-rhetoric
Short-form:  human-narrative (A, B, E, F only) → humanizer → farnsworth-rhetoric
Hard stops:  none of the three
```

`humanizer` runs after and has final say on any construction this skill introduces.

---

## Common issues

**Don't hunt for gates.** If a cluster's gate is human-side, move on. Do not re-read looking
for a reason to fire it.

**A flag is not a finding.** Gate plus corroborator, then the Step 3 threshold. A piece can
be AI-side on four individual features and still sit inside the human distribution, because
these are base rates over 61,608 stories and not tests on one document.

**Some AI patterns are the assignment.** A clean resolution may be what the piece is for. A
stated thesis may be the point of a thesis-driven essay. Flag and ask rather than silently
restructuring.

**Zero interventions is the expected result for short professional writing.** See Step 3.

**This skill doesn't replace humanizer.** AI vocabulary, em dash overuse, promotional
language, rule of three: not this skill's concern. Run `humanizer` after.

---

## Source

Russell, J., Rajendhran, R., Pham, C.M., Iyyer, M., & Wieting, J. (2026). *StoryScope:
Investigating idiosyncrasies in AI fiction.* COLM 2026. arXiv:2604.03136v6.

- **Corpus.** 10,272 human-written short stories extracted from Books3 short-story
  anthologies — published literary fiction — each paired with five LLM retellings of the same
  prompt (Claude, DeepSeek, Gemini, GPT, Kimi). 61,608 stories, **~5,000 words each** (mean
  target 6,242 / median 5,000), 304 extracted features per story.
- **Detection.** The full 257-feature narrative model reaches **93.2% macro-F1**. The **30
  core features this skill uses reach 84.8%** — slightly below style-only features (85.8%)
  and well below raw-text baselines (TF-IDF+XGBoost 99.7%, ModernBERT 99.9%). The core set's
  contribution is interpretability and edit-robustness, not raw detection power.
- **Robustness (§4.2).** After LAMP span-level artifact rewriting on 278 Gemini stories, the
  narrative model still detects them at **93.9% macro-F1 vs 95.5% unedited — a 1.6-point
  drop.** This is the result that justifies a structural skill separate from `humanizer`.
- **Feature tables.** Table 14 (20 AI-characterizing features), Table 15 (13
  human-characterizing), Table 16 (all 30 with human/AI means and gaps). Full reproduction,
  with scales and the eight features not used inline, in `references/features.md`.
