# Recommended GitHub Repository Settings

## Recommended repository name

```text
sports-prediction-codex-skill
```

Alternative names:

```text
sports-prediction-codex-plugin
sports-analytics-codex-skill
match-prediction-agent-skill
```

## Recommended description

```text
A transparent Codex skill/plugin for structured sports match prediction reports, team form analysis, odds context, and uncertainty-aware forecasts.
```

## Recommended topics

```text
codex
codex-plugin
agent-skills
skill-md
sports-analytics
sports-prediction
match-prediction
football
soccer
nba
mlb
odds-analysis
prediction-markets
ai-agents
```

## GitHub CLI command

Run this only after confirming that `gh` is authenticated and pointed at the correct repository.

```bash
gh repo edit \
  --description "A transparent Codex skill/plugin for structured sports match prediction reports, team form analysis, odds context, and uncertainty-aware forecasts." \
  --enable-issues \
  --enable-discussions \
  --add-topic codex \
  --add-topic codex-plugin \
  --add-topic agent-skills \
  --add-topic skill-md \
  --add-topic sports-analytics \
  --add-topic sports-prediction \
  --add-topic match-prediction \
  --add-topic football \
  --add-topic soccer \
  --add-topic nba \
  --add-topic mlb \
  --add-topic odds-analysis \
  --add-topic prediction-markets \
  --add-topic ai-agents
```

## Visibility

Do not make the repository public automatically unless the owner confirms.

Manual command after confirmation:

```bash
gh repo edit --visibility public --accept-visibility-change-consequences
```
