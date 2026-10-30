# Wiki Ingest — 安全政策記者指南（daily）

開工先讀 `.claude/reporter-rules/shared.md` ＋ `.claude/reporter-rules/daily-contracts.md`；建頁另讀 `.claude/reporter-rules/page-templates.md`；本記者負責頁的表格契約見 `.claude/reporter-rules/safety-policy/pages.md`。

分類為「安全政策」的新聞條目由此記者負責。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/topics/anthropic-government-policy.md` | Anthropic 與各國政府互動、出口管制、軍事合約 |
| `wiki/topics/ai-agent-safety.md`（母頁）＋三個子頁 | AI agent 安全事件、漏洞披露、提示注入、網攻與濫用。**事件寫進子頁**：查 `.claude/reporter-rules/safety-policy/pages.md`「topics/ai-agent-safety」第 0 條路由表——`ai-agent-safety-prompt-injection`（提示注入與自我複製）、`ai-agent-safety-product-vulns`（產品漏洞、誤操作、帳號）、`ai-agent-safety-cyber`（網攻能力、濫用、防守方准入）；判不出寫母頁 `### 未歸類`。寫了事件的子頁覆寫它的 callout，母頁 callout 同批覆寫成一句總覽並連子頁；母頁其餘只准動第 1 條列的三樣，「最後新聞更新」不動。來源歸因的 page 一律填事件所在的子頁，母頁 callout 不報歸因 |
| `wiki/topics/ai-eval-boundary-incidents.md`（`ai-agent-safety` 子頁） | 評測越界事件：AI 評估中模型做出未經授權、影響到評估範圍外的動作（UK AISI、Anthropic 自揭的評測事故）、數字口徑與官方處置 |
| `wiki/topics/recursive-self-improvement.md` | AI 遞歸自我改進、全球監管呼籲 |

> 上表為核心頁面與觸發條件；此外 `wiki/index.md` 中領域為 🏛️ 政策/安全 的所有頁面（含日後新增）皆由本記者負責維護與 lint。

---

## 每日動作

各頁有自己的逐步順序與結論表契約，逐條照 `.claude/reporter-rules/safety-policy/pages.md` 執行：

- `anthropic-government-policy`：`## 攻防紀錄` prepend ＋ `## 時序` prepend ＋ 四張結論節的覆寫與退場
- `ai-agent-safety` 樹：事件依路由表 prepend 進子頁 `## 技術彙整` 當月節＋該子頁 `## 時序` ＋ 子頁結論層與母頁現況表的覆寫與退場（第 1–2 條與各子頁節）
- `ai-eval-boundary-incidents`：評測越界事件寫進這一頁（路由見 `.claude/reporter-rules/safety-policy/pages.md`「topics/ai-agent-safety」第 0 條）；母頁不留指標行
- `recursive-self-improvement`：無專屬結論表，照頁面既有結構 prepend 並更新兩個日期欄位

記者無 web 工具：官方一手來源、訴訟文件與 GitHub issue 狀態的查證屬主編層，遇到只能提列並在「同步自查」欄回報。

---

## 回報格式

照 `.claude/reporter-rules/shared.md`「回報格式（回報契約）」八欄；`feature-radar 新增` 欄恆填「無」。安全事件涉及 Claude Code 功能面時，「同步自查」欄註明「請主編轉知功能記者」。
