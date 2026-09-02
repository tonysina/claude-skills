Here is the section rewritten so someone can follow it at 3 a.m. without reading a paragraph. The one thing that causes damage (promoting with lag) is now the first line, the decision is a two-branch check with a number attached, and every step is a single imperative sentence.

---

## Failover procedure

**Do not promote the standby until you have checked replication lag. Promoting with 30 seconds or more of lag loses data.**

**Use this when:** the primary database instance is unresponsive.

1. **Check replication lag.** Run the replication status query from the operations wiki.
2. **Read the lag and pick a branch:**
   - **Under 30 seconds:** continue to step 3.
   - **30 seconds or more:** stop. Escalate to the database team and do not promote until they say to. Promoting now will lose data.
3. **Promote the standby instance.**
4. **Update the connection string** in the configuration service to point at the new primary.
5. **Restart the application tier.**

---

What changed and why:

- **The warning leads.** In the original, "will result in data loss" was the last clause of the second paragraph. It is the only sentence in the section that prevents an incident from becoming a worse one, so it is now the first thing on the page, in bold.
- **Numbered steps instead of prose.** "Undertake verification of the replication lag prior to the initiation of any failover activity" became "Check replication lag." Each step is one action, so an engineer can track where they are with a finger.
- **The decision is a visible fork.** The under/over 30 seconds branch was buried across two sentences. Now it is a bullet pair directly under the step that produces the number.
- **Passive and nominalized verbs are gone.** "Promotion may proceed," "perform a restart," "undertake an update" became "promote," "restart," "update."

Two things I did not change but would fix before publishing, since they are why the section still requires trust in the reader:

- **Put the actual query in the runbook.** "Documented in the operations wiki" sends the on-call engineer to a second page during an outage. Paste the query inline, or at minimum link the exact wiki section.
- **Add the promote command and a verification step.** Step 3 says what to do but not how. Add the exact promotion command and a one-line check that confirms the standby is now accepting writes before step 4.

One boundary case I resolved conservatively: the original says "less than thirty seconds" to proceed and "exceeds thirty seconds" to escalate, which leaves exactly 30 undefined. I put 30 in the escalate branch. Change it if the database team intends otherwise.
