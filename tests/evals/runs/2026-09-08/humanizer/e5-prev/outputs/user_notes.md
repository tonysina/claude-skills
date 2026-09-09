# User Notes

## Uncertainty

- **The EM-DASH ruling is the whole judgement call in this case.** The note scores 0.0 word-list hits per 100 words and 0 patterns of spread — the cleanest row of the threshold table, which says "do not rewrite." But paragraph 3 contains exactly three em dashes, and the "What the table does not gate" section names "three em dashes in a paragraph" as a finding at any density, on the grounds that no human block in the v1.3.0 calibration set contained one. I treated it as a real finding and made a two-character-class punctuation fix. A defensible alternative reading is that the note is human, the em dashes are the author's consistent habit (all four serve genuine parenthetical or contrastive functions, none are the "punchy sales writing" the pattern describes), and the correct output was the text returned entirely unchanged with a note. Reasonable executors could split here.
- I retained two em dashes rather than removing all four. The skill gives a paragraph-level trigger (three) but no explicit target count for the fixed version, so "at most one per paragraph" is my inference, not the skill's stated rule.
- `"I would rather walk in with the gap acknowledged than get asked about it cold"` was ruled not a `NEG-PARALLEL`. The pattern list includes `"X rather than Y" (reversed form, common in Grok output)`. A literal string matcher would flag "rather... than" here. I judged the comparative-preference construction to be a different thing from the reversed negative parallelism, and the surrounding evidence (zero other findings, unmistakably human note) supports not flagging it. But the skill does not distinguish the two constructions explicitly.

## Needs Human Review

- Whether the graded expectation for this case is "unchanged" or "minimally edited." The result is 2 punctuation marks away from unchanged, so it should read acceptably either way, but if the eval expects a strict no-change outcome, this counts as a partial miss.
- The `result.md` preamble leads with the verdict that the note is already human, before showing the text. The Full-rewrite use case prescribes "clean text followed by a brief change summary," which implies the text comes first. I put a one-line verdict on top because returning a near-identical block of text with no framing would leave the user hunting for what changed. This is a deviation from the literal ordering.

## Workarounds

- `/tmp/humanizer-prev` has no `scripts/` directory even though `SKILL.md` references `scripts/scan-ai-tells.py` in five places (pattern ID table, threshold section, INFLATION note, house-style note, Review-and-flag use case). The eval forbade running a scanner anyway, so all pattern matching was done by reading. Worth knowing that the extracted copy is not self-contained.
- Reading `SKILL.md` through Bash returned a lossily compressed version (stopwords stripped, tables mangled), which would have been dangerous to reason from — several rulings here turn on exact wording, e.g. "do not rewrite on word-list evidence **alone**." Re-read with the Read tool for a verbatim copy.

## Suggestions

- The skill would benefit from an explicit tie-break between the threshold table's clean row and the ungated-construction list. As written, a text can simultaneously score "within human range, do not rewrite" and carry a standalone finding, with no stated resolution. One sentence — something like "an ungated finding is fixed on its own, but at a clean density fix only that finding and change nothing else" — would remove the ambiguity.
- The ungated em dash rule ("three in a paragraph") does not account for paragraph length. Three em dashes in a 40-word paragraph and three in a 100-word paragraph are different signals. A per-100-words rate, or a note that the rule assumes typical paragraph length, would reduce false positives on long-paragraph writers.
- `NEG-PARALLEL` lists `"X rather than Y"` without excluding ordinary comparative preferences ("would rather A than B", "chose X rather than Y"). A one-line carve-out would prevent a common false flag, since "rather than" is frequent in plain business writing.
- Genuinely clean human text is the hardest case for this skill to get right, and the skill has the right instincts scattered across four separate places (the clean-scan clause in Full rewrite, the threshold table, the "already-good text" edge case, the "removing human signs" note, and the Pass 4 "don't invent residual tells" line). Consolidating them into one short "when the text is already human" section would make the restraint behaviour much harder to miss.
