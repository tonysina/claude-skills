---
name: good-presentations
description: >
  Creates persuasive, rhetorically structured PowerPoint presentations using
  the Rhetoric of Decks framework. Use when asked to build a webinar, thought
  leadership deck, knowledge summary, presentation, or slides — especially
  when the goal is to persuade, inform, or move an audience to action. Triggers
  on: "build a deck", "create a presentation", "make slides", "webinar deck",
  "thought leadership", "knowledge summary", "help me present", "turn this into
  a deck", or any request to structure ideas into slides. Do NOT use for
  brand-specific presentations or templated sales decks with fixed formatting
  requirements.
metadata:
  version: 1.1.0
---

# Good Presentations

Build presentations that persuade. This skill applies the Rhetoric of Decks
framework to any PowerPoint output — webinars, thought leadership, knowledge
summaries, and conference talks.

For pptx mechanics (code, shapes, charts, QA), always read and follow
`/mnt/skills/public/pptx/SKILL.md`. This skill governs structure and
rhetoric. The pptx skill governs execution.

---

## Step 1: Triage Before Touching Anything

Answer three questions before writing a single slide.

**Q1: What context?**
- **Webinar / live presentation** — audience is present, attention is contested,
  slides support speech. Lean sparse. One idea per slide.
- **Thought leadership** — slides may circulate without you. Titles must carry
  the argument alone. Figures must be self-interpreting.
- **Knowledge summary** — reference material. Denser than live presentations,
  but still structured around a clear argument, not just information.

**Q2: What is the single takeaway?**
If the audience remembers one thing tomorrow, what is it? Write this sentence
before building anything. It belongs on the closing slide.

**Q3: What does the audience doubt?**
What is the strongest objection to your argument? You will address it directly
in a Devil's Advocate slide before Q&A.

---

## Step 2: The Non-Negotiable Rules

These are constraints, not guidelines.

### Assertion titles
Every slide title is a claim, not a label.
- Wrong: "Results" / "Approach" / "Key Findings"
- Right: "Human-AI teams outperform solo AI by 34%" / "Most organizations skip
  the step that determines outcome"

If someone reads only the titles in sequence, they must understand the full
argument. Titles ARE the argument. Everything else is evidence.

### One idea per slide
Exactly one. If a slide contains two ideas, split it. No exceptions for any
context, including knowledge summaries.

### Bullets only when justified
Bullets mean you haven't found the structure. Before writing a bullet list, ask:
Is this a sequence? A contrast? A causal chain? A hierarchy? Make that structure
visible instead. Use bullets only for genuinely parallel items of equal weight
(e.g., a list of axioms, a set of options to choose from).

### White space is confidence
Dense slides signal anxiety. Empty space signals you know what matters. Never
fill a slide because it looks sparse — the sparseness is the point.

### Minimum readable size
Body text: 24pt minimum. Absolute floor (footnotes, source notes): 18pt.
Text that can't be read from the back of a room doesn't belong on the slide.

---

## Step 3: Aesthetic Standards

These rules apply to every slide in every context. They are not stylistic
preferences — they are execution constraints.

### Typography
- Body text: 24pt minimum
- Absolute floor for footnotes and source notes: 18pt
- Sans-serif fonts only
- Never justify text — always ragged right
- Maximum two fonts: one for headings, one for body

### Composition
- White space is confidence — never fill a slide because it looks sparse
- One focal point per slide — use contrast (color, size, position) sparingly
  and only to direct attention to what matters most

### Charts and data
- Every chart communicates exactly one finding
- Chart title states the finding, not the chart type:
  "Adoption doubled after mandate" not "Adoption Over Time"
- Label data directly on the chart — no legends requiring eye movement
- Remove all chartjunk: gridlines, borders, 3D effects, unnecessary axis marks

---

## Step 4: Deck Structure

### Opening (first content slide)
Never start with an agenda. Never start with "Today I'll cover..."
Start with one of:
- A surprising statistic (large, centered, alone on the slide)
- An unanswered question the audience already feels
- A bold claim you'll spend the deck proving

The audience decides in the first 60 seconds whether to pay attention.
Win or lose in that window.

### Three-act arc
Every deck tells a story:
- **Act I — Setup**: Establish the problem or gap. Make the audience feel it.
- **Act II — Development**: Evidence, analysis, argument. Build the case.
- **Act III — Resolution**: The insight, the implication, the call to action.

### Pyramid principle
Lead with the conclusion, then prove it. State your finding on slide 2 or 3.
Spend the rest of the deck justifying it. Do not build suspense.

### Transition slides
Dark-background section dividers mark major structural shifts. They reorient
the audience without repeating content. Use them between acts.

### Devil's Advocate slide
Before the conclusion, present the strongest objection to your argument.
Acknowledge what makes it reasonable. Then explain why it doesn't hold.
Format: "A skeptic would say... / Here is how we address it..."
This builds credibility through transparency, not defensiveness.

### Closing slide
One sentence. The thing they should remember tomorrow.
Not "Questions?" Not a summary. One memorable claim.

---

## Step 5: Rhetorical Moves

### Ethos (credibility)
- Show your methodology, not just your conclusions
- Acknowledge limitations before Q&A — preempt objections
- The Devil's Advocate slide is the single strongest ethos move available

### Pathos (stakes)
- Open with a problem the audience already feels
- Connect data to human impact where relevant
- Validate frustrations they recognize

### Logos (argument)
- Every chart makes exactly one claim — see Step 3 for chart execution rules
- Structure reveals logic: sequences, contrasts, causal chains are all more
  persuasive than the same content in a bullet list

### MB/MC equivalence
Every slide should deliver roughly equal value relative to the cognitive load
it imposes. Walk through the finished deck and ask: is any slide carrying
more weight than its neighbors can sustain? Redistribute or cut.

### Defamiliarization
Find one moment in the deck to break the expected pattern: a single large
number alone on a slide, an unexpected reframe, a question where a statement
was expected. This breaks automatic processing and demands genuine engagement.
Use it once, deliberately.

---

## Step 6: Context-Specific Patterns

Read `references/context-patterns.md` for detailed structural guidance on:
- Webinar decks (live, contested attention, speaker-dependent)
- Thought leadership (circulates independently, titles carry everything)
- Knowledge summaries (reference material, denser but still argued)

---

## Step 7: Build the Deck

Once structure is clear, read `/mnt/skills/public/pptx/SKILL.md` for all
mechanics: pptxgenjs syntax, color palettes, typography, shapes, charts,
icons, and the required QA loop.

Key reminders from the pptx skill that matter most here:
- Never use `#` with hex colors
- Never reuse option objects across calls (use factory functions for shadows)
- Run the full visual QA loop — convert to images, inspect for overlaps,
  overflow, low contrast, and leftover placeholder text
- Every slide needs a visual element — not text-only

---

## Step 8: QA the Rhetoric

After the pptx QA loop, do a separate rhetoric pass:

1. Read only the slide titles in sequence. Do they tell the complete argument?
   If not, rewrite the failing titles.
2. Does every slide contain exactly one idea? Split any that don't.
3. Is the opening a provocation, not an agenda?
4. Is the closing a single memorable claim, not "Questions?"?
5. Is the Devil's Advocate slide present and substantive?
6. Are all bullet lists justified, or can any be replaced with structure?

---

## Reference Index

| File | When to read |
|------|-------------|
| `references/context-patterns.md` | Before structuring any deck — details for each context type |
| `/mnt/skills/public/pptx/SKILL.md` | All pptx mechanics, code syntax, shapes, charts, QA loop |
