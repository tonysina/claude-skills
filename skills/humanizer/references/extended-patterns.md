# Extended Patterns: Markup, Citations, and Technical Artifacts

These patterns are lower-frequency but unmistakable when present. They are drawn from the same Wikipedia "Signs of AI writing" source as the main SKILL.md patterns.

## Markup artifacts

### Curly quotation marks
ChatGPT and DeepSeek typically use curly quotes ("...") instead of straight quotes ("..."). They may also use curly apostrophes ('). This is inconsistent -- sometimes mixing curly and straight in the same response. Note: Gemini and Claude typically do not use curly quotes. Also note that macOS, iOS, and Microsoft Word have "smart quotes" features that produce the same result, so curly quotes alone do not prove AI use.

### Markdown in non-Markdown contexts
AI chatbots default to Markdown formatting: **bold** using asterisks, ## for headings, [text](url) for links. When pasted into contexts that don't render Markdown, these artifacts remain visible.

### turn0search0 artifacts
Since February 2025, ChatGPT has been known to leave "turn0search0" placeholder codes (with increasing numbers) where it intended to link to external sites. The codes are surrounded by Unicode Private Use Area characters. Variations include turn0image0, citeturn0news0, and citeturn1file0.

### contentReference and oaicite bugs
ChatGPT may insert `:contentReference[oaicite:0]{index=0}` or `oai_citation:0` markup in place of reference links. These are rendering bugs from the chatbot interface.

### utm_source parameters
ChatGPT adds `utm_source=chatgpt.com` or `utm_source=openai` to URLs it cites. Microsoft Copilot uses `utm_source=copilot.com`. Grok uses `referrer=grok.com`. This definitively proves chatbot involvement in citation, though not necessarily in generating the surrounding text.

### attribution and attributableIndex
ChatGPT may append JSON code like `({"attribution":{"attributableIndex":"X-Y"}})` at the end of sentences.

### grok_card tags
Grok may include XML-styled `<grok-card>` tags after citations.

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

## Title case in headings

AI chatbots capitalize all main words in section headings (Title Case) rather than using sentence case.

**Before:** `## Strategic Negotiations And Global Partnerships`
**After:** `## Strategic negotiations and global partnerships`

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
- **Didactic disclaimers:** "It's important to note..." (see main SKILL.md, pattern 13)
- **Section summaries:** "In summary..." / "In conclusion..." (see main SKILL.md, pattern 13)

---

## Ineffective indicators (do NOT flag these)

Per Wikipedia's guide, these are NOT reliable signs of AI writing:
- Perfect grammar (many humans write well)
- "Bland" or "robotic" prose (LLMs actually tend toward effusive and verbose prose)
- "Fancy" or unusual words (low-frequency words are less likely in AI text, not more)
- Letter-like writing with salutations and sign-offs (humans do this too)
- Conjunctions like "moreover" or "furthermore" in isolation (common in human essay writing)
- Bizarre wikitext errors (more likely from browser extensions or editing tools)

## Source

All patterns from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), WikiProject AI Cleanup.
