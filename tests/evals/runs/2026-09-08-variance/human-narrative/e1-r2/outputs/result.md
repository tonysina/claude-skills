---
**Register: case study / customer story.** Clusters in scope: A, B, E, F, C1. Out of scope by register: C2, D, G.

## Cluster scan

| Cluster | Gate | Corroborators | Fired |
|---|---|---|---|
| A — Thematic over-determination | States what the piece means: **yes** ("The lesson from the rollout is clear…") | Thematic unity 5 of 5 — every section serves one idea; moralizing 3; dialogue-as-debate no | ✅ |
| B — Sensory / embodied | Dominant mode: **behavioral cues** ("drivers waited in the yard", "asking why we hadn't done this years ago"). Embodied share 1 of 4 beats = 25%, below the 60% rule | Setting-as-mirror 1; no olfactory imagery; sensory density 2; inner-life depth 2; natural environment 1 — none AI-side | ❌ |
| C1 — Structural streamlining | Resolution: **external** (measured operational outcomes, not a realization) | Would have been: no subplots; causal continuity 4 of 5; Chen introduced by external description. Gate is human-side, so the cluster does not fire | ❌ |
| E — Reader engagement | Addresses the reader: **never** | Fourth-wall permeability at the floor | ✅ |
| F — Intertextual richness | Reference explicitness: **none** | Names no text, author, work or outside event — the named entities are all the piece's own subject | ✅ |

**Verdict: 3 clusters fired — some AI-side clustering. Cap of 2 interventions.** Order for a case study is A → B → F → E; B didn't fire, so A and F take the two slots.

The reason it "feels too neat" is almost entirely cluster A. The piece doesn't just report what happened, it tells you what it meant, and it does it twice in the last three sentences.

## Intervention 1 — A, thematic restraint

Deleted from "Looking ahead":

> The lesson from the rollout is clear: when the people who do the work can see the same picture, coordination stops being a daily negotiation and becomes a habit. For Ridgeline, that shift has transformed not just its mornings but its entire operating rhythm.

Nothing added in their place. Gate: yes → no.

**What it costs.** "Looking ahead" is now one sentence, and the piece ends on a plan rather than a verdict. That's the intended effect, but if this case study is running as a gated asset where the closing line does sales work, you'll want that line back — in which case tell me and I'll flag A rather than execute it. **Guardrail 3 check:** the point survives. Forty minutes to six, eleven percent fuel, twelve hours of overtime to two, plus Chen's "why we hadn't done this years ago" — a reader reconstructs the thesis without being handed it.

## Intervention 2 — F, name the reference

Added one sentence at the end of "The challenge":

> Eliyahu Goldratt argued in *The Goal* (1984) that an hour lost at a bottleneck is an hour lost for the whole system. Ridgeline's bottleneck was a phone call.

Reference explicitness: none → explicit named. This also absorbs some of the work the deleted moral was doing, one section earlier, where it reads as premise rather than verdict.

**What it costs.** It puts a business-book register into a customer story that didn't have one. If Ridgeline's marketing voice doesn't do that, drop the Goldratt sentence and keep "Ridgeline's bottleneck was a phone call" on its own — you lose the F fix but keep a concrete line. **Watch downstream:** the piece now makes a claim about a real book. Run `source-check` before it ships.

## Rewritten case study

**Ridgeline Logistics: From Spreadsheet Chaos to Coordinated Scheduling**

*The challenge*

Ridgeline Logistics runs 140 delivery vans across the Pacific Northwest. Until 2025, dispatch scheduling lived in a set of spreadsheets maintained by three regional coordinators. Every morning began the same way: coordinators phoned each other to reconcile overlapping routes, and drivers waited in the yard until the calls ended. On a typical day, vans left forty minutes late. Operations director Maria Chen felt the frustration in her chest every time she walked past the idle vans.

Eliyahu Goldratt argued in *The Goal* (1984) that an hour lost at a bottleneck is an hour lost for the whole system. Ridgeline's bottleneck was a phone call.

*The solution*

In March 2025, Ridgeline rolled out a shared scheduling platform across all three regions. Coordinators now see one live board. Route conflicts are flagged automatically, and drivers get their assignments on their phones the night before. The rollout took six weeks, including two weeks of parallel running with the old spreadsheets.

*The results*

Within the first quarter, average morning departure delay fell from forty minutes to six. Fuel spend dropped 11 percent because routes stopped overlapping. Coordinator overtime, which had run at roughly twelve hours a week per person, fell to under two.

"Honestly, I didn't expect the drivers to take to it so quickly," Chen said. "By the second week they were asking why we hadn't done this years ago."

*Looking ahead*

Ridgeline plans to extend the platform to its maintenance scheduling in 2026.

## What I didn't take, and why

- **E (fired, blocked by the cap).** The piece never addresses the reader. The fix would be one second-person line in "The challenge" — something like *if you have ever waited on a call before you could start your own work, you know what that yard felt like*. Cheap and reversible if you want it as a third change.
- **B (did not fire).** "Felt the frustration in her chest" is the one embodied beat, and it's the line most people would point at. But it's 1 of 4 emotional beats and no corroborator is AI-side — no smell imagery, no weather matching the mood, no interiority — so the cluster is inside human range and I'm not counting it as a finding. If you want it changed anyway, "Maria Chen was frustrated every time she walked past the idle vans" is the direct-label version. That's a preference, not a diagnosis.
- **C1 (did not fire).** The story resolves externally, on measured outcomes, which is the human-side call. I also can't invent an open thread here — the truth constraint means only a genuinely unresolved fact can be left unresolved, and I don't have one. If something about the rollout is still not fixed, that fact is the strongest ending available to this piece.
- **D and G.** Out of scope for the case-study register. Non-chronological ordering and moral ambiguity aren't available moves here.

Next passes: `humanizer` for surface tells, then `farnsworth-rhetoric` if you want the sentences sharpened. If `humanizer` deletes something I added, it wins.
---

Executed per skill Steps 1-5. Register triage put the piece in the case-study row (A, B, E, F, C1 in scope; C2, D, G excluded). Three clusters fired, so the Step 3 cap was 2 interventions, taken in the Step 4 short-form order A → B → F → E with B skipped for not firing. B and C1 were scored honestly as not fired despite having the piece's most visible "AI-ish" line (chest/frustration) and a tightly causal chain, per the gate-plus-corroborator rule and the "don't hunt for gates" guidance. The F insertion introduces an external factual claim, flagged for `source-check`.
