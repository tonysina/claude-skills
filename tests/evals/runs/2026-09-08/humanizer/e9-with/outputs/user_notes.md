# User Notes

## Uncertainty

- **No date on the draft.** The skill says to check the age first, since anything before 30 Nov 2022 can be cleared regardless of pattern hits. Nothing in the file or its directory dates it, so the date gate was inconclusive and I scanned anyway. Worth noting that a tired human writing a timeline at 06:00 could produce exactly this run-on style; `UNDER-PUNCT` is a prose-quality finding here as much as an AI-provenance one, and the rewrite is defensible either way.
- **Sentence 10 of the rewrite is exactly 30 words**, right at the pattern's "roughly 30" boundary. I kept it joined because the two remediation items belong together and the length gives the paragraph rhythm variation. Splitting it would be equally valid.
- **"introduced in March"** carries no year in the original. I preserved the ambiguity rather than inferring one.

## Needs Human Review

- **Passive voice was deliberately retained** ("was paged", "was killed", "the limit was raised"). This is standard incident-writeup convention and none of the skill's patterns flag it -- `NO-COPULA`'s subjectless-fragment note covers "No configuration file needed", not passives with explicit subjects. If the team's postmortem template requires named owners for each action, that is a house-style change beyond this skill's scope.
- **Causal claims I made explicit were implicit in the original.** "Because a release had gone out ... the initial assumption was a bad deploy" and "After the batch job was killed ... the error rate returned to baseline" name relationships the draft only implied by juxtaposition. The skill's undecided-connection test directs exactly this, but an incident author should confirm the causality is what they meant -- especially the second one, which is now the sentence that carries the root-cause conclusion.

## Workarounds

- The first `cat` of the input came back compressed and text-mangled, so I re-read the file with the Read tool to get an exact copy before doing any counting. Not a skill problem.
- The scan script was off-limits for this run, so all word-list scanning was done by reading and all rate measures with ad-hoc `wc`/python. The skill states the script does not compute the `UNDER-PUNCT` rates anyway, so nothing was lost on the finding that actually mattered.

## Suggestions

- This case is a good argument for the skill's current wording that `UNDER-PUNCT` sits outside the density/spread table. A reader who applied that table mechanically would score this text 0.0 per 100 words / 0 patterns, land on "within human range -- do not rewrite", and ship an unreadable paragraph. The "What the table does not gate" paragraph is what rescues it, and it might be worth naming `UNDER-PUNCT` explicitly in that paragraph's list of examples (it currently lists `NEG-PARALLEL`, `GENERIC-CLOSER`, the challenges formula, dash clusters and citation markers, but not this one -- its exemption is stated separately, one paragraph earlier).
- The `UNDER-PUNCT` rate signals ("commas per sentence, share of sentences over roughly 30 words, parentheses per 1,000 words") have no stated thresholds -- only a direction. Here the numbers were extreme enough that the call was easy (0.00 commas per sentence, 100% of sentences over 30 words), but a borderline draft would leave the judgment unanchored.
