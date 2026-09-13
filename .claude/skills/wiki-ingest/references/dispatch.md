# Wiki Ingest 派工模板

`.claude/skills/wiki-ingest/SKILL.md` 步驟 3／4b／4c 的 prompt 單一來源。步驟語意不在本檔。

## 類別↔角色檔對照表

| 類別 | 角色檔（`.claude/agents/`） |
|------|--------------|
| 模型 | `wiki-reporter-models` |
| 功能 | `wiki-reporter-features` |
| 商業 | `wiki-reporter-commercial` |
| 安全政策 | `wiki-reporter-safety-policy` |
| 社群 | `wiki-reporter-community` |
| 人物 | `wiki-reporter-people` |

## 六記者派工 prompt（步驟 3）

每個 Agent 呼叫一律 `subagent_type: "general-purpose"` + `model: "sonnet"`。prompt 傳入以下五個區塊（第一段角色前導不可省略——它是記者拿到規則的唯一途徑）：

```
你是 CLAUDE_NEWS wiki 的「[類別]」記者。開工前先 Read `.claude/agents/wiki-reporter-[category].md`——那是你的角色定義（含「開始前必讀」規則清單與回報契約），逐條照做後再處理下面的任務。你不可再呼叫 Agent tool 委派任何工作。

今日日報日期：[YYYY-MM-DD]
你負責的分類條目原文節錄：

[貼入步驟 2 整理好的該類別條目區塊]

你負責頁面今日命中的待查證項目（機械偵測，可能誤判；無則寫「無」）：

[貼入掃描器輸出中該類別的區塊，無命中該類別則寫「無」]

轉知待接手（其他記者先前交辦給你的事；無則寫「無」）：

[貼入 `python scripts/pending_handoffs.py list --to [類別]` 的輸出]
```

**防偏誤說明（隨每次派工附上，不可省略）：** 此清單僅供比對——若今日條目足以作為某筆懸置的後續，在該標記加 `｜訊 YYYY-MM-DD` 並更新內文；證據不足則不動並在回報說明。**不可為了消化懸置而過度解讀新聞；不可刪標記、改狀態符號或宣告結案**（結案屬 `/wiki-lint` 5c）。

記者的角色、規則引用、回報格式只定義在角色檔 `.claude/agents/wiki-reporter-[category].md`（單一來源），由上方角色前導導入；派工 prompt 不重抄規則內文。

**🚫 prompt 內不得臨場加寫「今日順手做 X」「記得同步 Y 頁」這類操作指示**——上方五個區塊（角色前導／日期／條目節錄／待查證命中／轉知待接手）加防偏誤說明即為完整 prompt，不再增加。針對單一條目的事實性提示寫在該條目的 `- **註：**` 行內。理由與 2026-08-15 教訓見 `.claude/reporter-rules/wiki-ingest.md`「派工 prompt 不得臨場加寫操作指示」。

## 4b devpractice 沉澱 prompt 首段

```
你是 CLAUDE_NEWS wiki 的「開發實務（devpractice）」記者。開工前先 Read `.claude/agents/wiki-reporter-devpractice.md`——那是你的角色定義，逐條照做後執行 **daily 沉澱**。今日日期：[YYYY-MM-DD]。你不可再呼叫 Agent tool 委派任何工作。
```

## 4c market 判讀 prompt 首段

```
你是 CLAUDE_NEWS wiki 的「投資分析（market）」記者。開工前先 Read `.claude/agents/wiki-reporter-market.md`——那是你的角色定義，逐條照做後執行 **daily 判讀**。今日日期：[YYYY-MM-DD]。你不可再呼叫 Agent tool 委派任何工作。
```
