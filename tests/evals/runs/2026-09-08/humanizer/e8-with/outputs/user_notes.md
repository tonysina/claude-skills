# User Notes

## Uncertainty

- **The threshold table points one way and the rewrite went the other.** Word-list density here is at most 1 hit per 144 words with a spread of 0-1 patterns, which is the table's "within human range -- do not rewrite on word-list evidence alone" row. I rewrote anyway, on `UNDER-PUNCT`. The skill authorises this explicitly ("`UNDER-PUNCT` is measured by rate, not by word-list hits, and does not contribute to density or spread. Assess it separately") and reinforces it ("a clean word-list scan is not a clean bill; run Passes 2-4"). Flagging it because an executor reading only the table would have returned the text unchanged, and that is the pivot the case turns on.
- **"the most cited achievement ... in subsequent reviews" -- `VAGUE-ATTRIB` or not?** It attributes a judgement to unnamed reviews, which is the shape of the pattern. But in an internal service review the author plausibly knows exactly which reviews and would cite them elsewhere in the document. I flagged it in the change summary and left the sentence intact, per "when uncertain, flag the pattern for the user rather than silently rewriting." A stricter reading would have applied the pattern's "[needs a source]" marker; that felt disproportionate for a summary paragraph excerpted from a longer document.
- **Whether three joints should have stayed as "and".** I kept plain "and" at the 2020 funding clause and at "two thirds ... and the remainder". Both pass the skill's test (the relation is genuine conjunction), and removing every "and" would have produced a different artificiality. Another executor could defend converting them.
- **"in that period" to "in the same period"** is a wording change not strictly required by any pattern. It reads better once the paragraph break lands before it. Minor, but it is a change beyond the punctuation work.

## Needs Human Review

- **The excerpt is described as "a summary paragraph for a service review" but is three paragraphs.** I treated the whole file as the unit and kept the paragraph breaks. If it is meant to be one paragraph in the final document, the sentence splitting still works but the paragraph structure may need collapsing.
- **Numbers were preserved verbatim, not verified.** "approximately 4000" gained a thousands separator; nothing else was touched. A domain reader should confirm the 11-week and 4-week wait figures and the referral split survive the rewrite intact -- they do textually, but I have no way to check them against source.
- **"expanded to seven"** drops the repeated noun ("seven boroughs" to "seven"). Natural in context, but if this paragraph gets excerpted again, the antecedent travels one sentence further than before.

## Workarounds

- SKILL.md (37.6KB) exceeded the Bash output limit and had to be read from the persisted tool-results file. Not a skill defect; worth knowing that loading this skill costs an extra step in a constrained context.
- The scanner script was off-limits for this eval, which turned out not to matter: the skill states that `scripts/scan-ai-tells.py` does not compute the `UNDER-PUNCT` rates at all. The finding that drove this entire rewrite is one the tool could not have produced. Anyone relying on the script alone would have scored this text clean.

## Suggestions

- `UNDER-PUNCT`'s separation from the density/spread table is stated in two places (the bullet under the table and the "This is a rate measure" paragraph in the pattern itself), but the table is the visually dominant element and reads as authoritative. A one-line note inside the table -- for instance a footer row saying "UNDER-PUNCT, constructions and residue are not gated here" -- would make the carve-out impossible to miss at a glance. The prose carve-out below the table ("What the table does not gate") lists constructions and residue but does not repeat `UNDER-PUNCT` by name; adding it there would close the gap cheaply.
- The `UNDER-PUNCT` worked example in SKILL.md ("The programme expanded to three cities in 2019 and the council increased its funding...") is very close to this eval input. That is good for teaching the pattern but means an executor may recognise the shape rather than measure it. Not a defect, just something to be aware of when this case is used to compare with/without-skill runs.
- The pattern says to measure "parentheses per 1,000 words," but for a 144-word input that measure is not meaningful -- one parenthesis would score 6.9 per 1,000. A note that the parenthesis rate needs a longer sample, or a per-document threshold, would help on short inputs.
