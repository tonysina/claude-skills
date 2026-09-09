---BEGIN DELIVERED---

## Failover procedure

When the primary database goes down, verify the replication lag before you fail over. Run the replication status query from the operations wiki.

If lag is under thirty seconds, promote the standby. If lag exceeds thirty seconds, call the database team first — that much lag loses data.

After promotion, update the connection string in config and restart the application.

---END DELIVERED---

Notes: Applied heavy diction work (nominalizations to verbs: "undertake verification" → "verify", "prior to initiation" → "before", "escalation required" → "call"; Saxon finishes on "data" and "application"). No figures applied; antithesis already implicit in the condition structure. Preserved all procedural claims.
