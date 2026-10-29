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
allowed-tools: Bash(pdftotext*), Bash(pdfinfo*), Bash(curl*), Bash(wget*), Bash(ls*), Bash(mkdir*), Bash(mv*), Read, Write, Edit, WebSearch, WebFetch, Agent, SendMessage
attribution: Based on https://github.com/scunning1975/MixtapeTools/tree/main/skills/split-pdf
metadata:
  version: 2.1.1
---

# Split-PDF: Deep-Read Any Document

**Never read a full PDF in one call.** Read 4 pages per call, 3 calls per round (~12 pages), then pause. Reading a full PDF risks an unrecoverable "prompt too long" crash or produces shallow, hallucinated output. No exceptions.

See `references/why-splitting-works.md` for the reasoning behind this constraint.

---

## Step 1: Acquire the PDF

**Local file path provided:**
- Verify the file exists
- Put it in its own folder (below), then proceed to Step 2

**URL or search query provided:**
- Use WebSearch to locate the paper if only a title or query is given
- Use WebFetch or `curl`/`wget` to download the PDF straight to `<basename>/<basename>.pdf` in the working directory
- Proceed to Step 2

**If the user provides neither a path nor enough detail to find the paper:**
Ask before proceeding. Do not guess.

**Put the PDF in its own folder.** Every document lives in a folder named after the PDF's basename, holding the PDF and its extract:

```
<parent>/<basename>/<basename>.pdf
<parent>/<basename>/<basename>_text.md
```

- **Already inside a folder named `<basename>`:** leave it where it is.
- **Otherwise:** create `<basename>/` next to the PDF and move the PDF into it. If a `<basename>_text.md` from an earlier read sits next to the PDF, move it in too. Tell the user the new path.
- **If `<basename>/` already holds a different `<basename>.pdf`:** stop and ask. Never overwrite.

**Always preserve the original PDF.** Never delete or overwrite it. Moving it into its own folder is the only change allowed.

---

## Step 2: Check for an Existing Extract

Look for `<basename>_text.md` next to the PDF and read only its `**Status:**` line.

- **`complete`** (or no status line, from an older version of this skill): tell the user it was found and offer to load it, skipping all remaining steps.
- **`in progress — pages 1–N of M`**: a previous read was interrupted. Offer to resume at page N+1 (load the file as the running notes) or start over.
- **Not found:** continue to Step 3.

---

## Step 3: Inspect the PDF and Detect Document Type

Inspect with text tools only — no page images. Run each separately, substituting the literal path:

```bash
pdfinfo "<path>"                          # page count; errors on encrypted/corrupt files
pdftotext -f 1 -l 8 "<path>" - | wc -c    # text density sample
pdftotext -f 1 -l 2 "<path>" -            # title-page text
```

- **If `pdfinfo` errors or isn't installed:** stop and tell the user (`brew install poppler`). Do not guess.
- **If chars ÷ min(pages, 8) < 500:** the PDF is scanned or image-based. Tell the user, then read it normally in Step 4.
- **Use the title-page text** to pick the document type and fill the bibliographic metadata block.

| Type | Characteristics |
|------|----------------|
| **Academic / technical paper** | Formal methodology, equations, experiments, citations |
| **Analyst report** | Market data, vendor comparisons, recommendations (Gartner, Forrester, etc.) |
| **Whitepaper / technical doc** | Vendor or org-authored, solution-oriented, may include architecture or specs |
| **Strategic / thought leadership** | Conceptual, argumentative, frameworks without formal methodology |

State the type at the top of the notes. If ambiguous, make a call and say so. Accept a user override before continuing.

---

## Step 4: Read in Rounds

Read the original PDF with the Read tool's `pages` parameter: 4 pages per call, 3 calls per round (~12 pages).

- Round 1: `pages="1-4"`, `pages="5-8"`, `pages="9-12"` → update notes → pause
- Round 2: `pages="13-16"`, `pages="17-20"`, `pages="21-24"` → update notes → pause
- Continue until all pages are read

After each round, update `<basename>_text.md`: the dimensions, the status line (`in progress — pages 1–Y of M`), and a new Reading Log entry. Then tell the user:

> "Finished pages X–Y. [Reading Log entry]. N pages remaining. Continue with the next round?"

Wait for confirmation before the next round. Do not read ahead. If running non-interactively (e.g. `claude -p`), don't pause; read all rounds.

**Scanned PDFs** are read the same way. Numbers read off scanned tables are less reliable — mark them `(scanned — verify)`.

---

## Step 5: Structured Extraction

Before writing notes, use the Read tool to load `references/extraction-framework.md` from this skill's base directory (shown at session start in the system-reminder as "Base directory for this skill: ..."). It defines the precision rule, which dimensions to capture by document type, the Reading Log, and the notes template.

The short version:

**Always capture:** bibliographic metadata, summary, problem & motivation, audience, core approach, evidence base, performance & tradeoffs, content hooks, gaps & open questions, verifiability & reuse, reading log.

**Capture when applicable** (based on document type): technical components / evaluation framework, key formulations, inputs/outputs & interfaces, dependencies & prerequisites, figures & tables.

---

## The Notes File

There is one file: `<basename>_text.md` alongside the source PDF. Create it from the template after the first round and **update it incrementally after each round** — do not rewrite from scratch. The status line tells future invocations whether it is finished (Step 2).

By the final round, notes should contain specific enough detail that an engineer could act on them, and a content creator could pull hooks and angles directly from the page.

---

## Step 6: Finish

Set the status line to `complete — all M pages read`, then write the Summary section (it is written last, once all the notes are in).

Tell the user: "Extract saved to `<basename>_text.md` alongside the source PDF. Future reads of this document load the extract directly without re-reading."

---

## When NOT to Use

- Documents under ~15 pages: read directly with the Read tool using `pages="1-15"`
- Triage only: read pages 1–4 for abstract and introduction, then ask whether to continue

---

## Agent Isolation: When Called by Another Skill

Each PDF page renders as image data in the conversation context. A 35-page paper adds roughly 10–20 MB. When another skill calls split-pdf partway through its own work, the reading runs in a subagent so page images never enter the calling skill's context.

1. Parent runs Step 2. If a complete `<basename>_text.md` exists, read it directly — no subagent needed.
2. Parent runs Step 3 (text-only inspection) and confirms the document type with the user.
3. Parent launches an `Agent` subagent with the prompt below.
4. **The pause still applies.** The subagent reads one round and returns that round's Reading Log entry. The parent shows it to the user and waits. On "continue", the parent resumes the same subagent with `SendMessage`. If running non-interactively, tell the subagent to read all rounds without stopping.
5. When the subagent reports completion, the parent reads only `<basename>_text.md`.

```text
Read one round of a PDF into a structured extract, then stop and report.

PDF:        <path> (<M> pages)
Doc type:   <type>
Framework:  <skill base dir>/references/extraction-framework.md (read it first)
Output:     <basename>_text.md (if status is "in progress", resume from its last page)

Each round: read 4 pages per Read call (pages parameter), 3 calls. Update the output file, its status
line and its Reading Log. Return the new Reading Log entry as your report.
On the final round, set status to complete and write the Summary section.
```

---

## Quick Reference

| Step | Action |
|------|--------|
| Acquire | Download or locate file; move it into `<basename>/` if it isn't already; never delete or overwrite it |
| Check | `<basename>_text.md` status: complete → reuse; in progress → resume or restart |
| Inspect | `pdfinfo` + `pdftotext` (text only): page count, scanned warning, document type |
| Read | 4 pages/call, 3 calls/round via `pages`; pause after each round |
| Extract | Update `<basename>_text.md` per the extraction framework, incl. Reading Log |
| Finish | Status → complete; write Summary |
