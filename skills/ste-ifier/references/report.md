# STE report template

Give the user this report after the last checker run. Use these five sections, in this order.
Write "None." in a section that has no content. Do not leave out a section.
Save the report to a file, run `python3 scripts/ste_dict.py verify REPORT ORIGINAL`, and correct
each line that it reports. Then give the report.

## 1. Result

The path of the STE file, or the STE text when there is no file.

## 2. What changed

The CHANGE REPORT from the last run of `check --compare ORIGINAL DRAFT`, copied without changes.
If the original is pasted text, save it to a file first, so that the comparison can run.
Then add the three to five rewrites that changed the most, as "original -> STE" pairs.

## 3. Kept on purpose

One line for each finding in the last checker output that you did not fix:
the line number, the finding, and the reason.
Example: `L33 branch* - noun ("select the branch"), TN in git-github.md.`

## 4. Rules checked by reading

One line for each rule in the checker's NOT CHECKED list that applies to this text, in one of two forms:
- `<rule> - OK.`
- `<rule> - changed: "<words copied from the original>" -> "<words in the STE text>".`

Copy the original words exactly. If you cannot copy them from the original, the rule changed nothing: write OK.
Example: `5.4 condition first - changed: "Apply the primer when the surface is dry" -> "When the surface is dry, apply the primer".`

For 1.3 (meaning), compare each STE sentence with its source sentence: the conditions, the order of
the steps, the negations ("do not", "until", "before"), and the quantities must be the same.
Put each sentence where you are not sure into section 5.

## 5. Decisions for you

A numbered list of the items that you could not decide from the source text and the standard.
An item goes here only if the dictionary and the rules cannot answer it. Before you add a word,
run `lookup` for it: if the dictionary answers the question, apply the answer instead. Do not
remove meaning from the source to avoid a word: if the word is approved, keep it.
Each option that you give must be correct STE. Run `lookup` on each word that you offer.
For each item, give the question, the dictionary evidence, the options, and the option that the text uses now.
The dictionary evidence is the `==` line that `lookup` prints for each word in the question and in the
options, copied exactly. A word with no `==` line in your report is not checked: do not offer it.
The text must be usable before the user answers, so apply your best option.

Put these items here:
- A word that you kept as a technical noun or technical verb, but that no term file lists.
  Ask if it goes into the project's `ste-terms.md`. Write the file only after approval.
- A sentence where the meaning of the source is unclear, or where the STE text can change the meaning.
- A part of the text that can be procedure or descriptive text, when the choice changes the rules.
- Two terms for one item when no term file decides (rule 1.11).
- A source statement that STE cannot say without a change of meaning (for example, a hedge with "may").

Example:
```
1. "manual check" (L5): keep "manual"?
   Dictionary: == APPROVED: MANUAL (adj) | == APPROVED: CHECK (n)
   Options: "Do a manual check of the permissions." / "Examine the permissions."
   The text uses: "Do a manual check of the permissions."
2. "dropdown menu" (L37): technical noun, not in a term file.
   Dictionary: == dropdown: not in dictionary (allowed only as a technical noun/verb, rules 1.5/1.12)
   Options: add "dropdown menu (TN)" to ste-terms.md / "menu".
   The text uses: "dropdown menu".
```
