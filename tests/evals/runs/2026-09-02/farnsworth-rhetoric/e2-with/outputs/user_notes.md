# User Notes

## Uncertainty
- Register call: an engineering-blog post-mortem is not an exact row in the skill's register table. I treated it as first-person narrative blog writing (closest to "thought leadership," half budget) rather than "technical, process, data" (stop, no figures). Under either reading the outcome is the same for a 91-word piece: at most 1 figure, and the author already spent it. But if the grader expected the "technical → stop" branch, the transcript reasoning differs even though the output does not.
- Word count: I counted 91 words by hand and with `wc -w`. The budget line in the note says 91 words; a count of 90 or 92 would not change the budget tier.
- I identified the closing "cost us ... signups and a lesson" as a zeugma. The skill's core figures list does not include zeugma, and I did not load references/figures.md (the skill says to load it only when the core figures do not fit or the user names a figure). If figures.md does not list zeugma either, my label is from general rhetoric, not from the skill's catalog. The judgment that the ending already carries a figure and should not get another one does not depend on the label.

## Needs Human Review
- The "half of Europe" claim is the author's, not mine. I flagged it in the claim check as a fact question rather than editing it, because the skill says not to touch author claims for rhythm and not to invent support. A reviewer may want to decide whether flagging it at all was in scope.
- The response returns the text unchanged. If the eval expects any diction edit at all, this will read as a null result. I believe null is correct per the skill's "Zero figures is a real answer" guidance.

## Workarounds
- None. The skill's workflow applied directly.

## Suggestions
- The register table could add a row for "narrative blog post / post-mortem / personal essay" so the executor does not have to choose between "thought leadership" and "technical." The two rows give different instructions (half budget vs. stop), and a post-mortem sits between them.
- The output-format template has no line for the ear test result, though the guardrails section makes it mandatory. I added an "Ear test:" line to the change note. Adding it to the template would make the mandatory check visible in every strengthen response.
- The template's "Applied:" line assumes at least one figure. A canonical phrasing for the zero-figure case (for example, "Applied: none, and why") would make the null result look deliberate rather than like a skipped step.
