# Eval Execution Transcript

## Eval Prompt

"This customer case study feels too neat. Can you make it read more human at the structural level?"

## Skill

- Path: /Users/tonysina/Documents/claude-skills/skills/human-narrative
- Name: human-narrative (v1.1.2)
- Description: Audits writing for AI-elevated narrative patterns and guides structural rewrites. Operates at scene/story-structure level (temporal order, thematic restraint, resolution mode, emotional expression, intertextual reference). Complements `humanizer` (surface/lexical) and `farnsworth-rhetoric` (sentence craft).

## Input Files

- `case-study-ridgeline.txt` (1.7k, plain text): a ~330-word B2B customer case study, "Ridgeline Logistics: From Spreadsheet Chaos to Coordinated Scheduling", with sections The challenge / The solution / The results / Looking ahead.

## Execution

### Step 0: Read executor instructions

**Action**: Read the executor agent spec.
**Tool**: Read `/Users/tonysina/.claude/skills/skill-builder/agents/executor.md`
**Result**: Success. Process, transcript/metrics/user-notes formats captured.

### Step 1: Load the skill

**Action**: Read SKILL.md in full; listed `references/` and read the relevant portion of `features.md`.
**Tool**: Read (SKILL.md), Bash (`ls` references + `cat` input file), Bash (`rg` over `references/features.md` for the Reader-engagement scale note and the Table 15 response-option list).
**Result**: Success. Skill has 5 steps: register triage, seven-cluster scan (A–G) with gate + corroborator rule, threshold table, intervention order, guardrails. References read: `features.md` only. `changelog.md` not read (not needed). Per the hard constraints I did not invoke the Skill tool, did not read any other skill directory, and did not run `scripts/scan-ai-tells.py`.

### Step 2: Register triage (SKILL.md Step 1)

**Action**: Classified the input against the register table.
**Result**: Row = "Case study, customer story, customer-facing narrative". Clusters in scope: **A, B, E, F, C1**. Never: **C2, D, G**. Not a hard stop, so the audit proceeds. Intervention order for this register (Step 4): A → B → F → E.

### Step 3: Cluster scan (SKILL.md Step 2)

**Action**: Answered each in-scope cluster's gate with the given option set, then checked corroborators. Applied the rule that a cluster fires only if gate is AI-side AND ≥1 corroborator is AI-side.

| Cluster | Gate call | Corroborators | Fired |
|---|---|---|---|
| A | Narrator states what the piece means: **yes** — "The lesson from the rollout is clear: when the people who do the work can see the same picture…" and "has transformed not just its mornings but its entire operating rhythm." AI-side (77% AI vs 52% human). | Thematic unity 5/5 (AI-side, threshold ≥5): every section serves one idea. Moralizing 3/5 (not AI-side, threshold ≥4). No philosophical dialogue. | ✅ |
| B | Dominant emotional mode: **embodied metaphors** — "Maria Chen felt the frustration in her chest". AI-side. Quantitative rule: 1 of ~3 emotional beats runs through the body (the Chen quote and the drivers' reaction are behavioral/reported), well under the >60% trigger; gate called AI-side on dominant-mode only. | Setting-as-mirror 1/5; olfactory imagery: no; sensory density 2/5; inner-life depth 2/5; natural-environment prominence 1/5. **Zero AI-side.** | ❌ |
| C1 | Main event chain resolved: **externally** — a platform was deployed and outcomes were measured; no internal-realization resolution. Human-side. | Causal-chain continuity 5/5 is AI-side, but per "Don't hunt for gates" a human-side gate ends the cluster. | ❌ |
| E | Direct reader address: **never**. AI-side. | Fourth-wall permeability at the floor of the ordinal scale. AI-side. | ✅ |
| F | Reference explicitness: **none**. AI-side. | Names no external text, author, work, standard, or event (Chen and the March 2025 date are internal to the story, not intertextual gestures). AI-side. | ✅ |

### Step 4: Threshold (SKILL.md Step 3)

**Action**: Counted fired clusters and checked the short-professional-text merge rule.
**Result**: A, E, F fired = **3 clusters** → "Some AI-side clustering" → **cap of 2 interventions**. The rule that collapses E and F into one cluster applies only "unless A or B also fires"; A fired, so E and F count separately. Report sized to a ~330-word input: compact table, no corpus percentages in the delivered body beyond what a gate call needs.

### Step 5: Interventions (SKILL.md Step 4, executed one at a time)

**Intervention 1 — A (thematic restraint).** Deleted the two closing sentences of "Looking ahead" ("The lesson from the rollout is clear…" and "For Ridgeline, that shift has transformed…"). Added nothing in their place, per the fix and per the Forbidden-constructions row (no "In summary" substitute — that is `humanizer` `DIDACTIC`). Section now ends on the concrete 2026 maintenance-scheduling fact, which avoids `GENERIC-CLOSER`. Gate moves yes → no.

**Intervention 2 — F blocked, E takes the slot.** F was next in order and is flagged by the skill as the highest value-per-effort cluster, but executing it requires naming a real external work, methodology, or event, and the piece supplies none. Step 5 guardrail 2 (no intervention may invent a fact) blocks it. Per Step 5, a blocked intervention is reported rather than counted and the next in order takes its slot under the same cap. Executed **E**: added one second-person claim to "The challenge" — "If you have ever kept a schedule in a spreadsheet that two other people also edit, you know what the first phone call of the morning is for." Checked against the Forbidden-constructions table: it is a claim about the reader's experience, not a forward-reference announcement, so it is not `SIGNPOSTING`.

Total executed: 2 of a cap of 2.

### Step 6: Guardrail pass (SKILL.md Step 5)

**Action**: Ran all four guardrails on the rewrite.
**Result**:
1. Still coherent — yes; only a deletion and one insertion.
2. Still true — yes; no fact invented. This is why F was blocked and why the C1 "leave a thread unresolved" fix was flagged for the author instead of executed (truth constraint, C1).
3. Point survived — yes; the results paragraph (40 min → 6, 11% fuel, 12 h → <2 h overtime) plus Chen's quote let a reader reconstruct the deleted takeaway. The deleted sentences were restating figures given one paragraph earlier.
4. Author would recognise it — yes; the piece is still a Ridgeline case study in the same voice. The one voice-level judgment call (second person in a case study) is flagged in the delivered answer as a house-style decision.

### Step 7: Write outputs

**Tool**: Write × 3, Bash × 1 (character counts).
**Result**: `result.md`, `transcript.md`, `user_notes.md`, `metrics.json` written to output_dir.

## Output Files

- `result.md`: the delivered answer (cluster table, verdict, two executed interventions with cost/watch notes, the revised case study, the not-taken section, downstream note), wrapped in the BEGIN/END DELIVERED markers with executor commentary after the END marker.
- `transcript.md`: this file.
- `user_notes.md`: uncertainties and suggestions.
- `metrics.json`: tool usage and size metrics.

## Final Result

Register: case study. A, E, F fired (3 clusters, cap 2). Executed A (deleted the stated lesson and the transformation claim, added nothing) and E (one second-person claim in the challenge section). F was blocked by the truth guardrail and reported with two specific things the author can supply to close it. B did not fire (gate AI-side, zero corroborators). C1 did not fire (external resolution) but the "leave a real thread unresolved" option was flagged as the highest-leverage remaining move, contingent on facts only the author has. D, G, C2 out of scope for the register. Closed by pointing at `humanizer` next, then `farnsworth-rhetoric`.

## Issues

- None blocking. One judgment call worth flagging: B's gate is AI-side while every corroborator is human-side, and the skill's firing rule means the piece's only embodied line stays. Documented in the delivered answer rather than silently dropped.
- A second judgment call: F is the cluster the skill rates highest for professional writing, and it is exactly the one an editor cannot execute without source facts. Handled as a flag with two concrete asks, per the C1 truth constraint's precedent.
