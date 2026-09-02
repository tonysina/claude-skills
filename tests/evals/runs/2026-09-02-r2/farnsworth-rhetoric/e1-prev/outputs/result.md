This is a runbook, so I'm going to push back on the ask a little before doing it.

A failover procedure is process text. The register table in this skill stops at process text: no rhetorical figures, diction work only. That's the right call here anyway. Nobody reads this section because the prose makes them decode it under pressure ("undertake verification of the replication lag prior to the initiation of any failover activity"), not because it lacks a memorable line. A figure would add one more thing to parse at 3 a.m. What it needs is to say each step in plain verbs so the engineer can act on it in one read.

Here is the diction-only revision. Every claim, threshold, and sequence is unchanged.

---

## Failover procedure

If the primary database instance stops responding, check the replication lag before you fail over. Run the replication status query from the operations wiki.

If the lag is under thirty seconds, promote the standby instance. If the lag is over thirty seconds, escalate to the database team before you promote. Promoting with significant lag will lose data.

After promotion, update the connection string in the configuration service, then restart the application tier.

---

```
Budget: 131 words, process register → 0 figures (register table: technical/process = diction only)
Applied: none
Free: nominalizations back to verbs throughout ("undertake verification of" → "check";
  "the initiation of any failover activity" → "fail over"; "can be accomplished through
  execution of" → "run"; "promotion ... may proceed" → "promote"; "escalation ... is
  required" → "escalate"; "will result in data loss" → "will lose data"; "undertake an
  update of" → "update"; "subsequently perform a restart of" → "restart"). "In the event
  that" → "If". "Following promotion" → "After promotion". "Prior to" → "before".
  Paragraph endings: "lose data" and "application tier" land on a stress; "operations
  wiki" stays because it is the pointer the reader needs, and reordering for the ear
  would bury it.
Left alone: no antithesis on the under/over thirty-second split, though the two poles
  are real and it would survive the swap test. The register forbids it, and the two
  plain conditionals already do the job. No hypophora ("Why check lag first? Because
  promoting with lag loses data") for the same reason. No isocolon on the three
  post-promotion actions; they are a sequence, not equals. Kept the three-paragraph
  structure: restructuring is out of scope for this skill.
Claim check: thresholds intact (under thirty / over thirty). "Significant lag" kept
  rather than sharpened to a number, because the original defines it only by implication.
  Sequence intact (check lag → promote or escalate → update connection string → restart).
  "Will result in data loss" stays a hard "will". Two modality shifts to confirm:
  "should undertake verification" and "promotion may proceed" became imperatives
  ("check", "promote"), which is normal runbook mode but slightly firmer than the
  original's "should" and "may". The original also leaves exactly thirty seconds
  undefined (less than / exceeds); I preserved that gap rather than closing it, but
  the author should pick a side.
```

Two things outside this skill that would do more for "nobody reads it" than any figure:

- Number the steps. Five actions in three paragraphs is the real reason it gets skimmed. A numbered list with the lag check as step 1 and the escalation branch as step 2 is what an on-call engineer scans for.
- Put the data-loss warning where the eye lands first, as a callout above the steps, since it is the one thing they must not get wrong.

Both are structure changes, not sentence craft, so I left them for you to decide.
