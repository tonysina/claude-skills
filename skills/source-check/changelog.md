# Changelog

## [1.0.0] - 2026-06-23
### Added
- Initial release. Many-agent claim verification against primary sources.
- Per-claim mode (default): one agent per claim, context-isolated.
- Per-source mode: one agent per source, for catching systematic stretch.
- Three failure states: secondhand, mismatch, unsupported.
- Scripts: init_workspace.py (timestamped output tree, original never touched),
  split_claims.py (inclusive heuristic claim extraction with manifest).
- Agent references: claim-agent.md (per-claim/per-source worker),
  consolidator.md (reviewer that adjudicates and writes report/corrected/footnotes).
- Environment guard: explicit subagent check with honest single-context
  fallback. No silent simulation of parallelism.

### Untested
- Not yet run end to end with live subagents against a real draft.
  First target: a draft already hand-verified, to confirm it flags what was
  caught and nothing false. Claim-extraction heuristics in split_claims.py
  most likely to move after first real use.
