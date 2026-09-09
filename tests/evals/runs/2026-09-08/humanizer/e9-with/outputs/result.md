Here it is.

---

The alert fired at 02:14, and the on-call engineer acknowledged it within four minutes. Because a release had gone out at 23:40 the previous evening, the initial assumption was a bad deploy. The rollback started before anyone checked the dependency graph.

The rollback did not resolve the errors. By 03:30 the error rate had climbed to 18 percent of requests, and a second engineer was paged. She found that the primary and replica connection pools had both been exhausted by a batch job that runs on the first of the month. That job had been introduced in March, but it had never coincided with a deploy window before.

After the batch job was killed at 04:05, the error rate returned to baseline within nine minutes. The release was rolled forward again at 06:00 without incident. That afternoon the connection pool limit was raised from 40 to 120, and a scheduling guard was added the following week to keep the batch job out of deploy windows.

---

## What changed

**`UNDER-PUNCT` (punctuation scarcity) -- the whole finding.** The draft was 172 words in three sentences: one sentence per paragraph, averaging 57 words each, with zero commas, zero semicolons and zero parentheses in the entire piece. All three sentences ran past 30 words. Thirteen instances of "and" carried the text, twelve of them as joints between two propositions rather than as items in a series. That is the profile the pattern describes: long sentences with no internal breaks, "and" doing the work that named relationships should be doing.

The rewrite runs 165 words in ten sentences (16.5 words each on average, none over 30) with six commas, 0.6 per sentence. Sentence lengths now vary from 7 to 30 words instead of sitting at 44, 69 and 59.

**Named the relationships the "and"s were hiding.** Per the pattern's joints test, I cut each connector and checked whether a real relationship survived. Most did, so I restored it and named it rather than leaving the neutral "and":

- "a release had gone out at 23:40 ... and the rollback was started" -> **Because** a release had gone out. The premature rollback followed from the assumption; the draft left that inference to the reader.
- "that job had been introduced in March and had never coincided" -> introduced in March, **but** it had never coincided. This is the concession that explains why nobody had seen it before.
- "The batch job was killed at 04:05 and the error rate returned to baseline" -> **After** the batch job was killed. This is the causal link that proves the diagnosis, and "and" was flattening it into coincidence.

Three "and"s survive, where the relation genuinely is simple addition or sequence ("fired at 02:14, and the on-call engineer acknowledged it"), plus one in the series "primary and replica", which the pattern explicitly exempts.

## What I checked and left alone

- **Word lists (Passes 1 and 2).** Zero hits across all watch lists -- no `INFLATION`, `AI-VOCAB`, `ING-ANALYSIS`, `VAGUE-ATTRIB`, `NO-COPULA`, `NEG-PARALLEL`, `RULE-OF-3` or `FALSE-RANGE`. Density 0.0 per 100 words, spread 0 patterns, which is inside the human range in the threshold table. `UNDER-PUNCT` is scored by rate, not by word-list hits, and doesn't feed that table -- it's assessed on its own, and on its own it fires.
- **"raised from 40 to 120"** is not a `FALSE-RANGE`. Those endpoints sit on a real numeric scale with a coherent middle.
- **No em dashes** in either version. Dash scarcity isn't evidence of anything by itself, so I didn't read into it and didn't add any.
- **`VAGUE-ATTRIB`**, which the punctuation pattern says to check when it fires, because unpunctuated and unsourced prose often share an origin. Clean here: every claim is a timestamped observation, and the sourcing is the incident log rather than an unnamed authority.
- **The passive voice** ("was paged", "was killed", "the limit was raised"). It's the standing convention for incident writeups, where what happened matters more than who did it, and the actors are already named where it counts ("a second engineer was paged. She found..."). Stripping it would be a style preference, not an AI fix.
- **Register.** Technical writeup, so I removed the run-ons without adding voice, opinion or first person. Every time, percentage, date and remediation detail is unchanged.
