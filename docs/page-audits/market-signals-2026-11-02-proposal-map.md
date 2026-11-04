> **2026-11-02 註：** 本檔是第一輪提案；評審 🔴1–3 的修正（`check_wiki_freshness.py` 那段 diff 不套、腳本 5 支；歸因只補 Citywire 1 筆、其餘 3 筆網址不在子頁不補）以 `market-signals-2026-11-02-review.md` 與 commit `7ec4d2b` 為準，文中相反的句子作廢。

# 第 22 波逐節去向表：topics/market-signals（2026-11-02）

> 行號指 `wiki/topics/market-signals.md` 在 commit `7dbc92e` 的原檔（1,699 行）。代號：**母**＝`topics/market-signals`、**A**＝`-ipo`、**B**＝`-legal`、**C1**＝`-compute`、**C2**＝`-customers`。
> 逐行保命：`<scratchpad>/w22/design/split.py` 斷言 1–1,699 每行恰消費一次（逐行帳 `accounting.txt`：A 446／B 429／C1 251／C2 457／母 114（含 frontmatter 25）／砍 2）；`verify.py` 另把 1,084 條照搬行逐字比對、懸置標記去 slug 比對 69→69。第二～四節由 `make_map.py` 從 `judgments_g.json`、`accounting.txt`、`split.py` 的 `MS` 清單產生。

## 一、原有各節

| 節（原行） | 去向 | 動了什麼 |
|---|---|---|
| frontmatter L1–25 | 五頁由 gen 重生 | — |
| H1＋標頭 L26–33 | 母 | H1 後插使命句；L31「最後更新」→ 11-02；「最後新聞更新」10-31 不動 |
| 免責 L35–36 | 母 | 原文；四子頁各寫一份同字（daily.md 規定常駐，測試逐頁驗） |
| callout L38–42 | 母 | L39、L42 句尾加「（見 [[子頁]]）」；四子頁各有自己的 callout（附當天歸因網址） |
| 摘要 L46–51 | 母 | 插「現在」段（S-1 已公開、未生效）；L50 時態改「公開版已於 10-26 提交」、「多數日子沒有」→「沒有這種消息的日子」 |
| 買得到的標的 L54–82 | 母 | L76 空行砍（Schwab 列回表內）；其餘原文。L81 MSFT 細節留（事實家該在事實頁 → handoff 3） |
| 近期判讀節頭 L85–89 | 母（同名節改成路由） | 新路由表（四子頁＋教材頁，「最新一則」欄每日覆寫）；L87、L89 原文留作記號說明；原 L1521 圖例改寫搬來；yann-lecun 錨點的同名 h4 殼；新 `### 未歸類` |
| 判讀 88 則 L91–1402 | A 25／B 24／C1 14／C2 25 | 照線別機械歸（第二節逐則）；改字只有照查證的 L181、185、406、447、451、458、459 |
| 回顧結算 L1405–1408 | 母 | L1407 說明原文；其後新合計表（四子頁一列一列＋合計，每週 5h 重寫） |
| 表頭 L1409–1410 | A 原文，B／C1／C2 各一份 | — |
| 結算列 L1411–1500（90 列） | A 25／B 26／C1 14／C2 25 | 照線名歸，與判讀同頁（第三節）；「當時判斷」「催化劑」欄一字不動 |
| L1502 股價半邊說明 | 母 | 跨 A（AMD、SNDK）、C1（BX）、C2（ACN、GOOGL）五個代號，放合計表下 |
| L1504 CRM 結算細節 | C2 | 原文 |
| L1506–1515 10-03 結算細節 | B（L1506–1511：GOOGL、ACN）；C2（L1512–1513 NVO）；C1（L1514–1515 澳洲） | C2、C1 各補一行小標副本（L1506 同字） |
| 里程碑節頭 L1519–1522 | A 原文，B／C1／C2 各一份；L1521 → 母 | L1521 改寫成「登記在該子頁的…」 |
| 里程碑 L1523–1687（86 筆頂層＋續行） | A 23／B 25／C1 13／C2 24 | 第四節逐筆；L1529、1547、1680、1681 照查證改；L1583、1587、1600、1686 補縮排；**L1543 砍（N1）** |
| 分隔 L1688–1690 | 砍 | 與 L1516–1518 重複 |
| 相關實體 L1691–1698 | 母 | 原文 |
| 拆頁評估 L1699 | 母（改寫） | 「已拆」一行：落選、殼、下一次瘦身點（12-01 起蒸 09 月） |

**砍整節：無。** 砍列兩處：L76（表中空行）、L1543（與 L1567 同事實的重複條，無懸置標記，`verify.py` 標記數 69→69 為證）。

**8 筆「沒縮排的續行」逐筆**（裁決 (6)）：L1583、1587、1600、1686 真是上一筆的續行 → 補縮排；L1681 是 L1680 的續行且過時 → 改寫並縮排；L1567、L1576 是獨立的已查證條（粗體開頭、自帶子條）→ 不動；L1543 是 L1567 的重複 → 砍。

## 二、88 則逐則歸群（行號＝判讀標題行；區塊到下一則標題前一行）

| # | 原行 | 判讀日 | 線（第幾則） | 群 | 改了什麼 |
|---|---|---|---|---|---|
| 1 | L91–105 | 10-31 | IPO 進程（第 21 則） | A ipo | — |
| 2 | L106–120 | 10-30 | Nscale 算力合約規模（第 3 則） | C1 compute | — |
| 3 | L121–135 | 10-29 | 德州資料中心債券流標（開線） | C1 compute | — |
| 4 | L136–150 | 10-29 | Financial Advisors 使用額度優惠（開線） | C2 customers | — |
| 5 | L151–165 | 10-29 | Copilot 性價比對標 Claude Code（開線） | C2 customers | — |
| 6 | L166–180 | 10-29 | 內部重建降低運算成本（開線） | C1 compute | — |
| 7 | L181–195 | 10-28 | GSA 政府採購折扣擴大（開線） | B legal | L181、L185 |
| 8 | L196–210 | 10-28 | 生技策略併購（開線） | C2 customers | — |
| 9 | L211–225 | 10-28 | 州層級 AI 監管遊說（開線） | B legal | — |
| 10 | L226–240 | 10-28 | 定價改版（第 6 則） | C2 customers | — |
| 11 | L241–255 | 10-27 | S-1 風險因素揭露（開線） | A ipo | — |
| 12 | L256–270 | 10-27 | S-1 操作風險揭露（開線） | A ipo | — |
| 13 | L271–284 | 10-27 | 晶片商循環融資疑慮（第 4 則） | C1 compute | — |
| 14 | L285–299 | 10-26 | IPO 進程（第 19 則） | A ipo | — |
| 15 | L300–314 | 10-26 | 雲端供應鏈承諾總額（開線） | C1 compute | — |
| 16 | L315–329 | 10-26 | IPO 進程（第 20 則） | A ipo | — |
| 17 | L330–343 | 10-25 | 音樂著作權訴訟（第 2 則） | B legal | — |
| 18 | L344–358 | 10-24 | Schwab RIA 通路准入（開線） | C2 customers | — |
| 19 | L359–372 | 10-24 | AI agent 法律風險（第 3 則） | B legal | — |
| 20 | L373–386 | 10-22 | 音樂著作權訴訟（開線） | B legal | — |
| 21 | L387–401 | 10-21 | IPO 進程（第 18 則） | A ipo | — |
| 22 | L402–416 | 10-20 | IPO 進程（第 17 則） | A ipo | L406 |
| 23 | L417–431 | 10-20 | 聯邦行政機關採用 Claude（開線） | B legal | — |
| 24 | L432–446 | 10-19 | Nscale 算力合約規模（第 2 則） | C1 compute | — |
| 25 | L447–461 | 10-18 | Public Benefit Fund（開線） | A ipo | L447、L451、L458、L459 |
| 26 | L462–476 | 10-19 | 國會AI安全法案遊說（開線） | B legal | — |
| 27 | L477–490 | 10-16 | IPO 進程（第 14 則） | A ipo | — |
| 28 | L491–505 | 10-17 | IPO 進程（第 15 則） | A ipo | — |
| 29 | L506–520 | 10-17 | IPO 進程（第 16 則） | A ipo | — |
| 30 | L521–535 | 10-17 | 私募信貸晶片融資（開線） | C1 compute | — |
| 31 | L536–550 | 10-17 | 具名客戶流失（開線） | C2 customers | — |
| 32 | L551–565 | 10-16 | 企業採用（第 5 則） | C2 customers | — |
| 33 | L566–580 | 10-15 | IPO 進程（第 13 則） | A ipo | — |
| 34 | L581–595 | 10-15 | 聯邦立法機關採用 Claude（開線） | B legal | — |
| 35 | L596–610 | 10-15 | IPO 進程（第 11 則） | A ipo | — |
| 36 | L611–625 | 10-15 | IPO 進程（第 12 則） | A ipo | — |
| 37 | L626–639 | 10-15 | 美國FTC產品風險調查（第 2 則） | B legal | — |
| 38 | L640–654 | 10-13 | 競品定價對標（開線） | C2 customers | — |
| 39 | L655–669 | 10-11 | SpaceX 運算容量交易（開線） | C1 compute | — |
| 40 | L670–684 | 10-10 | AI agent 法律風險（第 2 則） | B legal | — |
| 41 | L685–699 | 10-10 | Claude Startups 新創優惠（開線） | C2 customers | — |
| 42 | L700–714 | 10-09 | Azure Marketplace 轉售帳務爭議（開線） | C2 customers | — |
| 43 | L715–729 | 10-08 | 定價改版（第 5 則） | C2 customers | — |
| 44 | L730–744 | 10-08 | 訂閱方案新增 API credits（開線） | C2 customers | — |
| 45 | L745–759 | 10-07 | 競品採購 Claude API（開線） | C2 customers | — |
| 46 | L760–774 | 10-06 | 訂閱補貼與毛利結構（開線） | C2 customers | — |
| 47 | L775–788 | 10-05 | 晶片商循環融資疑慮（第 3 則） | C1 compute | — |
| 48 | L789–803 | 10-05 | 大型科技公司自建替代（開線） | C2 customers | — |
| 49 | L804–818 | 10-05 | 五角大廈供應鏈風險黑名單（第 2 則） | B legal | — |
| 50 | L819–833 | 10-05 | IPO 進程（第 10 則） | A ipo | — |
| 51 | L834–848 | 10-02 | 晶片商循環融資疑慮（第 2 則） | C1 compute | — |
| 52 | L849–863 | 10-01 | 晶片商循環融資疑慮（開線） | C1 compute | — |
| 53 | L864–878 | 10-01 | 企業採用（第 4 則） | C2 customers | — |
| 54 | L879–893 | 09-30 | 美國FTC產品風險調查（開線） | B legal | — |
| 55 | L894–908 | 09-30 | IPO 進程（第 9 則） | A ipo | — |
| 56 | L909–923 | 09-29 | AI agent 法律風險（開線） | B legal | — |
| 57 | L924–938 | 09-29 | IPO 進程（第 8 則） | A ipo | — |
| 58 | L939–955 | 09-28 | 定價改版（第 4 則） | C2 customers | — |
| 59 | L956–970 | 09-28 | 澳洲參議院AI調查聽證會（第 2 則） | B legal | — |
| 60 | L971–985 | 09-27 | 澳洲參議院AI調查聽證會（開線） | B legal | — |
| 61 | L986–1000 | 09-27 | 定價改版（第 3 則） | C2 customers | — |
| 62 | L1001–1015 | 09-25 | 五角大廈供應鏈風險黑名單（開線） | B legal | — |
| 63 | L1016–1030 | 09-25 | Akamai 算力合約（開線） | C1 compute | — |
| 64 | L1031–1045 | 09-25 | 英國模型審查限制（開線） | B legal | — |
| 65 | L1046–1060 | 09-22 | 定價改版（第 2 則） | C2 customers | — |
| 66 | L1061–1075 | 09-22 | IPO 進程（第 7 則） | A ipo | — |
| 67 | L1076–1090 | 09-22 | 反壟斷訴訟（第 3 則） | B legal | — |
| 68 | L1091–1105 | 09-21 | Nscale 算力合約規模（開線） | C1 compute | — |
| 69 | L1106–1120 | 09-19 | Reddit 資料訴訟（開線） | B legal | — |
| 70 | L1121–1134 | 09-19 | 反壟斷訴訟（第 2 則） | B legal | — |
| 71 | L1135–1149 | 09-19 | 反壟斷訴訟（開線） | B legal | — |
| 72 | L1150–1164 | 09-19 | 安全與治理爭議（第 2 則） | B legal | — |
| 73 | L1165–1179 | 09-17 | 企業採用（第 3 則） | C2 customers | — |
| 74 | L1180–1194 | 09-17 | 定價改版（開線） | C2 customers | — |
| 75 | L1195–1209 | 09-16 | 企業採用（第 2 則） | C2 customers | — |
| 76 | L1210–1224 | 09-16 | 多模型路由收入外流（開線） | C2 customers | — |
| 77 | L1225–1239 | 09-16 | 澳洲算力布局（開線） | C1 compute | — |
| 78 | L1240–1254 | 09-14 | 企業資料疑慮限縮使用（開線） | C2 customers | — |
| 79 | L1255–1269 | 09-12 | 政府客戶流失（開線） | B legal | — |
| 80 | L1270–1283 | 09-12 | IPO 進程（第 6 則） | A ipo | — |
| 81 | L1284–1298 | 09-11 | 安全與治理爭議（開線） | B legal | — |
| 82 | L1299–1313 | 09-09 | 競品估值（開線） | A ipo | — |
| 83 | L1314–1328 | 09-08 | IPO 進程（第 5 則） | A ipo | — |
| 84 | L1329–1342 | 09-07 | IPO 進程（第 4 則） | A ipo | — |
| 85 | L1343–1357 | 09-06 | IPO 進程（第 3 則） | A ipo | — |
| 86 | L1358–1372 | 09-04 | IPO 進程（第 2 則） | A ipo | — |
| 87 | L1373–1387 | 08-26 | 企業採用（開線） | C2 customers | — |
| 88 | L1388–1402 | 08-13 | IPO 進程（開線） | A ipo | — |

## 三、回顧結算 90 列（照線名歸群，與判讀同頁）

- **A ipo**（25 列）：L1411、L1421、L1422、L1424、L1426、L1431、L1432、L1435、L1437、L1438、L1439、L1443、L1445、L1446、L1460、L1465、L1467、L1476、L1490、L1494、L1495、L1496、L1497、L1498、L1500
- **B legal**（26 列）：L1417、L1419、L1427、L1429、L1430、L1433、L1436、L1444、L1447、L1450、L1459、L1464、L1466、L1469、L1470、L1472、L1474、L1477、L1479、L1480、L1481、L1482、L1489、L1491、L1492、L1493
- **C1 compute**（14 列）：L1412、L1413、L1416、L1423、L1425、L1434、L1440、L1449、L1457、L1461、L1462、L1473、L1478、L1487
- **C2 customers**（25 列）：L1414、L1415、L1418、L1420、L1428、L1441、L1442、L1448、L1451、L1452、L1453、L1454、L1455、L1456、L1458、L1463、L1468、L1471、L1475、L1483、L1484、L1485、L1486、L1488、L1499

## 四、追蹤中的里程碑（頂層條目＋其續行；起點→群）

| 起點 | 群 | 標記（標｜查）或條目開頭 |
|---|---|---|
| L1523 | C1 compute | 標 10-29｜查 Texas、bond |
| L1524 | A ipo | 標 10-31｜查 Blackstone、BB 級信評、投資級 |
| L1525 | C1 compute | 標 10-30｜查 Nvidia、信用支持 |
| L1526 | C2 customers | 標 10-29｜查 4,800、Financial Advisors |
| L1527 | C2 customers | 標 10-29｜查 Copilot Fusion、GitHub Copilot |
| L1528 | C1 compute | 標 10-29｜查 Zero-Rust、CPU 消耗 |
| L1529 | B legal | 標 10-28｜查 OneGov、屬地政府 |
| L1530 | C2 customers | 標 10-28｜查 Mithril Medicine、匿名創辦人 |
| L1531 | B legal | 標 10-28｜查 加州州長、法院封鎖 |
| L1532 | C2 customers | 標 10-28｜查 inference_geo、Managed Agents |
| L1533 | A ipo | 標 10-27｜查 Business Insurance、承保能力 |
| L1534 | A ipo | 標 10-27｜查 訓練暫停、資安事件 |
| L1535 | C1 compute | 標 10-27｜查 630 億美元、Blackstone |
| L1536 | A ipo | 標 10-26｜查 承銷商、定價區間 |
| L1537 | C1 compute | 標 10-26｜查 Broadcom、履約時程 |
| L1538 | A ipo | 標 10-26｜查 年化成長、客戶集中度 |
| L1539 | B legal | 標 10-25｜查 Elvis Presley、音樂著作權 |
| L1540 | C2 customers | 標 10-24｜查 Schwab、小型顧問 |
| L1541 | B legal | 標 10-24｜查 alignment-assessment-ukaisi、43 次評估 |
| L1542 | B legal | 標 10-22｜查 Reservoir、Suno |
| L1543 | 砍 | **公開版 S-1 實際於 2026-10-26 提交 SEC，非傳聞的 1… |
| L1544 | A ipo | 標 10-21｜查 SEC EDGAR、807億美元 |
| L1545 | B legal | 標 10-21｜查 sole-source award、FedScoop |
| L1546 | C1 compute | 標 10-20｜查 Nscale、450億美元 |
| L1547–1548 | A ipo | 標 10-18｜查 Public Benefit Fund、股東會表決 |
| L1549 | B legal | 標 10-19｜查 50 人以上死亡、10 億美元損害 |
| L1550–1551 | A ipo | 標 10-17｜查 Telegraph、1.5兆美元 |
| L1552–1553 | A ipo | 標 10-17｜查 Comptroller、展開對話 |
| L1554–1555 | A ipo | 標 10-17｜查 KBRA、EBITDA |
| L1556–1558 | C1 compute | 標 10-17｜查 Blackstone、殖利率 |
| L1559–1560 | C2 customers | 標 10-17｜查 Replit、終止合作 |
| L1561–1562 | C2 customers | 標 10-16｜查 Accenture、支出上限 |
| L1563–1564 | A ipo | 標 10-16｜查 valuation expectations、下修估值 |
| L1565–1566 | B legal | 標 10-16｜查 美國參議院、參議院幕僚 |
| L1567–1571 | A ipo | **公開版 S-1 已於 2026-10-26 提交 SEC**（2026-… |
| L1572–1573 | A ipo | 標 10-15｜查 Comptroller、退休基金 |
| L1574–1575 | C2 customers | 標 10-13｜查 Argon、Vals Index |
| L1576–1579 | C1 compute | **SpaceX 每月 12.5 億美元運算交易已獲證實，「Tom Brow… |
| L1580–1581 | B legal | 標 10-10｜查 PhillyUnsolvedMurders、簽證申請 |
| L1582–1583 | C2 customers | 已查證（2026-10-24，官方計畫頁）｜**Claude Startup… |
| L1584–1585 | C2 customers | 標 10-09｜查 Azure Marketplace、17,600 |
| L1586–1588 | C2 customers | 已查證（2026-10-24，Claude 定價文件、Haiku 5.5 公… |
| L1589 | C2 customers | 已查證（2026-10-24，官方文件）｜**Max／Team 每月 API… |
| L1590–1591 | C2 customers | 標 10-07｜查 Grok、Midjourney、Suno、整合細節 |
| L1592–1593 | C2 customers | 標 10-05｜查 Meta、Microsoft、減少內部使用 |
| L1594–1595 | B legal | 標 10-05｜查 Pentagon、停用工具、GovCloud |
| L1596–1597 | A ipo | 已查證（2026-10-24，Morningstar 轉載 PitchBoo… |
| L1598 | C1 compute | 標 10-02｜查 Broadcom、debt financing、600億 |
| L1599–1601 | C2 customers | 已查證（2026-10-24，SemiAnalysis X 貼文）｜**Se… |
| L1602–1603 | C1 compute | 標 10-01｜查 Broadcom、晶片租賃、循環投資 |
| L1604–1605 | C2 customers | 標 10-01｜查 Barclays、採用率 |
| L1606–1607 | B legal | 標 09-30｜查 Federal Trade Commission、subpoena、investigation scope |
| L1608–1610 | A ipo | 標 09-30｜查 Amazon、Google、customer concentration、calcalistech |
| L1611–1613 | B legal | 標 09-29｜查 rogue AI agents、uncertain legal risk |
| L1614–1616 | A ipo | 標 09-29｜查 Reuters、IPO prospectus、existential risks |
| L1617–1618 | C2 customers | 已查證（2026-10-17，Claude 定價文件）｜**Sonnet 5… |
| L1619–1621 | B legal | 標 09-28｜查 Australian senate、will not attend、October 1 |
| L1622 | B legal | 標 09-27｜查 Australian Senate、AI inquiry、hearing date |
| L1623–1625 | C2 customers | 已查證（2026-10-17，API 發行說明、拒答與備援文件）｜**拒答計… |
| L1626–1627 | B legal | 標 09-26｜查 D.C. Circuit、supply chain risk appeal、Anthropic petition、遷出計畫 |
| L1628–1630 | C1 compute | 標 09-25｜查 Akamai、10-Q、營收指引 |
| L1631–1632 | B legal | 標 09-25｜查 White House、AISI、UK review |
| L1633–1634 | C2 customers | 標 09-23｜查 GPT-6 Sol、毛利率 |
| L1635–1636 | A ipo | 標 09-23｜查 Bloomberg、derailed |
| L1637–1639 | C1 compute | 標 09-21｜查 Nscale、Microsoft、資料中心 |
| L1640–1641 | B legal | 標 09-20｜查 資料爬取、Mashable |
| L1642–1644 | B legal | 標 09-20｜查 書面承認、跨實驗室對話 |
| L1645–1647 | B legal | 標 09-19｜查 反壟斷合謀、collusion、pacing |
| L1648–1650 | B legal | 已查證（2026-10-03，Anthropic）｜**Accenture「… |
| L1651–1653 | C2 customers | 標 09-17｜查 JPMorgan、摩根大通、支出上限 |
| L1654 | C2 customers | 已查證（2026-10-03，Claude 方案與定價）｜**Claude … |
| L1655–1658 | C2 customers | 標 09-16｜查 Novo Nordisk、諾和諾德 |
| L1659–1661 | C2 customers | 標 09-16｜查 Dealroom、token 費用外流 |
| L1662–1666 | C1 compute | 標 09-16｜查 澳洲資料中心、Macquarie |
| L1667–1671 | C2 customers | 標 09-14｜查 Nvidia、Palantir、Booz Allen、資料外洩 |
| L1672 | B legal | 已查證（2026-09-26，DefenseScoop）｜**國防部證實近全… |
| L1673–1674 | A ipo | 標 09-12｜查 Nvidia、認購方、招股文件 |
| L1675 | B legal | 標 09-11｜查 出口管制、國防部 |
| L1676 | B legal | 已查證（2026-09-26，BeInCrypto）｜**Moonshot … |
| L1677 | B legal | 已查證（2026-09-26，CNN）｜**Anthropic 就 Coxo… |
| L1678 | B legal | 標 09-10｜查 American Prospect、監控系統 |
| L1679 | A ipo | 已查證（2026-09-26，TechCrunch）｜**Cognition… |
| L1680–1681 | A ipo | 已查證（2026-09-20，Anthropic 官方部落格＋SEC EDG… |
| L1682–1683 | A ipo | 標 09-04｜查 Morgan Stanley、Goldman Sachs |
| L1684–1686 | A ipo | 標 09-06｜查 calcalistech、IPO延後 |
| L1687 | A ipo | 標 09-08｜查 標普全球、穆迪評等、投資級信評 |
