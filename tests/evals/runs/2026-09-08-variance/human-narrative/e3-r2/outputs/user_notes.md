# User Notes

## Uncertainty

- **Output mode choice.** The prompt ("why does this still feel AI-written") is a
  diagnosis question, which the skill's Output format section maps to "Diagnosis only …
  Offer to execute." I delivered "Full audit + rewrite" instead, on the judgment that a
  user who asks *why* also wants to see what the fix looks like. If the intended behavior
  was diagnosis-plus-offer, the rewrite section is over-delivery.
- **Cluster B is the closest call in the scan.** The gate is AI-side (embodied is the
  plurality mode among emotional beats), and whether it fires depends on how you count
  beats. I counted six, of which three run through the body (50%, under the >60% rule),
  and zero corroborators were AI-side, so I withheld it. A stricter beat count — treating
  "stared at the calendar until the squares blurred" as embodied rather than behavioral,
  or excluding "which made me laugh" — pushes the embodied share to 60–75% and fires the
  gate quantitatively. It still would not fire the cluster, because the corroborators are
  uniformly human-side, but the reasoning is more fragile than the table suggests.
- **Cluster D's Likert calls (2/5 for chronological discontinuity, 3/5 for
  recontextualization) are single-rater judgments** on a scale the paper applies with
  model annotators over 61,608 stories. The essay does contain a mild
  recontextualization ("She had never wanted me to do both"), which is why I put it at 3
  rather than 1.
- **"So I had filled it in myself"** in the rewrite is a paraphrase of the deleted line
  "The fear I carried for eleven months was about a conflict that was never going to
  happen." I judged it a permitted A fix (moving the statement earlier so it reads as
  premise rather than verdict), but it is the piece of the rewrite most likely to be
  called a partial re-introduction of the thematic statement.

## Needs Human Review

- **Whether the essay's register really licenses D.** The Step 1 table puts personal essay
  in the all-clusters row and explicitly says a 400-word personal essay still gets D. But
  D is the most invasive intervention in the taxonomy with the smallest measured gaps
  (all four ≤0.34 on 1–5), and this essay is short enough that a reorder is a large
  proportion of the piece. I flagged this to the user with a revert instruction rather
  than presenting it as settled.
- **Guardrail 4 ("would the author recognize it")** is inherently unverifiable by an
  editor. The rewrite preserves every scene, all dialogue and the diction, but the
  in-medias-res opening is a different authorial move than the one the writer chose.
- **The essay may be autobiographical and factually load-bearing.** I made no factual
  changes, but a reader should confirm the reordered timeline ("three weeks earlier, on a
  Monday") matches the original's "the third week" framing. The source says the second ask
  came "on a Thursday in the third week" after the first ask "on a Monday", so ~3 weeks is
  right, but it is an inference.

## Workarounds

- **Cluster F could not be executed.** It fired, and the skill calls it the "highest
  value-per-effort cluster", but every available form of the fix (naming a book, author,
  or event the essay is in conversation with) would invent a fact about the author's
  reading or history, which Step 5 guardrail 2 forbids. The skill's explicit truth
  constraint is written under C1; I applied it to F by analogy. Per Step 5 I reported the
  blocked intervention and passed its slot to the next in order (E), keeping the total at
  three. This is the correct handling as I read it, but the skill does not state the
  truth constraint for F explicitly.

## Suggestions

- **Generalize the truth constraint beyond C1.** It currently sits in a blockquote under
  the C1 fix, but it binds F just as hard in any non-fiction register — naming a reference
  in a personal essay asserts something about the author's life, not just about an idea.
  A one-line cross-reference under F would prevent an editor from confidently fabricating
  an influence.
- **The worked example may under-model this.** In it, Brooks is added to a first-person
  thought-leadership piece with no discussion of whether the author had actually read
  *The Mythical Man-Month* — only a note to run `source-check` on the paraphrase. That
  checks whether the claim *about the book* is right, not whether the claim *about the
  author* is. Worth distinguishing.
- **The Output format section could disambiguate "why does this feel AI-written" prompts.**
  That phrase is in the skill's own trigger list but is not mapped to one of the three
  output modes, so an executor has to guess between "Diagnosis only" and "Full audit +
  rewrite".
- **Cluster B would benefit from a stated beat-counting convention.** The >60% rule is
  precise, but whether an action like "stared at the calendar until the squares blurred"
  counts as embodied, behavioral, or not a beat at all determines the result, and the
  skill leaves the taxonomy to the editor.
