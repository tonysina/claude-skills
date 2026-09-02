# User Notes

## Uncertainty
- The prompt says "clean this up" without specifying whether the user wants the citations preserved in some other form (footnotes, a sources line). I assumed a company history page does not carry inline citations and removed the markers outright. If the user wanted the underlying sources kept, they will need to supply them; the `[cite: N]` numbers refer to a Gemini session and are not recoverable from the text.
- I treated the prose as human-range and left it verbatim. Word-list density is 0 per 100 words with 0 patterns. That is a judgment that the skill's "already-good text" and "don't invent residual tells" rules apply; a grader expecting stylistic edits will not find any.

## Needs Human Review
- The factual claims (38 staff, two presses, packaging at about half of turnover by 2019, employee trust sale in 2023) were sourced by a chatbot. The `[span_2]` wrapper around the 2019 sentence suggests that sentence in particular was lifted or generated from a retrieved source. I flagged this to the user in the response but cannot verify any of it.

## Workarounds
- None. The skill's `references/extended-patterns.md` identified the Gemini `[cite: N]` and `[span_N](start_span)` / `[span_N](end_span)` residue directly.

## Suggestions
- The skill says residue "does not by itself prove the chatbot wrote the surrounding prose" but gives no guidance on what to tell the user about the citations that residue replaces. A one-line instruction such as "when stripping citation residue, tell the user the sources are unrecoverable from the text and the facts need independent checking" would make the residue case more consistent across runs.
- The prompt ("clean this up") is ambiguous between the skill's "Full rewrite" and "Edit with constraints" use cases. The skill could state that a bare "clean up" request on residue-only text should return the text with residue removed plus a one-paragraph explanation, rather than a findings list.
