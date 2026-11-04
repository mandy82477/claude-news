# 第 23 波 proposal-map：anthropic-business＋anthropic-ipo 逐節去向（2026-11-02）

> 行號一律指設計 commit `702e5a6` 的原檔（business 1,048 行／ipo 211 行）。逐行帳在 `<scratchpad>/w23/design/accounting.txt`（`split.py` 斷言兩檔每行恰消費一次），本檔是它的人讀版。
> 去向代號：**母**＝`topics/anthropic-business`；**ipo**＝`topics/anthropic-ipo`（改標題「上市與財報」）；**合作算力**＝`topics/anthropic-partnerships-compute`；**風險**＝`topics/anthropic-business-risks`；**archive**＝`topics/anthropic-business-archive`。

## 一、business 逐節

| 節（原行） | 行數 | 去向 | 改了什麼 |
|---|---|---|---|
| frontmatter、標題、標頭 L1–32 | 32 | 母 | 標題下插使命句（第 7 波定稿＋半句路由）；最後更新 11-02 |
| `%%` 拆頁評估 L33 | 1 | 母 | 改寫為「已拆」一行 |
| callout L35–37 | 3 | 母 | 不動（11-01 ≥ 子樹最新 11-01） |
| 現在的數字：兩段「最新」L43、L45 | 2 | 母 | 改寫：10-26 S-1／10-15 Q3；09-04 段砍（三件事各有家：承銷→ipo 五格、Stripe→風險「商業模式」、開源→風險表） |
| 現在的數字：框句 L47 | 1 | 母 | 「沒有公開財報」改「S-1 已提交未生效、上市前沒有季度財報」 |
| 指標表 L49–60、圖例 L62、備忘 L64 | 15 | 母 | L54 日期統一 10-15；L55 獲利寫明調整後口徑；L56 淨損降級「多家引 S-1」＋非現金句；L58 PBF「撥入全資子實體」 |
| 數字細節 L66–78、L81–96 | 29 | ipo `## 數字細節` | L67 降級、L71 724 億、L73 補營業層與調整後口徑、L74「年增率」→「季增率」、L94 錨點改跨頁、L95 去「讓位」 |
| 數字細節 Accenture L79–80 | 2 | 合作算力「戰略合作細節」 | 照搬，插在 10-19 Bedrock 之後 |
| IPO 走到哪一格 L98–102 | 5 | 母 | 節名保留（ms-ipo 7 筆＋daily 4 筆錨點）；一句改寫 |
| （新）往下鑽：三條子線 | 22 | 母 | 路由表三列＋四個 `####` 指路殼（三個有 daily/ 錨點，永久；一個等 tom-brown 改指後刪） |
| 商業模式 L106–137 | 32 | 風險 `## 商業模式` | L115 改條件句＋（推論） |
| PMF L141–159 | 19 | 風險 | 照搬 |
| 這些數字是誰說的 L163–212 | 50 | 依列分三頁（見第三節） | L189 圖例改寫、L198「IPO 追蹤」表→下方 IPO 細節；表頭、細節頭在三頁各一份；備忘 ipo 照搬、另兩頁新寫一行 |
| 還沒過去的風險 L216–265、L268–282 | 65 | 風險 | 新增一列「上市前的虧損、通路與算力長約」；UTRF 列（L226）讓位、表下一句點名；細節區新增一條、L238 改寫、L242 改指 ipo、「訊 … 追蹤」八條→「… 跟進」、L252 錨點改跨頁 |
| 還沒過去的風險·唱空 L266–267、L283–285 | 5 | ipo `### 誰說撐不住：唱空與質疑` | 照搬；ipo L87／141／177 錨點變頁內 |
| 算力與資金從哪來 L289–328 | 40 | 合作算力 | L296 Nscale 1,030 億一句、L300 SpaceX 後果、L309 AWS 改 S-1 1,100 億、L322 去「一行制」、L324／L326 改寫 |
| 哪個合作會改到你用的 Claude：表與表下 L330–351 | 22 | 合作算力 | L351 資本支出算術改寫（多年總額不比一年營收） |
| 一行制清單 L353–463 | 109 | 合作算力（08–10 月 79 列）／archive（07 月 30 列） | L353 去「一行制」；插 07 月彙整一段（30 筆） |
| 05～06 彙整 L464、備忘 L466 | 2 | 合作算力 | L464 Google 年份改 2026-04-24、去「一行制清單已蒸餾」；L466 備忘更新起點 |
| 戰略合作細節 L468–529 | 62 | 合作算力（50 行）／archive（07 月 12 行） | — |
| 人物 L533–547 | 15 | 母 | 不動（規則改為「子樹內」） |
| 相關實體、參考 L551–569 | 19 | 母 | 不動 |
| 時序 09–11 月 L573–899 | 327 | 依類別歸四頁（第二節） | 照搬；標頭各頁重生 |
| 時序 08 月 L900–1016 | 117 | archive `## 2026-08` | 蒸餾：照搬一字不刪（日標頭降一級）；母頁留 13 行時段總結（≤15） |
| 時序 07／06／06-14 以前總結 L1017–1048 | 32 | 母 | 不動 |
| 砍 | 1 | — | L226 UTRF 風險表列（讓位；細節住 L277–278，該處加 `%%` 註記；無懸置） |

## 二、ipo 逐節（全部留在 ipo）

| 節（原行） | 改了什麼 |
|---|---|
| 標題 L26、使命 L28 | 「Anthropic IPO 追蹤」→「Anthropic 上市與財報」；使命句改寫，互指 market-signals-ipo |
| 怎麼讀 L40 | 改寫：風險的家在 business-risks、判讀在 ms-ipo；保留 `#現在的數字` 錨點 |
| 五格表 L44–54 | 插 `## 上市走到哪一格`；L44「四件事」→五件；L49 時程改寫（⟨Q-03⟩ 改問掛牌日）；L50「10-20 S-1 首度揭露」→外流草稿；L54 下一個時點 |
| 估值算術、結論、資本佈局 L56–63 | L61 結論改寫（S-1 已提交）；L63 錨點改合作算力 |
| （新）誰說撐不住：唱空與質疑 | 收 business L266–267、L283–285 |
| S-1 揭露了什麼 L65–81 | 粗體→`##`；L67 去「anthropic-business 既有條目」；L71 降級＋724 億＋營業層；新增「營業損益口徑」「通路與客戶集中」兩列；L76 補（推論） |
| （新）數字細節、這些數字是誰說的 | 收 business 數字細節與財務 9 列 |
| IPO 細節 L83–204 | 粗體→`##`；錨點 L87／89／92／95／102／107／109／141／161／177 改指；L107 季增；L118 去 ⟨Q-03⟩；L130–131 ⟨Q-03⟩ 改問、複查日 11-10→11-24 |
| （新）時序 | business 09–11 月營收估值群 57 則 |
| 相關頁面 L207–211 | L209 母頁描述、L210 market-signals→market-signals-ipo；加兩新子頁 |

## 三、「這些數字是誰說的」逐列（21 列）與細節（17 行）

| 原行 | 訊號（前 30 字） | 去向 |
|---|---|---|
| L167 | Anthropic 與 Accenture 合計承諾五年至少 | 合作算力 |
| L168 | Futurism：獲利宣稱「未計入模型開發成本」 | ipo |
| L169 | Anthropic 啟動 500 萬美元身心福祉評測獎助計畫 | 合作算力 |
| L170 | CNBC：Anthropic 超越 OpenAI 成最熱門  | ipo |
| L171 | The Information：Anthropic 營收領先 | ipo |
| L172 | OpenAI Q2 業績落後 Anthropic（多來源，含 | ipo |
| L173 | TechRadar：「AI 界的 Apple」定價最高卻拿下 | ipo |
| L174 | Raleigh 合資企業招聘，最高職缺薪資逾 **60 萬美 | 合作算力 |
| L175 | Nvidia 對 Anthropic 等公司合計約 700  | 合作算力 |
| L176 | OpenAI／Anthropic 合計佔「AI 產業」營收  | ipo |
| L177 | Economic Futures Research Fund | 合作算力 |
| L178 | 著作權和解案再添細節：哈利波特出版商獲數百萬美元賠付 | 風險 |
| L179 | 訂閱補貼社群估算 13–40 倍 | 風險 |
| L180 | $30,983 tokens on $200/mo | 風險 |
| L181 | 定價強勢期 | 風險 |
| L182 | 3Q26 獲利 > $10 億美元 | ipo |
| L183 | 著作權集體訴訟 15 億美元和解獲法院核准 | 風險 |
| L184 | 著作權和解案執行細節：91% 賠付申請率、律師費 6.8%、 | 風險 |
| L185 | 著作權和解案讀者反應報導（非新增賠付事實） | 風險 |
| L186 | 未公開獲利時程 | ipo |
| L187 | 「Anthropic Tops $47B」報導；已查證，非新 | ipo |

細節：L194→合作算力、L195→ipo、L196→ipo、L197→ipo、L198→ipo、L199→合作算力、L200→合作算力、L201→ipo、L202→ipo、L203→ipo、L204→合作算力、L205→風險、L206→風險、L207→風險、L208→風險、L209→風險、L210→ipo

## 四、合作清單 07 月 30 列（→ archive `## 2026-07` 末「其餘合作彙整」）

L433、L434、L435、L436、L437、L439、L440、L441、L442、L443、L444、L445、L446、L447、L448、L449、L450、L451、L452、L453、L454、L455、L456、L457、L458、L459、L460、L461、L462、L463

戰略合作細節 07 月 12 條：L517、L518、L519、L520、L521、L523、L524、L525、L526、L527、L528、L529（L522 Amir Salek 是 08 月，留合作算力）

## 五、時序 280 則逐條歸群（groups.py 先看類別標籤、含糊才看標題關鍵詞；設計者覆寫 1 則：L774 Eisman G3→G2，隨唱空細節去 ipo）

| 行 | 月 | 類別 | 群 | 去向 | 標題（前 36 字） |
|---|---|---|---|---|---|
| L576 | 11 | 公司治理 | G2 | ipo | WSJ《Imperial CEO》／HN（13 分）：雙重股權結構讓創辦 |
| L577 | 11 | 商業模式 | G3 | 風險 | Business Insider：按對外收費價格換算，Anthropic |
| L578 | 11 | 戰略合作 | G1 | 合作算力 | The Next Web 引 Stratechery：Palantir  |
| L583 | 10 | 戰略合作 | G1 | 合作算力 | Reuters 引《The Information》：Nvidia 洽談 |
| L586 | 10 | 重大事件 | G1 | 合作算力 | Anthropic：AI for Science 擴大至 20 個基金會 |
| L587 | 10 | 戰略合作 | G1 | 合作算力 | The Paypers：荷蘭金融科技公司 Mollie 推出 AI pl |
| L588 | 10 | IPO 前瞻 | G2 | ipo | Bloomberg：華爾街銀行已撤回一筆與 Anthropic 相關的德 |
| L589 | 10 | IPO 前瞻 | G2 | ipo | Bloomberg Law News：S-1「存在性」AI 風險揭露正設 |
| L592 | 10 | 重大事件 | G1 | 合作算力 | Anthropic／FedScoop：GSA 擴大 OneGov 協議， |
| L593 | 10 | 重大事件 | G1 | 合作算力 | Anthropic 官方：生命科學團隊公開近況，與 BigHat、BMS |
| L594 | 10 | 戰略合作 | G1 | 合作算力 | Endpoints News／R&D World：Anthropic 收 |
| L595 | 10 | 戰略合作 | G1 | 合作算力 | Reuters／Law.com：Anthropic 推出「Claude  |
| L596 | 10 | 戰略合作 | G1 | 合作算力 | Yahoo Finance：資安治理平台 Lumia Security  |
| L599 | 10 | 重大事件 | G2 | ipo | Forbes／The Times of India：S-1 首度揭露 C |
| L600 | 10 | 商業風險 | G3 | 風險 | Fox News／CNBC 引路透社：S-1 揭露一個月訓練暫停與資安事 |
| L601 | 10 | 商業風險 | G3 | 風險 | Business Insurance：Anthropic 警告 AI 相 |
| L602 | 10 | 商業風險 | G3 | 風險 | CNN／WaPo：S-1 近 100 頁風險清單含生物武器、勒索、「AI |
| L603 | 10 | 商業模式 | G3 | 風險 | WSJ：Anthropic 自陳企業 AI 採用仍處「早期階段」 |
| L604 | 10 | IPO 前瞻 | G2 | ipo | Fortune：CFO Krishna Rao 隨 IPO 逼近面臨上任 |
| L605 | 10 | 戰略合作 | G1 | 合作算力 | Reuters：華爾街銀行與 Blackstone 安排 630 億美元 |
| L606 | 10 | 公司治理 | G2 | ipo | Reuters：Anthropic 規劃創辦團隊卸任後仍能監督強大 AI |
| L607 | 10 | 商業風險 | G3 | 風險 | Stanford Daily：點名逾 10 位史丹佛教授著作遭用於訓練  |
| L608 | 10 | 商業模式 | G3 | 風險 | Anthropic 官方隱私文件：商業方案按 👍👎 回報意見或另行同意者 |
| L611 | 10 | IPO 前瞻 | G2 | ipo | Anthropic 官方確認：公開版 S-1 今日正式提交 SEC |
| L612 | 10 | 戰略合作 | G1 | 合作算力 | SpaceX 再借 400 億美元，Anthropic 的運算合作被點名 |
| L613 | 10 | 商業風險 | G3 | 風險 | NYT／衛報／Mashable／Fox News 跟進 Elvis Pr |
| L616 | 10 | 商業風險 | G3 | 風險 | Billboard／Hollywood Reporter：音樂出版商另告 |
| L617 | 10 | 商業風險 | G3 | 風險 | The Information：分析 Anthropic 毛利結構可能成 |
| L620 | 10 | 重大事件 | G1 | 合作算力 | RIABiz：Charles Schwab 原宣布全數 1.6 萬家 R |
| L621 | 10 | IPO前瞻 | G2 | ipo | Yahoo Finance：稱 Anthropic IPO 可能是這波  |
| L624 | 10 | 商業模式 | G3 | 風險 | CTech：Anthropic 擬以約 $345,000 年薪招聘高管溝 |
| L625 | 10 | 戰略合作 | G1 | 合作算力 | Anthropic Blog／Simon Willison：將 Agen |
| L626 | 10 | 戰略合作 | G1 | 合作算力 | Financial Times／SQ Magazine：Anthropi |
| L627 | 10 | 戰略合作 | G1 | 合作算力 | Google Cloud 官方部落格：宣布擴大 Claude 在該平台的 |
| L628 | 10 | 商業模式 | G3 | 風險 | The Guardian：外部學者質疑 Anthropic 10-18  |
| L631 | 10 | IPO前瞻 | G2 | ipo | Yahoo Finance：消息人士稱 Anthropic 最快本週五（ |
| L632 | 10 | 商業風險 | G3 | 風險 | Billboard：音樂出版商 Reservoir 加入控告 Suno  |
| L633 | 10 | 公司觀察 | G3 | 風險 | Yahoo Finance：前 Google 執行長 Eric Schm |
| L636 | 10 | 重大事件 | G2 | ipo | WSJ：Anthropic S-1 首度揭露具體數字，2026 上半年淨 |
| L637 | 10 | 政府採購 | G1 | 合作算力 | FedScoop：HHS 將對 Anthropic 做出「唯一來源」聯邦 |
| L638 | 10 | 商業模式 | G3 | 風險 | MIXED Reality News：Claude API 轉售商現可單 |
| L639 | 10 | 商業風險 | G3 | 風險 | Reuters：Anthropic 與音樂出版商將在 AI 訓練資料訴訟 |
| L642 | 10 | 戰略合作 | G1 | 合作算力 | AWS 官方部落格：Amazon Bedrock 上的 Claude 模 |
| L643 | 10 | 重大事件 | G1 | 合作算力 | CNBC／Reuters／Bloomberg：Anthropic 傳與  |
| L644 | 10 | 公司治理 | G2 | ipo | Quartz／Reuters／Bloomberg：前 Google 執行 |
| L645 | 10 | IPO前瞻 | G2 | ipo | Yahoo Finance：稱 Anthropic 將是 2026 年最 |
| L646 | 10 | IPO前瞻 | G2 | ipo | The Motley Fool：稱 Dario Amodei 的 AI  |
| L647 | 10 | 商業模式 | G3 | 風險 | LA Times：報導稱 SpaceX 與 Anthropic 同步承諾 |
| L648 | 10 | 商業模式 | G3 | 風險 | Fortune／MIXED Reality News：讀完 Claude |
| L651 | 10 | 商業模式 | G3 | 風險 | NBC News／Business Insider：公益基金承諾引發各界 |
| L652 | 10 | IPO前瞻 | G2 | ipo | CNBC：稱 Anthropic 是今年美股 AI 概念股最後一個重大  |
| L653 | 10 | 商業模式 | G3 | 風險 | AI Magazine：綜合報導企業 AI agent 布局，引用估值約 |
| L656 | 10 | 重大事件 | G2 | ipo | Anthropic／Reuters：承諾捐 5% 股權成立 Public |
| L657 | 10 | 重大事件 | G3 | 風險 | Anthropic Research／TechCrunch：官方揭露內部 |
| L658 | 10 | IPO前瞻 | G2 | ipo | Hacker News：紐約市主計官公開信全文曝光，點名白宮自願承諾不足 |
| L659 | 10 | 商業模式 | G3 | 風險 | Financial Times：Anthropic 引入律師團隊，建立讓 |
| L662 | 10 | 戰略合作 | G1 | 合作算力 | Financial Times／Yahoo Finance：Anthro |
| L665 | 10 | 戰略合作 | G1 | 合作算力 | Anthropic Blog／Global News／CBC：EverW |
| L666 | 10 | IPO前瞻 | G2 | ipo | Bloomberg：Anthropic 與本週公開信要求暫緩 IPO 的 |
| L667 | 10 | 重大 | G2 | ipo | Reuters 獨家／Telegraph：投資人討論將 IPO 估值由  |
| L668 | 10 | IPO前瞻 | G2 | ipo | Motley Fool／Yahoo Finance：Anthropic  |
| L669 | 10 | IPO前瞻 | G2 | ipo | Fortune：企業 AI 預算規模可解釋 Anthropic IPO  |
| L670 | 10 | 公司治理 | G2 | ipo | Financial Times／Hacker News：Anthropi |
| L671 | 10 | 商業模式 | G3 | 風險 | Simon Willison：2026 Q1（1–3 月）營收約 $48 |
| L674 | 10 | 重大事件 | G2 | ipo | FT／Bloomberg：Anthropic 揭露 2026 Q3 營收 |
| L675 | 10 | IPO前瞻 | G2 | ipo | Bloomberg：紐約市主計官公開要求 Anthropic 暫緩 IP |
| L676 | 10 | IPO前瞻 | G2 | ipo | BBC：Anthropic 於上市前向潛在投資人進行路演 |
| L677 | 10 | 戰略回顧 | G0 | 母 | BigGo Finance：流出的 Anthropic 五年前內部路線圖 |
| L680 | 10 | 戰略合作 | G1 | 合作算力 | Anthropic 在新加坡開設亞太區第五個辦公室，並與新加坡數位發展與 |
| L681 | 10 | 戰略合作 | G1 | 合作算力 | Tenth Revolution Group 取得 Anthropic  |
| L684 | 10 | 併購 | G1 | 合作算力 | CTech：Amazon 可能以 55 億美元收購 Decart，稱 A |
| L685 | 10 | IPO前瞻 | G2 | ipo | Quartz：Anthropic 舉行第三季財務投資人說明會，為可能的  |
| L686 | 10 | IPO前瞻 | G2 | ipo | CNBC：隨 AI 實驗室財務漸成科技業焦點，Anthropic 擬揭露 |
| L689 | 10 | 戰略合作 | G1 | 合作算力 | WSJ：共同創辦人 Tom Brown 利用共和黨人脈牽線促成每月 $1 |
| L692 | 10 | 商業風險 | G3 | 風險 | The Register：Microsoft 與 Anthropic 就 |
| L695 | 10 | IPO前瞻 | G2 | ipo | Bloomberg：IPO 投資人設法替「失控 AI 風險」定價 |
| L696 | 10 | 戰略合作 | G1 | 合作算力 | DevOps.com：Aditi Consulting 達成 Anthr |
| L697 | 10 | 戰略合作 | G1 | 合作算力 | PR Newswire：Hexaware 成為 Anthropic Pr |
| L698 | 10 | 戰略合作 | G1 | 合作算力 | Techzine Global：OutSystems Agent Exp |
| L699 | 10 | 戰略合作 | G1 | 合作算力 | TradingView：Anthropic 承諾投入 1.5 億美元支持 |
| L700 | 10 | 戰略合作 | G1 | 合作算力 | ET Entrepreneur：Anthropic 向印度新創提供最高  |
| L703 | 10 | IPO前瞻 | G2 | ipo | CNBC：分析師稱 Anthropic 將是今年「最荒謬的 IPO」 |
| L704 | 10 | IPO前瞻 | G2 | ipo | Reuters：Haiku 5.5 發布框進「IPO 前擴充產品線」敘事 |
| L705 | 10 | 戰略合作 | G1 | 合作算力 | The Next Web／9to5Mac：xAI 旗下 Grok Bot |
| L706 | 10 | 戰略合作 | G1 | 合作算力 | TechPowerUp：三星晶圓代工將以 2 奈米製程生產 Anthro |
| L707 | 10 | 戰略合作 | G1 | 合作算力 | Yahoo Finance／GlobeNewswire：Anthropi |
| L710 | 10 | 商業風險 | G3 | 風險 | Financial Times：華爾街銀行啟動 600 億美元晶片融資案 |
| L711 | 10 | 商業模式 | G3 | 風險 | SemiAnalysis：Anthropic 訂閱方案提供的價值為 Op |
| L712 | 10 | 公司治理 | G2 | ipo | Reuters 獨家：Dario Amodei 去年薪酬 1,800 萬 |
| L713 | 10 | 商業風險 | G3 | 風險 | BBC 原始報導 10-06 於 HN 累積 12 分 |
| L716 | 10 | 商業風險 | G3 | 風險 | The Information：Meta、Microsoft 持續要求員 |
| L717 | 10 | 商業風險 | G3 | 風險 | BBC：五角大廈在列入黑名單後已停用 Anthropic 的 AI 工具 |
| L718 | 10 | IPO前瞻 | G2 | ipo | CNN：儘管市場降溫疑慮，投資人圈仍預期 Anthropic 推進 IP |
| L719 | 10 | IPO前瞻 | G2 | ipo | Morningstar／PitchBook：洩露財報顯示成長快，但撐不起 |
| L720 | 10 | 戰略合作 | G1 | 合作算力 | Channel Dive：Anthropic 與 AWS 攜手加碼推動  |
| L723 | 10 | 戰略合作 | G1 | 合作算力 | Barchart：SpaceX 與 Anthropic 簽署大型 AI  |
| L726 | 10 | 戰略合作 | G1 | 合作算力 | Anthropic 推出 Claude Frontier Academy |
| L727 | 10 | 戰略合作 | G1 | 合作算力 | Frontier Academy 的名單與媒體讀法 |
| L730 | 10 | 生態合作 | G1 | 合作算力 | Blocks & Files：Commvault AgentRecove |
| L731 | 10 | 商業風險 | G3 | 風險 | CRN：VMware 夥伴 11:11 的 CRO 評 Broadcom |
| L732 | 10 | IPO前瞻 | G2 | ipo | Financial Times：「Why does Anthropic' |
| L733 | 10 | 戰略合作 | G1 | 合作算力 | TechRepublic：Claude for Government 全 |
| L734 | 10 | 商業風險 | G3 | 風險 | Broadcom 啟動 600 億美元債務融資支應 Anthropic  |
| L737 | 10 | 戰略合作 | G1 | 合作算力 | Claude for Government 09-30 對聯邦與州政府機 |
| L738 | 10 | 戰略合作 | G1 | 合作算力 | Barclays 擴大導入 Claude Code 全行，目標 2026 |
| L739 | 10 | 商業風險 | G3 | 風險 | Reuters 獨家：Broadcom 考慮貸款 Anthropic 最 |
| L740 | 10 | 戰略合作 | G1 | 合作算力 | The Decoder：Anthropic 持續拓展聯邦文職機關採用，五 |
| L741 | 10 | IPO前瞻 | G2 | ipo | Hacker News（67 分）：John Gruber 評論 Ant |
| L742 | 10 | 生命科學布局 | G1 | 合作算力 | Endpoints News：專訪 Anthropic 生命科學團隊，談 |
| L747 | 09 | IPO前瞻 | G2 | ipo | calcalistech：Anthropic 近半營收來自 Amazon |
| L748 | 09 | 戰略合作 | G1 | 合作算力 | AWS 官方部落格：Amazon Bedrock 新增首爾、新加坡境內推 |
| L749 | 09 | 生態合作 | G1 | 合作算力 | EIN News：Pureinsights Discovery 2.12 |
| L752 | 09 | IPO前瞻 | G2 | ipo | Reuters 獨家：機密 IPO 招股書內容外流，揭露鉅額虧損、高速營 |
| L753 | 09 | 戰略合作 | G1 | 合作算力 | Fierce Healthcare：OpenEvidence 偕 Pen |
| L754 | 09 | 戰略合作 | G1 | 合作算力 | Bloomberg：避險基金 ExodusPoint 加入與 Anthr |
| L755 | 09 | 公司動態 | G1 | 合作算力 | The Boston Globe：地方媒體角度回顧 Anthropic- |
| L758 | 09 | 定價 | G3 | 風險 | Anthropic 官方：Claude Sonnet 5.5 上線，取代 |
| L759 | 09 | IPO前瞻 | G2 | ipo | Reuters 將 Sonnet 5.5 上線與 Anthropic I |
| L760 | 09 | 生態合作 | G1 | 合作算力 | 官方推出 Claude Marketplace，收錄逾 2,000 個  |
| L763 | 09 | 商業風險 | G3 | 風險 | 上訴法院維持五角大廈認定 Anthropic 為政府採購供應鏈風險 |
| L764 | 09 | 戰略合作 | G1 | 合作算力 | Yahoo Finance：分析 Accenture 能否把加入 Ant |
| L767 | 09 | 生命科學布局 | G1 | 合作算力 | the-scientist.com 揭露 Anthropic 保密中的「 |
| L768 | 09 | 戰略合作 | G1 | 合作算力 | Bloomberg：Anthropic 與 Akamai 簽署 7 年、 |
| L771 | 09 | 戰略合作 | G1 | 合作算力 | BioSpace：AI 製藥新創 Basecamp 獲 NVIDIA、A |
| L772 | 09 | 戰略合作 | G1 | 合作算力 | 9to5mac.com：Adobe 把 Acrobat 帶進 Claud |
| L773 | 09 | 勞工政策 | G0 | 母 | thecrimson.com：Anthropic 首席經濟學家表示公司正 |
| L774 | 09 | 商業風險 | G2 | ipo | Yahoo Finance：Steve Eisman 稱 AI CEO  |
| L775 | 09 | 估值敘事 | G2 | ipo | Yahoo Finance：SpaceX、OpenAI、Anthropi |
| L778 | 09 | 定價 | G3 | 風險 | Anthropic 官方：Claude Opus 5.5 發布，$4/$ |
| L779 | 09 | 戰略合作 | G1 | 合作算力 | Reuters 獨家：Anthropic 與醫療 AI 服務 OpenE |
| L780 | 09 | 戰略合作 | G1 | 合作算力 | GeekWire／About Amazon：Amazon 開放賣家工具予 |
| L781 | 09 | 資本支出 | G1 | 合作算力 | The Information：Anthropic 洽談加強對更多資料中 |
| L782 | 09 | IPO前瞻 | G2 | ipo | Bloomberg：IPO 計畫生變，市場情緒受衝擊 |
| L785 | 09 | 商業風險 | G3 | 風險 | Hacker News（32 分）＋AP News：反壟斷合謀訴訟原告身 |
| L786 | 09 | 戰略合作 | G1 | 合作算力 | Yahoo Finance：Palo Alto Networks 推出結 |
| L787 | 09 | 產品影響力 | G0 | 母 | the-decoder.com：Anthropic 稱 Claude 協 |
| L788 | 09 | 商業風險 | G3 | 風險 | Bloomberg：報導聚焦新創因 OpenAI、Anthropic 成 |
| L791 | 09 | 資本支出 | G1 | 合作算力 | Bloomberg：Nscale 總值 1,030 億美元資料中心合約中 |
| L792 | 09 | 生命科學布局 | G1 | 合作算力 | Channel 3000／80 Level 跟進 09-18 已記錄之自 |
| L793 | 09 | 戰略合作 | G1 | 合作算力 | The Information：OpenAI 與 Anthropic 傳 |
| L794 | 09 | 產品策略 | G3 | 風險 | citybiz：Anthropic 據報考慮推出新款 Claude 模型 |
| L795 | 09 | 財務評論 | G2 | ipo | Financial Times（Lex 專欄）：Anthropic 估值 |
| L798 | 09 | 重大事件 | G1 | 合作算力 | Anthropic 宣布 Accenture 出任首位「內嵌評估者」，獨 |
| L799 | 09 | 商業風險 | G3 | 風險 | The Hill、Politico、Bloomberg Law News |
| L800 | 09 | IPO前瞻 | G2 | ipo | NYT：Anthropic 積極籌備 IPO，儘管公司過去屢次就 AI  |
| L801 | 09 | 生命科學布局 | G1 | 合作算力 | TechCrunch、Yahoo Finance 跟進 09-18 已記 |
| L804 | 09 | 生命科學布局 | G1 | 合作算力 | 官方：推出生命科學驗證計畫（LSVP），開放生醫專業人士使用 Mytho |
| L805 | 09 | 生命科學布局 | G1 | 合作算力 | Reuters 獨家＋qz.com 跟進：Anthropic 悄悄設立自 |
| L807 | 09 | 資本支出 | G1 | 合作算力 | CNBC 引述消息人士：Anthropic 與 OpenAI 同步尋求規 |
| L810 | 09 | 生命科學布局 | G1 | 合作算力 | 官方部落格：說明 Claude 在生物分子建模的應用進展，與同期生命科學 |
| L811 | 09 | 商業風險 | G3 | 風險 | The New Stack：Claude Code Projects 多 |
| L812 | 09 | 產品策略 | G3 | 風險 | Claude Cowork 與 chat 合併為單一 Claude，同步 |
| L813 | 09 | 產品策略 | G3 | 風險 | 媒體框架：Axios 稱衝擊 Microsoft、Fortune 稱意在 |
| L814 | 09 | IPO前瞻 | G2 | ipo | euronews／Barron's：私募市場為 Anthropic 開出 |
| L815 | 09 | 基礎設施 | G1 | 合作算力 | TechCrunch：Google、Nvidia、Anthropic 支 |
| L818 | 09 | 戰略合作 | G1 | 合作算力 | Reuters／Bloomberg／WSJ／politico.eu：No |
| L819 | 09 | 基礎設施 | G1 | 合作算力 | finance.yahoo.com：Anthropic 簽署首份澳洲資料 |
| L821 | 09 | 市場策略 | G3 | 風險 | Business Insider：Anthropic 全力衝刺把 Cla |
| L822 | 09 | 商業風險 | G3 | 風險 | Dealroom（2 源）：開發者把 Claude Code 導向非 A |
| L825 | 09 | 戰略合作 | G1 | 合作算力 | Reuters 等 7+ 家財經媒體：Anthropic 定名並推出「C |
| L826 | 09 | 分析評論 | G1 | 合作算力 | RIABiz：分析師對 Schwab 卡位效果意見分歧 |
| L827 | 09 | 財務狀況 | G2 | ipo | Futurism：批評「連續第二季獲利」說法未計入模型開發成本 |
| L830 | 09 | 財務狀況 | G2 | ipo | Reuters 引 FT：Anthropic 向投資人表示將連續第二季獲 |
| L831 | 09 | 戰略合作 | G1 | 合作算力 | Bloomberg／Business Wire／Yahoo Financ |
| L832 | 09 | 產品線擴張 | G3 | 風險 | TestingCatalog AI News：據報 Anthropic  |
| L833 | 09 | 商業風險 | G3 | 風險 | The Information：Nvidia、Palantir、Booz |
| L835 | 09 | 公司動態 | G1 | 合作算力 | ChannelE2E：Claude 合作夥伴訓練計畫新增安全性相關認證課 |
| L838 | 09 | IPO 前瞻 | G2 | ipo | Reuters 獨家：Nvidia 洽談投資 Anthropic 鉅額  |
| L839 | 09 | 商業風險 | G3 | 風險 | DefenseScoop：美國國防部計畫十月前將全部機密 AI 工作負載 |
| L840 | 09 | IPO 前瞻 | G2 | ipo | ESG Dive：以 [[entities/joe-benton／Joe |
| L841 | 09 | IPO 前瞻 | G2 | ipo | Morningstar：〈Trustworthy AI〉專文說明投資人評 |
| L844 | 09 | 公司動態 | G0 | 母 | The Boston Globe：Anthropic 在麻州劍橋 Ken |
| L845 | 09 | 公司動態 | G3 | 風險 | NDTV Profit：報導稱 Anthropic 警告至 2030 年 |
| L846 | 09 | 戰略合作 | G1 | 合作算力 | Fable 5.1 已進 FedRAMP High 版 Claude f |
| L849 | 09 | 商業風險 | G3 | 風險 | Verge／Startup Fortune／The New Stack  |
| L850 | 09 | 商業風險 | G3 | 風險 | TechCrunch／Startup Fortune：駭客可在不竊取密碼 |
| L851 | 09 | 戰略合作 | G1 | 合作算力 | Crowdfund Insider：Anthropic 推出 Claud |
| L852 | 09 | 戰略合作 | G1 | 合作算力 | citybiz：LoanPro 採用 AWS＋Claude AI 原生客 |
| L853 | 09 | 戰略合作 | G1 | 合作算力 | Aviation Week：跟進報導 Amadeus 與 Anthrop |
| L854 | 09 | 戰略合作 | G1 | 合作算力 | Demand Gen Report：Salesforce 與 Anthr |
| L855 | 09 | 公司動態 | G0 | 母 | NPR：Anthropic 推出新模型，用於測試 AI 對美國經濟的可能 |
| L858 | 09 | 戰略合作 | G1 | 合作算力 | PYMNTS 等多家媒體：Anthropic 撤回收購以色列新創 Dec |
| L859 | 09 | IPO 前瞻 | G2 | ipo | Yahoo Finance：IPO 延至十月 |
| L860 | 09 | IPO 前瞻 | G2 | ipo | Banking Exchange：就潛在 2 兆美元 IPO 案即將敲定 |
| L861 | 09 | IPO 前瞻 | G2 | ipo | Yahoo Finance＋FT：Anthropic、OpenAI 尋求 |
| L863 | 09 | 公司動態 | G0 | 母 | Fast Company：Anthropic 名列 2026 年最適合創 |
| L866 | 09 | IPO 前瞻 | G2 | ipo | Forbes：IPO 延至 10 月中，同步鎖定 150 億美元信用額度 |
| L867 | 09 | 財務狀況 | G2 | ipo | The Information：11 個月內累計談成算力交易合計 5,1 |
| L868 | 09 | 戰略合作 | G1 | 合作算力 | Currently.com：Anthropic 對 AWS 承諾金額已逾 |
| L869 | 09 | 戰略合作 | G1 | 合作算力 | AI Magazine：Fluidstack 主導 Anthropic  |
| L870 | 09 | 戰略合作 | G1 | 合作算力 | Yahoo Finance：Hut 8 藉 350 億美元 Anthro |
| L871 | 09 | 商業風險 | G3 | 風險 | NDTV／TechCrunch：出版商、經紀人與作者陣營為 15 億美元 |
| L872 | 09 | 商業風險 | G3 | 風險 | Yahoo Finance：五角大廈維持 Anthropic 採購黑名單 |
| L873 | 09 | 公司動態 | G0 | 母 | EdTech Innovation Hub：Anthropic 首度對外 |
| L874 | 09 | 公司動態 | G0 | 母 | Business Insider（3 個獨立來源同步轉載）：一支小型 A |
| L875 | 09 | IPO 前瞻 | G2 | ipo | Morningstar：分析文章稱 Anthropic IPO 規模龐大 |
| L878 | 09 | IPO 前瞻 | G2 | ipo | calcalistech／ETF Trends：兩則標題方向矛盾——「I |
| L881 | 09 | 商業風險 | G3 | 風險 | NYT：企業界正轉向開源模型，分流 OpenAI／Anthropic 訂 |
| L882 | 09 | 商業模式 | G3 | 風險 | The Information：Anthropic 自建支付技術，傳分食 |
| L885 | 09 | IPO 前瞻 | G2 | ipo | FT／NYT：Anthropic 傳洽談由 Morgan Stanley |
| L886 | 09 | 戰略合作 | G1 | 合作算力 | Skift：Amadeus 將旅遊科技整合進 Claude Code 與 |
| L889 | 09 | 戰略合作 | G1 | 合作算力 | Anthropic 官方部落格：推出 Enterprise Fronti |
| L890 | 09 | 戰略合作 | G1 | 合作算力 | AWS 官方部落格：Claude Fable 5.1 上線 AWS 平台 |
| L891 | 09 | 商業風險 | G3 | 風險 | 24/7 Wall St.：質疑 Nvidia-Lambda-Anthr |
| L892 | 09 | IPO 前瞻 | G2 | ipo | Stocktwits：分析師稱 Anthropic 需達微軟等級 70% |
| L895 | 09 | 戰略合作 | G1 | 合作算力 | 多家媒體：Anthropic 與 Lambda 簽署 350 億美元雲端 |
| L896 | 09 | 戰略合作 | G1 | 合作算力 | crn.com：Claude 認證累計 8.5 萬張，Anthropic |
| L897 | 09 | 戰略合作 | G1 | 合作算力 | Morningstar：Trifecta Technologies 與  |
| L898 | 09 | 商業風險 | G3 | 風險 | Sony、Warner Chappell 等音樂出版商正式提告 |
| L903 | 08 | 戰略合作 | G1 | archive | Seeking Alpha：Amazon 將 OpenAI、Meta、A |
| L904 | 08 | 戰略合作 | G1 | archive | EdTech Innovation Hub：Anthropic 開放美國 |
| L905 | 08 | 商業風險 | G3 | archive | technology.org／The Guardian：Sony、War |
| L906 | 08 | 投資人／股權 | G2 | archive | Business Insider：回顧 FTX 案相關人士（Sam Ba |
| L909 | 08 | 商業風險 | G3 | archive | TechCrunch／Business Insider：Sony Mus |
| L910 | 08 | 戰略合作 | G1 | archive | Wccftech：OpenAI 退出與 SpaceX 旗下 Cursor |
| L913 | 08 | 戰略合作 | G1 | archive | Forbes／Financial Times：Anthropic 與英國 |
| L914 | 08 | 戰略合作 | G1 | archive | Yahoo Finance 獨家：Claude 營收年增稱達 1,000 |
| L915 | 08 | 戰略合作 | G1 | archive | 後續報導：Meta 傳將於 Anthropic 支出達 100 億美元 |
| L916 | 08 | 戰略合作 | G1 | archive | WSJ：Salesforce 財報獲利與營收雙雙成長，同步擴大與 Ant |
| L917 | 08 | 戰略合作 | G1 | archive | Yahoo Finance：財經評論員 Jim Cramer 稱 Sal |
| L920 | 08 | IPO/估值敘事 | G2 | archive | Hacker News 雙帖＋Anadolu Ajansı／Moomoo |
| L921 | 08 | 研究資助 | G1 | archive | Anthropic Blog：啟動 500 萬美元獎助計畫，資助 AI  |
| L922 | 08 | 戰略合作 | G1 | archive | Bloomberg：一家與 Anthropic、Google 合作之 A |
| L923 | 08 | 戰略合作 | G1 | archive | ABC News：內部郵件揭露 Anthropic 澳洲 AI 佈局規模 |
| L924 | 08 | 戰略合作 | G1 | archive | ababnews.com：轉載 Anthropic 推出免費「Claud |
| L927 | 08 | 基礎設施擴張 | G1 | archive | KXAN Austin：Anthropic 洽談租用德州 Bastrop |
| L928 | 08 | IPO/估值敘事分歧 | G2 | archive | 24/7 Wall St. 同日刊出兩篇方向相反文章：「意圖超越 Spa |
| L929 | 08 | 治理權分析 | G2 | archive | Bloomberg〈Who Should Control Anthrop |
| L930 | 08 | 企業採用反面訊號 | G3 | archive | cio.com：部分企業對 Anthropic 旗艦模型採用意願不如預期 |
| L933 | 08 | 人才／文化 | G0 | archive | Axios 獨家：Anthropic 面試候選人時會詢問其如何看待「使命 |
| L934 | 08 | 市場滲透 | G1 | archive | Bloomberg.com：Anthropic 表態指出澳洲在 Clau |
| L935 | 08 | 戰略合作 | G1 | archive | EdTech Innovation Hub：Anthropic 推出「C |
| L936 | 08 | 商業風險 | G3 | archive | The Daily Beacon：UT 校內學生報跟進報導 UTRF 專 |
| L937 | 08 | 戰略合作 | G1 | archive | citybiz：轉載 Amir Salek 加入 Anthropic 消 |
| L940 | 08 | IPO 前瞻 | G2 | archive | The New York Times：Anthropic 據傳評估在 I |
| L943 | 08 | IPO 前瞻 | G2 | archive | CNBC（消息人士）：Anthropic IPO 申報文件將把「AI 反 |
| L944 | 08 | IPO 前瞻 | G2 | archive | Financial Times：整理散戶投資人參與 Anthropic  |
| L945 | 08 | 戰略合作 | G1 | archive | Seeking Alpha／Bloomberg（雙重來源確認）：Anth |
| L948 | 08 | IPO 前瞻 | G2 | archive | Bloomberg：Anthropic 據傳預期 IPO 規模將比肩甚至 |
| L949 | 08 | 戰略合作 | G1 | archive | crn.com／Seeking Alpha／The Informatio |
| L950 | 08 | 計費/合規政策 | G3 | archive | 路透社／彭博社（消息人士）：Anthropic 據傳計畫調整企業資料保留 |
| L951 | 08 | 具名企業退出 | G3 | archive | Yahoo Finance：Goldman Sachs、OKX 雙雙於香 |
| L952 | 08 | 財務狀況 | G2 | archive | CNBC：Anthropic 已超越 OpenAI 成為市場最熱門 AI |
| L953 | 08 | 財務狀況 | G2 | archive | The Information：OpenAI 安全政策追上 Anthro |
| L954 | 08 | IPO 前瞻 | G2 | archive | Motley Fool：若 IPO 估值傳聞成真，Amazon 持有 A |
| L955 | 08 | 戰略合作 | G1 | archive | Yahoo Finance：與 Anthropic 相關資料中心取得 1 |
| L958 | 08 | IPO 前置動作 | G2 | archive | Reuters：Anthropic 傳保留創辦人超級投票權 |
| L959 | 08 | IPO 前置動作 | G2 | archive | Bloomberg：Anthropic 上市前信用額度傳擴大至逾 100 |
| L960 | 08 | 商業風險 | G3 | archive | The Hollywood Reporter／Reuters：Round |
| L961 | 08 | 財務狀況 | G2 | archive | WSJ／CoinDesk／SiliconANGLE：OpenAI 第二季 |
| L962 | 08 | 具名企業/機構採用 | G1 | archive | Payward 採用 Claude Mythos 5；Duke Univ |
| L965 | 08 | IPO 前瞻／財務狀況 | G2 | archive | Bloomberg、Reuters、CNBC、Benzinga：Anth |
| L966 | 08 | 財務狀況 | G2 | archive | TechRadar／Hacker News（22 分）：Anthropi |
| L967 | 08 | 商業風險 | G3 | archive | The Information：探討 Anthropic、OpenAI  |
| L970 | 08 | IPO 前瞻 | G2 | archive | Reuters 獨家：IPO 估值取決於 2028 年 $190–200 |
| L971 | 08 | 財務狀況 | G2 | archive | Yahoo Finance：2026 Q2 營收超過 $115 億美元 |
| L972 | 08 | IPO 前瞻 | G2 | archive | Forbes：以 2 兆美元估值切入討論 AI 泡沫疑慮 |
| L973 | 08 | 財務狀況 | G2 | archive | Business Journals：Anthropic 合資企業於 Ra |
| L976 | 08 | IPO 前瞻 | G2 | archive | CNBC（雙重來源確認）：CFO Krishna Rao 已展開早期 I |
| L977 | 08 | IPO 前瞻 | G2 | archive | Gizmodo：投資人評估估值上看 2 兆美元 |
| L980 | 08 | 戰略合作 | G1 | archive | Bloomberg、Reuters、calcalistech、Gizmo |
| L981 | 08 | IPO 前瞻 | G2 | archive | PYMNTS、Financial Times（雙重來源確認）、WSJ：A |
| L982 | 08 | 財務分析 | G2 | archive | Yahoo Finance：Nvidia 對 OpenAI、Anthro |
| L985 | 08 | 戰略合作 | G1 | archive | Anthropic 與 Riot Platforms 簽署 20 年、9 |
| L986 | 08 | 戰略合作 | G1 | archive | 南韓 Naver 投資 Anthropic 700 萬美元 |
| L987 | 08 | IPO 前瞻 | G2 | archive | WSJ：Anthropic IPO 前設法穩固投資人信心 |
| L988 | 08 | 戰略合作 | G1 | archive | VentureBeat：AWS Continuum 整合 Codex 與 |
| L991 | 08 | 戰略合作 | G1 | archive | Google News／Yahoo Finance：Anthropic  |
| L992 | 08 | 財務狀況 | G2 | archive | Hacker News 論戰：OpenAI／Anthropic 合計佔  |
| L993 | 08 | 基礎設施投資規模 | G1 | archive | ] 移入] SemiAnalysis（經 Stocktwits 轉引）： |
| L1000 | 08 | 新事業/人才佈局 | G1 | archive | Anthropic 任命 Robert Mahari 出任新設「Clau |
| L1001 | 08 | 法律風險 | G3 | archive |  |
| L1004 | 08 | 重大 | G1 | archive | Anthropic 正式證實成立內部晶片設計團隊 |
| L1005 | 08 | 戰略合作 | G1 | archive | Millennium 與 Anthropic 合作開發 AI 風險分析師 |
| L1006 | 08 | 戰略合作 | G1 | archive | AWS 攜手 Anthropic、OpenAI 推出 AWS Conti |
| L1007 | 08 | 企業採用 | G1 | archive | Syracuse University 擴大 Claude Enterp |
| L1010 | 08 | 戰略合作 | G1 | archive | Anthropic 與新創雲端運算商 Volta 簽署 100 億美元運 |
| L1011 | 08 | 戰略合作 | G1 | archive | SpaceX 財報揭露 Anthropic／Google 運算合作推升營 |
| L1012 | 08 | 企業採用 | G1 | archive | Fierce Biotech 二次報導 ICON 與 Anthropic |
| L1015 | 08 | 戰略合作 | G1 | archive | Morgan Stanley 領投 150 億美元 Anthropic  |

## 六、cell 閘搬家逐筆（`moves.py --md` 原樣；本機 `--allow-grow` 用）

cell：改後子樹命中 46；配回改前基線 46（其中換了頁名 46）；配不回（新寫或改長）0；改前槽位未用 28
| # | 新頁 | 行 | 類型 | 錨點 | 長度 | 原頁基線上限 |
|---|---|---|---|---|---|---|
| 1 | anthropic-business-risks | 93 | list_item | 企業轉向開源模型分流訂單 | 277 | topics/anthropic-business 277 |
| 2 | anthropic-business-risks | 96 | list_item | Nvidia-Lambda-Anthro | 405 | topics/anthropic-business 405 |
| 3 | anthropic-business-risks | 98 | list_item | Claude 浮水印被繞過 | 291 | topics/anthropic-business 291 |
| 4 | anthropic-business-risks | 99 | list_item | 音樂出版商著作權訴訟 | 377 | topics/anthropic-business 377 |
| 5 | anthropic-business-risks | 100 | list_item | 音樂訴訟升級：Sony Music、Wa | 704 | topics/anthropic-business 704 |
| 6 | anthropic-business-risks | 107 | list_item | 專利侵權訴訟（UTRF） | 212 | topics/anthropic-business 212 |
| 7 | anthropic-business-risks | 108 | list_item | 田納西大學提告（併入上列） | 268 | topics/anthropic-business 268 |
| 8 | anthropic-business-risks | 189 | list_item | 哈利波特出版商獲數百萬美元賠付 | 346 | topics/anthropic-business 346 |
| 9 | anthropic-business-risks | 191 | list_item | 著作權和解案執行細節 | 203 | topics/anthropic-business 203 |
| 10 | anthropic-ipo | 69 | list_item | 創投人士質疑 IPO 前景 | 232 | topics/anthropic-business 232 |
| 11 | anthropic-ipo | 71 | list_item | 知名放空投資人唱空估值敘事 | 232 | topics/anthropic-business 232 |
| 12 | anthropic-ipo | 145 | list_item | The Information | 229 | topics/anthropic-business 229 |
| 13 | anthropic-ipo | 146 | list_item | OpenAI Q2 業績落後 Anthr | 487 | topics/anthropic-business 487 |
| 14 | anthropic-ipo | 147 | list_item | TechRadar：「AI 界的 App | 429 | topics/anthropic-business 430 |
| 15 | anthropic-ipo | 151 | list_item | 「Anthropic Tops $47B | 299 | topics/anthropic-business 299 |
| 16 | anthropic-partnerships-compute | 212 | list_item | Enterprise Frontier  | 800 | topics/anthropic-business 800 |
| 17 | anthropic-partnerships-compute | 214 | list_item | AWS 官方公告 Claude Fabl | 276 | topics/anthropic-business 276 |
| 18 | anthropic-partnerships-compute | 216 | list_item | Lambda（09-01 交易，09-0 | 526 | topics/anthropic-business 526 |
| 19 | anthropic-partnerships-compute | 219 | list_item | Amazon AWS GovCloud（ | 340 | topics/anthropic-business 340 |
| 20 | anthropic-partnerships-compute | 220 | list_item | Claude for Teachers  | 364 | topics/anthropic-business 364 |
| 21 | anthropic-partnerships-compute | 221 | list_item | Nscale（08-28） | 271 | topics/anthropic-business 271 |
| 22 | anthropic-partnerships-compute | 222 | list_item | Claude 營收年增 1,000%（0 | 235 | topics/anthropic-business 235 |
| 23 | anthropic-partnerships-compute | 223 | list_item | Meta（$100 億美元支出，08-2 | 217 | topics/anthropic-business 217 |
| 24 | anthropic-partnerships-compute | 224 | list_item | Salesforce（Claudefor | 356 | topics/anthropic-business 356 |
| 25 | anthropic-partnerships-compute | 225 | list_item | CrowdStrike（08-27） | 233 | topics/anthropic-business 233 |
| 26 | anthropic-partnerships-compute | 226 | list_item | Meta（亦敵亦友，08-27） | 292 | topics/anthropic-business 292 |
| 27 | anthropic-partnerships-compute | 227 | list_item | Anthropic 澳洲市場（08-25 | 275 | topics/anthropic-business 275 |
| 28 | anthropic-partnerships-compute | 228 | list_item | 未具名 AI 資安新創（08-25） | 220 | topics/anthropic-business 220 |
| 29 | anthropic-partnerships-compute | 231 | list_item | UpToDate（08-24） | 292 | topics/anthropic-business 292 |
| 30 | anthropic-partnerships-compute | 235 | list_item | Casper Studios（08-20 | 409 | topics/anthropic-business 409 |
| 31 | anthropic-partnerships-compute | 236 | list_item | Anthropic 關聯資料中心私募信貸 | 351 | topics/anthropic-business 351 |
| 32 | anthropic-partnerships-compute | 237 | list_item | Decart（08-13起多輪跟進） | 727 | topics/anthropic-business 727 |
| 33 | anthropic-partnerships-compute | 239 | list_item | Riot Platforms（08-11 | 306 | topics/anthropic-business 306 |
| 34 | anthropic-partnerships-compute | 243 | list_item | Robert Mahari（08-07） | 308 | topics/anthropic-business 308 |
| 35 | anthropic-partnerships-compute | 244 | list_item | Millennium（08-06） | 269 | topics/anthropic-business 269 |
| 36 | anthropic-partnerships-compute | 245 | list_item | AWS Continuum（08-05） | 399 | topics/anthropic-business 399 |
| 37 | anthropic-partnerships-compute | 254 | list_item | SpaceX（08-04） | 254 | topics/anthropic-business 254 |
| 38 | anthropic-partnerships-compute | 255 | list_item | Google 近 2000 億美元融資機 | 440 | topics/anthropic-business 440 |
| 39 | anthropic-partnerships-compute | 256 | list_item | Anthropic 印度市場（08-03 | 226 | topics/anthropic-business 226 |
| 40 | anthropic-partnerships-compute | 257 | list_item | Morgan Stanley（08-02 | 340 | topics/anthropic-business 340 |
| 41 | anthropic-partnerships-compute | 258 | list_item | Amir Salek（08-21起，08 | 932 | topics/anthropic-business 932 |
| 42 | anthropic-partnerships-compute | 275 | list_item | 身心福祉評測獎助計畫 | 248 | topics/anthropic-business 248 |
| 43 | anthropic-partnerships-compute | 278 | list_item | Economic Futures Res | 355 | topics/anthropic-business 355 |
| 44 | anthropic-partnerships-compute | 460 | list_item | [戰略合作，官方一手來源] Anthro | 251 | topics/anthropic-business 251 |
| 45 | anthropic-partnerships-compute | 464 | list_item | [戰略合作] 多家媒體 | 208 | topics/anthropic-business 208 |
| 46 | anthropic-partnerships-compute | 465 | list_item | [戰略合作] crn.com | 201 | topics/anthropic-business 201 |
reader：改前子樹命中 0、改後 0、改後不在改前（新寫文字）0

