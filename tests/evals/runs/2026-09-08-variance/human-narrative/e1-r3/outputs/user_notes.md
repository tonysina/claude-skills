# User Notes

## Uncertainty

- **C1's gate call is genuinely borderline.** The event chain resolves externally (the metrics fell), but the piece's narrative resolution is a stated realization. I scored it "internally" because the closing move is the lesson sentence. Reading it as "externally" would drop the fired count from 4 to 3 — which still leaves the cap at 3, so the executed interventions would be identical either way.
- **The Senge reference is my choice, not the author's.** *The Fifth Discipline* (1990) and the beer distribution game are a real book and a real exercise, and "players who can only see their own segment overcorrect" is the standard characterization of it. But it is still a claim about a source, and I have not verified it against the text in this session. The delivered answer flags `source-check` before publication, per the skill's constraint on cluster F.
- **Whether a case study may cite an outside author at all** is a house-style question I can't answer. Some B2B brand guidelines prohibit it. If Ridgeline's marketing team refuses, F is unavailable and C1 should take its slot.

## Needs Human Review

- **The E intervention assumes an operations-leader reader** ("if you have run a yard at six in the morning"). Correct for a case study distributed to fleet and logistics buyers; wrong for a general marketing page, where the line should simply be cut.
- **Deleting the stated lesson removes the pull quote a sales team may be relying on.** This is the intended effect of cluster A, but it is a commercial decision, not an editorial one. The delivered answer proposes putting the takeaway in Chen's mouth as a quote if it has to return — that would require the customer's sign-off on new quoted words, which I can't obtain.
- **All figures, names, dates and the Chen quote were carried over verbatim.** They should still be checked against the approved customer copy, since case studies are usually customer-approved artifacts and any structural edit can require re-approval.

## Workarounds

- None needed. The skill's process ran end to end without gaps: register triage, gate/corroborator scan, threshold, ordered interventions, guardrail pass.
- Per the eval constraints I did not run `scripts/scan-ai-tells.py` and did not read any other skill directory, so the downstream `humanizer` pass the skill prescribes was not performed. The delivered answer says so explicitly rather than implying the piece is finished.

## Suggestions

- **Step 4's short-form order ("A → B → F → E") omits C1**, even though C1 is in scope for the case study register per Step 1. I inferred its position from the long-form order (C after E). Adding C1 to the tail of the short-form line — "A → B → F → E → C1" — would remove the inference.
- **Cluster A has no explicit rule for titles and subheads.** A subtitle like "From Spreadsheet Chaos to Coordinated Scheduling" states the arc as plainly as the closing lesson does. I treated it as part of A's deletion, but the skill doesn't say whether display copy is in scope for the thematic-statement gate.
- **The interaction I hit is worth naming in the skill.** In this piece one sentence was simultaneously A's thematic statement and C1's internal-understanding resolution, so a single deletion moved two gates. Step 3 warns that structural changes interact; a line noting that a fired cluster can be resolved as a side effect of an earlier intervention — and that this should be reported rather than claimed as a fourth intervention — would help.
