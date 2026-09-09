# User Notes

## Uncertainty

- **Cluster A's moralizing corroborator was a close call.** I scored "how heavily does the piece foreground moral or philosophical questions" at 3 of 5 (below the ≥4 AI-side threshold). A fired on thematic unity (5 of 5) instead. If a grader scored moralizing at 4, A still fires — the verdict is unchanged either way — but the corroborator line in the table would differ.
- **Cluster B's gate is genuinely ambiguous.** The piece has roughly three emotional beats: Chen's frustration (embodied), Chen's quoted surprise, and the drivers' reported reaction. Only the first is narratorial, so I called the dominant *narratorial* mode embodied and the gate AI-side, then let the cluster fail on zero corroborators. An equally defensible read calls the dominant mode "behavioral cues" and the gate human-side. Both routes end at "B does not fire", so no intervention hinged on it.
- **Cluster F's gate reading.** I treated "intertextual gesture" as reference to something outside the story world, so Maria Chen, Ridgeline, and "March 2025" do not count as named references. If a reader counts in-story proper nouns, F would not fire and the count drops to 2 clusters — which still lands in the same threshold band (2–3 fired, cap 2).
- **Word count vs register row.** The piece is ~330 words, which is under the 600-word row's ceiling, but I triaged on register (case study), as Step 1 explicitly instructs ("Length is not the mode; register is"). This matters only for whether C1 is in scope; C1 did not fire regardless.

## Needs Human Review

- **The second-person line I added is a voice decision, not just a structural one.** Many B2B case studies hold third-person neutrality on purpose; a marketing owner may reject it on brand grounds even though cluster E fired legitimately. It is the single change most likely to be reverted.
- **The deleted closing.** Some case studies exist precisely to deliver that takeaway sentence to a skimming buyer. The skill's own "Some AI patterns are the assignment" note applies. I judged the point survives in the numbers, but if this piece is used as a one-page leave-behind where readers only see the last paragraph, the deletion has a real cost.
- **Everything about F and C1 depends on facts I do not have** — the platform's actual name, what triggered the project, and whether anything about the rollout is genuinely still open. Those are the highest-leverage remaining edits and only the author can make them.

## Workarounds

- **F was blocked, so E was promoted into its slot.** SKILL.md Step 5 says a blocked intervention is reported rather than counted and the next in order takes its slot under the cap. I applied that literally: A + E executed, F reported. Worth confirming that this is the intended reading, since Step 4 says "take from the top; stop at the cap" and does not itself mention promotion.
- No tooling failures. `scan-ai-tells.py` was not run, per the eval's hard constraints.

## Suggestions

- **The F truth problem deserves its own note in SKILL.md.** The C1 fix carries an explicit truth constraint ("flag the intervention for the author instead of executing it"), and F needs the identical treatment for exactly the same reason: naming a real reference in someone else's case study means asserting a fact you do not have. The skill's two F constraints cover accuracy (`source-check`) and vagueness (`VAGUE-ATTRIB`) but not "you have no reference to name." Right now the editor has to borrow C1's language. In the case-study row, where the order is A → B → F → E, this is the common path, not an edge case.
- **A short worked example in a non-fiction register would help.** The only worked example is thought leadership, where the narrator is the author and can honestly name a book they read. A case study, where the narrator is a vendor writing about a customer, hits the truth constraint on two of the four available clusters, and the correct output is closer to "one edit plus two asks" than to the example's three clean interventions.
- **Consider naming what happens when B's gate fires with zero corroborators.** It is a common shape in short professional writing (one stray embodied line and nothing else), and the firing rule handles it correctly, but an explicit sentence would stop editors from either over-firing B or quietly deleting the line anyway.
