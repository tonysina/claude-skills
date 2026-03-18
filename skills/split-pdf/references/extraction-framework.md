# Extraction Framework

This file defines what to capture during deep reading, how it adapts by document type, and what good notes look like for each dimension.

---

## Document Type Mapping

The dimensions you capture and how you frame them depend on the detected document type. Use this table as your guide:

| Dimension | Academic / Technical | Analyst Report | Whitepaper / Tech Doc | Strategic / Thought Leadership |
|-----------|---------------------|----------------|-----------------------|-------------------------------|
| Problem & motivation | ✅ | ✅ | ✅ | ✅ |
| Core approach | ✅ | ✅ | ✅ | ✅ |
| Performance & tradeoffs | ✅ Results + benchmarks | ✅ Market data + ratings | ✅ Claimed benefits + limits | ✅ Argument strength + counterpoints |
| Content hooks | ✅ | ✅ | ✅ | ✅ |
| Gaps & open questions | ✅ | ✅ | ✅ | ✅ |
| Technical components | ✅ Architecture + modules | ❌ | ✅ System components | ✅ Framework elements |
| Key formulations | ✅ If mathematical | ❌ | ✅ If algorithmic | ❌ |
| Inputs, outputs & interfaces | ✅ If system described | ❌ | ✅ | ❌ |
| Dependencies & prerequisites | ✅ If stack specified | ❌ | ✅ If stack specified | ❌ |

---

## Dimension Definitions

### 1. Problem & Motivation
**Always capture.**

What specific problem does this document address? Why does the existing approach fail or fall short? Who is affected and why it matters to them.

Write this as a brief statement an intelligent non-expert could understand. This is the "why we need this" — the context that makes everything else meaningful.

**Good:** "Existing LLM context management discards information via summarization, which degrades downstream task performance. This paper addresses how to compress context without information loss."

**Weak:** "The paper is about KV cache compression."

---

### 2. Core Approach
**Always capture.**

The proposed method or argument in plain terms — before any math, before any technical detail. The conceptual model. If someone asked you to explain the idea in two minutes, what would you say?

For technical papers: what is the intuition behind the method?
For analyst reports: what is the central recommendation or thesis?
For strategic docs: what is the core argument or framework?

---

### 3. Performance & Tradeoffs
**Always capture. Frame by document type.**

What did they measure or claim, and against what baseline? What did they gain, and what did they give up?

- **Academic:** Specific benchmark results, comparisons to prior methods, stated limitations.
- **Analyst:** Market ratings, vendor comparisons, adoption data, caveats.
- **Whitepaper:** Claimed benefits, any stated limitations or prerequisites.
- **Strategic:** How well does the argument hold up? What is conceded or left unaddressed?

Capture numbers where they exist. "Performs better" is not useful. "Reduces KV cache size by 90% with less than 2% performance degradation on MMLU" is.

---

### 4. Content Hooks
**Always capture.**

Three types. Pull directly from the document — these should be grounded in what the authors actually say, not inferred:

**Counterintuitive or surprising:** A finding, claim, or result that goes against what a reader would expect. Flag these explicitly — they are the best leads for posts and talks.

**Strong claim to engage with:** A statement the authors make with confidence that you could meaningfully agree with, push back on, or extend. Quote or closely paraphrase.

**Analogy or metaphor from the document:** If the authors use a comparison, image, or framing device to explain their idea, capture it verbatim or near-verbatim. These are often the most memorable and reusable elements.

If a type is genuinely absent from the document, note that rather than inventing one.

---

### 5. Gaps & Open Questions
**Always capture.**

What did the paper not address, gloss over, or defer to future work? What would a practitioner need to figure out themselves? What assumptions does the approach rely on that are not validated?

This dimension serves both builders (what's missing from a spec) and content creators (what's worth arguing about or exploring further).

---

### 6. Technical Components
**Conditional. Capture for academic, whitepaper, and strategic documents. Skip for analyst reports.**

The named building blocks of the approach and how they connect.

- **Academic / technical:** Specific modules, algorithms, sub-methods, and their relationships. Name them as the authors name them.
- **Whitepaper:** System components, integration points, named features.
- **Strategic:** The elements of the framework or model — what the author distinguishes, what the named parts are, how they relate.

Include a brief description of each component's role. A diagram description if one exists in the document.

---

### 7. Key Formulations
**Conditional. Capture only if the document contains mathematical notation, formal algorithms, or decision rules that define the approach.**

The equations or algorithms an implementer would need to reference — not every formula in the paper, only the ones that define the core method.

For each:
- State what it computes or defines
- Note where in the paper it appears (section, equation number)
- Flag any non-obvious notation

If the document has no meaningful formulations, skip this section entirely.

---

### 8. Inputs, Outputs & Interfaces
**Conditional. Capture only if the document describes a system, API, pipeline, or process with defined stages.**

At each stage: what goes in, what comes out, and in what form?

Format, shape, type, or schema where specified. This is the information someone would need to integrate the approach with other systems or implement it end to end.

---

### 9. Dependencies & Prerequisites
**Conditional. Capture only if the document explicitly specifies a technical stack, tooling, model, hardware, or environment assumption.**

What does this build on? What must already exist for the approach to work?

- Frameworks or libraries named
- Model or hardware requirements stated
- Dataset or data format assumptions
- Anything the authors take for granted that a builder would need to source

If the document makes no explicit statements about prerequisites, skip this section.

---

## Notes Format Template

Start `notes.md` with this header block, then populate each applicable section:

```markdown
# Reading Notes: [Document Title]

**Document type:** [Academic / Analyst report / Whitepaper / Strategic]
**Source:** [URL or file path]
**Read:** [Date]

---

## Problem & Motivation

## Core Approach

## Technical Components
[Skip if analyst report or strategic doc without a framework]

## Key Formulations
[Skip if no mathematical or algorithmic content]

## Inputs, Outputs & Interfaces
[Skip if no system or pipeline described]

## Dependencies & Prerequisites
[Skip if no explicit stack or tooling stated]

## Performance & Tradeoffs

## Content Hooks

### Counterintuitive or surprising

### Strong claim to engage with

### Analogy or metaphor from the document

## Gaps & Open Questions
```

Omit sections marked for skipping entirely — don't leave blank headers.
