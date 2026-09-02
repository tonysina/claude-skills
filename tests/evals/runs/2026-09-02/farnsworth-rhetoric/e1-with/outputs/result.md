Before touching the text I checked the register. This is a process instruction, and the register table for this skill says stop: diction work only, no figures. That is not a dodge. A rhetorical figure in a failover runbook would draw the on-call engineer's attention to the sentence at the moment they need it on the database. The reason nobody reads this section is not that it lacks craft. It is that every action has been turned into a noun ("undertake verification of," "initiation of any failover activity," "perform a restart of") and the reader has to translate each one back into a verb before they can act on it. Removing that layer is free, and it is the whole fix.

## Revised text

## Failover procedure

If the primary database instance stops responding, run the replication status query from the operations wiki. Check the replication lag before you take any failover step.

If the lag is under thirty seconds, you are clear to promote the standby. If it is over thirty seconds, escalate to the database team before you promote. You will lose data if you promote with significant lag.

After promotion, update the connection string in the configuration service, then restart the application tier.

## Change note

```
Budget: 120 words, process register → 0 figures
Applied: none. Register table says technical/process text takes diction work only.
Free: nominalizations back to verbs throughout ("undertake verification of" → "check",
  "initiation of any failover activity" → "take any failover step", "escalation ... is
  required prior to promotion" → "escalate ... before you promote", "undertake an update
  of" → "update", "perform a restart of" → "restart"). "In the event that" → "If".
  "Following promotion ... and subsequently" → "After promotion ..., then". Saxon
  finishes on every paragraph: "step", "lag", "tier". 120 words → 82.
Left alone: the ordering, the three-paragraph structure, the thirty-second threshold, and
  the heading. No antithesis on the under/over thirty seconds pair, although the trigger
  is present (both poles real, swap test passes): the two sentences already sit in
  parallel and adding weight to the contrast would make the runbook read like a speech.
  No hypophora ("Why not promote anyway? Because...") for the same reason. The one
  sentence that carries the piece is the data-loss warning, and it now ends on "lag"
  rather than "data loss", which is the only emphasis change I made.
Claim check: threshold preserved (thirty seconds, both directions). "Significant lag"
  kept as written rather than tied to the thirty-second figure, since the original
  leaves that link implicit. "May proceed" kept as permission ("you are clear to"), not
  turned into an instruction. "Will result in data loss" kept as a certainty ("you will
  lose data"). Two things to confirm: (1) the original said the engineer "should"
  verify lag and "must" update the connection string; the imperative flattens both to
  the same weight, which is normal runbook style but is a small strengthening of
  "should". (2) "The on-call engineer" is now the implied "you". If other roles read
  this section, restore the noun in the first sentence.
```

One thing this rewrite does not fix and cannot: the original never says what to do when lag is exactly thirty seconds. That is a gap in the procedure, not the prose, and it belongs to whoever owns the runbook.
