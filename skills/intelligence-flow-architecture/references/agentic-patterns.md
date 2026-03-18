# Agentic Design Patterns

Advanced patterns for building autonomous AI agents that reflect, plan, use tools, and collaborate.

## What Are Agentic Patterns?

Agentic patterns transform AI from single-shot response systems into iterative, self-improving agents that can:
- Reflect on their own work
- Use external tools dynamically
- Plan multi-step approaches
- Collaborate with other agents

These patterns significantly improve performance on complex tasks by adding iterative workflows around AI models.

## Pattern 1: Reflection

**What it is**: AI evaluates its own output, identifies flaws, and iterates to improve.

**How it works**:
1. AI generates initial output
2. AI critiques its own work against criteria
3. AI refines output based on critique
4. Repeat until quality threshold met

**When to use**:
- Quality is critical (writing, code, analysis)
- Clear evaluation criteria exist
- Iteration cost is acceptable
- Perfection matters more than speed

**Implementation**:
```
User: [Task request]
  ↓
AI: [Generate initial output]
  ↓
AI: [Self-critique: "This output has issues X, Y, Z"]
  ↓
AI: [Generate improved version addressing X, Y, Z]
  ↓
AI: [Verify improvements]
  ↓
Output to user
```

**Example**: Code generation
- Generate code
- Review for bugs, style issues, edge cases
- Refine code
- Verify improvements
- Deliver polished result

**Benefits**:
- Higher quality outputs
- Catches obvious errors automatically
- Reduces human review burden

**Tradeoffs**:
- Slower (multiple AI calls)
- More expensive (more tokens)
- May over-correct or get stuck in loops

**Human role**: Set quality criteria, judge final output, break infinite loops

---

## Pattern 2: Tool Use

**What it is**: AI dynamically calls external tools/functions to accomplish tasks it can't do alone.

**How it works**:
1. AI receives task
2. AI identifies what tools are needed
3. AI calls appropriate tools with parameters
4. AI receives tool results
5. AI synthesizes results into final answer

**When to use**:
- Task requires real-time information (search, databases)
- Need deterministic computation (calculations, APIs)
- Must interact with external systems (CRM, email, etc.)
- AI knowledge alone is insufficient

**Implementation**:
```
User: "What's the weather in Tokyo and should I bring an umbrella?"
  ↓
AI: [Identifies need for weather data]
  ↓
AI: [Calls weather API for Tokyo]
  ↓
API: [Returns current conditions + forecast]
  ↓
AI: [Synthesizes: "It's 72°F and clear now, but rain forecast this afternoon. Yes, bring umbrella."]
```

**Tool categories**:
- **Information retrieval**: Search, databases, APIs
- **Computation**: Calculators, data processing, code execution
- **External actions**: Send email, create tasks, update systems
- **Specialized processing**: Image analysis, code execution, file parsing

**Benefits**:
- Overcomes AI knowledge limitations
- Enables real-time information
- Allows complex computations
- Interacts with real systems

**Tradeoffs**:
- Complexity in tool selection logic
- Error handling for tool failures
- Security concerns (tool access control)
- Cost and latency from tool calls

**Human role**: Define available tools, set permissions, validate tool outputs

---

## Pattern 3: Planning

**What it is**: AI breaks complex tasks into steps, creates a plan, then executes it sequentially.

**How it works**:
1. AI analyzes complex task
2. AI creates step-by-step plan
3. AI executes each step
4. AI checks progress after each step
5. AI adapts plan if needed

**When to use**:
- Multi-step tasks with dependencies
- Complex problem requiring decomposition
- Need visibility into AI's approach
- Tasks where order matters

**Implementation**:
```
User: "Analyze our Q4 sales data and create a presentation"
  ↓
AI: [Creates plan:
  1. Retrieve Q4 sales data
  2. Analyze trends and patterns
  3. Identify key insights
  4. Create visualizations
  5. Draft presentation outline
  6. Generate slides with data
  7. Write speaker notes
]
  ↓
AI: [Executes step 1] → "Retrieved sales data"
AI: [Executes step 2] → "Found 15% growth trend"
AI: [Executes step 3] → "Key insight: Mobile sales up 40%"
  ... continues through all steps ...
  ↓
Output: Completed presentation
```

**Planning approaches**:
- **Static planning**: Plan entire approach upfront
- **Dynamic planning**: Adjust plan based on intermediate results
- **Hierarchical planning**: Break into subplans at different levels
- **Contingent planning**: "If X then Y, else Z" logic

**Benefits**:
- Handles complex multi-step tasks
- Makes AI reasoning transparent
- Easier to debug failures
- Allows human oversight of approach

**Tradeoffs**:
- Overhead in planning time
- May over-plan simple tasks
- Plans can become outdated as task evolves
- Requires good task decomposition

**Human role**: Approve plan before execution, intervene during execution, validate final output

---

## Pattern 4: Multi-Agent Collaboration

**What it is**: Multiple specialized AI agents work together, each contributing their expertise.

**How it works**:
1. Task assigned to orchestrator agent
2. Orchestrator identifies subtasks
3. Specialized agents assigned to subtasks
4. Agents work independently or collaboratively
5. Orchestrator synthesizes results

**When to use**:
- Task requires diverse expertise
- Benefits from parallel processing
- Different parts need different approaches
- Complex tasks beyond single agent capability

**Implementation**:

**Sequential handoff**:
```
User: "Research competitors and write strategic analysis"
  ↓
Research Agent: [Gathers competitive intelligence]
  ↓ [passes findings to]
Analysis Agent: [Identifies strategic implications]
  ↓ [passes to]
Writing Agent: [Crafts executive summary]
  ↓
Output: Strategic analysis document
```

**Parallel collaboration**:
```
User: "Evaluate this acquisition target"
  ↓
Orchestrator: [Splits into parallel tasks]
  ├─ Financial Agent: [Analyzes financials]
  ├─ Market Agent: [Assesses market position]
  ├─ Tech Agent: [Evaluates technology stack]
  └─ Legal Agent: [Reviews legal considerations]
  ↓ [All results to orchestrator]
Orchestrator: [Synthesizes into recommendation]
```

**Agent types**:
- **Specialist agents**: Deep expertise in one domain
- **Coordinator agents**: Orchestrate other agents
- **Quality agents**: Review and validate outputs
- **Fallback agents**: Handle errors from others

**Benefits**:
- Leverage specialized models/prompts per domain
- Enable parallel processing
- Separate concerns cleanly
- Scale complexity by adding agents

**Tradeoffs**:
- Coordination complexity
- Context loss at agent boundaries
- Higher cost (multiple agents)
- Debugging distributed behavior

**Human role**: Define agent specializations, orchestrate high-level flow, resolve agent conflicts

---

## Combining Patterns

The most powerful systems combine multiple patterns:

### Pattern Combination Examples

**Research + Analysis + Presentation**
```
Planning → Tool Use → Reflection
1. Plan: Break into research, analysis, writing
2. Tool Use: Search for information, fetch data
3. Reflection: Review quality at each step
```

**Complex Investigation**
```
Multi-Agent → Planning → Tool Use → Reflection
1. Multi-Agent: Assign investigation angles to specialist agents
2. Planning: Each agent creates investigation plan
3. Tool Use: Agents use relevant tools (search, APIs)
4. Reflection: Each agent reviews findings before sharing
```

**Collaborative Problem-Solving**
```
Multi-Agent → Reflection
1. Multiple agents propose solutions independently
2. Agents critique each other's solutions
3. Synthesize best elements into final approach
```

### When to Combine

Combine patterns when:
- Single pattern insufficient for task complexity
- Different phases benefit from different patterns
- Need both depth (reflection) and breadth (multi-agent)
- Task has clear phases that map to different patterns

Don't combine if:
- Task is simple enough for one pattern
- Coordination cost exceeds benefit
- Patterns conflict (e.g., fast planning vs slow reflection)

---

## Architectural Integration

### Layer 2: Intelligence Layer

Most agentic patterns live in the Intelligence layer:
- **Planning**: Creates execution strategy
- **Tool selection**: Identifies what tools needed
- **Agent coordination**: Orchestrates multiple agents

### Layer 3: Execution Layer

Some patterns extend into Execution:
- **Tool use**: Actual tool calls happen here
- **Agent execution**: Individual agents work here
- **Reflection loops**: Quality checks during execution

### Design Principles

**Transparency**: Show humans the plan, tool calls, agent interactions

**Control**: Let humans approve plans, override decisions, stop execution

**Feedback**: Capture human input to improve future iterations

**Fallback**: When patterns fail, escalate to human

---

## Implementation Checklist

For each agentic pattern:

**Reflection Pattern**
- [ ] Define quality criteria for self-evaluation
- [ ] Set max iteration limit (prevent infinite loops)
- [ ] Log each reflection cycle for debugging
- [ ] Allow human override of reflection judgment

**Tool Use Pattern**
- [ ] Document available tools with clear descriptions
- [ ] Implement tool access control and permissions
- [ ] Handle tool failures gracefully
- [ ] Show humans which tools were called

**Planning Pattern**
- [ ] Make plan visible before execution
- [ ] Allow plan modification by humans
- [ ] Monitor plan execution progress
- [ ] Support dynamic replanning

**Multi-Agent Pattern**
- [ ] Define each agent's role and expertise
- [ ] Design clear handoff protocols
- [ ] Handle agent failures and conflicts
- [ ] Orchestrate agent coordination logic

---

## Anti-Patterns to Avoid

**❌ Reflection without criteria**: AI critiquing with no clear standards
**Fix**: Define explicit quality criteria

**❌ Tool spam**: AI calling tools excessively or unnecessarily
**Fix**: Gate tool use with relevance check

**❌ Plan rigidity**: Following plan despite changed circumstances
**Fix**: Build in replanning triggers

**❌ Agent chaos**: Too many agents with unclear responsibilities
**Fix**: Start simple, add agents only when needed

**❌ No human oversight**: Fully autonomous with no checkpoints
**Fix**: Insert human review gates at key points

---

## Performance Comparison

Research shows agentic workflows significantly improve performance:

**Code generation** (HumanEval benchmark):
- Zero-shot GPT-4: 67% correct
- Reflection pattern GPT-4: 95% correct
- Improvement: +28 percentage points

**Complex problem-solving**:
- Zero-shot: Solve in one attempt
- Agentic workflow: Iterate 3-5 times
- Result: 2-3x higher success rate

**Cost-Benefit Analysis**:
- Agentic patterns: 3-5x more API calls
- But: Often worth it for quality-critical tasks
- Break-even: When quality improvement exceeds cost increase

---

## When NOT to Use Agentic Patterns

Skip agentic patterns when:

✗ Simple tasks (e.g., "What's the capital of France?")
✗ Time-critical (need instant response)
✗ Cost-constrained (can't afford multiple API calls)
✗ Quality good enough (don't need perfection)
✗ No clear improvement path (reflection won't help)

Use direct single-shot AI for straightforward tasks.

---

## Further Reading

- **Reflection**: Chain-of-Thought Self-Consistency papers
- **Tool Use**: ReAct (Reasoning + Acting) framework
- **Planning**: Plan-and-Execute approaches
- **Multi-Agent**: AutoGEN, MetaGPT frameworks
