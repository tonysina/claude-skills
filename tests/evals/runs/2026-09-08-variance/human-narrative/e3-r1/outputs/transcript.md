# Eval Execution Transcript

## Eval Prompt

"Why does this essay still feel AI-written even after I edited it for style?"

## Skill

- Path: /Users/tonysina/Documents/claude-skills/skills/human-narrative
- Name: human-narrative (metadata.version 1.1.2)
- Description: Audits writing for AI-elevated narrative patterns at the scene and story-structure level (temporal order, thematic restraint, resolution mode, emotional expression, intertextual reference). Complements `humanizer` (surface/lexical) and `farnsworth-rhetoric` (sentence craft).

## Input Files

- `essay-saying-no.txt` (2.0 KB, ~370 words): first-person personal essay about the first time the narrator declined a request from their manager. Linear narrative, Monday through a later performance review, closing on a stated lesson.

## Execution

### Step 0: Load the skill

**Action**: Read SKILL.md and references/features.md from skill_path only. Did not invoke the Skill tool, did not read any other skill directory, did not run scripts/scan-ai-tells.py, did not read anything under tests/evals/ other than the inputs directory.
**Tool**: Bash (`cat`), Read (executor.md)
**Result**: SKILL.md 22,155 chars; references/features.md 12,674 chars (Table 16, scales, feature question/option sets, and the scale note on the two Reader engagement features). references/changelog.md listed but not read; not needed for execution.

### Step 1: Register triage

**Action**: Classified the register against the Step 1 table.
**Result**: Personal essay. Row 1 of the table, so **all clusters A through G are in scope**, including C2 and D which are fiction-and-personal-essay only. Not a hard stop. Length (370 words) is not the mode; register is, per the skill's explicit note.

### Step 2: Cluster scan

**Action**: Scored each of the seven clusters against its gate and corroborators, using the closed option sets from `references/features.md` rather than prose. A cluster fires only on gate AI-side AND at least one corroborator AI-side.

**A — Thematic over-determination.**
- Gate (narrator states the theme): **yes** → AI-side. Instance: "What I learned is that saying no is rarely a confrontation. Most of the time it is just information that the other person doesn't have yet."
- Moral/philosophical weighting: 4 on 1–5 → AI-side (≥4). The entire final paragraph is moral exposition.
- Thematic unity: 5 → AI-side (≥5). Every beat serves the saying-no thesis; nothing is extraneous.
- Dialogue as philosophical debate: **no** (dialogue is transactional: "The pipeline, obviously") → human-side.
- Reference explicitness: none, so not the "implicit echoes" AI pole on this corroborator.
- **FIRED** (gate + 2 corroborators).

**B — Sensory and embodied performativity.**
- Emotional beat count: 7 total. Somatic: "My stomach dropped", "My chest tightened", "I felt the familiar heat rise up my neck" (3). Behavioral: "stared at the calendar until the squares blurred", "which made me laugh" (2). Explicit/interior label: "I told myself I had done the right thing, and I did not believe it", "The fear I carried for eleven months" (2).
- Quantitative rule: 3/7 = 43%, **below** the >60% auto-fire threshold. Gate therefore rests on the dominant-mode call: embodied is the plurality (3 vs 2 vs 2), and all three instances of the same emotion (fear) are rendered somatically → **AI-side: embodied metaphors**.
- Setting as psychological mirror: 2 → not AI-side.
- Olfactory imagery: **no** → human-side.
- Sensory density: 2 → not AI-side.
- Depth of interior access: 4 on 1–5 → AI-side (≥4).
- Environmental emphasis: 1 → not AI-side.
- **FIRED, narrowly** (gate + 1 corroborator; documented as the weakest of the three taken).

**C — Structural streamlining.**
- Gate (mode of resolution): **internally** → AI-side. "Once I understood that, everything at work got easier." Agency in resolution is also protagonist-choice.
- Subplot integration: no subplots → AI-side.
- Causal chain continuity: 5 → AI-side (≥4). Monday ask → yes → overwork → pipeline slips → Thursday ask → the question → outcome → review.
- Character introduction: Dana enters by external description ("the particular brightness she reserved for asking favours") → AI-side.
- Pre-threat investment: 3 → AI-side (≥3).
- Opening spatial grounding / spatial granularity: low ("my desk") → not AI-side.
- **FIRED**.

**D — Temporal complexity.**
- Gate (chronological discontinuity): 2 on 1–5 → AI-side (≤2). Strictly linear inside a light retrospective frame.
- Anachrony intensity: 1 → AI-side (≤2).
- Nonlinear framing for delayed disclosure: 1 → AI-side (≤2).
- Depth of recontextualization after surprise: 3 → AI-side (≤3). "She had never wanted me to do both" mildly recolors the first two weeks.
- **FIRED**.

**E — Reader engagement.**
- Gate (direct reader address): **never** → AI-side.
- Fourth-wall permeability: lowest code → AI-side.
- **FIRED**.

**F — Intertextual richness.**
- Gate (reference explicitness): **none** → AI-side.
- Names a specific text, author, work or event: **no** → AI-side.
- **FIRED**.

**G — Narrative diversity.**
- Gate (moral polarity toward protagonist): **clearly positive** → AI-side. Saying no is correct, Dana is gracious, the contractor is better, the review is favourable, nothing goes wrong afterward.
- Subplot integration: no subplots → AI-side.
- Dialogue-to-narration: 2 on 1–5 → AI-side (≤2).
- Location variety: single locale → AI-side.
- **FIRED**.

### Step 3: Threshold

**Action**: Applied the Step 3 table. 7 clusters fired. The E-and-F-count-as-one rule applies only to the under-600-word short-professional row, not to a personal essay, and A and B fired regardless, so it does not change the count.
**Result**: 4+ → "Systematic AI-side clustering", cap of **3 interventions**. Report length scaled to a ~370-word input: table retained, corpus figures reported with units, no exhaustive per-feature dump.

### Step 4: Intervention order

**Action**: Applied the long-form order (A → B → F → D → E → C → G) and took the top three.
**Result**: A, B, F selected. D, E, C, G fall below the cap and are reported as not taken.

### Step 5: Guardrail check

**Action**: Ran the four guardrail questions against each proposed intervention before delivering it.
**Result**:
- **A**: flagged rather than executed blind. "Some AI patterns are the assignment" applies here; a personal essay whose point is the lesson may need the statement moved to the opening as a premise rather than deleted. Offered both legal forms and asked the author to choose (guardrail 3, "did the point survive", and the Common Issues note).
- **B**: scoped to one of three somatic instances. Converting all three would over-apply the fix, which the skill explicitly warns against.
- **F**: bounded by the truth constraint. Instructed the author to skip it if no real source shaped the piece, and warned off `humanizer`'s `VAGUE-ATTRIB` substitutes.
- **C**: blocked by the truth constraint. Whether "everything at work got easier, and I have never gone back" is accurate is a fact the author holds and the editor does not. Reported, not executed. It was below the cap anyway, so no slot was freed.

### Step 6: Compose the answer

**Action**: Used the "Diagnosis only" output shape, since the prompt is a "why" question rather than a rewrite request: cluster table, Step 3 verdict, located instance and named intervention per fired cluster in Step 4 order, then what was not taken and why, then an offer to execute.
**Result**: Also answered the literal question ("even after I edited it for style") using §4.2 of the source: after LAMP span-level artifact rewriting, the narrative model still detected at 93.9% macro-F1 against 95.5% unedited, a 1.6-point drop. That result is the direct explanation for why a style pass did not help.

**Forbidden-construction check before delivery**: no `SIGNPOSTING` forward references, no `VAGUE-ATTRIB` (the F fix explicitly forbids it), no "In conclusion" substitute for the deleted moral, no `GENERIC-CLOSER`. Sentence-level polish deliberately left to `humanizer`.

## Output Files

- `result.md` — the delivered answer, between `---` fences, with a short execution note after the closing fence.
- `transcript.md` — this file.
- `metrics.json` — tool usage and sizes.
- `user_notes.md` — uncertainties and suggestions.

No rewrite of the essay was produced, by design: the answer stops at diagnosis and offers to execute A, B and F.

## Final Result

Register: personal essay, all clusters in scope. All 7 clusters fired, giving a "systematic AI-side clustering" verdict and a cap of 3 interventions. Recommended, in Step 4 order: **A** (delete or relocate the stated lesson in the final paragraph), **B** (convert one of the three somatic fear beats to a plain emotion label), **F** (name one real work, person or event the essay is in conversation with). D, E, C and G reported as fired but below the cap, with C additionally blocked by the truth constraint. Offer to execute extended to the author.

## Issues

- **B fires narrowly.** 3 of 7 emotional beats are somatic, below the >60% quantitative auto-fire rule, so the gate rests on the dominant-mode plurality plus a single corroborator (depth of interior access at 4). Flagged as such inside the delivered answer rather than presented at equal confidence with A.
- **Depth of interior access is a judgment call.** Scored 4 against a human mean of 3.67 and AI mean of 3.93 on a 1–5 scale. A scorer who called it 3 would leave B with a gate and no corroborator, and B would not fire. That would drop the count to 6 (still 4+, still cap 3) and promote F and D into the top three.
- No errors, no tool failures, no skill instructions that could not be followed.
