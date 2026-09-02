Before I touch it: this is a process instruction, and the rhetoric skill's register table says to stop there. Figures are the wrong tool for a runbook. A figure draws the reader's ear to the sentence, and in a failover procedure the reader's attention needs to stay on the lag number and the escalation gate. So the figure budget here is zero, and I stayed inside it.

That is not the same as leaving it alone. The reason nobody reads this section is diction, not a missing flourish. Almost every verb has been turned into a noun ("undertake verification of," "the initiation of any failover activity," "perform a restart of"), so an engineer under pressure has to translate each sentence back into an action before they can act on it. Diction work is free under the skill's rules, and it is the whole fix. Here is the revised section.

---

## Failover procedure

If the primary database instance stops responding, run the replication status query from the operations wiki before you fail over. It gives you the replication lag.

If the lag is under thirty seconds, promote the standby instance. If it is over thirty seconds, escalate to the database team before you promote. Promoting under significant lag causes data loss.

After promotion, update the connection string in the configuration service, then restart the application tier.

---

```
Budget: 120 words, process register → 0 figures
Applied: none. Register is process instruction; the skill's table says stop
  before any figure. The text also sits under 300 words, so even a
  non-process register would have allowed only one.
Free: nominalizations back to verbs throughout ("undertake verification of"
  → "check"/"run"; "the initiation of any failover activity" → "before you
  fail over"; "escalation ... is required" → "escalate"; "perform a restart
  of" → "restart"). Latinate connectors cut ("in the event that," "prior to,"
  "subsequently"). Saxon finishes on every paragraph: "lag," "loss," "tier."
  Word count 120 → 78.
Left alone: no hypophora, even though the second paragraph is shaped like an
  objection-and-answer ("What if the lag is high?"). A question in a runbook
  reads as hesitation at exactly the moment the engineer needs a command.
  No antithesis on the under/over branches; the two branches are already in
  parallel and adding contrast would decorate a decision gate. System names
  kept as written: "configuration service," "application tier," "operations
  wiki." I did not renumber or restructure into steps; that is outside this
  skill's scope.
Claim check: thirty-second threshold preserved in both branches. "Will result
  in data loss" was unhedged in the original and stays unhedged ("causes data
  loss"); "significant" kept. Escalation gate preserved: escalate before
  promoting, not instead of promoting. Attribution to the operations wiki
  kept. Two things to confirm with the author, not changes I made:
  (1) "may proceed" and "can be accomplished" became imperatives. In a
      procedure the condition is the permission, so I read this as the same
      instruction, but if "may" was meant to leave the engineer discretion
      to hold off, say so and I will restore it.
  (2) The original leaves a gap at exactly thirty seconds ("less than" /
      "exceeds"). I preserved the gap with "under" / "over" rather than
      closing it silently. If you want the boundary defined, pick a side.
```

One thing outside this skill, since you said nobody reads it: if the section is meant to be followed under stress, numbered steps with the escalation gate as its own line would help more than any sentence-level change. Happy to do that as a separate pass if you want it.
