---
name: ste-ifier
description: Use when text must follow ASD-STE100 Simplified Technical English (STE) - writing, rewriting, or reviewing procedures, instructions, warnings, user guides, README, or Git and GitHub docs in STE, or checking whether a word is STE-approved. Triggers include "STE", "STE-ify", "Simplified Technical English", "ASD-STE100", "controlled language", "ste-terms.md". Not for marketing copy or general plain-language editing.
---

# STE-ifier

STE allows only words from the ASD-STE100 dictionary (Issue 9, bundled), technical nouns (TN), and technical verbs (TV). The dictionary decides approval, not memory. Paths are relative to this skill's folder.

## Workflow

1. Mark each part of the text as procedure (instructions) or descriptive (information).
2. Read `references/rules.md` (the standard's rule summaries, verbatim). Then draft the STE text.
3. Save the original and the draft to files (Markdown is fine). Run:
   `python3 scripts/ste_dict.py check --compare ORIGINAL [--mode auto|procedure|descriptive] [--terms FILE] DRAFT`
4. Act on every finding (below), and on each rule in the NOT CHECKED list that applies.
5. Repeat steps 3 and 4 until only deliberate items remain.
6. Report with the template in `references/report.md`. It is required: all five sections, in order. Its last section lists the decisions you could not make, for the user.

## Checker output

WORDS (dictionary):

| Finding | Action |
|---|---|
| not as v -> ALTERNATIVES | Use an alternative or a different sentence (9.1). `lookup WORD` shows examples. |
| OK as n; not as v | Use the word only as the approved part of speech. |
| TERM (TN) or (TV) | Allowed only as that part of speech, with its listed meaning. |
| 1.11 or 1.4 | Use the term or form that the note gives. |

STRUCTURE (writing rules): fix each `error`. A `check` can be correct, for example a passive with an unknown agent (3.6) or "-ing" in a technical noun (3.5): decide. `--mode` sets the sentence limit (procedure 20, descriptive 25). The default, auto, uses 20 for instructions.

NOUNS USED AS TECHNICAL NOUNS: the dictionary rejects only the verb (fuel, pump). Keep them as nouns only.

NOT IN DICTIONARY: keep only a TN (rule 1.5), a TV (rule 1.12), or a proper noun.

The checker cannot confirm meaning (rule 1.3), paragraph topics, or omitted words. For a rule's full text and examples: `grep -n -A40 "^ *Rule 5.4 " data/ste100-issue9.txt`. Frontmatter, code, links, bold UI labels, and quoted text are not checked. Each counts as one word (rule 8.6).

## Term files

The checker loads:
- `terms/computer-verbs.md`: computer technical verbs from rule 1.12.
- `terms/git-github.md`: Git and GitHub terms, with STE wording for Git actions. Read it for Git text.
- Project terms: in Claude Code, the nearest `ste-terms.md` above the current directory or draft, up to the git root. In claude.ai or the desktop app, pass a Project knowledge file or an upload with `--terms`. If it is not on disk, first write its content to `ste-terms.md`.

Format (only tagged list lines are read):
```
- tenant (TN): a customer workspace
- commit (TN, TV)
- repository (TN): a Git repository. Not: repo, codebase
```
Use one term for one item (rule 1.11). The checker flags each "Not:" word.

Requires Python 3. On claude.ai and the desktop app, turn on code execution.
