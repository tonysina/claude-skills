# User Notes

## Uncertainty

- **Cluster B fires on a judgment call.** 3 of 7 emotional beats run through the body, which is under the skill's >60% quantitative auto-fire rule. The gate therefore rests on the dominant-mode plurality (embodied 3, behavioral 2, explicit label 2) plus one corroborator, depth of interior access, which I scored 4 on a 1–5 scale against a human mean of 3.67 and an AI mean of 3.93. A scorer who called that 3 would leave B with a gate and no corroborator, and B would not fire. The delivered answer says so explicitly rather than hiding it.
- **Emotional-beat segmentation is not defined by the skill.** I counted 7 beats. Whether "I stared at the calendar until the squares blurred" is behavioral or embodied, and whether "I heard myself say yes" counts as a beat at all, changes the percentage materially. Someone counting 5 beats with 3 somatic would cross the 60% line and fire B on the quantitative rule alone.
- **Thematic unity scored 5, which is the AI-side threshold exactly.** The corroborator requires ≥5, not ≥4, so this one is at the boundary. Cluster A still fires on moral weighting alone, so the finding does not depend on it.
- **Register call.** I read this as personal essay, which puts every cluster in scope. If the author intends it as thought leadership or a LinkedIn post, C2, subplots and location variety drop out of scope. The three interventions I recommended (A, B, F) are in scope under both readings, so the recommendation is stable either way, but the "not taken" section would change.

## Needs Human Review

- **The A intervention was deliberately not executed and instead handed back as a question.** The skill's Common Issues section says a stated thesis may be the point of a thesis-driven essay and to flag rather than silently restructure. A grader expecting a decisive deletion may read the flag as hedging. I judged the flag to be the more faithful reading, since a personal essay built around "what I learned" is exactly the case that section describes.
- **The C1 finding depends on a fact I do not have.** Whether "everything at work got easier, and I have never gone back" is true is the author's to confirm. Under the truth constraint I reported it instead of rewriting it. It was below the cap regardless, so no intervention slot was freed by the block.
- **The F recommendation risks inviting a fabricated citation.** I told the author to skip it if no real source shaped the piece, and warned against `humanizer`'s `VAGUE-ATTRIB` substitutes, but the instruction "name a real book here" is the one recommendation in this report that can produce a false claim if followed carelessly. Worth watching if this eval is ever run in execute mode rather than diagnosis mode.

## Workarounds

- None. Every step of the skill applied cleanly to this input.
- Read `SKILL.md` and `references/features.md` directly per the hard constraints. Did not invoke the Skill tool, did not read any other skill directory, did not run `scripts/scan-ai-tells.py`, and read nothing under `tests/evals/` outside the assigned inputs directory. `references/changelog.md` was listed but not read; it is version history and not needed to execute an audit.

## Suggestions

- **The Output format section does not say which shape a "why does this feel AI-written" prompt gets.** That exact phrasing is listed as a trigger in the frontmatter, but the three output shapes are "Diagnosis only", "Full audit + rewrite" and "Targeted intervention", and a "why" question maps to the first only by inference. One sentence mapping the trigger phrases to the output shapes would remove the guess. This is likely a source of run-to-run variance: another run could reasonably deliver a full rewrite here.
- **Emotional beats need a counting rule.** Cluster B has a precise numeric threshold (>60%) sitting on top of an undefined denominator. A one-line definition of what counts as a beat, or a worked count in the existing example, would make B reproducible across runs. The worked example says "3 of 3 beats through the body" without showing the segmentation.
- **The threshold table saturates.** Anything at 4 or more fired clusters gets the same verdict and the same cap, so 4 fired and 7 fired are indistinguishable in the output even though they describe very different pieces. A note on how to phrase the difference, or a distinct label above some higher count, would help the report track the input.
- **Cluster A's thematic-unity corroborator uses ≥5 while every other Likert corroborator uses ≥4.** The asymmetry looks deliberate given the 4.41 / 4.74 means, but it is easy to misread as a typo when scanning the cluster quickly.
