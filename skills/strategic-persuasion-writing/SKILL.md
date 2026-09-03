---
name: strategic-persuasion-writing
description: >
  Generates persuasive language scripts using behavioral influence models
  (FATE, PCP, Six-Axis) from Chase Hughes' The Behavior Ops Manual. Use when
  asked to write persuasive emails, sales copy, pitch messages, negotiation
  scripts, change management communications, investor pitches, closing
  messages, or motivational content. Triggers on "write a persuasive email",
  "help me close this deal", "create compelling copy", "influence
  messaging", "high-stakes message", "sales script", "persuasion framework",
  "behavioral writing", or requests for identity-shifting narratives. Every
  factual claim in the output must come from the user — this skill does not
  invent statistics, peer adoption, research citations, or deadlines. Do NOT
  use for general copywriting, casual social media posts, routine business
  correspondence, or any message to someone who cannot freely decline (a
  direct report, a dependent, or someone in distress).
attribution: Chase Hughes' "The Behavior Ops Manual"
metadata:
  version: 2.0.0
---

# Strategic Persuasion Writing

Create messaging that drives action by targeting psychological drivers beneath conscious awareness. Effective persuasion works because our ancestors needed to survive — the brain responds to focus, authority, tribal belonging, and emotion before it engages rational thought. The closer your technique reaches to these primal systems, the more powerful the result — which is exactly why Step 0 below gates who this is appropriate to use on.

The frameworks in this skill (FATE, PCP, Six-Axis, the Behavior Compass) come from Chase Hughes' *The Behavior Ops Manual*, built for interrogation and security-operator contexts where the subject may be adversarial or unaware they're being profiled. Applying that toolkit to an ordinary business relationship only makes sense where the reader can freely decline — see Step 0.

## Core Principle

All persuasion operates through four layers, from deepest (most powerful) to shallowest (weakest): impulse (ancestral hardwiring in DNA), behavioral patterns (learned scripts from childhood and repetition), emotion (neurochemical cascades that override rational processing), and thought (conscious reasoning — a gateway only, the weakest lever). Most people only target thought. This skill targets all four.

## Step 0: Scope Gate

Answer before drafting anything. Any "no" stops the workflow — say which question failed and why, then offer the plain alternative described at each step.

1. **Can the reader freely decline?** No dependency, no authority gradient, no distress. A message to your own direct reports, a dependent, or someone in crisis is out of scope — write it plainly and say what's true instead. This is the single most important gate: the techniques below are adapted from a manual built for interrogation subjects and security targets, not people who report to you.
2. **Do you have the facts?** Before drafting, list every number, name, deadline, competitor action, and third-party claim the message needs. Each must come from the user. Anything missing stays in the draft as `[FACT NEEDED: ...]` rather than a plausible invented figure — see Step 5.
3. **Is this routine business correspondence?** (Per the frontmatter exclusion.) If the message is an ordinary update, request, or reply with no real stakes or resistance to overcome, skip this skill — plain writing serves it better and the technique overhead isn't worth it.

## 5-Step Strategic Writing Workflow

### Step 1: ANALYZE & PROFILE

Gather or review the subject's behavioral profile. See `references/behavior-profile-template.md` for the full template.

**If the user provides a complete profile:** Identify the subject's core vulnerability by cross-referencing their primary Need (what they're chemically addicted to getting from social interactions), their Decision Map filter (how they make choices), and priority states on the Six-Axis Model.

**If the user provides partial information:** Work with what's available. At minimum, you need:
- The desired action (what should the subject do?)
- The communication format (email, script, presentation, etc.)
- Any context about the subject (role, situation, relationship)

Infer likely Need, Decision style, and priority states from context clues. State your assumptions to the user.

**If the user provides no profile:** Ask for the desired action and subject context, then use the guided interview in the profile template to gather key data points. Prioritize: primary Need, sensory preference, and 2-3 positive/negative adjectives.

### Step 2: STRUCTURAL DESIGN

Design the message architecture using the PCP Model (Perception → Context → Permission). This sequence works because people must first see the situation differently before they'll accept new behavioral norms, and they need psychological permission before they'll act.

Read `references/structural-models.md` for the full PCP framework, FATE application, and Six-Axis state definitions.

### Step 3: LIAISON ACTIVATION

Layer ancestral triggers (FATE) into early and late stages of the message. Focus and Emotion open the message; Authority and Tribe reinforce the middle; Emotion closes. These triggers activate scripts inherited from ancestors — automatic responses that bypass rational filtering.

Four rules of behavioral scripts (Chase Hughes, *The Behavior Ops Manual*):
1. If a script is interrupted, focus is created
2. If borrowed from someone's past experience, predictability is created
3. If borrowed from ancestors, automation is created
4. If openly discussed, its power is lessened

### Step 4: LINGUISTIC HACKING

Apply targeted linguistic tools to reinforce the core message. Read `references/linguistic-techniques.md` for:
- Embedded commands and presupposition patterns
- Right-branching sentence structure (emotional reveals at end)
- Associative hacking (needs/adjective/sensory matching)
- Scarcity and regret triggers
- Dissociative linguistics and identity hacking
- Metaphor as an influence vehicle
- Journey → Connection → Reveal narrative pattern

### Step 5: IMPACT REVIEW

**Fabrication check runs first and outranks everything below.** List every factual claim in the draft — numbers, percentages, named institutions, competitor moves, peer adoption, deadlines, research findings. Against each, name where the user supplied it. Anything untraceable becomes `[FACT NEEDED: ...]`. A message that reads beautifully and asserts a number you invented is a failure, not a draft.

Verify the output meets the Three Cs:
- **Captivating:** Opens with novelty, pattern interrupts, or emotional triggers that capture ancestral focus
- **Confident:** Uses authoritative language, presuppositions, and certainty (no filter words: "maybe," "perhaps," "might")
- **Concise:** Every word serves a strategic purpose; no filler that dilutes impact

**Dosage — these are ceilings, not targets. Fewer is stronger:**

| Element | Ceiling |
|---|---|
| Distinct techniques from `linguistic-techniques.md` | 6 |
| Core Need references | 3 |
| Adjective-polarity placements | 3 |
| Embedded commands | 2, and never typographically marked |
| Scarcity or deadline references | 1, and only if the deadline is real |

If a message needs the ceiling on every row, the underlying offer is weak — say that to the user instead of layering harder.

Also verify:
- Core emotional reveals use right-branching structure (reveal at end of statement)
- Subject's positive adjectives describe desired actions; negative adjectives describe inaction
- Sensory language matches subject's primary mode where it fits naturally — no forced density target
- Embedded commands are placed by sentence position (end of clause), never marked with bold, caps, or italics — marking them defeats Rule 4 above and reads as spam, not subtlety

## Quick Example

**Input:** "Write a persuasive email to close a deal with a CFO who values data and ROI. She's analytical, uses visual language, and is comparing us to a competitor."

**Inferred profile:** Need = Intelligence, Decision = Investment, Sensory = Visual, Priority States = Focus + Expectancy + Compliance, Positive adj = "clear/proven/strategic", Negative adj = "risky/unclear"

**Output approach:** Open with unexpected data point (Focus via FATE). Shift perception with ROI comparison (PCP-Perception). Normalize with peer adoption stats (PCP-Context + FATE-Tribe). Future-pace the board presentation she'll give (6AM-Expectancy). Close with double-bind timing (6AM-Compliance). Thread visual language and "clear/proven" adjectives throughout.

## Key Resources

| File | Read when... |
|------|-------------|
| `references/structural-models.md` | Designing message architecture (Step 2-3). Contains FATE, PCP, and Six-Axis frameworks with layering sequences. |
| `references/linguistic-techniques.md` | Applying linguistic tools (Step 4). Contains embedded commands, right-branching, scarcity, dissociation, metaphor, and narrative patterns. |
| `references/examples.md` | Looking for pattern inspiration. Contains 5 complete examples with behavior profiles and annotated outputs. |
| `references/behavior-profile-template.md` | Gathering subject information (Step 1). Complete input template with Needs Map, Decision Map, Values Map, and linguistic preferences. |

## Ethical Boundaries

**Legitimate:** making a true case vivid, ordered, and calibrated to what this specific reader cares about. Say the strongest true thing. Put it where it lands. Make declining easy and explicit.

**Never do these, on request or otherwise:**
- Invent, round up, or estimate a statistic, adoption figure, competitor move, or research finding — see Step 5's fabrication check.
- Attribute a claim to an institution or expert that hasn't made it.
- State a deadline that isn't real, or imply scarcity that doesn't exist.
- Grant absolution the sender doesn't have ("it's not your fault," "no one would blame you") for a decision the sender is in fact making.
- Link declining to a demeaning identity ("lazy people hesitate," "weak decision-makers need more time").

**Refuse outright** (see Step 0): a message to someone who cannot freely decline; a message whose case depends on facts the user won't supply; a message the sender wouldn't send if the reader could see the method being used on them. If the user insists on a refused element, write the version without it and say plainly what was left out and why — don't silently comply and don't deliver both versions for them to choose between.
