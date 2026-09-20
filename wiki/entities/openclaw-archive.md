---
page: "entities/openclaw-archive"
kind: "entity"
status: "resolved（封存頁）"
domain: "🛠️ 工具/功能"
last_updated: "2026-09-20"
last_news_update: "2026-05-14"
status_main: "resolved"
days_since_news: 129
parent: "entities/openclaw"
children: "[]"
page_role: "archive"
days_since_news_subtree: 129
inbound_links: 0
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# OpenClaw——原始條目封存

**狀態：** resolved（封存頁）
**領域：** 🛠️ 工具/功能
**上層：** [[entities/openclaw]]
**最後更新：** 2026-09-20
**最後新聞更新：** 2026-05-14

> 本頁保存 [[entities/openclaw]] 被搬離主頁的原始「事件時序」條目。條目一字不刪，只是搬離主頁讓主頁讀得動；重點層見主頁。

---

## 2026-05

### 2026-05-14：OpenClaw 恢復允許，改走信用池計費

Anthropic 宣布 6 月 15 日起，包含 OpenClaw 在內的第三方 Agent SDK app 用量**重新被允許**，但用量全數脫離訂閱方案，按完整 API 費率計費（獨立信用池）。此舉等同宣示：Anthropic 不再透過禁令限制第三方工具，改以費率結構讓市場自然篩選。

對開發者的實際意義：重度使用者換算 API 費率後費用大幅上升（Max 5x 40% 週配額 ≈ $1,000/月），部分用戶轉向 OpenCode 或自行架設 API；社群同期出現 `claude-pee` 繞過工具；見 [[entities/pricing]]。

## 2026-04

### 2026-04-30：異常計費觸發行為（HN 近千則討論）
Claude Code 被發現存在異常行為：若 Git 提交訊息或文件內容中含有特定 JSON 格式的 "OpenClaw" 字串，工具會：
- 直接拒絕當次請求，或
- 立即將帳單的 Extra Usage 衝至 100%

此行為表明 Claude Code **正在主動掃描 repo 內容**並依此改變執行策略與計費結果，事件在 HN 引發近千則討論。Anthropic 至今未公開說明觸發條件是否屬預期設計，亦未提供任何官方聲明。

> ⚠️ **未解決**：Anthropic 未確認此為預期行為或 bug，缺乏透明說明。

### 2026-04-25：Anthropic 限制配額
Anthropic 明確限制 OpenClaw 等第三方 agentic 工具的使用配額。Claude Code 負責人 Boris Cherny 公開表示：

> 「訂閱方案的設計並非為這類第三方使用模式而生。」

此言論被視為 Anthropic 將持續提高第三方 agentic 工具門檻的明確信號。
