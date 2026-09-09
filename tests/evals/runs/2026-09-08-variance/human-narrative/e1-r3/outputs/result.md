---BEGIN DELIVERED---
Register: **case study / customer-facing narrative**. Clusters in scope: A, B, E, F, C1. Out of scope for this register: C2, D, G.

## Cluster scan

| Cluster | Gate | Corroborators | Fired |
|---|---|---|---|
| A — thematic over-determination | Narrator states what the piece means: **yes** ("The lesson from the rollout is clear…") | Thematic unity 5 on a 1–5 scale — every section serves the one idea; moral/philosophical weighting ~3 | ✅ |
| B — sensory / embodied | Dominant emotional expression: embodied ("felt the frustration in her chest"), but only 1 of 2 emotional beats runs through the body — under the 60% rule | None AI-side: no olfactory imagery, no setting-as-mirror, sensory density ~2 and interior access ~2 on a 1–5 scale, natural environment barely present | ❌ |
| C1 — structural streamlining | Mode of resolution: **internal understanding** (the piece closes on a realization, not on the numbers) | No subplots; causal chain continuity 4–5 on a 1–5 scale (chaos → platform → results → future, each causing the next); Chen introduced by external description ("Operations director Maria Chen") | ✅ |
| E — reader engagement | Direct reader address: **never** | Fourth-wall permeability at the bottom of the range | ✅ |
| F — intertextual richness | Reference explicitness: **none** | Names no text, author, work or outside event — Ridgeline, Chen and the March 2025 rollout are the subject, not a reference the piece is in conversation with | ✅ |

**Verdict: 4 clusters fired — systematic AI-side clustering. Cap: 3 interventions.**

Order for this register is A → B → F → E, with C1 after. B didn't fire, so: **A, F, E**. C1 fired but falls below the cap.

For scale: narratorial thematic commentary appears in 77% of AI stories vs 52% of published human ones (−25 percentage points); internal-understanding resolution 47% vs 27% (−20 pp); explicit named reference 24% vs 47% (+23 pp human-side).

## Intervention 1 — A, thematic restraint

Deleted from "Looking ahead":

> The lesson from the rollout is clear: when the people who do the work can see the same picture, coordination stops being a daily negotiation and becomes a habit. For Ridgeline, that shift has transformed not just its mornings but its entire operating rhythm.

Nothing added in its place. The subhead also stated the arc, so "From Spreadsheet Chaos to Coordinated Scheduling" becomes the concrete version.

**What changed structurally.** The narrator no longer delivers the verdict; the numbers in "The results" carry it. Gate: yes → no.

**What it costs.** A case study is often a sales asset, and someone may want that takeaway line back. If it has to return, the honest home for it is Chen's mouth as a quote, not the narrator's.

## Intervention 2 — F, name the reference

Added one paragraph at the end of "The challenge," placed early so the idea reads as premise rather than verdict — which is where cluster A wants it:

> Peter Senge used the beer distribution game in *The Fifth Discipline* (1990) to show what happens when everyone in a chain can only see their own segment: each person corrects for a picture no one else has, and the corrections collide.

**What changed structurally.** Reference explicitness: none → explicit named. The piece now has something outside itself to sit against.

**What it costs.** It slows the challenge section, and it imports an outside voice into a customer story — some brand guidelines don't allow that in a case study. It also creates a fact-checking obligation: run `source-check` on the Senge characterization before this ships.

## Intervention 3 — E, reader address

One second-person claim in "The challenge," about the reader's own experience rather than about the structure of the piece:

> If you have run a yard at six in the morning, you know what forty idle minutes does to a day that was already tight.

**What changed structurally.** Direct reader address: never → occasional aside.

**What it costs.** It assumes an operations reader. On a general marketing page that assumption is wrong and the line should go. Watch it in editing too — if it drifts toward "you might be wondering why this mattered," `humanizer` will delete it as signposting, and it should.

## Not taken

- **C1 (resolution mode)** fired and was next in order, but the cap was reached. Worth knowing: intervention A partly did C1's work by accident, because the sentence that stated the theme *was* the internal-understanding resolution. With it gone, the piece ends on "Ridgeline plans to extend the platform to its maintenance scheduling in 2026" — a real, concrete, genuinely unfinished thing, which is what C1's fix asks for. What C1 would still have addressed is the unbroken causal chain and Chen's introduction by job title. Those are untouched. I couldn't have gone further than the existing facts allow anyway: the truth constraint forbids inventing an open thread in a case study, and the only open thread the source text actually contains is the 2026 maintenance plan.
- **B** did not fire. "Felt the frustration in her chest" is the one embodied beat, and on its own it's a gate flag without a corroborator — no smell imagery, no weather matching the mood, low sensory density. Converting it to "was frustrated" would be a fine edit, but it isn't a structural finding and I'm not spending an intervention slot on it.
- **D (temporal) and G (moral ambiguity)** are out of scope for the case study register. Reordering this piece to open at the crisis, or complicating the moral center so the platform both solved and cost something, would both move it toward the human distribution — and both are things a customer-approved case study can't do without the customer's sign-off.

***

## Rewritten case study

**Ridgeline Logistics: 140 Vans, Three Spreadsheets, One Board**

**The challenge**

Ridgeline Logistics runs 140 delivery vans across the Pacific Northwest. Until 2025, dispatch scheduling lived in a set of spreadsheets maintained by three regional coordinators. Every morning began the same way: coordinators phoned each other to reconcile overlapping routes, and drivers waited in the yard until the calls ended. On a typical day, vans left forty minutes late. If you have run a yard at six in the morning, you know what forty idle minutes does to a day that was already tight. Operations director Maria Chen felt the frustration in her chest every time she walked past the idle vans.

Peter Senge used the beer distribution game in *The Fifth Discipline* (1990) to show what happens when everyone in a chain can only see their own segment: each person corrects for a picture no one else has, and the corrections collide. Ridgeline's three coordinators were each solving a real problem, on three separate boards.

**The solution**

In March 2025, Ridgeline rolled out a shared scheduling platform across all three regions. Coordinators now see one live board. Route conflicts are flagged automatically, and drivers get their assignments on their phones the night before. The rollout took six weeks, including two weeks of parallel running with the old spreadsheets.

**The results**

Within the first quarter, average morning departure delay fell from forty minutes to six. Fuel spend dropped 11 percent because routes stopped overlapping. Coordinator overtime, which had run at roughly twelve hours a week per person, fell to under two.

"Honestly, I didn't expect the drivers to take to it so quickly," Chen said. "By the second week they were asking why we hadn't done this years ago."

**Looking ahead**

Ridgeline plans to extend the platform to its maintenance scheduling in 2026.

***

Two things to watch downstream. The Senge claim is now a real citation and needs checking against the source before publication. And this was a structural pass only — I didn't touch sentences, so run `humanizer` next and `farnsworth-rhetoric` after that.
---END DELIVERED---

Executor commentary (not part of the delivered answer):

- Register triage put this in the "case study / customer story" row: clusters A, B, E, F, C1 in scope; C2, D, G excluded.
- The Step 3 "count E and F as one cluster" carve-out did not apply, because it is conditioned on A and B not firing, and A fired. So the count is 4 and the cap is 3.
- Intervention selection followed the Step 4 short-form/case-study order (A → B → F → E) with B skipped as unfired; C1 sits after E in the long-form order and fell below the cap.
- The C1 truth constraint was the binding limit on the ending: the only genuinely unresolved fact in the source is the 2026 maintenance extension, and no open thread was invented.
- The F reference (Senge, *The Fifth Discipline*, 1990, beer distribution game) is a real work and a standard characterization of that exercise, but it is a claim about a source and is flagged for `source-check` in the delivered answer, per the skill.
