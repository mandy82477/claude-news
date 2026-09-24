---
page: "topics/competitor-landscape"
kind: "topic"
status: "ongoing"
domain: "💼 商業"
last_updated: "2026-09-23"
last_news_update: "2026-09-23"
status_main: "ongoing"
days_since_news: 1
parent: null
children: "['topics/competitor-landscape-archive']"
page_role: "hub"
days_since_news_subtree: 1
inbound_links: 62
attribution_count: 116
attribution_last: "2026-09-23"
top_source: "google-news"
pending_count: 3
pending_overdue: 0
pending_next_review: "2026-09-27"
pending_signalled: 2
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# AI 編碼工具競品動態

**狀態：** ongoing
**領域：** 💼 商業
**蒐集邊界：** 以 Claude 為參照系的競品動態為主，另針對競品發布與定價定向補抓（每日至多 2 則）；競品自身未與 Claude 對比的發布可能延遲或缺漏。**帶跑分數字的第三方對照評測收不到**——這類內容多發表於對照型部落格，不在本站蒐集範圍，因此本頁的競品能力比較以官方數字與社群並排實測為主，缺口處改指向外部活榜單（見 [[topics/model-comparison]] 的外部評測榜單節），不自行推算。
**開始日期：** 2026-04
**最後更新：** 2026-09-24
**最後新聞更新：** 2026-09-24

> **本週衝擊**（2026-09-24）
> - 🔴 **GitHub Copilot 持續加碼企業信任功能**：code review 新增個人化設定＋企業層級預設，全面 GA（09-23）；疊加本地沙箱／OTel／JetBrains 工具核准（09-22），GitHub 官方 changelog——Claude Code 均無對應設定，企業採購比較時會被問到。
> - 🔴 **OpenAI V7 把機構記憶做成官方案例**：GPT-6 Astra 在最難圖查詢測試拿下 89% 準確率（09-21，OpenAI 官方部落格）——agentic 信任案例首度帶量化數字，長期 context／記憶需求高的人值得追蹤。

---

## 摘要

競爭的主戰場已從「誰更強」移到「誰更便宜」：Meta 以三層訂閱打價格戰、Google 推低價企業方案、中國市場出現「免費夠用」的論述。同一時間開源陣營把旗艦模型的權重也放了出來，低價層第一次同時具備可用的工具與可用的模型。對用 Claude 的人，眼前要判斷的不是換不換，而是自己所在的那一層有沒有出現可比的價格或能力落差——下方「對手雷達」即按這個標準排序。

## 對手雷達

> 衝擊度量的是「若這則屬實，你要不要改變什麼」；證據夠不夠硬是另一欄，兩者分開看。排序：衝擊度降序，同級以最新動態日期新者在上。

| 對手 | 最新動態（日期） | 衝擊面 | 衝擊度 | 這個消息有多硬 |
|---|---|---|---|---|
| **OpenAI（Codex CLI／ChatGPT Work・GPT-5.6）** 🏢 | V7 賦予 agent「機構記憶」，GPT-6 Astra 於最難圖查詢測試達 89% 準確率（09-21，官方）→ agentic 案例首度升級為量化數字，直指 Claude 長期 context／記憶定位 | 能力 | 🔴 | OpenAI 官方部落格自報準確率，無第三方複現或獨立驗證 |
| **Microsoft／GitHub** 🏢 | Code review 新增個人化設定＋企業層級預設全面 GA（09-23）；另有本地沙箱／OTel／JetBrains 1.18 工具核准（09-22）→ Claude Code 目前均無對應設定，企業信任功能持續追平 | 能力 | 🔴 | GitHub 官方 changelog 一手來源；HydraFusion 降本宣稱（09-04）仍缺品質基準對照，自研模型取代動機已獲官方高層證實（09-20 查證） |
| **Meta（Muse Code／Muse Glimmer）** | 結束 beta、三訂閱層主打價格戰（09-01）；旗艦模型 Muse Glimmer 開源（08-11）→ 想比價卻比不了，月費未公布 | 定價 | 🔴 | 跨 2 媒體（The New Stack／Intelligent Living），月費與 20x 層費率均缺 |
| **DeepSeek** 🏢 | Harness 開源＋V4-Pro 上線（08-14）、中國市場「免費夠用」論述（08-31）→ 低價層已有可用替代 | 定價 | 🔴 | VentureBeat 2 來源；V4-Pro 費率已查證 ⟨Q-01⟩（見下方細節與「競品定價對照」） |
| **Zhipu Z.AI** | GLM-5.3 主打資安、稱抓 bug 優於 Anthropic 與 OpenAI（08-17）→ 靠 Claude 做安全審查的人值得找機會實測對照 | 能力 | 🔴 | 2 家媒體（The Register／VentureBeat），無方法論、無 benchmark 數字 |
| **Moonshot AI（Kimi K3）** | 權重開源，效果與 Fable 5 相當、成本約三分之一但慢約 4 倍（07-27）→ 可離線批次的工作有便宜選項 | 能力 | 🔴 | The New Stack 量化實測＋官方一手規格；官方自陳整體仍落後 Fable 5 |
| **xAI（Grok 4.7）** | Grok 4.7（基於 4.6，主打 agentic coding／複雜工作流）於 GitHub Copilot 上線（09-21）→ 經 Copilot 生態擴大觸及，多一個推理模型選項 | 生態 | 🟡 | GitHub 官方 changelog 一手來源，惟無 benchmark 或定價資訊 |
| **Google（Gemini）** 🏢 | Gemini 3.8 Live／Extended Thinking 推出語音 agent 與近即時多步推理（09-15）→ 評估語音場景時多一個對照對象；另有低價企業方案劍指 Anthropic（08-27） | 能力 | 🟡 | DeepMind 官方部落格一手；企業方案為 Google Cloud 消費制計費，非固定席位價（2026-09-20 查證 ⟨Q-06⟩，見下方細節） |
| **Cursor** 🏢 | OpenAI 傳 11/12 斷供（09-04）→ 只影響 Cursor 使用者，Claude Code 使用者不必動 | 生態 | 🟡 | 單一 Reddit 週熱門討論串，無官方、無主流媒體 |
| **Alibaba（Qwen3.8）** | 免費開放「最強」模型、稱幾乎追平 Claude（08-04）→ 低價層再多一個免費選項，能力宣稱待證 | 能力 | 🟡 | Decrypt 單一來源，無模型名稱、無 benchmark（🔎 見下方定價細節） |
| **Kiro（AWS）** | spec-driven 編碼 agent，Free 至 Power $200 五級訂閱（08-03）→ 已在 AWS 生態的人可直接比價 | 定價 | 🟡 | 官網定價已查證（08-13）；標題並列的 80.8% SWE-bench 歸屬未獲證實 |
| **OpenCode** | 開源免費替代，社群採用規模仍是主要訊號（08-01）→ 想離開訂閱制時的第一個候選 | 定價 | 🟡 | 下載量倍數的統計方法未揭露，完整脈絡見 [[entities/opencode]] |

**🏢 圖例**：具名企業採用記錄（見 [[topics/enterprise-tool-tracker]]）或官方企業方案，缺一不標。企業評估候選名單：雷達表帶 🏢 者；具名採用／退出記錄見 [[topics/enterprise-tool-tracker]]。

**懸置細節**
- ⟨Q-06⟩ 已查證（2026-09-20，[antigravity.google/docs/plans](https://antigravity.google/docs/plans/)）：企業存取走 Gemini Enterprise Agent Platform，Google Cloud 消費制計費，無固定席位價，不支援 BYO-key／合約制組織方案。
- 個人方案不變：Pro ~$20／Ultra ~$100／Ultra 20x $200。

%% 維運備忘：上表固定 12 列，⚪ 級一律不佔列，動態只在時序累積。2026-09-07：騰訊 Hy4（唯一 ⚪ 列）讓位給新進 xAI（Grok 4.5，🟡），移入下方未列入清單。 %%
**未列入上表**（⚪ 級，動態仍記在下方時序）：騰訊 Hy4（08-29，開放權重 770B、不含視覺，尚無對比對象）、Slack Code（Salesforce，08-26 官方確認，整合 Claude 與 ChatGPT 而非取代）、Inherent（08-23，公司自宣）、Thinking Machines Inkling（07-20 首款開源權重模型）、Perplexity（07-07 傳聞開發中）、中國 360 Tulongfeng（06-28，網路安全 AI，對標 Mythos 5）、Sakana AI Fugu（06-28，宣稱對標 Fable 5）、Google 未命名競品（Sergey Brin 主導，04 月起無新動態）；AgentConnect（新聞稿自宣）依准入不入表。

## 硬答案

> 每條都要能回答「依據是什麼、哪天查的」；跨家跑分數字不寫在這裡，見下方「查證快照」與 [[topics/model-task-leaderboard]]。

- **Claude Code 是不是最貴？** 是，也最快——Composio 以 30 項真實工具任務實測：Claude Code $0.195／任務（122 秒，最快），OpenCode $0.073／任務（約 2.7 倍價差）（2026-08-13 查證）。
- **Codex 和 Claude Code 誰強？** 沒有單一答案——不同基準測不同能力面向，該看的是任務類型對應的基準與 [[topics/model-task-leaderboard]] 本週快照；當時的實測數字見下方「查證快照」節（2026-08-13 查證）。
- **便宜的 harness 真的省嗎？** 省，且差異多來自 harness 而非模型——Databricks 實測 GLM 5.2 省約 34%；Pi harness 在 Opus 4.8 high 下便宜約 2.08 倍，主因傳遞 context 量約為 Claude Code 的 1/3（2026-08-13 查證）。
- **Kiro 標題那個 $200 是跟 Claude Max 比嗎？** 不是——那是 Kiro 自身 Power 方案的月費，非跨產品比較（2026-08-13 查證 kiro.dev）。
- **Gemini CLI 還免費嗎？** 不是——2026-06-18 起免費／Pro／Ultra 帳號停止 Gemini CLI，併入 Antigravity CLI，個人開發者需轉付費 API key（2026-08-13 查證）。
- **GitHub Copilot Pro+ $39 比 Claude 便宜嗎？** 名義月費較低，但 Opus 存取採 27 倍加價換算，重度使用時實際成本可能反超（2026-05-06 查證，此後未回訪）。

## 競品定價對照

> 這裡回答「競品各多少錢」。Claude 自身方案價格不重複列，完整版本見 [[entities/pricing]]「我的方案現在有什麼」。數字均回溯 `news/` 原文查證；查無具體公開數字者依懸置標記語法標示，不可假設。
> **vs Claude** 欄基準取自 [[entities/pricing]] 2026-08-20 牌價（Sonnet 5 $2/$10 per Mtok），比例隨兩邊調價變動；訂閱制或免費工具無按 token 計費基礎，標 `—` 並註明理由。

| 工具/模型 | 定價 | vs Claude | vs Claude 定位 | 來源日期 |
|---------|------|-----------|--------------|---------|
| Muse Code / Muse Spark 1.2 / Muse Glimmer（Meta）| 按量計費：標準層 $1.25／$4.25、Contributor 層 $0.10／$0.20（每 M token）；Glimmer 開源免費 | 標準層≈0.43×、Contributor 層≈0.02×（對 Sonnet 5 $10/Mtok 輸出）；Glimmer 免費 | 明確對標 Claude Code 與 Codex，第一步策略是價格而非能力 | 2026-09-01（定價數字為媒體整理，2026-08-13 查證）|
| DeepSeek（V4-Pro／V4 Flash／Lindy 案例）| 官方查證：V4-Pro 輸入 $0.66／輸出 $1.98（離峰，每 M token，快取未命中；尖峰時段雙倍）；V4 Flash（官方頁列「DeepSeek-Flash」）輸入 $0.15／輸出 $0.60（離峰） | V4-Pro 輸出≈0.198×、V4 Flash 輸出≈0.06×（對 Sonnet 5 $10/Mtok 輸出，離峰價） | 低價 Flash／高價 Pro 雙軌已證實；Lindy 全量切換每月省數百萬美元 | 2026-08-14 上線（Google News/VentureBeat）；定價 2026-09-20 查證（[DeepSeek 官方定價頁](https://api-docs.deepseek.com/quick_start/pricing/)）|
| Alibaba Qwen3.8-Max（已查證 ⟨Q-03⟩）| 免費開放權重（Hugging Face／ModelScope） | 免費（無倍數可算） | 2.4 兆參數（95B 啟用），Terminal-Bench 2.1 得 86.6（Opus 4.8／Fable 5 同 84.6），細節見下方 | 2026-08-04 首報；08-03 發布＋benchmark 09-20 查證 |
| Kiro（AWS） | Free（50 credits）／Pro $20／Pro+ $40／Pro Max $100／Power $200，每人每月 | —（訂閱制，非按 token 計費，不可比） | AWS 旗下 spec-driven 編碼 agent（IDE/CLI/Web）；$200 為其自身頂層方案，非跨產品比較 | 2026-08-03（[kiro.dev](https://kiro.dev/)，2026-08-13 查證定價）|
| OpenCode | 免費（開源）| —（免費開源工具，實際成本取決於所接模型） | 開源免費 vs 訂閱付費（$20/月）的採用落差，是本頁最早的分流訊號；已查證 ⟨Q-04⟩：下載量統計為 npm registry 公開數字，非推算 | 2026-08-01（Google News/tech-insider.org）|
| Antigravity（Google） | Free（20 次/日）／Pro ~$20／Ultra ~$100／Ultra Max $200（原 $249.99 調降）| —（訂閱制，不可比） | 依附 Google AI 訂閱框架；與 Cursor、Claude Code 並列比較 | 2026-07-23（第三方比較站彙整，2026-08-13 查證）|
| Cline | 免費（Free，工具本身）| —（工具免費，token 費用另計） | 開源 VS Code 擴充，介於 Claude Code（$20/月）與 Copilot（$10/月）間的免費替代；用量限制已查證 ⟨Q-05⟩，見下方 | 2026-07-22（Google News/tech-insider.org）|
| Cursor | Hobby 免費／Pro $20／Pro+ $60／Ultra $200／Teams $40/user／Enterprise 客製 | —（訂閱制，不可比） | 已查證：SpaceX 收購後未見因收購而生的定價異動，6 級方案為既有架構延續 | 2026-08-13 查證（收購確認 2026-06-17）|
| OpenAI Codex CLI | Free（試用）／Go $8／Plus $20／Pro 5x $100／Pro 20x $200／Business $30/user／Enterprise 客製 | —（訂閱制，不可比） | 已查證：2026-04-02 起改按 token 用量計費，非固定訊息數 | 2026-08-13 查證（多方比較站彙整）|
| GPT-5.6（OpenAI API） | 已查證：Luna 降 80%（$0.20／$1.20）；Terra 降 20%（$2／$12）；Sol 未降價但提速 2.5 倍 | Luna≈0.12×、Terra≈1.2×（對 Sonnet 5 $10/Mtok 輸出）；Sol 未提新價 | OpenAI 官方明確訴求以更低價格對打 Anthropic | 2026-07-30（OpenAI 官方；2026-08-13 查證數字）|
| Gemini CLI / Gemini 系列 | 已查證：Free $10 一次性／Pro $60/月／Max $200/月；2026-06-18 起免費層併入 Antigravity CLI | —（訂閱制，不可比） | 免費層緊縮後，個人開發者需轉 Antigravity CLI 或付費 API key | 2026-08-13 查證（多方比較站彙整）|
| Grok 4.5（xAI） | $2／$6 per Mtok（input／output） | 輸入 1.0×、輸出 ≈0.6×（對 Sonnet 5 $2/$10 per Mtok） | 宣稱優於 GPT-5 與 Claude，對標哪個 Claude 模型未指明，無 benchmark 佐證 | 2026-09-07（單一來源 shattered.io）|

**競品定價細節**
- ⟨Q-01⟩ 已查證（2026-09-20，[DeepSeek 官方定價頁](https://api-docs.deepseek.com/quick_start/pricing/)）：V4-Pro 輸入 $0.66／輸出 $1.98（離峰，快取未命中）；V4 Flash 輸入 $0.15／輸出 $0.60（離峰）。
- V4-Pro 輸出約為 V4 Flash 的 3.3 倍，確認雙軌定價策略屬實；尖峰時段（UTC 01:00–04:00、06:00–10:00 週一至五）雙倍。
- **DeepSeek 雙軌與對比對象**：V4-Pro 隨開源工具 Harness 同步上線，API 定價較 V4 Flash 高，可能為「低價 Flash／高價 Pro」雙軌策略（推論）；KuCoin「逼近 Claude 3 Opus」是 DeepSeek 對 Claude 的比較，與內部兩模型互比不可混用。
- ❓ **待查證**（標 2026-08-13｜查 DeepSeek V4 Pro、Claude 3 Opus｜複 2026-09-27｜訊 2026-09-06）：對標對象曾為非最新旗艦 Claude 3 Opus；09-06 tech-insider.org 改對照 Opus 5（現行旗艦，另含 Gemini 3.1），稱「15 分差距」，惟測試方法論與具體分數仍未見，官方頁面未查證。
- **Lindy 案例（06-29，CNBC）**：AI 新創 Lindy 100% 流量自 Claude 切至 DeepSeek，每月省下數百萬美元，屬企業級大規模用量的相對節省，非單一訂閱價格對比。
- **Muse Code 定價來源**：定價數字為媒體整理（Wavect、The New Stack），Meta 官方獨立掛牌頁未見（2026-08-13 查證）；09-01 三訂閱層與「20x」折扣層的實際費率均未公布。
- ⟨Q-03⟩ 已查證（2026-09-20）：08-04 Decrypt 所稱「免費最強模型」即 08-03 正式發布的 **Qwen3.8-Max**——2.4 兆參數（95B 啟用）MoE、1M context，權重開源。
- 官方 benchmark：31 項文字測試 Fable 5 奪 15 冠、GPT-5.6 Sol 9 冠、Qwen 7 冠；Terminal-Bench 2.1 得 86.6（Opus 4.8／Fable 5 同 84.6）。「幾乎追平」與官方數字大致吻合，非誇大。
- **Kiro 的 80.8% SWE-bench**：該分數歸屬（Kiro 或 Claude Code）查證後仍未見官方或後續報導證實，kiro.dev 官網未列此分數。
- ⟨Q-04⟩ 已查證（2026-09-20）：5.4 倍統計基礎為 npm registry 公開下載數字——2026-07-31 止 30 天窗口 Claude Code 44,264,901 次 vs OpenCode 8,245,142 次，方法公開可驗證，非黑箱推算，脈絡見 [[entities/opencode]]。
- ⟨Q-05⟩ 已查證（2026-09-20，[Cline 官方 FAQ](https://cline.bot/faq)）：Cline 工具免費、僅收所接模型 token 費；官方載明免費模型（如 Gemini）常遇 rate limit，惟未公布量化上限數字。
- **已移出表**：GitHub Copilot Pro+（$39/月，Opus 採 27 倍加價換算）來源日期 2026-05-06 已逾 90 天，結論保留於「硬答案」；Kimi K3、HydraFusion 僅有相對成本的定性宣稱、無掛牌價，改記於「對手雷達」硬度欄與「雷達細節」。
- **pi-coding-agent**：低成本編碼 agent 的成本數字已升格為「硬答案」條目（Databricks，2026-08-13 查證）。
- **GLM-5.2 外部榜單佐證**：FrontierSWE 74.4 vs Opus 4.8 75.1、Terminal-Bench 2.1 81.0、SWE-bench Pro 62.1；單一外部來源、非日報進料，使用者 2026-07-17 手動查證，詳見 [[log]] 該日 Query 條目。

已查證（2026-09-20）｜**中美 AI 定價戰現已有具體數字**：08-14 FT／The Information 報導的定價戰敘事，後續已有量化佐證——OpenAI 官方將輕量版 GPT-5.6 Luna 降價 80%，API 費率降至 $0.20／$1.20（每 M token，輸入／輸出）；Anthropic 以 Opus 5 回應，官方定價約為前代旗艦的一半。中國開源模型仍以低 60–90% 每 token 定價施壓，惟截至 2026 年中，美中閉源模型定價差距已收斂至輸入 19%、輸出 14%（第三方統計）。本頁既有多筆「中國模型較 Claude 便宜數十至上百倍」的訊號（如 DeepSeek V4 Flash「降逾 100 倍」定性描述）與此處官方降價後的實際倍率需分開看——降價後價差已顯著收斂，不可再套用降價前的舊倍數。

## 雷達細節

> 只為衝擊度 🔴 的對手開節，每節只寫「現在」；軌跡看下方「時序」。

### Meta（Muse Code／Muse Glimmer）
**現在的答案**
- 09-01 結束 beta、三訂閱層主打價格戰，但月費未公布——現在算不出跟 Claude 加購方案誰划算，先不必動。
- 按量計費層已可比價：標準層 $1.25／$4.25，Contributor 層以「資料可能用於訓練 Meta 模型」換 $0.10／$0.20。
- 08-11 起旗艦模型 Muse Glimmer 開源，Meta 的戰線同時涵蓋產品層與模型層權重。
**還沒解決**
- 三訂閱層費率、「20x」折扣層對應價格、Glimmer 的授權條款與 benchmark 均未見報導。

### DeepSeek
**現在的答案**
- 低價層已有可用替代：開源工具 Harness 正式定名上線（08-14），與 V4-Pro 模型同步。
- V4-Pro 費率未載，只知高於 V4 Flash；V4 Flash 側僅有「較 Claude API 降低逾 100 倍」的定性描述。
- 中國市場已出現「免費 Harness 夠用、付費訂閱是否值得」的公開質疑（08-31，36Kr）。
**還沒解決**
- V4-Pro 具體費率、Harness 與既有「Deep Code」（07-07）是否同一產品線，報導均未說明。

### OpenAI（Codex CLI／ChatGPT Work・GPT-5.6）
**現在的答案**
- 選型看任務類型：不同基準測不同能力面向，無單一「孰優孰劣」結論（數字見「查證快照」）。
- 定價面已實際下修：GPT-5.6 Luna 降 80%、Terra 降 20%，Sol 未降價但提速 2.5 倍（07-30 官方）。
- 企業側戰線已擴至資料隱私：08-20「零資料保留」承諾明確定位為爭奪 Anthropic 企業客戶。
- GPT-6 Astra 官方自曝案例已升級為兩則：Perplexity 自主寫通訊、改軟體、監控正式環境（09-13）；V7 賦予 agent「機構記憶」，把企業檔案轉為 agent context，最難圖查詢測試達 89% 準確率（09-21）——兩則均直指 Claude Code 的自主任務與長期記憶定位。
**還沒解決**
- 「零資料保留」的技術實作與涵蓋範圍、以及 OpenAI 企業用戶「追近」的量化數字均未見。
- GPT-6 Astra 全面上線 Pro／Enterprise／API 的具體規格、V7 的產品化時程與是否對外開放均未見報導，89% 準確率的測試方法論未載。

### Microsoft／GitHub
**現在的答案**
- 09-23：code review 新增個人化設定選項、擴大適用方案，並提供企業層級預設，全面 GA。
- 09-22／23：本地沙箱（限制未預期指令存取檔案／網路／憑證）、OpenTelemetry 納入企業管理設定、JetBrains 1.18 新增 AI 工具核准與組織共享技能／指令——**Claude Code 目前均無對應設定**。
- 09-19 code review 改版＋10/19 起停用部分模型；09-17 官方 changelog 三連發：預算增加請求開放、Impact Dashboard、CLI 用量指標——企業管理可見度全面加強。
- 已查證（09-20）：自研模型取代已獲官方高層證實動機（首席 AI 官 Suleyman 公開發言），非僅傳聞，詳見 [[topics/anthropic-business#還沒過去的風險]]。
**還沒解決**
- 沙箱與 OTel 設定細節、JetBrains 版本適用範圍、停用模型清單均未見完整報導。
- code review 個人化設定的具體項目、擴大後適用哪些方案層級均未見細節。

### Zhipu Z.AI
**現在的答案**
- 差異化訴求已定在資安與除錯：GLM-5.3 主打進階資安能力，並稱已在 Cursor 找到一個「嚴重漏洞」（08-15）。
- 能力宣稱已從點名單一工具升級為正面對比 Anthropic 與 OpenAI 兩家模型商（08-17，The Register）。
- 產品層另有免費 ZCode（07-06）對標 Cursor 與 Claude Code，價格施壓對象是個人開發者與新創。
**還沒解決**
- 是否為同一款 GLM-5.3、測試方法論、benchmark 數字均未見；Cursor 官方亦未回應該漏洞宣稱。

### Moonshot AI（Kimi K3）
**現在的答案**
- 開源權重可直接取用（07-27），不必依賴 API；官方規格為 2.8 兆參數、100 萬 token context、原生視覺。
- 第三方量化實測：效果與 Fable 5 相當，成本約三分之一但速度慢約 4 倍——性價比構成威脅，時間敏感的工作不受影響。
- 官方自陳整體表現仍落後 Fable 5 與 GPT-5.6 Sol，社群「超越」說法未獲實測支持。
**還沒解決**
- 開源授權條款、下載規模與訓練成本未見細節。

## 查證快照（2026-08-13）

%% 維運備忘：本節不新增、不回訪。到期日 2027-02-09（建立日 +180 天），屆時整節移除 %%
> 本節是 2026-08-13 那一天查到的數字，**之後沒有再更新**；要看最新排名請去 [[topics/model-task-leaderboard]]。
>
> 當時可引用的四組數字（不同基準測不同能力面向，無單一結論）：
> - Supabase Evals：Build 階段 Opus 5／Kimi K3 均 100%，其他模型經 skills 輔助追平
> - SWE-bench Verified：兩者持平 ~88.6–88.7%，Opus 5 發布後 Claude 升至 97.0%
> - SWE-bench Pro：Claude Opus 4.8 領先 69.2% vs 58.6%
> - Terminal-Bench：Codex 領先 82.7% vs 69.4%

| 日期 | 來源 | 內容 | 量化數字 |
|------|------|------|---------|
| 2026-08-22 | 36Kr | 「Codex 是否開始反擊 Claude Code？」產業競爭態勢觀察，與同日 HN 高分貼文呼應同一主題（另見 [[topics/community-tech-discussions]]，詳見下方細節） | 🔎 查無官方 ⟨Q-02⟩ |
| 2026-07-15 | HackerNoon（跨 2 來源） | 「Claude Code vs Codex vs OpenCode：全端工程師誠實裁決」，三方比較文 | 🔎 查無官方（標 2026-08-10｜複 2026-09-13）：為工程師個人觀點比較文，查證後仍未見具體評分數據 |
| 2026-07-22 | South China Morning Post（跨 2 來源） | 中國 Qiushi Engine（浙江大學團隊）於 ResearchClawBench 自主研究排行榜奪冠，Claude Code 第三、Open Science Desktop 第二 | 已查證：2026-08-13，[SCMP 原文](https://www.scmp.com/news/china/science/article/3361370/chinese-ai-agent-outperforms-anthropics-claude-code-autonomous-research) |
| 2026-07-25 | SitePoint | 「Codex 5.3 生產環境工作流——何時該選它而非 Claude 做複雜重構」，工作流選型建議文 | 🔎 查無官方（標 2026-08-10｜複 2026-09-13）：為工作流選型建議文，查證後仍未見具體評測方法論或分數 |
| 2026-07-29 | The Information（跨 3 來源） | 儘管 Codex／開源模型討論度上升，Claude Code 採用黏著度仍領先 | 🔎 查無官方（標 2026-08-10｜複 2026-09-13）：留存率、活躍用戶數等量化數字查證後仍未見報導揭露 |
| 2026-08-01 | MarkTechPost | Supabase 推出開源評測套件 Evals，以真實 Supabase 任務對 Claude Code、Codex、OpenCode 評分比較 | 已查證（08-13）：Build 階段 Opus 5／Kimi K3 均 100%；Sonnet 5 skills 輔助 78%→100%（詳見下方細節） |
| 2026-08-01 | [quasa.io](https://news.google.com/rss/articles/CBMilwFBVV95cUxQc3VGQXhIUWNkSElXb2swMFRjVlFscUE1ZTNuTXlwNjdTVGlVNmcyN0dMNk05NnJKdjZkeXpZa2dWdHkwYzRIdEh1LUFDelo5UTNPVjdWQm9lQmxRSTV3N0dWUUdsd3Y5Wk5tS1dnSEh3VTVwd3VlY0s5Mnk2VEVBX2EwOWpRbG9BOHQyVjNYWFZGd2tfYXlR?oc=5)（2026-07-31 22:00 UTC） | 「Claude Code vs OpenAI Codex: What Published Coding Tests Actually Show」——整理已公開的程式碼測試結果比較兩者實測表現 | 已查證（08-13）：SWE-bench Verified 持平 ~88.7%；SWE-bench Pro Claude 領先；Terminal-Bench Codex 領先（詳見下方細節）|

**查證快照細節**
- **36Kr（08-22）**：「Codex 是否開始反擊 Claude Code？」產業競爭態勢觀察報導，與同日 Hacker News 高分貼文「Quick impressions: A week of using Codex more than Claude」呼應同一主題（該則個人觀察角度另見 [[topics/community-tech-discussions]]）。
- ⟨Q-02⟩ 🔎 **查無官方**（標 2026-08-22｜查 Codex、評測方法論｜複 2026-10-04）：延伸查證 36Kr 同系列報導確認此篇性質為產業競爭態勢觀察評論，非帶方法論的評測文章，站內未見任何一篇 36Kr 報導提供 Codex vs Claude Code 的量化分數或測試方法；判定此則本質上不存在可查證的「評測方法論」，非官方未公開。
- **MarkTechPost（08-01）**：Supabase Evals 已查證（2026-08-13）——Build 階段 Opus 5／Kimi K3 均 100%（未輔助）；Sonnet 5 經 skills 輔助由 78%→100%、GPT-5.6 Sol 由 89%→100%（[supabase.com/evals](https://supabase.com/blog/introducing-supabase-evals)）。
- **quasa.io（08-01）**：第三方彙整已查證（2026-08-13）——SWE-bench Verified 兩者持平 ~88.6–88.7%（Opus 5 於 07 月發布後 Claude 升至 97.0%）。
- **quasa.io 其餘兩組**：SWE-bench Pro Claude Opus 4.8 領先 69.2% vs 58.6%；Terminal-Bench Codex 領先 82.7% vs 69.4%（2026-08-13 查證）。

## 相關頁面

- [[topics/model-comparison]] — 決定「我這份工作該用哪個模型」；本頁只管外面出現了什麼。
- [[topics/model-task-leaderboard]] — 跨家能力的活榜單——跨家跑分數字看那一頁，本頁只寫「這對選型代表什麼」。
- [[entities/pricing]] — Claude 自身方案與計費規則；本頁只列競品價格。
- [[topics/anthropic-business]] — Anthropic 自己的融資、合作、估值與資本支出。
- [[topics/enterprise-tool-tracker]] — 具名企業採用／退出的事件層；本頁只留一句結論。
- [[topics/ai-talent-flow]] — 人才流動與各公司戰力影響。
- [[topics/anthropic-government-policy]] — 出口管制、地理封鎖與其實效（含繞過與灰市）。
- [[topics/market-signals]] — 這些消息的市場面判讀；本頁只寫產品語言。
- [[entities/claude-code]]、[[entities/google-investment]]、[[entities/opencode]]、[[topics/enterprise-cost-management]] — 對應實體與成本主題。

## 時序

### 2026-09-23
- **Microsoft／GitHub**：Copilot code review 新增個人化設定選項、擴大適用方案並提供企業層級預設，全面 GA；詳見「對手雷達」與「雷達細節」更新（Blog/GitHub Copilot Changelog）
- **Google DeepMind**：官方部落格說明 Private AI Compute 架構如何在裝置端隱私標準下提供跨裝置持久記憶，屬技術說明非新產品發布，未併入「對手雷達」表（Blog/Google DeepMind Blog）
- **Microsoft／GitHub**：Copilot app 新增本地沙箱，限制未預期指令對檔案／網路／憑證的存取；詳見「對手雷達」與「雷達細節」更新（Blog/GitHub Copilot Changelog）
- **Microsoft／GitHub**：Copilot app 新增 OpenTelemetry 設定，透過企業管理設定開放；詳見「對手雷達」與「雷達細節」更新（Blog/GitHub Copilot Changelog）
- **Microsoft／GitHub**：Copilot for JetBrains 1.18.0 新增 AI 工具核准、agent 對話更多控制、組織層級共享技能與指令；詳見「對手雷達」與「雷達細節」更新（Blog/GitHub Copilot Changelog）
- **DeepSeek／Moonshot AI**：Gizmodo 報導中國當局調查兩家公司，起因是 Anthropic 先前指控其將部分請求轉發給 Claude 處理——若屬實顯示部分中國模型的實測能力可能部分借道 Claude，衝擊本頁既有「低價可用替代」判讀的可信度（推論，安全政策面詳見 [[topics/ai-agent-safety]]）（Google News/Gizmodo）

### 2026-09-21
- **OpenAI**：官方部落格發布 V7，讓 AI agent 具備「機構記憶」，把公司檔案轉為 agent context；GPT-6 Astra 於其最難圖查詢測試達 89% 準確率；詳見「對手雷達」與「雷達細節」OpenAI 列更新（Blog/OpenAI News）
- **xAI（透過 GitHub Copilot）**：Grok 4.7（基於 4.6，主打 agentic coding／複雜工作流）於 GitHub Copilot 上線；詳見「對手雷達」列更新（Blog/GitHub Copilot Changelog）

### 2026-09-19
- **Microsoft／GitHub**：Copilot code review 改版——版本演進呈現更清楚、自動解決建議更聰明、accept 時產生 commit 訊息；詳見「對手雷達」與「雷達細節」更新（Blog/GitHub Copilot Changelog）
- **Microsoft／GitHub**：官方公告 10/19 起停用部分 Copilot 模型，涵蓋 Chat、inline edits、ask／agent 模式與程式碼補全；詳見「雷達細節」（Blog/GitHub Copilot Changelog）
- **Microsoft／GitHub**：09-14 週報彙整——新增模型選擇選項、code review 更新、App 內 Sentry 整合，另有 agent 新功能（Blog/GitHub Copilot Changelog）
- **OpenAI**：官方發布《澳洲青少年安全藍圖》（Australian Youth Safety Blueprint），六大支柱路線圖，聚焦青少年 AI 使用安全，非產品或定價異動（Blog/OpenAI News）

### 2026-09-18
- **中國頭部模型（整體）**：報告稱其營收合計僅為 OpenAI 與 Anthropic 合計營收的 10%（南華早報引述報告）

### 2026-09-17
- **Microsoft／GitHub**：Copilot 新增功能採用儀表板（Impact Dashboard）與 agentic CLI 用量指標 API（涵蓋 skills、custom agents、MCP、slash commands、plugins）；詳見「對手雷達」列與「雷達細節」更新（Blog/GitHub Copilot Changelog）
- **Microsoft／GitHub**：Copilot 預算增加請求正式開放（GA），額度用盡後可申請提高預算而非被完全鎖住；詳見「對手雷達」列更新（Blog/GitHub Copilot Changelog）
- **OpenAI**：官方部落格發布「模型不對齊回報框架」，含 6 份異常模型行為報告，非產品或定價異動（Blog/OpenAI News）

### 2026-09-16
- **Google（Gemini）**：DeepMind 官方部落格發布 Gemini 3.8 Live 與 3.8 Live Extended Thinking，主打語音 agent、對話智慧與近即時多步推理；詳見「對手雷達」列更新（Blog/Google DeepMind Blog）

### 2026-09-15
- **Microsoft／GitHub**：Copilot auto model selection 新增效率／平衡／智慧三檔，讓使用者自訂成本與品質取捨；詳見「對手雷達」列更新（Blog/GitHub Copilot Changelog）
- **Meta（Meta One）**：官方發布新訂閱服務 Meta One，整合更多功能與 AI 能力，定位為一般消費訂閱而非編碼工具，與 Muse Code 為不同產品線（Blog/Meta Newsroom）

### 2026-09-13
- **OpenAI（透過 Perplexity 案例）**：Perplexity 用 GPT-6 Astra 自主寫通訊、改軟體、監控正式環境，人工複查頻率大減；詳見「對手雷達」與「雷達細節」OpenAI 列更新（Blog/OpenAI News）

### 2026-09-12
- **Google（Gemini）**：HN 討論稱 Gemini 2.5 Pro／Flash 十月停用、尚無 GA 版 Pro 級後繼；長文件利基（千頁僅需 30 萬 tokens）Anthropic／OpenAI 均無同等方案，代價逾 10 倍 → 需要此利基的工程師暫無替代可轉。僅單一 HN 討論串（19 分），無官方公告佐證（Hacker News）

### 2026-09-08
- **Cognition**（Devin 開發商）：The Tech Buzz 報導完成新一輪募資，估值達 480 億美元，AI 編碼賽道戰力升級；僅標題可用，資金用途、投資人名單未見報導（Topic Watch）
- **Logitech**：推出可自訂快捷鍵的 MX Keypad，鎖定開發者作為多應用 AI 控制中心，廠商自宣性質，無 Claude 對比（Topic Watch）

### 2026-09-07
- **xAI（Grok 4.5）**：官方定價 $2/$6 per Mtok，宣稱優於 GPT-5 與 Claude；詳見「對手雷達」與「競品定價對照」新增列（Google News/shattered.io）

### 2026-09-05
- **OpenAI**：Google News/Pasquale Pillitteri 報導稱 GPT-6 Astra 全面上線 Pro、Enterprise、API，副標提及「Anthropic 重置 Claude 用量限制」，原文全文未能取得（Google News/Pasquale Pillitteri）

### 2026-09-04
- **Cursor**：斷供傳聞理由指向控制權變更（Reddit/r/artificial · 週熱門）

### 2026-09-01
- **Meta**：另一篇報導聚焦其「20x」折扣層對比 Claude Code 加購方案（Google News/The New Stack；Google News/Intelligent Living）

### 2026-08-31
- **DeepSeek**：36Kr 報導中國市場出現以 Harness 為核心的免費替代方案討論，質疑付費編碼 agent 訂閱是否仍值得（Google News/36Kr）
- **Google**：CNBC 以影音再報「低價 AI 方案劍指 Anthropic 與 Microsoft」，未見新增方案名稱或費率（Google News/CNBC）

### 2026-08-29
- **騰訊**：Simon Willison 轉引騰訊發布開放權重模型 Hy4 Preview，約 770B 參數、不含視覺能力（Blog/Simon Willison）

### 2026-08-27
- **Google**：CNBC 報導 Google 推出低價 AI 方案，對 Anthropic 與 Microsoft 的企業客戶形成價格壓力，無具體費率（Google News/CNBC）

### 2026-08-26
- **Claude Code（生態相容性）**：36Kr 稱 Claude Code 拒採 AGENTS.md 業界標準，官方回應引發開發者不滿，僅標題可用；社群反應見 [[topics/community-tech-discussions]]（Google News/36Kr）
- **Google**：Business Insider 報導 Google 加入法律 AI 賽道，與 Anthropic、OpenAI 競爭；Anthropic 側佈局見 [[topics/anthropic-business]]（Google News/Business Insider）
- **AgentConnect**：24-7 Press Release Newswire 新聞稿宣傳其為開源多代理替代方案、對標 Claude Tag，非獨立媒體報導（Google News/24-7 Press Release Newswire）
- **Slack Code**：International Business Times 報導 Salesforce 官方以自身名義確認推出 Slack Code，整合 Claude 與 ChatGPT（Google News/International Business Times）

### 2026-08-24
- **一般消費者端價格敏感度**：Financial Times 報導 Anthropic 旗艦模型在一般消費者市場不敵較低價競品，dev.to 與 Simon Willison 同期轉引，未見流失規模數字（dev.to；Blog/Simon Willison）

### 2026-08-23
- **OpenAI**：inc.com 稱 OpenAI 拓展企業用戶速度已超越 Anthropic，主張此比估值更能反映競爭力，無量化數字；公司層級的採用率數字與資料日期見 [[topics/anthropic-business]]「現在的數字」（Google News/inc.com）
- **Inherent**：TechCrunch 報導 DeepMind 校友創立的 Inherent 自宣其 AI「隊友」在複現研究任務上超越 Anthropic 與 OpenAI，未經第三方驗證（Google News/TechCrunch）
- **灰市轉售**：the-decoder.com 報導中國以遠低於官方定價轉售 Claude API token 額度，管制實效面見 [[topics/anthropic-government-policy]]（Google News/the-decoder.com）

### 2026-08-22
- **OpenAI**：36Kr 發表「Codex 是否開始反擊 Claude Code？」，與同日 HN 高分貼文呼應（Google News/36Kr）

### 2026-08-21
- **廠商鎖定成本**：Startup Fortune 分析 vendor-locked 編碼 agent 如何在未察覺下推升企業工程成本，無量化數字（Topic Watch）
- **Slack Code**：VentureBeat 稱 Slack 要把 AI coding 從終端機拖進群組聊天（Google News/VentureBeat）

### 2026-08-20
- **OpenAI**：The Register 報導「零資料保留」承諾正面搶攻 Anthropic 企業客戶；TechCrunch 另引新數據稱 OpenAI 正追近 Anthropic 企業用戶市場（Google News/The Register；Google News/TechCrunch）
- **Slack Code**：The Next Web 報導 Slack Code 讓 Claude 與 ChatGPT 進入同一頻道協作（Google News/The Next Web）

### 2026-08-19
- **OpenAI**：TechCrunch、WSJ 報導 OpenAI 推出新客戶資料隱私承諾，兩家均解讀為針對 Anthropic 隱私訴求的競爭回應（Google News/TechCrunch；WSJ）
- **新創定價擠壓**：Startup Fortune 分析建構於底層模型 API 之上的新創在成本結構上遭遇的擠壓，僅標題可用（Google News/Startup Fortune）

### 2026-08-17
- **GitHub**：Mshale 報導 Copilot 推出新計費模式，終結先前的「無限量」編碼方案，價格級距與生效時程未見（Google News/Mshale）
- **Cursor**：VentureBeat 報導 Cursor 推出程式碼託管平台 Origin，藉 GitHub 中斷事件切入市場空隙（Google News/VentureBeat）
- **Zhipu Z.AI**：The Register 稱 Zhipu 新模型抓 bug 能力優於 Anthropic 與 OpenAI，無方法論與分數（Google News/The Register）

### 2026-08-15
- **Zhipu Z.AI**：VentureBeat 報導 GLM-5.3 發布主打資安能力，並稱已在 Cursor 找到一個「嚴重漏洞」（Google News/VentureBeat）

### 2026-08-14
- **Zhipu Z.AI**：Bloomberg 報導 Z.ai 推出新程式碼生成模型，明確點名 Anthropic、OpenAI 為競爭對手（Google News/Bloomberg.com）
- **DeepSeek**：VentureBeat 報導開源工具正式定名 Harness、以 Claude Code 直接競品定位問世，同步上線 API 定價較高的 V4-Pro（Google News/VentureBeat）
- **中美定價戰**：FT 稱 OpenAI 與 Anthropic 因中國對手崛起涉入定價戰；The Information 引研究稱 Anthropic 在特定情境可能更便宜，均無數字（Google News/Financial Times；Google News/The Information）

### 2026-08-13
- **DeepSeek**：TradingView、Bloomberg 報導 DeepSeek 公開組建團隊挑戰 Claude Code；KuCoin 與 Simon Willison 報導 V4 Pro 經 OpenRouter 以 API 上線，聲稱逼近 Claude 3 Opus、成本大幅降低（Google News；Blog/Simon Willison）
- ❓ **待查證**（標 2026-08-13｜查 Grok、SpaceX｜複 2026-09-27｜訊 2026-09-07）｜**xAI/Grok 新版發布，加壓 Anthropic 與 OpenAI**：Barron's 僅標題可用，能力提升內容仍未見（Google News/Barron's）
- 後續（依 09-07 日報）：版本號為 **Grok 4.5**，shattered.io 稱定價每百萬 token 輸入 2 美元／輸出 6 美元、優於 GPT-5 與 Claude；該說法僅見媒體標題，xAI 官方頁面未查
- **訊 2026-09-07**：Grok 4.5 官方定價 $2/$6 per Mtok，宣稱優於 GPT-5 與 Claude（shattered.io，單一來源），為此前訊號補上版本號與定價，詳見「競品定價對照」與「對手雷達」新增列。

### 2026-08-11
- **Meta**：CNBC 與 Simon Willison 報導 Meta 宣布開源其最強模型 Muse Glimmer，戰線從產品層擴大至模型層權重（Google News/CNBC；Blog/Simon Willison）

### 2026-08-10
- **Microsoft**：Stocktwits 轉引 SemiAnalysis 討論 Microsoft 能否「Out-AI」OpenAI 與 Anthropic，估算每 GW 推理商機達千億美元（**該機構自家模型的估算，非財報數字**；方法論見 [[topics/anthropic-business]]）（Google News/Stocktwits）

### 2026-08-07
- **Meta**：WSJ 報導 Meta 發布程式碼撰寫 agent「Muse Code」，明確對標 OpenAI 與 Anthropic（Google News/WSJ）

### 2026-08-06
- **Claude Code 成本**：the-decoder.com 稱 Claude Code 是最快的 agent 框架但成本近最便宜對手三倍，已查證數字見「硬答案」（Google News/the-decoder.com）

### 2026-08-05
- **Meta**：CNET、Basic Tutorials、Simon Willison 同日報導 Meta 官方發布 Muse Code 與 Muse Spark 1.2，明確對標 Claude Code 與 Codex（Google News；Blog/Simon Willison）

### 2026-08-04
- **Alibaba**：Decrypt 報導阿里巴巴免費開放「最強」AI 模型，宣稱追平 Claude 與 ChatGPT，未指明模型名稱（Google News/Decrypt）

### 2026-08-03
- **Kiro（AWS）**：tech-insider.org 發表 Kiro vs Claude Code 比較文，並列 80.8% SWE-bench 與 $200 費用上限兩項數字（Google News/tech-insider.org）

### 2026-08-02
- **OpenCode**：tech-insider.org 比較 OpenCode 與 Claude Code 的下載量與定價（Free vs $20，稱 5.4 倍），統計方法未揭露；完整脈絡見 [[entities/opencode]]（Google News/tech-insider.org）

### 2026-08-01
- **Supabase Evals**：MarkTechPost 報導 Supabase 推出開源評測套件，以真實任務對 Claude Code、Codex、OpenCode 評分（Google News/MarkTechPost）
- **OpenAI**：quasa.io 彙整已公開的程式碼測試結果比較 Claude Code 與 Codex，數字見「查證快照」（Google News/quasa.io）

### 2026-07-30
- **OpenAI**：官方公告 GPT-5.6 降價「Advancing the price-performance frontier」，Luna 降 80%、Terra 降 20%、Sol 提速 2.5 倍（Blog/Simon Willison；[OpenAI 官方](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/)）

### 2026-07-29
- **OpenAI**：The Information 稱 Codex 與開源模型討論度上升，但 Claude Code 採用黏著度仍領先，無量化數字（Google News/The Information）

### 2026-07-27
- **Moonshot AI**：Tom's Hardware 與 Simon Willison 報導 Kimi K3 權重正式開源，宣稱運算成本僅前沿模型 2–3 分之一（Google News；Blog/Simon Willison）
- **產業聯盟**：The Verge 報導 Nvidia、Microsoft 發起開放 AI 安全聯盟，OpenAI、Google、Anthropic 均未列名（Google News/The Verge）

### 2026-07-26
- **開源立場對立**：Benzinga 報導白宮 AI 政策顧問 David Sacks 稱 Anthropic 的開源立場「將把一把匕首刺進美國開源生態系的心臟」（Google News/Benzinga）

### 2026-07-25
- **OpenAI**：SitePoint 發表「Codex 5.3 生產環境工作流——何時該選它而非 Claude 做複雜重構」，無量化比較（Google News/SitePoint）

### 2026-07-22
- **Cline**：tech-insider.org 比較 Cline、Claude Code 與 Copilot 定價（Free vs $20 vs $10）（Google News/tech-insider.org）
- **中國 agent**：SCMP 報導某中國 AI agent 在自主研究任務上超越 Claude Code，未具名廠商與方法（Google News/South China Morning Post）
- **Alibaba**：TipRanks 報導 Claude 曾自稱是阿里巴巴 Qwen AI，引發「蒸餾雙標」批評；蒸餾指控的法律戰見 [[topics/anthropic-government-policy]]（Google News/TipRanks）

### 2026-07-21
- **Moonshot AI／Alibaba**：Emerging Trajectories（HN 341 分）分析 Kimi K3 與 Qwen 3.8 逼近 Fable 5，直言對 Anthropic 產品差異化構成重大威脅；The New Stack 實測顯示 Kimi K3 效果與 Fable 5 相當、成本三分之一、速度慢 4 倍（Hacker News；The New Stack）

### 2026-07-20
- **Alibaba**：qz.com、WSJ、SCMP 同步報導 Qwen3.8 預覽，宣稱能力僅次於 Anthropic Fable 5；thestreet.com 稱此標誌 AI 編程競爭態勢轉變（Google News）
- **Moonshot AI**：r/LocalLLaMA 週熱門貼文稱 Kimi K3 在 Text Arena 與 arena.ai 勝過 Claude Fable，與官方 07-18 自陳方向相反，無方法論（Reddit）
- **Thinking Machines**：r/LocalLLaMA 報導其發表首款開源權重模型 Inkling（Reddit）
- **開源陣營節奏**：r/LocalLLaMA 彙整近期開源模型發布時程（Kimi K3、Deepseek V4、Liquid、Mistral、GLM 5.5）（Reddit）

### 2026-07-19
- **xAI**：The New Stack 報導 Musk 開源 Grok Build 對抗 Anthropic，標題並稱 Anthropic 每月支付對方 12.5 億美元，付款對象與用途原文未載，不可逕自推論（Google News/The New Stack）
- **Thinking Machines**：Fast Company 稱該新創在「智識調性」上對 Anthropic 構成競爭（Google News/Fast Company）
- **區域市場**：KED Global 稱企業需求帶動下 Claude 有望在南韓生成式 AI 市場領先，無市佔數字（Google News/KED Global）
- **競品陣營表態**：The Motley Fool 再報 Musk 稱先前低估 Anthropic 實力，與 07-13 報導幾乎一致（Google News/The Motley Fool）

### 2026-07-18
- **Moonshot AI**：Simon Willison 引述官方公告確認 Kimi K3 為 2.8 兆參數、Kimi Delta Attention 架構、100 萬 token context，官方自陳整體仍落後 Fable 5 與 GPT-5.6 Sol（Blog/Simon Willison）
- **媒體擴散**：BBC、Forbes、The Globe and Mail 同步報導 Kimi K3 能力逼近 Claude／ChatGPT（Google News）
- **總體分析**：WSJ 分析 AI 更廣泛普及對中國有利、對 OpenAI 與 Anthropic 未必是好消息（Google News/WSJ）
- **蒸餾指控**：The Times of India 報導 Anthropic 與 OpenAI 指控多家中國 AI 公司蒸餾，投資人 Chamath Palihapitiy 加入評論（Google News/The Times of India）

### 2026-07-17
- **Moonshot AI**：CNBC、TechCrunch、FT 同步報導 Kimi K3 正式發布，官方稱「最強模型」，TechCrunch 分析後續版本有望逼近 Opus 4.8（Google News；CNBC）
- **Microsoft**：CNBC 報導 Nadella 公開批評 Anthropic 的 Fable「受編輯層面控制」（Google News/CNBC）

### 2026-07-16
- **Moonshot AI**：Financial Times 報導 Moonshot 即將發布挑戰 Anthropic 領先地位的新模型（Google News/Financial Times）

### 2026-07-15
- **Microsoft**：Yahoo Finance 報導 Microsoft 據稱訓練業務團隊向客戶淡化 OpenAI 與 Anthropic 優勢；企業採購面見 [[topics/enterprise-tool-tracker]]（Google News/Yahoo Finance）
- **OpenAI**：HackerNoon 發表 Claude Code vs Codex vs OpenCode 的全端工程師比較文，無公開分數（Google News/HackerNoon）
- **Alibaba**：Technology Org 解讀 Claude Code 內部邏輯設計，稱其凸顯 Anthropic 與阿里巴巴的競爭關係（Google News/Technology Org）

### 2026-07-14
- **競品陣營表態**：Proactive 解讀 Musk 稱 Anthropic 為「AI 領域明確領先者」的發言意涵，無新引言（Google News/Proactive）

### 2026-07-13
- **Cursor**：TweakTown 報導 Cursor 對標 Claude Cowork 的 AI agent 確認代號「Sand」（[TweakTown](https://www.tweaktown.com/news/112601/cursor-builds-ai-agent-sand-to-rival-anthropics-claude-cowork/index.html)）
- **Microsoft**：Business Insider 報導 Nadella 對 Anthropic 等廠商的模型蒸餾做法提出隱晦批評（Business Insider）
- **TCS**：The Times of India 報導 TCS 執行長宣布組建「前線部署工程師」團隊與 OpenAI、Anthropic、Amazon、Microsoft 競爭；合作面見 [[topics/anthropic-business]]（The Times of India）
- **競品陣營表態**：Yahoo Finance 兩來源報導 Musk 稱先前對 Anthropic 的看法「明顯錯誤」（Yahoo Finance）

### 2026-07-10
- **pi-coding-agent**：Databricks 官方部落格證實 GLM 5.2 與 Opus 4.8 品質統計持平但成本 $1.28 vs $1.94／任務（省約 34%）；Pi harness 在 Opus 4.8 high 下便宜約 2.08 倍，主因 context 傳遞量約 1/3（[Databricks](https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase)）

### 2026-07-09
- **OpenAI**：Reuters、ZDNET 報導 OpenAI 發表「super app」ChatGPT Work 與 GPT-5.6，明確訴求在價格、速度、生產力超越 Anthropic（Reuters；ZDNET）
- **Cursor**：The Information 報導 Cursor 正開發 AI agent 直接對標 Claude Cowork（The Information）
- **競品陣營表態**：Business Insider、Yahoo Finance 報導 Musk 稱 Anthropic 為業界「領導者」，承認先前判斷有誤（Business Insider）
- **Meta**：CNBC 報導 Meta 跨入 AI 程式輔助工具市場追趕 Anthropic 與 OpenAI（CNBC）

### 2026-07-08
- **Microsoft**：SiliconANGLE、Bloomberg 兩獨立來源報導 Microsoft 正以自研模型取代部分產品中的 OpenAI 與 Anthropic 模型以降低成本，官方無回應（[SiliconANGLE](https://siliconangle.com/2026/07/07/microsoft-reportedly-ditching-openais-anthropics-ai-models-favor-cut-costs/)；[Bloomberg](https://www.bloomberg.com/news/articles/2026-07-07/microsoft-replaces-openai-anthropic-with-own-ai-in-some-apps)）
- **Perplexity**：Business Insider 報導 Perplexity 低調開發 AI 編碼工具，對打 Cursor 與 Claude Code（[Business Insider](https://www.businessinsider.com/perplexity-building-ai-coding-tool-take-on-cursor-and-openai-2026-7)）
- **總體分析**：TechCrunch 探討開源 AI 崛起為何目前尚未衝擊 Anthropic（[TechCrunch](https://techcrunch.com/2026/07/07/why-the-rise-of-open-source-ai-isnt-hurting-anthropic-yet/)）

### 2026-07-07
- **中國模型整體**：CNBC 報導在 OpenAI、Anthropic 成本上升下，中國本土模型在美企採用率上升（[CNBC](https://www.cnbc.com/2026/07/07/chinese-ai-models-costs-us-openai-anthropic.html)）
- **DeepSeek**：finance.biggo.com 報導 DeepSeek 生態推出開源 agent 工具「Deep Code」對標 Claude Code（finance.biggo.com）

### 2026-07-06
- **Zhipu Z.AI**：Techzine Global 報導 Z.ai 推出免費 ZCode，直接對標 Cursor 與 Claude Code（[Techzine Global](https://www.techzine.eu/news/devops/142702/z-ai-takes-on-cursor-and-claude-code-with-free-zcode/)）
- **Base 44**：Business Insider 實測 Base 44 新模型 base-1 與 Anthropic 模型的建站速度（[Business Insider](https://www.businessinsider.com/base44-first-llm-base-1-ai-coded-website-comparison-anthropic-2026-7)）

### 2026-07-02
- **Palantir**：HN 討論串（16 分）記錄 Palantir CEO Alex Karp 公開批評 Anthropic 與 OpenAI「竊取客戶 IP、token 價值偏低」；分析師同日調升其評等，背景涉及國防／企業市場競爭（Hacker News；Investor's Business Daily）

---

#### 2026-06（時段總結）

- **亞洲競品同時湧現**：中國 360 發布 Tulongfeng（網路安全 AI）、日本 Sakana AI 發布 Fugu，均宣稱對標 Mythos／Fable 5（06-28，TechCrunch HN 256 分）；WSJ 同步稱中國已在網路安全 AI 追平 Anthropic。
- **定價邏輯首度被打破**：DeepSeek V4 Flash（開源，成本較 Claude API 降低逾 100 倍）動搖「以較高 API 定價補貼自家 agent 服務」的前提，Microsoft 等已切換執行層（06-26）。
- **最省錢 > 最強模型的具名案例**：Lindy CEO 宣告 100% 流量自 Claude 切至 DeepSeek，每月省下數百萬美元（06-29，CNBC）——高吞吐 API 客戶的價格敏感度自此可量化。
- **管制空窗成為追趕加速器**：Zhipu Z.AI 趁出口管制與法律審查期快速縮小差距，走開源路線繞開管制（06-27，CNBC）。
- **法律戰開場**：Anthropic 正式指控阿里巴巴以約 25,000 個假帳號、2,880 萬次對話進行蒸餾攻擊，多家媒體同步報導（06-25，HN 605 分）；後續法律戰見 [[topics/anthropic-government-policy]]。
- **管制實效遭第一手推翻**：Wired 揭露中國用戶長期以 VPN 等手段繞過地理限制（06-28）；該線索的完整脈絡見 [[topics/anthropic-government-policy]]。
- **格局重塑**：SpaceX 以 600 億美元完成收購 Cursor（06-19 確認），Cursor 的 Claude 依賴度與生態歸屬自此進入觀察期。
- 人才流動對競爭格局的影響（誰流失、誰承接、戰力意涵）詳見 [[topics/ai-talent-flow]]。

原始條目見 [[topics/competitor-landscape-archive#2026-06]]

---

#### 2026-05（封存總結）

- **Microsoft 退出是當月主線**：去年 12 月起向數千名員工開放的 Claude Code 授權因成本陸續取消、改推 GitHub Copilot CLI（05-15 首報；The Verge 05-22 報導 HN 493 分、05-23 續報 330 分）；dev.to 內部揭露記為「開發者愛它，財務殺了它」（05-19）。
- **企業採用同時創高**：Ramp AI Index 顯示 Anthropic 企業採用率首次超越 OpenAI（34.4% vs 32.3%，05-15）；Business Insider 稱新創圈 Claude Code 已勝出、Cursor 消退（05-23）——大企業因成本退出、新創因效果採用的分層自此成形。
- **競品整棧化**：DeepSeek 宣告要做「模型到開發工具」全棧並招募 Agent Harness 工程師（05-21～05-22）；Qwen3.7-Max 宣稱支援 Claude Code harness、可自主運行 35 小時（05-22）；Codex 下載量首度超越 Claude Code（8,610 萬次 +1,397% vs 720 萬次 −38%，05-05）。
- **成本分流工具化**：vibe-skill 以 Claude 規劃＋Mistral 執行，10 天省 57M tokens、成本降逾九成（05-21）；6/15 programmatic 用量改按 API 費率加速轉換（05-14，見 [[entities/pricing]]）；OpenCode 達 157,000 名開發者（05-12）。
- **整合面擴張**：UiPath、Signadot、Adobe Lightroom Linux 移植（05-12～05-17）；GitHub Copilot 新應用首次以產品名直接對標 Claude Code（05-16）。

原始條目見 [[topics/competitor-landscape-archive#2026-05]]

---

#### 2026-04（封存總結）

- 早期格局以「Claude Code vs Codex 誰更好」為軸：HN「Is Anybody Using Codex?」認為 Claude Code 討論量遠超 Codex（04-30，此判斷已由 05-05 下載量數據取代）；大型 Python monolith 實測作者偏好 Codex（04-29）；XDA 四工具橫向評測（04-28）。
- 採用面：哈佛 FAS 以 Claude 取代 ChatGPT Edu（04-28）、GameMaker 整合（04-30）。
- 競爭訊號：Sergey Brin 親自主導 Google 版 Claude Code 競品、「投資者即競爭者」引發討論（04-25～26）；Anthropic CPO Mike Krieger 辭去 Figma 董事會（04-24）。

原始條目見 [[topics/competitor-landscape-archive#2026-04]]
