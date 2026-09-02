# User Notes

## Uncertainty
- The prompt is phrased as a full-rewrite request ("Humanize this paragraph"), but the skill's edge-case rule for already-good text says not to over-edit and to flag and leave the rest. I treated the edge case as overriding the use-case default and returned the text unchanged. A grader expecting any edit at all will disagree; I think returning it unchanged is what the skill asks for.
- The final sentence is a three-part list. I judged it load-bearing (each part is a distinct fact) and kept it. That is a judgment call under the skill's own test, but I am fairly confident.

## Needs Human Review
- Whether the user wants a response that says "this is fine" or wants at least light polish regardless. The skill is clear that polish which strips "in order to," "very," "the fact that," etc. is counterproductive, so I did not offer it.

## Workarounds
- None. No script was run (the eval rules prohibit scripts, and SKILL.md only mentions `scripts/scan-ai-tells.py` as a cross-reference, not as a required step). Density and spread were counted by hand against the word lists.

## Suggestions
- The skill would benefit from a one-line instruction in the "Full rewrite" use case pointing to the "Already-good text" edge case, so the precedence is explicit rather than inferred. Something like: "If the scan comes back within human range with no construction findings, return the text unchanged and say why."
- A short worked example of a clean-text response (what to say when there is nothing to fix) would make the output shape more consistent across runs.
