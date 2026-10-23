---
page: "entities/claude-duet"
kind: "entity"
type: "product"
status: "active（Research Preview，美國 Pro／Max 候補名單制）"
domain: "🛠️ 工具/功能"
last_updated: "2026-10-23"
last_news_update: "2026-10-23"
status_main: "active"
matrix_role: "產品"
days_since_news: 0
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 0
inbound_links: 3
attribution_count: 8
attribution_last: "2026-10-23"
top_source: "google-news"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Duet

**類型：** product
**狀態：** active（Research Preview，美國 Pro／Max 候補名單制）
**領域：** 🛠️ 工具/功能
**對照角色：** 產品（入口：獨立 app，電腦走網頁；誰起手：它自己判斷）
**別名：** Duet
**首次出現：** 2026-10-21
**最後更新：** 2026-10-23
**最後新聞更新：** 2026-10-23

由 [[entities/opus-5-5|Opus 5.5]] 驅動的主動式 agent，是一個獨立 app（iOS／Android，電腦上走 claude.ai 網頁）：攔截使用者未開口的待辦事項、在背景持續工作，只在需要使用者拍板時才打斷；2026-10-21 以研究預覽開放，美國 Pro／Max 訂閱戶需先加入候補名單。

> **最新動態**（2026-10-23 官方產品頁查證）
> 介面已明朗：Duet 是獨立 app（iOS／Android），電腦上在 claude.ai 網頁開啟，沿用 Claude app 的帳號、記憶、skills 與連接的 app；每天早上主動簡報、發送訊息或付款前會先問。取得方式是**候補名單**，不是開放即用；Team／Enterprise 官方明寫尚未納入。

---

## 現況

官方 2026-10-21 開放 Claude Duet 研究預覽，產品頁文案主打「主動式判斷」（Built for judgment）：先攔截使用者尚未開口的待辦事項、持續在背景工作，只在需要使用者拍板時才打斷，由 Opus 5.5 驅動。目前僅開放美國 Pro、Max 方案的候補名單，官方未提供擴及其他地區或方案的時間表。

**在哪裡用、跟 Claude app 什麼關係（2026-10-23 官方產品頁查證）：** 產品頁寫明「Claude Duet is a standalone app for iOS and Android」，電腦上則在 claude.ai 網頁開啟；未提及 macOS／Windows 桌面版。它沿用使用者既有的 Claude 帳號——Claude app 的記憶、skills 與已連接的 app 從第一則訊息就帶著，所有往來收在同一條對話串，可用文字或語音。產品頁對兩者的區分是：Claude app 等你開對話，Duet 主動來找你。官方稱可接 6,000 個以上的 connectors 與 plugins（頁面示意 Gmail、Google Calendar、Slack、Google Drive、Stripe、Shopify、QuickBooks、HubSpot、Notion、Microsoft 365）。

**現在能不能用：**

| 方案／地區 | 狀態 |
|---|---|
| 美國 Pro／Max | 研究預覽，**需加入候補名單**（產品頁唯一入口是「Join the waitlist」） |
| 其他地區 | 尚未開放，官方未提供時程 |
| Team／Enterprise | 官方明寫「not included yet」 |
| Free | 官方產品頁未列入，暫不可用 |

## 核心功能

- **主動攔截待辦**：官方文案稱會主動理解「什麼需要你注意」，不需使用者先下指令起手。
- **背景持續工作**：使用者離線期間任務持續執行。
- **只在需要時打斷**：每天早上主動簡報並草擬下一步，之後保持安靜，直到工作完成或需要使用者決定時才傳訊息。
- **敏感操作先問**：發送訊息、付款這類動作會先徵詢使用者（產品頁原文：「asks you before sensitive operations like sending messages or paying」）。
- **驅動模型**：Opus 5.5。

> 官方產品頁（2026-10-23 查證）仍未說明：通知走推播還是其他管道、除「發訊息／付款」外哪些操作算敏感、可存取資料的完整權限模型，以及與 Cowork 的任務分工；查到後補充。

## 相關議題

- [[entities/claude-code]]——同屬 Anthropic agent 產品線，OrcaRouter 2026-10-22 評論兩者「同一模型，對『完成』定義不同」（單一媒體觀點，未見官方比較文件）
- [[entities/cowork]]——另一條官方圖形化任務委派產品線，兩者定位差異官方未公開說明
- [[topics/anthropic-agent-stack]]——官方 agent 積木總覽

## 參考來源

- [官方產品頁](https://claude.com/product/claude-duet)（2026-10-21；2026-10-23 再查證介面、候補名單與方案）
- [Reuters（經 Google News）](https://news.google.com/rss/articles/CBMikwFBVV95cUxNRFhacjJyXzZ6ZzNUdkptUDkwRHFyV2pxSXhOc2JucmxQdDJFQ09WZ05DamcxS1NvNUx1b0cyR05DM1U3SzgwdXpvQlhaajl2dHNlVTVlYml2LVhLVENGaWtDbkdMWjFNVkdPMDRTWWFubXJsYkFZQ19peDBLMUI2cXF4cU1hN2lrU2FuZi1wSTRndFU?oc=5)（2026-10-21）

## 歷史記錄

| 日期 | 事件 |
|---|---|
| 2026-10-21 | 官方開放研究預覽，Opus 5.5 驅動，僅美國 Pro／Max 方案可用；Reuters、TechCrunch、VentureBeat、CNBC、The New York Times、The Verge 等多家媒體同日跟進報導。 |
| 2026-10-23 | 官方產品頁查證：獨立 app（iOS／Android，電腦走 claude.ai），取得方式為候補名單，Team／Enterprise 尚未納入。 |
