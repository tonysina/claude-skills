---
name: intelligence-flow-architecture
description: Design how humans and AI collaborate in products, workflows, and processes. Use when architecting AI integration, mapping intelligence flows, designing human-AI collaboration, determining task distribution, analyzing workflows for AI opportunities, redesigning existing processes with AI, evaluating where automation fits, planning AI product features, or defining handoff points between human and AI work. Triggers include "design the AI architecture," "where should AI handle this," "map the intelligence flow," "how should humans and AI work together," "what should be automated vs manual," "redesign this workflow with AI," "how can AI help with [process]," "what parts should AI do," "I want to add AI to [product]," "where does AI fit in," "what's the AI strategy for," or any request about human-AI task allocation and collaboration design.
metadata:
  version: 1.0.0
---

# Intelligence Flow Architecture

Design intelligent systems where humans and AI collaborate effectively. This skill architects HOW cognitive work flows between humans and AI—who does what, where intelligence lives, how they hand off tasks, and how to validate the design works.

## When to Use This Skill

Apply this methodology when:
- Designing new AI-powered products or features
- Redesigning existing workflows to incorporate AI
- Evaluating "should we automate this?" questions
- Defining what AI handles vs what stays human-controlled
- Planning how humans and AI will collaborate
- Analyzing where intelligence should live in your system
- Migrating from manual processes to AI-assisted ones

## Core Questions

Every intelligence flow design must answer:
1. WHERE does AI work autonomously?
2. WHERE does human provide direction?
3. HOW do they hand off work?
4. WHAT intelligence lives in which layer?
5. WHAT happens when the AI fails?
6. HOW do we validate this works?

## The Six Principles

**Principle 1: Design Backward from Autonomous Execution**
Start with "What will the system DO autonomously?"—not "What interface should we show?" The execution layer defines system value; everything else enables that autonomy.

**Principle 2: Embed Intelligence, Don't Bolt It On**
Test: Can you remove the AI and still have a functional product? If yes, it's bolted on. If no, it's embedded. Aim for embedded intelligence as a core architectural layer.

**Principle 3: Optimize the Generation-Verification Loop**
The fastest generation-verification loop wins—not the most autonomous AI. Design for rapid iteration cycles where AI generates and human validates quickly.

**Principle 4: Allocate by Cognitive Fit, Not Capability**
Not "Can AI do this?" but "SHOULD AI do this, or SHOULD human?" Match tasks to cognitive strengths. See [references/cognitive-mapping.md](references/cognitive-mapping.md).

**Principle 5: Design for Probabilistic Reality**
AI systems hallucinate, drift, and degrade under edge cases. Build validation gates, fallback paths, and human oversight into the architecture—not as afterthoughts.

**Principle 6: Preserve Human Control and Context**
Avoid expertise displacement and contextual blindness. Keep humans in strategic roles with sufficient context to make informed decisions.

## 5-Layer Architecture Pattern

| Layer | Function | Owner | Failure Mode |
|-------|----------|-------|--------------|
| 1. Input | Express intention, set parameters | Human | Unclear goals, poor specification |
| 2. Intelligence | Understand intent, plan strategy | AI | Misinterpretation, context blindness |
| 3. Execution | Perform autonomous work | AI | Hallucination, quality issues |
| 4. Output | Deliver results with transparency | AI → Human | Missing context, unexplained decisions |
| 5. Iteration | Evaluate, refine, redirect, loop back | Human | Insufficient oversight, trust calibration failure |

Cognitive split varies by architecture type:
- Discovery (20% human / 80% AI): Research, search, synthesis
- Curation (30% human / 70% AI): Selection, organization, formatting
- Creation (40% human / 60% AI): Content with voice, judgment
- Analysis (25% human / 75% AI): Data processing, visualization

## Design Process

### Phase 1: Understand Current State

**Step 1: Map the Current Workflow**
Document every step users currently do manually:
- What actions they take
- What decisions they make
- What information they need
- How long each step takes
- Where errors occur
- What's tedious vs what requires judgment

**Step 2: Identify Pain Points**
Where does the current workflow break down?
- Bottlenecks (human capacity limits)
- Error patterns (consistency issues)
- Cognitive overload (too much information processing)
- Tedious repetition (low-value manual work)

### Phase 2: Design the Intelligence Flow

**Step 3: Classify Cognitive Work**
For each workflow step, determine cognitive fit using [references/cognitive-mapping.md](references/cognitive-mapping.md):

Human cognitive strengths:
- Goal definition, context understanding, judgment calls
- Ambiguity resolution, ethical decisions, creative direction
- Stakeholder intuition, risk assessment

AI cognitive strengths:
- Information retrieval, pattern recognition, rapid iteration
- Consistency, tedious execution, multi-source synthesis
- 24/7 availability, scale processing

**Step 4: Define Task Allocation**
Decide what AI does autonomously and what human controls:
- **User-invoked**: Human initiates AI action (preferred for user acceptance)
- **AI-invoked**: System offers to help (use sparingly, can feel threatening)
- **Dynamic allocation**: Shift based on context (advanced pattern)

**Step 5: Design Handoff Points**
Define precisely where control transfers:
- What triggers the handoff?
- What information passes between agents?
- How does each party know what the other did?
- What happens if handoff fails?

**Step 6: Design Backward from Execution**
Work backward through layers:
1. Execution: What will AI actually DO?
2. Intelligence: What understanding/planning enables that execution?
3. Orchestration: How does the system manage the workflow?
4. Input: How does human express intent?
5. Iteration: How does human evaluate and refine?

### Phase 3: Validate and De-risk

**Step 7: Apply Validation Checks**
Test your architecture against common failure modes using [references/validation-framework.md](references/validation-framework.md):
- Contextual blindness: Does AI have sufficient context?
- Collaboration gaps: Are handoffs clear?
- Expertise displacement: Is human judgment preserved?
- Trust calibration: Can humans verify AI work quickly?
- Model trap: Are you dependent on one specific AI?

**Step 8: Plan Implementation Phases**
Don't build everything at once. Sequence by:
1. **MVP**: Simplest valuable flow
2. **Phase 2**: Add complexity handling
3. **Phase 3**: Optimize and scale

See [references/implementation-guidance.md](references/implementation-guidance.md) for cost/complexity tradeoffs.

**Step 9: Define Success Metrics**
How will you know this works? Specify:
- Task completion metrics (time, accuracy, cost)
- Collaboration metrics (handoff success, iteration speed)
- Experience metrics (user satisfaction, trust, adoption)
- Business metrics (ROI, efficiency gains)

## Required Outputs

Deliver THREE artifacts:

### Output 1: Architecture Document (Markdown)

```markdown
# [System Name] Intelligence Flow Architecture

## Problem & Opportunity
Current workflow pain points and what AI unlocks.

## Design Decisions
What AI does autonomously and why, based on cognitive fit analysis.

## The Flow
[Human action] → [AI action] → [Human action]
Specify user-invoked vs AI-invoked delegation.

## 5-Layer Architecture
Layer-by-layer breakdown with:
- Owner (Human/AI/Shared)
- Cognitive split percentage
- Failure modes
- Mitigation strategies

## Task Allocation Matrix
| Task | Owner | Rationale | Handoff Mechanism |
|------|-------|-----------|-------------------|
| [Task] | Human/AI | [Why this allocation] | [How control transfers] |

## Validation Results
How architecture addresses common failure modes:
- Contextual blindness: [How you avoid it]
- Collaboration gaps: [How handoffs work]
- Expertise displacement: [How human judgment preserved]
- Trust calibration: [How verification works]

## Implementation Roadmap
- MVP scope: [What to build first]
- Success metrics: [How to measure]
- Phased rollout: [What comes next]

## Edge Cases & Fallbacks
What happens when:
- AI fails at its task
- Human input is unclear
- Context is missing
- System needs to escalate
```

### Output 2: Visual Architecture Diagram (React Artifact)

Create an interactive layered diagram showing:
- 5 layers with clear labels
- Human vs AI ownership (color-coded)
- Cognitive split percentages
- Bidirectional flow arrows
- Failure mode indicators
- Handoff point markers

Design style: Professional with gradient backgrounds for AI layers, clean typography, clear visual hierarchy.

### Output 3: Task Allocation Table

Create a structured table (in the markdown doc or as separate artifact) showing:
- Every task in the workflow
- Assigned to Human/AI/Shared
- Rationale for allocation
- How handoff occurs
- What happens on failure

## After Delivering Outputs

Present options for next steps:
1. **PRD** — Product requirements document for implementation
2. **Content** — Blog post, presentation, or thought leadership explaining the architecture
3. **Validation Workshop** — Facilitate stakeholder review of the design
4. **Implementation Plan** — Technical specifications and development roadmap
5. **Change Management** — How to prepare teams for new roles

Ask which the user wants to pursue.

## Reference Files

Core frameworks:
- [references/cognitive-mapping.md](references/cognitive-mapping.md) — Human vs AI strengths framework for task allocation
- [references/validation-framework.md](references/validation-framework.md) — Test architecture against failure modes
- [references/implementation-guidance.md](references/implementation-guidance.md) — Cost/complexity tradeoffs and phasing strategies

Examples and patterns:
- [references/examples.md](references/examples.md) — Perplexity, NotebookLM, email transformation case studies
- [references/agentic-patterns.md](references/agentic-patterns.md) — Advanced patterns: reflection, tool use, planning, multi-agent

## Critical Reminders

**Avoid the Model Trap**: Don't mistake access to intelligence for ownership of capability. Design systems that work across models and vendors.

**Optimize Loops, Not Autonomy**: The fastest generation-verification loop wins. Don't pursue full automation if rapid human-in-the-loop is more effective.

**Design for Failure**: AI is probabilistic. Hallucinations, drift, and edge cases are inevitable. Build validation gates and fallback paths from day one.

**Preserve Context**: Avoid contextual blindness by ensuring AI has access to relevant information and humans maintain situational awareness.

**Respect User Control**: User-invoked delegation is more accepted than AI-invoked. Let humans initiate AI assistance when possible.
