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
allowed-tools: Bash(python*), Bash(pip*), Bash(curl*), Bash(wget*), Bash(mkdir*), Bash(ls*), Read, Write, Edit, WebSearch, WebFetch
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

## Step 3: Split the PDF

```python
from PyPDF2 import PdfReader, PdfWriter
import os

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

    # Copy original PDF into the split directory
    import shutil
    shutil.copy2(input_path, os.path.join(output_dir, os.path.basename(input_path)))

    print(f"Split {total} pages into {-(-total // pages_per_chunk)} chunks in {output_dir}")
```

Install PyPDF2 if needed: `pip install PyPDF2`

Name the split subdirectory after the original PDF filename (without extension) — e.g., `My Paper.pdf` → `My Paper/` — placed alongside the original. After splitting, copy the original PDF into that subdirectory.

---

## Step 4: Read in Batches of 3

Read exactly 3 split files at a time. After each batch:

1. Read the 3 splits using the Read tool
2. Update `notes.md` in the split subdirectory
3. Pause and tell the user:

> "Finished splits [X–Y], notes updated. [N] splits remaining. Continue with the next 3?"

4. Wait for confirmation before reading the next batch

Do not read ahead. The pause-and-confirm protocol is mandatory.

---

## Step 5: Structured Extraction

Read `references/extraction-framework.md` before writing notes. It defines exactly which dimensions to capture, which are conditional on document type, and what good notes look like for each.

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

After all batches are read and `notes.md` is finalized, delete the split PDF chunk files (the `_pp*.pdf` files). Keep the original PDF and the notes file. Use:

```bash
rm "<pdf-name>"/*_pp*.pdf
```

Confirm to the user that cleanup is complete and list what remains in the folder.

---

## When NOT to Split

- Documents under ~15 pages: read directly with the Read tool
- Triage only: read the first split (pages 1–4) for abstract and introduction, then ask whether to continue

---

## Quick Reference

| Step | Action |
|------|--------|
| Acquire | Download or locate local file |
| Detect | Identify document type, state it, invite override |
| Split | 4-page chunks into `<pdf-name>/`; copy original PDF into that folder |
| Read | 3 splits at a time, pause after each batch |
| Extract | Update `<original-filename>.md` using the extraction framework |
| Confirm | Ask user before continuing to next batch |
| Cleanup | Delete all split PDF chunk files after notes are complete |
