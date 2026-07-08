---
name: source-check
description: >
  Many-agent verification of factual claims in a draft against primary
  authoritative sources. Spawns one narrow agent per claim (or per source),
  each confirming its claim resolves to a first-hand source rather than an
  aggregator, then consolidates into one report plus a corrected draft.
  Use when the user says "source-check this", "verify these claims",
  "check the sources", "are these stats right", "find the primary sources",
  "audit the citations in this", or asks to confirm authority on a draft's
  claims before it ships. Works on posts, decks, one-pagers, RFP answers,
  ebooks, and any text whose claims need first-hand backing. Heavier the
  more claims there are. Do NOT use to judge whether a sourced fact supports
  the argument, to write the draft, or to fact-check opinions.
metadata:
  version: 1.0.0
---

# Source Check

Verify that every factual claim in a draft traces to a primary authoritative source, by giving each claim its own agent rather than checking them all in one pass.

The job is bounded. Per claim: does a first-hand source say this, in these words, with this number? It does not decide whether the claim earns its place in the draft or proves the point. Those stay with the author.

## Why many agents

One agent asked to check forty claims in a single pass drifts. Early claims get a real source hunt; later ones get pattern-matched against a "sounds right" prior and linked to whatever ranks first. The effect is invisible: the author can't see which claims got rigor and which got a glance.

This skill gives each claim its own agent with a full attention budget and a parallel sibling for the next claim. Claim forty gets the same hunt as claim one. The bottleneck moves to orchestration, which is what cheap parallel agents are for. This is the same structure as a per-citation bibliography audit, scoped to loose inline claims instead of formatted references.

## Requirement: subagents

This skill assumes you can spawn independent agents that run in parallel and don't share context. That's the whole point — context isolation is what stops drift, because no agent has seen the previous thirty-nine claims to get lazy about the fortieth.

**Check your environment first.** If you cannot spawn subagents — for example, you are running inside a single chat context such as a claude.ai conversation — this skill's central mechanism is unavailable, and its value collapses to a checklist over a single-pass check. When that's the case:

1. Say so plainly to the user. Don't pretend the architecture ran.
2. Either run the checks sequentially in your one context with that caveat stated, or tell the user that at low claim volume a clear fact-check prompt does the same job.
3. Never simulate parallelism by checking claims quickly in one context and reporting it as many-agent. A silent fall-back to sequential reintroduces the exact drift this skill exists to remove — that is the one outcome worse than not running at all.

Note that even where subagents are available, they do not automatically inherit this skill. You must pass the relevant reference file path (`references/claim-agent.md`) into each spawned agent's prompt, or the agents will run without the per-claim procedure.

## What counts as a primary source

Rank by distance from the fact:

- **Primary**: the body that produced the number. A statistical agency's own table, the study reporting the finding, a company's own filing, the standards body's own text.
- **Secondary**: someone reporting a primary source. News citing the agency, a blog summarizing the study, a vendor citing a report.
- **Unsupported**: no source locatable, or the located source doesn't say what the claim says.

A claim is verified only against a primary source. Secondary sources are leads to the primary, not the destination. A claim that resolves only to secondary sources is itself a flag.

## The three failure states

Each flagged claim is one of these. Name which; the fix differs.

1. **Secondhand** — a primary exists but the draft rests on something citing it. Fix: cite the primary.
2. **Mismatch** — primary source exists but number, date, or scope is off. Fix: correct to the source.
3. **Unsupported** — no source asserts this. Fix: cut or rebase.

The third is the one single-pass checking misses most: confirming a number exists somewhere, skipping whether the source asserts your version of it.

## Workflow

### Step 1: Initialize the workspace

```bash
python scripts/init_workspace.py <draft-file>
```

This creates a timestamped `source_check_<timestamp>/` tree, copies the draft to `input.md` (the original is never touched), and prints the workspace path. Use that path for the rest of the run.

### Step 2: Extract and split

```bash
python scripts/split_claims.py <workspace>/input.md --out <workspace>/claims/
```

The splitter writes one file per candidate claim plus a `manifest.json`. It is inclusive by design — it flags any sentence with a number, year, money figure, percentage, or attribution phrase, and leaves pure opinion out. Review `manifest.json` and drop any non-claims it caught before spawning agents. If it missed claims (rare, but possible with claims phrased without numbers), re-run with `--all-sentences` and filter down.

A checkable claim asserts something a source could confirm or deny. Opinions, predictions, framing, and rhetorical figures are not claims.

### Step 3: Spawn one agent per claim

For each claim file, spawn an agent and pass it the instructions in `references/claim-agent.md` (paste the file's contents or its path into the agent prompt — subagents don't inherit it automatically). Each agent:

1. Searches for the primary source from the claim's own terms, then narrows to the producing body.
2. Follows any secondary source upstream to its primary.
3. Compares source to claim: number, date, scope, attribution.
4. Assigns one status: verified, secondhand, mismatch, unsupported.
5. Writes a JSON record (schema in `references/claim-agent.md`) to `<workspace>/reports/claim_NNN.json`.

Spawn all claim agents in the same turn for parallelism. Cap concurrency with a max-parallel of 8 if throttled. Each agent runs 1–3 web searches, so a forty-claim draft is roughly forty to a hundred and twenty light searches plus consolidation — real cost, budget for it.

### Step 4: Consolidate

One reviewer agent reads all JSON records in `<workspace>/reports/` following `references/consolidator.md`, and writes into the workspace:

- `source_check_report.md` — grouped by status, failures first.
- `corrected.md` — the draft with mismatches corrected and secondhand citations repointed; unsupported claims marked in place, never silently cut.
- `footnotes.md` — first-comment-ready source lines for the verified claims.

The skill never overwrites the source draft. The author reviews the report and moves `corrected.md` into place.

### Output tree

```
<draft_dir>/source_check_<timestamp>/
  ├── input.md
  ├── claims/              # one file per claim + manifest.json
  ├── reports/             # per-agent JSON
  ├── source_check_report.md
  ├── corrected.md
  └── footnotes.md
```

## Modes

**Per-claim** (default): one agent per claim. Catches a single bad stat.

**Per-source**: one agent per distinct source, each checking every claim that leans on that source. Catches the systematic version — one report cited five times with one stretch. Run it when a draft leans hard on few sources, or as a second pass over claims the per-claim run flagged unsupported. The per-source variant instructions are in `references/claim-agent.md`.

Run both when a draft is going somewhere it can't afford a sourcing error.

## What this does not do

- Judge whether a verified claim supports the argument. A real number can be the wrong one to cite.
- Write or rewrite the draft beyond mechanical correction in `corrected.md`.
- Check opinions, predictions, or framing.
- Catch a claim the draft should have made but didn't.

## Reference index

| File | When to read |
|------|-------------|
| `references/claim-agent.md` | Spawning per-claim or per-source agents |
| `references/consolidator.md` | Running the reviewer/consolidation pass |
