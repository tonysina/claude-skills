# User Notes

## Uncertainty
- Whether clusters E and F should be recorded as "fired" for a 48-word status update. By the option set they do (gate AI-side + corroborator AI-side). By the skill's own guidance ("zero fired clusters is the most common correct answer for short professional writing", "some AI patterns are the assignment") they are register norms, not findings. I recorded them as fired by the letter and then declined every intervention under Step 5. A different executor could reasonably record 0 fired.
- Cluster F corroborator: I scored "names a specific text/author/work/event" as **no**. "Sprint 14", "Friday" and "the schema change" are the update's subject, not intertextual references. A looser reading could score this "yes" and un-fire F.
- The suggested example line ("DB-412", "Priya") is an illustration only; both names are invented placeholders for facts the author holds. The response labels it as something for the author to fill in, not as an edit.

## Needs Human Review
- Nothing in the delivered text was changed, so there is no rewrite to verify. The reviewer should check whether the "leave it alone" verdict is the intended outcome for this eval case.

## Workarounds
- None. The skill ran end to end without needing deviation.

## Suggestions
- For the "<600 words professional" register, clusters E and F fire by construction on essentially every status update, email or slide copy, because the gate ("never addresses reader", "no intertextual reference") is the register baseline. The Step 3 threshold then reports "some AI-side clustering" for a piece the skill itself expects to be human-range. Either the register table should drop E from status updates (keep it for thought leadership), or Step 3 should note that for this register E and F firing alone does not reach the intervention bar. As written, the executor has to reconcile the threshold table with the "zero is expected" guidance by hand.
- The F fix list ("book, film, person, company, or event") includes "person", which in a status update collapses into "name the reviewer". That is a good edit but it is a specificity edit, not an intertextual one. A one-line note under F saying that in professional registers the honest form of this fix is usually naming the actual person or ticket, and that it always depends on author-held facts, would remove ambiguity.
- The skill does not say what to do when the threshold permits interventions but none survive Step 5. Behaviour here (report each declined intervention with its reason, return text unchanged) followed the "Full audit + rewrite" output format's closing instruction, but an explicit sentence covering the "permitted but none taken" case would help.
