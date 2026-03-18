---
name: beyond-obvious
description: >
  Technique to generate diverse options beyond predictable defaults using
  verbalized sampling. Use when users want varied alternatives, different
  approaches, creative ideas, or a spectrum from mainstream to unconventional.
  Triggers include "give me options," "what are different ways," "alternatives,"
  "brainstorm," "explore approaches," "beyond the obvious," "creative ideas,"
  "diverse responses," "avoid the generic," "verbalized sampling," "mode
  collapse," or any request where showing range from common to uncommon adds
  value. Also use for synthetic data generation, dialogue simulation, or
  open-ended questions with many valid answers. Do NOT use for factual questions
  with one correct answer, math, or debugging.
metadata:
  version: 1.0.0
---

# Beyond Obvious — Verbalized Sampling for Diverse Output

Generate diverse options across the full probability spectrum rather than defaulting to the single most predictable response. Based on the Verbalized Sampling (VS) technique from Zhang et al. (2025).

## Why This Works

LLMs tend to collapse to a narrow set of "safe," stereotypical responses — a phenomenon called **mode collapse**. This happens because human preference training (RLHF) amplifies **typicality bias**: annotators systematically prefer familiar-sounding text, which sharpens the model's output distribution toward a few dominant responses.

The key insight is that **different types of prompts collapse to different modes**:

1. **Instance-level prompt** ("Tell me a joke about coffee") — collapses to the single most typical response. Repeated calls return near-identical output.
2. **List-level prompt** ("Tell me 5 jokes about coffee") — produces a list, but defaults to a uniform spread of related items without calibrated diversity.
3. **Distribution-level prompt** ("Generate 5 jokes about coffee with their corresponding probabilities") — recovers an approximation of the model's full pretraining distribution, restoring genuine diversity.

By asking for responses *with probabilities*, you shift what the model optimizes for: instead of producing the most typical single answer, it produces a calibrated distribution that spans common to uncommon responses. This is the mechanism that makes verbalized sampling principled rather than just a prompting trick.

## When to Use This Technique

**Use when:**
- Multiple valid responses exist (creative, strategic, or open-ended tasks)
- User wants options, alternatives, or variety
- Avoiding predictable outputs matters
- Exploring different angles, approaches, or framings
- Brainstorming or ideation
- Simulating realistic human variation in dialogue
- Generating diverse synthetic data
- Answering open-ended questions with many valid answers

**Common triggers:**
- "Give me some options for..."
- "What are different ways to..."
- "Brainstorm ideas for..."
- "Explore different approaches to..."
- "What are the alternatives?"
- "Give me varied/diverse..."
- "Beyond the obvious..."
- "Avoid the generic..."
- Any request where range from common to creative adds value

**Do NOT use when:**
- One correct answer exists (factual questions, math, debugging)
- User explicitly wants a single best recommendation
- Speed matters more than diversity

## The Technique: Three Variants

Verbalized sampling has three variants. Choose based on the task.

### VS-Standard (Default)

Generate k responses with explicit probabilities in a single pass. This is the simplest and fastest variant.

**Internal process:** For each response, estimate the probability that this response would be generated relative to the full distribution of possible responses. Produce responses spanning from common (higher probability) to uncommon (lower probability).

**Best for:** Most tasks — quick ideation, brainstorming, generating alternatives, any situation where you need a spread of options efficiently.

### VS-CoT (Highest Quality + Diversity)

Think step-by-step first — reason about the dimensions of variation, what makes responses different from each other, what the obvious answers are and what lies beyond them — then generate the distribution.

**Internal process:** First reason about the space of possible responses: what axes of variation exist? What would most people say? What's genuinely different? Then generate k responses with probabilities informed by this reasoning.

**Best for:** Creative writing, complex strategic questions, tasks where quality matters as much as diversity. The paper shows VS-CoT pushes the Pareto front of the diversity-quality trade-off, achieving the highest diversity while maintaining or improving quality — especially with capable models.

### VS-Multi (Maximum Diversity)

Multi-turn generation: produce k responses with probabilities, then generate additional rounds of k responses that deliberately differ from previous ones.

**Internal process:** Generate a first set of k responses with probabilities. Then, considering what you've already generated, produce another set of k responses that explore different territory — different angles, tones, framings, or creative directions not yet covered.

**Best for:** Synthetic data generation, exhaustive exploration, comprehensive coverage of an answer space, any task where you need maximum diversity across many options. The paper shows VS-Multi achieves the strongest average performance in synthetic data generation tasks.

### Choosing a Variant

| Situation | Use | Why |
|-----------|-----|-----|
| Quick brainstorm, simple ideation | VS-Standard | Fast, good diversity |
| Creative writing, complex strategy | VS-CoT | Best diversity-quality balance |
| Need 10+ diverse options | VS-Multi | Prevents repetition across batches |
| Synthetic data, exhaustive coverage | VS-Multi | Maximum diversity |
| User asks for "a few ideas" | VS-Standard | Matches the lightweight request |
| User asks for "really creative/unusual ideas" | VS-CoT with tail sampling | Combines reasoning with low-probability filtering |

## Diversity Tuning

Unlike temperature (which is a blunt instrument), verbalized sampling offers **fine-grained diversity control** through the probability threshold — a value you set in your internal process that filters which part of the distribution you sample from.

| Threshold | Diversity Level | Use When |
|-----------|----------------|----------|
| Full distribution (no filter) | Moderate | Balanced overview of common and uncommon options |
| Below 0.10 (10%) | Good | Default for most creative tasks — filters out the most obvious responses |
| Below 0.01 (1%) | High | User wants genuinely unconventional ideas |
| Below 0.001 (0.1%) | Maximum | Pushing boundaries; may trade some coherence for novelty |

The research demonstrates that diversity increases monotonically as the threshold decreases — this is a continuous dial, not a binary switch.

**Important:** Verbalized sampling is orthogonal to temperature. The two work through different mechanisms and can be combined. VS controls *which part of the distribution* you sample from; temperature controls *how sharp or flat* the distribution is. Using both together pushes the diversity-quality trade-off further than either alone.

## Presenting Results to Users

**Acknowledge the technique naturally when helpful:**
- "I'll give you options across the spectrum from mainstream to creative"
- "Here are 5 approaches ranging from common to unconventional"
- Brief mentions keep users informed without being heavy-handed

**Show probabilities in readable formats:**
- Parenthetically: "HIPAA-compliant data visualization dashboards (8%)"
- As a simple table with a probability column
- With contextual grouping: "Common approaches:" / "Creative alternatives:"

**Make diversity visible:**
Probability percentages signal the spectrum from high-probability (common, safe) to low-probability (creative, unconventional). Users can see where each option falls.

**Keep formatting natural:**
Present options in plain language — prose, simple lists, or tables. Avoid XML tags or JSON formatting unless the user specifically requests structured data.

## Parameters

| Parameter | Default | Range | Notes |
|-----------|---------|-------|-------|
| Number of options (k) | 5 | 3-20 | Higher k = broader coverage. Quality may degrade above 7-10 in a single pass; use VS-Multi for more. |
| Probability threshold | 0.10 | 1.0 to 0.001 | Lower = more unconventional. No filter (full distribution) for balanced spread. |
| Variant | VS-Standard | Standard / CoT / Multi | Match to task complexity and diversity needs. |

## Key Principles

1. **Probability verbalization is the mechanism** — Asking for responses *with probabilities* is what shifts the model from mode-collapsed to distribution-level output. Simply listing options doesn't achieve the same diversity. This is the core finding of the research.
2. **Diversity tuning is continuous** — The probability threshold is a dial from conservative to creative. Adjust it to the task rather than treating it as on/off.
3. **Orthogonal to temperature** — VS and temperature work through different mechanisms. Combine them for maximum effect.
4. **Preserves accuracy and safety** — The research confirms VS does not increase hallucination or unsafe outputs. Factual accuracy on commonsense reasoning tasks remains equivalent to direct prompting.
5. **Larger models benefit more** — More capable models gain 1.5-2x more diversity improvement from VS, and the CoT/Multi variants can actually *improve* quality (not just diversity) in strong models.
6. **Natural presentation matters** — Show probabilities in readable formats (percentages, contextual grouping) rather than code-like structures.

## Validated Domains

The research measures VS improvements across specific task types:

| Domain | Key Finding |
|--------|-------------|
| Creative writing (poems, stories, jokes) | 1.6-2.1x diversity increase; +25.7% human evaluation scores |
| Dialogue simulation | Donation distributions closer to real human behavior; models approach fine-tuned performance |
| Open-ended QA (many valid answers) | KL divergence from reference drops from 14.4 to 3.2; answer coverage rises from 10% to 71% |
| Synthetic data generation | Downstream math accuracy improves from 30.6% (direct) to 37.5% (VS-Multi) |
| Commonsense reasoning | No accuracy loss; VS-CoT slightly improves accuracy |

## Examples and References

- See `references/examples.md` for practical examples across use cases, showing how to present results naturally
- See `references/variants.md` for detailed guidance on each VS variant, including the prompt templates validated in the research
- See `references/theory.md` for deeper explanation of mode collapse, typicality bias, and the theoretical foundation

## Citation

Based on: Zhang et al. (2025) "Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity" — https://arxiv.org/abs/2510.01171 | https://www.verbalized-sampling.com/