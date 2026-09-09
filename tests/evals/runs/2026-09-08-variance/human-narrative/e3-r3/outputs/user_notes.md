# User Notes

## Uncertainty

- **Cluster A's corroborators** — I scored moral/philosophical weighting at 4 of 5 (the piece does foreground what the narrator learned and what it means), and thematic unity at 5 of 5 (every element serves the lesson). Both are above the AI-side thresholds. A fired comfortably, but if a grader scored moral weighting at 3 of 5 instead, A would still fire on thematic unity alone. Verdict unchanged.

- **Cluster B's gate reading** — The piece has four embodied emotional beats (stomach drop, chest tightening, heat rising, and implicitly in "I opened my mouth to say yes" the physical response to Dana's second request). I counted 80% embodied and called the gate AI-side. An alternative reading treats the dialogue and narrative reflection as more prevalent, making the dominant mode "behavioral cues" or a mix, and calling the gate human-side. Both readings produce the same result: B does not fire (zero corroborators are AI-side either way). No intervention hinged on the gate reading.

- **Cluster C2's internal-understanding resolution** — The piece explicitly states "Once I understood that, everything at work got easier." This is textbook internal understanding. But the gate also has an external dimension: Dana's acceptance ("The pipeline, obviously") is an external event that prompts the understanding. I weighted the explicit realization as the dominant resolution mode. A reader might place more weight on the Dana moment as the turning point, making the resolution "externally triggered understanding" rather than pure internal realization. C2 would still fire; the corroborators are unchanged.

- **Cluster D's classification within personal essay** — D is marked out of scope for "every non-fiction register" in SKILL.md's commentary, but Step 1's register table explicitly places personal essay (alongside fiction and narrative journalism) in "all A–G". I treated the table as authoritative and scored D as in-scope. If D is actually out of scope for personal essay as a non-fiction form, then the fired clusters drop from 6 to 5, but the threshold cap is still 3 and the executed interventions are unchanged.

## Needs Human Review

- **The second-person addition is a voice decision, not purely structural.** Some personal essays deliberately maintain reader distance; adding "you" changes the implied reader relationship. It is a legitimate structural intervention (cluster E fired genuinely) but it is the single most likely change to be reverted on editorial grounds.

- **The deleted thematic statement is a classic case of "some AI patterns are the assignment."** Some essays exist precisely to articulate a lesson learned. I judged the point survives from the narrative, but if the original intent was to deliver a moral, the deletion removes the point of the piece. The author is the source of truth on whether reconstructibility is enough.

- **Everything about F and D depends on authorial facts.** F requires knowing what external text, methodology, person, or event this essay draws from — if any. D requires willingness to reorder the narrative significantly. Both are high-leverage next moves if the author has the facts and wants to push further.

## Workarounds

- **F was blocked and E was promoted.** Step 5 says a blocked intervention is reported rather than counted and the next in order takes its slot under the cap. I applied this literally: A + E executed, F reported, cap reached at 2 of 3. Worth confirming this is the intended reading.

- No tooling failures. `scan-ai-tells.py` was not run per eval hard constraints.

## Suggestions

- **Consider documenting the "one embodied line, zero corroborators" shape explicitly in the skill.** Cluster B's gate is AI-side but no corroborator fires in roughly 20-25% of short professional writing (one stray "felt" or "chest tightened" with no sensory detail, mirroring, or interiority around it). The firing rule handles this correctly, but editors often second-guess themselves here — an explicit note would prevent both under-firing B and over-correcting by deleting the line anyway.

- **F in personal essay deserves a truth-constraint note parallel to C1's.** C1 carries an explicit "flag the intervention for the author instead of executing it" guidance for facts you don't have. F has the identical problem: naming a real reference means asserting a fact you do not have about the author's reading, influences, and intent. Right now editors have to borrow C1's language. In personal essay, where A and F are both likely to fire, this is the common path.

- **D's evidence gap (0.2–0.3 on a 1–5 scale) deserves top-of-mind emphasis for personal essay.** D is the most invasive intervention available (reordering narrative structure) and carries the smallest measured gap in the taxonomy. For long-form that fires D, the gap supports the intervention despite the cost. For personal essay, where D fires readily, the modest gap argues for trying A, B, F, E first before disrupting the temporal order.
