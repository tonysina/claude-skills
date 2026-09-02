# User Notes

## Uncertainty
- The eval prompt ("make this land") is a listed trigger for the skill, but the input is a runbook, which the skill's description lists under "Do NOT use for". I resolved this via the register table inside SKILL.md ("Technical, legal, process, data → Stop. Diction work only. No figures.") rather than refusing the task. If the intended behavior was to decline and redirect, this run diverges from that.
- "Significant lag" in the original is not explicitly equated to "more than thirty seconds". I kept the word "significant" rather than resolving the ambiguity. A grader might have preferred "that much lag" as the tighter reading.
- The imperative mood flattens the original's modal distinctions ("should" verify, "may proceed", "is required", "must" update). I preserved "may proceed" as permission and flagged the "should" → imperative change in the claim check, but a strict reading could count this as a hedge becoming a command.

## Needs Human Review
- Whether dropping "the on-call engineer" in favor of the implied second person is acceptable for the runbook's actual readership. Flagged in the change note.
- The thirty-second boundary gap (exactly thirty seconds is unaddressed) is inherited from the source. I called it out rather than fixing it, per the skill's claim check rule against manufacturing detail.
- "Run the replication status query from the operations wiki" reorders the original's two sentences (check lag first, then how). The query is the check, so I read them as one action, but a reviewer should confirm the reorder does not change the procedure.

## Workarounds
- None. The skill's register table gave a clear stop condition and the diction rules were sufficient for the rest.
- Did not load references/figures.md: SKILL.md says to load it only when core figures don't fit or the user names a figure, and the budget was zero. Did not load references/changelog.md; nothing in SKILL.md points to it.

## Suggestions
- The skill's front matter says "Do NOT use for ... process instructions" while the body's register table handles that case gracefully with "diction work only". The two are consistent in outcome but could confuse a router: one says don't trigger, the other says trigger and stop at diction. A one-line note in the description ("process text gets diction work only") would reconcile them.
- The output format template assumes at least one figure was applied. A worked example of a zero-figure change note would help, since the skill says zero is a valid spend but never shows what that report looks like.
- The Saxon-finish rule is hard to apply to runbook sentences that must end on a system noun ("configuration service", "application tier", "standby instance"). A line acknowledging that precision outranks the finish in process text would save a round of second-guessing.
