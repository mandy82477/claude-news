---
page: "entities/opencode"
kind: "entity"
type: "product"
status: "active（快速成長）"
domain: "💼 商業"
last_updated: "2026-10-19"
last_news_update: "2026-10-19"
status_main: "active"
days_since_news: 8
parent: null
children: "['entities/opencode-archive']"
page_role: "hub"
days_since_news_subtree: 8
inbound_links: 8
attribution_count: 1
attribution_last: "2026-10-19"
top_source: "google-news"
pending_count: 1
pending_overdue: 0
pending_next_review: "2026-11-02"
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# OpenCode

**類型：** product
**狀態：** active（快速成長）
**領域：** 💼 商業
**首次出現：** 2026-04-27
**最後更新：** 2026-10-19
**最後新聞更新：** 2026-10-19

> **最新動態**（2026-10-19）
> 36Kr 報導 OpenCode 發生重大當機危機，使用者反映 GPT 與 Claude 帳戶餘額一覺醒來遭歸零；官方尚未公告修復時程或賠償方案。

---

## 現況

**最新動態（2026-10-19）：** 36Kr 報導 OpenCode 發生重大當機危機，使用者反映 GPT 與 Claude 帳戶餘額一覺醒來遭歸零；OpenCode 官方表示仍在搶修服務，尚未對外公告賠償或復原時程，僅標題可用（36Kr）。❓ **待查證**（標 2026-10-19｜查 [[entities/opencode]]、帳戶餘額歸零）｜**事故成因與修復時程未載**：影響範圍、復原時程與是否賠償均未見報導。

**（2026-05-22）：** XDA 正式評為 Claude Code 的可行開源替代方案，同期 `OpenCode-power-pack` 完成移植官方 11 個 skills。

OpenCode 是 Claude Code 的主要開源替代品，截至 2026-05-12 已吸引 **157,000 名開發者**轉向（The New Stack 報導）。功能與體驗被 XDA 評測認為與 Claude Code 相當，且完全開源免費。即便 Anthropic 宣布倍增速率限制，對 vendor lock-in 的顧慮仍持續驅動開發者轉向開源方案。

另有 tech-insider.org（Google News 轉載，2026-08-01）比較兩者下載量與定價（Free vs $20）：2026-07-31 止 30 天 npm 下載數 Claude Code 44,264,901 次、OpenCode 8,245,142 次，即 **Claude Code 約為 OpenCode 的 5.4 倍**（媒體稱，tech-insider.org；GitHub star 則 OpenCode 領先）。2026-10-24 查證：先前「OpenCode 達 Claude Code 5.4 倍」的方向寫反，已更正；統計基礎是 npm registry 公開下載數（30 天窗口），方法可驗證、非黑箱推算。npm API 本輪無法直連（403），數字取自該文（[tech-insider.org](https://tech-insider.org/opencode-vs-claude-code-2026)），尚無獨立第二來源或 npm 官方頁面逐字覆核。

## 熱度與試用價值

| 項目 | 評分 |
|------|------|
| 社群熱度 | 🔥🔥🔥🔥 |
| 試用價值 | ✅ 廣泛採用 |
| 最適合 | 成本敏感開發者、希望避免 vendor lock-in 的團隊、需要開源方案的使用者 |
| 不適合 | 依賴 Anthropic 官方整合深度功能的場景 |

> 詳細最新熱度見 [[feature-radar]]

---

## 核心功能

- **開源免費**：無訂閱費，對成本敏感開發者最直接的替代路徑
- **插件生態**：`OpenCode-power-pack` 已移植 Anthropic 官方 11 個 Claude Code skills（代碼審查、安全審計、前端設計等），打破官方插件的工具綁定限制
- **社群整合**：`claude-anyteam` 工具已讓 OpenCode 代理加入 Claude Code Agent Teams，實現跨工具協作
- **競爭定位**：XDA 於 2026-05 正式評為 Claude Code 的可行替代方案，直接回應 OpenClaw 禁令後的替代需求

---

## 分流背景

OpenCode 的成長發生在幾個推力同時出現的時間點：
1. **OpenClaw 禁令**（2026-04 底）：Anthropic 對第三方 agentic 工具的限制引發開源替代需求
2. **6/15 計費調整**：`claude -p` 改按全額 API 費率計費，推動尋找低成本替代
3. **Claude Code 效能退步事件**（2026-03～04）：品質下滑期間開發者開始評估替代方案

---

## 相關實體

- [[topics/competitor-landscape]]（主要競品分析）
- [[entities/openclaw]]（OpenClaw：Anthropic 限制後促成 OpenCode 需求的前置事件）
- [[entities/pricing]]（計費調整是分流動因之一）
- [[topics/code-quality-decline]]（效能退步期間開發者評估替代方案）

---

## 參考來源

- [[news/2026-04-27]]
- [[news/2026-05-12]]
- [[news/2026-05-22]]
- [The New Stack 報導（157K 開發者）](https://thenewstack.io/)

---

## 歷史記錄

### 2026-05 時段總結
- XDA 評為 Claude Code 可行替代方案，`OpenCode-power-pack` 完成移植官方 11 個 skills（05-22）；The New Stack 報導 157,000 名開發者轉向里程碑（05-12）
- 原始條目見 [[entities/opencode-archive#2026-05]]

### 2026-04 時段總結
- 04-27 首次出現社群討論，OpenCode-power-pack 移植 Anthropic 官方 11 個 skills
- 原始條目見 [[entities/opencode-archive#2026-04]]
