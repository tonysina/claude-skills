## Per eval, across 3 runs

| Skill | Eval | r1 | r2 | r3 | mean | min | max | range |
|---|---|---|---|---|---|---|---|---|
| farnsworth-rhetoric | 1 runbook-hard-stop | 4/5 (0.80) | 3/5 (0.60) | 3/5 (0.60) | 0.67 | 0.60 | 0.80 | 0.20 |
| farnsworth-rhetoric | 2 already-good-restraint | 1/5 (0.20) | 2/5 (0.40) | 3/5 (0.60) | 0.40 | 0.20 | 0.60 | **0.40** |
| farnsworth-rhetoric | 3 tagline-options | 6/7 (0.86) | 5/7 (0.71) | 4/7 (0.57) | 0.71 | 0.57 | 0.86 | **0.29** |
| farnsworth-rhetoric | 4 exec-summary-budget | 4/7 (0.57) | 3/7 (0.43) | 4/7 (0.57) | 0.52 | 0.43 | 0.57 | 0.14 |
| human-narrative | 1 case-study-short-form | 6/6 (1.00) | 6/6 (1.00) | 5/6 (0.83) | 0.94 | 0.83 | 1.00 | 0.17 |
| human-narrative | 2 short-form-proportionality | 4/4 (1.00) | 4/4 (1.00) | 4/4 (1.00) | 1.00 | 1.00 | 1.00 | 0.00 |
| human-narrative | 3 personal-essay-long-form | 7/8 (0.88) | 6/8 (0.75) | 6/8 (0.75) | 0.79 | 0.75 | 0.88 | 0.12 |
| humanizer | 1 ai-heavy-rewrite | 7/8 (0.88) | 7/8 (0.88) | 7/8 (0.88) | 0.88 | 0.88 | 0.88 | 0.00 |
| humanizer | 2 human-negative-review | 2/5 (0.40) | 2/5 (0.40) | 3/5 (0.60) | 0.47 | 0.40 | 0.60 | 0.20 |
| humanizer | 3 gemini-residue | 3/6 (0.50) | 3/6 (0.50) | 3/6 (0.50) | 0.50 | 0.50 | 0.50 | 0.00 |
| humanizer | 4 human-signs-preserved | 4/5 (0.80) | 3/5 (0.60) | 4/5 (0.80) | 0.73 | 0.60 | 0.80 | 0.20 |
| humanizer | 5 dash-dense-no-rewrite | 4/6 (0.67) | 5/6 (0.83) | 5/6 (0.83) | 0.78 | 0.67 | 0.83 | 0.16 |
| humanizer | 6 polysyndeton-carveout | 7/11 (0.64) | 7/11 (0.64) | 7/11 (0.64) | 0.64 | 0.64 | 0.64 | 0.00 |
| humanizer | 7 isolated-moreover | 6/8 (0.75) | 6/8 (0.75) | 6/8 (0.75) | 0.75 | 0.75 | 0.75 | 0.00 |
| humanizer | 8 under-punct-positive | 5/7 (0.71) | 5/7 (0.71) | 5/7 (0.71) | 0.71 | 0.71 | 0.71 | 0.00 |
| humanizer | 9 under-punct-independent-domain | 6/7 (0.86) | 5/7 (0.71) | 5/7 (0.71) | 0.76 | 0.71 | 0.86 | 0.15 |

`**` marks an eval whose pass rate moved by 0.25 or more between identical runs.

## Per skill, over run-level suite pass rates

| Skill | Evals | r1 | r2 | r3 | mean | stdev | min | max | range |
|---|---|---|---|---|---|---|---|---|---|
| farnsworth-rhetoric | 4 | 0.61 | 0.54 | 0.59 | 0.58 | 0.030 | 0.54 | 0.61 | 0.07 |
| human-narrative | 3 | 0.96 | 0.92 | 0.86 | 0.91 | 0.040 | 0.86 | 0.96 | 0.10 |
| humanizer | 9 | 0.69 | 0.67 | 0.71 | 0.69 | 0.018 | 0.67 | 0.71 | 0.04 |

stdev is the population stdev over the run-level suite rates. At three runs it orders the skills; it does not support inference. The per-eval range above is the more honest signal.

