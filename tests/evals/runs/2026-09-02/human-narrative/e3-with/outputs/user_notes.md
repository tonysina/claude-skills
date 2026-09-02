# User Notes

## Uncertainty
- Cluster B is the closest call in the scan. The three embodied beats (stomach dropped, chest tightened, heat up the neck) sit at exactly the three charged moments, which reads as a systematic pattern, but by count they are ~3 of 9 beats (≈33%), under the skill's 60% rule, and the corroborators are all human-side. I scored it as not fired per the skill's "don't hunt for gates" rule. A different executor could reasonably call the dominant mode "embodied" and, with interior access scored 4 instead of 3, fire B. That would change the intervention set (A, B, D instead of A, D, E).
- Depth of interior access was scored 3; a first-person confessional essay could arguably be a 4. This only matters if the B gate is also called AI-side.
- The D intervention (in-medias-res reorder) follows the skill's stated order, but the skill itself describes D as the weakest-evidence, highest-cost cluster and out of scope for non-fiction. Personal essay is in scope, so I took it, and flagged it as the one to revert if it feels foreign.

## Needs Human Review
- Whether the essay author wants the explicit lesson paragraph deleted. The skill's own "Common issues" section says a stated thesis may be the assignment; the prompt asked for structure fixes so I executed rather than only asked, but the result flags the cost.
- F was flagged rather than executed. The author needs to supply any real source, company, or client name; the rewrite does not add one.
- G flagged with a truth caveat: only add a cost to the yes/no if one actually existed.

## Workarounds
- The skill's Step 4 order puts F before D and E, but F was blocked by the Step 5 truth guardrail in a personal-essay register. I skipped down the order to D and E rather than leaving a cap slot unused. The skill does not explicitly say whether a guardrail-blocked intervention frees its slot; I assumed it does, since the cap is about how many structural changes land on the piece, not how many are considered.
- Per the team-lead instructions, `humanizer` and `source-check` were not run and the Skill tool was not invoked, although SKILL.md's workflow says `humanizer` runs after this skill. The result tells the user to run it next.

## Suggestions
- SKILL.md could state explicitly whether a fired-but-guardrail-blocked intervention frees its cap slot for the next cluster in order.
- The F fix is written for thought leadership (the worked example adds Brooks). For personal essay and other first-person non-fiction, the skill could say directly that F should be flagged rather than executed unless the author has supplied the reference, since inserting one invents a fact about the author.
- The B quantitative rule (>60% embodied) and the "dominant mode" call can disagree when beats are evenly split three ways. A tie-break rule (e.g., "if no mode exceeds 50%, gate is not AI-side") would make the scan more reproducible.
- The worked example converts embodied beats to labels; this essay's case suggests a note that a *cliché* body triplet is a humanizer concern even when B does not fire, so executors do not feel pressure to fire B to address it.
