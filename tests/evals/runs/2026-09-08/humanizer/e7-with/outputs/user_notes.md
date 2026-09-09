# User Notes

## Uncertainty

- The draft is undated. The skill's "Date first" rule can rule out AI use for anything written before 30 November 2022, and I could not apply it. If this text is older than that, the whole scan is moot. I flagged this in the answer rather than assuming a date.
- "showcases" is a genuine judgment call. It is a literal AI-VOCAB list word, but "showcase" is also ordinary English in nonprofit and funder writing, where showcasing results is a normal thing to say. I reported it as below threshold rather than as evidence, which is what the threshold table dictates, but a grader who expected zero findings would see one, and a grader who expected it flagged harder would see it soft-pedalled.
- "I would rather wait for it than publish" sits close to the reversed "X rather than Y" form listed under NEG-PARALLEL, which is an ungated finding at any density. I ruled it out because it is a real preference between two available actions rather than a balanced construction correcting a misconception the reader never held. If that ruling is wrong, the verdict changes materially, since NEG-PARALLEL is not gated by the density table.

## Needs Human Review

- The "admission against interest" argument (attendance was lowest among the pupils the referral criteria targeted) is my reasoning about what a generated draft would avoid saying, not a pattern in the skill. It is persuasive but it is inference, not a codified indicator.
- UNDER-PUNCT was measured by hand on a 138-word sample. Parentheses per 1,000 words and similar rates are not meaningful at this length. The comma rate and sentence-length variance are, and both read human, but the sample is small.

## Workarounds

- Per eval constraints I did not run scripts/scan-ai-tells.py, so density and spread were counted by reading. For a text this short that is reliable; on a longer document a hand count would be more error-prone, and the script's word-list coverage might catch a hit I missed.

## Suggestions

- The Review-and-flag use case tells you to report findings ordered by signal strength, but says nothing about reporting *cleared* patterns. On a clean text the most useful part of the answer is the list of things that look like tells and are not (a lone "Moreover," zero em dashes, "rather than"), because that is exactly where a user's own instinct goes wrong. Pass 4 says "don't invent residual tells," which correctly stops you inflating, but the skill could say explicitly that naming the near-misses you dismissed is the right way to fill a clean report.
- The reversed "X rather than Y" entry under NEG-PARALLEL has no worked example distinguishing it from ordinary comparative preference ("I would rather A than B"), which is very common in human prose. A one-line disambiguator there would prevent a false positive that is not gated by the density table.
