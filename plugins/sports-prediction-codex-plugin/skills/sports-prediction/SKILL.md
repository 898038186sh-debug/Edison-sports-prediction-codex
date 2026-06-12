---
name: sports-prediction
description: Structured sports match prediction workflow emphasizing transparency, uncertainty, data freshness, and educational analysis. Not betting or financial advice.
---

# Sports Prediction Skill

## Purpose

Use this skill to produce transparent, structured pre-match sports prediction reports. The goal is educational sports analytics and workflow standardization, not gambling advice, financial advice, or outcome guarantees.

## Non-negotiable rules

- Never claim a certain outcome.
- Never present a prediction as betting advice, financial advice, or investment advice.
- Never describe a pick as risk-free.
- Never fabricate live data, injuries, odds, weather, lineups, or results.
- Always disclose uncertainty and missing information.
- Always distinguish verified facts, model assumptions, and qualitative judgments.
- If fresh data is unavailable, say so clearly.
- If odds are discussed, frame them as market context, not a recommendation to wager.
- Use probabilities and confidence levels rather than absolute claims.
- Include the responsible-use disclaimer at the end of every prediction report.

## Required output structure

When analyzing a match, use this structure:

1. **Match Overview**
   - Teams
   - League or competition
   - Date and time, if available
   - Venue, if available

2. **Data Freshness**
   - Available data
   - Missing data
   - Last-updated notes, if known
   - Source notes, if sources are available

3. **Team Form**
   - Recent results
   - Attacking and defensive trends
   - Home or away trend
   - Relevant qualitative notes

4. **Injuries and Availability**
   - Confirmed absences
   - Doubtful players
   - Lineup uncertainty
   - Impact on prediction

5. **Head-to-Head Context**
   - Recent head-to-head results, if available
   - Explain why head-to-head data should not be overweighted

6. **Schedule and Fatigue**
   - Travel
   - Rest days
   - Fixture congestion
   - Back-to-back games, if relevant

7. **Tactical or Style Factors**
   - Matchup style
   - Pace or tempo
   - Possession profile
   - Defensive matchup
   - Key player dependencies

8. **Odds or Market Context, if available**
   - Opening odds
   - Current odds
   - Movement
   - Implied probability
   - Warning that odds are not recommendations

9. **Prediction**
   - Probability estimate
   - Likely outcome
   - Confidence level: Low / Medium / High
   - Do not use absolute certainty language

10. **Key Uncertainties**
    - Injury uncertainty
    - Lineup uncertainty
    - Data limitations
    - Weather or venue uncertainty, if relevant
    - Late-news risk

11. **Responsible Use Disclaimer**
    - Educational only
    - Not betting advice
    - Not financial advice
    - Predictions may be wrong

## Probability format

For soccer/football:

- Home win probability:
- Draw probability:
- Away win probability:
- Confidence:
- Risk level:

For two-outcome sports such as NBA, MLB, NFL, NHL, or tennis:

- Team or player A win probability:
- Team or player B win probability:
- Confidence:
- Risk level:

## Data handling

If live data access is available, gather relevant information and cite sources. Prioritize current injuries, likely lineups, recent form, schedule context, and odds movement where appropriate.

If live data access is not available, do not invent facts. Write:

> Current live data is unavailable in this environment. This report demonstrates the analysis workflow and should not be treated as a live prediction.

## Final disclaimer text

Always include this disclaimer:

> This report is for educational and analytical purposes only. It is not betting advice, financial advice, or a guarantee of outcome. Sports predictions are probabilistic and can be wrong.
