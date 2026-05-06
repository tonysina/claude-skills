# Demo Design

How to build a demo from prospect context using the Great Demo! method.

## What You Need Before Drafting

Six inputs. If any are missing, ask the user before proceeding. Do not invent them.

1. **Audience**: each person's name, title, role, decision authority
2. **CBI per stakeholder**: the Critical Business Issue each person owns
3. **Reason per CBI**: why they can't currently solve it
4. **Specific Capabilities to demonstrate**: the agreed list, mapped to CBIs
5. **Time budget**: total minutes for the demo segment
6. **Demo objective**: Technical Proof (prove specific capabilities to close the technical sale) or Vision Generation (help customer envision the solution). Cohan rules out Information demos as too risky.

If the user has only some of these, build what you can and flag the gaps explicitly. A demo built without a CBI is a feature parade in disguise.

## The Five-Step Strategy (Single Solution)

This is the core flow. Every demo segment runs through these five steps in order.

1. **Present the Illustration, Summarize.** Show the wow screen. Two minutes. Audience asks "How did you do that?"
2. **Do It, Summarize.** Walk through the path to the Illustration. Fewest mouse clicks possible. One to two minutes. No side trips.
3. **Do It Again, Summarize.** Same pathway, now with detail, options, and explanation. Five to ten minutes.
4. **Q&A.** Address the Not Now List items.
5. **Summary.** Recap each Specific Capability and how it addresses the customer's CBI.

End every step with the strongest Illustration screen on display.

## The Outline (What, Not How)

The Outline is a short list of building blocks in order. It is the agenda. The Introduction reads it out loud.

Single-solution outline:

1. Introduction
2. Present the Illustration
3. Do It (rapid pathway), with brief summary
4. Do It Again (detailed pathway), with brief summary
5. Q&A
6. Final Summary

Multiple-solution outline: present **all** Illustrations upfront before handling each solution in turn. The audience sees every payoff before any path. Then for each solution: re-present Illustration, Do It, Do It Again, summarize. Then a final summary across all, then Q&A, then a closing summary.

## Building the Illustration

The Illustration is the most important screen in the entire demo. It's the headline.

Selection rules:

- Pick the screen that triggers "How did you do that?"
- The completed report on the chemist's desk, the finished invoice, the rendered dashboard, the cleared-out alert queue: artifacts the audience already wants
- Indicators it's strong: audience leans in, asks how, asks if it'll work with their data
- Indicators it's weak: nods, polite questions, "interesting" with no follow-up

If the user proposes a generic feature screen as the Illustration, push back. The Illustration must show **outcome**, not capability.

Multiple Illustrations work hard. Three escalating Illustrations (baseline, improved, knock-their-socks-off) can drive an audience from "How did you do that?" to "Please show us how you made those, now!"

## Building the Situation Slide

The Situation Slide goes immediately before the Illustration. It re-establishes the customer's situation and sets the scene.

Contents:

- Company name and job title of the key player
- CBI
- Reasons (the sub-problems blocking the CBI)
- Specific Capabilities that address those Reasons
- The Delta (Cheaper, Better, Faster, or Couldn't Be Done Before, expressed in money, time, or people)

For Technical Proof demos: use the customer's actual situation (gathered in qualification). For Vision Generation demos: use a Reference Story (a sanitized situation slide reused from a past success with the same job title at a different company). If the audience reacts strongly to a Reference Story, pivot the conversation to their specific situation immediately and qualify before continuing.

The Situation Slide template lives in `assets/situation-slide-template.md`.

## Building the "Do It"

The Do It is the fewest mouse clicks required to go from launching the software to generating the Illustration. The straight line. No extra explanations, no side trips. Most Do It segments take one to two minutes.

Construction rules:

- Count the clicks. Reduce them. Every click the audience sees is a step they think they'll have to perform.
- Organize demo files in top-level directories or desktop icons. Burying the file under five folders adds five clicks the audience will remember.
- Use the customer's name or company name in file names. Never "demo," "test," "demo1," "demo2." Realistic names build the vision of real use.
- Never use keyboard shortcuts. The audience needs to see menu choices to envision themselves doing it.
- End the Do It on the strongest Illustration screen. Leave it up during the brief summary and the questions that follow.

The Do It proves two things at once: (1) your software can achieve the Illustration, (2) it's fast and easy. The audience feels the second one viscerally; that's where emotional buy-in comes from.

## Building the "Do It Again"

The Do It Again is the same pathway, walked more deliberately, with options and detail. Five to ten minutes typical.

Construction rules:

- Address the questions raised during the Do It. Most "Great Questions" from the first pass become natural beats here.
- Stay focused on the Specific Capabilities. Don't drift into unrelated features just because they're cool.
- Use the Do It Again to show breadth, more complex examples, and flexibility within the Specific Capabilities.
- End on the strongest Illustration screen and leave it up.

A useful axiom: the first demo to a customer generates a set of questions. The second demo to a similar audience generates roughly 80 percent of the same questions. Those overlapping questions are excellent feedstock for future Do It Again sections. One real demo gives you enough material to refine the second pass.

## The Introduction

The Introduction reads the Outline out loud. It tells the audience exactly what's coming and in what order.

Two questions to ask at the start, even if you already know the answers:

1. What does the customer want to accomplish in this meeting?
2. What are their time constraints?

Asking shows respect and catches changes since the agenda was set. Things shift between the meeting agreement and the meeting itself.

## Timing

Cohan's single-solution timing:

| Segment | Target |
|---|---|
| Introduction | 1-2 min |
| Illustration | 1-2 min |
| Do It | 1-2 min |
| Do It Again | 5-10 min |
| Q&A | 5-10 min |
| Summary | 2-4 min |
| **Total** | **15-30 min** |

If the demo is too long: trim Do It Again first, then drop lower-priority Specific Capabilities. If the demo is too short: confirm the Illustration genuinely lands and check no Specific Capability got skipped. If everything's covered, leave it alone. Audiences appreciate meetings that finish early.

## Practice and Rehearsal

The amount of practice should be proportional to the deal value.

- Memorize the demo. Don't read a script.
- Time it without questions, then add Q&A buffer.
- Run a full rehearsal with the Selling Team. Other team members play audience and surface gaps.
- Take rehearsal feedback. Make agreed changes. Resist the urge to add capabilities. Stay focused on the agreed Specific Capabilities.
- Confirm infrastructure with the customer before traveling. Ask: have meeting objectives changed, are there new audience members, are there new time constraints?

## Worked Example: Designing from Sparse Inputs

User says: "Help me design a 30-minute demo for the VP of Operations at a regional hospital. Their CBI is reducing time-to-diagnosis in the ED."

What to do:

1. Confirm what's known and what's missing. Known: audience (VP Ops), time (30 min), CBI (reduce time-to-diagnosis). Missing: Reason behind the CBI, Specific Capabilities, demo objective, other stakeholders.
2. Surface the gaps. Ask the user to fill in the Reason and the Specific Capabilities, or propose plausible defaults and flag them as assumptions.
3. Once filled in: build the Situation Slide (job title, CBI, Reason, Specific Capability, Delta). Build the Illustration (probably the patient throughput dashboard or a triaged-case view). Sketch the Do It pathway in click-count terms. Time-box each segment against Cohan's targets.
4. Output: a structured demo plan with timing, the Situation Slide content, the Illustration choice with rationale, the Do It click sequence, the Do It Again expansions, and the planned summary language.

Don't draft an entire 30-minute monologue. Output the structure with talking points. The user's voice fills in the language during delivery.
