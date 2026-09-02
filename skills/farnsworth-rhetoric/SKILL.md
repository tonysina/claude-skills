---
name: farnsworth-rhetoric
description: |
  Apply classical rhetorical figures to make existing writing more memorable and
  persuasive, at the sentence and paragraph level. Based on Ward Farnsworth's
  Classical English Rhetoric and Classical English Style. Diagnoses where a piece
  is flat, applies figures under a strict dosage budget, and checks that craft did
  not inflate the claim.

  Triggers: "make this memorable", "strengthen this", "make this land", "make this
  persuasive", "apply rhetoric", "craft this message", "sharpen this line", "this
  ending is flat", "speech writing", "key message", "tagline", "farnsworth"

  Do NOT use for: generating a message from scratch (use strategic-persuasion-writing),
  deck structure (use good-presentations), message architecture (use start-with-why),
  removing AI tells (use humanizer), narrative structure (use human-narrative),
  technical documentation, process instructions, data reporting, or legal language.
metadata:
  version: 1.1.1
---

# Farnsworth Rhetoric: Memorable Writing

Apply classical figures to writing that already exists. This skill does not generate
messages and does not restructure arguments. It works on the sentence and the
paragraph — word choice, parallel structure, and where the emphasis falls.

**Figures are expensive.** Each one draws attention to itself, and attention spent on
the sentence is attention not spent on the point. Most text needs one figure. Some
needs none. The dosage budget below is a hard constraint, not a suggestion.

## Workflow position

Run this skill **last**.

```
Long-form:   human-narrative → humanizer → farnsworth-rhetoric
Short-form:  humanizer → farnsworth-rhetoric
```

Figures applied before humanizer get stripped by humanizer. Figures applied to text
that still carries AI tells amplify those tells — a rhetorical flourish on top of
promotional prose reads worse than the promotional prose alone.

This skill's output is designed to pass humanizer. If you re-run humanizer afterward
and it flags something, check "Forbidden constructions" below. If the construction
isn't on that list, the figure is intentional — leave it.

## How to use this skill

1. Read the whole piece before changing anything. Find the one sentence that carries it.
2. Triage: set the context, the register, and the figure budget (Step 1 below).
3. Diagnose flatness — where does the prose fail to land? Endings first; they matter most.
4. Check each candidate figure's **trigger condition**. No trigger, no figure.
5. Apply within budget. Work backward from the ending.
6. Run the claim check and the ear test. Both are mandatory.
7. Report what you changed and what you deliberately left alone.

When one line carries the whole piece — a tagline, a closing sentence, a headline —
chain `beyond-obvious` to generate 3–5 distinct rhetorical treatments before choosing.
Applying the first figure that fits is the most common failure mode of this skill.

Load `references/figures.md` for figures not covered here: anadiplosis, symploce,
asyndeton and polysyndeton, epizeuxis, praeteritio, litotes, and strategic passive
voice. Load it when the core figures below don't fit, or when the user names a
figure by its classical name.

### Use cases

**Diagnose only:** User asks "why does this fall flat?" or "where could this be
sharper?" Report where the prose loses energy, name the figure each spot would take,
and give the budget. Don't rewrite until asked.

**Strengthen:** User says "make this land" or "farnsworth this." Triage, apply within
budget, return the revised text plus a change note naming each figure and the trigger
that justified it.

**Single line:** User wants one sentence sharpened — a tagline, a closing line, a slide
title. Chain `beyond-obvious` for options, present 3–5 treatments with the figure named,
and recommend one. Budget is 1 figure. Run the claim check on every treatment before
presenting it; a treatment that fails is withdrawn, not offered with a caveat. Output
shape: the treatments list, each with its figure named, then one change note for the
recommended treatment only.

---

## Step 1: Triage

Answer three questions before touching the text.

**Q1: What is the register?**

| Register | Approach |
|---|---|
| Speech, keynote, closing argument | Full budget. The ear is the only channel. |
| Thought leadership, executive summary, engineering blog, post-mortem | Half budget. Figures at the open and close only. |
| Business email, internal memo | 1 figure maximum, at the ask. |
| Slide title, subject line, tagline | 1 figure, or none. Compression usually beats ornament. |
| Technical, legal, process, data | **Stop.** Out of scope for figures; this is the description's "Do NOT use for" list. If invoked anyway, say so and do diction work only (free, below). |

**Q2: What is the figure budget?**

Count the words. Do not estimate them; the budget tiers have hard edges.

| Length | Max figures |
|---|---|
| >600 words | 1 per 150 words, 6 total |
| 300–600 words | 3 |
| <300 words | 1 |

Additional hard caps:
- Never two figures from the same family in one paragraph.
- Never the same figure twice in one piece. One anaphora run counts as one figure, not three.
- Zero is a valid budget spend. Say so if the text doesn't need a figure.

**Q3: What is free?**

Diction work does **not** count against the budget, because it removes ornament rather
than adding it. Apply it everywhere, always:

- **Saxon default.** Trigger: three or more Latinate polysyllables in one sentence, or a
  chain of abstract nouns. Move: turn nominalizations back into verbs. "The
  implementation of our transformation initiative will require" → "We will have to."
- **Saxon finish.** Trigger: a sentence or paragraph ends on a Latinate polysyllable
  (`-tion`, `-ment`, `-ity`, `-ance`, `-ize`). Move: rebuild so the last word is a
  stressed Saxon monosyllable. The last word rings longest.
  Strong finishers: work, fight, stand, fall, hate, love, live, die, win, lose, end,
  start, break, build, cost, pay, lost, gone.

Holmes: "...freedom for the thought that we hate." Four Latinate-free words after a
formal legal buildup. "Hate" is the punch, and it's the last thing you hear.

---

## Master principle: contrast

**The ear detects differences, not qualities.** A Saxon word lands because Latinate
words surround it. A short sentence hits because long ones preceded it. Every figure
below is a way of engineering a difference.

This has a practical consequence: a figure with nothing to push against does nothing.
Six punchy Saxon sentences in a row are as flat as six Latinate ones. If you cannot
name what the figure contrasts with, don't apply it.

---

## Core figures

Each figure has a **trigger** (the detectable condition that licenses it), a **move**,
and a **cap**. Skip any figure whose trigger is absent. Do not go looking for triggers.

### Antithesis — the figure of contrast

**Trigger:** You can name what the thing is *not*, and both poles are real.

**Move:** Put the two poles in parallel grammatical frames, adjacent, with equal weight.

**Swap test:** Reverse the poles. If the sentence still makes sense, the contrast is
fake — you have two unrelated statements in a parallel costume. Cut it.

Franklin: "We must indeed all hang together, or most assuredly we shall all hang
separately."

Before: "Our pricing is competitive and our support is a differentiator."
After: "Our competitors win on price. We win after the sale."

**Not the same as negative parallelism.** "It's not just X, it's Y" asserts one pole and
dismisses a straw pole — humanizer flags it (`NEG-PARALLEL`) because the dismissed pole was never a
real option. Antithesis gives both poles weight and lets them stand.

**Cap:** 1 per three paragraphs.

---

### Isocolon — parallel members of equal shape

**Trigger:** Two to four items that carry *equal weight* and can take *equal grammatical
shape*. Three is the number that resolves; two feels open, four feels like a list.

**Move:** Match clause length and structure so the members scan alike.

**Load-bearing test — required.** An isocolon earns its place only if each member adds
something the others don't. Ask: could I cut this to one member and lose information?
If no, cut it to one. Interchangeable adjectives and padded parallel phrases are
humanizer's decorative triad (`RULE-OF-3`), not a figure. humanizer states the same
load-bearing test from its side, so the two skills agree on which triads survive.

Fails the test: "We value innovation, collaboration, integrity, excellence, and growth."
(Five interchangeable abstractions. Cut to what you actually do.)
Passes: "We came, we saw, we conquered." (Three distinct events, in sequence, each
required.)

**Cap:** 1 per piece short-form, 1 per section long-form.

---

### Antimetabole — words reversed

**Trigger — test all three:**
1. **"They have it backwards."** The relationship is inverted.
2. **"And vice versa."** The situation is genuinely reciprocal.
3. **"It's the other way around."** There's a mismatch to correct.

**Move:** Repeat the same words in reverse order. A-B-B-A, with word identity.

Kennedy: "Ask not what your country can do for you — ask what you can do for your
country." (country → you → you → country)

Before: "Don't let work define your life. Make sure your life shapes your work."
After: "Don't let your work define your life. Let your life define your work."

**Antimetabole vs. chiasmus:** Antimetabole reverses the *same words* and is therefore
checkable — you can verify it mechanically. Chiasmus inverts parallel *structure* without
word repetition and is much harder to land. **Default to antimetabole.** Attempt chiasmus
only when the antimetabole is unavailable and the inversion is genuinely worth having.

**Cap:** 1 per piece, maximum. Most pieces should have none. This is the most
over-attempted figure in the catalog — if the trigger tests don't fire cleanly, the
result will read as a fortune cookie.

---

### Hypophora — ask, then answer

**Trigger:** The reader has an objection or question you are about to address anyway.

**Move:** Ask it in their words. Answer it in the next sentence.

**Why it works in business writing:** It names the objection instead of routing around
it, which is why it reads as confidence rather than ornament. It also turns the reader
from evaluator into participant.

Before: "There are cost considerations associated with the migration timeline."
After: "So why not wait a year? Because the license renews in March, and renewing locks
us in for three more."

**Anti-patterns:** Never ask a question you don't answer immediately. Never announce it
("You might be wondering...") — humanizer flags that as `SIGNPOSTING`. Just ask.

**Cap:** 2 per piece. The most under-used figure in business writing; spend here first.

---

### Erotema — the rhetorical question

**Trigger:** The answer is obvious, and the obviousness is the point.

**Move:** Ask. Don't answer.

**Cap:** 1 per piece, and prefer hypophora instead. In business writing an unanswered
question often reads as evasion or as a rhetorical move the reader has seen too often.
Use it when the audience already agrees and you want them to say so to themselves.

---

### Anaphora — repeated opening

**Trigger:** Three or more parallel commitments or actions sharing one subject, at the
emotional peak of the piece.

**Move:** Repeat the opening words verbatim across consecutive clauses.

Churchill: "We shall fight on the beaches, we shall fight on the landing grounds, we
shall fight in the fields."

**Cap:** **1 run per piece, at the peak. Never in anything under 300 words.** Anaphora in
an executive summary or an email reads as speechifying, because it is. This is the figure
most likely to blow the whole budget in one paragraph — the run is one figure, but a
second run in the same piece is a tell, not a technique.

---

### Epistrophe — repeated ending

**Trigger:** One word or phrase is the piece's actual subject and can fall naturally at
the end of consecutive clauses.

**Move:** End consecutive clauses on it. The repeated word lands in the most memorable
position.

Lincoln: "government of the people, by the people, for the people."

**Cap:** 1 run per piece. Do not combine with anaphora in the same paragraph — the two
compete for the same attention, and the ear reads the collision as a stutter. Farnsworth's
shift from one to the other across a longer passage (symploce) is covered in
`references/figures.md`.

---

## Forbidden constructions

These are figures the model reaches for by default, and each one is on humanizer's flag
list. Producing them makes this skill actively counterproductive.

| Do not produce | humanizer flag | Use instead |
|---|---|---|
| "not just X, it's Y" / "not only X but Y" / "X is more than Y. It's Z." | `NEG-PARALLEL` | Antithesis, both poles real |
| Three interchangeable adjectives or padded parallel phrases | `RULE-OF-3` | Isocolon that passes the load-bearing test, or one member |
| "Put simply:" / "In other words:" / "What this means is" | `DIDACTIC` | Juxtapose the two sentences with no transition |
| "You might be wondering..." / "Let's explore" | `SIGNPOSTING` | Ask the question outright (hypophora) |
| Three or more em dashes in close proximity | `EM-DASH` | Commas, colons, periods |
| "The real question is" / "At its core" / "Fundamentally" | `INFLATION` (authority tropes) | Ask the real question, or state the point |
| "we will lead" / "the future is bright" / "poised for growth" closers | `GENERIC-CLOSER` | A concrete claim, with a Saxon finish |

Flags are humanizer's stable pattern IDs (see the table at the top of its SKILL.md), not
display numbers, which can change between humanizer versions.

The general rule: a figure that could be dropped into any piece about any topic is not a
figure, it's filler with parallel structure.

---

## Guardrails

Both checks are mandatory before returning revised text.

### Claim check

Figures compress, and compression eats qualifiers. Compare the claims in your revision
against the original:

1. Did a hedge become a promise? ("an opportunity to improve" → "we will lead")
2. Did a qualifier vanish? ("in most cases," "for enterprise accounts," "after year two")
3. Did a number, date, or scope get dropped for rhythm?
4. Did an attribution disappear?

If yes to any: restore it, even at the cost of the figure. **Flat prose that states the
claim correctly beats a memorable sentence that overstates it.** If the original claim was
vague and you cannot sharpen it without inventing support, say so and leave it — don't
manufacture a concrete detail to give the figure something to land on.

### Ear test

Read the last five words of each paragraph aloud. Two checks:

- **Stress.** Does the final syllable land on a stress? Latinate endings trail off;
  Saxon monosyllables land.
- **Breath.** Does the closing clause fit in one breath? If it needs a second, split it
  or cut it.

Farnsworth's method is auditory throughout. A figure that only works on the page isn't
working.

---

## Revision checklist

1. **Budget set?** Length and register both checked, number written down.
2. **Endings.** Does each paragraph finish on a stressed Saxon word?
3. **Latinate pileups.** Broken up with verbs, not synonyms?
4. **Key claim.** Stated once abstractly, once concretely — with no transition phrase between?
5. **Contrast.** Does every figure have something to push against?
6. **Triggers.** Can you name the trigger condition for each figure you applied?
7. **Budget respected?** Count the figures. Over budget means cut, not justify.
8. **Forbidden constructions.** None present?
9. **Claim check.** Hedges, qualifiers, numbers, attributions all intact?
10. **Ear test.** Read the closings aloud.

---

## Output format

**Diagnose only:** A findings list. Each finding locates the flat passage, names the
figure its trigger licenses, and states the budget. Order by impact — endings first.
Offer to apply.

**Strengthen:** Revised text, then a change note in this shape:

```
Budget: [length] → [N] figures
Applied: [figure] at [location] — trigger: [which condition fired]
Free: [diction changes, summarized in one line]
Left alone: [what you could have done and chose not to, and why]
Claim check: [any hedge/qualifier/number preserved or restored, or "clean"]
```

**Single line:** 3–5 treatments, each labeled with its figure, then a recommendation with
one sentence of reasoning.

Always report what you left alone. Restraint is the deliverable as much as the figures are.

---

## Worked example

**Before:**
> The implementation of our customer experience transformation initiative will require
> significant organizational commitment and cross-functional collaboration. This strategic
> priority represents an opportunity to enhance our competitive positioning and drive
> sustainable growth.

Claims present: (a) it requires commitment and cross-team work; (b) it *represents an
opportunity* — hedged — to improve competitive position and growth.

**Overcooked — do not produce:**
> This transformation will test us. It will demand commitment. It will require every team
> to work together. But if we commit, if we collaborate, if we follow through—we will not
> just compete. We will lead.

Diagnosis: two anaphora runs in forty words against a budget of one. A negative
parallelism ("not just compete"). A generic positive closer ("we will lead"). And the
hedge, "an opportunity to enhance," became an unqualified promise. Six figures in one
paragraph, four of them on humanizer's flag list, and a claim the original never made.
This is what blowing the budget looks like.

**Strengthened:**
> Customer experience programs fail for a boring reason: they need teams that don't report
> to each other to change how they work at the same time. That's the cost. Get it right
> and it could put us ahead of the competitors still selling on price. Get it wrong and
> we've spent a year on work nobody uses.

```
Budget: 68 words → 1 figure
Applied: antithesis at the close ("Get it right and... / Get it wrong and...") —
  trigger: both poles real, survives the swap test
Free: nominalizations to verbs ("the implementation of... will require" → "they need");
  Saxon finishes on "the cost," "on price," "nobody uses"
Left alone: no anaphora — under 300 words. No antimetabole — trigger tests don't fire.
  Isocolon considered for the three requirements and cut; they aren't equal in weight.
Claim check: hedge preserved ("could put us ahead," not "will"). "Cross-functional
  collaboration" made concrete as "teams that don't report to each other" — same claim.
  "Drive sustainable growth" dropped: the source gives no mechanism, and inventing one
  to feed the figure would be claim inflation. Flag for the author rather than restore.
  "Work nobody uses" adds a failure case the original only implied — confirm with the
  author before publishing.
```

Note the last two lines. The claim check runs in both directions: it stops you from
inflating, and it makes you declare what you added.

---

## Common issues

**Zero figures is a real answer.** If the text is clear, correctly hedged, and ends on a
stress, you're done. Say that. Adding a figure to already-working prose is the most common
way this skill makes writing worse.

**The author's voice outranks the figure.** If they write in short flat declaratives, a
Churchillian triad is not an improvement, it's a costume. Match what's there.

**Run humanizer first on AI-generated text.** Figures layered onto promotional prose
compound the problem. Clean the surface, then add craft.

**Don't hunt for triggers.** The trigger conditions exist to stop you from applying
figures, not to help you find excuses. If you're reasoning hard about whether a trigger
fired, it didn't.

**Antimetabole is over-attempted.** Most pieces should have none. If the three trigger
tests don't fire cleanly, the output reads as a fortune cookie.

**Some flatness is correct.** A recall notice, a status update, a price change — these
should be flat. Check the register table before doing anything.

---

## Source

Ward Farnsworth, *Classical English Rhetoric* (2011) and *Classical English Style* (2020),
plus his interview on David Perell's "How I Write" podcast.

Quotations are as delivered, condensed where noted. One exception: the active-voice
version of Churchill's "so much owed by so many to so few" in `references/figures.md` is
Farnsworth's own hypothetical foil, not a line Churchill wrote — it is labeled there.
