# Cognitive Distribution Mapping

Framework for deciding SHOULD AI or human handle each task, with dynamic allocation strategies and trust considerations.

## Human Strengths

Assign to humans when the task requires:

| Strength | Examples |
|----------|----------|
| Goal definition | Setting objectives, defining success criteria |
| Context understanding | Organizational dynamics, stakeholder needs |
| Judgment calls | Decisions with incomplete information, risk assessment |
| Ambiguity resolution | Interpreting unclear requirements |
| Ethical decisions | Values-based choices, privacy tradeoffs |
| Creative direction | Aesthetic vision, brand voice, design direction |
| Stakeholder intuition | Reading people, negotiation, trust-building |

## AI Strengths

Assign to AI when the task requires:

| Strength | Examples |
|----------|----------|
| Information retrieval | Search, database queries, finding data at scale |
| Pattern recognition | Anomaly detection, clustering, trend identification |
| Rapid iteration | Fast generation of alternatives, draft variations |
| Consistency | Applying rules uniformly, formatting, compliance |
| Tedious execution | Data entry, transcription, repetitive tasks |
| Multi-source synthesis | Research summaries, comparisons across sources |
| 24/7 availability | Monitoring, alerts, always-on processing |

## Collaborative Intelligence Pattern

Highest value emerges at the intersection:

```
Human: Defines goal
   ↓
AI: Discovers options, synthesizes information
   ↓
Human: Applies judgment to select approach
   ↓
AI: Executes at scale with consistency
   ↓
Human: Evaluates results, refines direction
```

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| Human doing AI work | Tedious processing by humans | Automate discovery/synthesis |
| AI doing human work | AI making strategic decisions | Keep judgment with humans |
| No clear handoffs | Confusion about responsibility | Define explicit control points |
| Over-automation | Removing humans from verification | Keep fast feedback loops |

## Cognitive Split Reference

| Architecture Type | Human % | AI % | Human Focus | AI Focus |
|-------------------|---------|------|-------------|----------|
| Discovery | 20% | 80% | Direction, evaluation | Search, synthesis, citation |
| Curation | 30% | 70% | Source selection, exploration | Analysis, mapping, formats |
| Creation | 40% | 60% | Voice, judgment, editing | Drafting, research, formatting |
| Analysis | 25% | 75% | Questions, interpretation | Data processing, visualization |

## Dynamic Task Allocation

Beyond static assignment, advanced systems shift responsibilities based on context:

### When to Use Dynamic Allocation

**Context-based shifts**:
- Normal conditions: AI handles routine processing
- Anomalies detected: Human reviews and decides
- High stakes: Human involved earlier in workflow
- Learning phase: Human validates more frequently

**Capability-based shifts**:
- AI confident: Autonomous execution
- AI uncertain: Human consultation
- Human fatigued: AI takes on more tasks
- Human available: AI delegates complex decisions

### Implementation Patterns

**Confidence-based handoff**:
```
AI assesses task → 
  If confidence > 90%: Execute autonomously
  If confidence 70-90%: Execute with human review
  If confidence < 70%: Hand off to human
```

**Adaptive automation**:
```
Monitor human workload →
  If workload low: Human handles complex decisions
  If workload high: AI handles more autonomously
  Adjust boundaries in real-time
```

**Progressive autonomy**:
```
New task type: Human in the loop for all instances
System learns: Gradually increase AI autonomy
Stable performance: Mostly autonomous with spot checks
```

### Cautions on Dynamic Allocation

- **User acceptance**: People prefer user-invoked delegation over AI-invoked
- **Self-threat**: Unexpected AI delegation can threaten user sense of competence
- **Control perception**: Maintain user control even when AI suggests automation
- **Transparency**: Always show when allocation shifts and why

## Trust Calibration

Effective collaboration requires appropriate trust levels—not too high, not too low.

### Trust Dimensions

| Dimension | What it means | How to build it |
|-----------|---------------|-----------------|
| **Performance** | Does AI do its job well? | Track accuracy, show metrics |
| **Reliability** | Does AI work consistently? | Minimize failures, handle errors gracefully |
| **Transparency** | Can I see what AI did? | Show reasoning, surface confidence |
| **Controllability** | Can I intervene/override? | Provide control points, enable override |

### Trust Evolution Phases

**Phase 1: Initiation**
- User has expectations but limited experience
- Show capabilities clearly upfront
- Set realistic performance expectations
- Provide easy success experiences

**Phase 2: Execution**
- User actively works with AI
- Demonstrate consistent performance
- Explain decisions transparently
- Respond to feedback

**Phase 3: Adaptation**
- User adjusts mental model of AI
- Show how system learns/improves
- Highlight successful collaborations
- Acknowledge and fix failures

**Phase 4: Evaluation**
- User reflects on experience
- Solicit feedback explicitly
- Adjust system based on learnings
- Reinforce trust through improvements

### Building Appropriate Trust

**Avoid over-trust**:
- Show AI confidence levels honestly
- Surface uncertainty clearly
- Require validation for critical decisions
- Make errors visible, not hidden

**Avoid under-trust**:
- Demonstrate consistent quality
- Show successful outcomes
- Reduce friction in workflow
- Build competence gradually

**Calibrate continuously**:
- Monitor trust signals (override rate, verification time)
- Adjust transparency based on trust level
- More explanation when trust is low
- Less friction when trust is established

## Fusion Skills

New capabilities emerge at the human-AI boundary:

### Intelligent Interrogation
**What**: Skilled questioning of AI systems to extract best outputs

**Techniques**:
- Ask for multiple approaches, then synthesize
- Request AI to explain reasoning
- Challenge assumptions explicitly
- Probe edge cases and limitations

**Example**: "Show me three different approaches to this problem, explain tradeoffs, and recommend which one fits our constraints."

### Reciprocal Apprenticing
**What**: Humans and AI mutually train each other

**Human teaches AI**:
- Provides examples of good/bad outputs
- Corrects misunderstandings
- Shares domain context
- Guides strategic direction

**AI teaches human**:
- Surfaces patterns human missed
- Provides alternative perspectives
- Explains new analytical techniques
- Accelerates skill development

### Judgment Integration
**What**: Combining AI pattern recognition with human context/values

**Process**:
```
AI: "Pattern analysis suggests option A"
Human: "But given stakeholder dynamics, option B better"
Together: "Adapt option A with elements of B"
```

**Skills required**:
- Understand AI's analytical framework
- Apply contextual knowledge AI lacks
- Synthesize into hybrid decision
- Explain rationale to others

### Shared Cognitive Workspace
**What**: Humans and AI work on different aspects of same problem simultaneously

**Setup**:
- AI processes data, finds patterns, generates options
- Human sets strategy, applies judgment, validates direction
- Both see each other's work in real-time
- Handoffs are fluid and bidirectional

**Example**: 
- AI analyzes customer data, surfaces segments
- Human reviews segments, applies market knowledge
- Human adjusts segmentation criteria
- AI re-runs analysis with new parameters
- Iterate until both agree on approach

## Allocation Decision Framework

Use this decision tree for each task:

```
1. Is this a goal-setting or strategic decision?
   YES → Human leads (may use AI for analysis)
   NO → Continue

2. Does this require ethical judgment or stakeholder intuition?
   YES → Human leads (may use AI for information)
   NO → Continue

3. Is this pattern recognition or data synthesis at scale?
   YES → AI leads (human validates results)
   NO → Continue

4. Is this tedious, repetitive, or requires 24/7 availability?
   YES → AI handles (human monitors periodically)
   NO → Continue

5. Is this a creative direction or brand voice decision?
   YES → Human leads (may use AI for drafts)
   NO → Continue

6. Does this benefit from both pattern recognition AND context?
   YES → Collaborative (shared cognitive workspace)
   NO → Evaluate case-by-case
```

## Monitoring Task Allocation Effectiveness

Track these metrics to validate allocation decisions:

**Efficiency Metrics**:
- Task completion time (AI vs human vs collaborative)
- Cost per task (accounting for both AI and human time)
- Throughput (tasks per hour/day)

**Quality Metrics**:
- Error rate by task type and owner
- Rework frequency
- User satisfaction with outputs

**Collaboration Metrics**:
- Handoff success rate (clean transitions vs failures)
- Iteration cycles needed (more = poor allocation)
- Override frequency (human changing AI decisions)

**Experience Metrics**:
- User confidence in delegation decisions
- Cognitive load (subjective assessment)
- Frustration points in workflow

Review quarterly and adjust task allocation based on data.
