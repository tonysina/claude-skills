---BEGIN DELIVERED---
The alert fired at 02:14. The on-call engineer acknowledged it within four minutes. The initial assumption was a bad deploy because a release had gone out at 23:40 the previous evening. The rollback was started before anyone checked the dependency graph.

The rollback did not resolve the errors. By 03:30 the error rate had climbed to 18 percent of requests. A second engineer was paged. She found that the primary and replica connection pools had both been exhausted by a batch job that runs on the first of the month. The batch job had been introduced in March and had never coincided with a deploy window before.

The batch job was killed at 04:05 and the error rate returned to baseline within nine minutes. The release was rolled forward again at 06:00 without incident. The connection pool limit was raised from 40 to 120 that afternoon. A scheduling guard was added the following week to keep the batch job out of deploy windows.
---END DELIVERED---

Notes: Severe under-punctuation with many independent clauses chained only by "and." Restructured into proper sentences while preserving all details and sequence. Timeline and technical facts remain identical; improved readability and clarity of incident flow.
