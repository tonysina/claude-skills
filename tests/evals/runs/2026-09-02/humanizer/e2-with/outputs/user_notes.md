# User Notes

## Uncertainty
- The input filename (`human-2020-gillingham.txt`) leaks the ground-truth label. I based the verdict on the text alone and did not cite the filename in the response, but a grader should know the executor could see it.
- "world-famous" and "premier" are promotional adjectives but are not literally on the `INFLATION` watch list. The skill says to take the lists literally, so I reported them as puffery, not as counted hits. A stricter reading could count them and raise density to roughly 2.2 per 100, which would flip the table verdict to "rewrite" on word-list evidence alone. I think that would be a false positive on this text, and the skill's own human-signs list (superlatives, definite statements) supports not counting them.
- Spread counting: "boasts" appears on three watch lists (`INFLATION`, `AI-VOCAB`, `NO-COPULA`). I counted it as one hit in one pattern. If one word on three lists counted as spread 3, the table would say "rewrite" for a single word, which cannot be intended. The skill does not say how to handle this case.

## Needs Human Review
- None of the findings require domain expertise. Whether the Black Lion Leisure Centre or Jumpers Rebound Centre is actually "world-famous" is a factual question outside the skill's scope.

## Workarounds
- None. The skill's "Review and flag" use case matched the prompt directly.

## Suggestions
- State how to count a word that sits on more than one watch list (count once, under the first pattern in pass order, for example). This matters for the spread column.
- Consider a short note on grammar errors and run-on sentences as a soft human sign. The extended reference lists "perfect grammar" as an ineffective indicator, but nothing says what to do with visibly imperfect grammar. I used it as supporting evidence, which felt right, but it is not backed by the skill text.
- Load-bearing test for `RULE-OF-3` worked well here; the facility lists passed cleanly. No change needed.
