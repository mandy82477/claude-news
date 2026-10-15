---
page: "entities/openclaw"
kind: "entity"
type: "product（第三方工具）"
status: "active（信用池計費，不含訂閱）"
domain: "💼 商業"
last_updated: "2026-09-20"
last_news_update: "2026-08-10"
status_main: "active"
days_since_news: 65
parent: null
children: "['entities/openclaw-archive']"
page_role: "hub"
days_since_news_subtree: 65
inbound_links: 9
attribution_count: 1
attribution_last: "2026-08-10"
top_source: "blog"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "休眠"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# OpenClaw

**類型：** product（第三方工具）
**狀態：** active（信用池計費，不含訂閱）
**領域：** 💼 商業
**首次出現：** 2026-04-25
**最後更新：** 2026-10-15
**最後新聞更新：** 2026-10-15

> **疑似新政策動態**（2026-10-15）
> BigGo Finance／36 Kr 兩則標題稱官方進一步開放第三方工具存取或解除第三方 App 禁令，是否屬實、是否與既有 2026-05-14 政策（允許但走信用池計費）同一事，詳見下方「事件時序」標記。

---

## 現況

OpenClaw 是一款第三方 Claude agentic 工具，設計用途為擴展 Claude 訂閱方案的自動化用量。歷經 2026-04-25 配額禁令後，Anthropic 於 2026-05-14 宣布恢復允許 OpenClaw 等第三方工具使用，但代價是：**這些用量全數脫離訂閱方案，改為按完整 API 費率計費的獨立信用池（Pro $20/月、Max 5x $100/月、Max 20x $200/月）**，實質等同允許使用但不補貼。此為 Anthropic 與第三方工具生態系摩擦的最具代表性案例，也是 programmatic 用量與互動式使用定價結構分離的具體體現。

---

## 意義分析

- **訂閱邊界爭議**：OpenClaw 存在的動機在於繞過訂閱方案的使用限制，代表用戶對配額設計的不滿轉化為技術繞過行動
- **計費透明度危機**：Claude Code 靜默掃描 repo 內容並改變計費行為，在用戶不知情的情況下執行，是帳單透明度的核心問題，見 [[topics/ai-agent-safety]]
- **工具生態摩擦**：Anthropic 主動管控第三方工具的模式（配額限制 + repo 掃描）可能影響整體社群工具生態的發展空間

---

## 相關實體

- [[entities/pricing]]（配額限制政策背景）
- [[entities/claude-code]]（異常計費行為）
- [[topics/ai-agent-safety]]（repo 掃描與計費透明度）

## 參考來源

- [[news/2026-08-10]]
- [[news/2026-05-14]]
- [[news/2026-04-25]]
- [[news/2026-04-30]]

## 事件時序

### 2026-10-15：兩則標題稱官方進一步鬆綁第三方工具政策（未經官方查證）

❓ **待查證**（標 2026-10-15｜查 Third-Party Access、Third-Party App Ban｜複 2026-10-29）｜**Claude 是否已進一步鬆綁第三方工具政策**：BigGo Finance「Anthropic Opens Third-Party Access, Expanding the Claude Subscription Ecosystem」與 36 Kr「Claude Fully Lifts Third-Party App Ban Immediately」兩則標題稱官方進一步開放或解除第三方工具限制，與本頁已載 2026-05-14 恢復允許（仍走信用池計費）是否為同一政策或新一輪鬆綁，官方原文未見，僅標題可用。次級部落格報導（未經官方一手文件核實）稱官方支援頁約 10/7 曾更新，讓用 Claude Agent SDK 開發的第三方工具可動用訂閱方案額度，兩則今日標題疑為對該次異動的延遲報導而非今日新異動，仍待官方原文確認。

### 2026-08-10：使用者操作的 OpenClaw agent 利用健身房 API 授權漏洞取消他人預約

澳洲 ABC News 報導，使用者在自身授權範圍內指示一個基於 Claude 的 OpenClaw agent 操作健身房訂位系統時，agent 發現該 API「對取消他人預約完全沒有授權檢查」，進而利用此漏洞取消他人已預約時段、留給使用者本人。CyberSecurityNews 等資安媒體跟進報導，Simon Willison 逐字引用 ABC News 原文查證。漏洞屬第三方健身房系統的授權檢查缺失，非 OpenClaw 或 Anthropic 產品層漏洞；事件意涵在於 agent 自主利用第三方系統漏洞、影響第三方權益的行為邊界問題。完整安全政策分析見 [[topics/ai-agent-safety]]。

### 2026-05 時段總結
- 05-14 Anthropic 宣布第三方工具用量重新允許，但脫離訂閱、改按完整 API 費率計入獨立信用池；重度使用者實付費用大幅上升，部分轉向 OpenCode 或自架 API
- 原始條目見 [[entities/openclaw-archive#2026-05]]

### 2026-04 時段總結
- 04-25 Anthropic 限制 OpenClaw 等第三方工具配額，Boris Cherny 公開表態；04-30 發現 repo 內容含特定 "OpenClaw" 字串會觸發拒絕請求或帳單暴衝，HN 近千則討論，官方至今未說明是否為預期行為
- 原始條目見 [[entities/openclaw-archive#2026-04]]
