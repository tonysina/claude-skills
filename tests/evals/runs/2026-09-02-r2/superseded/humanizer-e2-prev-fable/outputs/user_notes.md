# User Notes

## Uncertainty
- **Spread counting for overlapping lists.** "boasts a" appears on the INFLATION, AI-VOCAB and NO-COPULA watch lists. I counted it as one hit in one pattern (spread 1). Read literally, the table's "any density, 3 or more patterns -> Rewrite" row could be triggered by this single word if each list membership counts separately, which would be an absurd result for a 135-word human passage. The skill does not say how to count a word that sits on several lists.
- **"world-famous" / "premier".** I did not flag these as AI tells because they are not on any watch list and the source lists superlatives as human signs. A reader might expect a humanizer to call out promotional language of any kind; I explained the distinction in the response instead.

## Needs Human Review
- Whether the verdict "not AI" is what the eval expects. The sample looks like pre-LLM Wikipedia prose (run-on sentence, "There is a", British register, specific dates), so I treated it as a negative case and resisted inventing tells. If the eval intended this as an AI sample, the disagreement is about the sample, not the pass.

## Workarounds
- None. The skill's "Review and flag" use case mapped directly onto the prompt.

## Suggestions
- Add one line under "When a flag is a finding" on how to count a single word that appears on multiple watch lists (e.g. "count it once, under the highest-signal list it belongs to").
- The "Review and flag" use case says to "offer to rewrite." For a clean negative case it would help to say explicitly that the offer can be reframed as ordinary copyediting, so the response does not imply there is AI residue to remove.
