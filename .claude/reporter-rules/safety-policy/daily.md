# Wiki Ingest — 安全政策記者指南（daily）

開工先讀 `.claude/reporter-rules/shared.md`；建頁另讀 `.claude/reporter-rules/page-templates.md`；本記者負責頁的表格契約見 `.claude/reporter-rules/safety-policy/pages.md`。

分類為「安全政策」的新聞條目由此記者負責。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/topics/anthropic-government-policy.md` | Anthropic 與各國政府互動、出口管制、軍事合約 |
| `wiki/topics/ai-agent-safety.md` | AI agent 安全事件、漏洞披露、提示注入 |
| `wiki/topics/recursive-self-improvement.md` | AI 遞歸自我改進、全球監管呼籲 |

> 上表為核心頁面與觸發條件；此外 `wiki/index.md` 中領域為 🏛️ 政策/安全 的所有頁面（含日後新增）皆由本記者負責維護與 lint。

---

## 每日動作

兩頁各有自己的逐步順序與結論表契約，逐條照 `.claude/reporter-rules/safety-policy/pages.md` 執行：

- `anthropic-government-policy`：`## 攻防紀錄` prepend ＋ `## 時序` prepend ＋ 四張結論節的覆寫與退場
- `ai-agent-safety`：事件 prepend 進 `## 技術彙整` ＋ `## 時序` prepend ＋ 三張結論表的覆寫與退場
- `recursive-self-improvement`：無專屬結論表，照頁面既有結構 prepend 並更新兩個日期欄位

記者無 web 工具：官方一手來源、訴訟文件與 GitHub issue 狀態的查證屬主編層，遇到只能提列並在「同步自查」欄回報。

---

## 回報格式

照 `.claude/reporter-rules/shared.md`「回報格式（回報契約）」八欄；`feature-radar 新增` 欄恆填「無」。安全事件涉及 Claude Code 功能面時，「同步自查」欄註明「請主編轉知功能記者」。
