**Short answer: no, this does not read like AI wrote it.** It reads like a human-written local-interest passage, probably from an older gazetteer or Wikipedia-style article about Gillingham. Across all four passes I found one word-list hit and no structural, formatting, or markup tells, and the text carries several signs the source page lists as markers of *human* writing.

## Scoring

| Measure | Value | Threshold |
|---|---|---|
| Words | 135 | |
| Watch-list hits (Passes 1-2) | 1 | |
| Density | 0.7 per 100 words | Human range is under 1 per 100 |
| Spread | 1 pattern | Human range is 0-1 patterns |

Verdict from the table: within human range. Nothing here justifies a rewrite on AI grounds.

## Findings (ordered by signal strength)

**1. `INFLATION` / `AI-VOCAB` / `NO-COPULA` -- "boasts a"**

> "The area **boasts a** sub-regional sports centre..."

"Boasts" meaning "has" sits on all three watch lists, so it is the one literal flag. On its own it is weak evidence: it is a stock phrase in British local writing and tourism copy going back decades, and there is nothing else from those lists nearby to cluster with. If you want to neutralise it anyway: "The area has a sub-regional sports centre..." or "Medway Park (formerly the Black Lion Leisure Centre) is a sub-regional sports centre with...".

That is the only finding.

## What I checked and did not flag

- **"world-famous facility" and "Kent's premier Ice Hockey Club."** These are puffery, and a Wikipedia editor would trim them as peacock terms regardless of who wrote them. But they are unsourced superlatives, which the source page lists as *more* common in human writing than in AI output. LLMs tend to inflate with abstractions ("a pivotal moment", "underscores its importance"), not with blunt local pride like "world-famous."
- **The first sentence is a run-on with missing punctuation.** "...gym, sports hall and squash courts also in the same area is Jumpers Rebound Centre for trampolining a world-famous facility for the sport." Two clauses have been jammed together with no comma or full stop. That is an error current LLMs almost never make, and it points to a human author writing quickly.
- **"There is an outdoors sporting centre..."** "There is a" openers are on the source's list of human-writing signs, and LLMs tend to edit them out. Its presence counts against AI authorship.
- **Concrete specifics throughout.** Named venues, a renaming (Black Lion Leisure Centre to Medway Park), the River Medway, a narrow-gauge railway, the Invicta Dynamos and their former name, and a dated opening (1984). AI text about a place usually goes the other way: fewer proper nouns, more generic "vibrant community" filler.
- **Structure.** No em dashes, no bold or inline-header lists, no triads (the four-item facilities list is load-bearing: each item is a different thing you can do there), no "it's not just X, it's Y", no signposting, no generic upbeat closer. The last sentence ends on a fact, not a mood.
- **Register.** Consistent British English ("centre", "Her Majesty the Queen"), "SCUBA" in capitals, and slightly awkward phrasings like "outdoors sporting centre." No style seam between paragraphs, so no `STYLE-SHIFT`.
- **Markup residue.** None. No citation placeholders, no stray Markdown, no curly-quote mixing.

## Recommendation

Leave it as it is from an AI-detection standpoint. If you want it tightened for other reasons, the useful edits are ordinary copyediting, not de-AI-ing: fix the run-on in the first sentence, and decide whether "world-famous" and "premier" can be supported or should go. I can do that pass if you want it, but I have not rewritten anything, since you asked for a diagnosis.
