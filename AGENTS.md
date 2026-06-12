# Agent Instructions

This repository contains a Codex plugin and skill for educational sports prediction analysis.

## Rules for future agents

- Preserve responsible-use disclaimers.
- Do not add betting advice claims.
- Do not imply certain outcomes or assured profit.
- Do not fabricate live data, injuries, odds, or results.
- Update README and docs when changing skill behavior.
- Keep `.agents/plugins/marketplace.json` valid JSON.
- Keep `plugins/sports-prediction-codex-plugin/.codex-plugin/plugin.json` valid JSON.
- Keep manifest paths relative to the plugin root and starting with `./` when required.
- Do not commit secrets.
- Run validation before commit.

## Suggested validation

```bash
python -m json.tool .agents/plugins/marketplace.json
python -m json.tool plugins/sports-prediction-codex-plugin/.codex-plugin/plugin.json
python scripts/validate_repo.py || true
```
