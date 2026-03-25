---
name: split-pdf
description: >
  Downloads, splits, and deeply reads PDFs — producing structured notes built
  for implementation briefing and content creation. Use when asked to read,
  review, analyze, or summarize any PDF: academic papers, technical reports,
  analyst reports, whitepapers, or long-form documents. Triggers on "read this
  paper", "summarize this PDF", "analyze this report", "what does this say",
  "extract the key points", or any request to read a document at a URL or file
  path. Splits documents into 4-page chunks and reads in small batches to avoid
  context crashes and shallow comprehension. Do NOT use for documents under
  ~15 pages — read those directly.
compatibility: Requires Bash (python, pip, curl), Read, Write, WebSearch, WebFetch
allowed-tools: Bash(python*), Bash(pip*), Bash(curl*), Bash(wget*), Bash(mkdir*), Bash(ls*), Bash(rm*), Read, Write, Edit, WebSearch, WebFetch
attribution: Based on https://github.com/scunning1975/MixtapeTools/tree/main/skills/split-pdf
metadata:
  version: 1.0.0
---

# Split-PDF: Deep-Read Any Document

**Never read a full PDF directly.** Only read the 4-page split files, and only 3 at a time (~12 pages). Reading a full PDF risks an unrecoverable "prompt too long" crash or produces shallow, hallucinated output. No exceptions.

See `references/why-splitting-works.md` for the reasoning behind this constraint.

---

## Step 1: Acquire the PDF

**Local file path provided:**
- Verify the file exists
- Proceed to Step 2

**URL or search query provided:**
- Use WebSearch to locate the paper if only a title or query is given
- Use WebFetch or `curl`/`wget` to download the PDF to the working directory
- Proceed to Step 2

**If the user provides neither a path nor enough detail to find the paper:**
Ask before proceeding. Do not guess.

**Always preserve the original PDF.** Never delete, move, or overwrite it. Split files are derivatives; the original is permanent.

---

## Step 2: Detect Document Type

After acquiring but before splitting, identify the document type. State it explicitly at the top of the notes file. Accept a user override before continuing.

| Type | Characteristics |
|------|----------------|
| **Academic / technical paper** | Formal methodology, equations, experiments, citations |
| **Analyst report** | Market data, vendor comparisons, recommendations (Gartner, Forrester, etc.) |
| **Whitepaper / technical doc** | Vendor or org-authored, solution-oriented, may include architecture or specs |
| **Strategic / thought leadership** | Conceptual, argumentative, frameworks without formal methodology |

If ambiguous, make a call and say so. The user can correct you.

---

## Step 3: Check Text Density & Choose Reading Mode

Before splitting, run this to detect whether the PDF is text-based or image-heavy:

```python
from PyPDF2 import PdfReader

path = "/path/to/file.pdf"
reader = PdfReader(path)
total = len(reader.pages)
sample = min(8, total)
text = "".join(reader.pages[i].extract_text() or "" for i in range(sample))
chars_per_page = len(text) / sample
print(f"Total pages: {total}, avg chars/page: {chars_per_page:.0f}")
```

**If `chars_per_page >= 500` → text-based PDF:** proceed to Split Mode (Step 4a).

**If `chars_per_page < 500` → image-heavy / scanned PDF:** use Direct Read Mode (Step 4b). Tell the user the PDF appears image-based and you'll read it visually without splitting.

---

### Split Mode (text-based PDFs only)

```python
from PyPDF2 import PdfReader, PdfWriter
import os, shutil

def split_pdf(input_path, output_dir, pages_per_chunk=4):
    os.makedirs(output_dir, exist_ok=True)
    reader = PdfReader(input_path)
    total = len(reader.pages)
    prefix = os.path.splitext(os.path.basename(input_path))[0]

    for start in range(0, total, pages_per_chunk):
        end = min(start + pages_per_chunk, total)
        writer = PdfWriter()
        for i in range(start, end):
            writer.add_page(reader.pages[i])
        out_name = f"{prefix}_pp{start+1}-{end}.pdf"
        with open(os.path.join(output_dir, out_name), "wb") as f:
            writer.write(f)

    shutil.copy2(input_path, os.path.join(output_dir, os.path.basename(input_path)))
    print(f"Split {total} pages into {-(-total // pages_per_chunk)} chunks in {output_dir}")
```

Install PyPDF2 if needed: `pip install PyPDF2`

Name the split subdirectory after the original PDF filename (without extension) — e.g., `My Paper.pdf` → `My Paper/` — placed alongside the original.

---

## Step 4a: Read in Batches of 3 (Split Mode — text PDFs)

Read exactly 3 split files at a time. After each batch:

1. Read the 3 splits using the Read tool
2. Update `<pdf-name>.md` in the split subdirectory (e.g., `My Paper/My Paper.md`)
3. Pause and tell the user:

> "Finished splits [X–Y], notes updated. [N] splits remaining. Continue with the next 3?"

4. Wait for confirmation before reading the next batch

Do not read ahead. The pause-and-confirm protocol is mandatory.

---

## Step 4b: Direct Read Mode (image-heavy / scanned PDFs)

Do **not** split the file. Splitting image-heavy PDFs copies full page images into each chunk, inflating sizes and crashing the Read tool.

Instead, read the original PDF in 12-page batches using the Read tool's built-in `pages` parameter:

- Batch 1: `pages="1-12"`
- Batch 2: `pages="13-24"`
- etc. (max 20 pages per Read call)

After each batch:

1. Read the original PDF with `pages="X-Y"`
2. Update `<pdf-name>.md` alongside the original (no subdirectory needed in this mode)
3. Pause and tell the user:

> "Finished pages [X–Y], notes updated. [N] pages remaining. Continue with the next batch?"

4. Wait for confirmation before reading the next batch

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

Output: a `.md` file named after the original PDF (e.g., `My Paper.pdf` → `My Paper.md`) in the split subdirectory.

Structure the file with the detected document type declared at the top, followed by headers for each applicable dimension. **Update incrementally after each batch** — do not rewrite from scratch. By the final batch, notes should contain specific enough detail that an engineer could act on them, and a content creator could pull hooks and angles directly from the page.

---

## Step 6: Cleanup

**Split Mode only:** After all batches are read and notes are finalized, delete the split chunk files. Keep the original PDF and the notes file.

```bash
rm "<pdf-name>"/*_pp*.pdf
```

**Direct Read Mode:** No cleanup needed — no intermediate files were created.

Confirm to the user that cleanup is complete and list what remains.

---

## When NOT to Split

- Documents under ~15 pages: read directly with the Read tool
- Triage only: read the first split (pages 1–4) for abstract and introduction, then ask whether to continue

---

## Quick Reference

| Step | Text PDF (≥500 chars/page) | Image PDF (<500 chars/page) |
|------|---------------------------|------------------------------|
| Acquire | Download or locate file | Same |
| Detect type | Academic / analyst / whitepaper / strategic | Same |
| Density check | PyPDF2 text extraction → ≥500 → Split Mode | <500 → Direct Read Mode |
| Split | 4-page chunks into `<pdf-name>/` subdirectory | Skip — no splitting |
| Read | 3 split files at a time (Read tool) | Original PDF, `pages="1-12"` etc. |
| Notes file | `<pdf-name>/<pdf-name>.md` | `<pdf-name>.md` alongside original |
| Extract | Update notes using extraction framework | Same |
| Confirm | Pause and ask user after each batch | Same |
| Cleanup | `rm "<pdf-name>"/*_pp*.pdf` | Nothing to clean up |
