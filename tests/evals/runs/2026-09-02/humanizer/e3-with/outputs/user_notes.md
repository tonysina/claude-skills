# User Notes

## Uncertainty
- The prompt says "clean this up," which I read as the skill's "full rewrite" use case. The skill's "already-good text" edge case then applied: the only changes were removing markup residue. If the eval expected prose rewrites as well, none were warranted under the skill's own density/spread table (0 word-list hits in 76 words).
- I assumed a company history page is professional/business register, so I did not add first-person voice or opinions to the paragraph.

## Needs Human Review
- The removed `[cite: 4]`, `[cite: 5, 6]`, and `[cite: 9]` markers referenced a source list that was not supplied. The factual claims (2011 founding, 38 staff, two presses, ~50% packaging turnover, 2023 employee-trust sale) are now unsourced. The response tells the user to verify these against company records; a grader may want to check that this caveat is present.
- The response identifies the residue as Gemini's. That attribution comes from the skill's extended-patterns reference (Gemini section). It is accurate per the reference but the user did not say which tool produced the draft.

## Workarounds
- None. The skill's extended-patterns reference matched the residue strings directly.

## Suggestions
- The skill has no explicit guidance on what to tell the user when removing citation residue strips the only sourcing from factual claims. I added a verification note on my own judgment. A one-line instruction under "Model-specific markup residue" (for example: "when removing citation markers, tell the user the facts are now unsourced") would make this consistent across runs.
- The "Full rewrite" use case says to return "clean text followed by a brief change summary naming the patterns fixed." For residue-only cases, it might help to say whether to name the model (Gemini, ChatGPT, etc.) in the summary, since that can feel like an accusation to some users.
