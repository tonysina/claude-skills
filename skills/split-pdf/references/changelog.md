# Changelog

## [2.1.0] - 2026-10-29

Review against the upstream skill (scunning1975/MixtapeTools) and its open issues and PRs.

### Fixed

- **Density check failed silently.** With poppler missing or an encrypted PDF, the script reported
  0 chars/page under zsh (routing to scanned mode) and divided by zero under bash. Inspection is now
  three plain commands; a `pdfinfo` error stops the skill.
- **Text and scanned modes differed only in name.** Both put ~12 pages into context per notes update,
  and the rationale for larger scanned batches ran backwards. One reading mode now; scanned PDFs get
  a warning and `(scanned — verify)` marks on table values.
- **Document-type detection was unspecified** and, in subagent mode, would have pulled page images
  into the parent. It now uses title-page text from `pdftotext`.
- **Three names for the notes file plus a `cp`** (not in `allowed-tools`) into a duplicate. Notes are
  now written directly to `<basename>_text.md`.
- **"Technical components / key claims" naming mismatch;** analyst reports now capture evaluation
  criteria and vendor placements under Technical Components / Evaluation Framework.
- **Inaccurate PyPDF2 history** in `why-splitting-works.md`.

### Added

- Status line on the extract, with resume from the next unread page after an interrupted read.
- Reading Log: per-round record of pages, additions, judgment calls and open questions, shown at
  each pause.
- Pause in subagent mode, relayed by the parent and resumed with `SendMessage`.
- Precision rule with page anchors on every claim.
- Sections: Bibliographic Metadata, Summary (≤200 words, written last), Audience, Evidence Base,
  Figures & Tables, Verifiability & Reuse.
