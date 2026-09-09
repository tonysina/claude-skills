# User Notes

## Uncertainty

- **Register boundary.** A sprint status update reports data, and "data reporting" is a hard-stop row in the Step 1 table. I resolved this in favour of the in-scope row because "status update" is named there explicitly, and because the piece is a narrative-of-work (blocked on X, asked for Y, deadline Z) rather than a metrics dump. A reader who treated it as data reporting would hard-stop instead, and would reach the same practical outcome: no changes.
- **Cluster B gate with zero emotional beats.** The B gate asks for the *dominant* mode of emotional expression. This text has no emotional beats at all. I scored that as not-AI-side rather than as unscorable. The skill does not say what to do when the denominator is zero, and the quantitative rule (">60% run through the body") is undefined on an empty set. Either reading leaves B unfired here, so it did not change the verdict.
- **"If it slips past Wednesday we lose the sprint" as a cluster A candidate.** I read this as a factual consequence, not narratorial thematic commentary. A stricter reader could call it the piece stating what it means. If A fired, the E+F merge rule would lift the count to 3 and unlock up to 2 interventions. I think that reading is wrong, but it is the one judgment call in this audit that would change the outcome.

## Needs Human Review

- Nothing requiring domain expertise. No claims were made about the sprint, the schema change, or the DBA process, and no facts were added or removed.

## Workarounds

- None. The skill was followed as written: register triage, gate-plus-corroborator scan of the four in-scope clusters, the short-form E+F counting rule, the 0–1 threshold row, and the under-100-words report-sizing clause.

## Suggestions

- The prompt asked to "fix anything that reads as AI," and the correct answer was to fix nothing. The skill handles this well (Step 3 says zero interventions is the expected result for short professional writing, and the Common Issues section repeats it), but the Output Format section has no entry for "audit-and-rewrite request that returns zero interventions." It describes "Diagnosis only," "Full audit + rewrite," and "Targeted intervention." A one-line addition saying that a rewrite request with a 0–1 verdict is answered with the verdict and no rewrite would remove the only place I had to infer.
- Step 3's report-sizing rule ("under 100 words, a one-paragraph verdict, no table, no corpus percentages") is easy to miss because it sits at the end of a section about thresholds rather than in Output Format. Cross-referencing it from Output Format would help.
