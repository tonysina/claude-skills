# Structural audit: Ridgeline Logistics case study

**Register:** customer case study. Clusters in scope: A, B, E, F, C1. Out of scope for this register: C2, D, G.

## Cluster scan

| Cluster | Gate | Call | Corroborators | Fired |
|---|---|---|---|---|
| A — Thematic over-determination | Does the narrator state what the piece means? | **Yes.** "The lesson from the rollout is clear: when the people who do the work can see the same picture, coordination stops being a daily negotiation and becomes a habit. For Ridgeline, that shift has transformed not just its mornings but its entire operating rhythm." (AI-side: 77% AI vs 52% human, a 25-point gap) | Thematic unity **5** on a 1–5 scale, every section serves "shared visibility fixes coordination" (AI-side, 4.74 vs 4.41). Moral weighting 2 (human-side). Dialogue as philosophical debate: no (human-side). Intertextual gestures: none. | **Yes** |
| B — Sensory / embodied | How are emotions most commonly conveyed? | **Mixed.** Three emotional beats: "felt the frustration in her chest" (embodied), "I didn't expect the drivers to take to it so quickly" (explicit label, in quote), drivers "asking why we hadn't done this years ago" (behavioral). Embodied share 1 of 3 = 33%, under the 60% rule. | Setting as mirror 2 on a 1–5 scale. Olfactory: no. Sensory density 2. Interior access 2. Natural environment 1. All human-side. | No |
| C — Structural streamlining (C1 only) | Is the main event chain resolved internally, externally, or unresolved? | **Externally.** A platform was rolled out and the metrics moved. Human-side. | No subplots (AI-side, 79% vs 57%). Causal continuity 5 on a 1–5 scale (AI-side, 4.20 vs 3.92). Chen introduced by external description (AI-side, 52% vs 30%). | No, gate is human-side |
| E — Reader engagement | How often does the text address the reader? | **Never.** AI-side (the paper reports direct address at 28% human vs 7% AI). | Fourth-wall permeability 1 on the 1–4 code range, the lowest. AI-side. | **Yes** |
| F — Intertextual richness | Explicit or diffuse gestures? | **None.** The piece names its own subject (Ridgeline, Chen, March 2025) but no outside text, author, work, or event. AI-side. | Names a specific external reference: no (human 47% vs AI 24%, a 23-point gap). AI-side. | **Yes** |

## Verdict

Three clusters fired (A, E, F). That is "some AI-side clustering": up to 2 interventions.

Case-study order is A → B → F → E. B did not fire, so the two interventions are A and F. E fired but sits below the cap.

## Intervention 1 — A, thematic restraint

**Changed.** Deleted the last two sentences of "Looking ahead": the stated lesson and the "transformed its entire operating rhythm" claim. Nothing added in their place. The section now ends on the one fact that is genuinely still open, the 2026 maintenance-scheduling extension.

**Point survives?** Yes. "The challenge" already shows the daily negotiation (three coordinators on the phone every morning) and "The solution" already shows the shared picture ("one live board"). A reader can reconstruct "same picture, less negotiation" without being told it. Gate: yes → no. Thematic unity stays at 5, which is fine; the AI signal was the verdict, not the coherence.

**Cost.** The piece loses its quotable takeaway line. If the publishing template requires a "key takeaway" box, it now has to be supplied outside the narrative rather than as the closing verdict. The final section is one sentence long, which reads abrupt next to the other four; that is a layout question, not a structural one.

**Watch.** If a later editor adds a closing line "to round it off," this cluster returns. The forbidden replacement forms are "In summary" and "the road ahead is promising."

## Intervention 2 — F, name the reference

**Changed.** Added one sentence to "The challenge," after "vans left forty minutes late":

> It was the constraint Eliyahu Goldratt describes in *The Goal* (1984): a system moves at the pace of its slowest step, and at Ridgeline the slowest step was a phone call.

Reference explicitness: none → explicit named.

**Cost.** The case study now makes a claim about a real book, so the paraphrase has to be verified against the source before it ships. Some customer-story house styles do not allow outside references at all; if that is the case here, drop the sentence and E becomes the second intervention instead.

**Watch.** The Goldratt sentence is the only place the narrator steps outside Ridgeline's own facts. Keep it to one clause of gloss. If it grows into a paragraph on the Theory of Constraints, the piece stops being a case study.

## Rewritten text

Ridgeline Logistics: From Spreadsheet Chaos to Coordinated Scheduling

The challenge

Ridgeline Logistics runs 140 delivery vans across the Pacific Northwest. Until 2025, dispatch scheduling lived in a set of spreadsheets maintained by three regional coordinators. Every morning began the same way: coordinators phoned each other to reconcile overlapping routes, and drivers waited in the yard until the calls ended. On a typical day, vans left forty minutes late. It was the constraint Eliyahu Goldratt describes in *The Goal* (1984): a system moves at the pace of its slowest step, and at Ridgeline the slowest step was a phone call. Operations director Maria Chen felt the frustration in her chest every time she walked past the idle vans.

The solution

In March 2025, Ridgeline rolled out a shared scheduling platform across all three regions. Coordinators now see one live board. Route conflicts are flagged automatically, and drivers get their assignments on their phones the night before. The rollout took six weeks, including two weeks of parallel running with the old spreadsheets.

The results

Within the first quarter, average morning departure delay fell from forty minutes to six. Fuel spend dropped 11 percent because routes stopped overlapping. Coordinator overtime, which had run at roughly twelve hours a week per person, fell to under two.

"Honestly, I didn't expect the drivers to take to it so quickly," Chen said. "By the second week they were asking why we hadn't done this years ago."

Looking ahead

Ridgeline plans to extend the platform to its maintenance scheduling in 2026.

## Not taken, and why

- **E (reader address)** fired but is fourth in the case-study order and the cap is 2. The available fix is one second-person claim about the reader's own dispatch mornings, not a "you might be wondering" announcement. Author's call whether to spend it.
- **B** did not fire. "Felt the frustration in her chest" is the single embodied beat, and one of three is under the threshold. The one-word version, "Chen was frustrated," is available if you want it, but the skill does not hunt for gates that are human-side.
- **C1** did not fire because the resolution is external. The neatness you are sensing probably lives in C's corroborators: every event causes the next, there are no side threads, and Chen is introduced by title. The truth constraint means none of those can be changed in a case study unless the facts support it. You cannot add a subplot that did not happen or break a causal link that did. The one thread that is genuinely open, maintenance scheduling in 2026, was already in the text, and after intervention A the piece now ends on it.
- **C2, D, G** are out of scope for the case-study register.

## Next

Run `humanizer` next for sentence-level tells; it has final say on anything added here. Before publishing, run `source-check` on the Goldratt paraphrase, since the claim about *The Goal* now has to be right.
