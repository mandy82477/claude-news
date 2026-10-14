---
page: "entities/linus-torvalds"
kind: "entity"
type: "person"
status: "active"
domain: "👤 人物"
last_updated: "2026-10-12"
last_news_update: "2026-10-12"
status_main: "active"
days_since_news: 1
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 1
inbound_links: 3
attribution_count: 1
attribution_last: "2026-10-12"
top_source: "hacker-news"
pending_count: 0
pending_overdue: 0
pending_next_review: null
pending_signalled: 0
staleness_exempt: null
signal: "孤島"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Linus Torvalds

**類型：** person
**狀態：** active
**領域：** 👤 人物
**身分：** Linux 核心創造者
**與 Anthropic：** 外部觀察者
**職能：** 工程產品
**為何追蹤：** Linux 核心維護者具名使用 Claude Code 開發 kernel 分支
**首次出現：** 2026-10-12
**最後更新：** 2026-10-14
**最後新聞更新：** 2026-10-14

> **36Kr 稱分支效能提升 3 倍，未獲證實**（2026-10-14）
> 分支 10-13 已正式貼上信件列表，Linus 親自撰寫 cover letter；36Kr 稱效能提升達 3 倍，尚無他源佐證。

---

## 現況

36Kr 報導稱這個 Claude Code 協作分支效能實測提升達 3 倍，為單一中國媒體轉述，尚無 Linus 本人或其他來源佐證這個數字（2026-10-14，詳見下方歷史記錄的懸置標記）。

此前分支已於 2026-10-13 正式整理成 patch 貼上 Linux 核心信件列表，Linus 在 cover letter 親自寫下：「程式碼、測試程式、前述審查與這份文字的初稿，都是在我的指示下用 LLM coding assistant（Claude Code）完成的，效能測量是在我自己的機器上跑的」。

## 相關議題

- [[entities/claude-code]] — 本次具名使用的工具

## 參考來源

- [Linus Torvalds used Claude Code to rewrite how Linux reads cached files](https://startupfortune.com/linus-torvalds-used-claude-code-to-rewrite-how-linux-reads-cached-files/) — Hacker News／StartupFortune，2026-10-13
- [Linus Torvalds Embraces AI: Writing Linux Kernel Code with Claude Code Delivers 3X Performance Surge](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1Sejh2bUFBMmZGTzR5QWhaSThBRFl2OTNuSVJfdGhnOEQxWGlqY0xPRDNuejVoX1dyVjZsR3NwSEV0NEJGVDBmNTZkU1hXRUVmNmFJ?oc=5) — Google News／36Kr，2026-10-14
- [Linus Torvalds Working on a Hefty Linux Kernel Improvement with Claude Code](https://www.phoronix.com/news/Linus-Torvalds-Claude-Code) — Hacker News／Phoronix，2026-10-12
- [Quoting Linus Torvalds](https://simonwillison.net/2026/Aug/22/linus-torvalds/) — Blog／Simon Willison，2026-08-22（背景：未點名工具的除錯發言）

## 歷史記錄

- 2026-10-14：❓ **待查證**（標 2026-10-14｜查 36Kr、3X Performance Surge）｜**36Kr 稱 kernel 分支效能提升達 3 倍**：36Kr 報導稱該 Claude Code 協作分支效能實測提升達 3 倍，為單一中國媒體轉述，尚未見 Linus 本人或其他來源證實具體數字（來源：Google News／36Kr）
- 2026-10-13：這個 Claude Code 協作分支正式整理成 patch 貼上 Linux 核心信件列表，Linus 在 cover letter 親自寫下程式碼、測試程式與效能測量皆在自己指示下用 Claude Code 完成、在自己機器上測得（來源：Hacker News／StartupFortune）
- 2026-10-12：重新整理 `torvalds/linux.git` 時意外發現新分支 `noref-filemap-read-with-llm`；Phoronix 判讀為使用 Claude Code 開發 kernel 新功能，與他過去僅在主線推 master 的習慣不同（來源：Hacker News／Phoronix）
- 2026-08-22：Simon Willison 部落格轉引其 commit 訊息，稱某次「地獄等級」除錯過程主要靠 AI 完成繁瑣工作，未點名具體工具（來源：Blog／Simon Willison）
