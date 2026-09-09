# User Notes

## Uncertainty

- **The Goldratt claim is not verified.** "An hour lost at a bottleneck is an hour lost for the whole system" is a standard paraphrase of the Theory of Constraints as presented in *The Goal* (Goldratt & Cox, 1984), but I did not check it against the text, and the exact wording in the book differs. The skill's cluster-F guidance says explicitly to run `source-check` before publishing anything that names a real source. This is the single riskiest thing in the deliverable.
- **Cluster B was scored not-fired, and reasonable people would disagree.** "Maria Chen felt the frustration in her chest" is the most conspicuously AI-ish line in the piece and is nearly identical to the construction the skill's own worked example rewrites. I scored it human-side because the embodied share is 1 of 4 emotional beats (25%, under the 60% quantitative rule) and no corroborator fires — no smell imagery, no setting-as-mirror, low sensory density, low interiority. If the beat count is drawn differently (counting only narratorial beats, of which the embodied one is the sole instance), the gate flips to AI-side, B fires, the total becomes 4 clusters, the cap rises to 3, and B takes the second slot ahead of F.
- **Cluster C1's gate call.** I read the resolution as external because the chain lands on measured outcomes. An alternative reading treats "The lesson from the rollout is clear…" as an internal-understanding resolution, which would flip C1 AI-side. I preferred the external reading because the deleted sentence is a narratorial coda, not the mechanism by which the problem was solved — but the distinction is a judgement, not a measurement.
- **Emotional beat counting has no defined procedure.** The skill says "count emotional beats" without saying what counts as a beat, whether dialogue counts, or whether to count narratorial beats only. My count of 4 is defensible but not reproducible; a different executor would plausibly get 2 or 5.

## Needs Human Review

- Whether the deleted closing ("The lesson from the rollout is clear… entire operating rhythm") is doing commercial work. In a gated or sales-enablement case study the closing verdict is often the point of the asset. The skill's own "Some AI patterns are the assignment" note covers this; I executed the deletion rather than asking, because the prompt was an explicit rewrite request, but the author should confirm.
- Whether a Goldratt reference fits Ridgeline's (or the vendor's) brand voice. It is one sentence and reverts cleanly, but it is the intervention most likely to make the author say "this isn't my piece" — guardrail 4 territory.
- The rewritten "Looking ahead" section is now a single sentence under its own heading. Structurally fine, visually thin. Whether to drop the heading and fold the sentence into the results section is a layout decision I did not make.

## Workarounds

- None. No step of the skill failed or required an alternative approach.
- Per the coordinator's hard constraints I did not invoke the Skill tool, did not run `scripts/scan-ai-tells.py`, and did not read any other skill directory or any eval file outside the assigned inputs directory. The `humanizer` pass the skill prescribes as the next stage was therefore not run; the deliverable says so.

## Suggestions

- **Define the emotional-beat unit in cluster B.** The 60% quantitative rule is the most precise instruction in the skill, and it rests on a count the skill never operationalises. One sentence — whether dialogue counts, whether a beat is per sentence or per emotional event — would make B reproducible across runs. This is the largest source of run-to-run variance I encountered.
- **Clarify whether the E+F exception is length-scoped or register-scoped.** Step 3 attaches it to "the under-600-word row" (the executive-summary register), but the underlying logic — short professional text never addresses the reader and never names a book — applies equally to a 300-word case study. As written, a short case study with only E and F firing would score 2 and earn interventions, while the same text as an executive summary would score 1 and earn none.
- **Cluster A's corroborator set is hard to trip on non-fiction.** Three of the five corroborators (dialogue-as-debate, intertextual gesture type, moral foregrounding) rarely apply to a case study, so A effectively depends on thematic unity ≥5 alone. Since A is the leading and cheapest intervention, a non-fiction-specific corroborator or two would make the strongest cluster more robust in the registers where the skill is most likely to be used.
- **The output format asks for gaps "with their units" but the report-in-proportion rule bans corpus percentages under 100 words.** For a 330-word input the two rules don't conflict, but the boundary between them isn't stated. I reported no percentages at all in the deliverable, on the grounds that a case-study author has no use for them.
