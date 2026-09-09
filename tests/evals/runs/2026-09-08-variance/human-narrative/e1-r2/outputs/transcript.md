# Eval Execution Transcript

## Eval Prompt

"This customer case study feels too neat. Can you make it read more human at the structural level?"

## Skill

- Path: /Users/tonysina/Documents/claude-skills/skills/human-narrative
- Name: human-narrative (version 1.1.2)
- Description: Audits writing for AI-elevated narrative patterns and guides structural rewrites — scene/story structure level (temporal order, thematic restraint, resolution mode, emotional expression, intertextual reference). Complements `humanizer` (surface/lexical) and `farnsworth-rhetoric` (sentence craft).

## Input Files

- `case-study-ridgeline.txt` (1.7 KB, 331 words): a customer case study for "Ridgeline Logistics," structured as The challenge / The solution / The results / Looking ahead, with a customer quote from operations director Maria Chen.

## Execution

### Step 1: Load the executor spec and inventory the working set
**Action**: Read the executor agent spec; listed the inputs directory and the skill directory.
**Tool**: Read (`/Users/tonysina/.claude/skills/skill-builder/agents/executor.md`); Bash (`ls -la` on inputs dir and skill dir).
**Result**: Success. Skill dir contains `SKILL.md` (22 KB) and `references/` with `changelog.md` and `features.md`. Inputs dir contains one file.

### Step 2: Read the input and the skill's reference files
**Action**: Read the case study text; listed `references/`.
**Tool**: Bash (`cat` on the input; `ls -la` on references).
**Result**: Success. Input is 331 words, four headed sections plus title.

### Step 3: Load the skill
**Action**: Read `SKILL.md` in full, then `references/features.md` in full (needed for the cluster E scale note that `SKILL.md` explicitly defers to, and for the human/AI means used in reporting).
**Tool**: Read (SKILL.md, 466 lines); Read (references/features.md, 207 lines).
**Result**: Success. Did not read `references/changelog.md` — it documents skill version history, not audit method.
**Constraint honored**: Skill tool was NOT invoked; no other skill directory was read; `scripts/scan-ai-tells.py` was NOT run.

### Step 4: Step 1 of the skill — register triage
**Action**: Classified the register against the skill's register table.
**Result**: "Case study, customer story, customer-facing narrative" row. Clusters in scope: **A, B, E, F, C1**. Never: **C2, D, G**. Not a hard stop, so the audit proceeds. Length (331 words) noted but per the skill "length is not the mode; register is," so the case-study row governs rather than the under-600-word row.

### Step 5: Step 2 of the skill — cluster scan (gate + corroborators, in-scope clusters only)
**Action**: Scored each in-scope cluster against its gate and corroborators using the closed option sets from `references/features.md`.

**Cluster A — Thematic over-determination.**
- Gate: *Does the narrator state what the piece means?* → **yes**. Instance: "The lesson from the rollout is clear: when the people who do the work can see the same picture, coordination stops being a daily negotiation and becomes a habit." Second instance: "that shift has transformed not just its mornings but its entire operating rhythm."
- Corroborators: thematic unity **5 of 5** (title, all four headings and the close serve a single before/after arc) → AI-side. Moral/philosophical weighting **3 of 5** → not AI-side. Dialogue-as-philosophical-debate → **no** (Chen's quote is concrete). Reference explicitness → none (handled under F).
- **FIRED** (gate AI-side + at least one corroborator AI-side).

**Cluster B — Sensory and embodied performativity.**
- Gate: *How are emotions most commonly conveyed?* Counted emotional beats: (1) "Maria Chen felt the frustration in her chest" — embodied; (2) "Honestly, I didn't expect the drivers to take to it so quickly" — explicit/reported; (3) "they were asking why we hadn't done this years ago" — behavioral cue. Embodied share = **1/3 = 33%**, below the skill's 60% quantitative rule. Dominant mode reads as behavioral, not embodied → **gate human-side**.
- Corroborators (recorded, not decisive): setting-as-psychological-mirror 2 of 5; olfactory imagery **no**; sensory density 2 of 5; depth of interior access 2 of 5; environmental emphasis low. All human-side.
- **DID NOT FIRE.** Per "Don't hunt for gates," moved on rather than re-reading for a reason to fire it. The single embodied beat was flagged in the delivered report as a watch item, not counted as a finding.

**Cluster C1 — Structural streamlining.**
- Gate: *Is the main event chain resolved through the protagonist's own choice or internal understanding?* → **resolved externally** (a platform was rolled out and adopted; the resolution is an external action, not an internal realization) → **gate human-side**.
- Corroborators (recorded, not decisive): causal chain continuity 5 of 5; subplot integration → no subplots; character introduction → external description ("Operations director Maria Chen"). All AI-side.
- **DID NOT FIRE.** Gate human-side means no fire regardless of corroborators; documented explicitly in the delivered report because the corroborators are the visible source of the "too neat" feel.

**Cluster E — Reader engagement.**
- Gate: *How often does the text address the reader directly?* → **never** → AI-side.
- Corroborator: fourth-wall permeability at the lowest code → AI-side.
- **FIRED.**

**Cluster F — Intertextual richness.**
- Gate: *Are intertextual gestures explicit or diffuse?* → **none** → AI-side.
- Corroborator: *Does the piece name a specific text, author, work, or event?* → **no**. The scheduling platform is unnamed across all four sections; the spreadsheet tool is unnamed. (Ridgeline and Maria Chen are the subject of the piece, not intertextual references.) AI-side.
- **FIRED.**

**Out of scope, not scored**: C2, D (temporal complexity), G (narrative diversity / moral ambiguity) — excluded by the case-study register row.

### Step 6: Step 3 of the skill — threshold
**Action**: Counted fired clusters and checked the E/F collapse rule.
**Result**: **3 clusters fired (A, E, F) → "some AI-side clustering" → cap of 2 interventions.**
The short-professional-text rule ("count E and F as one cluster between them") was checked and does **not** apply, because its stated exception is "unless A or B also fires," and A fired. E and F therefore count separately.

### Step 7: Step 4 of the skill — intervention order and execution
**Action**: Applied the short-form/case-study order A → B → F → E, taking from the top to the cap.

**Slot 1 — A (thematic restraint).** Deleted both thematic statements in the closing paragraph, adding nothing in their place. The piece now ends on the concrete maintenance-scheduling fact. Avoided the forbidden substitutions ("In summary" → `DIDACTIC`; "the road ahead is promising" → `GENERIC-CLOSER`).

**Slot 2 — B skipped (did not fire). F attempted, BLOCKED.** The F fix requires naming a real specific work/product/event. The case study never names the scheduling platform or the spreadsheet tool, and neither name is available in the input. Writing one would violate Step 5 guardrail 2 ("Is it still true?") and put a fabricated fact into a customer-facing asset. Per Step 5, "a blocked intervention is reported, not counted: the next intervention in order takes its slot." F was reported to the author with the exact insertion point and clause shape, and its slot passed to E.

**Slot 2 (actual) — E (reader address).** Added one second-person claim about the reader's own experience in the challenge section: "If you have run a dispatch floor, you can price forty idle minutes without doing the arithmetic." Deliberately not a forward-reference announcement, which would be `humanizer` `SIGNPOSTING`.

Two interventions executed; cap respected.

### Step 8: Step 5 of the skill — guardrail check
**Action**: Ran all four guardrails against the rewrite.
1. *Still coherent?* Yes — the deletion removes a summary paragraph; no causal link was broken.
2. *Still true?* Yes — nothing invented. This is what blocked F, and what kept me from adding a rollout setback (which would also have been cluster G, out of register scope).
3. *Did the point survive?* Yes — the results section (one live board, 40 min → 6 min, 12 h → under 2 h overtime) plus Chen's quote lets the reader reconstruct "shared visibility ended the daily negotiation" without being told it.
4. *Would the author recognize it?* Yes — 331 → 305 words, one added sentence, one deleted paragraph, no reordering, no sentence-level rewriting.

### Step 9: Compose and save the delivered answer
**Action**: Wrote the audit report, the two interventions with cost/watch notes, the full rewrite, and the "what I didn't take" section (F blocked on facts; G out of register scope; the title as a remaining A-cluster instance; the retained embodied beat).
**Tool**: Write → `outputs/result.md`.
**Result**: Success. Closed with the workflow-position handoff to `humanizer`, including the instruction not to re-add anything `humanizer` deletes.

### Step 10: Write eval artifacts
**Action**: Wrote transcript, user notes, metrics; computed character counts.
**Tool**: Write ×3, Bash (`wc -c` / `find`), Edit (metrics sizes).

## Output Files

- `result.md` — the delivered answer (audit table, verdict, 2 executed interventions, full rewrite, not-taken section), wrapped in the BEGIN/END DELIVERED markers, plus coordinator commentary after the END marker.
- `transcript.md` — this file.
- `user_notes.md` — uncertainties and suggestions.
- `metrics.json` — tool usage and sizes.

## Final Result

Audit verdict: 3 of 5 in-scope clusters fired (A thematic over-determination, E reader engagement, F intertextual richness) → cap of 2 interventions. Executed A (deleted the two-sentence stated theme, ending on the concrete 2026 maintenance-scheduling fact) and E (one second-person line in the challenge section). F was blocked by the truth constraint — the platform is unnamed and inventing a name is not permitted — so it was handed back to the author with the exact one-clause fix. B and C1 were scored as not-firing on their gates despite AI-side corroborators. G (the uniformly positive framing, which is the most visible source of the "too neat" feel) was flagged as out of scope for the case-study register and handed back as an author decision. Rewrite: 331 → 305 words, no sentence-level editing, handed off to `humanizer`.

## Issues

- None blocking. One methodological judgment worth surfacing: "felt the frustration in her chest" is a conspicuous AI tell and the likely reason the user flagged the piece, but cluster B's gate and its 60% quantitative rule both land human-side on a single embodied beat out of three. I scored it honestly as not-firing and flagged the line in the report rather than inflating the cluster count to justify acting on it.
