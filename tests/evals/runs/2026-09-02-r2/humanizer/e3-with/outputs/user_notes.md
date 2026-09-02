# User Notes

## Uncertainty
- The prompt says "clean this up" rather than "humanize this." I read it as the skill's "full rewrite" use case combined with a context constraint (company history page, so professional register, no added voice). The skill has no explicit guidance for "clean up" phrasing, but the trigger list includes "clean up AI writing," so this seems the intended reading.
- I judged "the firm" / "it" / "the business" as ordinary referent variation, not `ELEGANT-VAR`. Three ordinary nouns for a company across four sentences is normal English. A stricter reader might flag it; I did not.
- I did not verify any of the facts (2011, Leeds, 38 staff, two presses, 2023 employee trust). The skill only asks that I tell the user they are now unsourced, which I did.

## Needs Human Review
- Whether the user wants the source list restored as real footnotes on the history page. The `[cite: N]` numbers imply a Gemini-side bibliography that was not supplied. I flagged the gap; I could not fill it.
- The observation that `span_2` implies an excerpt from a longer output is an inference from the numbering, not something the reference file states outright. It seems sound (the reference says spans are "numbered upward through the text") but the user should not treat it as certain.

## Workarounds
- None. The skill's residue guidance covered this case directly: strip markers, name the model, say "touched" not "drafted," warn that the figures are now unsourced.

## Suggestions
- The skill could state explicitly that a residue-only case (clean prose plus markup) should return the prose unchanged apart from marker removal. The "full rewrite" use case says "if the scan is clean under the threshold, return the text unchanged," and the residue section says markers are findings at any density, but the two are in different sections and a reader has to combine them.
- The skill's note about `span_N` numbering could mention that a starting number above 1 signals an excerpt. That is a useful thing to tell the user and is currently left to inference.
