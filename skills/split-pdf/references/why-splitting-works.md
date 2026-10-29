# Why Splitting Works

Reference for the methodology behind the split-pdf skill.

---

## The Two Problems With Reading Full PDFs

**Problem 1: Session-breaking crashes.** PDFs are not plain text — they encode fonts, vector graphics, images, tables, and multi-column layouts. Rendering a long PDF into tokens is expensive. Combined with conversation context, a 40-page paper can exceed the model's input limit entirely, returning an unrecoverable "prompt too long" error that destroys all session context.

**Problem 2: Shallow, unreliable comprehension.** Even when a full PDF doesn't crash the session, attention degrades over long documents. The model attends more carefully to the beginning and end, skimming the middle. The result: abstracts and introductions read well, methodology and results sections get fuzzy, appendices get missed or hallucinated.

Batched reading addresses both. The first is a hard constraint — the session dies. The second is a soft degradation — the session continues but output is unreliable.

---

## Why Batched Reading Works

Reading ~12 pages per round accomplishes four things:

**Forces focused attention.** With only 12 pages, the model cannot skim. It must engage with specific equations, exact variable definitions, and precise data descriptions.

**Creates natural checkpoints.** After each round, understanding is externalized to a file. Errors caught early don't compound.

**Accumulates rather than summarizes.** One-shot full-paper reads produce lossy compressions. Batched reading with incremental notes produces richer, more specific output.

**Controls front-loading.** Attention is not uniform over a long document. Batching means every section gets to be "the beginning" of some chunk.

---

## Why 4-Page Batches (Text PDFs)

- Small enough that the model attends carefully to every detail
- Large enough that logical sections (a methodology subsection, a results table and its discussion) stay together
- A 40-page paper in 4-page batches = 10 batches = 4 rounds of reading

Scanned PDFs use the same batching. They are harder to read, not easier, so they get no larger batches.

---

## Why pdftotext Replaced PyPDF2

The original skill used PyPDF2 to write physical 4-page chunk files to disk. This version reads page ranges directly, so it needs no Python. `pdftotext` and `pdfinfo` (poppler) are used only to inspect the PDF: page count, text density (to warn about scanned PDFs), and title-page text for document-type detection and bibliographic metadata.

Inspection uses text only, so it puts no page images into context — which is what lets the parent session run it safely before handing reading to a subagent.

---

## Why the Pages Parameter Replaced Physical Splitting

Earlier versions created physical 4-page `.pdf` chunk files on disk using PyPDF2, then read each chunk file separately. This worked but introduced unnecessary complexity: a build directory, chunk files to track and delete, and a Python dependency for file creation.

The Read tool's `pages` parameter reads a specific page range from the original PDF without creating any intermediate files.

Benefits:
- No Python required
- No chunk files created or deleted
- No build directory to manage
- Same batching discipline, cleaner implementation

---

## Why the Pause-and-Confirm Protocol

The human pause between rounds:
- Lets the user review intermediate output and catch errors before they compound
- Allows redirecting: ask follow-up questions, skip sections, change focus
- Controls pacing for sections that warrant extra care

The pause applies even when reading runs in a subagent: the subagent stops after each round, and the parent relays its report and resumes it on confirmation.

---

## Why a Reading Log

Incremental notes show what was learned, not the judgment calls behind it: which document type was chosen, which sections were skipped, which values were read approximately, how an ambiguous claim was interpreted. The Reading Log records those per round. At each pause it is what the user reviews; afterwards it is the audit trail for the finished extract. If it's not documented, it didn't happen.

---

## Why Persistent Extraction (`_text.md`)

The first deep read of a 40-page paper costs 4 rounds of PDF rendering and 10–15 minutes of elapsed time. Without persistence, this work is lost when the session ends.

The skill writes `<basename>_text.md` alongside the source PDF from the first round onward, with a status line. Future invocations check it at Step 2: a complete extract loads directly — no re-reading, no re-rendering, one markdown file read. An in-progress extract means a previous session died mid-read (the failure this skill exists to guard against), so the skill offers to resume at the next unread page instead of starting over.

---

## Why Agent Isolation Matters in Multi-Paper Sessions

Each PDF page rendered in a conversation accumulates as image data in the context. A 35-page paper adds roughly 10–20 MB of rendered page data. After 2–3 papers in the same session, the accumulated image data alone can hit API request size limits — not the context window token limit, but the raw request payload size.

When another skill calls split-pdf as a subroutine, the PDF reading must run in a subagent. The subagent's context holds all the image data; it writes plain-text notes to disk after each round. The parent skill reads only the resulting `.md` file — no image data enters the parent context.

This makes multi-paper sessions reliable regardless of how many papers are processed.

---

## Limitations

- **It is slow.** A 37-page paper requires 4 rounds and 10–15 minutes rather than 1 minute.
- **Notes can become repetitive** if the paper revisits themes. Some manual editing of the final notes may be useful.
- **Best for documents worth reading carefully.** For triage, read only pages 1–4 (usually abstract and introduction).
