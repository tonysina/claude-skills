# Eval Execution Transcript

## Eval Prompt

"This customer case study feels too neat. Can you make it read more human?"

## Skill

- Path: /Users/tonysina/Documents/claude-skills/skills/human-narrative
- Name: human-narrative (metadata.version 1.1.2)
- Description: Audits writing for AI-elevated narrative patterns at the scene/structure level (temporal order, thematic restraint, resolution mode, emotional expression, intertextual reference) and guides structural rewrites. Complements `humanizer` (surface/lexical) and `farnsworth-rhetoric` (sentence craft).

## Input Files

- `case-study-ridgeline.txt` (1.7 KB, plain text): a ~300-word customer case study for "Ridgeline Logistics" with four labeled sections — The challenge / The solution / The results / Looking ahead — including a customer quote from operations director Maria Chen.

## Execution

### Step 1: Load the skill

**Action**: Read SKILL.md in full and listed `references/`.
**Tool**: Read (`skills/human-narrative/SKILL.md`), Bash (`ls references/`).
**Result**: Success. SKILL.md is a 5-step process: register triage → cluster scan (A–G, gate + corroborator) → threshold → intervention order → guardrails, plus a forbidden-constructions table and a worked example. `references/` contains `features.md` (13 KB) and `changelog.md` (16 KB).

### Step 2: Read the input and the E-cluster scale note

**Action**: Printed the case study; grepped `references/features.md` for the reader-address / fourth-wall scale note that SKILL.md cross-references from cluster E.
**Tool**: Bash (`cat`, `grep -n -A6`).
**Result**: Success. features.md documents Direct Reader Address as an ordinal mean over zero-based codes (human 0.28 / AI 0.07) with never / occasional asides / frequent-structural as the response set, and Fourth-Wall Permeability on a 1–4 scale (human 0.67 / AI 0.39 as ordinal means). Noted the file's instruction to report these as ordinal means with the code scale stated, not as bare percentages.

Per the task's hard constraints, no other skill directory was read, `scripts/scan-ai-tells.py` was not run, and nothing under `tests/evals/` other than this case's `inputs/` was opened.

### Step 3: Register triage (SKILL.md Step 1)

**Action**: Matched the piece to a row in the register table.
**Result**: Row 3 — "Case study, customer story, customer-facing narrative." Clusters in scope: **A, B, E, F, C1**. Never: **C2, D, G**. Not a hard stop, so the audit proceeds.

### Step 4: Cluster scan (SKILL.md Step 2)

**Action**: Answered each in-scope cluster's gate with its given option set, then checked corroborators. Applied the rule that a cluster fires only on gate AI-side AND ≥1 corroborator AI-side.

- **A — thematic over-determination.** Gate "does the narrator state what the piece means?" → **yes** (AI-side). The statement is explicit: "The lesson from the rollout is clear: when the people who do the work can see the same picture, coordination stops being a daily negotiation and becomes a habit," reinforced by "that shift has transformed not just its mornings but its entire operating rhythm." Corroborators: thematic unity 5/5 (all four sections serve the one idea); moralizing 3/5 (below the ≥4 bar); dialogue-as-debate no. Unity alone corroborates. **FIRED.**
- **B — sensory and embodied performativity.** Counted emotional beats: (1) "felt the frustration in her chest" — embodied; (2) "Honestly, I didn't expect the drivers to take to it so quickly" — explicit/attitudinal; (3) "they were asking why we hadn't done this years ago" — behavioral. Embodied share 1/3 = 33%, under the >60% quantitative rule. Dominant mode = behavioral cues, human-side. Corroborators all human-side: setting-as-mirror 1/5, no olfactory imagery, sensory density 2/5, inner-life depth 2/5, natural environment 1/5 ("Pacific Northwest" is a place name, not environmental prominence). **NOT FIRED.** Applied "Don't hunt for gates" and did not re-read looking for a reason to fire it.
- **C1 — structural streamlining.** Gate "resolved through protagonist's own choice or internal understanding?" → **internally**: the chain resolves entirely on Ridgeline's own decision to roll out the platform. Corroborators: causal continuity 5/5 (challenge causes solution causes results causes future plan, with nothing extraneous); protagonist introduced by external description ("Operations director Maria Chen"), AI-side at 52% vs 30%. **FIRED.**
- **E — reader engagement.** Gate → **never** addresses the reader (AI-side). Corroborator: fourth-wall permeability at the floor of the 1–4 scale. **FIRED.**
- **F — intertextual richness.** Gate → **none** (AI-side). Corroborator: names no specific text, author, work, or event; the proper nouns present (Ridgeline, Chen, Pacific Northwest) are the subject matter, not an intertextual gesture. **FIRED.**

### Step 5: Threshold (SKILL.md Step 3)

**Action**: Counted fired clusters and checked the E/F short-text carve-out.
**Result**: A, C1, E, F = **4 fired** → "systematic AI-side clustering" → cap **3 interventions**. The rule that E and F count as one cluster between them applies only "unless A or B also fires"; A fired, so E and F count separately. The piece is ~300 words but well over the "under 100 words" one-paragraph reporting threshold, so a full table is appropriate.

### Step 6: Intervention order and selection (SKILL.md Step 4)

**Action**: Applied the short-form/case-study order **A → B → F → E**.
**Result**: B did not fire and is skipped. Interventions taken: **A, F, E** (3 = cap). C1 fired but does not appear in the case-study order and its fix is truth-constrained, so it is reported rather than executed (see Step 8).

### Step 7: Execute interventions one at a time

**Action**: Rewrote the case study, applying each intervention in order and recording what changed / what it costs / what to watch.

1. **A (deletion).** Deleted both thematic statements from "Looking ahead," adding nothing in their place — per the forbidden-constructions table, no "In summary" replacement (`DIDACTIC`) and no "the road ahead is promising" closer (`GENERIC-CLOSER`). The section now ends on the concrete unresolved fact: the 2026 maintenance-scheduling plan. Gate: yes → no.
2. **F (name the reference).** Added a two-sentence paragraph at the end of "The challenge" naming Eliyahu Goldratt and *The Goal* (1984) on local scheduling producing global waiting, and tying it to the three-spreadsheet situation. Avoided `VAGUE-ATTRIB` ("industry reports," "experts argue"). Reference explicitness: none → explicit named. Flagged for `source-check` per the cluster-F constraint.
3. **E (reader address).** Added one second-person experiential claim ("If you have ever had to wait for someone else's phone call before your own day could start, you know what forty minutes of it costs by Friday"). Deliberately not a forward-reference announcement, which would be `humanizer` `SIGNPOSTING`.

Sentences elsewhere were left alone — the skill states it does not touch sentence craft.

### Step 8: Guardrail pass (SKILL.md Step 5)

**Action**: Checked all four guardrails against the rewrite.
**Result**:
1. *Still makes sense?* Yes — no causal link was broken (C2 is out of scope anyway).
2. *Still true?* The three executed interventions invent no facts about Ridgeline. The one new factual dependency is the Goldratt paraphrase, flagged for `source-check`. **C1's intervention failed this guardrail**: leaving a thread unresolved in a customer story would require inventing an open question, which the C1 truth constraint forbids. Reported to the author with a concrete suggestion (name a genuinely open item if one exists) rather than executed.
3. *Point survive?* Yes — the forty-minutes-to-six figure plus the Goldratt framing let a reader reconstruct the thesis without it being stated. Noted in the deliverable that if stakeholders require a stated takeaway, one sentence should be restored, not both.
4. *Author recognize it?* Yes — section structure, voice, all figures and the customer quote are unchanged.

Per Step 5, the blocked C1 intervention is reported, not counted; its slot was not reassigned because C1 was last in the applicable order and the cap of 3 was already met by A, F, E.

### Step 9: Write outputs

**Action**: Wrote `result.md` (delivered answer between `---` fences), then `transcript.md`, `metrics.json`, `user_notes.md`.
**Tool**: Write, Bash (character counts).
**Result**: Success.

## Output Files

- `result.md` — the delivered answer: cluster table, verdict, full rewritten case study, per-intervention change/cost/watch notes, "Not taken" section, downstream warnings. Delivered text sits between two `---` fences; execution commentary follows the second fence.
- `transcript.md` — this file.
- `metrics.json` — tool usage and size counts.
- `user_notes.md` — uncertainties and suggestions.

## Final Result

Register: case study (A, B, E, F, C1 in scope). Four clusters fired — A (stated theme), C1 (internal resolution, total causal continuity, protagonist introduced by external description), E (never addresses the reader), F (no named reference) — for a cap of 3 interventions. B scored honestly as not firing: the dominant emotional mode is behavioral, embodied beats are 1 of 3 (33%, under the 60% rule), and every corroborator is human-side.

Three interventions executed in the case-study order A → F → E: deleted both thematic statements from the closing section and added nothing; named Goldratt's *The Goal* (1984) at the end of the challenge; added one second-person experiential claim. C1 fired but was flagged rather than executed under its truth constraint — a case study cannot be given an invented open thread — with a note that a genuinely unresolved item, which only the author has, would address the "too neat" complaint more directly than any of the three edits. Closed with downstream warnings: run `source-check` on the Goldratt paraphrase, then `humanizer`, then `farnsworth-rhetoric`, and don't re-add anything `humanizer` deletes.

## Issues

- None blocking. One judgment call worth recording: cluster C's gate wording ("resolved through the protagonist's own choice **or** internal understanding" with options externally / internally / unresolved) lumps agency with internal realization, so a case study in which the company solves its own problem by deliberate action reads as "internally" even though nothing psychological happens. Scored AI-side on that reading; the alternative reading (deployment = external cause) would have left C1 unfired and dropped the count to 3, which would not have changed the intervention cap (still 3) or the selection (still A, F, E).
- Second judgment call: cluster F's fix required introducing an outside reference into a customer case study, which is a register-sensitive addition. Executed it because F is in scope for the case-study row and the skill calls it the highest value-per-effort cluster for professional writing, but flagged both the `source-check` dependency and an alternative (naming a real external event instead) in the deliverable.
