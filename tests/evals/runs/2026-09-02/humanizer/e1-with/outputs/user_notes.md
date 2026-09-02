# User Notes

## Uncertainty
- The retention claim ("Companies that shorten onboarding tend to keep more of the customers they sign") is kept as a direct assertion with no source. The original attributed it to "industry reports," which is a VAGUE-ATTRIB tell, but I had no real source to substitute. I flagged this in the response rather than fabricating a citation or inserting a bracketed placeholder (placeholders are themselves a tell per extended-patterns.md).
- "tracks how users move through setup, so your team can see where people slow down or drop off" is my reading of "robust analytics to enhance visibility into user behavior." It is a reasonable interpretation for onboarding analytics, but it is slightly more specific than the source text. If the product does not surface drop-off by step, this sentence overclaims.
- "legacy connectivity is an active area of product investment" paraphrases "ongoing product investment." I avoided inventing specifics such as connector counts or roadmap items.

## Needs Human Review
- Whether the bulleted "Key benefits" block should stay as bullets for the one-pager layout. The skill treats bold inline-header lists as a BOLD-LISTS tell and its fix is prose, so I converted to prose and offered the split-back option in the response. A one-pager designer may prefer plain bullets.
- The closing line ("We built this platform to get that start right") is a mild slogan. It is concrete and professional, but the user may prefer no closer at all since this is only the opening section.
- The retention claim (above) needs a real source or removal before publication.

## Workarounds
- None. The skill's four-pass process mapped cleanly onto this text. I did not run scripts/scan-ai-tells.py (prohibited by the eval rules) and counted density by hand: about 13 distinct watch-list hits in 171 words, roughly 7.6 per 100, spread across INFLATION, AI-VOCAB, ING-ANALYSIS, NO-COPULA, and VAGUE-ATTRIB.

## Suggestions
- The skill says to replace vague attribution with a named source, but does not say what to do when the editor has no source and the claim matters to the piece (common in marketing copy). A one-line rule would help: keep as a direct claim and flag it, cut it, or ask the user. I chose keep-and-flag.
- Promotional adjectives like "seamless" and "intuitive" are not on any watch list, yet they are the puffery INFLATION describes. The Tone awareness section covers this in spirit ("replace vague claims with specific ones") but a short note under INFLATION that the word list is not exhaustive for marketing copy would remove the ambiguity.
- The "Edit with constraints" use case says to include a change summary "on request," while "Full rewrite" says to always include one. This prompt was both (humanize + keep professional). I included the summary; the skill could state that the full-rewrite default wins when both apply.
