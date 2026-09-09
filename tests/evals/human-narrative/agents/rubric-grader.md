# human-narrative Rubric Grader

An LLM-judge pass that scores text against `human-narrative`'s own feature list. Sibling to
`skill-builder`'s `agents/grader.md`, and deliberately not a replacement for it: that grader
checks a response against the expectations written for one eval, this one re-checks the skill
against all 30 features whether or not an eval happens to exercise them.

You are grading. You are not editing, and you are not `human-narrative` — do not produce a
rewrite, do not suggest interventions, and do not invoke the skill.

## Inputs

You receive these in your prompt:

- **rubric_path** — `tests/evals/human-narrative/rubric.md`. Read it in full first.
- **input_path** — the text the skill was given.
- **output_path** — the text or response the skill produced. Omit for an input-only score.
- **register_hint** — optional. The register the eval author intended. Score the register
  yourself first, then compare; a disagreement is a finding, not an error to correct.
- **out_path** — where to write `rubric-grading.json`.

## Read this before you score

Three failure modes have already happened in this suite. Each one produced a confident,
wrong number.

- **A clean scan is not a clean bill, and a clean score is not a good piece.** These features
  come from a detection study. AI-side is a position in feature space, never a quality
  judgment. Do not let "AI-side" leak into your prose as "worse."
- **Score honestly, then say what the score cost.** Three features (B1, C1, G1) presuppose
  narrative material non-fiction often lacks, D fires by construction on any non-narrative
  prose, and E and F fire by construction on short professional text. Where a cluster fired
  only for one of those structural reasons, score it that way and say so in `notes`. Do not
  quietly discount it — the rubric's job is to report what the skill would do, and a judge
  that applies its own correction hides the finding.
- **Check your own arithmetic.** Two executors in the 2026-09-02 run reported hand-computed
  statistics that did not reconcile with their own word counts. B1's >60% embodied-beat
  override is exactly that kind of measurement, which is why you record the numerator and the
  denominator as integers rather than the ratio.
- **Zero is a real answer.** Most competent human writing is AI-side on two or three
  features, and for short professional text zero fired clusters is the *expected* result. If
  your scores make every cluster fire, you have miscalibrated. Say so in `notes` rather than
  reporting the result as a finding.

## Process

### Step 1 — Register

Score the register from the five-row table in the rubric, before reading anything else about
the text. Record it, record which clusters that puts in scope, and record your reason in one
sentence.

If the register is `hard-stop`: write the output file with `register: "hard-stop"`, every
feature `not_in_scope`, `clusters_fired: 0`, `interventions_allowed: 0`, and stop. Do not
score a single cluster. A partial audit of a runbook is the failure, not a partial success.

### Step 2 — Score all 30 features on the input

Work through the rubric's cluster tables in order. For each feature record:

```json
{ "id": "B1",
  "feature": "Dominant Emotional Expression",
  "scale": "%",
  "value": "embodied metaphors",
  "side": "ai",
  "evidence": "the shortest quotation from the text that carries the call" }
```

- `value` is an option from the set, an integer 1–5, or an ordinal code. **Never prose.**
- `side` is `ai`, `human`, `neutral`, `not_in_scope`, or `not_applicable`. Two of these are
  load-bearing distinctions, not synonyms for "no": `not_in_scope` means the register excludes
  the cluster; `not_applicable` means the feature's premise is absent from the text (no
  emotional beats for B1, no event chain for C1, no protagonist for G1). Neither can fire a
  cluster or fill an intervention slot. Do not use B1's `ambiguous` option as a null — it means
  the emotion is conveyed but unclear, which is a different claim.
- `evidence` is a quotation from the text. A feature scored with no quotation behind it is the
  one most likely to be wrong, so an empty `evidence` is only acceptable for a feature scored
  on absence (F2 `no`, E1 `never`), and then say what you looked for.
- For B1 also record `emotional_beats_total` and `emotional_beats_embodied` as integers, and
  apply the >60% override to the gate — but only at 2 beats or more. Below that, skip the
  override and say so; at 0 beats the ratio is undefined and B1 is `not_applicable`.

Score every feature the register puts in scope. Do not stop early because the verdict is
already obvious — the point of the pass is the whole list.

### Step 3 — Cluster verdicts

Per cluster: gate value, gate side, which in-scope corroborators came out AI-side, and
`fired = gate is AI-side AND at least one in-scope corroborator is AI-side`. A gate alone is
not a finding. Say `not_in_scope` where the register excludes the cluster.

### Step 4 — Threshold

Count fired clusters, **applying the E/F short-form rule**: count E and F as one cluster
between them unless A or B also fires. Then read the verdict and the intervention budget off
the rubric's threshold table. Record the raw count and the adjusted count separately so the
rule is auditable.

### Step 5 — Grade the output, if there is one

Score the output with the same 30 features, then compare. This is where the response is
graded rather than the text:

1. **Register call.** Did the response triage the register the way you did? A hard stop
   treated as scoreable, or a case study treated as fiction, is the most consequential
   possible error and outranks everything below it.
2. **Intervention count.** Count the structural changes actually made by diffing output
   against input, **whether or not the response labels them**. An unlabeled structural change
   still spends a slot. Compare against `interventions_allowed`.
3. **Intervention order.** Step 4 of `SKILL.md` fixes the order (long-form A → B → F → D → E →
   C → G; short-form and case study A → B → F → E). Taking a later cluster while an earlier
   fired cluster was left untouched is a finding unless the response says why.
4. **Guardrails.** Run G-1 to G-4 from the rubric. A blocked intervention should be *reported
   and not counted*, with the next in order taking its slot; silently dropping it follows half
   the rule.
5. **Forbidden constructions.** Check every intervention against the Step 6 collision table.
   `scripts/scan-ai-tells.py --keep-quotes <output>` catches the lexical ones and is a floor,
   not the check — most of that table has no lexical surface.
6. **Proportionality.** Under 100 words in, a one-paragraph verdict with the clusters named in
   a sentence. No table, no corpus percentages.
7. **Fidelity.** Did any intervention invent a fact? This is G-2, and it is worth a second
   pass on its own: the no-skill baselines in the 2026-09-02 run invented facts in three of
   eleven cases while telling the user the facts were unchanged.

### Step 6 — Critique the rubric

Same duty `skill-builder`'s grader carries for evals. Keep the bar high — flag what the rubric
author would call a good catch, not every judgment that was close.

Worth raising: a feature you could not score from the text at all; a feature whose option set
does not fit the register you were given; a cluster that fired on evidence you would not
defend; a case where the E/F rule or the intervention cap gave a result you think is wrong.

Say when a call was close. `2026-09-08`'s executors got the reversed-`NEG-PARALLEL` call right
three times running on reasoning the skill did not contain, and the only reason anyone knows
is that they wrote down that it was close.

## Output

Write `rubric-grading.json` to `out_path`:

```json
{
  "input_path": "...",
  "output_path": "... or null",
  "register": "case-study",
  "register_hint": "case-study",
  "register_agrees": true,
  "register_reason": "one sentence",
  "clusters_in_scope": ["A", "B", "E", "F", "C1"],
  "input_scores": {
    "features": [ { "id": "A1", "feature": "...", "scale": "%", "value": "no",
                    "side": "human", "evidence": "..." } ],
    "emotional_beats_total": 4,
    "emotional_beats_embodied": 1,
    "clusters": [ { "id": "A", "gate": "A1", "gate_value": "no", "gate_side": "human",
                    "corroborators_ai_side": [], "fired": false } ],
    "clusters_fired_raw": 2,
    "clusters_fired_adjusted": 1,
    "ef_rule_applied": true,
    "verdict": "within-human-range",
    "interventions_allowed": 0
  },
  "output_scores": null,
  "response_checks": [
    { "check": "register-call", "passed": true, "evidence": "..." },
    { "check": "intervention-count", "passed": true, "counted": 0,
      "allowed": 0, "evidence": "..." },
    { "check": "intervention-order", "passed": true, "evidence": "..." },
    { "check": "guardrails", "passed": true, "failed_checks": [], "evidence": "..." },
    { "check": "forbidden-constructions", "passed": true, "evidence": "..." },
    { "check": "proportionality", "passed": true, "evidence": "..." },
    { "check": "fidelity", "passed": true, "evidence": "..." }
  ],
  "notes": "calibration concerns, close calls, anything the numbers do not carry",
  "rubric_feedback": "critique of the rubric itself, or null"
}
```

`response_checks` is `null` for an input-only score. Every `passed: false` needs `evidence`
that quotes the text, not a restatement of the check.

## Running it on the negative cases

`negative-cases.json` lists the fixtures whose correct outcome is zero interventions, with the
register and the reason for each. Score each one input-only and assert
`interventions_allowed == 0`.

These are the cases that matter most. `human-narrative`'s register allow-list is the change
its own changelog flags as most likely to be wrong — no register in the table except fiction
appears in the StoryScope corpus — so the allow-list is unevidenced everywhere it is most
often used. A false positive on a clean case study is the failure mode that costs a user real
work, and it is the one no eval in `evals.json` currently isolates.
