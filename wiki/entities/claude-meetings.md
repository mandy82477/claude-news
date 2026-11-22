---
page: "entities/claude-meetings"
kind: "entity"
type: "feature"
status: "beta（Team／Enterprise；Auto-join 2026-11-16 起暫停）"
domain: "🛠️ 工具/功能"
last_updated: "2026-11-22"
last_news_update: "2026-11-16"
status_main: "beta"
matrix_role: "功能"
days_since_news: 6
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 6
inbound_links: 8
attribution_count: 1
attribution_last: "2026-11-16"
top_source: "anthropic-status"
pending_count: 2
pending_overdue: 0
pending_next_review: "2026-12-06"
pending_signalled: 0
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude Meetings

Claude 以可見參與者身分加入視訊會議、邊聽邊動手做事的 beta 功能，2026-11-10 起開放 Team／Enterprise。

**類型：** feature
**狀態：** beta（Team／Enterprise；Auto-join 2026-11-16 起暫停）
**領域：** 🛠️ 工具/功能
**對照角色：** 功能（Capabilities；Claude 進入外部會議的入口）
**別名：** Claude Meetings beta
**首次出現：** 2026-11-10
**最後更新：** 2026-11-22
**最後新聞更新：** 2026-11-16

> **最新動態**（2026-11-16）
> Claude Meetings（beta）部分通話仍無法加入，Auto-join 持續暫停；進行中的通話與其他 Claude 功能不受影響。依賴自動加入排會議的 Team／Enterprise 用戶，先改手動加入。

---

## 現況

Claude Meetings 於 2026-11-10 以 beta 推出，限 **Team／Enterprise** 方案，官方說明中心 release notes 於 11-13 補上方案範圍。Claude 以可見參與者身分加入視訊會議，邊聽邊動手，同步寫會議記錄與待辦事項。

會中可用語音或文字向 Claude 提問，預設以文字回答。目前已知的支援平台是 Google Meet（Reuters 報導，11-10）。

## 是什麼、能做什麼

- **加入方式**：Claude 作為可見參與者進入通話，其他與會者看得到它；另有 Auto-join 功能，11-16 起暫停（見下方時間線）。
- **會中動作**：媒體描述為把討論轉成計畫與任務（TechCrunch）、即時處理任務（Reuters）、起草文件與白板（VentureBeat，11-12）。
- **官方介紹文**：[Introducing Claude Meetings](https://claude.com/resources/articles/claude-meetings)，登上 Hacker News 首頁（104 分，11-14），留言內容未取得，見 [[topics/community-tech-discussions]]。

## 方案與計費

- **方案範圍**：Team 與 Enterprise 的 beta（官方 release notes 11-13、Axios 11-10 一致）。
- **計費**：Meetings 通話中建立的 artifact 至 **2027-02-10** 前免費；其他 artifact 用量規則見 [[entities/pricing]]。

## 與 Whiteboards 的關係

會議中產出的白板與文件屬 artifact 體系：Whiteboards 是 [[entities/claude-workspace-suite]] 的 beta 成員，Meetings 則是另一條產品線，不列為三件組成員。兩者的銜接細節（白板如何從通話建立、能否共編）官方介紹文之外未取得。

## 時間線

- 2026-11-16：Anthropic Status 通報 Claude 無法加入部分 Meetings 通話，Auto-join 持續暫停；已在進行中的通話不受影響（[來源](https://status.claude.com/incidents/b5cq662qf2wm)），收錄於 [[entities/claude-code-known-issues]]。
- 2026-11-14：官方介紹文登 Hacker News 首頁，104 分。
- 2026-11-13：官方 release notes 寫明 Meetings 在 Team 與 Enterprise 以 beta 推出。
- 2026-11-12：VentureBeat 稱會議中可起草文件與白板。
- 2026-11-10：TechCrunch、Reuters、The Verge、Bloomberg 同日報導；The Verge、Bloomberg 稱這批產品是 Anthropic 自己的辦公套件、對上 Microsoft。

## 尚未取得的細節

- ❓ **待查證**（標 2026-11-22｜查 Claude Meetings、Auto-join、Google Meet）｜**Zoom、Microsoft Teams 是否支援**：僅見 Google Meet，其他平台官方介紹文未取得
- ❓ **待查證**（標 2026-11-22｜查 Claude Meetings、Auto-join、Google Meet）｜**錄音與逐字稿保存、與會者同意提示、用量是否算進方案額度**：官方介紹文細節未取得

## 相關議題

- [[entities/claude-workspace-suite]]
- [[topics/anthropic-product-matrix]]
- [[entities/pricing]]
- [[entities/pricing-history]]
- [[topics/community-tech-discussions]]

## 參考來源

- [Introducing Claude Meetings](https://claude.com/resources/articles/claude-meetings)（官方，HN 104 分，2026-11-14）
- [Help Center release notes](https://support.claude.com/en/articles/12138966-release-notes)（2026-11-13）
- [Anthropic Status：Claude unable to join meetings](https://status.claude.com/incidents/b5cq662qf2wm)（2026-11-16）
- 日報：news/2026-11-10、11-13、11-14、11-16

## 歷史記錄

- 2026-11-22：建頁，集中原散於四頁的 Meetings 事實。
