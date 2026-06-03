---
name: humanizer
description: |
  Remove signs of AI-generated writing from text. Use when editing or reviewing
  text to make it sound more natural and human-written. Based on Wikipedia's
  "Signs of AI writing" page, maintained by WikiProject AI Cleanup -- a catalog
  of patterns observed across thousands of AI-generated texts.

  Triggers: "make this sound less AI", "humanize this", "clean up AI writing",
  "does this sound like ChatGPT", "de-slop this", "make this more natural",
  "remove AI patterns", "this sounds too robotic", "edit for voice",
  "make this sound like a person wrote it", "review for AI tells"

  Do NOT use for: general editing unrelated to AI patterns, grammar-only fixes,
  style preferences that don't involve AI detection.
metadata:
  version: 1.2.0
---

# Humanizer: Remove AI Writing Patterns

Remove signs of AI-generated text to make writing sound natural and human-written. Based on Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup).

## How to use this skill

When given text to humanize:

1. Scan for high-signal patterns first (significance inflation, -ing phrases, AI vocabulary)
2. Then check structural patterns (copula avoidance, negative parallelisms, rule of three)
3. Then check formatting and surface patterns (em dashes, boldface, lists)
4. Rewrite problematic sections while preserving meaning
5. Match the intended tone -- don't force a single voice (see "Tone awareness" below)
6. Pass 4 -- voice check: read the result aloud. Does it sound like a person wrote it? Is rhythm varied? Are there specific details rather than vague claims? Would you still flag a tell if a stranger sent you this draft? If yes, fix it. If no, stop -- don't invent residual tells.

Load `references/extended-patterns.md` when you encounter technical markup (turn0search0, contentReference, utm_source), citation problems (hallucinated DOIs, source-to-text mismatches), or need to check whether a suspected indicator is on the "ineffective indicators" list (patterns that are NOT reliable signs of AI writing).

### Use cases

**Review and flag:** User pastes text and asks "does this sound like AI?" or "review for AI tells." Scan for patterns, report what you found with pattern names, and offer to rewrite. Don't rewrite automatically -- the user wants a diagnosis first. Return a findings list ordered by signal strength; each finding names the pattern, quotes the offending text, and suggests a fix.

**Full rewrite:** User pastes text and says "humanize this" or "de-slop this." Scan, rewrite, and return clean text followed by a brief change summary naming the patterns fixed.

**Edit with constraints:** User says "make this less AI but keep the formal tone" or "clean up this draft but don't change the structure." Apply pattern fixes within the stated constraints. Respect the user's boundaries over the skill's defaults. Include a change summary on request.

**Voice calibration with sample:** User provides a sample of their own writing (inline or via file path) and asks for a humanized rewrite that matches their voice. Before rewriting, analyze the sample for sentence length patterns, word choice register (casual vs academic), paragraph openings, punctuation habits, transition style, and any recurring phrases. Then rewrite the target text using patterns drawn from the sample, not generic "human" defaults. If the sample uses short sentences, don't produce long ones. If the writer says "stuff" and "things," don't upgrade to "elements" and "components." If no sample is provided, fall back to the default behavior in "Tone awareness" below.

## Tone awareness

Removing AI patterns is only half the job. But the fix depends on context.

A LinkedIn post needs a different voice than a technical report. A sales email differs from an academic paper. Don't force casual first-person onto formal writing, and don't strip personality from pieces that need it.

**Match the target context:**
- Formal/technical: Remove AI patterns but keep professional register. Replace vague claims with specific ones. Don't add "I" or humor.
- Professional/business: Remove patterns, add concrete details. Light personality is fine where appropriate.
- Casual/thought leadership: Remove patterns AND add voice -- opinions, varied rhythm, specific feelings, first-person where it fits.
- Creative: Remove formulaic patterns. Preserve or add distinctive voice, unexpected phrasing, real texture.

**Signs of voiceless writing (even if technically "clean"):**
- Every sentence is the same length and structure
- No opinions or reactions, just neutral reporting
- No acknowledgment of uncertainty or mixed feelings
- Reads like a press release or tourism brochure

**For casual contexts, add voice by:**
- Having opinions ("I keep coming back to..." rather than neutrally listing)
- Varying rhythm (short sentences, then longer ones)
- Acknowledging complexity ("impressive but unsettling" beats just "impressive")
- Being specific about reactions rather than using generic evaluative words

**Edge cases -- when NOT to fully humanize:**
- Already-good text: If text has few AI patterns, don't over-edit. Flag what you found and leave the rest.
- Intentionally formal writing: Academic, legal, or regulatory text may legitimately use some patterns (e.g., "it should be noted" in legal disclaimers). Don't strip context-appropriate formality.
- Technical documentation: Precision matters more than personality. Focus on removing vague puffery and filler, not adding voice.

---

## HIGH-SIGNAL PATTERNS (scan first)

*Pass 1 covers these. They cluster -- finding one usually means others are nearby.*

### 1. Significance inflation, promotional language, and persuasive authority tropes

**Words to watch:** stands/serves as, is a testament/reminder, vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing ongoing/enduring/lasting, setting the stage for, marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted, boasts a, vibrant, rich (figurative), profound, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking

**Authority trope phrases:** the real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter, the truth is, more importantly

**Problem:** LLMs puff up importance by adding statements about how aspects of a topic represent or contribute to broader themes. They also default to promotional adjectives absorbed from marketing copy in training data. A related sub-pattern uses authority-claiming openers ("at its core, what really matters is") to imply the writer is revealing a deeper truth -- but the sentence that follows usually just restates an ordinary point with extra ceremony. Both patterns signal depth that isn't there. The difference: significance inflation adds importance to the *subject*; authority tropes claim insight for the *writer*.

**Wikipedia insight:** This comes from statistical regression to the mean -- LLMs replace specific facts with generic, positive-sounding descriptions that could apply to many topics. As Wikipedia editors put it, the subject becomes "simultaneously less specific and more exaggerated."

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement to decentralize administrative functions and enhance regional governance.

**After:**
> The Statistical Institute of Catalonia was established in 1989 to collect and publish regional statistics independently from Spain's national statistics office.

**Before:**
> The real question is whether teams can adapt. At its core, what really matters is organizational readiness.

**After:**
> The question is whether teams can adapt. That depends on whether the organization is ready to change its habits.

---

### 2. Superficial -ing analyses

**Words to watch:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering (figurative)..., encompassing..., showcasing...

**Problem:** AI chatbots attach present participle ("-ing") phrases to the end of sentences, adding fake depth. Often paired with vague attributions to third parties. Per Wikipedia's guide, this is one of the patterns that is hardest to unsee once you recognize it.

**Before:**
> The civil rights movement emerged as a powerful continuation of this struggle, emphasizing the importance of solidarity and collective action in the fight for justice. This historical legacy has influenced contemporary African-American families, shaping their values, community structures, and approaches to political engagement.

**After:**
> The civil rights movement built on earlier struggles for equality. Its organizing methods and institutions shaped Black community life for decades afterward.

---

### 3. AI vocabulary words

**Key words:** Additionally (especially starting a sentence), align with, crucial, delve (pre-2025), emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), pivotal, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

**Problem:** Studies have shown these words appear far more frequently in post-2023 text than in comparable pre-2023 text. They often co-occur -- where there is one, there are usually others. One or two may be coincidental, but a cluster is one of the strongest tells for AI use.

**Note:** Distribution varies by model and has changed over time. "Delve" was overused by ChatGPT in 2023-2024 but dropped sharply in 2025. Em dash overuse and didactic disclaimers have also declined in newer models (2025+) but still appear. Context matters -- "underscore" can refer to a literal character; "key" can be a physical object.

**Before:**
> Additionally, a distinctive feature of Somali culinary tradition is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.

**After:**
> Somali cuisine includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.

---

### 4. Vague attributions, overgeneralization, and notability name-dropping

**Words to watch:** Industry reports, Observers have cited, Experts argue, Some critics argue, several sources/publications (when few are cited), has been described as, studies have shown (without citation)

**Notability phrases:** profiled in, regional/national media outlets, active social media presence, independent coverage

**Problem:** LLMs attribute opinions to vague authorities. They also exaggerate source quantity -- presenting one or two sources as "several" or "many," or claiming views are "widely held" when only one source expresses them. A related sub-pattern lists source names as proof of notability, echoing Wikipedia's own guideline language (e.g., claiming "active social media presence" as evidence of significance). With retrieval-augmented generation, LLMs may attribute fabricated analyses to named sources regardless of what those sources actually say.

**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Efforts are ongoing to monitor its ecological health.

**After:**
> The Haolai River supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences.

**Before:**
> The band's rise has been cited by several publications as "bridging worlds through music." [only 2 sources cited]

**After:**
> A 2024 Time Magazine profile described her as bridging worlds through music.

---

## STRUCTURAL PATTERNS

*Pass 2 covers these. Sentence- and paragraph-level constructions LLMs reach for habitually.*

### 5. Copula avoidance

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a]

**Problem:** LLMs substitute elaborate constructions for simple "is" and "are." One study documented a 10%+ decrease in "is" and "are" usage in academic writing after 2023. This is especially visible in AI copyedits, which "improve" text by replacing copulas.

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces.

**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms.

**Related: Subjectless fragments.** LLMs also drop the subject entirely with lines like "No configuration file needed" or "Results are preserved automatically." Rewrite when active voice with an explicit subject would be clearer and more direct.

---

### 6. Negative parallelisms

**Patterns to watch:** "It's not just X, it's Y" / "Not only X, but Y" / "X is more than just Y. It's Z." / "Not X, it's Y" / "No X, no Y, just Z"

**Problem:** These constructions appear in LLM writing to seem balanced and thoughtful. LLMs also use explicit negation patterns that negate primary properties altogether.

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere.

**After:**
> The heavy beat adds to the aggressive tone.

**Related: Tailing negations.** Watch for clipped negative fragments like "no guessing," "no wasted motion," or "no fuss" tacked onto the end of a sentence instead of written as a real clause.

**Before:**
> The options come from the selected item, no guessing.

**After:**
> The options come from the selected item without forcing the user to guess.

---

### 7. Rule of three

**Problem:** LLMs overuse groups of three ("adjective, adjective, adjective" or "short phrase, short phrase, and short phrase") to make superficial analyses appear comprehensive.

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes talks, panels, and informal networking between sessions.

---

### 8. Em dash overuse

**Problem:** LLMs use em dashes more often than human writers, especially in formulaic, "punchy" ways that mimic sales writing. Multiple em dashes in close proximity is a strong tell.

**Before:**
> The term is primarily promoted by Dutch institutions -- not by the people themselves. You don't say "Netherlands, Europe" as an address -- yet this mislabeling continues -- even in official documents.

**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling continues in official documents.

**Replacement options:** commas (most common), parentheses (for asides), colons (for explanations), periods (separate sentences), or remove the interrupted clause if it adds little.

---

### 9. Formulaic sections

**"Challenges and future prospects" formula:**
Watch for "Despite its [positive words], [subject] faces challenges..." followed by vague optimism. This rigid formula, often with a separate "Future Outlook" section, is a strong AI tell. The problem is the formula, not simply mentioning challenges.

**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion. With its strategic location and ongoing initiatives, Korattur continues to thrive.

**After:**
> Traffic congestion increased after 2015 when three new IT parks opened. The municipal corporation began a stormwater drainage project in 2022.

---

### 10. Elegant variation (synonym cycling)

**Problem:** AI uses repetition-penalty mechanisms, causing excessive synonym substitution for the same referent (e.g., "the protagonist" then "the main character" then "the central figure" then "the hero").

**Before:**
> Vierny committed to supporting artists resisting the constraints of socialist realism. In the challenging climate of Soviet artistic constraints, Yankilevsky, alongside other non-conformist artists, faced obstacles in expressing their creativity freely.

**After:**
> Vierny supported artists working under Soviet censorship, including Yankilevsky, Kabakov, and Bulatov.

---

### 11. False ranges

**Problem:** LLMs use "from X to Y" constructions where X and Y aren't on a meaningful scale. If no coherent middle ground exists between the endpoints, it's a false range.

**Before:**
> Intelligence and Creativity: From problem-solving and tool-making to scientific discovery, artistic expression, and technological innovation...

**After:**
> Human intelligence spans problem-solving, tool use, scientific inquiry, and artistic creation.

---

## FORMATTING AND SURFACE PATTERNS

*Pass 3 covers these. Visible markup, meta-commentary residue, and chatbot artifacts.*

### 12. Boldface, list formatting, and title-case headings

**Boldface:** AI chatbots emphasize phrases mechanically, often in a "key takeaways" fashion inherited from slide decks, listicles, and sales pitches.

**Inline-header lists:** AI outputs lists where items start with bolded headers followed by colons. This format is common in ChatGPT output but rare in human writing.

**Title-case headings:** LLMs capitalize all main words in section headings (e.g., "Impact of Technology and Digitalization") rather than using sentence case.

**Before:**
> - **User Experience:** The interface has been significantly improved.
> - **Performance:** Load times have been optimized.
> - **Security:** End-to-end encryption has been added.

**After:**
> The update improves the interface, speeds up load times, and adds end-to-end encryption.

---

### 13. Fragmented headers

**Pattern:** A heading followed by a one-line paragraph that simply restates the heading before the real content begins.

**Problem:** LLMs add a generic warm-up sentence under headings as rhetorical scaffolding. It usually adds nothing and makes prose feel padded.

**Before:**
> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.

**After:**
> ## Performance
>
> When users hit a slow page, they leave.

---

### 14. Didactic disclaimers and filler

**Words to watch:** it's important/critical/crucial to note/remember/consider, worth noting, may vary, it should be noted, In summary, In conclusion, Overall, in order to, due to the fact that, at this point in time

**Problem:** Older LLMs added unsolicited advice about topics being "important to note." These have become less frequent in newer models (2025+) but still appear. Section summaries ("In summary...") and wordy filler phrases are related patterns. Human writers typically let conclusions flow naturally without announcing them.

**Before:**
> It's important to note that these caucuses operate outside the formal structure and their influence on policy decisions may vary.

**After:**
> These caucuses operate outside the formal structure and have varying influence on policy.

---

### 15. Generic positive conclusions

**Phrases to watch:** the future looks bright, exciting times ahead, a major step forward, on the journey to excellence, continues to thrive, represents a step in the right direction, poised for growth, the road ahead is promising

**Problem:** LLMs close sections or paragraphs with vague upbeat endings that say nothing concrete. Often paired with formulaic challenges sections (#9) -- the closer reassures the reader that things will work out, regardless of the actual content.

**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence.

**After:**
> The company plans to open two more locations next year.

---

### 16. Knowledge-cutoff disclaimers and gap speculation

**Words to watch:** as of [date], Up to my last training update, While specific details are limited/scarce..., based on available information..., not widely documented, keeps personal details private, maintains a low profile

**Problem:** AI disclaimers about incomplete information get left in text. When AI can't find information about someone's personal life, it often claims the person "maintains a low profile" or "keeps personal details private." Per Wikipedia's guide, this is entirely speculative, including the claim that information is "not documented."

**Before:**
> Matthews Manamela keeps much of his personal life private, choosing instead to focus public attention on his professional work.

**After:**
> [Remove -- if there's no information, don't speculate about why]

---

### 17. Signposting and announcements

**Phrases to watch:** let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado, in this article we'll cover, you might be wondering, before we begin, first let's talk about

**Problem:** LLMs announce what they're about to do instead of doing it. This meta-commentary slows the writing down and gives it a tutorial-script feel. Closely related to fragmented headers (#13) -- both are rhetorical throat-clearing before the real point.

**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.

**After:**
> Next.js caches data at multiple layers, including request memoization, the data cache, and the router cache.

---

### 18. Sycophantic tone and chatbot artifacts

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

**Problem:** Text meant as chatbot correspondence (advice, prewriting) gets pasted as content. Also includes overly agreeable, people-pleasing language.

**Before:**
> Great question! Here is an overview of the French Revolution. Let me know if you'd like me to expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

---

## Common issues

**Ambiguous patterns:** Many AI patterns also appear in human writing (the Wikipedia source repeatedly warns about this). A single em dash, one use of "moreover," or a group of three is not proof of AI writing. Look for clusters -- multiple co-occurring patterns are a much stronger signal than any single one. When uncertain, flag the pattern for the user rather than silently rewriting.

**Mixed AI/human text:** Users often edit AI output before asking for humanization. The text may be partly clean and partly formulaic. Don't rewrite sections that already read naturally just because nearby sections triggered patterns.

**Meaning loss on rewrite:** Some flagged patterns carry meaning the user intended. "It's not just X, it's Y" is a negative parallelism, but the user may want that contrast. When removing a pattern would lose a point the user clearly intended, restructure to preserve the point in a different form rather than deleting it.

**User disagrees with a flag:** If the user says a flagged pattern is intentional, accept it. The skill removes AI artifacts, not personal style choices.
