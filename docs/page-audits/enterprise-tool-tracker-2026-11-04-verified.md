# 主編官方查證 — 第 25 波 topics/enterprise-tool-tracker（2026-11-04）

查證工具：WebFetch anthropic.com/news（官方一手索引與個別公告）、WebSearch 多家交叉（二手，標明）。行號為 `wiki/topics/enterprise-tool-tracker.md` 2026-11-04 原檔（366 行）。

## 一、頁面數字與狀態對官方

| # | 頁面句（行號） | 一手／交叉 | 判定 |
|---|---|---|---|
| 1 | L48、L99 Barclays「擴大導入 Claude Code 全行，目標 2026 年底開發者採用率 50%、2027 年擴及多數軟體工程師」（確認日 10-01） | anthropic.com/news「Barclays scales Claude to upgrade operations and improve client experience」（2026-10-01）；多家引該稿：50% 為**預期**而非已達成；另有 Global Markets 郵件分流約 12 萬封／日、1.6 萬名員工用於知識檢索 | 一致；可補「預期，不是已達成」與兩個官方量化數字（目前表上只有目標） |
| 2 | L96 Accenture「Anthropic『內嵌評估者』夥伴」 | anthropic.com/news「Partnering with Accenture on embedded evaluation」**2026-09-18**：雙方各預期「at least $1 billion … over the next five years」、「Anthropic will fund Accenture's work directly」 | 一致；日期是 09-18（market-signals 子頁寫 09-19，非本頁事） |
| 3 | 官方 10-02「Anthropic invests $100 million to train 10,000 engineers」具名 Accenture、Bain、CBA、Deloitte、McKinsey、Morgan Stanley、Novo Nordisk | 官方一手 | **本頁未收**：七家官方具名的人才培訓合作夥伴，其中 Bain、CBA、Deloitte、McKinsey、Morgan Stanley 本頁表上沒有——交設計者判是否屬「企業採用」範圍（是培訓夥伴，不一定是內部使用者） |
| 4 | L118 Microsoft ⚠️（10-05 內部支出砍逾三分之一）與 L138 Microsoft ❌「停用 Claude Code」（06-21）、L139 GitHub Copilot ✅ 三列並存 | 2025-11-18 Microsoft 承諾投資最高 $50 億、Anthropic 承諾 $300 億 Azure（多家，第 23 波 verified 第四節）；Microsoft Foundry 為官方通路（anthropic.com 05-06 頁提及） | 三列同一家、三種狀態，讀者要自己拼。摘要「6 家退出」把 Microsoft 算退出，但它同時是投資人與通路——建議把「內部工程師使用」與「通路／投資」分開寫一句，事實的家在 `anthropic-partnerships-compute` 三大雲表 |
| 5 | L114 Cognizant「官方公告擴大合作…Global Premier Partner」（07-28） | 官方新聞索引 06–11 月未見 Cognizant 專文（本次只抓到索引頁） | 🔎 未能在官方索引確認；維持原標，交記者補一手連結或改等級 |
| 6 | L39 摘要「追蹤 51 家」與 L83 計數口徑 | 本頁自算 | 設計者用腳本重數表列（同一家多列：Microsoft 3 列、Goldman 2 列、JPMorgan 2 列） |

## 二、考題的官方錨句

- **Q1 誰在用、規模多大**：官方一手可證的具名客戶／夥伴：Barclays（10-01，50% 目標、12 萬封／日、1.6 萬人）、Accenture（09-18，各 ≥$10 億／五年）、10-02 人才計畫七家、GSA（10-27，政府 40% 折扣）。其餘多為媒體。
- **Q2 工具之間怎麼選**：官方不談；本頁「工具競爭態勢」節是唯一答案來源，全為二手。
- **Q3 導入踩過的坑**：Accenture $29／月、JPMorgan $2,000／月上限皆媒體；官方方案門檻（Team 年繳 20 席起、Enterprise $20／席＋API 費率）住 `entities/pricing`。

## 三、給設計者三句

1. Microsoft 三列把「內部用不用」與「投資／通路」混在一起，摘要的「退出」計數跟著失真；寫一句分工並指向 partnerships-compute 三大雲表。
2. Barclays 補「預期而非已達成」與官方兩個量化數字；Accenture 日期 09-18。
3. 官方 10-02 人才計畫七家是否入表，先判本頁範圍是「內部使用」還是「所有具名合作」，範圍句寫進摘要首段。

來源：一手 anthropic.com/news（索引、Accenture 09-18 專文）；二手 [ChannelInsider](https://www.channelinsider.com/channel-business/news-barclays-anthropic-claude-banking-emea-uk/)、[FourWeekMBA](https://fourweekmba.com/ai-barclays-expects-half-its-developers-on-claude-code-by-2026/)、[IT Brief UK](https://itbrief.co.uk/story/barclays-expands-anthropic-s-claude-across-bank-operations)。
