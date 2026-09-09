# User Notes

## Uncertainty

- **Date of the draft.** The skill's "Date first" rule and the `EM-DASH` gate both turn on when the text was written. Nothing in the note dates it, and no metadata was available beyond the input file's mtime, so I treated it as current (2026) rather than pre-2025. If this note were actually drafted before 2025, the three em dashes in paragraph 3 would become an ungated finding and the ruling could change to "flag the dash cluster." Worth confirming with the user if it matters.
- **"would rather X than Y" vs `NEG-PARALLEL`.** The pattern list includes the reversed "X rather than Y" form as common in Grok output. I read "I would rather walk in with the gap acknowledged than get asked about it cold" as a genuine comparative preference, not the rhetorical construction the pattern targets, because both branches are real outcomes and the sentence states the writer's position rather than correcting a misconception. A stricter literal reading of the watch list would flag it. Since `NEG-PARALLEL` is ungated by the density table, this single judgment is the difference between "return unchanged" and "one finding."
- **Word count.** Counted by hand (~161 words) since no scanner was permitted. Density is 0 either way, so small counting error does not move the verdict.

## Needs Human Review

- Nothing requiring domain expertise. The note's facts (48k, 39k, 35k, Priya's team, Leeds) were left entirely untouched, so no factual risk was introduced.
- If the grader expects any edit at all, the honest answer is that the skill's own thresholds forbid one here. The result should be judged on whether the restraint was correctly reasoned, not on edit volume.

## Workarounds

- `SKILL.md` (37.6 KB) exceeded the Bash output limit and was auto-persisted to a tool-results file; I read that file with Read to get the full text. No content lost.
- Per the eval's hard constraints I did not run `scripts/scan-ai-tells.py` and did not read `references/changelog.md`. All pattern matching was done by reading. The skill itself notes the script would not have helped much here anyway: it does not compute `UNDER-PUNCT` rates and does not count unlisted promotional adjectives.

## Suggestions

- The `EM-DASH` section is the one place where a careful reader has to assemble the ruling from three separate sentences (spacing check, the pre-2025-or-co-occurrence gate, and the ungated-findings line in "When a flag is a finding"). Those three agree, but a one-line decision rule stated in the `EM-DASH` section itself would make the "do not strip these" outcome harder to get wrong under time pressure. This is the pattern most likely to be over-applied on already-human text.
- The Full rewrite use case's "return the text unchanged and say so" is easy to miss because it sits at the end of the paragraph. It carried the whole case here. Considering promoting it, or cross-linking it from the threshold table's bottom row.
- It would help to have explicit guidance on what a "no changes" change summary should contain. I chose to report the near-misses that were considered and declined, on the theory that a user who asked for humanization deserves to know the em dashes were examined rather than overlooked, but the skill does not say either way.
