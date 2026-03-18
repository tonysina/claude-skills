# Verbalized Sampling Examples

Practical examples showing how to apply verbalized sampling and present results naturally to users. Organized by use case.

---

## Ideation & Brainstorming

### Business Ideas

**User request:** "A software developer with expertise in healthcare data wants to start a side business. Give me some ideas beyond the obvious."

**How to present (tail sampling, threshold < 0.10):**

Here are 5 business ideas, ranging from practical to unconventional:

| Idea | Probability |
|------|-------------|
| HIPAA-compliant data visualization dashboards for small medical practices who can't afford enterprise solutions | 8% |
| Consulting service helping health startups pass security audits and compliance reviews | 6% |
| Open-source tools for anonymizing patient data for research use, with paid support tiers | 4% |
| Course teaching other developers healthcare data regulations and best practices | 7% |
| API service that validates healthcare data formats and flags compliance issues before submission | 5% |

### Product Naming

**User request:** "Name options for a mobile app that helps people track and reduce daily water usage."

**How to present (full distribution):**

Here are 7 options from straightforward to unconventional:

1. **AquaSave** (18%) — Clear, descriptive, immediately communicates purpose
2. **DropCount** (14%) — Playful, focuses on the tracking aspect
3. **FlowMinder** (11%) — Gentle, habit-oriented
4. **TapTrack** (9%) — Short, catchy, alliterative
5. **Watershed** (7%) — Double meaning: a turning point + water
6. **Drip** (5%) — Minimalist, one word, trendy feel
7. **Blue Conscience** (3%) — Abstract, emotional, stands out from utility-focused names

---

## Writing & Communication

### Alternative Phrasings

**User request:** "Give me different ways to say 'We need to reduce costs while maintaining quality.'"

**How to present (full distribution):**

Here are 5 alternatives, from conventional to creative:

- "Our goal is to cut expenses without compromising on quality." (22%)
- "We're looking to spend less while keeping our standards high." (18%)
- "The challenge is doing more with less — without sacrificing what makes us good." (9%)
- "Cost efficiency and quality aren't mutually exclusive, and we need to prove that." (6%)
- "We need to find the fat to trim without cutting into muscle." (4%)

### Different Tones

**User request:** "I need to tell my team the project deadline moved up by two weeks. Give me options in different tones."

**How to present (full distribution):**

| Tone | Message | Probability |
|------|---------|-------------|
| Direct/Neutral | "The project deadline has been moved from March 15 to March 1. Please adjust your schedules accordingly." | 30% |
| Empathetic | "I know this isn't ideal news — the deadline has shifted to March 1. I want to work with each of you to figure out what support you need to make this work." | 25% |
| Urgent | "Heads up: we now have two fewer weeks. New deadline is March 1. Let's meet today to reprioritize." | 18% |
| Apologetic | "I'm sorry to share that the deadline has been pulled forward to March 1. I pushed back but wasn't able to hold the line. Let me know how I can help." | 12% |

---

## Planning & Strategy

### Project Approaches

**User request:** "A 10-person team needs to migrate a legacy system to a new platform with minimal downtime. The legacy system has poor documentation. What are some creative approaches?"

**How to present (tail sampling, threshold < 0.10):**

Here are 5 approaches beyond the standard lift-and-shift, each with trade-offs:

1. **Strangler fig pattern** (9%) — Build new features in the new system while gradually routing traffic away from legacy components. Slow but low-risk.
2. **Parallel run** (8%) — Operate both systems simultaneously for 3 months, comparing outputs to catch discrepancies before full cutover.
3. **Reverse-engineer first** (7%) — Spend 4 weeks documenting legacy system behavior through testing and observation before writing any migration code.
4. **Feature-flag migration** (6%) — Migrate user-by-user or feature-by-feature with instant rollback capability. Slower but controllable.
5. **Big bang with safety net** (5%) — Do a hard cutover but keep the legacy system warm for 30 days as fallback. Fast but higher risk.

---

## Analysis & Problem-Solving

### Alternative Interpretations

**User request:** "Website traffic increased 40% last month, but conversion rate dropped from 3.2% to 2.1%. What could explain this?"

**How to present (full distribution):**

Four interpretations, ordered from most to least likely:

**Common explanations:**
- The traffic increase came from a less-targeted source — viral content, broad ads — that brought visitors who weren't purchase-ready. (28%)
- Something on the site broke or degraded (slow checkout, payment issues) that prevented otherwise-willing buyers from converting. (22%)

**Less obvious possibilities:**
- Seasonal browsing behavior: more people researching but not yet ready to buy, like pre-holiday window shopping. (15%)
- Competitor action — a price drop or promotion — made visitors compare-shop on your site but purchase elsewhere. (9%)

### Counterarguments

**User request:** "What are some counterarguments to requiring all employees to return to the office full-time?"

**How to present (full distribution):**

Here are 4 counterarguments from strongest to most nuanced:

1. **Talent pool shrinks** (24%) — Remote work expands hiring beyond commuting distance. A full mandate means losing candidates who won't relocate.
2. **Retention risk** (21%) — Many employees have restructured their lives around remote work — moved, adjusted childcare. Forcing return creates churn.
3. **Productivity evidence** (18%) — Studies show knowledge workers are often more productive at home due to fewer interruptions and no commute fatigue.
4. **Wrong problem** (11%) — Hybrid models preserve collaboration benefits while respecting autonomy. A full mandate may be solving for office culture when the real issue is coordination.

---

## Simulation & Testing

### Dialogue Simulation

**User request:** "Generate plausible responses for this character: Sarah, 34, software engineer. Introverted but passionate about work. Deflects personal questions with humor. Recently went through a difficult breakup but hasn't told anyone at work. Her coworker just asked: 'Hey Sarah, you seem distracted lately. Everything okay?'"

**How to present (full distribution):**

Five plausible responses Sarah might give:

| Response | Probability | Character Notes |
|----------|-------------|-----------------|
| "Oh, you know — just debugging my life one error at a time. Did you see the new API specs? I have thoughts." | 18% | Classic deflection-to-work |
| "Yeah, just... a lot going on. Nothing work-related though. Hey, did you try the new coffee machine?" | 15% | Brief acknowledgment, quick redirect |
| "*laughs* Distracted? I prefer 'selectively focused on things that aren't this conversation.' What's up?" | 12% | Humor as shield |
| "Just tired. Been staying up too late watching terrible reality TV. Don't judge me." | 11% | Plausible cover story |
| "*pauses* I'm fine. Thanks for asking though. Really. So what's on your plate today?" | 9% | Closest to vulnerability, then retreat |

### Test Scenarios

**User request:** "Edge-case test scenarios for a file upload component that accepts images up to 10MB."

**How to present (tail sampling, threshold < 0.10):**

Six edge cases that are easy to miss:

1. Upload exactly 10MB file — boundary condition (9%)
2. Upload 10.001MB file — just over limit (8%)
3. Upload filename with special characters and spaces: "my image (1).jpg" (7%)
4. Upload file with .jpg extension but PNG content — mismatched format (6%)
5. Upload file with no extension (5%)
6. Upload while network disconnects mid-transfer (4%)

---

## Open-Ended QA

### Broad Answer Coverage

**User request:** "Name a US state."

**How to present (VS-Standard, full distribution):**

When the research asks models to generate US states using verbalized sampling, the distribution closely matches how frequently states appear in real-world text (KL divergence of just 0.12 from the pretraining distribution). Direct prompting collapses to California and Texas ~95% of the time.

Example VS output for 5 responses:

| State | Probability |
|-------|-------------|
| California | 15% |
| Texas | 12% |
| New York | 10% |
| Florida | 8% |
| Ohio | 5% |

With tail sampling (threshold < 0.10): Vermont (3%), New Mexico (2%), Delaware (1%), Wyoming (0.8%), Rhode Island (0.5%)

This demonstrates VS's core value: recovering the full breadth of valid answers rather than collapsing to the few most typical ones.
