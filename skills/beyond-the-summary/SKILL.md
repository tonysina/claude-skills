---
name: beyond-the-summary
description: >
  Extracts non-obvious insights, tensions, actionable implications, and gaps
  from documents — going far beyond basic summarization. Use when user says
  "analyze this document", "what are the insights", "what's really going on
  in this", "extract insights", "briefing on this", "what am I missing",
  "what does this really mean", "break this down for me", "what should I
  take away from this", or uploads a document and asks for more than a
  simple summary. Also triggers on "insight extraction", "strategic briefing",
  "deep read", or "analyze this report/paper/article/plan/transcript".
  Do NOT use for simple summarization requests where the user explicitly
  just wants a shorter version, or for document format conversion tasks.
metadata:
  author: Tony
  version: 1.3.0
---

# Document Insight Extractor

Transform documents from "what does it say" into "what does it mean" — extracting the insights, tensions, and implications that surface-level summaries miss.

## Why This Exists

"Summarize this" compresses information. This skill *analyzes* it. The difference: a summary tells you what the document says in fewer words. An insight extraction tells you what matters, what's contradictory, what's missing, and what to do about it.

This is particularly valuable for:
- Research papers where methodology choices shape conclusions
- Strategy documents where unstated assumptions determine success or failure
- Meeting transcripts where implicit decisions hide in plain sight
- Industry reports where narrative framing obscures inconvenient facts
- Competitor materials where what's *not* said reveals positioning

## Core Analysis Framework

Read the full document carefully before beginning any analysis. Depth of thinking matters more than speed of output — sitting with the material produces better insights than rushing to generate a response. This is analytical work, not summarization, so give it the attention it deserves.

Apply all four lenses to every document, in this order:

### 1. Non-Obvious Insights (3–5)

Identify things that aren't stated explicitly but can be inferred by connecting dots across sections or reading between the lines. Skip anything the author already highlights as a key point or conclusion — the user can read those themselves. Look for:
- Second-order implications the author may not have intended to reveal
- Patterns that emerge across sections but are never called out
- Assumptions embedded in word choices, framing, or structure
- What the document reveals about the author's priorities or blindspots

For each insight, signal its grounding: mark it **[textual]** if it's directly supported by specific language or data in the document, or **[inferential]** if it's a logical leap connecting dots that the document doesn't explicitly link. For both types, anchor to specific passages, sections, or data points in the document — even inferential leaps should be traceable to particular textual moments that prompted the inference, not general impressions of the document's tone or direction. This helps the reader gauge how much weight to place on each insight and which ones warrant further verification.

### 2. Tensions and Contradictions

Find where the argument conflicts with itself or with conventional wisdom. Look for:
- Internal friction (e.g., optimistic projections alongside cautious hedging)
- Gaps between stated goals and proposed actions
- Claims that sit uneasily with evidence presented elsewhere in the document
- Positions that contradict mainstream thinking without acknowledging the disagreement

Present these as genuine analytical observations, not gotchas. The goal is to help the reader think more clearly, not to score points against the author.

### 3. The "So What" (Single Actionable Takeaway)

Commit to one prioritized implication — the thing a smart, busy person should walk away with. This is not a theme or a topic; it's a specific, actionable statement. Frame it as: "If you only take one thing from this document, it should be X, because Y."

Resist the urge to hedge with multiple equally-weighted takeaways. Prioritization is the value here.

### 4. What's Missing

Identify the most important question the document raises but never answers. This often reveals:
- The follow-up research or conversation that needs to happen
- Data the author didn't have (or chose not to include)
- Perspectives or stakeholders not represented
- The "next domino" — what happens after the document's scope ends

## Document Type Detection and Specialized Lenses

After applying the four core lenses, detect the document type and add the appropriate specialized analysis. If the type is ambiguous, ask the user or apply the closest match.

### Research Papers / Academic Articles
Add: **Methodological Leverage Points** — Flag specific methodological choices (sample selection, statistical methods, study design, timeframe, variable definitions) that could meaningfully change the conclusions if done differently. Not a general critique — identify the 1-2 choices with the highest impact on the findings.

### Strategy Documents / Business Plans
Add: **Strongest Unstated Assumption** — Identify the single biggest assumption this plan depends on that is never explicitly stated or defended. Frame it as: "This entire plan assumes X. If X turns out to be wrong, the consequence is Y."

### Meeting Notes / Transcripts
Add: **Implicit Decisions** — Identify moments where a decision was effectively made but never explicitly confirmed. These are the "everyone nodded and moved on" moments that later cause confusion about what was actually agreed. Flag them as: "It appears the group decided X, but this was never formally confirmed."

### News Articles / Industry Reports
Add: **Narrative Architecture** — Identify what narrative the piece is constructing and what facts would complicate or undermine it. This isn't about bias — it's about helping the reader see the framing choices so they can think independently.

### Policy / Regulatory Documents
Add: **Implementation Gap** — Identify where the stated intent of the policy diverges most from what would likely happen in practice, given real-world incentives and constraints.

### Sales / Marketing Materials
Add: **Positioning Tells** — Identify what the material reveals about the company's perceived weaknesses, competitive threats, or market position based on what it emphasizes, avoids, or reframes.

## Output Format

Produce the briefing as clean, readable markdown with these sections:

```
## Document Insight Briefing

**Source:** [document title or description]
**Type detected:** [research / strategy / meeting / news / policy / sales / other]

### Non-Obvious Insights
1. **[textual]** [insight] — [specific passage or data point that supports this]
2. **[inferential]** [insight] — [specific sections or passages that prompted this inference]
3. ...

### Tensions & Contradictions
- [tension] — [where it appears and why it matters]
- ...

### The "So What"
[Single actionable takeaway with reasoning]

### What's Missing
[Key unanswered question and why it matters]

### [Type-Specific Section Title]
[Specialized analysis based on detected document type]
```

Keep the total briefing concise — aim for roughly 400-600 words. The value is in density and precision, not length.

Do NOT include in the briefing:
- A summary or recap of the document before the analysis (the user already has the document)
- A closing section that restates all the insights in condensed form
- Generic observations the user could have reached by skimming the headings
- Caveats about AI limitations or disclaimers about the analysis being "just one perspective"

## Guidelines

- **Work from full text.** If the user pastes or uploads the document, analyze it directly. If they provide a URL, fetch and read the full content first.
- **Don't combine with summarization.** If the user also asks for a summary, produce the insight briefing first as the primary deliverable, then offer a brief summary separately if they still want one. Mixing the two dilutes both.
- **Encourage follow-up.** After presenting the briefing, invite the user to drill into any section — e.g., "Want me to go deeper on tension #2?" or "I can explore what's missing in more detail."
- **Be honest about confidence.** If the document is too short, too vague, or too narrow for meaningful insight extraction, say so rather than manufacturing pseudo-insights.
- **Fewer and stronger beats more and weaker.** If a section has fewer genuine findings than the template suggests, report fewer. Two strong insights beat four where two are padding. An empty tensions section with a note that the document is internally consistent is more valuable than a fabricated contradiction. The template is a structure, not a quota.
- **Quote sparingly.** Reference specific passages to support your analysis, but the briefing should be your analytical voice, not a collage of excerpts.

## Examples

### Example 1: Strategy Document
User says: "What are the real insights in this quarterly strategy update?"
Actions:
1. Read the full document
2. Apply four core lenses
3. Detect type as strategy document
4. Add "Strongest Unstated Assumption" section
5. Produce structured briefing
Result: Briefing revealing that the growth targets assume a competitor acquisition that hasn't closed, and the hiring plan contradicts the stated budget constraints.

### Example 2: Research Paper
User says: "Analyze this paper for me — what should I actually take away?"
Actions:
1. Read the full paper including methodology sections
2. Apply four core lenses
3. Detect type as research/academic
4. Add "Methodological Leverage Points" section
5. Produce structured briefing
Result: Briefing identifying that the sample excludes the fastest-growing market segment, and the 3-year timeframe misses a known cyclical pattern.

### Example 3: Meeting Transcript
User says: "Break down what really happened in this meeting"
Actions:
1. Read the full transcript
2. Apply four core lenses
3. Detect type as meeting/transcript
4. Add "Implicit Decisions" section
5. Produce structured briefing
Result: Briefing surfacing two decisions that were implicitly made when the group moved past objections without resolution, plus a contradiction between the agreed timeline and resource allocation.
