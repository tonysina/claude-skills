# Extraction Framework

This file defines what to capture during deep reading, how it adapts by document type, and what good notes look like for each dimension.

---

## Precision Rule (applies to every section)

Record specifics, not paraphrase: exact numbers with units, sample sizes, named entities, verbatim definitions.

Tag every claim with its location: `(p. 14)`, or `(Table 3, p. 20)` / `(Fig. 2, p. 9)`.

If a value was hard to read, say so rather than smoothing it over. This is a structured extraction, not a summary.

---

## Document Type Mapping

The dimensions you capture and how you frame them depend on the detected document type. Use this table as your guide:

| Dimension | Academic / Technical | Analyst Report | Whitepaper / Tech Doc | Strategic / Thought Leadership |
|-----------|---------------------|----------------|-----------------------|-------------------------------|
| Bibliographic metadata | ✅ | ✅ | ✅ | ✅ |
| Summary | ✅ | ✅ | ✅ | ✅ |
| Problem & motivation | ✅ | ✅ | ✅ | ✅ |
| Audience | ✅ | ✅ | ✅ | ✅ |
| Core approach | ✅ | ✅ | ✅ | ✅ |
| Evidence base | ✅ | ✅ | ✅ | ✅ |
| Technical components / evaluation framework | ✅ Architecture + modules | ✅ Criteria + vendor placements | ✅ System components | ✅ Framework elements |
| Key formulations | ✅ If mathematical | ❌ | ✅ If algorithmic | ❌ |
| Inputs, outputs & interfaces | ✅ If system described | ❌ | ✅ | ❌ |
| Dependencies & prerequisites | ✅ If stack specified | ❌ | ✅ If stack specified | ❌ |
| Performance & tradeoffs | ✅ Results + benchmarks | ✅ Market data + ratings | ✅ Claimed benefits + limits | ✅ Argument strength + counterpoints |
| Figures & tables | ✅ If present | ✅ If present | ✅ If present | ✅ If present |
| Content hooks | ✅ | ✅ | ✅ | ✅ |
| Gaps & open questions | ✅ | ✅ | ✅ | ✅ |
| Verifiability & reuse | ✅ | ✅ | ✅ | ✅ |
| Reading log | ✅ | ✅ | ✅ | ✅ |

---

## Dimension Definitions

### Bibliographic Metadata
**Always capture.** Fill from the title-page text in Step 3.

Authors, verbatim title, year, publisher or venue, DOI or URL. Record `null` for any field not shown in the document. Do not guess.

---

### Summary
**Always capture. Write last**, after the final round.

At most ~200 words, plain English, no jargon. What the document is about, why it matters, what it argues or finds, and the main take-away.

---

### Problem & Motivation
**Always capture.**

What specific problem does this document address? Why does the existing approach fail or fall short? Who is affected and why it matters to them.

Write this as a brief statement an intelligent non-expert could understand. This is the "why we need this" — the context that makes everything else meaningful.

**Good:** "Existing LLM context management discards information via summarization, which degrades downstream task performance. This paper addresses how to compress context without information loss."

**Weak:** "The paper is about KV cache compression."

---

### Audience
**Always capture.**

Who is this written for (roles, industries, communities), and who else would care? For content: which audience would a post built on this land with?

---

### Core Approach
**Always capture.**

The proposed method or argument in plain terms — before any math, before any technical detail. The conceptual model. If someone asked you to explain the idea in two minutes, what would you say?

For technical papers: what is the intuition behind the method?
For analyst reports: what is the central recommendation or thesis?
For strategic docs: what is the core argument or framework?

---

### Evidence Base
**Always capture.**

What do the claims rest on, and where did it come from? Data, surveys, benchmarks, case studies, interviews, or expert opinion — with sample size, respondent profile, time period, and who produced or funded the work.

- **Academic:** Datasets, where obtained, unit of observation, sample, period.
- **Analyst:** Survey n and respondent profile, research dates, vendor briefings vs. customer references.
- **Whitepaper:** Vendor-authored? Named customers or anonymous? Independent validation?
- **Strategic:** Data-backed, anecdotal, or assertion?

If the document doesn't say, record that — the absence is a finding.

---

### Technical Components / Evaluation Framework
**Conditional. Capture for every type, framed as below.**

The named building blocks of the approach and how they connect.

- **Academic / technical:** Specific modules, algorithms, sub-methods, and their relationships. Name them as the authors name them.
- **Analyst:** Evaluation criteria and weightings, inclusion criteria, and each named vendor's placement or score.
- **Whitepaper:** System components, integration points, named features.
- **Strategic:** The elements of the framework or model — what the author distinguishes, what the named parts are, how they relate.

Include a brief description of each component's role. A diagram description if one exists in the document.

---

### Key Formulations
**Conditional. Capture only if the document contains mathematical notation, formal algorithms, or decision rules that define the approach.**

The equations or algorithms an implementer would need to reference — not every formula in the paper, only the ones that define the core method.

For each:
- State what it computes or defines
- Note where in the paper it appears (section, equation number, page)
- Flag any non-obvious notation

If the document has no meaningful formulations, skip this section entirely.

---

### Inputs, Outputs & Interfaces
**Conditional. Capture only if the document describes a system, API, pipeline, or process with defined stages.**

At each stage: what goes in, what comes out, and in what form?

Format, shape, type, or schema where specified. This is the information someone would need to integrate the approach with other systems or implement it end to end.

---

### Dependencies & Prerequisites
**Conditional. Capture only if the document explicitly specifies a technical stack, tooling, model, hardware, or environment assumption.**

What does this build on? What must already exist for the approach to work?

- Frameworks or libraries named
- Model or hardware requirements stated
- Dataset or data format assumptions
- Anything the authors take for granted that a builder would need to source

If the document makes no explicit statements about prerequisites, skip this section.

---

### Performance & Tradeoffs
**Always capture. Frame by document type.**

What did they measure or claim, and against what baseline? What did they gain, and what did they give up?

- **Academic:** Specific benchmark results, comparisons to prior methods, stated limitations.
- **Analyst:** Market ratings, vendor comparisons, adoption data, caveats.
- **Whitepaper:** Claimed benefits, any stated limitations or prerequisites.
- **Strategic:** How well does the argument hold up? What is conceded or left unaddressed?

Capture numbers where they exist. "Performs better" is not useful. "Reduces KV cache size by 90% with less than 2% performance degradation on MMLU" is.

---

### Figures & Tables
**Conditional. Capture when the document has them.**

For each one that matters: label, page, caption, what it shows, and one line on why it matters. In analyst reports these are often the most reusable asset.

---

### Content Hooks
**Always capture.**

Three types. Pull directly from the document — these should be grounded in what the authors actually say, not inferred:

**Counterintuitive or surprising:** A finding, claim, or result that goes against what a reader would expect. Flag these explicitly — they are the best leads for posts and talks.

**Strong claim to engage with:** A statement the authors make with confidence that you could meaningfully agree with, push back on, or extend. Quote or closely paraphrase.

**Analogy or metaphor from the document:** If the authors use a comparison, image, or framing device to explain their idea, capture it verbatim or near-verbatim. These are often the most memorable and reusable elements.

If a type is genuinely absent from the document, note that rather than inventing one.

---

### Gaps & Open Questions
**Always capture.**

What did the paper not address, gloss over, or defer to future work? What would a practitioner need to figure out themselves? What assumptions does the approach rely on that are not validated?

This dimension serves both builders (what's missing from a spec) and content creators (what's worth arguing about or exploring further).

---

### Verifiability & Reuse
**Always capture.**

What could be checked independently? Note any methodology appendix, public dataset, code repository, or source links. Note what is reusable (charts, frameworks, definitions) and any citation or licensing limits.

---

### Reading Log
**Always capture.** Append one entry per round; never rewrite earlier entries.

Each entry records the pages read, what was added, the judgment calls made (document type, sections skipped, values read approximately, ambiguous claims and how they were interpreted), and open questions to resolve in later pages. The same entry is what you show the user at the pause.

**Example:**

```markdown
- **Pages 1–12:** Typed as analyst report (title page: "Magic Quadrant…"). Added Evidence Base (survey n=312, p. 3).
  Judgment calls: Fig. 1 vendor positions read visually; exact coordinates approximate.
  Open: methodology appendix referenced (p. 4) but not yet reached.
```

---

## Notes Format Template

Create `<basename>_text.md` with this header block after the first round, then populate each applicable section:

```markdown
# Reading Notes: [Document Title]

**Status:** in progress — pages 1–12 of 42
**Document type:** [Academic / Analyst report / Whitepaper / Strategic]
**Source:** [URL or file path]
**Read:** [Date]

---

## Bibliographic Metadata
authors: [LastName1, LastName2, ...]
title: <verbatim>
year:
publisher / venue:
doi_or_url:

## Summary

## Problem & Motivation

## Audience

## Core Approach

## Evidence Base

## Technical Components / Evaluation Framework

## Key Formulations
[Skip if no mathematical or algorithmic content]

## Inputs, Outputs & Interfaces
[Skip if no system or pipeline described]

## Dependencies & Prerequisites
[Skip if no explicit stack or tooling stated]

## Performance & Tradeoffs

## Figures & Tables
[Skip if none]

## Content Hooks

### Counterintuitive or surprising

### Strong claim to engage with

### Analogy or metaphor from the document

## Gaps & Open Questions

## Verifiability & Reuse

## Reading Log
```

Omit sections marked for skipping entirely — don't leave blank headers. The Summary header stays empty until the final round.
