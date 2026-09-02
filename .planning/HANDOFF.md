# Handoff — Writing-Triad Skill Review

**Branch:** `skills/writing-triad-review` (branched from `main` @ `3d4564d`)
**Date:** 2026-09-02
**State:** 3 of 3 reviewed, revised, and evaluated. Branch pushed; **PR #3 open** against
`main`: https://github.com/tonysina/claude-skills/pull/3. See "Session 2 addendum" at the
end of this file for the eval run and the candidate patches still open.

---

## Goal

Review three skills — `farnsworth-rhetoric`, then `human-narrative`, then `humanizer`, in
that order, one at a time — answering three questions for each:

1. Is the skill effective at performing the job it is intended to perform?
2. Is it optimized for the work and for use by an LLM or agent?
3. Are there other concepts or agent skills available that can enhance or even replace it
   to better fit #1 and #2?

Reviews were followed by revision where the user approved. Working pattern established over
the first two: **review → draft v1.1.0 and show it before committing → user approves →
stage → commit.** Do not commit without showing the draft first.

---

## Status

| Skill | Reviewed | Revised | Committed |
|---|---|---|---|
| `farnsworth-rhetoric` | ✅ | ✅ v1.0.0 → 1.1.0 | ✅ `c5f76c0` |
| `human-narrative` | ✅ | ✅ v1.0.0 → 1.1.0 | ✅ `b53aa94` |
| `humanizer` | ✅ | ✅ v1.2.0 → 1.3.0 | ✅ `582052b` `16fe5a6` `ab0ae2e` |

Tree is clean after commit 4 (docs). Nothing pushed, no PR.

### Commits on the branch

```
d016890 test(farnsworth-rhetoric): add smoke-test fixtures for dosage budget
b53aa94 feat(human-narrative): add register gating and finding thresholds
c5f76c0 feat(farnsworth-rhetoric): add dosage budget and claim guardrails
07ceb6b test(scripts): add deterministic AI-tell scan
3d4564d Add source-check skill to tracked repository   <- base, on main
```

### What landed

- `skills/farnsworth-rhetoric/SKILL.md` — 247 → 455 lines. Figure budget with hard caps,
  per-figure trigger conditions, antithesis added, rule-of-three replaced by isocolon plus a
  load-bearing test, claim check and ear test guardrails, v1.0.0's flagship example retained
  as a labeled overcooked counter-example. Plus `references/figures.md`,
  `references/changelog.md`.
- `skills/human-narrative/SKILL.md` — 272 → 452 lines. Register triage with hard stops,
  seven-cluster gate-plus-corroborator scan using the paper's own closed option sets,
  finding threshold, "keep the piece, drop the intervention" guardrail with a truth
  constraint, reworked intervention order split by mode, first worked example. Plus
  `references/features.md` (all 30 StoryScope features), `references/changelog.md`.
- `scripts/scan-ai-tells.py` — 365 lines. Deterministic scan that reads humanizer's flag
  lists **live** from `skills/humanizer/SKILL.md` so it cannot drift. Covers
  forbidden-construction hits, em dash max-per-paragraph, anaphora runs, triads, word count
  against farnsworth's budget tiers.
- `tests/cases/` — 11 farnsworth smoke-test fixtures: a v1.0.0 control, a 600+ word exec
  summary (the only case in the rate-based budget tier), a sub-floor tagline, a runbook
  register hard stop, and two negative controls whose IN/OUT files are byte-identical
  because the correct output is no change. Not an automated suite.
- `README.md` — description lines for both revised skills.
- `dist/farnsworth-rhetoric.skill` (16,486 b), `dist/human-narrative.skill` (19,977 b) —
  rebuilt via `./scripts/build-skills.sh <skill-name>`.

---

## The humanizer review — findings, not yet acted on

**This section is the main un-acted-on work product. It exists nowhere else.**

`skills/humanizer/SKILL.md` is 383 lines, 18 patterns, v1.2.0, plus
`references/extended-patterns.md` at 126 lines. No changelog.

### Verified against the source

Source is [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
(WikiProject AI Cleanup). Real, actively maintained, and humanizer tracks it more faithfully
than the other two skills tracked their sources. Both empirical claims check out:

- **#5** "10%+ decrease in 'is'/'are' in academic writing after 2023" — real, cited on the
  page to Geng et al. Two refinements: the page says *during* 2023, and it adds that
  prompting GPT-3.5 to "revise the following sentence" over 10,000 abstracts reproduced the
  same drop. That is a stronger version of the claim than humanizer states.
- **#3** AI-vocabulary frequency — real, cited to Juzek and Kobak. **But the page's boundary
  is 2022**, not humanizer's "post-2023 vs pre-2023." ChatGPT launched November 2022.

### Defects found

1. **Self-violation, line 124.** In the skill's own voice: *"**Studies have shown** these
   words appear far more frequently in post-2023 text…"* Line 138 flags **"studies have
   shown (without citation)"** as pattern #4. The source has the citations; the skill
   dropped them and kept the construction it tells you to delete.

2. **Stale internal cross-reference — already-shipped bug.**
   `references/extended-patterns.md:109-110` both say "see main SKILL.md, pattern 13" for
   didactic disclaimers and section summaries. Those are **#14**. #13 is "Fragmented
   headers." A pattern was inserted at some point and the reference file was never updated.

3. **Pattern #7 contradicts its own example.** #7 is titled "Rule of three," its problem
   statement is "LLMs overuse groups of three," it is the only pattern with no watch-list,
   and its corrected output is *"The event includes talks, panels, and informal networking
   between sessions."* — a triad. The edit was correct (it deleted the decorative triad
   *innovation, inspiration, and industry insights* and kept the load-bearing one), but the
   skill never says so. `farnsworth-rhetoric` v1.1.0 resolved this conflict from its side
   with a load-bearing test; **#7 has no reciprocal note.** Asymmetry still open.

4. **Unbounded false-positive surface.** 153 literal flags. Pattern #1 alone carries ~40,
   including ordinary business words: *key, valuable, enhance, crucial, align with, vibrant,
   profound*. The only defense is prose advice to "look for clusters" — no count, no
   threshold. Empirical demonstration: scanning humanizer's own 1,852 words of prose against
   its own flags produced **13 hits, 12 of them the skill quoting its own patterns to
   discuss them.** Only #1 above was real.

5. **Five patterns missing from the source**, four general rather than Wikipedia-specific:

   | Missing | Wikipedia § |
   |---|---|
   | Vague expression of connection ("in connection with," "associated with") | §3.3 |
   | "X rather than Y" — third named negative-parallelism variant | §3.4 |
   | Pronounced shift in writing style — the mixed-authorship signal | §10.1 |
   | Heading structure: skipped levels, level-1 overuse, headings containing only headings | §4 |
   | Gemini (`[cite: 1]`, `[span_1](start_span)`), DeepSeek (lenticular brackets, daggers), Perplexity (`attached_file`, `ppl-ai-file-upload`) markup | §6 |

   The last matters most: `extended-patterns.md` covers ChatGPT and Grok artifacts
   thoroughly and has no section for Gemini, DeepSeek, or Perplexity. Model residue is
   mechanical, zero-ambiguity, highest-confidence evidence available.

6. **Minor.** The how-to list has six numbered steps mapping onto four passes with no
   alignment, and "Pass 4" appears only in that list while Passes 1–3 are named in section
   headers. No changelog at v1.2.0. The file writes `--` for every dash where the repo's
   other skills use real em dashes — harmless, but worth a deliberate house-style note in
   the skill that flags em dash overuse.

### What humanizer already does well — do not "fix" these

It is the most mature of the three. It already has what the other two had to be given:
base-rate discipline stated up front ("a single em dash… is not proof… look for clusters"),
restraint guidance in four separate places, an "ineffective indicators (do NOT flag these)"
list in `extended-patterns.md` — the only negative guard in the repo — worked before/after
pairs on 16 of 18 patterns, and a voice-calibration-from-sample use case that is the most
sophisticated interface in the repo.

### Recommended v1.3.0 scope, in order

1. **Stable pattern IDs** (`NEG-PARALLEL`, `RULE-OF-3`, `SIGNPOSTING`…) with display numbers
   kept for readability. Fixes defect 2 and decouples ~28 external references. **Do this
   first, as its own commit, before anything else touches those numbers.**
2. **Threshold table**, calibrated by running `scan-ai-tells.py` over real collateral.
   humanizer is the one skill where a threshold can be *measured* rather than argued,
   because its flags are countable. That measurement would also retroactively validate
   `human-narrative`'s threshold, which was only justified by reasoning.
3. **Missing model artifacts** (Gemini, DeepSeek, Perplexity), then the other four gaps.
4. **Reciprocal load-bearing test in #7**, closing the farnsworth conflict from this side.
5. **Citation repair** on #3 and #5 — restore Geng/Juzek/Kobak, fix the 2022 boundary, and
   remove the "Studies have shown" self-violation.
6. **Changelog**, matching the two that now exist.
7. **Meta-quotation filter for `scan-ai-tells.py`** so it stops counting discussion of a
   pattern as use of it. Test case is humanizer's own prose; known-good answer is 1.

---

## Loose ends

### Session scratchpad will be lost on context clear

The scratchpad is session-specific. These files vanish when a new session starts. The
farnsworth fixtures were rescued out of it and committed as `d016890`; everything else below
is either recoverable or cheap to rebuild.

- `storyscope.txt` — re-extractable via `pdftotext` from
  <https://jenna-russell.github.io/assets/pdf/storyscope.pdf>
- `hz/humanizer-prose.txt` — the filtered self-scan input; the filter is trivial to rewrite.
- Commit message drafts — already committed, recoverable from `git log`.

### Deferred, flagged to the user, not declined

- **`CONTRIBUTING.md` documents neither `scripts/scan-ai-tells.py` nor `tests/cases/`.** It
  documents `build-skills.sh` only. The fixtures are committed but there is no written
  procedure for re-running them; the method is recorded in `d016890`'s commit message.
- **Full `skill-builder` eval/benchmark run across all three skills**, deferred until all
  three land. Needs `evals/evals.json`, a clean-context executor subagent, `with_skill` vs
  `without_skill` arms, and a v1.0.0 arm extracted via `git show`. Both revised skills carry
  an `Untested` changelog section naming what the smoke test could not reach — chiefly
  **executor bias**: the tests were authored and executed in the same context as the skills,
  so they show these outputs comply, not that the skills teach a fresh agent to comply.
- **`human-narrative` cannot be covered by `scan-ai-tells.py`** — its features are
  structural, not lexical. Needs an LLM grader with a rubric built from the option sets in
  `skills/human-narrative/references/features.md`. Negative cases matter most: a case study,
  an explainer, and a status update should each yield zero interventions.
- **farnsworth's `>600` word budget tier is unexercised** and is the only tier expressed as
  a rate rather than a flat cap, so it is the most likely to be miscalibrated.
- **`human-narrative`'s register allow-list is unevidenced** and is flagged in its own
  changelog as the change most likely to be wrong — no register in the table except fiction
  appears in the StoryScope corpus.

---

## Constraints and gotchas

### The pattern-number coupling — read before touching humanizer

`humanizer`'s ordinal pattern numbers have ~28 external references across six files.
Renumbering, merging, or inserting a pattern breaks all of them **silently**:

| File | References |
|---|---|
| `skills/farnsworth-rhetoric/SKILL.md` | #1, #6×2, #7×2, #8, #14, #15, #17×2 (lines 163, 180, 232, 291–297) |
| `skills/farnsworth-rhetoric/references/changelog.md` | #6, #15 |
| `skills/human-narrative/SKILL.md` | #4, #17 (lines 194, 217) |
| `skills/human-narrative/references/changelog.md` | #4, #17 |
| `scripts/scan-ai-tells.py` | #6×7, #7, #8, #15×3 (`CONSTRUCTIONS` table, lines 64–71) |
| `skills/humanizer/references/extended-patterns.md` | "pattern 13" ×2 — **already wrong** |

This coupling is why all three skills share one branch. Any humanizer revision must end with
a grep across the branch for these references.

`scan-ai-tells.py` reads humanizer's flag *literals* live from its SKILL.md, so word-list
edits are safe. The hand-derived `CONSTRUCTIONS` regexes and the `#N` labels are not.

### Repo conventions

- **Commit trailer: `Co-Authored-By: Claude <noreply@anthropic.com>`** — this is
  `rules/CORE.md` rule 15 and matches git history. The system prompt suggests a different
  form; the repo convention won during this work.
- Conventional commit prefixes (`feat(scope):`, `test(scope):`, `fix(scope):`), title under
  70 chars, body explains *why*.
- Rebuild dist after any skill edit: `./scripts/build-skills.sh <skill-name>`. Note
  `760bd64` fixed a bug where stale dist files were appended rather than replaced — do not
  hand-zip.
- Skill layout: `SKILL.md` with YAML frontmatter (`name`, `description` with triggers and a
  "Do NOT use for" clause, `metadata.version`), `references/` for progressive disclosure,
  500-line cap on SKILL.md. farnsworth is 455, human-narrative 452.
- README has a skills table; description lines run ~15–20 words, verb-first, em-dash
  specifier list. Update the row when a skill's frontmatter description changes.

### Environment

- **The `rtk` hook rewrites Bash commands and compresses output** — it strips stopwords,
  dedupes lines, and mangles file displays. Use `rtk proxy <cmd>` for raw output when exact
  text matters, and the `Read` tool rather than `cat` for verifying file contents. Use the
  `Write`/`Edit` tools rather than shell heredocs for authoring skill content; hook
  interference on file writes is a real risk.
- `pdftotext` is available. `WebFetch` cannot read PDF binaries — fetch, then extract from
  the saved file.
- Tooling per CLAUDE.md: `rg` not grep, `fd` not find, `gh` for GitHub, `eza` not ls.

---

## Next steps

1. **Draft `humanizer` v1.3.0** using the scope above. Show it to the user before
   committing. Split into at least two commits: stable pattern IDs + the #13/#14 fix as one
   (it is a bug fix with dependents), then the content additions.
2. **Grep the branch** for pattern-number references after the ID change and update
   farnsworth, human-narrative, and `scan-ai-tells.py` in the same commit as the rename.
3. **Then the deferred cross-skill work:** `CONTRIBUTING.md` entry for the scan, the
   `skill-builder` eval run across all three, and the LLM rubric for human-narrative.
4. **Open a PR** once humanizer lands. Nothing has been pushed; the branch is local only.
   Per `rules/BRANCHING-PR.md`, add a test plan section to the PR description.

---

## Session 2 addendum — humanizer v1.3.0 draft (2026-09-02)

Everything in the v1.3.0 scope list above was executed, plus the `CONTRIBUTING.md` entry
from the deferred list. Committed as:

```
582052b fix(humanizer): add stable pattern IDs and repair stale cross-references
16fe5a6 feat(humanizer): add finding threshold, missing patterns, citation repairs
ab0ae2e feat(scripts): filter quoted text and report density in scan-ai-tells
(next)  docs: document the writing-skill test aids in CONTRIBUTING
```

Commit 1 carries IDs on the 18 original headings under the *old* numbering with no
content change, so `git show 582052b:skills/humanizer/SKILL.md` is the v1.2.0 text plus
IDs. The renumbering (`VAGUE-CONNECT` at #6) happens in commit 2, after the IDs exist.

### Verification already run

- `skills/humanizer/SKILL.md` is 467 lines (cap 500). Description 297 chars.
- Self-scan: v1.3.0 → 0 hits. v1.2.0 under the same script → exactly 1 (the "Studies
  have shown" self-violation). Both known-good answers hold.
- Fixture regression: with 1.2.0 watch lists, all nine farnsworth fixtures identical
  before/after the script change. With 1.3.0 lists, only `01-exec-summary-IN` changes
  (+2 hits, "associated with" is now `VAGUE-CONNECT`); every OUT file still 0.
- Cross-ref grep: only historical changelog lines carry numbers, each as "(#N at the time)"
  next to the ID.
- Dist rebuilt for humanizer, farnsworth-rhetoric, human-narrative.
- Calibration numbers in the changelog and `tests/calibration/README.md` are from the
  final run against the 1.3.0 lists.

### Findings beyond the original review

- The exec-summary fixture is 399 words, not 600+. The `>600` farnsworth tier is still
  unexercised; the handoff above was wrong about that fixture.
- Source now lists "in order to" / "the fact that" as signs of *human* writing; 1.2.0
  flagged them as AI filler. Removed.
- `ELEGANT-VAR` and `DIDACTIC` moved to the source's historical section. Reflected.
- "Letter-like writing" is no longer on the source's ineffective-indicators list.
- Scan bug: curly apostrophes defeated the `isn't just` regexes. Fixed in the script.

### Eval run (2026-09-02, later the same session)

`tests/evals/` now holds the clean-context eval suite and its first run. 25 executor
subagents (11 with skill, 11 without, 3 previous-version), 11 grader subagents, 106
graded expectations. With-skill mean pass rates: farnsworth 0.95, human-narrative 0.88,
humanizer 0.95; no-skill 0.47 / 0.56 / 0.53. Full findings, four with-skill failures
triaged (two skill, two eval), and four candidate patches in
`tests/evals/runs/2026-09-02/REPORT.md`. The `evals.json` files were corrected per the
graders' critiques (filename leak, undefined thresholds, contradictory expectations,
missing fidelity checks) for the next run. Changelogs of all three skills carry an
"Evaluated" section.

### Still deferred

- **Candidate patches** from the eval report (humanizer residue-authorship sentence in
  SKILL.md; farnsworth withdraw-failing-treatment rule and single-line output shape;
  human-narrative blocked-slot rule and short-form length floor). Patch-level; show
  before committing.
- Re-run the corrected eval suite; three runs per configuration for variance.
- LLM rubric for `human-narrative` beyond the eval expectations.
- Thresholds unchecked on non-encyclopedic human prose.
