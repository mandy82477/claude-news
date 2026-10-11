---
page: "entities/mythos-archive"
kind: "entity"
status: "resolved（封存頁）"
domain: "🤖 模型"
last_updated: "2026-09-27"
last_news_update: "2026-05-30"
status_main: "resolved"
days_since_news: 134
parent: "entities/mythos"
children: "[]"
page_role: "archive"
days_since_news_subtree: 134
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
# Claude Mythos · 原始條目

**狀態：** resolved（封存頁）
**領域：** 🤖 模型
**上層：** [[entities/mythos]]
**最後更新：** 2026-09-27
**最後新聞更新：** 2026-05-30

> 本頁是原始條目的存放處，重點層見 [[entities/mythos]]。

---

## 2026-04

#### 2026-04-29 / 04-30
Bloomberg / WSJ 報導白宮正式反對擴大 Mythos 存取，聯邦政府首次直接干預。Steve Blank 發文：「我們已打開潘朵拉的盒子」（HN 廣泛討論）。

#### 2026-04-27 / 04-28
The Philosophical Hacker 指出 SWE-bench 方法論循環論證，HN 再次精選持續擴散。IEEE Spectrum 報導：需程式碼隔離、執行沙盒、權限最小化才能安全部署。

#### 2026-04-25
七週測試發現 2,000+ 未知軟體漏洞，大量涉及加密貨幣基礎設施（Fox News / CoinDesk / Crypto Briefing 同步報導）。

#### 2026-04-24
**Mythos 遭未授權存取事件**：Anthropic 已就此發出聲明——「We're investigating a report claiming unauthorised access to Claude Mythos Preview through one of our third-party vendor environments」，並稱**無證據顯示自家系統遭入侵、亦無證據顯示未授權活動擴及該第三方廠商環境之外**。存取管道為一處第三方廠商（vendor）環境；據報導，取得存取的是一個專門關注未發布模型的 Discord 私密社群，多次嘗試後成功並持續使用。當時 Mythos 僅開放少數企業測試（報導點名 Amazon、Apple、JP Morgan Chase）。（[Euronews](https://www.euronews.com/next/2026/04/22/hackers-breach-anthropics-too-dangerous-to-release-mythos-ai-model-report)，2026-04-22 報導／04-24 更新；2026-09-20 查證）

## 2026-05

#### 2026-05-30
Anthropic red team 發布《Measuring LLMs' ability to develop exploits》，公開確認 Mythos Preview 漏洞開發能力是「step-change」，超越所有現有前沿模型。

#### 2026-05-29
Reuters 確認：Anthropic to roll out Claude Mythos in coming weeks（數週內面向公眾推出）。

#### 2026-05-27
印度政府宣布在網路安全計畫中部署 Mythos，首個主權政府採用案例。

#### 2026-05-26
10K–23K 漏洞數字媒體密集報導（Help Net Security / eWeek / PYMNTS / Techzine，數字分歧來自篩選門檻不同）。The Register / Gotrade / CyberSecurityNews 三家媒體同日確認公開釋出路線。

#### 2026-05-25
Anthropic 安全團隊發布 Exploit 評估完整論文（https://red.anthropic.com/2026/exploit-evals/）。Politico 引述美國議會閉門簡報：眾議員 Lou Correa 表示 Mythos 能輕易入侵其銀行帳戶；UK AISI 測試企業網路接管成功率 6/10。The Register 報導 Anthropic 準備釋出 Mythos 等級模型。

#### 2026-05-24
CVD 儀表板正式上線（281 個專案 / 1,596 筆記錄）。Claude Code app 字串洩露：「Access to the Claude Mythos model in Claude Code and Claude Security」，Anthropic 聲明初期仍限制存取。

#### 2026-05-23
Project Glasswing 第一個月報告：約 50 個夥伴、10,000+ 高危漏洞。安全團隊同步發布 Mythos exploit 開發能力評估報告，確認可組合完整攻擊鏈。

#### 2026-05-08
Claude Code CVE-2026-39861（CVSS 7.7）沙箱逃逸漏洞曝光，社群廣泛討論 Mythos 的諷刺性。見 [[topics/ai-agent-safety]]。

#### 2026-05-01
TechCrunch：Sam Altman 批評 Mythos 限制後，旋即宣布 OpenAI GPT-5.5 Cyber 採同策略，僅開放給關鍵防禦者。

## 2026-06

#### 2026-06-29
**美國政府正式許可恢復 Mythos 存取（信任合作夥伴）+ 中國 Z.Ai 聲稱對標**：
- **政府許可進一步確認**：qz.com 報導 Anthropic 正式獲得美國政府許可，可向特定信任合作夥伴恢復 Mythos 存取（[qz.com](https://qz.com/anthropic-mythos-5-clearance-trusted-partners-commerce-062926)）；此為繼 6/27 商務部長 Lutnick 致函後，政府鬆綁政策的進一步落實，Fable 5 全面解禁談判同步推進中
- **中國 Z.Ai 聲稱對標 Mythos**：Reuters 報導（[Reuters](https://www.reuters.com/legal/litigation/chinas-360-says-it-has-developed-tools-match-anthropics-mythos-2026-06-24/)，HN score 8）中國 Z.Ai 與 360 聲稱已開發出可與 Mythos 匹敵的網路安全 AI 模型。**後續（2026-08-26 查證）**：Z.Ai 於 08-14 公布開源 GLM-5.3 的具體數字——CyberGym（審視程式碼、找出並確認真實漏洞）得 **84.5%**，略高於其測得的 Mythos 5 **83.8%**；但在把漏洞轉為可用攻擊的 ExploitBench 僅 **54.4%**，遠低於 Mythos 5 的 **78.0%**。兩家數字**均為自行公布、未經獨立驗證**；GLM-5.3 屬通用編碼模型經擴充後訓練取得資安能力，與 360 專建的 Tulongfeng 路線不同

#### 2026-06-28
**TechCrunch / Mashable 後續確認 Mythos 5 部分解禁 + 競品聲稱對標（Sakana Fugu / WSJ）**：
- **TechCrunch 補充細節**（HN n/a）：補充 Lutnick 致信收件人為 Anthropic **chief compute officer Tom Brown**（TechCrunch 用的是他的現職；他同時是 Anthropic 共同創辦人，見 [[entities/tom-brown]]），確認 100+ 受信任機構範圍含其**非美籍員工**，是兩週禁令後的差異化部分鬆綁（[TechCrunch](https://techcrunch.com/2026/06/26/trump-admin-releases-anthropic-mythos-to-be-used-by-more-than-100-us-companies-agencies/)）；Mashable 同步報導（[Mashable](https://mashable.com/tech/claude-mythos-5-reinstated-by-us-government)）
- **Sakana AI Fugu**：日本 Sakana AI 發布 Fugu，聲稱可與 Fable 5 / Mythos Preview 比肩，支援 multi-agent API 協調其他模型（[TechCrunch](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/)，HN score 256）；與同日中國 360 Tulongfeng 聲明合看，亞洲 AI 新創正以出口禁令空檔加速追趕 Mythos 等級能力
- **WSJ：中國已在網路安全 AI 追上 Anthropic**：WSJ 報導指中國在網路安全 AI 能力上已逼近 Anthropic，Tulongfeng 為代表案例（[WSJ](https://www.wsj.com/tech/ai/chinese-ai-anthropic-mythos-cybersecurity-574b02c2)，Reuters HN score 7）。**後續（2026-08-26 查證）**：360 稱 Tulongfeng 以「AI 模型＋資安資料＋自動化工具」組合達到 Mythos 等級，累計辨識 **3,432 個軟體漏洞、其中 105 個經中國官方確認**；此組數字與「達到 Mythos 等級」的宣稱**皆未經獨立驗證**，本頁不採信為能力對等的證據（同線的 Z.Ai GLM-5.3 數字見 06-29 條目）

#### 2026-06-27
**Mythos 5 部分解禁：美國商務部批准 100+ 機構有限存取**：
- 美國商務部正式批准 Anthropic 向 100+ 美國機構（含企業與聯邦機構）有限釋出 Mythos 5，前提條件為「受信任合作夥伴」認定，並需具備適當安全措施。商務部長 Howard Lutnick 透過致 Anthropic 聯合創辦人 Tom Brown 的信件正式確認此決定（[Semafor](https://www.semafor.com/article/06/27/2026/us-releases-powerful-anthropic-model-mythos-to-some-us-companies)、[CNBC](https://www.cnbc.com/2026/06/26/us-government-anthropic-claude-mythos5-ai.html)）。
- 此為 2026-06-13 出口管制令發布後首次官方鬆綁，Mythos 5 的存取範圍從先前少數 Glasswing 夥伴正式擴展至更廣泛的機構層級；Fable 5 全面解禁仍待談判。

#### 2026-06-24
**AP News：情報機構合作測試發現機密系統漏洞 + 中國 360 聲稱對標工具**：
- **AP News 報導 — 情報機構合作測試**：Anthropic Mythos 在與美國情報機構的授權合作測試中，數小時內發現美國機密系統漏洞；美國官員特別強調「發現」（find）不等於「利用」（exploit），試圖區隔能力確認與惡意使用（[AP News](https://apnews.com/article/anthropic-mythos-ai-classified-systems-vulnerabilities-testing-3e8762c0527c4d8ed657cbe48c84a718)）。此報導與 2026-06-23 Tom's Hardware 引述的 NSA 紅隊測試訊息相互印證，但強調這屬授權合作而非入侵事件
- **中國 360 聲稱對標工具**：Reuters 報導，中國網路安全公司 360 聲稱已開發出對標 Anthropic Mythos 的工具（[Reuters](https://www.reuters.com/legal/litigation/chinas-360-says-it-has-developed-tools-match-anthropics-mythos-2026-06-24/)）；此為繼 Zhipu GLM-5.2 聲明後，第二家中國公司公開宣稱追平 Mythos 的案例，中美 AI 網路安全能力競爭態勢進一步升溫

#### 2026-06-23
**Tom's Hardware：Mythos 紅隊測試數小時內突破 NSA 幾乎所有機密系統 + MIT Technology Review 三點分析**：
- **Tom's Hardware 報導**：Sen. Mark Warner（參議院情報委員會副主席）引述 NSA 局長 Gen. Joshua Rudd 的陳述，確認 Mythos 在紅隊測試中「數小時內突破 NSA 幾乎所有機密系統」。這是迄今最高層級、最具體的政府官員公開陳述，直接解釋出口管制的安全理由，也與 Tom's Hardware 同名報導互相呼應（[Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-powerful-mythos-ai-reportedly-breached-almost-all-nsa-classified-systems-within-a-few-hours-during-red-team-test-report-sheds-more-light-on-the-u-s-governments-sudden-ban-on-the-flagship-models)）
- **MIT Technology Review 三大觀察點**（[MIT Tech Review](https://www.technologyreview.com/2026/06/22/1139424/three-things-to-watch-amid-anthropics-latest-feud-with-the-government/)，2026-06-22）：
  1. **AI 安全定義爭議**：「安全」的定義在 Anthropic（對用戶無害）與政府（對國家安全無害）之間存在根本分歧，是出口管制衝突的深層矛盾
  2. **主權問題**：各國政府越來越關注對本國 AI 基礎設施的主權控制權
  3. **中國競爭窗口**：出口管制期間，Zhipu GLM-5.2 等中國模型加速填補被封鎖市場，管制可能適得其反地擴大中國 AI 的影響力

#### 2026-06-20
**全球媒體持續報導 + 境外付費帳號停用**：
- **國際媒體全面跟進**：Al Jazeera、DW.com、SiliconANGLE、dev.to 同步報導 Fable 5 / Mythos 出口禁令，核心敘事從「美國技術管制」擴大至「盟友間地緣政治緊張」與「AI Kill-Switch」爭議
- **境外付費用戶帳號停用**：確認有非美國 Claude 付費訂閱用戶在管制期間帳號遭停用，Mythos 可及性衝擊擴大至一般訂閱層
- **解禁預期**：承接 Ciauri 2026-06-18 首爾記者會「數日內恢復」聲明，後續見 [[entities/fable-5]]

#### 2026-06-19
**Wired 深度調查確認多重管制動機 + 解禁聲明 + 早期用戶豁免**：
- **SK Telecom 中國關聯確認為根本動機**（Wired HN score 110）：Anthropic 先前授予 SK Telecom 對 Mythos（非 Fable 5）的存取權，美方對 SK Telecom 中國關聯的疑慮是出口管制啟動的真正起點；後 Amazon 研究人員向白宮舉報 Fable 5 越獄漏洞，兩件事疊加加速管制動作，澄清「jailbreak 是唯一原因」的既有說法
- **Ciauri 首爾記者會**：Anthropic 國際總監宣稱「數日內恢復可用」
- **Bloomberg**：部分 Mythos 早期用戶在政府指令後仍保有存取權（早期用戶豁免）
- **Amazon 研究員角色確認**：Amazon 安全研究人員發現 Fable 5 越獄漏洞後直接向白宮通報，是出口管制的直接觸發原因之一（見 2026-06-14 事件記錄）

#### 2026-06-18
**SK Telecom / China 關聯被揭露為出口管制根本起因**：Wired 獨家報導，美國政府對 Anthropic 啟動 Fable 5 / Mythos 出口管制的真正起點，是政府對 SK Telecom 疑似中國關聯的憂慮——Anthropic 先前已授予 SK Telecom 對 Mythos（非 Fable 5）的存取權，此舉令美方官員警惕；後來 Fable 5 的 jailbreak 問題（Amazon 通報白宮）進一步加速了管制動作。此揭露澄清了「jailbreak 是唯一原因」的既有說法，顯示管制動機具有多重層次（Wired）。

#### 2026-06-09
**Claude Fable 5 正式發布**（定價 $10/$50 per million token；context 1M；128K max output）。與 Claude Mythos 5 共用相同模型權重，差異在前置安全分類器——觸發時靜默 fallback 至 Opus 4.8（不到 5% session 受影響）。同日發布的 Claude Mythos 5 為無護欄完整版，僅限授權用戶（政府防禦者、企業安全研究員）存取，定價更高。HN 討論達 2,448 分、近 2,000 評論。Anthropic 同步發布系統卡（含 ASL-4 安全評估框架）。30 天資料保留政策（Fable 5 / Mythos 5 所有流量強制保留 30 天供安全審查，Bedrock 用戶資料離開 AWS 邊界）生效，引發 Bedrock 用戶隱私爭議。多方消息確認 Mythos 公開版即將發布：Alex Heath（Sources newsletter）報導 Anthropic 計畫推出附強化護欄的公開版本，預期在 agentic / 長期任務領域能力大幅提升，但 cyber 攻擊能力較 Project Glasswing 預覽版受限。Reddit 社群在官方公告前即爆料版本名稱可能為「Claude Fable 5」，**該傳聞已由同日官方發布證實**（名稱即 Claude Fable 5；查證 2026-09-13）——這是一起社群爆料先於官方公告且事後被證明準確的案例。此外，Anthropic 研究「Measuring LLMs' impact on N-day exploits」揭示 LLM 已顯著降低 N-day 漏洞利用門檻。

#### 2026-06-08
Dragos（工業網路安全公司）將 Mythos Preview 應用於 OT（營運技術）安全軟體漏洞挖掘，為 Mythos 在企業安全場景的落地新案例。Pentagon 因 Claude「太安全」而尋求替代 AI 方案的報導再次被廣泛引述，Tech Times 報導五角大廈積極評估替代品。

#### 2026-06-05
NSA 使用 Mythos 發動進攻性網路攻擊（FT 獨家，HN 89）。Anthropic 同日開源 `defending-code-reference-harness` 作為防禦工具，呈現「同源攻防」格局。另：Anthropic AI 發現 Zcash Orchard pool 無限偽造漏洞（2022 年起即存在），ZEC 價格暴跌 30%。

#### 2026-06-04
ICE（美國移民海關執法局）加入 Project Glasswing，繼 ENISA 之後的第二個政府機構。

#### 2026-06-03
Project Glasswing 第一批夥伴在 HN（score 176）分享一手使用體驗：假陽性嚴重，訊噪比是核心挑戰。Anthropic 總裁 Daniela Amodei 首度公開表示 Mythos「非常擅長網路戰」，在 $965B IPO 申請背景下引發商業化壓力討論。

#### 2026-06-02
Glasswing 夥伴從 50 擴展至 150 個新組織（共 200 個，15+ 國家）。Anthropic 承諾 6–12 個月內推出公開版本。

#### 2026-06-01
ENISA（歐盟網路安全局）獲准存取，成首個歐洲政府機構。英國銀行同日遭拒，OpenAI 主動提出替代方案——AI 安全能力開始成為地緣政治談判籌碼。The Information 報導授權費被稱「Budget Buster」。
