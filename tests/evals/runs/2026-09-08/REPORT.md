# Eval run 2026-09-08 -- humanizer 1.4.0 merge gate

Gate run for humanizer 1.3.2 -> 1.4.0, shipping alongside farnsworth-rhetoric 1.1.3 and
human-narrative 1.1.2. The 1.4.0 release adds one un-thresholded pattern (`UNDER-PUNCT`),
reverses a pattern that had pointed one way since the skill was written (`EM-DASH`), and
introduces a three-way carve-out spanning two skills. None of that had been tested, so the
release was gated on this run in the pattern the 1.3.1 entry established.

**Result: all five 1.4.0 arms pass, 32/32 expectations. The 1.3.2 control fails 3 of 6,
which is the release working.** Two patches landed before merge, both found by executors
rather than by review.

## Results

| Eval | Arm | Score | What it gates |
|---|---|---|---|
| 5 dash-dense-no-rewrite | with (1.4.0) | 6/6 | T1/T1b -- revised `EM-DASH` must not fire on current dash-dense text |
| 5 dash-dense-no-rewrite | **prev (1.3.2)** | **3/6** | control -- expected to fail |
| 6 polysyndeton-carveout | with | 8/8 | T9 -- the figure survives an executor that just read `UNDER-PUNCT` |
| 7 isolated-moreover | with | 5/5 | T3 / coverage-diff gap 2 -- one *moreover* is not a tell |
| 8 under-punct-positive | with | 6/6 | T2 -- `UNDER-PUNCT` fires without a threshold |
| 9 under-punct-independent-domain | with | 7/7 | T2 again, on a fixture that cannot be pattern-matched |

Mean pass rate: **1.00** across five 1.4.0 arms, **0.50** on the control.

Machine-readable table in `results-table.md`; per-arm detail in `<arm>/grading.json`.

## What the control proves

e5 is a true A/B: identical fixture, prompt and expectations across both arms, one variable.

1.3.2 removed two of the source's four em dashes and reported the cluster as its sole
finding. The grader verified the rule verbatim against the extracted 1.3.2 file, so this is
the old skill working as designed, not executor error. Its three failures map exactly onto
what T1b scoped: dashes not surviving, dashes reported as a finding, two sentences edited.

1.4.0 returned the note byte-identical, citing all three gating conditions -- dashes
unspaced, text not pre-2025, no co-occurring Pass 2 patterns.

The 1.3.2 executor also found the contradiction T1b exists to resolve, unprompted:

> The Full-rewrite clause says return text unchanged when the scan is clean; the
> ungated-construction list says three em dashes in a paragraph is a finding regardless of
> density. This text satisfies both conditions at once and the skill states no tie-break.

It then invented a retention rule ("one per paragraph is normal punctuation") to justify
which dashes it kept, and stated it to the user as the skill's standard. That is what an
unresolved contradiction produces under pressure.

## Why eval 9 exists

Eval 8's fixture shared subject matter and rewrite move sequence with the worked
`UNDER-PUNCT` example inside `SKILL.md`. Its grader judged that the run did measure
independently but that **the fixture could not prove it** -- a recall-driven model would
produce a near-identical artefact and pass all six assertions. That is a fixture defect, not
an executor defect, and it was mine.

Eval 9 is the same pattern in an unrelated domain (a software incident postmortem), built to
settle it. Its grader's verdict:

> This run measured independently; recall could not have produced it. Decisive evidence: the
> arithmetic is fixture-specific and correct. The 12-vs-1 joint/series split required
> per-instance judgment on 13 tokens in an unseen text.

Supporting: the rewrite diverges from the example on its most distinctive move (the example
uses a semicolon; e9 produced zero), and it resolved three questions the example cannot
supply -- exempting a series the example does not contain, ruling "40 to 120" a genuine range
rather than `FALSE-RANGE`, and keeping passive voice as postmortem genre convention.

**Eval 8 is retained as a regression case only.** Eval 9 is the load-bearing evidence for
`UNDER-PUNCT`.

## Patches driven by this run

Both in `skills/humanizer/SKILL.md`, both found by executors.

1. **`UNDER-PUNCT` was missing from "What the table does not gate."** Its exemption was
   stated a paragraph earlier, but the paragraph that enumerates table-bypassing findings
   omitted it. Two executors, on unrelated fixtures, independently reported the same
   consequence: a reader applying the table mechanically scores an unpunctuated text at
   density 0.0, spread 0, and ships it unchanged. Both caught it anyway, but both had to
   assemble the ruling from two places.
2. **The scanner caveat was too weak.** It said the script "does not compute these," which
   reads as a missing feature rather than a trap. It now states that a clean report from the
   script is not evidence against the pattern, plus an instruction to check arithmetic before
   quoting a rate.

Eval 9 ran against the *unpatched* skill and passed 7/7, so both patches are clarifications
on top of behaviour already demonstrated, not fixes the evidence depends on.

## Deferred, with evidence

**`NEG-PARALLEL`'s reversed "X rather than Y" variant has no example separating it from
ordinary comparative preference.** Three executors hit the judgment call this run ("I would
rather walk in with the gap acknowledged," "I would rather wait for it") and all three
resolved it correctly. The variant is ungated by the density table, so one false positive
flips a verdict with nothing to check it. Predates 1.4.0; out of scope for it. Ticket.

## What this run says about the evals

The graders' second job produced more value than the grades. Recorded in
`tests/evals/README.md` as rules; the load-bearing ones:

- **Assertions that pass on absence measure nothing.** Four of eval 7's five original
  assertions were satisfied by a response that says "reads human" and stops. Lazy restraint
  and correct restraint scored identically. Every eval whose right answer is restraint now
  carries at least one assertion only a working response can satisfy.
- **A carve-out needs a positive assertion.** "Does not flag X" passes for a response that
  never noticed X.
- **Grade the delivered text, not `result.md`.** Every grader had to neutralise the same
  artifact by hand: the change summary quotes the patterns it removed, so a raw
  `--keep-quotes` scan counts citations as commissions. On the control arm the whole file
  reads 10 em dashes and the delivered text reads 2. One grader noted that a grader trusting
  the raw scan "would have passed an arm that destroyed half the source's dashes."
  `tests/evals/extract-delivered.py` now does this.
- **Assert arithmetic.** Two executors reported hand-computed statistics that did not
  reconcile with their own word counts. Neither changed a verdict; no assertion caught
  either. Eval 9's arithmetic assertion is what settled its independence question.
- **A control arm must be told it is expected to fail,** or it is graded charitably and the
  A/B collapses.

Assertions were strengthened after grading (e5 5->7, e6 8->11, e7 5->8, e8 6->8). The
per-arm `eval_metadata.json` files are unchanged, so every recorded grade still corresponds
to the assertions it was graded against. **e6, e7 and e8's scores are against the weaker
set** and should not be compared directly with future runs.

## Method notes

- Executors: fresh general-purpose agents, one per arm, blocked from the Skill tool, other
  skills, `changelog.md` (which would have told them the answer), the scanner, and other
  eval directories.
- The 1.3.2 control ran from a `git show` extract at `/tmp/humanizer-prev`, not from the
  working tree.
- Scans in `<arm>/scan.txt` were run on whole `result.md` files and are **not reliable
  evidence**; see the extraction rule above. Retained as run artifacts only.
