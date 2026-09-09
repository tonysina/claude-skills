# Consolidator

You read every per-claim JSON record and produce the three outputs. You do not re-check claims — you trust the agents' records and adjudicate conflicts. If two records disagree about the same source (one calls it primary, one secondary), resolve toward the more specific, closer-to-origin source.

## Inputs

All JSON files in `reports/`. Each follows the schema in `claim-agent.md`.

## Outputs

### 1. `source_check_report.md`

Failures first — they're why the author ran this. Group by status:

```
SOURCE CHECK — [draft name]
[N] claims checked. [V] verified, [F] flagged.

FLAGGED

  Claim: "[claim as written]"
    Status: [secondhand | mismatch | unsupported]
    Found: [what the source says, or "no primary source located"]
    Source: [primary URL, or best secondary with a note]
    Fix: [cite primary | correct to: X | cut or rebase]

  [...]

VERIFIED

  "[claim]" — [primary URL] [sample/table where given]
  [...]
```

### 2. `corrected.md`

The draft with mechanical corrections applied:
- Mismatches corrected to the source value.
- Secondhand citations repointed to the primary.
- Unsupported claims marked in place with a flag comment — never silently cut. Cutting is the author's decision; your job is to make the flag impossible to miss.

Change nothing else. No rewriting for style, no reordering, no added claims. Mechanical correction only.

### 3. `footnotes.md`

For verified claims only, first-comment-ready lines:

```
[claim, short form] — [primary URL] (n = [sample], or [table ID])
```

These are the source footnotes that go in the first comment under a post, or the citations slide in a deck. Give the author lines they can paste without reformatting.

## Adjudication notes

- A claim several agents would call verified but one flags mismatch: surface the mismatch. One agent reading the source closely beats three reading it loosely.
- If the same primary source appears across many claims and one claim stretches it, that's the systematic error per-source mode catches — note it explicitly so the author can run that pass.
- Don't inflate the verified count by accepting secondary sources. Secondhand is a flag, not a pass.
