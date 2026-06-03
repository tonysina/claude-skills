---
name: human-narrative
description: |
  Audit writing for AI-elevated narrative patterns and guide structural rewrites to make
  it read as human-authored. Operates at the scene and story structure level — temporal
  order, thematic restraint, subplot architecture, character interiority, resolution mode.
  Complements humanizer (surface/lexical) and farnsworth-rhetoric (sentence craft).

  Triggers: "does this read like AI at the structural level", "humanize the narrative",
  "make this story read more human", "audit narrative structure", "this feels too neat/tidy",
  "why does this feel AI-written even after editing", "make this essay less formulaic",
  "add depth to this story", "this feels over-explained", "human-narrative"

  Do NOT use for: surface-level AI tells (use humanizer), sentence-level craft
  (use farnsworth-rhetoric), grammar or style-only fixes.
metadata:
  version: 1.0.0
---

# Human-Narrative: Structural AI Pattern Removal

Audit and rewrite writing at the narrative structure level — where AI patterns survive
surface editing. Based on Core feature taxonomy from StoryScope (Russell et al., 2026),
which identified 30 structural features that distinguish AI from human writing with 93%
detection accuracy, stable even after aggressive style editing.

**This skill does not touch sentences.** It diagnoses and rewrites at the scene,
section, and structural level. Run humanizer after this skill, farnsworth-rhetoric last.

---

## How to Use This Skill

When given writing to audit or restructure:

1. Read the full piece before responding
2. Determine mode: **long-form** or **short-form** (see below)
3. Run the AI-elevated checklist — flag each pattern present with a specific example
4. Run the human-elevated checklist — flag each absent pattern worth introducing
5. Produce 3–5 prioritized structural interventions (not line edits)
6. Offer to execute one intervention at a time if the user wants rewrites

### Use Cases

**Diagnosis only:** User asks "does this read like AI at the narrative level?" or "why does this feel formulaic?" Scan both checklists, report findings with specific examples from the text, and offer intervention options. Don't rewrite unless asked.

**Full structural audit + rewrite:** User says "human-narrative this" or "restructure this to read more human." Run both checklists, propose and execute the top 3 structural interventions. Describe what changed and why after each one.

**Targeted intervention:** User identifies a specific issue ("this feels too neat," "the ending is too tidy," "the theme is too heavy-handed"). Focus the audit on that dimension and propose targeted structural fixes.

---

## Modes

### Long-Form Mode
*For: fiction, essays, case studies, thought leadership articles, narrative journalism, LinkedIn articles (>600 words)*

Apply the full checklist — all AI-elevated and human-elevated patterns. Both structural and thematic signals apply.

### Short-Form Mode
*For: LinkedIn posts (<600 words), executive summaries, emails, work collateral, slide copy*

**Apply only:**
- Thematic over-determination signals (moralizing, tidy resolution, philosophical weight)
- Emotional expression mode (embodied vs. explicit label)
- Reader address / fourth-wall signals

**Skip:** Temporal complexity, subplot signals, setting-as-mirror, intertextual reference. These don't apply at short-form length.

---

## AI-Elevated Patterns to Suppress

These appear significantly more often in AI writing than human writing. Numbers are human vs. AI rates from StoryScope's 30-feature Core taxonomy (61,608 stories).

### Thematic Over-Determination

The strongest AI signal cluster. AI writing over-explains its own meaning, states its moral explicitly, and makes sure the reader cannot miss the theme.

| Pattern | AI rate | Human rate | Gap |
|---|---|---|---|
| Narratorial thematic commentary (narrator states the theme) | 77% | 52% | −25pp |
| Philosophical or debate-driven dialogue | 59% | 34% | −25pp |
| Explicit moral or lesson at scene/story end | AI 3.94 | Human 3.28 | −0.65 |
| High thematic unity (all elements serve one theme) | AI 4.74 | Human 4.41 | −0.33 |

**What to look for:** A narrator explaining what the story means. Characters having philosophical debates that articulate the theme. A conclusion that states the moral. Every scene neatly reinforcing a single message.

**Structural fix:** Remove or move the thematic statement. Let the reader infer. Introduce a counter-element that complicates the theme. If dialogue is philosophical, make it about something concrete instead — let the subtext carry the philosophy.

---

### Sensory and Emotional Performativity

AI conveys emotion through the body and sensory detail far more than humans do. Human writers are more likely to name the emotion directly.

| Pattern | AI rate | Human rate | Gap |
|---|---|---|---|
| Emotion expressed via physical sensation / embodied metaphor | 81% | 38% | −42pp |
| Olfactory (smell-based) imagery | 82% | 57% | −26pp |
| Setting used as psychological mirror of character state | AI 4.07 | Human 3.58 | −0.49 |
| High sensory density | AI 3.93 | Human 3.66 | −0.26 |

**What to look for:** Characters' hearts clenching, throats tightening, chests swelling. The smell of rain used as an emotional signal. Weather or setting that mirrors the character's mood. Paragraphs of physical sensation as a proxy for saying "she was afraid."

**Structural fix:** Cut one embodied-emotion passage and replace with a direct emotion label or an action that implies the emotion without announcing it through the body. Reduce setting-as-mirror: let the setting be neutral or incongruent with the character's state.

**Note:** One or two embodied moments are fine and often effective. The AI signal is *systematic overuse* — when every emotional beat goes through the body. Human writers mix direct labels, embodied moments, and behavioral cues.

---

### Structural Streamlining

AI stories are tidier than human stories. Problems get solved. Protagonists make choices that fix things. Subplots resolve or don't exist. Structure is linear.

| Pattern | AI rate | Human rate | Gap |
|---|---|---|---|
| No subplots | 79% | 57% | −22pp |
| Resolution driven by protagonist's internal choice | 69% | 46% | −23pp |
| Resolution via internal understanding / epiphany | 47% | 27% | −21pp |
| Character introduced via external description | 52% | 30% | −22pp |
| High causal chain continuity (every event causes the next) | AI 4.20 | Human 3.92 | −0.28 |
| Linear opening (begins at the beginning) | AI 2.33 | Human 2.12 | −0.20 |

**What to look for:** The protagonist has an epiphany that solves the conflict. Nothing is left unresolved. The story begins at the beginning and moves chronologically to a clean end. Characters are described before they act. Every scene follows causally from the last.

**Structural fix:** Introduce one unresolved thread. Have the resolution come from outside the protagonist's control, or be partial. Introduce a character in the middle of action rather than with a description. Break one causal link — let something happen that doesn't follow logically from what preceded it.

---

## Human-Elevated Patterns to Introduce

These appear significantly more often in human writing. Introducing them moves writing toward human narrative space.

### Temporal Complexity

The single most robustly human structural signal. Human writers scramble time; AI writers tell stories chronologically.

| Pattern | Human rate | AI rate | Gap |
|---|---|---|---|
| Chronological discontinuity | 2.40 | 2.12 | +0.28 |
| Nonlinear framing for delayed disclosure | 1.96 | 1.68 | +0.28 |
| Anachrony intensity (flashbacks, flash-forwards) | 2.58 | 2.31 | +0.27 |
| Deep recontextualization after a surprise | Human 3.28 | AI 2.95 | +0.34 |

**What to introduce:** Open in the middle. Start at the end and work backward. Let a revelation reframe everything that preceded it (and take time with that reframing). Drop a flash-forward that creates dramatic irony. Delay a piece of information that would explain earlier events.

**Structural intervention:** Identify the story's most emotionally charged moment. Move it to the opening. Let the narrative spiral backward from there rather than build toward it.

---

### Moral Ambiguity

Human writing tolerates unresolved moral complexity. AI writing resolves it.

| Pattern | Human rate | AI rate | Gap |
|---|---|---|---|
| Moral polarity → ambivalent/mixed | 59% | 38% | +21pp |

**What to introduce:** A character whose actions are right and wrong simultaneously. A resolution that solves one problem and creates another. A moral stance that the narrative neither endorses nor condemns. A "good" character who does something unkind. A "bad" character who does something generous.

**Structural fix:** Find the story's moral center and complicate it. Add one element that the narrative doesn't editorialize about — let it sit unresolved.

---

### Reader Address and Fourth-Wall Permeability

Human fiction writers acknowledge the reader far more than AI writers do.

| Pattern | Human rate | AI rate | Gap |
|---|---|---|---|
| Fourth-wall permeability (any acknowledgment of audience) | 0.67 | 0.39 | +0.28 |
| Direct reader address | 0.28 | 0.07 | +0.21 |

**What to introduce:** A "you" directed at the reader. A moment where the narrator acknowledges they are telling a story. An aside. A wink. This applies to essays and LinkedIn pieces as much as fiction — direct address is a strong humanizing signal in professional writing.

**Structural fix:** Add one moment of direct address or self-aware narration. Even a single "you'll understand why this matters in a moment" shifts the register significantly.

---

### Intertextual Reference

Human writers name their influences and reference other texts; AI writing keeps implicit echoes vague.

| Pattern | Human rate | AI rate | Gap |
|---|---|---|---|
| Explicit named intertextual reference | 47% | 24% | +23pp |
| Balanced mix of explicit and implicit reference | 37% | 16% | +21pp |

**What to introduce:** Name a specific book, film, person, or event the piece is in conversation with. Make the reference concrete rather than an unnamed "echo." This applies to essays and thought leadership as much as fiction.

---

### Location and Subplot Variety

Human stories move through more locations and carry parallel threads.

| Pattern | Human rate | AI rate | Gap |
|---|---|---|---|
| Location variety scope | 1.34 | 1.08 | +0.26 |
| Subplot integration → thematically parallel | 42% | 21% | +22pp |

**What to introduce:** A second location that contrasts with the first. A subplot that runs parallel to the main thread without being explicitly resolved against it. A secondary character whose situation echoes (but doesn't mirror) the protagonist's.

---

## Scanning Process

**Step 1 — Thematic audit:** Is the meaning stated or withheld? Does the narrator explain the theme? Does dialogue carry philosophical weight? Does the ending resolve the moral question cleanly? (Highest-gap signals; check first.)

**Step 2 — Emotional expression audit:** How is emotion conveyed? Embodied/physical, explicit label, or behavioral cue? Count the ratio. If >60% of emotional moments go through the body, flag it.

**Step 3 — Structural audit:** Does the protagonist's internal choice drive the resolution? Is there a single clean causal chain from start to end? Are there subplots? Does the opening begin chronologically?

**Step 4 — Temporal audit:** Does time move only forward? Are there flashbacks, flash-forwards, or moments that reframe earlier events? (Most robustly human signal — easy to introduce.)

**Step 5 — Reader/voice audit:** Does the narrator ever acknowledge the reader or the act of narration? Are there named intertextual references?

---

## Prioritizing Interventions

When multiple patterns are present, prioritize interventions in this order:

1. **Temporal complexity first** — highest human signal, most impactful structural move, can be introduced without rewriting the entire piece
2. **Thematic restraint second** — removing moralizing commentary changes how the whole piece feels
3. **Resolution mode third** — shifting from epiphany to external or partial resolution changes the ending
4. **Emotional expression fourth** — rebalancing embodied vs. explicit emotion
5. **Reader address last** — easiest to add, often high impact for professional writing

---

## Output Format

**Diagnosis only:**
A structured findings list. Each finding names the pattern, quotes or locates the instance in the text, gives the human/AI rate gap, and suggests a structural intervention. Order by gap size (highest-impact first). Offer to execute one or more interventions.

**Full audit + rewrite:**
Present findings first (brief), then execute interventions one at a time. After each intervention, note what changed structurally and why. Don't polish sentences — that's humanizer's job.

**Targeted intervention:**
Execute the specific structural fix. Note what changed and what downstream effects the user should watch for (e.g., "removing the moral commentary in paragraph 4 means the ending now needs to work harder — the final image carries all the thematic weight").

---

## Workflow Position

This skill operates at the structural level. Run it first when combining with other skills:

```
Long-form:   human-narrative → humanizer → farnsworth-rhetoric
Short-form:  humanizer → farnsworth-rhetoric
             (human-narrative optional; limit to thematic + emotion signals only)
```

---

## Common Issues

**Don't over-intervene.** The goal is to introduce human variance, not to make the piece incoherent. One strong temporal disruption is more effective than five. Flag what's present and let the user decide how far to go.

**Some AI patterns are intentional.** A clean resolution may be what the user wants. A thematic statement may be the piece's purpose. When in doubt, flag and ask rather than silently restructuring.

**Short professional writing needs a lighter touch.** For LinkedIn posts and work collateral, focus on thematic restraint and emotional expression only. Don't introduce temporal complexity or subplots into a 300-word post.

**This skill doesn't replace humanizer.** Surface patterns (AI vocabulary, em dash overuse, promotional language, rule of three) are not this skill's concern. After structural work is done, run humanizer to clean the surface.

---

## Source

Feature taxonomy and gap statistics from: Russell, J., Rajendhran, R., Pham, C.M., Iyyer, M., & Wieting, J. (2026). *StoryScope: Investigating Idiosyncrasies in AI Fiction*. arXiv:2604.03136v4. Core features (Table 15) identified via bootstrap SHAP analysis over XGBoost classifiers trained on 61,608 stories across 5 AI models and 10,272 human-written short stories.
