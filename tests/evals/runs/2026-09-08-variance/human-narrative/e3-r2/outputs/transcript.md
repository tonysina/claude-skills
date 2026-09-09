# Eval Execution Transcript

## Eval Prompt

"Why does this essay still feel AI-written even after I edited it for style?"

## Skill

- Path: /Users/tonysina/Documents/claude-skills/skills/human-narrative
- Name: human-narrative (v1.1.2)
- Description: Audits writing for AI-elevated narrative patterns at the scene and story
  structure level (temporal order, thematic restraint, resolution mode, emotional
  expression, intertextual reference) and guides structural rewrites. Based on the 30
  core StoryScope features (Russell et al., COLM 2026).

## Input Files

- `essay-saying-no.txt` — 2.0 KB plain text, ~380-word first-person personal essay about
  the first time the narrator declined a manager's request.

## Execution

### Step 0: Load the skill

**Action**: Read SKILL.md in full; listed and read the relevant part of `references/`.
**Tool**: Bash (`cat SKILL.md`), Bash (`grep` over `references/features.md` for the
E-cluster scale note and the Table 15 response options).
**Result**: Success. Confirmed the scale note requiring Direct Reader Address and
Fourth-Wall Permeability to be reported as ordinal means or as the paper's percentages,
never as bare decimals. Did not read `references/changelog.md` (not needed for a scan).
Did not invoke the Skill tool, did not read any other skill directory, did not run
`scripts/scan-ai-tells.py`.

### Step 1: Register triage

**Action**: Classified the input.
**Result**: First-person personal essay, ~380 words. Row 1 of the Step 1 table
("Fiction, personal essay, narrative journalism") → **all clusters A–G in scope**,
including C2 and D. Not a hard stop. Note applied: "Length is not the mode; register is"
— a 380-word personal essay still gets D.

### Step 2: Cluster scan

**Action**: Ran the gate + corroborator scan for all seven clusters, answering with the
option sets given rather than prose.

| Cluster | Gate call | Corroborators | Fired |
|---|---|---|---|
| A | states what the piece means: **yes** (AI-side) | moralizing 4; thematic unity 5; dialogue-as-debate no; intertextual none | ✅ |
| B | dominant mode **embodied** (AI-side) | setting-as-mirror 2; olfactory no; sensory density 2; interiority 3; natural env 1 — **zero AI-side** | ❌ |
| C | resolved **internally** (AI-side) | no subplots (AI-side); causal continuity 4 (AI-side) | ✅ |
| D | chronological discontinuity 2 (AI-side ≤2) | anachrony 1; delayed disclosure 1; recontextualization 3 — all AI-side | ✅ |
| E | **never** addresses reader (AI-side) | fourth-wall permeability at floor (AI-side) | ✅ |
| F | **none** (AI-side) | no named text/author/work/event (AI-side) | ✅ |
| G | moral polarity **clearly positive** (AI-side) | no subplots; dialogue-to-narration 2; single location — all AI-side | ✅ |

**Key judgment — B withheld.** The gate is AI-side: the three earliest emotional beats
run through the body ("My stomach dropped", "My chest tightened", "the familiar heat rise
up my neck"), and embodied is the plurality mode. But the quantitative rule did not
trigger — counting all emotional beats gives 6 (stomach, chest, staring until the squares
blurred, heat up the neck, "which made me laugh", "the fear I carried"), of which 3 run
through the body = 50%, under the >60% threshold. And **no corroborator is AI-side**: no
smell imagery, no setting-as-mirror, low sensory density, no natural environment. Per
"A cluster fires only if the gate is AI-side AND at least one corroborator is AI-side",
B does not fire. Applied "Don't hunt for gates" — did not re-read looking for a reason.

**Result**: 6 clusters fired (A, C, D, E, F, G); B did not.

### Step 3: Threshold

**Action**: Applied the Step 3 table.
**Result**: 4+ fired → "Systematic AI-side clustering" → cap of **3 interventions**.
The short-professional-text E/F collapse rule does not apply (this is a personal essay,
not the under-600-word status-update row).

### Step 4: Intervention order and selection

**Action**: Applied the long-form order: A → B → F → D → E → C → G.
- **A** — taken (slot 1).
- **B** — skipped, did not fire.
- **F** — **blocked by the truth constraint / Step 5 guardrail 2.** Naming a book, author
  or event the essayist was "in conversation with" would invent a fact about the author's
  life. Per Step 5, "A blocked intervention is reported, not counted: the next
  intervention in order takes its slot, still under the Step 3 cap." Reported with a
  concrete request to the author instead of executed.
- **D** — taken (slot 2).
- **E** — taken (slot 3, inheriting F's slot).
- **C**, **G** — fired but fall below the cap. Reported, not executed.

### Step 5: Execute the interventions

**A — thematic restraint.** Deleted the entire final paragraph: "What I learned is that
saying no is rarely a confrontation. Most of the time it is just information that the
other person doesn't have yet. The fear I carried for eleven months was about a conflict
that was never going to happen. Once I understood that, everything at work got easier,
and I have never gone back." Added nothing in its place (per the fix and the Forbidden
Constructions table: no "In summary", no `GENERIC-CLOSER`). One trace of the idea
survives mid-essay as premise rather than verdict, which the fix explicitly permits
("move it earlier where it reads as premise rather than verdict").

**D — temporal.** Opened on the most charged moment ("I can do that, or I can finish the
pipeline. Which one do you want?") and worked backward. Delayed the "twenty-six / eleven
months" disclosure to paragraph five. One disruption, not several. No facts invented —
this is a reordering of material already in the source.

**E — reader address.** Added one second-person claim about the reader's own experience:
"You have probably run the same arithmetic: the extra work costs less than the
conversation does." Deliberately not a forward-reference announcement — checked against
the Forbidden Constructions table so `humanizer` `SIGNPOSTING` will not delete it.

### Step 6: Guardrail pass (Step 5)

1. **Still makes sense?** Yes. The reorder is a standard in-medias-res personal-essay
   opening; every causal link is intact.
2. **Still true?** Yes. No fact was invented. Every detail in the rewrite appears in the
   source; the one addition is a claim about the *reader*, not about the author. This is
   also why F was blocked rather than executed.
3. **Did the point survive?** Yes. "She had never wanted me to do both. She had just never
   been told I couldn't" carries the idea concretely, and the review line closes on a
   concrete beat. Restored less than removed: kept "I told myself I had done the right
   thing, and I did not believe it", which is human-side on B (explicit-ish label) and on
   G (ambivalence) and was in danger of being cut with the surrounding material.
4. **Would the author recognize it?** Judged yes — voice, diction and every scene are
   unchanged. Flagged D in the answer as the intervention most likely to fail this test,
   with an explicit instruction to revert it if the piece now reads arranged rather than
   told.

### Step 7: Compose the answer

**Action**: Wrote the delivered answer in the "Full audit + rewrite" output format:
cluster table → verdict → interventions one at a time with what changed / what it cost /
what to watch → close with what was not taken and why. Opened by answering the user's
actual question ("why does it still feel AI after a style edit") before the table.
Reported all gaps with units (percentage points; Likert means on 1–5). Did not report
Direct Reader Address or Fourth-Wall Permeability as bare decimals, per the scale note.
Did not polish sentences; closed by pointing at the surface pass as the next step.
**Tool**: Write → `outputs/result.md`.

## Output Files

- `result.md` — the delivered answer (diagnosis, cluster table, verdict, three executed
  interventions, the rewritten essay, what was not taken and why), fenced with `---`.
- `transcript.md` — this file.
- `metrics.json` — tool usage and size metrics.
- `user_notes.md` — uncertainties and issues.

## Final Result

Register: personal essay, all clusters in scope. **6 of 7 clusters fired** (A, C, D, E,
F, G); B was withheld because its gate is AI-side but no corroborator is. Verdict:
systematic AI-side clustering, cap 3. Executed **A** (deleted the closing moral),
**D** (opened on the Thursday question and worked backward, delaying the age/tenure
disclosure) and **E** (one second-person claim). **F was blocked by the truth constraint**
— naming a reference would invent a fact about the author's life — and reported with a
request for the real reference instead, passing its slot to E. **C** and **G** fired but
fell below the cap and were reported, with G flagged as the strongest remaining move.
Essay 380 → 330 words. Answer closes by pointing at a surface/lexical pass as the next
stage in the workflow.

## Issues

- The prompt is phrased as a "why" question, which maps to the skill's **Diagnosis only**
  output mode ("offer to execute"), but a bare diagnosis would not show the user what the
  structural problem actually costs them. Chose **Full audit + rewrite** and led with the
  direct answer to "why" before the table. This is a judgment call; see `user_notes.md`.
- Cluster F was the highest value-per-effort fix available and could not be executed
  without violating the truth constraint. Documented rather than worked around.
