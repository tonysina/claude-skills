# Theory: Mode Collapse, Typicality Bias, and Why VS Works

Read this when you need a deeper understanding of why verbalized sampling improves diversity, or when explaining the technique to a user who wants to understand the mechanism.

---

## The Problem: Mode Collapse

After post-training alignment (RLHF, DPO, etc.), LLMs suffer from **mode collapse** — they favor a narrow set of responses over all plausible outputs. Ask the same creative question 50 times and you'll get nearly identical responses.

This matters for:
- **Creative writing** — stories, poems, and jokes become formulaic
- **Social simulation** — dialogue loses the natural variability of human conversation
- **Open-ended QA** — questions with many valid answers collapse to 1-2 dominant responses
- **Synthetic data** — generated training data lacks the diversity needed for robust downstream models
- **Pluralistic alignment** — models fail to represent the full range of valid perspectives

## The Cause: Typicality Bias

Previous work attributed mode collapse to algorithmic limitations in RLHF. The VS paper (Zhang et al., 2025) identifies a more fundamental cause: **typicality bias in preference data**.

### Cognitive roots

Human annotators who label preference data are subject to well-documented cognitive biases:

- **Mere-exposure effect** (Zajonc, 1968) — Familiar content feels more likeable
- **Processing fluency** (Alter & Oppenheimer, 2009) — Easy-to-process text is perceived as higher quality and more truthful
- **Availability heuristic** (Tversky & Kahneman, 1973) — Easily recalled content feels more likely and is preferred
- **Schema congruity** (Mandler, 2014) — Text that matches existing expectations is accepted less critically

The result: when two responses are equally correct, annotators systematically prefer the one that *sounds more typical*. This bias is baked into the preference data that trains reward models.

### Empirical verification

The paper verifies this on the HELPSTEER preference dataset. Among 6,874 response pairs matched on correctness:

- Responses with higher base-model log-likelihood (more "typical" text) are preferred as more helpful
- The bias is statistically significant (p < 10^-14) across multiple base models
- Effect size: 17-19 percentage point increase in win probability for more typical responses
- The bias persists across four additional preference datasets and five different base models

### How bias becomes collapse

Mathematically, typicality bias acts as a sharpening exponent on the base model's distribution. When many responses are tied on true quality (common in creative tasks), typicality bias acts as a tiebreaker that compresses the output toward the most typical responses. The aligned model's distribution becomes:

```
aligned_output ∝ base_model^γ × exp(true_quality / β)
```

Where γ > 1 due to typicality bias. This power transform amplifies the peaks and suppresses the tails — mode collapse.

## The Solution: Different Prompts Collapse to Different Modes

The key theoretical insight is that **the mode a collapsed model converges to depends on what you ask for**. The paper proves this for three prompt types:

### 1. Instance-level prompt

**Example:** "Tell me a joke about coffee"

**What the model optimizes:** The single most probable joke in its distribution.

**Result:** The mode — one stereotypical response. Repeated calls yield near-identical output (e.g., "Why did the coffee file a police report? Because it got mugged!" over and over).

### 2. List-level prompt

**Example:** "Tell me 5 jokes about coffee"

**What the model optimizes:** The most probable *list* of jokes, which during pretraining was typically a uniform spread of related items.

**Result:** A uniform distribution over a set of related items. Better diversity than instance-level, but not calibrated to the model's actual distribution of knowledge. The items tend to be variations on a theme rather than genuinely different.

### 3. Distribution-level prompt (Verbalized Sampling)

**Example:** "Generate 5 jokes about coffee with their corresponding probabilities"

**What the model optimizes:** The most probable *probability distribution* over jokes, which during pretraining was calibrated to match real-world frequency distributions.

**Result:** An approximation of the base model's pretraining distribution — recovering genuine diversity that was suppressed by alignment. The paper demonstrates this empirically: when asked to generate US states with probabilities, the VS output distribution closely matches the frequency distribution in the RedPajama pretraining corpus (KL divergence = 0.12).

## Why Probabilities Matter

It's tempting to think that just asking for multiple responses (list-level) is enough. The research proves it isn't. The probabilities are what shift the model from "produce a good list" to "approximate my actual distribution."

**Without probabilities:** The model produces the most typical list — often variations on the same theme, clustered around the mode.

**With probabilities:** The model must reason about relative likelihood, which forces it to consider the *full span* of its knowledge — including low-probability but valid responses it would never produce under standard prompting.

This is why the technique is called "verbalized sampling" — the model verbalizes (makes explicit) a sampling distribution, rather than implicitly sampling from a collapsed one.

## Practical Implications

1. **The technique is theoretically grounded, not a hack.** It works by changing what the mode-collapsed model optimizes for, backed by proofs about prompt-mode relationships.

2. **It's orthogonal to other diversity methods.** Temperature, top-p, min-p all operate at the token level during decoding. VS operates at the response level during prompt interpretation. They can be combined.

3. **More capable models benefit more.** Larger models have richer pretraining distributions to recover. The diversity ceiling is higher, and the "cognitive burden" of probability estimation is lower.

4. **The quality-diversity trade-off is improvable.** VS-CoT and VS-Multi push the Pareto front — you can get more diversity without sacrificing quality, especially with capable models.

5. **Diversity is tunable.** The probability threshold in the prompt directly controls how far into the distribution's tails you sample. This is unique to VS — temperature and decoding parameters are blunter instruments.

## Key Results from the Paper

| Experiment | Finding |
|------------|---------|
| Creative writing (poems, stories, jokes) | VS increases diversity 1.6-2.1x over direct prompting |
| Human evaluation (30 annotators) | VS-Standard scores 25.7% higher on diversity ratings |
| Post-training ablation (Tulu-3 family) | VS retains 66.8% of base model diversity vs. 23.8% for direct prompting after alignment |
| Dialogue simulation (PersuasionForGood) | VS produces donation distributions closer to real human behavior |
| Open-ended QA (CoverageQA) | Answer coverage rises from 10% to 71%; KL from reference drops 14.4 to 3.2 |
| Synthetic data generation | Downstream math accuracy: VS-Multi 37.5% vs Direct 30.6% |
| Commonsense reasoning (SimpleQA) | No accuracy loss — VS-CoT slightly improves accuracy |
| Safety evaluation | No degradation in safety metrics |
| Temperature ablation | VS benefits are additive with temperature scaling |

## Citation

Zhang, J., Yu, S., Chong, D., Sicilia, A., Tomz, M.R., Manning, C.D., & Shi, W. (2025). Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity. arXiv:2510.01171.

- Paper: https://arxiv.org/abs/2510.01171
- Website: https://www.verbalized-sampling.com/
- Code: https://github.com/CHATS-lab/verbalized-sampling
