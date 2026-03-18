# Why Splitting Works

Reference for the methodology behind the split-pdf skill.

---

## The Two Problems With Reading Full PDFs

**Problem 1: Session-breaking crashes.** PDFs are not plain text — they encode fonts, vector graphics, images, tables, and multi-column layouts. Rendering a long PDF into tokens is expensive. Combined with conversation context, a 40-page paper can exceed the model's input limit entirely, returning an unrecoverable "prompt too long" error that destroys all session context.

**Problem 2: Shallow, unreliable comprehension.** Even when a full PDF doesn't crash the session, attention degrades over long documents. The model attends more carefully to the beginning and end, skimming the middle. The result: abstracts and introductions read well, methodology and results sections get fuzzy, appendices get missed or hallucinated.

Splitting addresses both. The first is a hard constraint — the session dies. The second is a soft degradation — the session continues but output is unreliable.

---

## Why Batched Reading Works

Reading 3 splits at a time (~12 pages) accomplishes four things:

**Forces focused attention.** With only 12 pages, the model cannot skim. It must engage with specific equations, exact variable definitions, and precise data descriptions.

**Creates natural checkpoints.** After each batch, understanding is externalized to a file. Errors caught early don't compound.

**Accumulates rather than summarizes.** One-shot full-paper reads produce lossy compressions. Batched reading with incremental notes produces richer, more specific output.

**Controls front-loading.** Attention is not uniform over a long document. Splitting means every section gets to be "the beginning" of some chunk.

---

## Why 4-Page Chunks

- Small enough that the model attends carefully to every detail
- Large enough that logical sections (a methodology subsection, a results table and its discussion) stay together
- A 40-page paper becomes 10 chunks = 4 rounds of reading

---

## Why the Pause-and-Confirm Protocol

The human pause between batches:
- Lets the user review intermediate output and catch errors before they compound
- Allows redirecting: ask follow-up questions, skip sections, change focus
- Controls pacing for sections that warrant extra care

---

## Limitations

- **It is slow.** A 37-page paper split into 10 chunks, read 3 at a time, requires 4 rounds and 10–15 minutes rather than 1 minute.
- **Notes can become repetitive** if the paper revisits themes. Some manual editing of the final notes may be useful.
- **Best for documents worth reading carefully.** For triage, read only the first split (pages 1–4, usually abstract and introduction).
