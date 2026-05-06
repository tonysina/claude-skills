# Pre-Demo Qualification

How to capture the CBI/Reason/Specific Capability framework, build a Chain of Pain, and quantify the Delta before any demo gets built.

## The Core Framework

Three terms, one chain. Memorize the order.

**CBI (Critical Business Issue)**: each person's key annual or quarterly objective. Stated in their own terms. Examples:

- "Unable to achieve quota this quarter" (Salesperson)
- "Unable to reduce average ED time-to-diagnosis below 90 minutes" (VP Operations, Hospital)
- "Unable to consolidate vendor contracts before fiscal year-end" (CFO)

**Reason**: the sub-problem(s) blocking the CBI. Specific. Examples:

- "Demonstrations are not closing the technical sale" (Reason behind Salesperson's CBI)
- "Patient triage takes too long because of paper-based intake" (Reason behind VP Ops's CBI)
- "No central view of contract terms across business units" (Reason behind CFO's CBI)

**Specific Capability**: what your product does that addresses the Reason. Concrete, demonstrable. Examples:

- "Demo-skill methodology and clear elucidation of CBIs to the SE"
- "Mobile-tablet triage form with auto-routing to the on-call physician"
- "Cross-business-unit contract repository with side-by-side term comparison"

The chain runs CBI to Reason to Specific Capability. Anything you demonstrate should sit at the third position with the first two named.

## "No Pain, No Change"

If the customer is not in pain, they will not change. The qualification work is essentially pain discovery. If you can't surface a CBI, the demo will not close.

The single most useful qualification question: "Tell me, what is the biggest challenge you face in your job today?"

This question gets a physical response every time. The person leans forward, exhales, picks one. Whatever they pick is the CBI.

For junior staff who can't articulate a CBI directly, ask: "How are you measured? How do you know you deserve a raise?" That surfaces the CBI indirectly.

If you're walking into a demo without CBI/Reason information: invest the first few minutes of the meeting asking. Cohan's words: "It is far better to delay or sacrifice a few demonstration minutes than to give a poor or unsuccessful demonstration."

## The Chain of Pain

Pain flows down the org chart. Gain flows up. Senior people's Reasons become junior people's CBIs.

Worked example for a software vendor selling to a software company:

| Role | CBI | Reason |
|---|---|---|
| CEO | Unable to increase shareholder value (stock price) | Quarterly revenues and profits below analyst expectations |
| VP Sales | Unable to achieve quarterly corporate revenue targets | Salespeople as a whole not achieving quotas |
| Salesperson | Unable to achieve quarterly quotas | Product demonstrations fail to close the technical sale |
| SE | Unable to produce demonstrations sufficient to close the technical sale | Lack of demonstration skills and understanding of customer CBIs |

The VP Sales's Reason ("salespeople not achieving quotas") becomes the Salesperson's CBI ("unable to achieve quarterly quotas"). The Salesperson's Reason ("demos fail to close") becomes the SE's CBI ("unable to produce sufficient demos"). That's the chain.

Why this matters for demo design: when you demonstrate a Specific Capability that addresses the SE's CBI, the value implicitly addresses the Salesperson's Reason, the VP Sales's Reason, and ultimately the CEO's CBI. Gain flows up. Tying a capability to a single low-level CBI lets you make a credible case for executive impact.

Senior people can articulate CBIs more precisely than junior people. Start at the top of the chain when possible.

## Building the Chain of Pain (Procedure)

Given a list of stakeholders and any starter information:

1. List every audience member with name, title, and decision authority.
2. For each one, write down their CBI in their own words. If you don't know it, write "[unknown — qualify]" and note the question to ask.
3. For each CBI, write the Reason(s) blocking it. If unknown, mark and note the question.
4. For each Reason, identify the Specific Capability your product offers that addresses it.
5. Cross-reference: does the VP's Reason match the Manager's CBI? The Manager's Reason match the IC's CBI? If so, the chain is intact. If not, you have either a discovery gap or a real organizational mismatch worth flagging.
6. Identify the Champion: the person who will actively support the purchase. Map their position in the chain.

Output goes into the Demo Information Sheet (`assets/demo-information-sheet.md`).

## Quantifying the Delta

The Delta is the measurable difference between how the customer does it today and how they'd do it with your solution. Express it in money, time, or people. Never in features.

Cohan's four measure types:

- Cheaper
- Better
- Faster
- Couldn't Be Done Before

A worked example from the book:

- Customer's current process: "2 weeks, 4 people" per cycle
- Future state with the product: "2 days, 2 people" per cycle
- Cycles per year: 20
- Delta per cycle: (10 days × 4 people) - (2 days × 2 people) = 40 - 4 = 36 person-days
- Delta per year: 36 × 20 = 720 person-days
- Burdened FTE rate: $100K
- Annual value: (720 / 200 working days per year) × $100K = **$360,000 per year**

The numbers must come from the customer. Your job is to ask the questions that produce them. The book's two-question pair:

1. "How long does your process take today?"
2. "What do you need this to become?"

The gap is the Delta.

Err conservative when stating the Delta back to the customer: "I believe you can achieve X. It may be possible to do even better, but that will depend on your implementation." Overstating the Delta poisons trust if the actual implementation falls short. Understating builds credibility.

Quantify both direct value (the 720 person-days) and indirect value (what else those people could do with the time). The indirect value sometimes dwarfs the direct.

## Workflow Mapping

When you can sit with the customer, get them to draw their workflow on a whiteboard. Hand them the pen. Take notes. Ask follow-ups.

What you'll learn:

- Bottlenecks and problem areas
- What currently works (don't change it; this is where you avoid breaking what's not broken)
- People and relationships involved at each step
- Time per step
- Other processes impacted
- Vocabulary and acronyms specific to that customer
- How workflow output is reported (this often becomes the Illustration)

Workflow mapping doubles as relationship-building. The customer feels heard. The Champion gets stronger.

After the workflow, ask the customer to articulate the Solution they want: which steps to eliminate or change, what output format they need, what new dashboards or alerts.

## Direct vs. Indirect Research

**Direct Research**: contact the customer, ask questions. Best source of CBI/Reason information. Always get explicit agreement to use their data in the demonstration. Determine whether an NDA is needed. Direct Research builds an Earned Reputation: trust and efficacy generated by handling customer information well.

**Indirect Research**: when the customer can't or won't share. Less targeted but better than nothing. Sources:

- Customer's website (workflows, output illustrations; public, no confidentiality risk)
- Papers and publications (search by person, company, topic; can warm a cold contact)
- Patents (rich examples and search terms)
- Customer's competition (public information may be relevant across accounts)
- Your competition (only if you're clearly superior and confident they don't know your method)

## The Pro-Tip Question

At the end of any qualification session: "Is there anything I should be asking that I haven't yet asked?"

This often surfaces the most important piece of context in the entire conversation. Ask it every time.

## Output: The Demo Information Sheet

Once you have the chain mapped and the Delta calculated, produce the Demo Information Sheet (template in `assets/demo-information-sheet.md`).

Required fields:

- Each audience member: name, job title, CBI, Reason(s), Specific Capabilities
- The Delta in money/time/people terms
- Meeting objective (Technical Proof or Vision Generation)
- Meeting date, location, time, duration

This sheet is the single most commonly skipped artifact in real selling. Cohan: information is typically shared "in the car, in the parking lot, at the customer's site." That's why so many demos miss the target.

Hand the completed sheet to the SE before the demo gets built. Reach explicit agreement on which Specific Capabilities will be shown and which will not.

Axiom: "No surprises, thank you very much."

## When the Customer Won't Engage in Qualification

Some customers refuse to share. Reasons vary: NDA concerns, internal politics, competitive sensitivity, simple wariness of vendors.

Options:

1. Lean on Indirect Research and propose a Reference Story (a sanitized situation from a similar customer at a different company). Watch their reaction; if they engage, the Reference Story is doing the qualification work for you.
2. Use the Menu Approach (covered in special-cases.md): present three to five Situation Slides drawn from likely scenarios for their industry and job title; let them pick the one that resonates.
3. Decline the demo. If you genuinely can't establish a CBI, an Information demo is high-risk and Cohan recommends against it. Surface the gap to the Salesperson and propose more discovery before committing to a demo slot.

## Worked Example: Building a Chain from Sparse Notes

User input: "Demo next Tuesday for the City of Glendale. Bill Rand is the buyer. He cares about APM lifecycle, hosting/cloud, rationalization, and capability management. Mixed audience: technical and non-technical."

What to produce:

1. Stakeholder list with what's known and what's missing. Bill Rand is identified; other audience members "[unknown — ask]."
2. Bill's CBIs (plural, since he named four areas):
   - APM lifecycle: presumably "unable to retire applications on schedule" or "unable to track which applications are at end-of-life"; mark as inferred and ask to confirm.
   - Hosting/cloud: presumably "unable to optimize hosting costs" or "unable to consolidate redundant cloud spend"; mark as inferred.
   - Rationalization: presumably "too many overlapping applications, unclear which to keep"; mark as inferred.
   - Capability management: presumably "unable to map applications to business capabilities" or "no shared view of what the business does and how"; mark as inferred.
3. Reasons for each: marked as "[needs discovery]." Recommend specific questions to extract them in pre-demo conversation.
4. Specific Capabilities tied to each (drawn from the product the user is selling; if not specified, leave abstract: "capability that addresses [Reason]").
5. Delta: marked as "[needs discovery]." Recommend the two-question pair: "How long does X take today?" and "What do you need this to become?"
6. Open question to surface to the Salesperson: who else will be in the room, and what are their CBIs? A "mixed audience" with no other names is a qualification gap.

Output is the partially-filled Demo Information Sheet plus a discovery question list to close the gaps.
