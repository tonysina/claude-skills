# Eval Execution Transcript

## Eval Prompt

"Audit the narrative structure of this and fix anything that reads as AI."

## Skill

- Path: /Users/tonysina/Documents/claude-skills/skills/human-narrative
- Name: human-narrative (version 1.1.2)
- Description: Audits writing for AI-elevated narrative patterns at the scene and story
  structure level — temporal order, thematic restraint, resolution mode, emotional
  expression, intertextual reference. Complements `humanizer` (surface/lexical) and
  `farnsworth-rhetoric` (sentence craft).

## Input Files

- `status-difficult.txt` → actual filename `status-update.txt`: 284 bytes, plain text.
  A 51-word engineering sprint status update.

Full text:

> Sprint 14 status: the search reindex finished Friday. Two of the five reporting endpoints
> are migrated; the remaining three are blocked on the schema change that needs DBA review.
> I have asked for review by Wednesday. If it slips past Wednesday we lose the sprint. No
> other blockers.

## Execution

### Step 1: Load the skill

**Action**: Read SKILL.md in full, then listed `references/`.
**Tool**: Read (SKILL.md, 465 lines); Bash `ls -la references/`
**Result**: Success. References are `features.md` (13k) and `changelog.md` (16k).

### Step 2: Read the input and the relevant reference section

**Action**: Read the input file; targeted search of `references/features.md` for the
cluster E scale note that SKILL.md's E gate points at.
**Tool**: Bash `cat` on input; `rg -n "scale note|fourth wall|reader|direct address"` on
features.md
**Result**: Success. Confirmed the two E features and their scales — Frequency of Direct
Reader Address (never / occasional asides / frequent-structural, human-side: frequent) and
Fourth-Wall Permeability (1–4, human-side: high). Did not read `changelog.md` — it is
version history, not audit input.

### Step 3: Register triage (SKILL.md Step 1)

**Action**: Placed the piece in the register table.
**Result**: "Executive summary, **status update**, email, slide copy (<600 words)" row.
51 words, well inside the bound.

- Clusters in scope: **A, B, E, F**
- Explicitly out of scope for this register: **C, D, G**

Not a hard stop — the hard-stop row is technical docs, runbooks, process instructions, data
reporting, legal and RFP answers. A sprint status update is narrative-adjacent professional
writing, not a runbook, so the audit proceeds. Noted that the skill says length is not the
mode, register is; the register call does the work here, not the word count.

### Step 4: Cluster scan (SKILL.md Step 2)

Four in-scope clusters scanned. Rule applied: a cluster fires only if the gate is AI-side
**and** at least one corroborator is AI-side.

**A — Thematic over-determination**
- Gate: *Does the narrator state what the piece means?* → **no**. Human-side.
- The nearest candidate is "If it slips past Wednesday we lose the sprint." Read as a stated
  consequence — a fact about the schedule — not a narratorial statement of meaning. There is
  no verdict, no lesson, no "what this shows is."
- Corroborators not reached (gate human-side). Per "Common issues," did not re-read hunting
  for a reason to fire it.
- **Not fired.**

**B — Sensory and embodied performativity**
- Gate: *How are emotions most commonly conveyed?* → no emotional beats present. Nothing
  runs through the body; nothing is labeled either.
- Quantitative rule (>60% of emotional beats through the body): denominator is zero, so the
  rule cannot fire.
- Corroborators: no setting-as-mirror, no olfactory imagery, sensory density 1, inner-life
  depth 1, natural environment absent — all human-side or absent.
- **Not fired.**

**E — Reader engagement**
- Gate: *How often does the text address the reader directly?* → **never**. AI-side.
- Corroborator: fourth-wall permeability at the floor. AI-side.
- **Fired** — but by construction, per Step 3's short-professional note.

**F — Intertextual richness**
- Gate: *Are intertextual gestures explicit or diffuse?* → **none**. AI-side.
- Corroborator: *Does the piece name a specific text, author, work, or event?* → no. AI-side.
  ("Sprint 14," "Friday," "Wednesday" are internal project referents, not intertextual
  gestures.)
- **Fired** — also by construction.

Clusters C, D and G were not scored: out of scope for the <600-word register row.

### Step 5: Threshold (SKILL.md Step 3)

**Action**: Applied the short-professional counting rule.
**Result**: SKILL.md Step 3 states that in the under-600-word row, E and F come out AI-side
on almost every piece and are to be **counted as one cluster between them unless A or B also
fires**. Neither A nor B fired.

- Effective clusters fired: **1**
- Verdict row: 0–1 → "Reads within human structural range"
- Interventions permitted: **None. Report and stop.**

### Step 6: Steps 4 and 5 — not reached

**Action**: None taken.
**Result**: Step 4 (intervention order) and Step 5 (guardrail) are downstream of a verdict
that permits interventions. With a cap of zero there is nothing to order and nothing to
guard. Considered and rejected the two interventions the short-form order would have offered
had the threshold been met:

- **E (reader address)** — would require inserting a second-person claim or an aside
  acknowledging the telling into a five-sentence sprint update. Fails Step 5 guardrail 4
  ("would the author recognize it?").
- **F (name the reference)** — would require naming a book, author or external event. Fails
  guardrail 2 (nothing true to name) and guardrail 4. Naming a text here would read as more
  synthetic, not less.

Both are recorded in the delivered answer as reasons not to act rather than as findings.

### Step 7: Compose the delivered answer

**Action**: Wrote the response at the length SKILL.md Step 3 prescribes — "Under 100 words,
a one-paragraph verdict with the clusters named in a sentence. No table, no corpus
percentages." Input is 51 words. Delivered two short paragraphs: the verdict with the
cluster reasoning, then why the two available interventions were declined.
**Tool**: Write → `outputs/result.md`
**Result**: Success. Deliverable is ~215 words. Slightly over the one-paragraph guidance
because the prompt explicitly asked for a fix, and a bare "nothing to fix" without the
reasoning would not answer it.

Added one editorial observation — "I have asked for review by Wednesday" does not say whom
was asked — explicitly labeled as editorial rather than as a cluster intervention, so it
does not count against the Step 3 cap of zero. It is an accountability gap in the update, not
an AI narrative pattern.

**Forbidden constructions check**: the delivered text introduces no reader-address
signposting, no vague attribution, no "in summary," no generic closer, and no didactic
emotion label. Nothing for `humanizer` to strip.

## Output Files

- `result.md` — the delivered answer, fenced between `---` lines, with commentary after the
  second fence.
- `transcript.md` — this file.
- `user_notes.md` — uncertainties and one suggestion for the skill.
- `metrics.json` — tool usage and sizes.

No rewritten version of `status-update.txt` was produced. That is the finding, not an
omission.

## Final Result

**Verdict: reads within human structural range. Zero interventions.**

Clusters A and B did not fire. E and F fired but count as one cluster between them under the
Step 3 short-professional rule, giving an effective score of 1 — the "report and stop" row.
The delivered answer explains why, and declines the two interventions the short-form order
would otherwise offer, on the grounds that both would degrade a 51-word status update.

## Issues

- **Prompt/skill tension.** The prompt asked for a fix; the skill's threshold says no fix is
  warranted. Resolved in favor of the skill, which states in three separate places that zero
  interventions is the expected and correct result for short professional writing. Recorded
  in `user_notes.md`.
- **Vacuous gate on cluster B.** With no emotional beats in the text, B's gate has nothing to
  evaluate. Scored not-fired; the skill does not address this case explicitly.
- No tool errors. No file access outside `skill_path` and the eval's own `inputs/`
  directory. `scripts/scan-ai-tells.py` was not run, per the hard constraints.
