Here's the humanized version.

---

What the November migration taught us

Coordination and planning caused more trouble than the technology did. The cutover touched billing and provisioning and support tooling and reporting. Every one of those teams found something the runbook had missed.

Three things we got wrong:

- Status updates were inconsistent across channels.
- Staging did not match production configuration.
- The documented rollback procedure had never been rehearsed.

The team got it done, but by improvising past the runbook. Fixing those three things is the work before the next cutover.

---

## What changed

The draft scored well past the rewrite threshold: roughly 4 word-list hits per 100 words across 8 distinct patterns.

- `INFLATION` + `ING-ANALYSIS` — "was a pivotal moment in our platform's evolution, underscoring the importance of cross-team coordination and highlighting the value of early planning." Two participle phrases explaining the significance of the thing instead of saying it. Replaced with the actual finding: coordination and planning were the hard part.
- `NEG-PARALLEL` — "It's not just a technical exercise, it's a test of how we work together." The point survives in the opening sentence; the correcting-a-misconception frame is gone.
- `AI-VOCAB` — *pivotal*, *underscoring*, *highlighting*, and *key* ("Key learnings"). The section header is now "Three things we got wrong."
- `BOLD-LISTS` — the bolded inline headers (**Communication:**, **Testing:**, **Rollback:**) are ChatGPT list formatting. The three bullets stay, because each one carries a fact the others don't (`RULE-OF-3` load-bearing test); only the mechanical bold-and-colon scaffolding came off.
- `CHALLENGES-FORMULA` — "Despite these challenges, the team demonstrated remarkable resilience" is the Despite-its-X-faces-challenges template with vague reassurance attached. The team getting it done is still there, with what it actually cost.
- `GENERIC-CLOSER` — "The road ahead is promising as we continue to refine our processes" is on the watch list nearly verbatim. Replaced with what happens next.
- `VAGUE-ATTRIB` — **I deleted "Industry reports indicate that most migrations of this scale encounter similar friction."** There is no source named, and in a retro that sentence reads as pre-emptive cover for the three failures below it. If you have a real report, put it back with the name and year attached; otherwise it's better gone.

## What I deliberately left alone

**"The cutover touched billing and provisioning and support tooling and reporting."** The repeated *and* is polysyndeton across a series, not a run-on joint between propositions. It's doing work here — it makes the blast radius feel like it kept expanding, which is the point of the sentence. The under-punctuation rule covers *and* joining two ideas, never *and* between items in a list, so this stays exactly as written.

Also untouched: the three bullet facts themselves, the sentence-case title, and "Every one of those teams found something the runbook had missed" — the most concrete line in the draft.

One gap worth filling: the original closed on process improvement without naming any. The rewrite points at the three fixes, but if there are owners or dates for them, that's what belongs at the bottom of a retro.
