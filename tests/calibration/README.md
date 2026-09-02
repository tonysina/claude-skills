# Threshold calibration for `humanizer`

Reproduces the measurement behind the "When a flag is a finding" table in
`skills/humanizer/SKILL.md` (v1.3.0). The corpus is not committed: it is Wikipedia text
(CC BY-SA) and about 22,000 words. Rebuild it with the three scripts here.

## Corpus design

The source page, [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
contains both halves of a labelled set:

- **Positives** — its quoted examples, each one editor-confirmed AI text.
- **Human set 1** — its own editorial prose, written by Wikipedia editors.
- **Human set 2** — Wikipedia articles on the same subjects as the examples, at their last
  revision before 2021. The page's own rule: text older than November 2022 cannot be AI.

## Rebuild

```bash
# 1. source page wikitext (calibrated against the page as of 2026-09-02)
curl -sL 'https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&action=raw' -o signs.wiki

# 2. positives + human set 1
./tests/calibration/extract-corpus.py signs.wiki corpus

# 3. human set 2: pre-2021 revisions. Send a User-Agent and pace requests; the API
#    rate-limits anonymous bursts.
mkdir -p corpus/human2020
for t in Somali_cuisine Korattur Los_Angeles_Art_Association Harian_Metro Rotary_saw \
         Huey_Lewis_and_the_News Advisory_Neighborhood_Commission Gillingham,_Kent \
         Vladimir_Yankilevsky; do
  sleep 1
  curl -s -A 'claude-skills-calibration/1.0' \
    "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=$t&rvlimit=1&rvstart=2021-01-01T00:00:00Z&rvdir=older&rvprop=content&rvslots=main&format=json&formatversion=2" \
    | jq -r '.query.pages[0].revisions[0].slots.main.content // empty' > "corpus/human2020/$t.wiki"
done
./tests/calibration/chunk-human.py corpus/human2020 corpus/human2020txt

# 4. measure
./tests/calibration/calibrate.py scripts/scan-ai-tells.py skills/humanizer/SKILL.md \
    pos=corpus/pos editorial=corpus/neg human2020=corpus/human2020txt
```

## Result on 2026-09-02 (v1.3.0 watch lists)

| Set | Blocks | Words | Median density | p90 | Max | Max patterns |
|---|---|---|---|---|---|---|
| AI examples | 84 | 11,881 | 0.1 | 3.8 | 10.8 | 5 |
| Human editorial | 10 | 2,200 | 0.0 | 0.6 | 0.7 | 1 |
| Human pre-2021 | 50 | 7,486 | 0.0 | 0.4 | 1.6 | 2 |

Density is watch-list hits per 100 words after the meta-quotation filter. No human block
contained a `CONSTRUCTIONS` hit. 42 of 84 AI blocks scored zero on word lists; their
tells were markup, negative parallelism, or structure.

## Known biases

- Positives were chosen by editors as examples of *specific* patterns, many of them
  markup, so the zero-hit rate overstates how often real AI prose evades the word lists.
- Both human sets are encyclopedic register. Marketing and business prose from human
  writers has not been measured and may sit higher on `INFLATION` words.
- The page changes. Re-running against a later revision will move the numbers.
