Yes. Here's the structural audit and the rewrite.

**Register:** customer case study. That puts clusters A, B, E, F and C1 in scope and rules out C2, temporal restructuring (D), and the subplot/location half of G. 267 words, so this stays a light-touch pass.

## Cluster scan

| Cluster | Gate | Corroborators | Fired |
|---|---|---|---|
| **A** — thematic over-determination | states what the piece means: **yes** | thematic unity 5/5; moralizing 3/5; no philosophical dialogue | ✅ |
| **B** — sensory/embodied performativity | emotion mode: **embodied** ("felt the frustration in her chest") | setting-as-mirror 2/5; no smell imagery; sensory density 2/5; inner-life depth 2/5; natural environment 1/5 — **none AI-side** | ❌ |
| **C1** — resolution mode | resolved **externally** (a platform shipped, numbers moved) — human-side | not checked; gate is human-side | ❌ |
| **E** — reader engagement | addresses the reader: **never** | fourth wall unbroken (lowest) | ✅ |
| **F** — intertextual richness | reference explicitness: **none** | names no text, author, or outside event | ✅ |

**Three clusters fired → verdict: some AI-side clustering, cap of 2 interventions.** Taking A and F, in that order.

Two notes on what didn't fire, because both are close calls:

- **B is the one people would flag by eye.** "Felt the frustration in her chest" is the classic tell, and it is the only emotion the narrator renders directly, so the gate goes AI-side. But every corroborator is human-side — the setting never mirrors anyone's mood, there is no smell imagery, the sensory register is flat. One embodied beat is a gate, not a cluster. I'm not spending an intervention on it. If you want it anyway, "felt the frustration in her chest" → "was frustrated" is a free swap that costs the piece nothing.
- **C1 does not fire and that's a genuine strength.** The story resolves externally: a system was deployed, delays fell. It does not resolve on someone's realization. That is the human-side answer, and it's the reason this piece isn't as AI-shaped as it feels.

## Intervention 1 — A, thematic restraint

Deleted, with nothing put in their place:

> The lesson from the rollout is clear: when the people who do the work can see the same picture, coordination stops being a daily negotiation and becomes a habit.

> For Ridgeline, that shift has transformed not just its mornings but its entire operating rhythm.

The first states the theme; the second restates it one abstraction level up. Gate: yes → no.

**What it costs.** "Looking ahead" is now a single sentence about 2026 maintenance scheduling, which ends the piece on a concrete open fact rather than a verdict. The takeaway itself survives — forty minutes to six, three coordinators to one board — but it now has to be inferred. If your marketing team requires an explicit stated lesson, that requirement wins and you should restore a shorter version of the first line only; this is a case where the AI-shaped pattern may be the assignment.

**Flagged, not executed:** the headline "From Spreadsheet Chaos to Coordinated Scheduling" is the same move in miniature. Headlines are usually not the writer's to change, so I left it.

## Intervention 2 — F, name the reference

Added one specific outside referent, in "The challenge" rather than the close — putting it at the end would rebuild the verdict I just removed:

> Each spreadsheet was correct on its own terms; the conflicts existed only between them. That is the trap Eliyahu Goldratt built *The Goal* (1984) around: a plant where every station runs at peak efficiency and the plant as a whole still loses money.

Reference explicitness: none → explicit named. Human-written pieces name a specific work 47% of the time against 24% for AI — a 23 percentage point gap, and the cheapest cluster to close at this length.

**What it costs.** It puts an outside voice into customer collateral, and it's an editorial framing rather than something Ridgeline said. It does not claim Chen or anyone at Ridgeline read the book. Two things to check before this ships: run `source-check` on the Goldratt characterization, and confirm Ridgeline is comfortable having their operation described through someone else's frame.

## Rewritten

> **Ridgeline Logistics: From Spreadsheet Chaos to Coordinated Scheduling**
>
> **The challenge**
>
> Ridgeline Logistics runs 140 delivery vans across the Pacific Northwest. Until 2025, dispatch scheduling lived in a set of spreadsheets maintained by three regional coordinators. Every morning began the same way: coordinators phoned each other to reconcile overlapping routes, and drivers waited in the yard until the calls ended. On a typical day, vans left forty minutes late. Each spreadsheet was correct on its own terms; the conflicts existed only between them. That is the trap Eliyahu Goldratt built *The Goal* (1984) around: a plant where every station runs at peak efficiency and the plant as a whole still loses money. Operations director Maria Chen felt the frustration in her chest every time she walked past the idle vans.
>
> **The solution**
>
> In March 2025, Ridgeline rolled out a shared scheduling platform across all three regions. Coordinators now see one live board. Route conflicts are flagged automatically, and drivers get their assignments on their phones the night before. The rollout took six weeks, including two weeks of parallel running with the old spreadsheets.
>
> **The results**
>
> Within the first quarter, average morning departure delay fell from forty minutes to six. Fuel spend dropped 11 percent because routes stopped overlapping. Coordinator overtime, which had run at roughly twelve hours a week per person, fell to under two.
>
> "Honestly, I didn't expect the drivers to take to it so quickly," Chen said. "By the second week they were asking why we hadn't done this years ago."
>
> **Looking ahead**
>
> Ridgeline plans to extend the platform to its maintenance scheduling in 2026.

## Not taken

- **E** (reader engagement) fired and was next in order, but the cap of 2 was reached. The fix would be one second-person line — an aside about the reader's own morning standup, not a "you might be wondering." Available next pass if you want it.
- **B** did not fire; see above.
- **C1** gate is human-side; nothing to do.
- **D** (temporal restructuring) and **G** (moral ambiguity, subplots, locations) are out of scope for a case study. Reordering a customer story out of chronology or complicating its moral center is not a change this register survives.

## Downstream

This was structural only — I didn't touch sentences. Run `humanizer` next, then `farnsworth-rhetoric`. If `humanizer` deletes something I added here, it's right and I wouldn't put it back. And run `source-check` on the Goldratt sentence before this goes anywhere near a customer.
