# Eval Execution Transcript

## Eval Prompt

"This customer case study feels too neat. Can you make it read more human?"

## Skill

- Path: /Users/tonysina/Documents/claude-skills/skills/human-narrative
- Name: human-narrative (version 1.1.2)
- Description: Audits writing for AI-elevated narrative patterns and guides structural rewrites. Operates at scene/story-structure level (temporal order, thematic restraint, resolution mode, emotional expression, intertextual reference). Complements `humanizer` (surface/lexical) and `farnsworth-rhetoric` (sentence craft).

## Input Files

- `case-study-ridgeline.txt` (1.7 KB, ~330 words): a customer case study for "Ridgeline Logistics", structured as The challenge / The solution / The results / Looking ahead, with one pull quote from operations director Maria Chen.

## Execution

### Step 0: Load the executor spec
**Action**: Read the executor agent definition to confirm required outputs and format.
**Tool**: Read `/Users/tonysina/.claude/skills/skill-builder/agents/executor.md`
**Result**: Success. Required artifacts: `result.md` (per coordinator instruction), `transcript.md`, `metrics.json`, `user_notes.md`.

### Step 1: Load the skill
**Action**: Read `SKILL.md` in full; listed `references/`; targeted read of `references/features.md` for the cluster-E scale note that SKILL.md defers to.
**Tool**: Read (SKILL.md), Bash (`cat` input + `ls` references), Bash (`rg` over features.md)
**Result**: Success. Confirmed the E-cluster features are zero-based ordinal means (Fourth-Wall Permeability 0.67 human / 0.39 AI; Direct Reader Address 0.28 / 0.07) and confirmed the full option sets for Reference Explicitness and Character Introduction. Did not invoke the Skill tool, did not read any other skill directory, did not run `scan-ai-tells.py`, and read nothing under `tests/evals/` outside the assigned inputs directory.

### Step 2: Register triage (skill Step 1)
**Action**: Classified the register from the Step 1 table.
**Result**: "Case study, customer story, customer-facing narrative" row. Clusters in scope: **A, B, E, F, C1**. Never: **C2, D, G**. Not a hard stop, so the audit proceeds.

### Step 3: Cluster scan (skill Step 2)
**Action**: Answered each in-scope cluster's gate with the given option set, then checked corroborators. Applied the rule that a cluster fires only on gate AI-side **AND** ≥1 corroborator AI-side.

**A — Thematic over-determination: FIRED.**
- Gate (narrator states what the piece means): **yes**. Instance: "The lesson from the rollout is clear: when the people who do the work can see the same picture, coordination stops being a daily negotiation and becomes a habit." Second instance: "For Ridgeline, that shift has transformed not just its mornings but its entire operating rhythm."
- Corroborators: thematic unity **5/5** (AI-side, threshold ≥5) — every section serves the single visibility-fixes-coordination idea; moral/philosophical foregrounding 3 (not AI-side); dialogue as philosophical debate: no; reference explicitness: none.
- Gate yes + one AI-side corroborator → fires.

**B — Sensory and embodied performativity: NOT FIRED.**
- Emotional beats counted: (1) "drivers waited in the yard until the calls ended" — behavioral; (2) "Maria Chen felt the frustration in her chest" — embodied; (3) Chen's "I didn't expect the drivers to take to it so quickly" — explicit-ish label in dialogue; (4) "asking why we hadn't done this years ago" — behavioral.
- Quantitative rule: embodied share **1 of 4 = 25%**, below the 60% trigger. Dominant mode is behavioral cues → gate human-side.
- Corroborators all human-side: setting-as-mirror 1 (no weather/environment mirroring); smell imagery no; sensory density 2; inner-life depth 2; natural environment prominence 1.
- Gate human-side and zero AI-side corroborators → does not fire. Applied "Don't hunt for gates" and did not re-read looking for a reason to fire it, despite "felt the frustration in her chest" being the piece's most conspicuous single line.

**C1 — Structural streamlining: NOT FIRED.**
- Gate (main event chain resolved through protagonist's own choice / internal understanding / externally / unresolved): **externally** — the chain resolves on measured operational outcomes (delay 40 → 6 min, fuel −11%, overtime 12h → <2h), not on a realization. Human-side.
- Corroborators would have been AI-side (no subplots; causal continuity 4/5; Chen introduced by external description, "Operations director Maria Chen"), but the gate is human-side, so the cluster does not fire.
- Noted the C1 truth constraint: an open thread cannot be invented for a case study.

**E — Reader engagement: FIRED.**
- Gate (frequency of direct reader address): **never** → AI-side.
- Corroborator: fourth-wall permeability at the floor (no acknowledgement of the telling) → AI-side.

**F — Intertextual richness: FIRED.**
- Gate (reference explicitness): **none** → AI-side.
- Corroborator (names a specific text, author, work, or event): **no**. The named entities — Ridgeline, Maria Chen, March 2025 — are the piece's own subject matter, not intertextual references → AI-side.

**D, G:** out of scope for this register; not scored.

### Step 4: Threshold (skill Step 3)
**Action**: Counted fired clusters and applied the short-professional-text exception.
**Result**: **A, E, F fired = 3.** The "count E and F as one cluster between them" exception applies only when neither A nor B fires; A fired, so E and F count separately. 3 fired → "some AI-side clustering" → **cap of 2 interventions**. Report sized to a ~330-word input: cluster table plus per-intervention notes, no corpus percentage dump.

### Step 5: Intervention order (skill Step 4)
**Action**: Applied the short-form / case-study order A → B → F → E. B did not fire, so it is skipped rather than executed. Slots go to **A** and **F**; **E** is blocked by the cap.

**Intervention 1 (A).** Deleted both thematic statements from "Looking ahead" — "The lesson from the rollout is clear: …becomes a habit." and "For Ridgeline, that shift has transformed not just its mornings but its entire operating rhythm." Added nothing in their place, per the fix instruction and the `DIDACTIC` row of the forbidden-constructions table (no "In summary" replacement). Gate: yes → no.
- Structural change: the piece now ends on a concrete forward-looking fact (2026 maintenance scheduling) rather than a verdict, satisfying the `GENERIC-CLOSER` constraint.
- Cost recorded in the deliverable: "Looking ahead" shrinks to one sentence; if the closing line does sales work for a gated asset, A should be flagged rather than executed.

**Intervention 2 (F).** Added one sentence at the end of "The challenge": "Eliyahu Goldratt argued in *The Goal* (1984) that an hour lost at a bottleneck is an hour lost for the whole system. Ridgeline's bottleneck was a phone call." Reference explicitness: none → explicit named. Named the work, the author and the year, avoiding `VAGUE-ATTRIB` ("industry reports", "experts argue").
- Placed before the solution so it reads as premise, which also absorbs part of the load carried by the deleted moral (the A fix's "move it earlier" option, applied indirectly).
- Cost recorded: introduces a business-book register the customer's voice may not have; fallback given (drop the Goldratt sentence, keep "Ridgeline's bottleneck was a phone call").
- Downstream flag recorded: the piece now makes a checkable claim about a real book → run `source-check`.

**E not executed** — fired but below the cap. Reported with the concrete fix it would have received (one second-person line in "The challenge"), phrased as a claim about the reader's own experience rather than a forward-reference announcement, to avoid `humanizer` `SIGNPOSTING`.

### Step 6: Guardrail pass (skill Step 5)
1. **Still makes sense?** Yes. No causal link was broken; the only structural removals were two summary sentences.
2. **Still true?** Yes. No fact about Ridgeline was invented, no open thread manufactured, no external cause asserted. The only new factual content is the attributed Goldratt claim, flagged for `source-check`.
3. **Did the point survive?** Yes. The results paragraph and Chen's quote let a reader reconstruct the thesis unaided; the Goldratt line carries the bottleneck framing without stating a moral.
4. **Would the author recognize it?** Mostly. Flagged the F insertion as the one place where voice could drift, with an explicit revert option.
No guardrail forced a blocked intervention, so no slot was reassigned.

### Step 7: Write artifacts
**Action**: Wrote `result.md` (delivered answer between `---` fences, commentary after), then `transcript.md`, `user_notes.md`, `metrics.json`.
**Tool**: Write ×4, Bash (character counts)
**Result**: Success.

## Output Files

- `result.md` — the delivered answer: cluster table, verdict, the two executed interventions with cost and downstream notes, the full rewritten case study, and the not-taken list. Commentary follows the closing fence.
- `transcript.md` — this file.
- `user_notes.md` — uncertainties, review needs, suggestions.
- `metrics.json` — tool usage and size metrics.

## Final Result

Register: case study. Three clusters fired (A, E, F); cap of 2. Executed **A** (deleted both thematic statements from the closing section, added nothing) and **F** (named Goldratt's *The Goal*, 1984, at the end of "The challenge"). Reported **E** as fired-but-capped with its concrete fix, and reported **B** and **C1** as not fired with the reasoning, explicitly declining to treat "felt the frustration in her chest" as a finding since the gate and every corroborator sit human-side. **D** and **G** are out of scope for the register. Closed with the workflow position (`humanizer` next, then `farnsworth-rhetoric`) and a `source-check` flag on the new external claim.

## Issues

- The prompt is a rewrite request ("make it read more human"), not a diagnosis request, so the "Full audit + rewrite" output mode was used. The skill does not say whether the rewritten artifact should be reproduced in full or only as a diff; the full rewritten case study was included since the user asked for a changed document.
- Cluster B is the judgement call in this run. "Felt the frustration in her chest" is the line a casual reader would flag first, and the skill's own worked example converts exactly that construction. But the beat count (1 of 4 embodied, 25%, versus the 60% rule) and zero AI-side corroborators put it human-side, and Step 2 plus "Don't hunt for gates" forbid firing on a gate alone. Reported it as an optional preference change rather than a finding.
- The E/F "count as one cluster" exception is written into the under-600-word row of Step 3, while this piece is ~330 words but sits in the case-study register row. The ambiguity is moot here because A fired, which disables the exception either way — but a shorter case study with neither A nor B firing would leave the rule's applicability unclear.
- No errors, tool failures, or blocked operations.
