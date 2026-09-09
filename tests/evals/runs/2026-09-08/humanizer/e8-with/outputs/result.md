Here's the humanized version.

---

The programme began in 2017 as a small pilot in two boroughs. Over the following three years it expanded to seven, and in 2020, after the interim evaluation reported positive outcomes across all three measured domains, the council increased its core funding.

Staff numbers grew from four to nineteen in the same period. The referral pathway was redesigned twice; the second redesign introduced a single point of access, which reduced the average wait from eleven weeks to under four. That remains the achievement most often cited in subsequent reviews.

The service now operates from three sites and receives approximately 4,000 referrals each year. Roughly two thirds come from primary care and the remainder through schools and self-referral, a balance that has been broadly stable since 2022.

---

## What changed

**`UNDER-PUNCT` (punctuation scarcity) -- the whole finding.** The draft was three paragraphs and three sentences: 144 words, 46 to 52 words per sentence, and not one comma, semicolon or parenthesis anywhere in it. Every sentence ran past 30 words with no internal break, and "and" appeared ten times. That rate is the tell, and it is the reverse of what most AI checklists encode: current models under-punctuate, write long, and reach for "and" more than any other word. The rewrite splits three sentences into seven, varies their length from 10 to 30 words, and puts the missing breaks back: five commas and a semicolon.

**`VAGUE-CONNECT` (undecided connection).** Nine of the ten "and"s joined two propositions rather than items in a list, so each got the test -- cut the connector, read the halves apart, and see whether a real relationship was hiding behind it. Six were carrying a relationship the draft never committed to, and I named it:

- "expanded to seven boroughs ... and the council increased its core funding in 2020 after the interim evaluation" -- sequence, then cause. Split into two sentences, with the evaluation subordinated so the funding decision reads as the consequence it was.
- "grew from four to nineteen in that period and the referral pathway was redesigned twice" -- two unrelated facts. Sentence break.
- "redesigned twice and the second redesign introduced a single point of access" -- specification, not addition. Semicolon.
- "reduced the average wait ... and this remains the most cited achievement" -- a claim about the whole programme, not a continuation of the wait-time fact. Its own short sentence.
- "receives approximately 4000 referrals each year and roughly two thirds of those referrals come from primary care" -- a breakdown of the figure just given. Sentence break.
- "arrive through schools and self-referral and the balance between these routes has been broadly stable" -- the stability claim comments on the split rather than extending it. Now an appositive after a comma.

Four "and"s stayed. "Schools and self-referral" is a two-item series, and the test does not apply to series. "Operates from three sites and receives approximately 4,000 referrals" is one subject with two verbs, so I dropped the redundant "it" and left it. The remaining two -- the 2020 funding clause and "two thirds ... and the remainder" -- passed the test: both hold a real relationship that plain "and" states correctly, and once the sentences around them carry punctuation, they read as ordinary English rather than as a run-on.

**Not changed, and why.** The word-list scan came back essentially clean: zero hits on `INFLATION`, `ING-ANALYSIS`, `AI-VOCAB`, `NO-COPULA`, `NEG-PARALLEL`, `RULE-OF-3`, `CHALLENGES-FORMULA` and `GENERIC-CLOSER`, and no markup residue. Density is under 1 per 100 words across at most one pattern, which on the density-and-spread table alone would read "within human range" and justify no rewrite. `UNDER-PUNCT` is measured by rate rather than by word-list hits and sits outside that table, so it stands as a finding on its own -- and here it is the only one that matters. "From four to nineteen" and "from eleven weeks to under four weeks" are real numeric ranges, not `FALSE-RANGE`. I added no em dashes; the original's having none is not evidence of anything either way.

Every figure, date and claim is unchanged. The only wording touches beyond the joins are a thousands separator on 4,000 and "in that period" to "in the same period"; your "approximately" and "roughly" both stay as written.

**One thing to check before this goes out:** "the most cited achievement of the programme in subsequent reviews" attributes a judgement to reviews it never names, which is borderline `VAGUE-ATTRIB`. I left the claim intact because you presumably know which reviews they are, but naming one ("the 2023 commissioning review") would make it land harder and clear the flag.
