---
name: split-pdf
description: >
  Downloads and deeply reads PDFs — producing structured notes built for
  implementation briefing and content creation. Use when asked to read,
  review, analyze, or summarize any PDF: academic papers, technical reports,
  analyst reports, whitepapers, or long-form documents. Triggers on "read this
  paper", "summarize this PDF", "analyze this report", "what does this say",
  "extract the key points", or any request to read a document at a URL or file
  path. Reads documents in small page batches to avoid context crashes and
  shallow comprehension. Do NOT use for documents under ~15 pages — read those
  directly.
compatibility: Requires Bash (pdftotext, pdfinfo from poppler), Read, Write, WebSearch, WebFetch
allowed-tools: Bash(pdftotext*), Bash(pdfinfo*), Bash(curl*), Bash(wget*), Bash(mkdir*), Bash(ls*), Read, Write, Edit, WebSearch, WebFetch, Agent
attribution: Based on https://github.com/scunning1975/MixtapeTools/tree/main/skills/split-pdf
metadata:
  version: 2.0.0
---

# Split-PDF: Deep-Read Any Document

**Never read a full PDF in one call.** Read in batches of 4 pages at a time (3 batches per round, ~12 pages). Reading a full PDF risks an unrecoverable "prompt too long" crash or produces shallow, hallucinated output. No exceptions.

See `references/why-splitting-works.md` for the reasoning behind this constraint.

---

## Step 1: Acquire the PDF

**Local file path provided:**
- Verify the file exists
- Proceed to Step 1.5

**URL or search query provided:**
- Use WebSearch to locate the paper if only a title or query is given
- Use WebFetch or `curl`/`wget` to download the PDF to the working directory
- Proceed to Step 1.5

**If the user provides neither a path nor enough detail to find the paper:**
Ask before proceeding. Do not guess.

**Always preserve the original PDF.** Never delete, move, or overwrite it. The original is permanent.

---

## Step 1.5: Check for Cached Extract

Before doing any work, check whether a persistent extract already exists:

```bash
PDF_PATH="/path/to/file.pdf"
BASENAME="${PDF_PATH%.pdf}"
ls "${BASENAME}_text.md" 2>/dev/null && echo "FOUND" || echo "NOT FOUND"
```

**If `<basename>_text.md` exists** alongside the PDF: tell the user it was found and offer to load it directly, skipping all remaining steps. A cached extract means the paper was fully read in a previous session — no re-reading needed.

**If not found:** continue to Step 2.

---

## Step 2: Detect Document Type

After acquiring but before reading, identify the document type. State it explicitly at the top of the notes file. Accept a user override before continuing.

| Type | Characteristics |
|------|----------------|
| **Academic / technical paper** | Formal methodology, equations, experiments, citations |
| **Analyst report** | Market data, vendor comparisons, recommendations (Gartner, Forrester, etc.) |
| **Whitepaper / technical doc** | Vendor or org-authored, solution-oriented, may include architecture or specs |
| **Strategic / thought leadership** | Conceptual, argumentative, frameworks without formal methodology |

If ambiguous, make a call and say so. The user can correct you.

---

## Step 3: Check Text Density

Run this to detect whether the PDF is text-based or image-heavy:

```bash
PDF_PATH="/path/to/file.pdf"
PAGES=$(pdfinfo "$PDF_PATH" 2>/dev/null | awk '/^Pages:/{print $2}')
SAMPLE=$(( PAGES < 8 ? PAGES : 8 ))
CHARS=$(pdftotext -f 1 -l "$SAMPLE" "$PDF_PATH" - 2>/dev/null | wc -c)
CHARS_PER_PAGE=$(( SAMPLE > 0 ? CHARS / SAMPLE : 0 ))
echo "Total pages: $PAGES, avg chars/page: $CHARS_PER_PAGE"
```

**If `chars_per_page >= 500` → text-based PDF:** use 4-page batches (Step 4, text mode).

**If `chars_per_page < 500` → image-heavy / scanned PDF:** tell the user the PDF appears image-based and you will read it visually. Use 12-page batches (Step 4, image mode).

No splitting, no chunk files, no Python required.

---

## Step 4: Read in Batches

Use the Read tool's `pages` parameter to read the original PDF in controlled batches. Do not read the full PDF in one call.

### Text-based PDFs (≥500 chars/page)

Read 4 pages per batch. Process 3 batches per round (~12 pages), then pause.

- Round 1: `pages="1-4"`, `pages="5-8"`, `pages="9-12"` → update notes → pause
- Round 2: `pages="13-16"`, `pages="17-20"`, `pages="21-24"` → update notes → pause
- Continue until all pages are read

After each round, update `<pdf-name>/<pdf-name>.md` and tell the user:

> "Finished pages [X–Y], notes updated. [N] pages remaining. Continue with the next round?"

Wait for confirmation before the next round. Do not read ahead.

### Image-heavy / scanned PDFs (<500 chars/page)

Read 12 pages per batch (one batch per round).

- Batch 1: `pages="1-12"` → update notes → pause
- Batch 2: `pages="13-24"` → update notes → pause
- Continue until all pages are read (max 20 pages per Read call)

After each batch, update `<pdf-name>.md` alongside the original and tell the user:

> "Finished pages [X–Y], notes updated. [N] pages remaining. Continue with the next batch?"

Wait for confirmation before the next batch.

---

## Step 5: Structured Extraction

Before writing notes, use the Read tool to load `references/extraction-framework.md` from this skill's base directory (shown at session start in the system-reminder as "Base directory for this skill: ..."). It defines exactly which dimensions to capture, which are conditional on document type, and what good notes look like for each.

The short version:

**Always capture:**
1. Problem & motivation
2. Core approach
3. Performance & tradeoffs
4. Content hooks
5. Gaps & open questions

**Capture when applicable** (based on detected document type):
6. Technical components / key claims
7. Key formulations (mathematical or algorithmic docs only)
8. Inputs, outputs & interfaces (system or pipeline docs only)
9. Dependencies & prerequisites (technical docs with explicit stack only)

---

## The Notes File

**Working notes** (updated incrementally after each round):
- Text-based PDFs: `<pdf-name>/<pdf-name>.md` in a subdirectory alongside the original
- Image-heavy PDFs: `<pdf-name>.md` alongside the original

Structure the file with the detected document type declared at the top, followed by headers for each applicable dimension. **Update incrementally after each round** — do not rewrite from scratch. By the final round, notes should contain specific enough detail that an engineer could act on them, and a content creator could pull hooks and angles directly from the page.

---

## Step 6: Persist Final Extract

After all rounds are complete and notes are finalized, write the persistent extract:

```bash
# Copy finalized notes to the persistent extract location
cp "<pdf-name>/<pdf-name>.md" "<basename>_text.md"
# or for image-heavy PDFs:
cp "<pdf-name>.md" "<basename>_text.md"
```

The `<basename>_text.md` file lives alongside the source PDF and survives across sessions. Future invocations of this skill will find it at Step 1.5 and skip re-reading entirely.

Tell the user: "Extract saved to `<basename>_text.md` alongside the source PDF. Future reads of this paper load the extract directly without re-reading."

---

## When NOT to Use

- Documents under ~15 pages: read directly with the Read tool using `pages="1-15"`
- Triage only: read pages 1–4 for abstract and introduction, then ask whether to continue

---

## Agent Isolation: When Called by Another Skill

Each PDF page renders as image data in the conversation context. A 35-page paper adds roughly 10–20 MB. In multi-paper sessions, this accumulates and hits API request size limits after 2–3 large papers.

**When another skill calls split-pdf for reading**, isolate the PDF reading in a subagent:

1. Parent skill checks for `<basename>_text.md` — if found, read it directly (no subagent needed)
2. If not found, parent skill launches an `Agent` subagent with:
   - The PDF path
   - The document type (detected beforehand)
   - Instructions to read all batches, write notes to `<pdf-name>.md`, and persist `<basename>_text.md`
3. Subagent reads the PDF pages and writes the extract to disk
4. Parent reads only the `<basename>_text.md` file — no image data in parent context

The parent never reads PDF pages directly. All image rendering stays contained in the subagent's context.

---

## Quick Reference

| Step | Text PDF (≥500 chars/page) | Image PDF (<500 chars/page) |
|------|---------------------------|------------------------------|
| Acquire | Download or locate file | Same |
| Check cache | Look for `<basename>_text.md` — skip all steps if found | Same |
| Detect type | Academic / analyst / whitepaper / strategic | Same |
| Density check | `pdftotext` → ≥500 chars/page | <500 → image mode |
| Split | None — use `pages` parameter | None |
| Read | 4 pages/batch, 3 batches/round via `pages` | 12 pages/batch via `pages` |
| Notes file | `<pdf-name>/<pdf-name>.md` | `<pdf-name>.md` alongside original |
| Extract | Update notes using extraction framework | Same |
| Confirm | Pause and ask user after each round | Pause after each batch |
| Persist | `<basename>_text.md` alongside source PDF | Same |
| Cleanup | Nothing to clean up | Nothing to clean up |
