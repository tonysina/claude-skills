# VS Variants: Detailed Guide

Read this when you need specific guidance on choosing and applying verbalized sampling variants, or when you need the research-validated prompt structures.

---

## Overview of Variants

The research defines three VS variants. Each targets a different point on the diversity-quality-effort spectrum.

| Variant | Calls | Diversity | Quality | Complexity |
|---------|-------|-----------|---------|------------|
| VS-Standard | 1 per batch | Good (1.6-2.1x over direct) | Comparable to direct | Low |
| VS-CoT | 1 per batch | Highest in creative tasks | Maintains or improves quality in capable models | Medium |
| VS-Multi | Multiple turns | Highest overall | Strongest in synthetic data tasks | Higher |

---

## VS-Standard

**What it does:** Generate k responses with explicit probabilities in a single pass.

**Research-validated prompt structure:**

The paper uses this format for creative writing, open-ended QA, and general tasks:

```
Generate {k} responses to the input prompt. Each response should be 
approximately {target_words} words.

Each response must include:
- text: the response itself
- probability: the estimated probability from 0.0 to 1.0 of this response 
  given the input prompt (relative to the full distribution)
```

**With tail sampling (diversity tuning):**

```
Generate {k} responses to the input prompt.

Each response must include:
- text: the response itself
- probability: the estimated probability from 0.0 to 1.0 of this response 
  given the input prompt (relative to the full distribution)

Randomly sample the responses from the tails of the distribution, with the 
probability of each response below {threshold}.
```

**When to use:**
- Default choice for most tasks
- Quick ideation and brainstorming
- When the user wants a manageable number of options (3-7)
- Simple open-ended questions

**Performance notes:**
- Achieves significant diversity gains over direct prompting across all tested tasks
- Quality remains comparable to direct prompting
- "Explicit probability" format (probability from 0.0 to 1.0 relative to full distribution) performs best empirically for this variant

---

## VS-CoT (Chain of Thought)

**What it does:** Reason step-by-step about the space of possible responses before generating the distribution. The reasoning step helps the model explore dimensions of variation it might otherwise miss.

**Research-validated prompt structure:**

```
Generate {k} responses to the input prompt using chain-of-thought reasoning.
Each response should be approximately {target_words} words.

First, reason step-by-step about:
- What dimensions of variation exist for this task
- What the most common/obvious responses would be
- What less obvious angles, framings, or approaches exist

Then generate {k} responses, each with:
- text: the response itself
- probability: the estimated probability from 0.0 to 1.0 of this response 
  given the input prompt (relative to the full distribution)
```

**When to use:**
- Creative writing (poems, stories, jokes) — this is where VS-CoT shines brightest
- Complex strategic questions with many dimensions
- When quality matters as much as diversity
- Tasks where reasoning about the space of possibilities improves output
- When working with capable models (GPT-4+, Claude Opus/Sonnet, Gemini Pro)

**Performance notes:**
- Achieves the highest diversity scores in creative writing tasks while maintaining or improving quality
- Pushes the Pareto front of the diversity-quality trade-off — more diverse AND higher quality
- The quality improvement is especially pronounced in larger, more capable models
- Smaller models may experience "cognitive burden" from the added complexity — use VS-Standard instead for less capable models

**Why it works better than just listing options:**
The chain-of-thought step forces explicit exploration of the variation space before generation. Without it, the model tends to generate along a single dimension of variation (e.g., all different stories about the same type of character). With reasoning, it discovers multiple axes: genre, tone, setting, narrative structure, perspective — producing genuinely diverse output.

---

## VS-Multi (Multi-Turn)

**What it does:** Generate responses across multiple turns, where each subsequent turn is instructed to produce responses that differ from those already generated.

**Research-validated prompt structure:**

First turn:
```
You will generate a total of {N} responses to the input prompt. Each response 
should be approximately {target_words} words.

First, sample {k} responses.

Each response must include:
- text: the response itself
- confidence: the normalized likelihood score between 0.0 and 1.0 that indicates 
  how representative or typical this response is compared to the full distribution
```

Following turns:
```
Generate {k} alternative responses to the original input prompt. These should 
explore different territory from the responses already generated.

Each response must include:
- text: the response itself
- confidence: the normalized likelihood score between 0.0 and 1.0 that indicates 
  how representative or typical this response is compared to the full distribution
```

**When to use:**
- Need more than 7-10 diverse options (single-pass quality degrades with high k)
- Synthetic data generation — the paper shows this produces the most diverse training data
- Exhaustive coverage of an answer space
- Dialogue simulation across many scenarios
- Any task where maximum diversity across a large set matters more than speed

**Performance notes:**
- Achieves the strongest average accuracy in downstream math tasks when used for synthetic data generation (37.5% vs 30.6% for direct prompting)
- The "confidence" probability format performs best empirically for this variant (vs "explicit probability" for VS-Standard)
- Multi-turn structure naturally prevents the repetition that occurs when generating large batches in a single call
- Works well for dialogue simulation where responses need to cover the full range of human behavior

**Practical notes:**
- Total responses N = k * number_of_turns
- Keep k at 5-7 per turn for best quality
- Each turn sees the context of previous responses, enabling genuine novelty
- If quality degrades in later turns, reduce total turns rather than increasing k

---

## Probability Format

The paper tested seven different ways to express probabilities. Two emerged as best:

| Variant | Best format | Definition |
|---------|------------|------------|
| VS-Standard, VS-CoT | **Explicit probability** | "the estimated probability from 0.0 to 1.0 of this response given the input prompt (relative to the full distribution)" |
| VS-Multi | **Confidence** | "the normalized likelihood score between 0.0 and 1.0 that indicates how representative or typical this response is compared to the full distribution" |

Other tested formats (implicit, relative, percentage, perplexity, negative log-likelihood) all work but show slightly lower performance. When in doubt, use explicit probability.

---

## Combining with Temperature

The research demonstrates that VS is **orthogonal to temperature scaling** — the two improve diversity through different mechanisms and their effects are additive.

- **Temperature** controls how peaked or flat the sampling distribution is at each token generation step
- **VS** controls what the model is optimizing for at the response level (single instance vs. distribution)

Practical implication: if you're generating responses programmatically via API, you can use VS prompting AND set temperature > 0.7 for maximum diversity. The paper used temperature 0.7 and top-p 1.0 across all experiments.

---

## Scaling Behavior

The paper documents an emergent trend: **more capable models benefit more from VS**.

- Large models (GPT-4.1, Gemini-2.5-Pro, Claude-4-Sonnet) gain 1.5-2x more diversity improvement than smaller models
- VS-CoT and VS-Multi can actually *improve* quality in larger models, while simpler methods create "cognitive burden" that degrades quality in smaller ones
- This suggests VS helps unlock latent diversity that capable models have but don't express under standard prompting

**Practical implication:** Use VS-CoT and VS-Multi confidently with top-tier models. Fall back to VS-Standard for smaller or less capable models.
