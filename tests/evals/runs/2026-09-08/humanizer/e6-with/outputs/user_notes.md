# User Notes

## Uncertainty

- Density was computed by hand (~4 hits per 100 words) because the eval forbade running `scripts/scan-ai-tells.py`. The exact number depends on whether you count *moment* and *importance* separately from the phrases *pivotal moment* and *underscoring the importance*. It does not matter here — spread alone (8 patterns) and three ungated constructions each independently trigger the rewrite verdict.
- "Coordination and planning caused more trouble than the technology did" is my compression of two things the original asserted separately (the -ing analysis about cross-team coordination and early planning, and the negative parallelism about it being "a test of how we work together"). I believe that is what the author meant, but it is an interpretation, not a transcription.

## Needs Human Review

- **The deleted Industry-reports sentence.** If a real benchmark exists, it should go back in with a name and year. If the author wanted it there as reassurance rather than evidence, they may object to its removal — in which case the skill's rule is to accept the author's judgment, but they should know it reads as excuse-making directly above a list of three preventable failures.
- **The closer.** The original ended on "we continue to refine our processes," which named no process and no owner. I replaced it with a pointer to the three fixes. A real retro closer needs owners and dates, and I could not invent those.
- **"The team got it done, but by improvising past the runbook."** This is a sharper self-assessment than "demonstrated remarkable resilience." It is accurate to the facts in the draft (every team found a runbook gap, rollback was unrehearsed), but whether an internal audience should read that sentence is a judgment about the room, not about AI tells.

## Workarounds

None. The skill's rules resolved every case, including the one that required *not* editing.

## Suggestions

- The polysyndeton carve-out is stated twice (under `UNDER-PUNCT` "Joints, not series" and under `VAGUE-CONNECT` "Do not run this test on a series"), and the redundancy helped — I hit the rule from the `VAGUE-CONNECT` direction first. Worth keeping both.
- `BOLD-LISTS` and `RULE-OF-3` interact in a way the skill does not spell out: the bolded inline-header format was a finding while the three items underneath were load-bearing and had to survive. The `BOLD-LISTS` before/after example collapses its list into a single sentence, which would have been the wrong move here. A one-line note that the fix targets the scaffolding, not necessarily the list, would remove the ambiguity.
