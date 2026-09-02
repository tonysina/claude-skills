# User Notes

## Uncertainty
- Option 2 (isocolon, "Contoso: integrated visualization, collaborative governance.") drops the explicit "strategic alignment" outcome claim entirely. This is an omission, not an inflation, so it passes the claim check as written — but a human reviewer may still prefer it over the recommended hypophora line if brevity matters more than stating the outcome. Flagging the tradeoff rather than deciding it.
- "Contoso" is retained as a bare brand token with no verb attached to it in options 2-4 (it reads as a label, not a subject). This is a normal tagline convention but worth a human sanity-check against the brand's existing tagline style guide, which wasn't provided.

## Needs Human Review
- Confirm "strategic alignment" is still the term Contoso wants to lead with; this eval treated it as fixed (per the claim check, options may compress the source's claims but not replace them), but a marketer may want a different outcome word entirely — that would be a content decision upstream of this skill, not a rhetoric one.

## Workarounds
- The skill's "Single line" instructions say to chain the `beyond-obvious` skill for divergent options before choosing. Per this task's explicit constraint, the Skill tool was not invoked; instead the divergence step (drafting across multiple distinct figures before narrowing) was performed directly in this session. The output shape and rigor should be equivalent, but it was not literally routed through beyond-obvious.
- `scripts/scan-ai-tells.py` was not run, per this task's explicit constraint, even though sibling arms in this eval batch appear to include a `scan.txt` output. No scan artifact was produced for this run.

## Suggestions
- None beyond what's in the transcript. The skill's claim-check-then-withdraw instruction for the "Single line" use case worked exactly as specified: two of six generated candidates (antithesis, erotema) were cut here because their most natural phrasing smuggled in an unsupported claim about competitors or the status quo, and the skill's own guardrail caught both before they reached the output.
