# User Notes

## Uncertainty

- **Cluster A's delivered verdict.** I scored the essay as having all elements serve one theme (thematic unity 5/5), which fires A alongside the gate. The moralizing corroborator scored 3 of 5 (below ≥4 AI-side threshold), but thematic unity alone is enough. If a grader scores moralizing at 4, the verdict is unchanged — A still fires — but the corroborator would be listed as AI-side.
- **Cluster B's interpretation.** The essay has three named emotional beats: stomach drop (embodied), familiar heat rise (embodied), and the "blinked" moment (not embodied). That is 2 of 3, above 60%, which makes the quantitative rule trigger and the gate AI-side on that basis alone. However, the dominant narrative mode is still best read as embodied. Either way, B does not fire because no corroborators are AI-side, so the interpretation does not affect the output.
- **Cluster G's likelihood.** G fired, but the decision to not execute it (cap hit after A and E) means a grader could reasonably verify it differently and still reach the same conclusion. The essay does frame the protagonist positively throughout; whether you score the moral stance as "clearly positive" or "ambivalent with a positive conclusion" determines whether G fires, but in either case it comes late enough in the intervention order that it would not execute under cap.

## Needs Human Review

- **The second-person line is a voice decision.** Some readers and editors believe personal essays should hold consistent narrative perspective; the added line breaks that. It is structurally justified by cluster E firing, but it may not fit the author's intent for the piece.
- **The deleted closing matters for downstream use.** If this essay is excerpt ed in a highlights reel or used as a quick-read case for "saying no," the deleted lesson-statement is a real loss. The skill judges that the point survives in the facts, but that judgment is qualitative and context-dependent. An editor who knows the downstream use case might reject this intervention.
- **F's execution depends on information you have and I don't.** You read this essay and decided it feels AI-written; you have context (perhaps other essays, the revision history, what you were aiming for) that would tell you whether it draws from a named source. If it does, naming it closes the highest-value remaining move.

## Workarounds

- **F was blocked by the truth guardrail.** The essay does not name any external work, methodology, person, book, or article that shaped its argument. The F fix requires naming one. Without that from the author, I could not execute it — inventing a reference would violate Step 5 guardrail 2. Reported instead and the next cluster (E) took the slot.
- No tool failures or script runs. Per the hard constraints, `scan-ai-tells.py` was not run, and the Skill tool was not invoked.

## Suggestions

- **F deserves the same truth-constraint framing for non-fiction that C1 has.** C1 carries an explicit note: "In non-fiction you may only leave unresolved what is *actually* unresolved." F needs equivalent guidance for case studies and essays: "You may only name a reference that the author actually used or the piece actually invokes." Right now an editor has to infer this from the guardrail pass (no intervention may invent a fact), but it is not explicit in the F cluster itself.
- **Consider noting what B's firing rule looks like in short work.** B's corroborators require very specific sensory markers (olfactory, setting-mirror at 4+, inner-life depth 4+). In essays of 400–600 words, B's gate often fires (embodied metaphors are not uncommon) while corroborators are sparse. The rule handles it correctly (no fire without both), but seeing it happen repeatedly might lead an editor to either skip B or second-guess the corroborators. A note on the expected pattern would help.
