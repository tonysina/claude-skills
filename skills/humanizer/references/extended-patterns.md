# Extended Patterns: Markup, Citations, and Technical Artifacts

These patterns are lower-frequency but unmistakable when present. They are drawn from the same Wikipedia "Signs of AI writing" source as the main SKILL.md patterns. Cross-references to SKILL.md use its stable pattern IDs (for example `DIDACTIC`), not display numbers, because display numbers can change between versions.

## Model-specific markup residue

Residue is the highest-confidence evidence in this file: it is mechanical, it has no human explanation, and it identifies the tool. Search for these strings before reading for style. Finding one proves a chatbot touched the citation or paragraph it sits in; it does not by itself prove the chatbot wrote the surrounding prose (some writers use a chatbot only to find sources).

### ChatGPT
- **turn0search0 codes.** Since February 2025, placeholder codes like `turn0search0` (with increasing numbers) where a link was intended, surrounded by Unicode Private Use Area characters. Variants: `turn0image0`, `citeturn0news0`, `citeturn1file0`.
- **contentReference and oaicite.** `:contentReference[oaicite:0]{index=0}` or `oai_citation:0` in place of reference links.
- **attributableIndex.** JSON like `({"attribution":{"attributableIndex":"X-Y"}})` appended to sentences.
- **utm_source.** `utm_source=chatgpt.com` or `utm_source=openai` on cited URLs.

### Gemini
- **[cite: N] markers.** `[cite: 1]` or `[cite: 3, 12, 13]` at the end of sentences.
- **span markers.** `[span_1](start_span)` and `[span_1](end_span)` wrapped around sentences or titles, numbered upward through the text.

### Grok
- **grok-card tags.** XML-styled `<grok-card data-id="..." data-type="citation_card">` after citations.
- **grok_render_citation_card_json.** `[](grok_render_citation_card_json={"cardIds":["..."]})` in place of a link.
- **referrer.** `referrer=grok.com` on cited URLs.

### DeepSeek
- **Lenticular brackets with daggers.** `【85†L261-269】` style markers, sometimes with long numeric IDs like `【854140639155648†L119-L123】`. Seen since June 2025; appears specific to DeepSeek and its derivatives.

### Perplexity
- **attached_file and web tags.** `[attached_file:1]` or `[web:1]` at the end of sentences (seen since fall 2025).
- **ppl-ai-file-upload.** Citations to an Amazon S3 bucket with `ppl-ai-file-upload` in the URL.

### Microsoft Copilot
- **utm_source.** `utm_source=copilot.com` on cited URLs.

### Unattributed
- **:::writing blocks.** `:::writing{variant="document" id="12345"}` (random five-digit ID), often with a closing `:::`. Seen since June 2026, also in other languages (`:::écriture{variante="document" ...}`).

### Not model-specific, still residue
- **Markdown in non-Markdown contexts.** `**bold**` asterisks, `##` headings, `[text](url)` links, `---` rules, showing as literal characters where Markdown is not rendered.
- **Curly quotation marks.** ChatGPT and DeepSeek typically produce curly quotes and apostrophes, sometimes mixed with straight ones in the same text. Gemini and Claude typically do not. macOS, iOS, Microsoft Word, and Chicago-style publishing all produce curly quotes too, so curly quotes alone do not prove AI use.

---

## Heading structure

Structure-level tells that survive a copyedit of the prose:

- **Title heading.** A heading carrying the document's own title placed above all content, because the chatbot did not picture the title as already present.
- **Skipped levels.** Sections starting at the third level with no second level above them.
- **Level-1 overuse.** Every section at level 1 (`# Heading` / `= Heading =`), usually from Markdown being translated into another markup.
- **Headings containing only headings.** A heading whose entire body is more headings, with no text of its own.
- **Thematic breaks between every section.** A horizontal rule (`---` or `----`) after each section.
- **Title case.** All main words capitalized in headings: `## Strategic Negotiations And Global Partnerships`. Rewrite as `## Strategic negotiations and global partnerships`. (Also in SKILL.md under `BOLD-LISTS`.)

---

## Placeholder text and templates

LLMs sometimes leave fill-in-the-blank templates the user was supposed to replace:
- Bracketed placeholders: [Your Name Here], [Company Name], [Date]
- Placeholder dates: 2025-xx-xx, INSERT_DATE
- URL placeholders: INSERT_SOURCE_URL, PASTE_YOUTUBE_VIDEO_URL_HERE
- Generic templates: "[Describe the specific section...]"
- Infobox comments: `<!-- Add if available with citation -->`

**Action:** Identify and fill in all placeholders, or remove if content is not available.

---

## Subject lines and formal preambles

AI-generated text sometimes includes email-style subject lines or formal preambles meant for correspondence, not content:
- "Subject: Request for Permission to Edit..."
- "Dear Wikipedia Editors, I hope this message finds you well..."

**Action:** Remove entirely -- this is correspondence structure, not content.

---

## Citation patterns

### Hallucinated references
LLMs may generate citations to non-existent articles with DOIs that appear valid but are assigned to unrelated papers. Book citations may exist but lack page numbers, making them unverifiable. Citations may include an access-date that is unexpectedly old relative to when the text was written.

### Source-to-text integrity
Per Wikipedia's talk page, modern LLMs are better about complete hallucinations, but "the main place problems creep in is source-to-text integrity -- many 'X highlighted Y and noted Z' statements are completely different from what they are cited to."

### Overemphasis on sources in body text
LLMs painstakingly attribute even trivial or uncontroversial facts to named sources in the body text, where a human writer would use a footnote or no citation at all.

### Named references declared but unused
LLM-generated reference sections may include named references that are never actually cited in the article body.

---

## Emojis in headings

AI chatbots sometimes decorate section headings or bullet points with emoji. This is most common in informal or talkpage contexts.

**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity

**After:**
> The product launches in Q3. User research showed a preference for simplicity.

---

## Unusual use of tables

AI tends to create unnecessary small tables that would be better represented as prose.

---

## Verbose edit summaries

AI-generated edit summaries are often unusually long, written as formal first-person paragraphs that itemize conventions and guidelines. Human edit summaries are typically brief and informal.

---

## Historical indicators (declining frequency)

These patterns were common in older AI models but are less frequent in 2025+ models. They may still appear in older undetected AI-generated content:

- **Prompt refusal:** "As an AI language model, I can't directly..." (increasingly rare)
- **Abrupt cutoffs:** Text stopping mid-sentence due to token limits
- **Didactic disclaimers:** "It's important to note..." (see main SKILL.md, `DIDACTIC`)
- **Section summaries:** "In summary..." / "In conclusion..." (see main SKILL.md, `DIDACTIC`)
- **Elegant variation:** synonym cycling from repetition penalties in older models (see main SKILL.md, `ELEGANT-VAR`). The source moved this to its historical section in 2026.
- **Outdated access-dates:** citations dated well before the text was written; newer chatbots seldom do this, and copied citations produce it legitimately

---

## Signs of human writing (do not "fix" these)

The source lists constructions that are *more* common in human-written text than in AI output. Removing them makes text read more like AI, not less:

- Simple *is*/*has* phrases: "there is a," "it has a"
- Plain verbs where a stiffer synonym exists: *wrote* (not *authored*), *moved* (not *relocated*), *used* (not *utilized*), *tried* (not *attempted*), *died* (not *passed away*)
- Superlatives and definite statements: "one of the best," "is the only," "was the first"
- Hedges and intensifiers: *very*, *perhaps*, *tends to*
- Isolated wordy constructions: *as a result of*, *in order to*, *all of the*, *a part of*, *the fact that*

The last item is why v1.3.0 removed *in order to* and *due to the fact that* from the `DIDACTIC` watch list: they were on it as "filler," and the source says the opposite.

---

## Ineffective indicators (do NOT flag these)

Per Wikipedia's guide, these are NOT reliable signs of AI writing. False accusations drive writers away; check for confirmation bias before flagging:
- Perfect grammar (many humans write well)
- A mix of casual and formal registers, or prose that is both "clinical" and "emotional" (a technical person writing casually, a young writer, a mixed-register preference, or several authors on one page)
- "Bland" or "robotic" prose (LLMs actually tend toward effusive and verbose prose)
- "Fancy," academic, or formal prose in general (the overused words are *specific words*; the correlation does not extend to all formal writing)
- Transition words in isolation ("moreover," "furthermore," "additionally"): only a few are overused by AI, and essay-style human writing uses them too
- Unsourced content (most unsourced text predates LLMs; modern chatbots cite, inaccurately)
- Bizarre markup errors (more likely from browser extensions or editing tools)
- Correct, complex markup (normal for anyone who has found the preview button)

## Source

All patterns from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), WikiProject AI Cleanup. Checked against the live page on 2026-09-02.
