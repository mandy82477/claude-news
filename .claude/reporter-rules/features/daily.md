# Wiki Ingest — 功能記者指南（daily）

開工先讀 `.claude/reporter-rules/shared.md`；建頁另讀 `.claude/reporter-rules/page-templates.md`；本記者負責頁的表格契約見 `.claude/reporter-rules/features/pages.md`。

分類為「功能」的新聞條目由此記者負責。

---

## 負責頁面

| 頁面 | 觸發條件 |
|------|---------|
| `wiki/entities/claude-code.md` | Claude Code 版本更新、新指令/旗標、Breaking change |
| `wiki/entities/bugcrawl.md` | BugCrawl 漏洞偵測工具動態 |
| `wiki/topics/anthropic-agent-stack.md` | 官方 agent 積木總覽（母頁）：八張積木卡（為什麼出／多給了什麼／還做不到什麼）、「怎麼疊」、決策樹與兩份附錄。agent 架構相關功能經「多標三件事」寫入本頁（見 `.claude/reporter-rules/features/pages.md`）；官方查證欄位由主編維護 |
| `wiki/entities/managed-agents.md` | Managed Agents 框架更新（[[topics/anthropic-agent-stack]] 的子頁，收代管平台產品事實：現況、計費、零件成熟度、歷史） |
| `wiki/entities/claude-design.md` | Claude Design 工具更新 |
| `wiki/entities/claude-security.md` | Claude Security 資安產品動態 |
| `wiki/entities/claude-skills.md` | Skills 官方產品線與生態：官方技能包、平台支援、分享機制、第三方移植（設計面歸社群記者 patterns 頁） |
| `wiki/topics/official-community-gap.md` | 官方功能 vs 社群痛點缺口變化 |
| `wiki/topics/coding-workflow-guide.md` | 🗓️ 主體週更（吃技能清冊）；**官方對既有功能的使用指南**在每日 ingest 即寫入對應流程階段節——見 `.claude/reporter-rules/features/pages.md`；`## 6. 測試與上線` 段末保留一行指向 [[topics/anthropic-agent-stack]]「你該用哪個」的出口（連頁不連錨——該段標題帶進度標記會改名）|
| `wiki/topics/long-context-1m.md` | 1M context 的**計費規則、預設行為、可控性、可見性**（世代加價分界、預設開啟／關閉、model picker 保不保得住 `[1m]` 變體、UI 顯示的 context 上限是否正確、1M 觸發獨立計費通道）——觸發邊見 `.claude/reporter-rules/features/pages.md` |
| `wiki/topics/claude-code-experimental.md` | 「Build Flags」來源條目（每版至多一則）：條目列的功能候選旗標各入追蹤表第一階；同輪跑 `python scripts/build_flags_mentions.py` 對社群提及，有命中才升第二階；官方承認、出貨、消失各要對應證據——頁面契約見 `.claude/reporter-rules/features/pages.md` |
| `wiki/feature-radar.md` | 新增/更新功能條目（**須回報主編彙整**，不直接寫入） |

> 上表為核心頁面與觸發條件；此外 `wiki/index.md` 中領域為 🛠️ 工具/功能 的所有頁面（含日後新增）皆由本記者負責維護與 lint。

GitHub Issues 來源的高互動 bug/issue 條目歸功能記者，記入 claude-code.md 已知問題（含 issue 編號與連結）；不進 feature-radar。

---

## feature-radar 准入定義

feature-radar 只收**使用者可實際取用、呼叫、設定或執行的官方產物**。收錄前先問：

> 「使用者拿這個能做什麼**具體操作**？」答不出來 → 不收錄。

✅ **屬於功能（收錄）：** 新模型 / 模型能力（可 `--model` 選用）、新指令 / 旗標 / 設定項、新 API / SDK 變更 / 棄用、影響使用方式的 Breaking change。

❌ **不屬於功能（不收錄，改投對應頁面）：**

| 類型 | 範例 | 改投 |
|------|------|------|
| 研究成果 / 論文（無可用介面）| 化學 NMR 分析 | 對應 entities 或略過 |
| 公益 / CSR / 組織 / 人事 | Claude Corps | `topics/anthropic-business` |
| 定價 / 計費 / 配額政策 | Agent SDK 計費切割 | `entities/pricing` |
| 商業合作 / 融資 | TCS / DXC 合作 | `topics/anthropic-business` |
| 純策略表態（無新功能）| HTML 輸出背書 | `topics/community-tech-discussions` 或略過 |

> 模型本身算功能（可選用）；模型的**定價**歸 `entities/pricing`。

---

## feature-radar 動作表

| 情況 | 動作 |
|------|------|
| 日報出現新的官方功能（先過准入定義）| 準備新條目，**回報主編** |
| 已追蹤功能再次出現（討論、工具跟進）| 熱度 +1 格（上限 🔥🔥🔥🔥🔥），回報主編 |
| 出現多個正面使用案例 | 試用價值升級（⏳→⚡→✅），回報主編 |
| 出現重大 bug 或集中負評 | 試用價值降級，回報主編 |
| 功能從 Preview 升格正式 | 考慮升為 ✅，回報主編 |
| 已追蹤功能連續 4 週未在日報出現 | 熱度 **−1 格**（下限 🔥），回報主編並同步對應 entities 頁的熱度表 |

條目與表列的格式、上限、退場與同步規則見 `.claude/reporter-rules/features/pages.md`「feature-radar」節。

### 否定證據也要有路回來

**收到主編轉知的**日報條目若拿某個官方功能當對照組，宣稱替代方案在成本、準度或速度上更好（無論該條目被分類成社群、是否達收錄標準），在對應 `entities/` 頁的細節區記一行，**必附證據等級與缺什麼**（如「單一貼文，未附測試方法」），並於回報「同步自查」欄註明來源日期。**不進 feature-radar、不改熱度以外的評級**——它是讀者判斷「值不值得」的唯一反向材料，不是功能異動。發訊端規則見 `.claude/reporter-rules/community/daily.md`「官方功能的負向對照要回流」。

---

## 版本更新收錄判斷

版本號本身不是收錄理由，**必須有至少一項使用者端的具體異動**才進 feature-radar：

| 情況 | 判斷 | 處置 |
|------|------|------|
| 純 bug fix / reliability（無具體功能說明）| ❌ 不收錄 | 記入 `entities/claude-code` 版本表 |
| 內部基礎設施更新 | ❌ 不收錄 | 略過 |
| 單一 bug 的 hotfix（已屬於另一功能的修正）| ❌ 不收錄 | 附記在對應功能條目「注意事項」 |
| 有新指令 / 新旗標 / Breaking change | ✅ 收錄 | 正常建立條目 |
| API 棄用 / 重大 SDK 變更 | ✅ 收錄 | 以「SDK / 棄用」為主題建立條目 |

---

## 回報格式

照 `.claude/reporter-rules/shared.md`「回報格式（回報契約）」八欄，本記者無專屬欄位差異；`feature-radar 新增` 欄填條目標題或「無」。
