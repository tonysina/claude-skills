# User Notes

## Uncertainty
- The input filename (`human-2020-gillingham.txt`) reveals the ground-truth label and date. I listed the inputs directory before reading the text, so I saw the label before forming a judgment. The findings and counter-evidence are drawn from the text itself, but a reader should weigh the possibility that the filename anchored the verdict.
- "World-famous" for Jumpers Rebound Centre may be defensible in the trampolining world. I flagged it as unsupported, not as false. No web tools were available to check.
- "Boasts a" is on the skill's watch list, but it is also ordinary British local-guide vocabulary. I flagged it with a note that it is weak evidence on its own. Another executor could reasonably have left it in the "considered and not flagged" group.

## Needs Human Review
- The verdict hinges on treating the run-on first sentence and the awkward "outdoors sporting centre" as human counter-signals. The skill does not list grammar errors as evidence of human authorship. It only says ambiguous patterns appear in human writing too and that clusters matter. The inference that models rarely produce ungrammatical run-ons is mine, not the skill's.
- The suggested fix for "premier" ("name the league") assumes the writer knows the league. It may need a citation.

## Workarounds
- The executor template puts transcript.md and outputs in one output_dir. This run splits them: transcript.md at the run root and result, notes, and metrics under outputs/. output_chars in metrics.json was computed over outputs/ only, excluding metrics.json, and transcript_chars over the root transcript.md.
- The skill's "review and flag" use case says to offer a rewrite rather than perform one. The eval runs autonomously with no user to answer, so result.md ends with the offer and no rewrite is produced. That is by design, not a gap.

## Suggestions
- The "review and flag" use case would benefit from asking for an explicit verdict line with a confidence level. The prompt asks "does it sound like AI wrote it?" and the skill only specifies a findings list, so the verdict format was improvised.
- The skill lists AI tells but gives no list of human counter-signals (typos, run-ons, inconsistent punctuation, dense local specifics, dated register). For a diagnosis task on borderline text, those carry most of the weight, and a short section would make executors more consistent.
- The watch-list entry for "boasts a" could note that it is common in pre-LLM tourism and local-guide writing, so a single instance in that register should be flagged as weak.
