---BEGIN DELIVERED---
The alert fired at 02:14; the on-call engineer acknowledged it within four minutes. The initial assumption was a bad deploy—a release had gone out at 23:40 the previous evening—so the rollback was started before anyone checked the dependency graph.

The rollback didn't resolve the errors. By 03:30, the error rate had climbed to 18 percent. A second engineer was paged and found the root cause: both the primary and replica connection pools had been exhausted by a batch job that runs on the first of the month. That job had been added in March and had never coincided with a deploy window before.

At 04:05, the batch job was killed and the error rate returned to baseline within nine minutes. The release was rolled forward again at 06:00 without incident. That afternoon, the connection pool limit was raised from 40 to 120. The following week, a scheduling guard was added to keep the batch job out of deploy windows.
---END DELIVERED---

Notes: Broke up run-on sequences connected by "and" into separate clauses and sentences. Used em-dashes for parenthetical explanation, semicolons for closely related ideas, and periods to separate distinct events. Tightened "did not resolve" to "didn't resolve" for conversational tone. The chronology and causality now read more clearly.
