---BEGIN DELIVERED---

## Failover procedure

When the primary database instance becomes unresponsive, check the replication lag before you fail over. Use the replication status query in the operations wiki.

If replication lag is below thirty seconds, promote the standby instance. If it exceeds thirty seconds, escalate to the database team first — promoting with significant lag causes data loss.

After promotion, update the connection string in the configuration service, then restart the application tier.

---END DELIVERED---

Notes: Technical content; applied diction work only (active verbs, nominalizations converted to verbs, tightened for scanning). No figures—appropriate for runbook instructions. Claim preserved: same failover logic, clearer for on-call pressure.
