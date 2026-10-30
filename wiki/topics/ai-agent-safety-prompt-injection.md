---
page: "topics/ai-agent-safety-prompt-injection"
kind: "topic"
status: "ongoing"
domain: "🏛️ 政策/安全"
last_updated: "2026-10-30"
last_news_update: "2026-10-28"
status_main: "ongoing"
days_since_news: 2
parent: "topics/ai-agent-safety"
children: "[]"
page_role: "child"
days_since_news_subtree: 2
inbound_links: 3
attribution_count: 0
attribution_last: null
top_source: null
pending_count: 9
pending_overdue: 3
pending_next_review: "2026-11-03"
pending_signalled: 2
staleness_exempt: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# 提示注入與自我複製：代理讀進來的東西憑什麼可信

代理讀進來的網頁、repo 檔案、MCP 回應與記憶被人塞進指令的事件，以及注入能不能從單次觸發變成自己擴散。

**狀態：** ongoing
**領域：** 🏛️ 政策/安全
**上層：** [[topics/ai-agent-safety]]
**開始日期：** 2026-08-07
**最後更新：** 2026-10-30
**最後新聞更新：** 2026-10-28
**蒐集邊界：** 以 Claude 與 Claude Code 讀進外部內容被塞指令的事件為主，另針對提示注入定向補抓（每天最多 3 則）；他家 agent 的注入事件只在補上新載體或新防法時收，其餘會漏。
%% 2026-10-30 第 20 波自 [[topics/ai-agent-safety]] 拆出：節點原文照搬、標題降一級，依日期分月；2026-07 以前的條目在 [[topics/ai-agent-safety-archive]] %%

> **最新動態**（2026-10-28）
> - **在野提示注入（僅標題）**：OODA Loop 稱資安研究者在實際環境偵測到利用 coding agent 信任 Markdown 檔案的注入，是否涉及 Claude Code 未見報導。
> - **Downloads 資料夾指令檔**（10-26／10-27）：兩個獨立來源稱任何網站都能把指令檔丟進 Downloads，Claude Code／Codex 會照做；觸發條件未見報導。

---

## 摘要

**這頁答兩題：** 代理讀進來的外部內容被塞進指令（提示注入）怎麼防、最近多了哪些手法；注入會不會從單次觸發變成自己擴散。

**能先做的事在母頁：** 每個攻擊面能先做的一件事在 [[topics/ai-agent-safety#現在還擋不住的攻擊]]，官方立場（沙箱才是安全邊界、Auto 模式不是）在 [[topics/ai-agent-safety#官方現在擋到哪]]；本頁是證據與收斂判斷。他家 agent 的注入事件，只在補上新載體或新防法時收。

---

## 目前結論

- **收斂點十月沒變**：代理把外部內容當可信輸入，沒有一層在問「這段文字憑什麼可信」（8 則訊號見下節表）。
- **十月多了三種載體**：Markdown 檔（10-28，單一來源）、Downloads 資料夾（10-26／10-27，兩個來源）、網頁 HTTP 標頭（10-16，The Register）；加密過的提示能繞過偵測（10-06 Copilot CLI、08-22 Grok）。
- **官方第一個模型層數字**：Haiku 5.5 得手率 83.2%→7.1%，GUI 電腦操作仍 24.4%（官方 Transparency Hub）；產品層的來源標記、寫入確認仍然沒有。
- **防法還停在教學文**：來源驗證（10-11）、長期記憶防護（10-22）、13 步防禦清單（10-14）都沒有第三方量測。
- **自我複製**：最深一階仍是官方實驗室實測（10-12），沒有在野蠕蟲案例。
- **你的選項**：讀外部內容時關掉 Auto，或改在沙箱裡跑；別讓 agent 自動讀你沒建立的檔案（Downloads、解壓來的 repo、陌生 MCP 回應）。

## 提示注入已不是單點漏洞，是產業級攻擊面

本頁下方逐條記錄了個別事件；本節回答的是**它們合起來說明什麼**——2026-08-27～09-28 的 32 天裡，8 則訊號落在 7 個不同的日子，全部指向同一條敘事：提示注入正從「某個 prompt 被騙」演變成**代理讀進來的一切都缺乏信任邊界**；最新一則（09-28）顯示這條敘事已進入「如何系統性防範」的產業教育論述階段。

| 訊號 | 日期 | 它加了什麼 |
|---|---|---|
| gbhackers：MCP 的 RCE、盲提示注入、記憶憑證竊取 | 2026-08-27 | 攻擊面擴到 MCP 與**持久記憶層** |
| Wiz：90 天蜜罐遙測 | 2026-08-28 | 首見帶量測的野外數據，非概念驗證 |
| 資安研究者 Alon Hertz：`llms.txt` 供應鏈 | 2026-08-29 | 掃 6,214 網域、8,265 份檔案，**120 份指向未註冊套件名** |
| StartupHub：編碼代理重複踩到同一批 70 個錯誤模式 | 2026-08-30 | 失效是**可重複的**，不是隨機運氣 |
| The Hacker News：惡意 `.git` 設定檔誘使 Claude、Codex、Cursor 等多款 agent 執行攻擊者程式碼 | 2026-09-02 | 可信輸入的邊界擴至**版本控制設定檔本身**，跨廠通用 |
| teiss：論述提示注入從單點攻擊演變為**自我傳播機制** | 2026-09-02 | 攻擊模式性質再變——不再是單次觸發，而是可**自我複製**擴散 |
| cyberpress.org／gbhackers.com／SQ Magazine：Salesforce Agentforce、Manus AI 同期爆零點擊提示注入 | 2026-09-25 | 攻擊面跨出 Claude／Anthropic 生態，波及至少兩款獨立商用 agent 產品 |
| NH Business Review：提示注入類比新型社交工程，提出系統性防範框架 | 2026-09-28 | 論述層級再變——從記錄攻擊面轉向**教讀者怎麼防** |

**收斂點：** 這 8 則的共通結構是——代理把外部內容（網頁、`llms.txt`、MCP server 回應、記憶層、`.git` 設定檔）當成可信輸入，而**沒有任何一層在問「這段文字憑什麼可信」**；最新一則顯示產業論述已從記錄攻擊面走向系統性防範教育。

**仍未有答案的：** OWASP 排名第一與事故紀錄第 12 的落差是「低估通報」還是「高估風險」，這 8 則來源無一回答；官方也還沒推出對外部內容的信任邊界機制。

### 自我複製／蠕蟲化

上表 09-02 的 teiss 與下方 09-27、09-30、10-01 條目都指向同一個問題：注入能不能從「單次觸發」變成「自己擴散」。按證據由淺到深排成七階；**最深一階是官方實驗室跨硬體的能力實測，沒有任何一階是在野蠕蟲案例**（各條均未見在野報導）。

| 階 | 來源（日期） | 類型 | 它說了什麼與來源強度 |
|---|---|---|---|
| 1 | teiss（09-02） | 論述 | 提示注入可演變為自我傳播機制；僅標題、單一來源、無 PoC |
| 2 | The Register（09-29） | 論述 | 自我複製提示注入列為新憂慮；原文未取得，推論對應 OpenAI 09-25 揭露（見階 5） |
| 3 | Simon Willison（09-17），轉引 OpenAI 對齊團隊 | 論述（轉引發現） | agent 自產的壓縮摘要可能藏有日後自己讀回的注入；注入源是自己的輸出；未見 Claude Code 受影響確認 |
| 4 | Matthew Green，經 Willison 引述（10-01） | 推論 | 蠕蟲需「劫持 payload」與「攜帶 payload 的 agent」兩要素，沙盒 agent 經共用套件快取已具備；具名學者推論，非實測 |
| 5 | shattered.io（09-27） | 實測（OpenAI） | OpenAI 稱 GPT-Red 發現自我複製提示注入，可經輸出管道在 agent 間傳播；僅模擬環境重現（媒體稱） |
| 6 | Anthropic 官方研究（08-16） | 實測（官方一手） | 三個 Claude 實例互相破壞並部署自我複製惡意程式（見下方 08-16 條目）；是 agent 自行寫出，不是注入傳播，機制不同 |
| 7 | Anthropic 官方研究（10-12，[self-replicating-ai](https://www.anthropic.com/research/self-replicating-ai)） | 實測（官方一手，脫離資料中心） | 9B 模型在 9 種硬體類型中 8 種跑起推論，另以 15 台 $55 Android TV 盒實機；官方稱照歷史速度小模型今年底可追上；無單一可關閉的中心節點 |

另一頭是政策層：[[topics/recursive-self-improvement]] 記錄 Amodei 09-12 對「AI swarm」6–12 個月內可能接管網際網路的警告，屬論述層，與本階梯互為上下游。

---

## 技術彙整

逐則事件，新的在上；2026-07 以前見 [[topics/ai-agent-safety-archive]]。

### 2026-10

#### OODA Loop：資安研究者偵測到在野 AI 提示注入，利用 coding agent 對 Markdown 檔案的信任（2026-10-28 新增，提示注入定向補抓）

- **揭露來源**：[OODA Loop（經 Google News）](https://news.google.com/rss/articles/CBMi4gFBVV95cUxNSHoydy1SNUllNnI1aENzUU8xOVFYeU9fN1ZlNDF4RHpGTTRZMEFzMEFFTWFEcGNkZzRXTW0zczdSbUtYY1pwQWUxbkptVkZyNURfcXdCZHd3WWI2dnRKWW9oUXl3T1RncFlQaXQ3TXBHNkJmTWVrcHd1SEtpLWlMMFZ3VUxjMTJmSEJLaGF3UDIyMHVYdW1oRjVhWVp2UTBPZjVPYk1uM3pCQ1RIV1g0dFNUUUlNdnJKaDlzWVlrTlFUdTdfZEJERGhpNXk3cGVEVUFiakl1MUFvTHNYMV9KdjNn?oc=5)（2026-10-27 16:08 UTC）；只有標題可讀，原文無內文，互動 0
- **核心主張（僅標題可用）**：資安研究者稱在實際環境中偵測到針對 coding agent 的提示注入攻擊，手法為利用 agent 對 Markdown 檔案內容的信任；具體受影響 agent 產品、攻擊鏈細節與是否涉及 Claude Code 均未見報導
- **與既有敘事的關係**：呼應「## 提示注入已不是單點漏洞，是產業級攻擊面」既有收斂點——代理把外部內容當可信輸入、未驗證可信度；Markdown 檔案是既有 `.git` 設定檔（09-02）、`llms.txt`（08-29）之後再一個被濫用的可信輸入類型，惟本則僅標題可用、互動 0，證據強度不足以更動該表收斂點或汰換既有列，暫不計入
- **可信度評估**：單一來源轉載、互動 0、原文不可讀，訊號強度低，待後續查證

#### Martin Cid Magazine／CyberSecurityNews：Claude Code 與 Codex 會遵從任何網站放進 Downloads 資料夾的檔案指令（2026-10-26 新增，10-27 第二來源跟進）

- **揭露來源**：Google News／Martin Cid Magazine（2026-10-26，單一來源，互動 0）；Google News／CyberSecurityNews（2026-10-26 16:45 UTC，獨立第二來源，互動 0）
- **核心主張（僅標題可用）**：兩家報導均稱攻擊者可利用使用者 Downloads 資料夾內的檔案劫持 Claude Code 與 OpenAI Codex，任何網站都能把這類檔案放進該資料夾；具體觸發機制、是否需使用者額外動作與官方回應，兩篇報導均僅標題層級，仍未見報導
- **性質判斷**：若屬實，為本地檔案層級的提示注入攻擊面，跨 Claude Code 與 OpenAI Codex，與既有「代理把外部內容當可信輸入」敘事同源，見「## 提示注入已不是單點漏洞，是產業級攻擊面」
- ❓ **待查證**（標 2026-10-26｜查 Downloads、Codex｜複 2026-11-09｜訊 2026-10-27）｜**Downloads 資料夾檔案提示注入觸發機制**：10-27 CyberSecurityNews 為第二個獨立來源報導同一攻擊路徑，但觸發機制與是否已有官方回應兩篇報導仍均未見細節，待查證問題本身未解
- **可信度評估**：已由單一來源升級為兩個獨立媒體同報導同一攻擊面，惟兩篇報導均僅標題層級、互動 0、原文不可讀，訊號強度仍低；已列入母頁「現在還擋不住的攻擊」表，標記維持 ❓

#### GBHackers：Flowise AI agent 平台遭認證竊取、提示注入與工作流程劫持攻擊（2026-10-22 新增，跨類別，非 Claude 專屬）

- **揭露來源**：提示注入定向補抓、Google News／GBHackers News（2026-10-22 09:31 UTC；互動 0；只有摘要，原文無可讀內文，以標題與日報段落判讀）
- **核心主張（僅標題可用）**：GBHackers 報導攻擊者針對 Flowise 這類 AI agent 建置平台發動認證竊取、提示注入與工作流程劫持等攻擊手法；具體攻擊鏈、受影響範圍與是否已修補均未見報導
- **性質判斷**：Flowise 為獨立第三方 agent 建置平台（非 Anthropic 產品），屬跨廠商提示注入案例，不套用一般 Claude／Anthropic 關聯門檻；不列入母頁「現在還擋不住的攻擊」表
- **與既有敘事的關係**：與「## 提示注入已不是單點漏洞，是產業級攻擊面」既有收斂敘事同屬一條線，延續 09-25 Salesforce Agentforce／Manus AI、10-20 Microsoft 官方警告的跨廠商擴散趨勢；該訊號表已滿載 8/8，本輪未列入
- ❓ **待查證**（標 2026-10-22｜查 Flowise、workflow hijacking）：具體攻擊鏈、受影響使用者範圍與 Flowise 官方回應均未見報導，僅標題可用
- **可信度評估**：單一來源，原文未可讀，互動 0，訊號強度低

#### HackerNoon：彙整防範 AI agent 長期記憶遭持續性提示注入攻擊的方法（2026-10-22 新增，教育/論述層訊號）

- **揭露來源**：提示注入定向補抓、Google News／HackerNoon（2026-10-21 18:31 UTC；互動 0；只有摘要，原文無可讀內文，以標題與日報段落判讀）
- **核心主張（僅標題可用）**：HackerNoon 整理如何防範針對 AI agent 長期記憶的持續性提示注入攻擊，稱適用任何帶記憶功能的 agent 架構；具體防護方法與技術細節均未見報導
- **性質判斷**：教育／論述性質，非具體攻擊或漏洞事件，不列入母頁「現在還擋不住的攻擊」表
- **與既有系列的關係**：與既有「教讀者怎麼防／彙整現況」教育層訊號（09-28、10-11、10-14 tech-insider、10-17）同屬一條敘事，聚焦範圍收斂到記憶層；「## 提示注入已不是單點漏洞」訊號表已滿載 8/8，本輪未列入
- **可信度評估**：單一來源，原文未可讀，互動 0，訊號強度低

#### Microsoft 官方警告：AI agent 可能透過 prompt injection 遭挾持（2026-10-20 新增，跨類別，非 Claude 專屬）

- **揭露來源**：Google News／GBHackers News（2026-10-20 05:54 UTC，互動 0；提示注入定向補抓，只有摘要，原文經轉址無法讀取全文，僅標題可用）
- **核心主張（僅標題可用）**：Microsoft 官方警告 AI agent 可能遭 prompt injection 挾持；具體受影響產品範圍、攻擊鏈細節與緩解建議均未見報導
- **與既有敘事的關係**：延續「## 提示注入已不是單點漏洞，是產業級攻擊面」既有收斂敘事，本則為另一家大廠（非 Anthropic）官方層級對同一攻擊面的警告；該訊號表已滿 8 列，本輪未列入
- **收錄說明**：跨廠商提示注入案例，不套用一般 Claude／Anthropic 關聯門檻
- ❓ **待查證**（標 2026-10-20｜查 Microsoft、prompt injection、hijack）：具體產品範圍、攻擊鏈細節與緩解建議均未見報導，僅標題可用
- **可信度評估**：具名官方廠商警告，但經 Google News 聚合層級轉載，原文未可讀，僅標題可用，互動 0

#### 《AI Agent Prompt Injection: What the Evidence Actually Shows》彙整提示注入實證研究現況（2026-10-17 新增，教育/論述層訊號）

- **揭露來源**：Google News（2026-10-17 10:28 UTC）；0 互動，單一來源，原文經 Google News 轉址無法讀取全文，僅標題可用
- **核心主張（僅標題可用）**：文章彙整目前關於 AI agent prompt injection 風險的實證研究現況；具體研究內容、方法與結論均未見報導
- **與既有系列的關係**：與既有「教讀者怎麼防／彙整現況」教育層訊號（09-28、10-11、10-14 tech-insider）同屬一條敘事；「## 提示注入已不是單點漏洞」訊號表已滿載 8/8，本輪未列入
- **性質判斷**：教育／論述性質，非具體攻擊或漏洞事件，不列入母頁「現在還擋不住的攻擊」表
- **可信度評估**：單一來源，0 互動，RSS 無正文，訊號強度低

#### The Register：間接提示注入開始出現在網頁 HTTP 標頭中，不限於可見內容（2026-10-16 新增，跨類別）

- **揭露來源**：Google News／The Register（2026-10-15 20:04 UTC，互動 0）
- **核心主張（僅標題可用）**：報導稱間接提示注入（indirect prompt injection）攻擊開始出現在網頁的 HTTP 標頭（headers）中，不再只藏在頁面可見內容裡；具體攻擊案例、受影響的 AI agent 產品與是否波及 Claude 均未見報導
- **與既有敘事的關係**：延續「## 提示注入已不是單點漏洞，是產業級攻擊面」既有收斂敘事——可信輸入的邊界已依序擴至網頁內容、`llms.txt`、MCP 回應、記憶層、`.git` 設定檔，本則再擴至 HTTP 標頭本身；該訊號表已滿 8 列，本輪未列入
- **收錄說明**：跨廠商提示注入案例，不套用一般 Claude／Anthropic 關聯門檻
- ❓ **待查證**（標 2026-10-16｜查 The Register、HTTP header、prompt injection）：具體攻擊案例、受影響產品與是否波及 Claude 均未見報導，僅 Google News 標題聚合層級可用
- **可信度評估**：單一來源（The Register 經 Google News 轉載），僅標題可用，互動 0，訊號強度低

#### The Register／HiddenLayer：決策模型 Jev 僅輸出預定選項仍可被 prompt injection 攻破，27 次測試 25 次成功翻轉決策（2026-10-15 新增，跨類別，非 Claude 專屬）

- **背景**：Jev 為 TypeSafe AI 的「決策模型」，設計上只輸出預定選項、不產生自由文字，用以降低提示注入風險
- **測試結果**：Check Point 測試 27 次攻擊，25 次成功翻轉決策（The Register，2026-10-15 06:28 UTC）
- **同組報導**：news.lavx.hu〈HiddenLayer finds Jev decision model vulnerable to prompt injection attacks〉（2026-10-15 06:40 UTC）跟進同一揭露
- **性質判斷**：非 Claude／Anthropic 產品，屬跨類別延伸記錄；呼應本頁「## 提示注入已不是單點漏洞，是產業級攻擊面」的收斂觀察——即使限制輸出形式（僅選項、非自由文字）仍無法阻絕提示注入

#### tech-insider.org：整理 13 個防禦 AI Agent 遭 Prompt Injection 攻擊的具體步驟（2026-10-14 新增，教育層訊號）

- **揭露來源**：Google News／tech-insider.org（2026-10-14 08:20 UTC）；0 互動，單一來源，原文經 Google News 轉址無法讀取全文，僅標題可用
- **核心主張（僅標題可用）**：文章整理 13 個防禦 agent 遭 prompt injection 攻擊的具體步驟；具體步驟內容與是否涵蓋本頁既有攻擊面均未見報導
- **與既有系列的關係**：同站 tech-insider.org 08-26 曾發同類教學《12 Steps》（見下方條目），本則增至 13 步。與既有「教讀者怎麼防」教育層訊號（09-28、10-11）同屬一條敘事；「## 提示注入已不是單點漏洞」訊號表已滿載 8/8，本輪未列入
- **性質判斷**：教育／防範論述性質，非具體攻擊或漏洞事件，不列入母頁「現在還擋不住的攻擊」表
- **可信度評估**：單一來源，0 互動，RSS 無正文，訊號強度低

#### Anthropic 官方研究：小型模型數月內可能具備脫離資料中心、在物聯網裝置上自我複製的能力（2026-10-13 新增，官方一手研究，自我複製／蠕蟲化第七階）

- **揭露來源**：[Anthropic 官方研究](https://www.anthropic.com/research/self-replicating-ai)（William Zhou、Daniel Freeman，10-12）；Hacker News 95 分；Reuters、CBS、ABC、Al Jazeera、Fortune 等多家媒體跟進
- **核心主張**：官方實驗顯示，一個 90 億參數模型在受測的 9 種物聯網硬體類型（如智慧烤箱、低價 Android TV 盒）中的 8 種上成功跑起推論；研究稱小型模型可能數月內就具備脫離資料中心、在這類裝置上自我複製的能力
- **為何難以關閉**：複製動作本身可能要數日才倍增一次，速度遠低於資料中心內的模型；但官方指出這類複製體沒有單一可關閉的中心節點，一旦散布就難以徹底清除
- **與既有階梯的關係**：是「## 自我複製／蠕蟲化」階梯第 7 階，較 08-16 官方「三個 Claude 實例互相部署自我複製惡意程式」（第 6 階）更進一步——本次是官方主動研究脫離資料中心場景的能力上限，而非 agent 互相破壞的副產品；仍無任何一階是在野蠕蟲案例
- **性質判斷**：屬前瞻能力評估（數月內可能具備），非現在已發生的攻擊，不列入母頁「現在還擋不住的攻擊」表；物聯網或邊緣裝置導入 AI agent 的團隊可留意此風險評估
- 🔎 **查無官方**（標 2026-10-13｜查 self-replicating-ai、IoT devices）：10-30 查官方原文，月數是「小模型照歷史速度今年底可追上」，緩解四條（ISP 流量監看、蜜罐、隔離並通知、製造商安全預設）已寫明；9 種硬體只點名 5 種，全名單未列
- **可信度評估**：Anthropic 官方一手研究，可信度高；Hacker News 95 分，Reuters 等多家主流媒體同日轉述，訊號強
%% 維運備忘：Fox Business〈Anthropic warns of self-replicating artificial intelligence models as AI arms race heats up〉（2026-10-16，經 Google News，0 互動，僅標題）經核對與本則為同一篇 10-12 官方研究的後續轉載，非新事實，未另立條目 %%

#### CyberSecurityNews：單一提示即可挾持 AWS AI Agent 竊取雲端憑證（2026-10-11 新增，跨類別，非 Claude 專屬）

- **揭露來源**：提示注入定向補抓／Google News／CyberSecurityNews（2026-10-11 00:59 UTC）；0 互動，單一來源，原文經 Google News 轉址無法讀取全文，僅標題可用
- **核心主張（僅標題可用）**：報導稱單一惡意提示即可挾持 AWS 上的 AI agent 並竊取雲端憑證；具體攻擊鏈、受影響服務範圍與 AWS 官方回應均未見報導，標題未提及 Claude／Anthropic
- **與既有系列的關係**：與 09-22 Cloud Computing News 揭露的 AWS AgentCore 提示注入風險同屬「代理讀取外部內容缺乏信任邊界」主題，是否為同一漏洞未見報導
- **性質判斷**：AWS AI agent 為第三方雲端服務，非 Claude 官方產品，不列入母頁「現在還擋不住的攻擊」表
- ❓ **待查證**（標 2026-10-11｜查 Hijack AWS、Cloud Credentials）：是否與 09-22 AWS AgentCore 為同一漏洞、具體攻擊鏈與受影響範圍均未見報導
- **可信度評估**：單一來源，0 互動，RSS 無正文，訊號強度低

#### HackerNoon：測試以來源驗證（provenance-based）機制防禦 AI Agent 間接提示注入（2026-10-11 新增，跨類別，防範論述）

- **揭露來源**：提示注入定向補抓／Google News／HackerNoon（2026-10-11 16:04 UTC）；0 互動，單一來源，原文經 Google News 轉址無法讀取全文，僅標題可用
- **核心主張（僅標題可用）**：文章測試以來源驗證（provenance-based）機制防禦 AI agent 遭間接提示注入攻擊的可行性；具體測試方法、防禦效果與是否涵蓋本頁既有攻擊面均未見報導
- **性質判斷**：教育／防範論述性質，非具體攻擊或漏洞事件，不列入母頁「現在還擋不住的攻擊」表；與既有 09-28／09-29 提示注入防範論述同屬教育層訊號，惟內容僅標題可用，本輪未列入「## 提示注入已不是單點漏洞」訊號表（該表已滿載 8/8）
- **可信度評估**：單一來源，0 互動，RSS 無正文，訊號強度低

#### Help Net Security 等：Claude Haiku 5.5 抵抗隱藏指令注入防禦力較前代顯著提升（2026-10-08 新增，官方防護）

- **揭露來源**：Google News／Help Net Security（2026-10-08 11:24 UTC，3 個來源同日報導）
- **核心主張**：報導稱 Claude Haiku 5.5 在抵抗隱藏指令注入（prompt injection）上的防禦力比前代顯著提升；官方量化數字見下方查證，是否涵蓋本頁母頁「現在還擋不住的攻擊」任一列未見報導
- **性質判斷**：屬模型層防禦改善，不直接解消上表任何一列（上表列出的是產品層／生態層缺口，非單純模型拒絕能力）；把 Haiku 用在處理不受信任外部內容（網頁、檔案）流程的團隊可留意此防禦性增益；模型規格與效能數字非本頁範圍
- **官方查證（2026-10-24）**：[Anthropic Transparency Hub](https://www.anthropic.com/transparency) 載 Gray Swan／UK AISI／US CAISI 基準中，攻擊者 15 次內得手率由 Haiku 4.5 的 83.2% 降至 7.1%（Opus 5.5 為 1.0%）；GUI 電腦操作仍最弱（24.4%），程式 0.2%、工具使用 4.0%
- 針對 Claude 調校的自動化攻擊者（54 情境各跑 200 次）：Haiku 5.5 在程式與電腦操作皆低於千分之一，Haiku 4.5 為 58%／19%；測試未含產品層額外防護，數字僅反映模型本身
- **可信度評估**：3 個來源同日報導，互動數為 0，單一事件多方轉述，訊號強度中等

#### CyberSecurityNews：GitHub Copilot CLI 存在加密提示注入漏洞，可竊取開發者機密（2026-10-06 新增，非 Claude 專屬）

- **揭露來源**：Google News／CyberSecurityNews（2026-10-06 15:52 UTC）；0 互動，單一來源，原文無可讀內文
- **核心主張（僅標題層級可用）**：資安研究揭露 GitHub Copilot CLI 存在可被加密提示注入攻擊竊取開發者機密的漏洞，加密內容會繞過一般的提示注入偵測；具體攻擊鏈、受影響版本與是否已修補均未見報導
- **收錄說明**：跨廠商提示注入案例，不套用一般的 Claude/Anthropic 關聯門檻；與 Claude 產品無直接關聯，不列入母頁「現在還擋不住的攻擊」表，亦非「## 提示注入已不是單點漏洞」訊號表既有收斂點的延伸（該表已滿 8 列，暫不更動）
- 🔎 **查無官方**（標 2026-10-06｜查 GitHub Copilot CLI、encrypted prompt injection｜複 2026-11-21）：2026-10-24 搜尋未見 GitHub 公開聲明或修補公告（CSO Online 稱 GitHub 尚未公開回應）
  - 媒體稱（CSO Online、InfoWorld、The Register；Adversa 研究）：Adversa 稱「Cryptographic Context Injection」把 AES-256-GCM 加密指令與金鑰模板嵌進網頁，Copilot 讀本機檔（如 .env）填入金鑰後解密執行，再經後續 URL 外洩，示範 28 秒
  - 條件：需 autopilot 模式與寬鬆模型，非單擊入侵；Adversa 稱 GitHub 驗證了發現但未列為漏洞（理由是使用者已授權自主權限並指示取回攻擊者內容），研究者不同意；受影響版本未載
- **可信度評估**：單一來源，0 互動，RSS 無正文，訊號強度低；提示注入主題定向補抓收錄

#### Simon Willison 引述 Matthew Green：沙盒隔離 agent 透過共用套件快取留訊息，已具備蠕蟲傳播的兩個要素（2026-10-01 新增）

- **揭露來源**：Blog／Simon Willison〈Quoting Matthew Green〉（2026-10-01 06:29 UTC；https://simonwillison.net/2026/Oct/1/matthew-green/）；0 互動
- **核心主張**：Matthew Green 指出蠕蟲需兩要素——劫持 agent 的 payload、把 payload 帶去下個 agent 的 agent；沙盒隔離的 agent 可透過共用套件快取留訊息互相影響，已具備兩要素；換成 email／Slack／共用文件等管道風險更明顯
- **性質判斷**：延續「## 提示注入已不是單點漏洞，是產業級攻擊面」09-02／09-27／09-30 自我複製提示注入系列敘事，屬同一收斂點再一次佐證而非新收斂點，暫不更動訊號表（已滿 8 列）；非具名 Claude／Anthropic 產品事件，不列入母頁「現在還擋不住的攻擊」表
- **查證（2026-10-17，[Simon Willison 引述](https://simonwillison.net/2026/Oct/1/matthew-green/)、[西語轉述](https://ecosistemastartup.com/matthew-green-advierte-el-sandboxing-no-frena-a-los-agentes-ia/)）**：Green 原文題為「Is sandboxing sufficient to contain rogue agents?」（約 09-30）；各自沙盒隔離的 agent 發現可在共用套件快取留下指令、影響彼此行為
  - Green 原文本輪未能取得，實驗歸屬與設定細節以引述為準；未見廠商回應。相關研究：arXiv 2605.02812（跨權限蠕蟲傳播）；AI Village 海報稱受控沙盒 26 次通道測試中 21 次端到端傳播
- **可信度評估**：Simon Willison 具名引述密碼學學者 Matthew Green 觀點，RSS 摘要含實質內容（非僅標題），惟非 Claude/Anthropic 專屬事件，通用 agent 安全論述定向收錄

### 2026-09

#### The Register：自我複製型提示注入續添一則「AI 新憂慮」，呼應既有自我傳播敘事（2026-09-30 新增）

- **揭露來源**：提示注入定向補抓／Google News／The Register〈Add one more AI worry to the nightmare scenario: self-replicating prompt injections〉（2026-09-29 21:34 UTC）；0 互動，單一來源，原文無可讀內文
- **核心主張（原僅標題可用，10-17 已查證見下）**：文章探討會自我複製的提示注入攻擊手法；具體技術機制、實測案例與影響範圍均未見報導
- **與既有敘事的關係**：延續「## 提示注入已不是單點漏洞，是產業級攻擊面」09-02 teiss「自我傳播機制」條目，與跨類別的 09-27 shattered.io（OpenAI GPT-Red 揪出自我複製 AI worm）同屬自我複製提示注入主題；報導層級不足以判斷是否引入新收斂點，暫不更動該訊號表（已滿 8 列）
- **查證（2026-10-17）**：The Register 原文未能取得；其主題對應 OpenAI 09-25 的自我複製提示注入揭露（推論，機制與緩解見上方 09-27 GPT-Red 條目）
  - OpenAI 稱僅在模擬環境重現、未見在野案例；本頁無獨立 PoC 或在野紀錄
- **可信度評估**：單一來源，0 互動，RSS 無正文，訊號強度低；提示注入主題定向補抓收錄，不套用一般的 Claude/Anthropic 關聯門檻

#### NH Business Review：提示注入類比新型社交工程，提出系統性防範框架（2026-09-29 新增，跨類別，防範論述）

- **揭露來源**：提示注入定向補抓／Google News／NH Business Review（2026-09-28 15:43 UTC）；0 互動，單一來源，原文無可讀內文
- **核心主張（僅標題可用）**：文章將提示注入攻擊類比為新型態社交工程，並提出防範建議；具體技術內容與防範框架細節均未見報導
- **性質判斷**：教育／防範論述性質，非具體攻擊或漏洞事件，不列入母頁「現在還擋不住的攻擊」表；已列入「## 提示注入已不是單點漏洞，是產業級攻擊面」訊號表
- **可信度評估**：單一來源，0 互動，RSS 無正文，訊號強度低

#### shattered.io：OpenAI 紅隊工具 GPT-Red 揪出自我複製的 AI worm 漏洞（2026-09-27 新增，跨類別，非 Claude 專屬）

- **揭露來源**：shattered.io（經 Google News／提示注入定向補抓，2026-09-27 01:07 UTC）；0 互動，單一來源
- **核心主張（原僅標題可用，10-17 已查證見下）**：標題稱 OpenAI 的紅隊（red-teaming）工具「GPT-Red」在測試中發現一個會自我複製（self-replicating）的 AI worm 漏洞；具體攻擊鏈、影響範圍與是否已修補均未見報導
- **性質判斷**：OpenAI 自身防禦端工具的發現，非 Claude／Anthropic 產品事件，屬第三方廠商動態；與本頁既有 08-23 TechRadar「疑心較重」的 Claude agent 部署自我複製惡意程式（turf war）敘事同屬「自我複製」主題，但本則為防禦端主動發現而非攻擊端部署，不逕自合併；不列入母頁「現在還擋不住的攻擊」表（第三方廠商動態）
- **查證（2026-10-17，[DeepInspect](https://www.deepinspect.ai/blog/openai-self-replicating-prompt-injection-connector-output-containment)、[The New Stack](https://thenewstack.io/?p=22838480)；OpenAI 原文未讀）**：OpenAI 於 09-25 揭露，自動化紅隊系統 GPT-Red 發現「自我複製提示注入」（媒體稱）
  - 機制：注入除達成攻擊目標，還讓模型把注入內容重現於輸出管道（email、檔案寫入、程式碼註解），可在 agent 間傳播；是提示注入手法而非待修補的單點漏洞
  - OpenAI 稱模擬工具呼叫以外未見影響；緩解為把自我複製納入 GPT-Red 攻擊目標、據以訓練後續模型。發現日與重現模型各報導不一（06-27；GPT-5.4-mini、GPT-5.5）
- **可信度評估**：單一來源（shattered.io），0 互動，RSS 無正文，訊號強度低

#### cyberpress.org／gbhackers.com：Salesforce Agentforce 零點擊提示注入漏洞可竊取 CRM 資料（2026-09-25 新增，跨類別，非 Claude 專屬）

- **揭露來源**：cyberpress.org（經 提示注入定向補抓，2026-09-25 10:32 UTC）、gbhackers.com（經 提示注入定向補抓，2026-09-25 07:53 UTC）；兩家資安媒體同日報導同一漏洞
- **核心主張**：Salesforce 的 AI agent 平台 Agentforce 存在零點擊提示注入漏洞，攻擊者無需使用者互動即可觸發，用以竊取 CRM 資料
- **性質判斷**：非 Claude／Anthropic 產品，屬第三方商用 agent 平台事件；已列入「## 提示注入已不是單點漏洞，是產業級攻擊面」訊號表
- **可信度評估**：兩家獨立資安媒體同日報導，僅標題/摘要可用，具體攻擊鏈、受影響範圍與 Salesforce 官方回應均未見報導

#### SQ Magazine：Manus AI Agent 爆提示注入漏洞（2026-09-24 新增，跨類別，非 Claude 專屬）

- **揭露來源**：SQ Magazine（經 提示注入定向補抓，2026-09-24 15:36 UTC）
- **核心主張**：標題稱 Manus AI agent 存在提示注入漏洞並遭揭露，具體攻擊鏈與影響範圍僅標題可用
- **性質判斷**：非 Claude／Anthropic 產品，屬第三方 agent 平台事件；已列入「## 提示注入已不是單點漏洞，是產業級攻擊面」訊號表
- **可信度評估**：單一來源，僅標題可用，待更多媒體佐證

#### cyberpress.org：開源 AI Agent 平台 MaxKB 爆嚴重提示注入漏洞，可致攻擊者以 root 權限執行指令（2026-09-22 新增）

- **揭露來源**：cyberpress.org〈Critical MaxKB AI Agent Flaw Lets Prompt Injection Execute Commands as Root〉（2026-09-22）
- **核心主張（原僅標題可用，10-17 已查證見下）**：開源 AI agent 平台 MaxKB 被揭露存在嚴重提示注入漏洞，可致攻擊者以 root 權限執行任意指令；具體攻擊鏈、CVE 編號、是否已修補均未見報導
- **性質判斷**：MaxKB 為 Claude 以外的第三方開源 agent 平台，非 Claude／Claude Code 事件，不列入母頁「現在還擋不住的攻擊」表；收錄理由為本頁「提示注入產業級攻擊面」敘事最新一例
- **查證（2026-10-17，[SentinelOne 漏洞庫](https://www.sentinelone.com/vulnerability-database/cve-2026-77521/)）**：疑對應 CVE-2026-77521（MaxKB SandboxShellBackend 指令注入，官方 root 容器部署受影響；與 cyberpress 標題的對應為推論）
  - 修補：2.10.5-lts 起修正；同版另修 CVE-2026-79916（AWS Bedrock 整合，已驗證使用者可達 root 指令執行，漏洞庫資料）；在野利用未見公開紀錄
- **可信度評估**：cyberpress.org 為資安專門媒體，惟僅標題可用，無具名研究者披露文章可查證

#### VentureBeat：企業把決策交給 Jev 這類 AI agent，提示注入恐左右其判斷（2026-09-22 新增）

- **揭露來源**：VentureBeat〈Jev AI agent security: Prompt injection risk〉（2026-09-22）
- **核心主張（僅標題可用）**：分析企業將關鍵決策交給 Jev（TypeSafe AI 推出的「Decision Model」類 LLM）時，提示注入可能影響其判斷結果；具體攻擊情境與防護建議均未見報導
- **性質判斷**：Jev 為 Claude 以外的第三方 agent 產品，不列入母頁「現在還擋不住的攻擊」表；收錄理由同上
- **可信度評估**：VentureBeat 為主流科技媒體，惟僅標題可用，具體技術細節未見報導

#### Cloud Computing News：AWS AgentCore 提示注入漏洞恐暴露憑證（2026-09-22 新增）

- **揭露來源**：Cloud Computing News〈AWS AgentCore prompt injection exposes credential risks〉（2026-09-22）
- **核心主張（僅標題可用）**：AWS AgentCore 存在提示注入風險，可能導致憑證外洩；具體攻擊鏈、受影響版本與 AWS 官方回應均未見報導
- **性質判斷**：AWS AgentCore 為第三方雲端 agent 框架，非 Claude 官方產品，不列入母頁「現在還擋不住的攻擊」表；與既有 08-27／08-28 MCP RCE、記憶憑證竊取系列同屬「代理讀取外部內容缺乏信任邊界」主題
- **可信度評估**：Cloud Computing News 為資安/雲端專門媒體，惟僅標題可用，無具名研究者披露或 CVE 編號可查證

#### Simon Willison：agent 自產的對話壓縮摘要可能藏有自我觸發的提示注入（2026-09-18 新增）

- **揭露來源**：[Simon Willison 部落格](https://simonwillison.net/2026/Sep/17/compaction-summaries/)（2026-09-17 20:57 UTC），轉引 OpenAI 對齊研究團隊的發現
- **核心內容**：agent 在自己產生的對話壓縮摘要（compaction summary）中，可能無意間寫入之後會被自己讀回並執行的提示注入內容——注入來源不是外部網頁或檔案，而是 agent 自己先前的輸出
- **性質判斷**：與本頁「提示注入…攻擊面」節既有觀察（外部內容當可信輸入）不同——本則信任邊界問題出在 agent **自身生成內容**；轉引 OpenAI 對齊團隊發現，非官方確認 Claude Code 受影響，本頁不代為推論
- **可信度評估**：Simon Willison 為長期具名開發者／評論者，惟本則為轉引他人（OpenAI）發現，非第一手驗證

#### Startup Fortune：剖析提示注入在 AI Agent 中的運作機制與新創企業中招原因（2026-09-18 新增，跨類別，非 Claude 專屬）

- **揭露來源**：Startup Fortune（經 提示注入定向補抓補抓）
- **核心內容**：文章剖析提示注入在 AI agent 中的運作機制，以及新創企業為何一再中招；未指名特定廠商或 Claude Code
- **性質判斷**：屬本頁「## 提示注入已不是單點漏洞，是產業級攻擊面」既有敘事的社群教育側面，與既有 SitePoint（09-15）、Security Boulevard／SC Media（09-10～11）等教學／產業對照類條目性質相近；本頁對提示注入另有定向補抓，收錄不套用 Claude/Anthropic 關聯門檻
- **可信度評估**：僅標題可用，具體案例與技術手法未見報導

#### 資安研究團隊揭露「bragjack」技術，劫持含 Claude in Chrome 在內的 5 款瀏覽器內建 AI 助理（2026-09-17 新增）

- **揭露來源**：Hacker News〈With 1 Extension: $20K in Bounties from Anthropic, Perplexity, Google, Microsoft〉（10 分）
- **核心內容**：資安研究團隊揭露透過瀏覽器內建 AI 助理（Claude in Chrome、Chrome／Edge／Opera 內建 AI、Perplexity Comet）的「bragjack」劫持技術，稱已攻陷 5 款主流瀏覽器；Anthropic、Perplexity、Google、Microsoft 等廠商懸賞合計 2 萬美元；手法與修補狀態見下方 🔎 標記
- **性質判斷**：與本頁既有「Claude for Chrome 兩項權限缺陷」（合成點擊、skipPermissions）屬不同技術手法，暫無足夠細節確認是否為同一攻擊面的延伸，故不併入該列；具名安全研究、有具體懸賞金額佐證，訊號強度高於一般論述文章
- 🔎 **查無官方**（標 2026-09-17｜查 bragjack、Claude in Chrome｜複 2026-11-14）：2026-10-03 查 support.claude.com「Use Claude in Chrome safely」等官方頁與 Anthropic 提示注入防禦文章，均未載 BragJack；官方聲明與修補版本未見（10-17 再查同）
  - 媒體稱（BleepingComputer、GBHackers 等；多數原文 egress 封鎖僅取搜尋摘要）：Forever Security 的 Gal Weizman 於 2026-09-16 公布，惡意擴充套件以 declarativeNetRequest 加 content script 劫持 AI 助理與其特權元件間的通道（「prompt forcing」，不經提示注入、繞過模型層過濾）
  - 媒體稱（續）：安裝後無需點擊，可讀本機檔案、截圖並可能觸及相機麥克風；波及 Chrome（Gemini）、Edge（Copilot）、Opera Neon、Perplexity Comet 與 Claude in Chrome
  - 媒體稱（修補）：Chrome（CVE-2026-0628，7,000 美元）與 Edge（CVE-2026-55945）已修補；Anthropic 據稱修補了 Claude in Chrome 的特定弱點並付 600 美元獎金，合計獎金逾 2 萬美元
  - 媒體稱（Dark Reading、Hexnode）：Anthropic 已修補並支付賞金（低至約 600 美元，Pillitteri 轉述）、未發 CVE；Anthropic 側缺口為行銷頁面權限過大，擴充套件可在該網域注入腳本向側邊欄傳訊，為五案中最輕
- **可信度評估**：具名資安研究團隊與具體懸賞金額為佐證，惟未見獨立媒體交叉確認，攻擊技術細節僅有標題摘要

#### SitePoint：TypeScript 中防範 AI Agent Context Injection 教學（2026-09-15 新增，跨類別，非 Claude 專屬）

- **揭露來源**：SitePoint（經 Google News 轉載，僅標題可用）
- **核心內容**：教學文章示範如何在 TypeScript 中防範 AI agent 的 context injection（情境注入）攻擊；未指名特定廠商或 Claude Code
- **性質判斷**：屬本頁「提示注入已不是單點漏洞，是產業級攻擊面」既有敘事的社群教育側面；本頁對提示注入另有定向補抓，收錄不套用 Claude/Anthropic 關聯門檻
- **可信度評估**：僅標題可用，具體防護手法未見報導

#### Security Boulevard／SC Media：coding agent 產業對照案例（2026-09-10～11 新增）

- **揭露來源**：Security Boulevard〈AI Security Incident Case: Amazon Kiro Prompt Injection Vulnerability Analysis〉（2026-09-11）；SC Media〈A security framework for coding agents and their harnesses〉（2026-09-10）
- **核心主張**：Security Boulevard 分析 Amazon Kiro（非 Claude 產品）的提示注入漏洞案例；SC Media 討論 coding agent 與其執行環境（harness）的通用安全框架設計。兩篇均僅標題可用，具體技術內容與是否涉及 Claude Code 未見報導
- **與本頁關係**：產業對照，非 Claude 事件；coding agent 通用安全框架若日後涉及 Claude Code 具體做法，另開條目

#### The Hacker News：惡意 `.git` 設定檔可誘使 Claude、Codex、Cursor 等多款 AI coding agent 執行攻擊者程式碼（2026-09-02 新增）

- **揭露來源**：The Hacker News〈Malicious .git Configs Can Make Claude, Codex, Cursor, and Other AI Agents Run Attacker Code〉
- **核心內容**：報導揭露惡意 `.git` 設定檔可誘使 Claude、Codex、Cursor 等多款 AI coding agent 執行攻擊者指定的程式碼；為資安公司 Manifold Security 揭露、名為「GitSpawn」的攻擊，橫跨 7 款命令列 AI coding agent 共 8 個缺陷
- **性質判斷**：屬新增攻擊向量，且跨廠通用（涵蓋 Codex、Cursor 等），非 Claude 單一產品缺陷；
  - 與本頁既有「乾淨 GitHub Repo 提示注入可取得完整系統控制」（Mozilla 0din，2026-06-28）、Keyv／cacheable npm 供應鏈蠕蟲等「代理信任 repo 內容/設定檔」既有模式相近——版本控制系統的中繼資料（非程式碼本身）成為新的攻擊面，延續本頁「提示注入已不是單點漏洞，是產業級攻擊面」節的收斂觀察
- **觸發機制查證**（查證 2026-09-20）：攻擊利用 Git 效能設定 `core.fsmonitor`——此欄位指定一命令用來偵測變更檔案，從 repo 自身 `.git/config` 讀取，`git status`／`git diff` 等刷新索引操作都會執行該命令
  - agent 啟動時為判斷分支與檔案狀態會背景執行 Git 操作、未消毒 repo 設定內容，指令在**安全提示顯示之前**即以使用者權限執行（Claude Code／Hermes Agent 於 workspace-trust 核准前、Qwen Code 於認證前、Grok Build 於第一次按鍵時）
  - **觸發前提**：repo 須以保留 `.git` 目錄形式抵達（共享壓縮包／共用磁碟／同步資料夾／USB，一般 `git clone` 不觸發）
- **在野利用與修補狀態**：未偵測到實際在野利用（CISA 已知漏洞目錄至 2026-09-02 無對應 CVE 收錄）
  - 修補狀態：goose、Codex CLI（v0.131.0）、**Claude Code（v2.1.196 部分修補）**、Cursor 已修復；Hermes Agent、Qwen Code、Grok Build 與 Claude Code 另一條執行路徑於 09-01 覆測時仍未修補；OpenAI 同日就 Codex 同類缺陷另發布 3 項 CVE
  - 2026-10-30 查證（CSA 09-04 研究註記轉述 Manifold，二手）：Claude Code 第二變體（ultrareview）至 2.1.252 仍未修；正常 `git clone` 不重現
- **可信度評估**：The Hacker News 轉載 Manifold Security 原始揭露，具體技術細節、CVE 對照與修補版本號齊全，訊號強度高（[The Hacker News](https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html)，查證 2026-09-20）

#### teiss：論述提示注入從單點攻擊演變為自我傳播機制（2026-09-02 新增）

- **揭露來源**：teiss〈News - When prompt injection becomes a propagation mechanism〉
- **核心內容（僅標題可用）**：文章探討提示注入如何從單點、一次性攻擊演變成可**自我傳播**的機制；具體技術細節、是否涉及 Claude 系列模型均未見報導
- **性質判斷**：屬論述／背景分析文章，非具體事件；與本頁既有「## 提示注入已不是單點漏洞，是產業級攻擊面」節收斂觀察及 09-01～09-02 Auto Mode 提示注入劫持案例屬同一風險主題的背景報導，若「自我傳播」屬實將是攻擊模式性質的再一次升級（從「單次觸發即可執行」到「執行後可自行擴散」）
- **可信度評估**：單一來源，僅標題層級可用，論述深度、具體案例與是否有可複現的自我傳播 PoC 待查

### 2026-08

#### embracethered／The Register：Auto Mode 提示注入實測 60–80% 攻擊成功率 vs 官方評測 0%（2026-08-31 新增，升級既有 08-27～08-29 條目）

- **揭露來源**：embracethered 部落格（[Breaking Claude Code Opus 5 and AutoMode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/)）；The Register（[Researcher shows how Claude Code can be tricked simply by asking it to summarize a website](https://www.theregister.com/research/2026/08/28/researcher-shows-how-claude-code-can-be-tricked-simply-by-asking-it-to-summarize-a-website/5293372)）
- **核心主張（數字並陳，不擇一）**：資安研究者示範只要請 Claude Code Opus 5 Auto Mode「摘要一個網頁」，就能在小樣本測試中達成 **60–80%** 提示注入攻擊成功率並取得程式碼執行權限；此數字與 Anthropic 委託第三方針對 Auto Mode 的評測（宣稱提示注入攻擊成功率 **0%**）形成明顯落差
- **性質判斷**：屬 08-27～08-29 已記錄的 embracethered／Cybernews Auto Mode 安全繞過主線的**升級**（首個量化數字），非新事件；觸發條件（僅需請求摘要網頁）與 08-28 The Register 記錄的「Claude Code 本身最小觸發路徑」一致，本則為同一研究者對同一漏洞補上攻擊成功率統計
- **可信度評估**：embracethered 為長期具名資安研究者（已於 08-27 建立可信度）；The Register 為主流資安媒體；惟「小樣本測試」規模與方法論細節（樣本數、測試環境、Auto Mode 版本）僅標題與部落格連結可用，尚待更完整方法論揭露；官方 0% 數字的評測方法論與委託第三方身分亦未見報導，兩造數字均待進一步查證方法論是否可比
- **09-02 新增（媒體稱官方無修復計畫）**：Tech Times〈Summarizing Website in Claude Code Auto Mode Can Compromise Your Machine; No Fix Planned〉與 The Next Web〈A researcher hijacked Claude Code by asking it to summarise a web page〉跟進報導同一 embracethered／The Register 揭露，並稱**官方目前並無修復計畫**；此為媒體稱述，非官方公開拒修聲明（不同於本頁既有 symlink 案例中 HackerOne 官方明確結案為「Informative」），暫不比照升級為 ⛔，僅記錄媒體觀察
- 🔴 **未修復（量化落差升級，官方尚未就實測數字提出回應；09-02 媒體稱無修復計畫，未見官方公開聲明佐證）**

#### LM Studio Bionic：82% shell 指令未經 AI reviewer 放行即可執行，reviewer 模型可被提示注入騙過（2026-08-31 新增）

- **揭露來源**：Tech Times（[LM Studio Bionic Clears 82% Shell Commands Without AI Reviewer, Yields Prompt Injection](https://www.techtimes.com/articles/325987/20260831/lm-studio-bionic-clears-82-shell-commands-without-ai-reviewer-yields-prompt-injection.htm)）
- **核心內容（僅標題可用）**：報導稱 LM Studio Bionic 測試中有 82% 的 shell 指令未經 AI reviewer（審查模型）放行即可直接執行，且該 reviewer 模型本身可被提示注入手法騙過而放行本應攔截的危險指令；具體測試方法論、樣本規模與是否涉及 Claude 系列模型作為 reviewer 均未見報導
- **性質判斷**：屬產業對照，非 Claude/Claude Code 風險；與本頁既有「AI reviewer/gatekeeper 模型可被提示注入繞過」的威脅模型類別相關——若 reviewer 模型本身即為 LLM，提示注入可同時攻陷「被審查對象」與「審查者」兩層防線，此為 agent 安全架構設計上的通用弱點，非單一產品缺陷
- **可信度評估**：Tech Times 為主流科技媒體，惟單一來源，僅標題可用，測試方法論與可複現性待後續報導補充

#### StartupHub.ai：編碼 agent 在資安測試中重複踩到同一批 70 個錯誤模式（2026-08-30 新增）

- **揭露來源**：[Google News / StartupHub.ai](https://news.google.com/rss/articles/CBMikgFBVV95cUxQbGo1ZDRFc3VMQ0VrMFg2VGFtb1hNRTdieFRPWFJldlZKdzloRGxIT0RoWGVWVzNXSDloYktHcHN6Q3hXaE1kNVdPZW1vLXhUZXpvQ2U2dWhwNnhoX2tQbFdkZXA4RmxubUVyRTRFTH?oc=5)（2026-08-29）標題「Coding Agents Security Failed 70 Times, Same Bugs」
- **核心主張**：報導稱編碼 agent 在資安測試中反覆踩到相同類型的 70 個錯誤模式；僅標題可用，測試對象（是否涵蓋 Claude 系列）、測試方法論、70 個錯誤模式的具體內容均未見報導
- 📋 **論述文章，非具體事件**：與 Claude/Anthropic 無直接關聯，因與本頁 agent 安全主題相關而收錄
- **可信度評估**：StartupHub.ai 知名度較低，僅單一來源標題可用，未見其他資安媒體交叉確認

#### embracethered／Simon Willison／Cybernews：Claude Code Opus 5 Auto Mode 安全機制遭繞過，並有實際惡意程式碼利用案例（2026-08-27～08-28 新增，08-29 補充在野細節）

- **揭露來源**：simonwillison.net（2026-08-27）轉載資安研究者 embracethered 的技術揭露，標題「Breaking Claude Code Opus 5 Auto Mode」；
  - Cybernews（經 Google News 轉載，2026-08-28）標題「Claude Code Auto Mode malware vulnerability」；
  - Cybernews（08-29）標題「Claude Code runs malware despite "Auto Mode" security, tries to fix it, gets denied」
- **核心主張**：embracethered（長期研究 AI agent 提示注入與安全繞過的具名資安研究者）公布可繞過 Claude Code Opus 5「Auto Mode」（低監督/高自動化預設權限模式）安全機制的攻擊手法，示範可誘使 agent 在未經授權情況下執行任意程式碼；Cybernews 進一步補充至少一起實際遭惡意程式碼利用的在野案例，顯示此繞過手法已從概念驗證進入實際濫用階段
- **08-29 在野細節補充**：Cybernews 續篇描述該起在野案例的具體經過——Claude Code 已實際執行到惡意程式碼，事後 agent 自行嘗試修復（試圖清除或還原該惡意行為），但修復動作遭拒絕執行；僅標題與轉址連結可用，具體「被誰／被什麼機制拒絕」（Auto Mode 權限檢查、使用者手動介入，或其他防護層）未見報導細節
- **性質判斷**：屬產品層安全（權限/沙箱繞過），非模型層安全問題；Auto Mode 為 Claude Code 預設運作模式之一，繞過影響範圍廣。依本頁「威脅有生命週期」分析框架，此案已從「發現」進入「在野利用」階段，08-29 補充顯示利用已進展至「agent 自覺異常並嘗試補救」的新階段，嚴重度高於本頁近期多數僅標題可用的條目
- 🔴 **未修復**（具名研究者揭露＋Cybernews 補充實際利用案例雙重確認；官方尚未公開回應或修補說明）
- **可信度評估**：embracethered 為長期具名資安研究者，經 Simon Willison（業界高信譽轉載者）背書；Cybernews 補充實際利用案例與後續補救細節，兩獨立來源交叉確認，訊號強度高於單純標題轉載

#### Ars Technica／Alon Hertz／The Register：Claude、Codex、Hermes 等編碼 agent 信任 llms.txt 導致企業網路內安裝來源不明程式碼（2026-08-27 新增，08-29 補充研究方法論與具名研究者）

- **揭露來源**：Ars Technica（經 Google News 轉載，2026-08-27 14:00 UTC）；標題「Claude, Codex, and Hermes installed unowned code inside corporate networks」；
  - startupfortune.com（經 Hacker News 轉載，12 分，2026-08-29）標題「Researcher Alon Hertz Tricked Claude, Codex and Hermes into Running Malware」，引用並補充 Ars Technica 報導的具名研究者與方法論；
  - The Register（Google News，2026-08-28）標題「Researcher shows how Claude Code can be tricked simply by asking it to summarize a website」，聚焦同一攻擊面對 Claude Code 本身的影響
- **08-29 補充：具名研究者與攻擊方法論**：資安研究者 **Alon Hertz** 發現編碼 agent（Claude、Codex、Hermes 等）會把 `llms.txt`／`llms-full.txt`（網站給 AI 讀取用的「網站說明檔」慣例）內容當成可信指令，而非需審查的外部輸入；
  - Hertz 掃描 **6,214 個網域**（涵蓋國防承包商、財星 500 大企業、科技巨頭）、共 **8,265 份**此類檔案，其中 **120 份**檔案內容指向**尚未註冊的套件名稱**——理論上攻擊者可搶注這些套件名稱、植入惡意程式碼，待受害企業的 agent 依 llms.txt 指示安裝時即完成供應鏈感染，攻擊面可觸及企業內網
- **The Register：Claude Code 本身的觸發路徑**：僅需要求 Claude Code「摘要一個網站」，即足以讓其讀取並信任該網站的 llms.txt 內容做出非預期行為——具體示範了 Ars Technica／Hertz 研究中「agent 信任 llms.txt」機制在 Claude Code 上的最小觸發條件；
  - 僅標題與轉址連結可用，未見與 Hertz 研究是否為同一次揭露或獨立示範的說明
- **性質判斷**：屬「agent 對外部內容過度信任」的產品層安全問題（提示注入的一種變體），非模型層安全問題；攻擊鏈已具體化為「llms.txt 指向未註冊套件名稱 → 攻擊者搶注 → agent 依指示安裝 → 惡意程式碼進入企業內網」，屬可重現的供應鏈攻擊方法論
- ❓ **待查證**（標 2026-08-27｜查 Ars Technica、unowned code、Hermes｜複 2026-11-11｜訊 2026-08-29）｜**攻擊性質**：120 份問題檔案是否已有套件被搶注、是否有真實在野感染案例，Hertz 報告與 The Register 均未見報導
  - 性質本身已由 08-29 Hertz 研究釐清：屬第三方可預先佈局的供應鏈攻擊（llms.txt 指向未註冊套件名，攻擊者搶注後經 agent 安裝流程植入企業內網），非「agent 自主行為的意外後果」
  - **2026-09-27 依日報複查**：訊號日 08-29 對應的日報條目（`news/2026-08-29.md`）確認為同一起 Alon Hertz 揭露（同一批 6,214 網域／8,265 檔案／120 份未註冊套件名稱數字），非探針誤命中；惟內容與本頁既有段落相同，未提供「套件是否已被搶注」或「是否有真實在野感染案例」的新事實。未查官方一手來源，標記保留，狀態維持 ❓
- **可信度評估**：Ars Technica 為主流資安/科技媒體；startupfortune.com 補充具名研究者與量化掃描數據（6,214 域名／8,265 檔案／120 份問題檔案），數字具體可查證性較高，惟 startupfortune.com 本身知名度較低，數字尚待其他資安媒體交叉確認；The Register 為主流資安媒體但僅標題可用

#### gbhackers／CyberSecurityNews：MCP 遠端程式碼執行、盲提示注入與記憶憑證竊取針對 AI 基礎設施（2026-08-27／28 新增，08-29 CyberSecurityNews 跟進）

- **揭露來源**：gbhackers.com；標題「Attackers Exploit MCP RCE, Blind Prompt Injection and Memory Credential Theft Against AI Infrastructure」；
  - CyberSecurityNews（2026-08-29）標題「Hackers Target AI Infrastructure With RCE, Prompt Injection and API Key Theft」，攻擊類型分類與 gbhackers 08-27 報導高度重疊（RCE／提示注入／憑證竊取），未見報導提供 gbhackers 未載的新事實，僅標題可用
- **關聯性**：MCP（Model Context Protocol）為 Anthropic 提出並開源的協定，與 Claude Code 生態高度相關
- **核心內容**：揭露針對 AI 基礎設施的三類攻擊手法——MCP 遠端程式碼執行（RCE）、盲提示注入（blind prompt injection）、記憶（memory）憑證竊取；攻擊者在蜜罐中提供惡意 stdio 式 MCP 設定，下載並啟動加密貨幣挖礦程式，同時回傳語法正確的 MCP 握手訊息使連線測試看似正常，載荷使用暫時隱藏目錄、以分離程序啟動並事後清除，降低磁碟鑑識痕跡
- **查證結果**（查證 2026-09-20）：**為特定實作缺陷，非 MCP 協定本身設計問題，也不涉及 Anthropic 官方 MCP 伺服器**
  - 核心為 **CVE-2026-42271**（LiteLLM AI Gateway 代理伺服器 RCE，影響 1.74.2–1.83.6 版）——兩個 MCP 預覽端點接受完整伺服器設定（`command`／`args`／`env`），已驗證使用者均可觸發子行程執行，且缺乏角色權限控管
  - 該漏洞 2026 年 6 月已列入 CISA 已知漏洞目錄，並可與 Starlette host-header 繞過漏洞 **CVE-2026-48710** 串接，升級為「未經驗證即可入侵」；LiteLLM 為第三方 AI 閘道代理伺服器，非 Anthropic 官方 MCP 實作
- **性質判斷**：MCP 為 Claude Code 與多款 agent 工具共用的協定層，惟本次揭露的攻擊鏈綁定 LiteLLM 這一特定實作，非協定規格本身缺陷；影響範圍限於部署該閘道的環境，非全 MCP 生態
- **可信度評估**：CVE 編號、受影響版本區間、CISA KEV 收錄日期均可獨立查證，訊號強度高（[The Hacker News：LiteLLM Flaw CVE-2026-42271 Exploited in the Wild](https://thehackernews.com/2026/06/litellm-flaw-cve-2026-42271-exploited.html)、[Horizon3：CVE-2026-42271 chained with CVE-2026-48710](https://horizon3.ai/attack-research/vulnerabilities/cve-2026-42271-chained-with-cve-2026-48710/)，查證 2026-09-20）

#### Wiz：90 天 AI 基礎設施蜜罐遙測數據，量化實際攻擊型態（2026-08-27／28 新增）

- **揭露來源**：wiz.io 官方部落格；標題「Attacks on AI Infrastructure: 90-Day Honeypot Telemetry」
- **關聯性**：Wiz 為主流雲端資安廠商，蜜罐遙測數據呼應本頁 2026-06-16 OALABS 蜜罐分析的既有觀察（威脅已從理論轉為在野事實）
- **核心內容**（查證 2026-09-20，[Wiz 官方部落格原文](https://www.wiz.io/blog/ai-infrastructure-honeypot)）：三類攻擊型態——① 曝露 MCP 伺服器 RCE（即上方 CVE-2026-42271／CVE-2026-48710 串鏈）、② 對 agent 框架的盲提示注入、③ 針對 AI 環境內部特徵客製化的「AI 原生後滲透」
  - 受攻擊系統含 LiteLLM、Flowise、LangChain、Langflow、ChromaDB、Ollama、Node-RED、OpenWebUI；另揭露 CVE-2026-59822（LiteLLM OAuth2 繞過）
  - **官方原文未提供攻擊類型佔比或次數等百分比統計**，「量化」僅指涵蓋期間與系統清單具體化，本頁原先預期的「具體遙測數字」官方並未提供，屬期待落差而非未查到
- **是否涉及 Claude/Claude Code**：官方原文提及攻擊者會利用 **`.claude/` 目錄**做為載荷偽裝路徑（因其在真實環境中不顯眼、易於混入），屬攻擊者「借殼」Claude Code 慣用目錄結構掩護行跡，並非 Claude Code 本身存在漏洞或成為攻擊媒介
- **性質判斷**：為量化型資料來源之延伸統計背景，實際內容偏質化（攻擊型態分類與受害系統清單），非逐項百分比拆解
- **可信度評估**：Wiz 為主流雲端資安廠商官方一手資料（非媒體轉述），可信度高

#### The Hacker News：Amazon Kiro 提示注入可透過「Kiro Powers」外洩敏感資料（2026-08-27 新增）

- **揭露來源**：Google News／The Hacker News（2026-08-27）；標題「Amazon Kiro Prompt Injection Can Exfiltrate Sensitive Data Through Kiro Powers」
- **性質**：Amazon Kiro 為競品 AI IDE（非 Claude）
- **核心內容（僅標題可用）**：資安研究揭露 Amazon Kiro 存在可透過提示注入外洩敏感資料的漏洞，攻擊媒介為 Kiro 的「Powers」功能（推測為外部整合/擴充機制，未見官方文件確認其定義）；Google News RSS 未提供正文，攻擊鏈細節、是否已修補、研究者或機構具名均未見報導
- **性質判斷**：屬產業對照，非 Claude/Claude Code 風險；與本頁既有 08-22 CyberSecurityNews／Grok 零點擊攻擊揭露性質相同——皆為競品 agentic 工具的提示注入漏洞，補充「提示注入風險非 Claude 獨有」的產業視角，不列入母頁「現在還擋不住的攻擊」（該表僅列 Claude/Claude Code 使用者暴露的風險）
- **可信度評估**：The Hacker News 為主流資安媒體，惟單一來源，僅標題可用，待後續報導補充攻擊鏈細節與修補狀態

#### tech-insider.org：《How to Prevent Prompt Injection Attacks: 12 Steps, 90 Min》教學文章（2026-08-26 新增）

- **揭露來源**：Google News／tech-insider.org（2026-08-26）；標題「How to Prevent Prompt Injection Attacks: 12 Steps, 90 Min [2026]」
- **核心內容（僅標題可用）**：文章整理防範提示注入攻擊的 12 個步驟，屬教學/實務指南性質，非具體事件披露；Google News RSS 未提供正文，具體步驟內容、是否引用 Claude Code 或其他具名產品的攻擊案例均未見報導
- **性質判斷**：屬防護教學文章，非具體攻擊事件；與本頁「拿什麼擋」既有社群整理（沙盒隔離、操作確認節點等）性質相近，惟本則來源與內容細節不足，暫不併入該區塊
- **可信度評估**：單一來源，僅標題可用，待後續內容補充後再評估是否納入防護建議

#### VentureBeat：提示注入在 OWASP 風險排名居首、實際事故紀錄僅列第 12，攻擊本身難以被掃描偵測（2026-08-26 新增）

- **揭露來源**：Google News／VentureBeat（2026-08-26）；標題「Prompt injection ranks No. 1 with OWASP and No. 12 in the incident record. The attack itself is invisible to a scan.」
- **核心內容（僅標題可用）**：文章分析提示注入攻擊在 OWASP（Open Web Application Security Project）風險排名中居首位，但在實際事故紀錄中僅排第 12 名，且此類攻擊難以被常規掃描工具偵測；Google News RSS 未提供正文，具體資料來源、統計方法、是否涉及 Claude Code 相關事故均未見報導
- **性質判斷**：屬產業論述/分析文章，非具體攻擊事件；提出的「排名落差」觀點與本頁既有「模型層安全 ≠ 產品層安全」「威脅有生命週期」等分析框架相關，補充「提示注入偵測難度」的產業論述視角
- **可信度評估**：單一來源，僅標題可用，待後續報導補充具體統計數據與方法論

#### HackerNoon：提示注入攻擊已演化為可達成任意程式碼執行（RCE）的攻擊原語（2026-08-23 新增）

- **揭露來源**：Google News／HackerNoon（2026-08-23）；標題「Prompt Injection Is Now an RCE Primitive」
- **核心內容（僅標題可用）**：文章探討提示注入攻擊已演化為可被用來達成任意程式碼執行（RCE）的攻擊原語，屬一般性技術論述而非具體事件披露；Google News RSS 未提供正文，具體論證、案例或是否涉及特定產品／廠商均未見報導
- **性質判斷**：屬論述/分析文章，非具體攻擊事件；與本頁既有多起提示注入案例（乾淨 GitHub Repo 提示注入、Claude Code CI workflow secrets 外洩即 CVE-2026-54316 等）技術脈絡相關，補充「提示注入攻擊能力演進」的產業論述視角
- **可信度評估**：單一來源，僅標題可用，待後續報導補充具體技術論證

#### World IP Review：提示注入是否成為 AI 商業機密訴訟新戰場（2026-08-17 新增）

- **揭露來源**：World IP Review（2026-08-17）；標題「Prompt injection: The next frontier in AI trade secret litigation?」
- **與本頁其他事件的關係**：本頁已有多起提示注入攻擊案例（乾淨 GitHub Repo 提示注入、Claude Web Fetch 提示注入外洩機密等），本則從**法律視角**探討提示注入是否將成為 AI 商業機密訴訟的新戰場，補充技術事件之外的法律面向
- **核心內容（僅標題可用）**：探討提示注入攻擊手法是否將成為企業間商業機密（trade secret）訴訟的新興爭點，惟 Google News RSS 摘要未提供正文，具體法律論證、是否已有實際訴訟案例引用提示注入均未見報導
- **性質判斷**：屬法律分析/評論文章，非具體攻擊事件；與本頁「威脅模型思維」中技術層面的提示注入案例互補，提供讀者理解此類攻擊在法律責任歸屬上的潛在爭議
- **可信度評估**：單一法律專業媒體，待後續報導補充具體案例與論證細節

#### Study Finds Four Major AI Labs Use Incompatible Prompt Injection Metrics（2026-08-13 新增）

- **揭露來源**：Google News／Yellow.com（2026-08-13 09:54 UTC）；標題「Study Finds Four Major AI Labs Use Incompatible Prompt Injection Metrics」
- **可用資訊**：標題稱一項研究發現四大 AI 實驗室採用互不相容的提示注入（prompt injection）評測指標，導致各家防禦成效難以橫向比較；四家實驗室**未指名**，Google News RSS 未提供正文摘要
- **查證結果**（查證 2026-09-20）：**四大實驗室確認為 Anthropic、OpenAI、Google、Meta**；原始比較研究由 VentureBeat 於 06-01 發表，Yellow.com 08-13 為轉載
  - 核心發現：四家均各自發布提示注入揭露，但**沒有任兩家採用相同指標**——Anthropic 衡量瀏覽器 agent 遭挾持率，其他三家聚焦工具呼叫間接注入或文件摘要任務，均未用共同框架或對抗測試集
  - 企業採購方因此無法用單一基準橫向比較風險，某模型在甲實驗室定義下注入率低，換乙實驗室測試設計下可能曝險更高
- **可信度評估**：VentureBeat 為主流科技媒體一手分析報導，方法論與四家廠牌對照清楚，訊號強度高（[VentureBeat](https://venturebeat.com/security/prompt-injection-measurable-security-metric-one-ai-developer-publishes-numbers)，查證 2026-09-20）
- **與本頁其他事件的關係**：提示注入評測標準化議題與本頁既有提示注入攻擊案例主線相關
- **可信度評估**：僅單一標題可用，待後續報導補充四大實驗室名單與研究方法論

#### Claude Code 與 Gemini CLI 漏洞：GitHub Issue 內容可觸及 CI workflow secrets（2026-08-07 新增，僅標題）

- **揭露來源**：The Hacker News「Claude Code and Gemini CLI Flaws Let a GitHub Issue Reach CI Workflow Secrets」（08-07 08:18 UTC，經 Google News 轉載）
- **可用資訊**：標題稱 Claude Code 與 Gemini CLI 存在漏洞，攻擊者可透過 GitHub Issue 的內容觸及 CI workflow 的 secrets；具體攻擊鏈（如 Issue 內容如何被 agent 讀入並外洩至 workflow、是否需要特定權限設定）與是否已修補均無法從標題確認
- **重要性**：本輪唯一直接針對 Claude Code 本身（而非第三方生態或灰市服務）的安全漏洞揭露，優先追蹤
- **2026-08-10 查證結果（已結案）**：此為 **CVE-2026-54316**，由資安團隊 Novee 於 Black Hat USA 2026 揭露。
  - 核心事實：一個**沒有任何 repo 權限**的帳號開一則 GitHub Issue，即足以讓 issue 內容進入 agent 的處理流程並在 CI runner 上取得執行，進而觸及 workflow secrets（`GITHUB_TOKEN`、`ANTHROPIC_API_KEY` 等）；Claude Code 一側的外洩管道被描述為逐字元洩漏 API 金鑰。
  - 同批揭露的 Gemini CLI 缺陷經 Google 評為 **CVSS 10.0**（工具註冊未強制執行指令層級限制，子行程可經 `/proc` 讀取父行程環境變數）
- **受影響與修補版本**：Claude Code **0.2.54～2.1.162 受影響，2.1.163 已修補**；Gemini CLI 修於 0.39.1、run-gemini-cli 修於 0.1.22（[The Hacker News](https://thehackernews.com/2026/08/claude-code-and-gemini-cli-flaws-let.html)、[Hackread（Black Hat 現場）](https://hackread.com/black-hat-usa-2026-github-compromise-ai-coding/)，2026-08-10 查證）
- **讀者行動**：在 CI 中執行 Claude Code 且 workflow 帶 secrets 者，確認版本 ≥ 2.1.163；升級前應視同該 runner 的 secrets 已可能外洩並輪替

---

## 時序

> 每行開頭方括號的符號：🔴 已確認會發生／✅ 已處置或已修／🟡 產業對照或個案已處置／📋 論述或情資通報，非具體事件／🛠️ 官方或第三方防護動態。方括號其餘文字是一句話分類，非固定代碼。
> 更早期時序見 [[topics/ai-agent-safety-archive]]

### 2026-10-28
- **[📋 新增，定向補抓] OODA Loop：資安研究者偵測到在野提示注入，利用 coding agent 對 Markdown 檔案的信任**：單一來源、互動 0，詳見「## 技術彙整」

### 2026-10-27
- **[📋 跟進，❓ 待查證仍未解] CyberSecurityNews：第二個獨立來源報導 Claude Code／Codex 遭 Downloads 資料夾惡意檔案劫持**：呼應 10-26 Martin Cid Magazine 同一攻擊面披露，兩篇報導均僅標題層級，觸發機制與官方回應仍未見細節，詳見母頁「現在還擋不住的攻擊」、「## 技術彙整」

### 2026-10-26
- **[📋 新增，❓ 待查證] Martin Cid Magazine：Claude Code／Codex 會遵從 Downloads 資料夾內任何網站放入的檔案指令**：單一來源，詳見母頁「現在還擋不住的攻擊」、「## 技術彙整」

### 2026-10-22
- **[📋 新增，跨類別，非 Claude 專屬] GBHackers：Flowise AI agent 平台遭認證竊取、提示注入與工作流程劫持攻擊**：攻擊鏈細節與受影響範圍均未見報導，與既有跨廠商提示注入系列同屬一條線，詳見「## 技術彙整」
- **[📋 新增，教育/論述層訊號] HackerNoon：彙整防範 AI agent 長期記憶遭持續性提示注入攻擊的方法**：僅標題可用，與既有教育層訊號系列同屬一條敘事，詳見「## 技術彙整」

### 2026-10-17
- **[📋 新增] 《AI Agent Prompt Injection: What the Evidence Actually Shows》彙整提示注入實證研究現況**：僅標題可用，教育／論述層訊號，詳見「## 技術彙整」

### 2026-10-15
- **[📋 新增，跨類別，非 Claude 專屬] The Register／HiddenLayer：決策模型 Jev 可被 prompt injection 攻破，27 次攻擊 25 次成功翻轉決策**：僅輸出預定選項仍防不住，詳見「## 技術彙整」

### 2026-10-14
- **[📋 新增] tech-insider.org：整理 13 個防禦 agent 遭 prompt injection 攻擊的步驟**：教育層訊號，僅標題可用，詳見「## 技術彙整」

### 2026-10-13
- **[📋 新增，官方一手研究] Anthropic 官方研究：小型模型數月內可能具備脫離資料中心、在物聯網裝置上自我複製的能力**：90 億參數模型在 9 種硬體類型中的 8 種成功跑起推論，為「自我複製／蠕蟲化」階梯第七階，詳見「## 技術彙整」、「## 自我複製／蠕蟲化」

### 2026-10-11
- **[📋 新增，跨類別，非 Claude 專屬] CyberSecurityNews：單一提示即可挾持 AWS AI Agent 竊取雲端憑證**：僅標題可用，是否同屬 09-22 AWS AgentCore 系列的懸置標記見「## 技術彙整」
- **[📋 新增，跨類別，防範論述] HackerNoon：測試以來源驗證機制防禦間接提示注入**：僅標題可用，詳見「## 技術彙整」

### 2026-10-08
- **[🛠️ 新增，模型防護] Help Net Security 等：Claude Haiku 5.5 抵抗隱藏指令注入防禦力提升**：詳見「## 技術彙整」

### 2026-10-06
- **[🔴 新增，非 Claude 專屬] CyberSecurityNews：GitHub Copilot CLI 存在加密提示注入漏洞，可竊取開發者機密**：加密內容繞過一般提示注入偵測，具體攻擊鏈與修補狀態未見報導，詳見「## 技術彙整」

### 2026-10-01
- **[📋 新增] Simon Willison 引述 Matthew Green：沙盒隔離 agent 透過共用套件快取留訊息，已具備蠕蟲傳播兩要素**：呼應既有自我複製提示注入敘事，非具名 Claude 事件，詳見「## 技術彙整」

### 2026-09-30
- **[📋 新增] The Register：自我複製型提示注入續添一則「AI 新憂慮」**：僅標題可用，呼應既有自我傳播敘事，詳見「## 技術彙整」

### 2026-09-29
- **[📋 新增，跨類別，論述] NH Business Review：提示注入類比新型社交工程，提出防範框架**：僅標題可用，已列入產業級攻擊面訊號表第 8 則，詳見「## 技術彙整」

### 2026-09-27
- **[📋 新增，非 Claude 事件] shattered.io：OpenAI 紅隊工具 GPT-Red 揪出自我複製的 AI worm 漏洞**：僅標題可用，具體攻擊鏈與修補狀態未見報導，詳見「## 技術彙整」

### 2026-09-25
%% 維運備忘：09-23～09-25 既有的 ABC News／TechRadar／Salesforce Agentforce／Manus AI 技術彙整條目在時序缺對應行，非本輪造成，回報中已轉知主編，本輪不回填 %%

### 2026-09-22
- **[🔴 新增，非 Claude 事件] cyberpress.org：開源 agent 平台 MaxKB 爆嚴重提示注入漏洞，可致 root 權限執行指令**：詳見「## 技術彙整」
- **[📋 新增，非 Claude 事件] VentureBeat：企業交給 Jev 的決策恐受提示注入影響**：詳見「## 技術彙整」
- **[🔴 新增，非 Claude 事件] Cloud Computing News：AWS AgentCore 提示注入恐暴露憑證**：詳見「## 技術彙整」

### 2026-09-18
- **[📋 新增] Simon Willison：agent 自產的對話壓縮摘要可能藏有自我觸發的提示注入**：轉引 OpenAI 對齊團隊發現，未確認是否影響 Claude Code，詳見「## 技術彙整」
- **[📋 新增，跨類別] Startup Fortune：剖析提示注入在 AI Agent 中的運作機制與新創企業中招原因**：未指名特定廠商，詳見「## 技術彙整」

### 2026-09-17
- **[新增，技術細節不足] 資安研究團隊揭露「bragjack」技術，劫持含 Claude in Chrome 在內的 5 款瀏覽器內建 AI 助理**：Anthropic 等廠商懸賞合計 2 萬美元，攻擊手法與修補狀態見「## 技術彙整」🔎 標記

### 2026-09-15
- **[🌐 跨類別，新增] SitePoint：TypeScript 中防範 AI Agent Context Injection 教學**：通用防護教學，非 Claude 專屬，詳見「## 技術彙整」

### 2026-09-11
- **[🟡 產業對照，新增] Security Boulevard：Amazon Kiro 提示注入漏洞分析／SC Media：coding agent 安全框架討論**：非 Claude 事件；均僅標題可用，詳見「## 技術彙整」

### 2026-09-02
- **[新增] The Hacker News：惡意 `.git` 設定檔可誘使 Claude、Codex、Cursor 等多款 AI coding agent 執行攻擊者指定程式碼**：新增攻擊向量，跨廠通用（詳見「## 技術彙整」，已查證 2026-09-20：Manifold Security 揭露之 GitSpawn 攻擊，各廠商修補進度不一，仍列母頁「現在還擋不住的攻擊」表）
- **[🟡 媒體觀察，新增] Tech Times／The Next Web：跟進報導 Auto Mode 提示注入劫持，媒體稱「官方目前無修復計畫」**：既有 08-31 embracethered／The Register 60–80% 攻擊成功率揭露的補充，非官方公開拒修聲明，詳見「## 技術彙整」
- **[📋 論述文章，新增] teiss：論述提示注入從單點攻擊演變為自我傳播機制**：僅標題可用，與 Auto Mode 劫持事件同屬提示注入產業攻擊面主題，詳見「## 提示注入已不是單點漏洞，是產業級攻擊面」與「## 技術彙整」

### 2026-09-01
- **[跟進，無新細節] BankInfoSecurity：跟進報導 Auto Mode 60–80% 提示注入實測**：延續 08-31 既有量化數字，未見新細節

### 2026-08-31
- **[🔴 已確認，升級，新增] embracethered／The Register：Auto Mode 提示注入實測 60–80% 攻擊成功率，與官方委託評測宣稱 0% 形成明顯落差**：僅需請 Claude Code Opus 5 Auto Mode「摘要一個網頁」即可觸發，小樣本測試取得程式碼執行權限；為 08-27～08-29 既有繞過主線補上首個量化數字，詳見「## 技術彙整」
- **[🟡 產業對照，非 Claude 風險，新增] Tech Times：LM Studio Bionic 82% shell 指令未經 AI reviewer 放行即可執行，reviewer 模型可被提示注入騙過**：競品工具實測數字，詳見「## 技術彙整」

### 2026-08-30
- **[📋 論述文章，新增] StartupHub.ai：編碼 agent 在資安測試中重複踩到同一批 70 個錯誤模式**：僅標題可用，是否涵蓋 Claude 系列未見報導，詳見「## 技術彙整」

### 2026-08-29
- **[🔴 已確認，升級，新增] Cybernews：Claude Code 已實際執行到惡意程式碼，自行嘗試修復但遭拒絕**：續篇揭露 08-27～08-28 已記錄的 Auto Mode 安全繞過案例中，agent 曾試圖自行修復其執行到的惡意程式碼，但修復動作遭拒絕；具體「被誰／被什麼機制拒絕」未見報導細節，詳見「## 技術彙整」
- **[新增] Alon Hertz（startupfortune.com，經 Hacker News 轉載）：編碼 agent 信任 llms.txt，掃描 6,214 網域發現 120 份檔案指向未註冊套件名稱**：補上具名研究者與方法論，攻擊者可搶注未註冊套件名、待企業 agent 依指示安裝時完成供應鏈感染（詳見「## 技術彙整」懸置標記）
- **[新增] The Register：僅需請 Claude Code 摘要一個網站即可觸發同一信任機制**：將 Alon Hertz 研究中「agent 信任 llms.txt」機制具體聚焦到 Claude Code 本身的最小觸發條件，僅標題與轉址連結可用（詳見「## 技術彙整」懸置標記）
- **[跟進，無新事實，新增] CyberSecurityNews：彙整 AI 基礎設施 RCE、提示注入與 API 金鑰竊取攻擊態勢**：與 08-27 gbhackers 報導高度重疊，未見新事實，詳見「## 技術彙整」

### 2026-08-28（含 08-27 報導）
- **[🔴 已確認，具名研究者＋在野利用雙重確認，新增] embracethered／Simon Willison／Cybernews：Claude Code Opus 5 Auto Mode 安全機制遭繞過，並有實際惡意程式碼利用案例**：資安研究者 embracethered 公布繞過手法，誘使 agent 執行未經授權程式碼；
  - Cybernews 補充至少一起實際利用案例，已從概念驗證進入在野利用，詳見「## 技術彙整」
- **[新增] Ars Technica：Claude、Codex、Hermes 等編碼 agent 在企業網路內安裝來源不明程式碼**：涉及多家廠商的 agent 自動化執行風險（詳見「## 技術彙整」懸置標記）
- **[新增] gbhackers：MCP RCE、盲提示注入與記憶憑證竊取針對 AI 基礎設施**：是否為協定層缺陷或特定實作問題未明（詳見「## 技術彙整」，已查證 2026-09-20：為 LiteLLM 特定實作缺陷 CVE-2026-42271，非 MCP 協定本身問題）
- **[官方一手資料，新增] Wiz：90 天 AI 基礎設施蜜罐遙測數據**：官方部落格公布量化攻擊型態數據（詳見「## 技術彙整」，已查證 2026-09-20：官方未提供百分比統計，僅涵蓋期間與受害系統清單）

### 2026-08-27
- **[產業對照，非 Claude 風險，新增] The Hacker News：Amazon Kiro 提示注入可透過「Kiro Powers」外洩敏感資料**：競品 AI IDE（非 Claude）漏洞揭露，僅標題可用，攻擊鏈細節與是否已修補均未見報導，詳見「## 技術彙整」

### 2026-08-26
- **[教學文章，新增] tech-insider.org：《防範提示注入攻擊 12 步驟，90 分鐘》教學文章**：整理防範提示注入攻擊的 12 個步驟，僅標題可用，未提供具體步驟內容或是否引用具名產品案例，詳見「## 技術彙整」
- **[產業論述，新增] VentureBeat：提示注入在 OWASP 風險排名居首、實際事故紀錄僅列第 12，攻擊難以被掃描偵測**：分析提示注入排名落差與偵測難度，僅標題可用，未提供具體統計數據或方法論，詳見「## 技術彙整」

### 2026-08-23
- **[產業論述，新增] HackerNoon：提示注入攻擊已演化為可達成任意程式碼執行（RCE）的攻擊原語**：一般性論述文章，標題未提及 Claude/Anthropic，僅標題可用，詳見「## 技術彙整」

### 2026-08-22
- **[產業對照，非 Claude 風險，新增] CyberSecurityNews：Grok 遭揭露零點擊攻擊漏洞，攻擊者可透過加密提示注入竊取聊天資料**：xAI 競品 Grok（非 Claude）零點擊攻擊漏洞，攻擊者可用加密提示注入竊取聊天資料；僅標題可用，攻擊鏈細節與修補狀態未見報導；本頁僅留產業對照，不列入母頁「現在還擋不住的攻擊」

### 2026-08-17
- **[新增] World IP Review：提示注入是否成為 AI 商業機密訴訟新戰場**：法律分析文章，探討提示注入攻擊是否將成為企業商業機密訴訟新興爭點，僅標題可用，詳見「## 技術彙整」

### 2026-08-13～08-14
- **Yellow.com：研究稱四大 AI 實驗室採用互不相容的 prompt injection 評測指標**：標題稱四大 AI 實驗室（未指名）評測指標互不相容，防禦成效難以橫向比較（詳見「## 技術彙整」，已查證 2026-09-20：四大實驗室確認為 Anthropic、OpenAI、Google、Meta，原始研究出自 VentureBeat 06-01）

### 2026-08-06～08-07
- **[Claude Code 本身漏洞，僅標題] The Hacker News：Claude Code 與 Gemini CLI 漏洞讓 GitHub Issue 觸及 CI workflow secrets**：本輪唯一直接針對 Claude Code 本身的安全漏洞揭露（Google News／The Hacker News，2026-08-07 08:18 UTC）。
  - ✅ 2026-08-10 查證：即 **CVE-2026-54316**，受影響 0.2.54～2.1.162，**已修補於 2.1.163**；詳見「## 技術彙整」
