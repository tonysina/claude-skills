---
name: great-demo
description: >
  Apply Peter Cohan's Great Demo! method to design, critique, and qualify
  software demonstrations. Use when the user asks to plan a demo, build a
  demo script or outline, critique an existing demo, qualify a prospect,
  build a Chain of Pain, calculate the Delta, or handle special-case demos
  (trade show, large unqualified group, remote, scripted RFP). Triggers on
  "design a demo", "critique this demo", "is this demo any good", "Chain
  of Pain", "what is their CBI", "Specific Capability", "Illustration",
  "Situation Slide", "Do It / Do It Again", "Not Now List", "To Do List",
  "do the last thing first", "remote demo", "trade show demo". Product-
  agnostic. Do NOT use for general slide decks or thought leadership (use
  good-presentations); do NOT use for evaluation management or Sequence
  of Events work.
metadata:
  version: 1.0.1
---

# Great Demo

Apply the Great Demo! method to plan, sharpen, and recover software demos.

## Two Non-Negotiable Principles

These are the bedrock. Every recommendation in this skill ties back to them.

**1. Do The Last Thing First.** Show the most compelling result in the first two minutes. Then walk through how you got there in under four minutes. Then let the audience pull you into depth. The newspaper-article structure: headline first, summary lead next, deep body last. The audience self-selects depth. You don't have to show everything.

**2. CBI to Reason to Specific Capability.** Every capability shown must trace back to a customer's Critical Business Issue. A capability with no CBI behind it is a feature parade, and feature parades lose deals. Pain flows down the org chart. Gain flows up. If you can't name the CBI a screen addresses, cut the screen.

If a request would violate either principle, say so plainly before producing the work the user asked for.

## Mode Detection

Read the user's request and route to the right mode. If it spans modes, name them and ask which to tackle first.

| User intent | Signals | Load |
|---|---|---|
| Design a new demo | "design a demo", "build a demo for", "plan a demo", "structure this demo", "outline a demo", prospect context with goals | `references/design.md` |
| Critique an existing demo | "critique this demo", "review my demo script", "is this demo any good", "what's wrong with this demo", "score this against Great Demo!" | `references/critique.md` |
| Pre-demo qualification | "qualify this prospect", "build a Chain of Pain", "what's their CBI", "what's the Delta", "Demo Information Sheet" | `references/qualify.md` |
| Live-demo delivery questions | "Not Now List", "To Do List", "handle a Stupid Question", "buzzwords", "mouse movement", "recover from a crash", "what to do when X happens mid-demo" | `references/delivery.md` |
| Special-case demo | "trade show demo", "large unqualified group", "remote demo", "scripted RFP demo", "deployment demo", "canned demo", "Generic Demo" | `references/special-cases.md` |
| Term lookup | "what does CBI mean", "define Specific Capability", "what's an Illustration in Great Demo!" | `references/glossary.md` |

If unsure: ask one question to disambiguate. Don't guess silently when the request is ambiguous between modes.

## Universal Pre-Work

For Design and Critique modes, you need this minimum context. If the user hasn't supplied it, ask before drafting.

- Audience: who is in the room, job titles, decision authority
- Time budget: how many minutes for the demo segment
- CBI per stakeholder: what they each need to solve
- Specific Capabilities being demonstrated: the agreed list
- Demo objective: Technical Proof or Vision Generation (Cohan rules out Information demos)

Gaps are normal. Flag the gap, propose an assumption, proceed if the user confirms. Never proceed silently on a missing CBI; it's the load-bearing input.

## Output Norms

Different modes produce different output, but a few rules apply across all of them.

State concrete time estimates against Cohan's targets, not vague ranges. Cohan's single-solution timeline:

| Segment | Target |
|---|---|
| Introduction | 1-2 min |
| Illustration | 1-2 min |
| Do It | 1-2 min |
| Do It Again | 5-10 min |
| Q&A | 5-10 min |
| Summary | 2-4 min |
| **Total** | **15-30 min** |

If a draft exceeds 30 minutes for a single solution, name it and recommend the cut.

Quantify the Delta whenever possible: in money, time, or people. Not in features. "3 days with 4 people becomes 1 day with 1 person, 11 person-days saved per cycle, 20 cycles per year, 220 person-days saved per year" beats "much faster" every time. If the user has no numbers yet, surface the missing measurement and suggest the question that would extract it.

Flag buzzwords. The Content-Free Buzzword-Compliant list (robust, powerful, flexible, integrated, seamless, extensible, scalable, interoperable, easy-to-use, intuitive, user-friendly, comprehensive, best-of-breed, world-class, cutting-edge) erodes credibility. Replace with concrete facts: "10,000 users in production worldwide" beats "robust"; "3 clicks to complete the task" beats "easy-to-use." When critiquing, point them out by name.

## Bundled Templates

The `assets/` directory holds reusable templates from the book's appendices. Pull them down when the user wants a working artifact rather than a free-form draft.

| Asset | Use when |
|---|---|
| `assets/demo-information-sheet.md` | Capturing CBI/Reason/Specific Capability per stakeholder, plus the Delta and meeting objective |
| `assets/situation-slide-template.md` | Building the slide that precedes the Illustration |
| `assets/meeting-information-sheet.md` | Logging meeting logistics, agenda, and roles |
| `assets/infrastructure-checklist.md` | Pre-demo hardware, software, network, AV verification |

## Reference Index

| File | When to read |
|---|---|
| `references/design.md` | Building a new demo from prospect context |
| `references/critique.md` | Scoring an existing demo against the Great Demo! rubric |
| `references/qualify.md` | Pre-demo discovery: CBI/Reason/SC, Chain of Pain, Delta calculation |
| `references/delivery.md` | Live-demo techniques: question handling, language, mouse, props, bug recovery |
| `references/special-cases.md` | Trade show, large unqualified, remote, scripted RFP, deployment, canned demos |
| `references/glossary.md` | Definitions of Cohan's terms |
| `references/changelog.md` | Skill version history |

## Critical Habits

A few habits matter enough to repeat at the top level.

**Always end every segment with the strongest Illustration screen on display.** It's the last image the audience takes home. If a demo ends on a settings page or a default view, the audience remembers the settings page.

**Never use keyboard shortcuts in a live demo.** The audience needs to see menu choices to envision themselves doing it. Shortcuts break the vision.

**Use the customer's name in file names, never "demo" or "test."** Realistic names build the vision of real use.

**Restate every question before answering.** It identifies the questioner, gives you a beat to think, and turns the answer into a personalized 1:1 dialog.

**The Not Now List is the question-management tool.** Acknowledge sincerely, write publicly, ask "is that OK with you?", and answer it later without fail. Failing to answer a Not Now List item leaves an open wound that can cost the sale.
