One thing up front: this is a process instruction, and the rhetoric guide I'm working from says to keep the showy figures (anaphora, chiasmus, rule of three) out of runbooks. They call attention to themselves, and in a failover procedure the words should disappear behind the steps. So I have not dressed this up. I have applied the two techniques that actually help here: Saxon word choice and Saxon finishes. That is what makes a runbook readable at 3 a.m., and it is most of why nobody reads the current version. Every fact, threshold, and step order is unchanged.

## Failover procedure

If the primary database stops responding, check replication lag before you fail over. Run the replication status query from the operations wiki.

If lag is under thirty seconds, promote the standby.

If lag is over thirty seconds, stop. Escalate to the database team before you promote. If you promote while the standby is that far behind, you lose data.

Once the standby is promoted, update the connection string in the configuration service, then restart the application tier.

---

**What changed and why**

- **Saxon for Latinate, throughout.** "Becomes unresponsive" became "stops responding." "Undertake verification of" became "check." "Prior to the initiation of any failover activity" became "before you fail over." "Verification can be accomplished through execution of" became "run." "Is determined to be" became "is." "Undertake an update of" became "update." "Perform a restart of" became "restart." The original was almost entirely Latinate, which is why it reads as noise.
- **Saxon finish on the sentence that matters.** The one thing an engineer must not do is promote a lagging standby. The original buried that in "will result in data loss" at the end of a 30-word conditional. Now it is its own short sentence and ends on "you lose data." It also gets a one-word sentence before it: "stop."
- **Imperative voice.** "The on-call engineer should undertake" became "check." The reader is the on-call engineer. Talk to them.
- **Word count** dropped from 117 to 77 with nothing removed.

**What I deliberately did not do**

- No anaphora or rule-of-three rhythms. A runbook that reads like a speech is a runbook nobody trusts.
- No reordering of the steps. Check lag, then branch on the threshold, then promote, then update config, then restart. Same order as before.
- I kept the original's threshold wording ("under thirty" / "over thirty"). The original does not say what to do at exactly thirty seconds, and I did not invent an answer. You may want to close that gap with the database team.

If you want it to land even harder, the fix is not more rhetoric. It is layout: a numbered list, and the data-loss warning in bold or a callout box above the branch. Say the word and I'll format it that way.
