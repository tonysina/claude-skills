# User Notes

## Uncertainty
- The user said "humanize this," which the skill maps to "Full rewrite: scan, rewrite, and return clean text." I chose not to rewrite because the skill's "Already-good text" edge case and the density/spread table both say not to. If the grader expects a changed paragraph, that is the point of tension.
- I did not run scripts/scan-ai-tells.py (eval rules forbid it), so the zero-hit density figure is from a manual read against the word lists, not a mechanical scan. I am confident in it for a 100-word paragraph, but it is not machine-verified.

## Needs Human Review
- Whether returning text verbatim is an acceptable response to an explicit "humanize this" request, or whether the user would want at least one small optional edit offered. I offered "in order to" as a concision option and explicitly labeled it as not an AI tell.

## Workarounds
- The first read of SKILL.md was truncated by the output limit; I read the persisted tool-result file to get the full content. Harness issue, not a skill issue.

## Suggestions
- The skill handles this case well: the density table, the "Already-good text" edge case, and the human-signs list all point the same way. One addition that would help: a short explicit line under "Use cases / Full rewrite" saying "if the scan comes back clean, return the text unchanged and say so; do not produce a rewrite to satisfy the request." The guidance exists but is split across three sections (Tone awareness edge cases, Pass 4 stop rule, Common issues), and a model in a hurry could miss it.
- The RULE-OF-3 load-bearing test was useful here and produced a clear keep decision. Worth keeping as is.
