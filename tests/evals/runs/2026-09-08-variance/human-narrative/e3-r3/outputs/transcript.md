# Eval Execution Transcript

## Eval Prompt

"Why does this essay still feel AI-written even after I edited it for style?"

## Skill

- Path: /Users/tonysina/Documents/claude-skills/skills/human-narrative
- Name: human-narrative (metadata.version 1.1.2)
- Description: Audit writing for AI-elevated narrative patterns and guide structural rewrites. Operates at scene/story structure level (temporal order, thematic restraint, resolution mode, emotional expression, intertextual reference). Complements `humanizer` (surface/lexical) and `farnsworth-rhetoric` (sentence craft).

## Input Files

- `essay-saying-no.txt` (2.0 KB, ~380 words): first-person personal essay about the first time the narrator said no to a manager (Dana), covering an overcommitment, a slipped pipeline, a boundary-setting question, and a closing reflection paragraph.

## Execution

### Step 0: Load instructions and skill

**Action**: Read the executor spec, then loaded the skill without invoking the Skill tool.
**Tool**: `Read` (executor.md); `Bash` (`cat SKILL.md`, `ls -R references/`); `Bash` (`cat` input essay); `Bash` (`grep` on `references/features.md` for the cluster-E scale note).
**Result**: SKILL.md loaded in full (Steps 1–5, forbidden constructions, worked example, output formats). `references/` contains `changelog.md` and `features.md`. Confirmed the cluster-E reporting rule: report Fourth-Wall Permeability (0.67 human / 0.39 AI) and Direct Reader Address (0.28 / 0.07) as ordinal means over zero-based codes, not as bare decimals or percentages.
**Constraints honored**: did not invoke the Skill tool, did not read any other skill directory, did not run `scripts/scan-ai-tells.py`, read nothing under `tests/evals/` outside the assigned `inputs/` directory.

### Step 1: Register triage

**Action**: Classified the register per the Step 1 table.
**Result**: **Personal essay.** Row 1 of the table — "Fiction, personal essay, narrative journalism" — all clusters A–G in scope, including C2 and D, which are out of scope for every professional register. Not a hard stop. Length (~380 words) does not change the mode; the skill states explicitly that "length is not the mode; register is," and that "a 400-word personal essay still gets D if the author wants it."

### Step 2: Cluster scan

**Action**: Scored each of the seven clusters gate-first, then corroborators, applying the rule that a cluster fires only if the gate is AI-side AND at least one corroborator is AI-side.

**A — Thematic over-determination.** Gate: does the narrator state what the piece means? **Yes** (AI-side; 77% AI vs 52% human). Instance: "What I learned is that saying no is rarely a confrontation. Most of the time it is just information that the other person doesn't have yet." Corroborators: moralizing/philosophical foregrounding 4/5 (AI-side, ≥4); thematic unity 5/5 — every beat serves the one idea (AI-side, ≥5); dialogue as philosophical debate: **no**, the only dialogue is concrete and operational ("The pipeline, obviously") — human-side; reference explicitness: none (scored under F). **FIRED.**

**B — Sensory and embodied performativity.** Counted emotional beats: (1) "My stomach dropped" — embodied; (2) "My chest tightened" — embodied; (3) "stared at the calendar until the squares blurred" — behavioral; (4) "I felt the familiar heat rise up my neck" — embodied; (5) "I told myself I had done the right thing, and I did not believe it" — internal statement; (6) "which made me laugh" — behavioral; (7) "The fear I carried for eleven months" — explicit label. Embodied share = 3/7 ≈ 43%, below the 60% quantitative rule, so the gate is not forced AI-side by count. Corroborators, all human-side: setting-as-mirror 2/5 (no weather or room mirroring mood); olfactory imagery **absent**; sensory density 2/5; inner-life depth 3/5; natural environment 1/5. **DID NOT FIRE** — zero AI-side corroborators, so the cluster cannot fire regardless of the dominant-mode call.

**C — Structural streamlining.** Gate: main event chain resolved **internally** — "Once I understood that, everything at work got easier" (AI-side; protagonist-choice agency 69% AI vs 46% human, internal-understanding resolution 47% vs 27%). Corroborators: no subplots (AI-side, 79% vs 57%) — the contractor is a beat, not a thread; causal continuity ~4.5/5, each event drives the next with no slack (AI-side, ≥4); investment before jeopardy 3/5 (AI-side, ≥3). Human-side: opening spatial grounding and spatial granularity are both low ("It started on a Monday," "walked over to my desk"). **FIRED.**

**D — Temporal complexity.** Gate: chronological discontinuity 2/5 — Monday, two weeks, Thursday of week three, the following week, the review, then a present-tense frame; strictly forward (AI-side, ≤2; human 2.40 vs AI 2.12 on 1–5). Corroborators: anachrony 1/5 (AI-side); nonlinear framing for delayed disclosure 1/5 — nothing is withheld (AI-side); depth of recontextualization 3/5 — "She had never wanted me to do both" mildly recasts the preceding two weeks (AI-side, ≤3). **FIRED.**

**E — Reader engagement.** Gate: **never** addresses the reader (AI-side). Corroborator: fourth-wall permeability at floor (AI-side). **FIRED.**

**F — Intertextual richness.** Gate: reference explicitness **none** (AI-side). Corroborator: no named text, author, work, or event — Dana is a character in the story, not an external referent (AI-side; explicit named reference 47% human vs 24% AI). **FIRED.**

**G — Narrative diversity.** Gate: moral framing **clearly positive** — the contractor did it better, the review was positive, "everything at work got easier, and I have never gone back," with no cost admitted (AI-side; ambivalent 59% human vs 38% AI). Corroborators: no subplots (AI-side); dialogue-to-narration ~1.5/5 (AI-side, ≤2); one effective location (AI-side, fewer). **FIRED.**

### Step 3: Threshold

**Action**: Counted fired clusters.
**Result**: **6 fired** (A, C, D, E, F, G); B did not fire. 4+ → "systematic AI-side clustering," cap of **3 interventions**. The E/F merge rule in Step 3 applies only to the under-600-word professional-writing row, not to a personal essay, and A fires here anyway, so it does not change the count. Report proportioning: the "one-paragraph verdict, no table" rule applies under 100 words; at ~380 words the cluster table is appropriate.

### Step 4: Intervention order and output-format selection

**Action**: Applied the long-form order A → B → F → D → E → C → G, dropping B (did not fire).
**Result**: Top three available = **A, F, D**. E, C, and G fire but fall below the cap.

Output format decision: the prompt is a diagnostic question ("why does this feel AI-written"), not a rewrite request, so the skill's **Diagnosis only** format applies — cluster table, Step 3 verdict, located instance plus named intervention per fired cluster in Step 4 order, offer to execute. No rewrite was performed.

Answered the literal question first using the skill's Source section: the StoryScope §4.2 robustness result (narrative model detects LAMP-rewritten AI stories at 93.9% macro-F1 vs 95.5% unedited, a 1.6-point drop) is the direct explanation for why a style pass left the feeling intact.

### Step 5: Guardrails applied

**Action**: Checked each proposed intervention against the Step 5 guardrails.
**Result**:
- **C1 flagged, not executed.** The truth constraint forbids inventing an open thread in non-fiction. Whether anything actually stayed unresolved, and whether "everything got easier" is accurate, are facts only the author has. Reported the finding with the specific questions the author needs to answer, per the worked example's handling of the same cluster.
- **F carries a downstream obligation.** Named the requirement that any real reference must be verified (`source-check`) and that "research shows"-style substitutes are `humanizer` `VAGUE-ATTRIB`.
- **E fix pre-empted against `SIGNPOSTING`.** Explicitly ruled out "you might be wondering."
- **"Some AI patterns are the assignment."** Flagged that a stated thesis may be intentional in some venues, and said what the pass looks like if A is kept.
- **B protected.** Noted that re-editing the emotional register risks pushing a currently human-side cluster AI-side.

### Step 6: Write outputs

**Tool**: `Write` × 4 (`result.md`, `transcript.md`, `metrics.json`, `user_notes.md`), `Bash` for character counts.

## Output Files

- `result.md`: the delivered answer, fenced between two `---` lines, with execution commentary after the second fence.
- `transcript.md`: this file.
- `metrics.json`: tool usage and size metrics.
- `user_notes.md`: uncertainties, judgment calls, and skill suggestions.

## Final Result

Diagnosis delivered. Register: personal essay, all clusters in scope. Six of seven clusters fired (A, C, D, E, F, G); B did not fire and is the cluster the author's style pass evidently already fixed. Verdict: systematic AI-side clustering, cap 3. Interventions named in Step 4 order — A (delete the stated theme in the closing paragraph, add nothing), F (name one real work with author and year), D (open on the Thursday question and work backward). E, C, and G reported below the cap; C additionally flagged as blocked by the truth constraint. Offer to execute extended, with the downstream `humanizer` → `farnsworth-rhetoric` order stated.

## Issues

None. No errors, no failed tool calls, no ambiguity in the skill that blocked execution. The one genuinely close call is documented in `user_notes.md` (cluster B's gate).
