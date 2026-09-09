# User Notes

## Uncertainty
- Register call: I classified the input as "Executive summary, status update, email, slide copy (<600 words)" from the Step 1 table. It is a sprint status update at 48 words, so this is unambiguous. It is *not* a Step 1 hard stop — hard stops are technical docs, runbooks, process instructions, data reporting, legal, and RFP answers. A status update is a listed in-scope register with A, B, E, F available, so I audited rather than refusing.
- Cluster A gate ("does the narrator state what the piece means?"): I read "If it slips past Wednesday we lose the sprint" as a factual consequence of a schedule risk, not a narratorial thematic statement. A stricter reader could call it a statement of what the update means. Even if A were scored AI-side on the gate alone, the skill requires a corroborator (moralizing >=4, dialogue-as-debate, thematic unity 5, implicit intertextual echoes), and none is present, so the cluster would still not fire.
- Cluster B: there are zero emotional beats, so the ">60% run through the body" quantitative rule has an empty denominator. I treated an absent signal as not-AI-side rather than forcing a call.

## Needs Human Review
- Nothing requiring domain expertise. The verdict is "no change," so there is no rewrite that could misrepresent facts about the sprint, the reindex, or the DBA review.

## Workarounds
- None. The skill covers this case explicitly: Step 3's paragraph on short professional text says E and F fire by construction, count as one cluster between them unless A or B also fires, and that "zero fired clusters is a real answer and the most common correct one for short professional writing."
- Per the constraint in my task, I did not run scripts/scan-ai-tells.py and did not invoke the Skill tool; the skill was loaded by reading SKILL.md and references/features.md directly from skill_path.

## Suggestions
- The Step 3 "report in proportion to the input" rule (under 100 words -> one-paragraph verdict, no table, no corpus percentages) is easy to miss because it sits at the end of a long threshold section rather than in the Output format section. Cross-referencing it from "Output format" would make the short-input behaviour harder to get wrong.
- Step 1's register table lists status updates as in-scope, but the prompt phrasing users actually type ("fix anything that reads as AI") invites a rewrite. A one-line note that the correct output for an in-range short piece is a verdict plus an offer to run `humanizer`, not an edit, would reinforce the no-op path.
