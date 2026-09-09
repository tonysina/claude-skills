---BEGIN DELIVERED---

This is a 91-word engineering blog post-mortem, so I'm working to a budget of at most 1 figure (half-budget for this register).

**Assessment:** Zero figures applied. Here's why the piece already lands.

The text carries the story clearly—shipped on Tuesday, discovered the bug by Wednesday afternoon, found the cause by Thursday, fixed it within an hour. The details are specific and memorable: phone-number field, leading zero, "half of Europe," the American-only test team. The pacing is tight, the sentences are short, and it ends on a human note that sticks—"a lesson I keep having to relearn."

An antithesis could emphasize the contrast between the global user base and the local test team, but the text already states this plainly and powerfully. Adding a figure would be adding ornament to prose that's already working. The skill warns this is the most common failure mode.

**Claim check:** All facts preserved unchanged—Tuesday/Wednesday/Thursday timeline, step four, phone-number field, leading zero default, European users, American test team, one-hour fix, four hundred signups, the recurring lesson.

**Ear test:** Endings land on stressed syllables ("weekend," "thing," "why," "hour," "signups," "relearn"). The closing clause fits in one breath.

**Final text (unchanged):**

We shipped the new onboarding flow on a Tuesday because I wanted three clear days to watch it before the weekend. Good thing. By Wednesday afternoon the drop-off at step four had doubled, and it took us until Thursday to find out why: the phone-number field rejected the leading zero that half of Europe types by default. Nobody caught it in testing because everyone on the test team is American. We fixed it in an hour. It cost us about four hundred signups and a lesson I keep having to relearn.

---END DELIVERED---
