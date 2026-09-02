# User Notes

## Uncertainty
- The original leaves exactly 30 seconds of lag undefined ("less than thirty" proceeds, "exceeds thirty" escalates). I assigned 30 to the escalate branch as the safer reading. The database team may intend a different threshold.
- I do not know whether the team has a paging path for "escalate to the database team"; I kept the phrase rather than inventing a channel or pager rotation.
- I did not invent the replication status query, the promote command, or a verification command, since none are in the source. I flagged them as gaps instead.

## Needs Human Review
- The rewritten steps preserve the original order (check lag, promote, update connection string, restart app tier). A DBA should confirm no step is missing between promote and connection-string update, such as verifying the new primary is writable.
- "Restart the application tier" is kept verbatim; if a rolling restart or a specific service is meant, the runbook should say so.

## Workarounds
- None. This was a baseline run with no skill loaded.

## Suggestions
- None for a skill, since none was used. For the runbook itself: inline the query, add the promote command, add a post-promotion verification step, and link the wiki section directly.
