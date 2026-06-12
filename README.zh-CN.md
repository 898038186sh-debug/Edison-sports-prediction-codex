# Sports Prediction Codex Skill

这是一个给 Codex / AI agent 使用的球赛预测分析 skill/plugin。

它的定位不是“喊单”或“稳赢投注建议”，而是让 AI 按结构分析球赛，输出透明、可审查、带不确定性说明的预测报告。

## 它能做什么

它可以帮助 AI agent 按下面结构分析比赛：

- 比赛背景
- 数据新鲜度
- 球队近期状态
- 伤病和出场情况
- 历史交锋
- 赛程和疲劳
- 战术或风格因素
- 赔率或市场背景，如果有数据
- 概率估计
- 信心等级
- 风险提示
- 负责任使用免责声明

## 它不能做什么

本项目不是：

- 投注建议工具
- 财务建议工具
- 保证收益系统
- 默认实时数据源
- 专业判断的替代品

## 安装方式

可以在 Codex CLI 中添加 marketplace：

```bash
codex plugin marketplace add 898038186sh-debug/Edison-sports-prediction-codex --ref main
codex plugin marketplace list
codex plugin list --available --json
codex plugin add sports-prediction-codex-plugin --marketplace sports-prediction-skills
```

## 示例 prompt

```text
Use the sports-prediction skill to analyze Arsenal vs Chelsea and produce a transparent pre-match prediction report.
```

```text
Use the sports-prediction skill to compare Lakers vs Celtics, including team form, injury uncertainty, confidence level, and risk notes.
```

## 输出结构

- Match Overview
- Data Freshness
- Team Form
- Injuries and Availability
- Head-to-Head Context
- Schedule and Fatigue
- Tactical / Style Factors
- Odds / Market Context
- Prediction Probabilities
- Confidence Level
- Key Uncertainties
- Responsible Use Disclaimer

## 方法论

这个 skill 要求 AI 先检查数据是否新鲜，再分析球队状态、伤病、赛程、战术、赔率背景和不确定性，最后输出概率和信心等级，而不是输出绝对判断。

## 局限性

- 当前环境可能没有实时数据。
- 伤病和阵容消息可能临场变化。
- 赔率变化很快。
- 输出质量取决于输入数据质量。
- 任何预测都可能错误。

## 免责声明

本项目仅用于教育、研究和体育数据分析 workflow，不构成投注建议、财务建议、投资建议或保证收益系统。任何球赛预测都是概率性判断，可能错误。请不要把本项目作为任何投注或资金决策的唯一依据。
