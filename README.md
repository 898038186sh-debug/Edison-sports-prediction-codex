# 体育预测 Codex Skill

A transparent Codex skill/plugin for structured sports match prediction reports, uncertainty-aware forecasts, and educational sports analytics. The public display name is **体育预测**.

## Overview

This repository is a Codex repo marketplace that exposes one plugin:

```text
plugins/sports-prediction-codex-plugin
```

The plugin contains one skill:

```text
sports-prediction
```

The skill helps an AI agent create structured, transparent pre-match sports analysis reports. It emphasizes data freshness, uncertainty, probability estimates, and responsible-use disclaimers.

## What it does

The skill guides analysis through:

- Match overview
- Data freshness
- Team form
- Injuries and availability
- Head-to-head context
- Schedule and fatigue
- Tactical or style factors
- Odds or market context, when available
- Probability estimates
- Confidence level
- Key uncertainties
- Responsible-use disclaimer

## Who it is for

- AI agent builders
- Codex users
- Sports analytics learners
- Fantasy sports researchers
- Prediction market researchers
- Developers experimenting with sports analytics workflows

## What it is not

This repository is not a betting advice product, financial advice product, gambling recommendation system, live-data provider by default, or replacement for professional judgment.

## Installation

Add the marketplace from Codex CLI:

```bash
codex plugin marketplace add Edison-777-crypto/sports-prediction --ref main
codex plugin marketplace list
codex plugin list --available --json
codex plugin add sports-prediction-codex-plugin --marketplace sports-prediction-skills
```

For local testing from the repository root:

```bash
codex plugin marketplace add ./
codex plugin marketplace list
codex plugin list --available --json
```

## Repository structure

```text
.agents/plugins/marketplace.json
plugins/sports-prediction-codex-plugin/
  .codex-plugin/plugin.json
  skills/sports-prediction/SKILL.md
  docs/
  examples/
```

## Example prompts

```text
Use the sports-prediction skill to analyze Arsenal vs Chelsea and produce a transparent pre-match prediction report.
```

```text
Use the sports-prediction skill to compare Lakers vs Celtics, including team form, injury uncertainty, confidence level, and risk notes.
```

```text
Use the sports-prediction skill to create a non-betting educational analysis for an upcoming match.
```

## Methodology

The workflow is:

1. Identify match context.
2. Check data freshness.
3. Review recent form.
4. Review injuries and availability.
5. Consider head-to-head data carefully.
6. Consider schedule and fatigue.
7. Consider tactical or style matchup.
8. Treat odds as market context, if available.
9. Estimate probabilities.
10. Disclose uncertainty.
11. Add the responsible-use disclaimer.

See [docs/methodology.md](plugins/sports-prediction-codex-plugin/docs/methodology.md).

## Limitations

- Live data may be unavailable.
- Injury reports can change quickly.
- Odds can move quickly.
- Output quality depends on input quality and available sources.
- Predictions are probabilistic and may be wrong.
- The skill does not provide betting or financial advice.

See [docs/limitations.md](plugins/sports-prediction-codex-plugin/docs/limitations.md).

## Responsible use disclaimer

This project is for educational and analytical purposes only. It does not provide betting advice, financial advice, investment advice, or assured outcomes. Sports predictions are probabilistic and may be wrong. Do not rely on this project as the sole basis for financial decisions or gambling activity.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

See [SECURITY.md](SECURITY.md).

## License

MIT.
