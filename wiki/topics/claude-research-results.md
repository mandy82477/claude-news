---
page: "topics/claude-research-results"
kind: "topic"
status: "ongoing"
domain: "🤖 模型"
last_updated: "2026-11-24"
last_news_update: "2026-11-24"
status_main: "ongoing"
days_since_news: 1
parent: null
children: "[]"
page_role: "root"
days_since_news_subtree: 1
inbound_links: 8
attribution_count: 5
attribution_last: "2026-11-24"
top_source: "google-news"
pending_count: 4
pending_overdue: 0
pending_next_review: "2026-11-30"
pending_signalled: 1
staleness_exempt: null
signal: "健康"
generated_by: "scripts/gen_wiki_frontmatter.py"
---
# Claude 原創科研成果與驗證狀態

Claude 參與的科學與數學聲稱清單，逐項記錄是誰宣稱、有沒有經過同行審查或獨立驗證。

**狀態：** ongoing
**領域：** 🤖 模型
**開始日期：** 2026-08-11
**最後更新：** 2026-11-24
**最後新聞更新：** 2026-11-24
**蒐集邊界：** 只收 Anthropic 官方或媒體報導過的 Claude 科研／數學聲稱；第三方實驗室的獨立複驗只有在媒體報導時才會進來，漏收是常態。

> **最新動態**（2026-11-24）
> VP≠VNP形式化證明聲稱：Anthropic與OpenAI互爭優先權，GitHub commit時間戳記比對結果不一；黎曼猜想仍未經同行審查，另有標題稱證明『是個笑話』待查證。

---

## 摘要

截至 2026-11-24，本站收到的七項聲稱中，沒有任何一項見到同行審查完成的報導。費馬最後定理的形式化有領域專家公開回應，橢圓曲線 rank 紀錄有第三方題庫登錄，其餘都只有宣稱方自己的說法。

最新的是 VP≠VNP 代數複雜度猜想形式化證明：Anthropic 11-23 發布 Claude 完成的版本，OpenAI 11-24 稱自家證明更早完成，雙方互貼 GitHub commit 時間戳記、討論串分別衝上 355 分與 77 分。黎曼猜想聲稱（11-20）仍未經同行審查，11-24 另有兩則標題稱證明達 25 萬頁、一名 Anthropic 數學家稱其「是個笑話」，原文均無法讀取，待查證。

zeta、rank、費馬三項明載用內部研究模型，黑洞、黎曼與 VP≠VNP 三項未見點名版本；都不能直接當成 [[entities/fable-5]] 產品版的能力。

## 驗證總表

| 日期 | 成果 | 誰宣稱 | 審查／驗證狀態 | 來源 |
|---|---|---|---|---|
| 2026-11-23 | VP≠VNP 代數複雜度猜想形式化證明 | Anthropic（Claude 完成）；OpenAI 稱自家證明更早完成 | 雙方均未見同行審查；GitHub commit 時間戳記互為佐證、孰先有爭議 | [Anthropic](https://github.com/anthropics/formal-math/tree/main/vp-vnp)、[OpenAI](https://github.com/openai/math/tree/main/preprints/VP-and-VNP-are-different-November-23-2026) |
| 2026-08-11 | 黎曼 zeta 函數零點比例的下界紀錄（先前 87 年未破） | Anthropic 官方部落格 | 未見獨立驗證報導；僅媒體轉載 | [Anthropic](https://www.anthropic.com/research/riemann-zeta) |
| 2026-08-23 起（09-16 報導） | 橢圓曲線 rank ≥30、≥31 紀錄 | Alpöge 與 Ava Howell；Scientific American 報導 | Epoch AI 題庫頁載有紀錄；未見同行審查 | [Epoch AI](https://epoch.ai/frontiermath/open-problems/elliptic-curve-rank) |
| 2026-09-04 | 費馬最後定理的 Lean 形式化證明 | Anthropic 官方研究文章 | Buzzard 公開表示被搶先；未見第三方複驗報導 | [Anthropic](https://www.anthropic.com/research/formalizing-fermats-last-theorem) |
| 2026-11-09 | 兩個開放數學問題（發布文一句帶過） | Anthropic 官方發布文 | 未點名題目，無從驗證 | [Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2) |
| 2026-11-19／20 | 黑洞物理兩道理論問題 | Anthropic 研究部落格 | 附兩篇預印本；未經同行審查，未見獨立驗證 | [Anthropic Research](https://www.anthropic.com/research/claude-black-hole-physics) |
| 2026-11-20 | 黎曼猜想證明（個人論文草稿） | Alpöge；多家媒體轉述 | 未經同行審查；史丹佛 11-21 另發人類競爭草稿，亦未經審查 | [Simon Willison](https://simonwillison.net/2026/Nov/20/levent-alpoge/) |

## 各項細節

- **VP≠VNP（11-23 Anthropic 發布、11-24 OpenAI 跟進）**：Anthropic 稱 Claude 完成代數複雜度理論猜想 VP≠VNP 的形式化證明（Lean），OpenAI 翌日公開聲稱自家證明更早完成（[Anthropic](https://github.com/anthropics/formal-math/tree/main/vp-vnp)；[OpenAI](https://github.com/openai/math/tree/main/preprints/VP-and-VNP-are-different-November-23-2026)，2026-11-23/24）。
- **VP≠VNP 優先權的時間戳記佐證**：雙方於 Hacker News 互貼 GitHub commit 時間戳記（Anthropic 11-23 12:04、OpenAI 17:30，太平洋時間），討論串分別衝上 355 分與 77 分，孰先未有共識，均未見同行審查。
- **黎曼猜想的 11-24 後續報導**：Interesting Engineering 與 The Register 同日標題稱 Alpöge 的證明長達 25 萬頁、一名 Anthropic 數學家稱其「是個笑話」；兩則原料均僅有標題與連結、無法讀取正文，是否為正式撤回或作者自嘲待查證（[Interesting Engineering](https://news.google.com/rss/articles/CBMikwFBVV95cUxOOWx2VGRIM0F6YkFpLWxRMnpfcERZcUF0MFVfcHVmcnl4Z1ZyUlJVNElJRDBNbFY1azBLQzd6ZUx1S0JJdmo2LTZoWEJleGFxVjBBM0kwekgtXzR2c29vdm1tWWdQZnNtQzZ5QmFJakxrMGZHblRSM1duWWlIbl92WHp2V2lKUnEwVjBuY0k3U3FzTVE?oc=5)；[The Register](https://news.google.com/rss/articles/CBMi6wFBVV95cUxPc1hFcE5MWURoX29EZXNEXzBaU1A4RC1VZGlzUHBBWTUwdXJGSUQyTzh0Rm9NU09qN3lxS2pvdVBlN1JxdjBzY3E3ZFZEMUN1aVhlR3NuWWlEWE5ncEdxV3A3Wl9zeFhEQWZfcXdua3puSkp3MkpkaGl6S3N6UzFLMGZna3JabWgwUFp5N3pFaWlkbDlXWXdGQzdTZWk5XzFUMktnOEFVSnk4aVpETEZXUGEzci1kb19hd0NOMHdJS01MLV9CRENMWWVXMHc2LUd1RktsWUdRRF8zc0xkaDZ1aENsUDlpcGFaSmdF?oc=5)，2026-11-24）。
- **zeta 零點下界（08-11）**：官方稱是一個未發布的研究版 Claude 在嘗試證明黎曼假設未果時意外取得（[Anthropic](https://www.anthropic.com/research/riemann-zeta)，HN 211 分、4 個獨立來源轉載）；TechSpot 08-13 為同一事件的接力報導，無新增細節。
- **橢圓曲線 rank（08-23 提交、09-16 報導、10-03 查證）**：Alpöge 與密碼學者 Ava Howell 用 Claude 於數日內先後提交 rank ≥30 與 ≥31；此前由 rank 28 到 29 耗時逾 18 年。
- **rank 紀錄的來源限制**：所用為內部未發布版本；Scientific American 本環境無法讀全文，內容取自搜尋摘要（[Scientific American](https://www.scientificamerican.com/article/anthropics-ai-steals-mathematicians-record-for-most-complicated-curve/)；[Epoch AI](https://epoch.ai/frontiermath/open-problems/elliptic-curve-rank)，查證 2026-10-03）。
- **費馬最後定理（09-04）**：Claude 歷時 11 天完成，Lean 程式碼約 1,300 萬行（行數轉引 [dev.to](https://dev.to/techaiwire/anthropics-ai-formalizes-fermats-last-theorem-in-lean-lf3)，2026-09-09）。
- **費馬的模型與外界回應**：官方 2026-09-07 查證用的是「內部研究模型，約略相當 Fable 5.1」。[[entities/kevin-buzzard]] 在 Xena Project 部落格表示「被 Anthropic 搶先」，並指出這是 Freek Wiedijk 百大形式化挑戰清單最後完成的一項（[Xena Project](https://xenaproject.wordpress.com/2026/09/04/flt-anthropic-has-beaten-me-to-it/)，2026-09-04）。
- **黑洞兩題（11-19 首發、11-20 補第二項）**：第一項是物理學家 20 多年前設下、始終未解的計算，結果顯示黑洞形成相關的突變在時空不再有明確定義時仍存在。
- **黑洞第二項與預印本**：第二項找出測試候選量子重力理論某項技術方法的精確極限。官方部落格 11-20 版本附兩篇預印本，HN 分數 133 升至 543；原文未點名模型版本（[Anthropic Research](https://www.anthropic.com/research/claude-black-hole-physics)；[Mashable](https://news.google.com/rss/articles/CBMidkFVX3lxTFBBYkVUNFdNUHY4TGo2TnhfOGpReDNjLWNydjluX2ZVd19uclJKU2NlUXhOd1F6RTBpQmRFTUFaYXlVUWt4Rnd1U0JveWFJdmtFQmdBT0oxaFVXRzRDVlozUjIzQ0tONF9xc1hMcElsNy1mZEN6eWc?oc=5)，2026-11-20）。
- **黎曼猜想（11-20）**：Alpöge 在個人草稿中寫道相信自己與 Claude 合作發現了證明，並稱方法可延伸到其他問題。
- **黎曼猜想的媒體反應**：WSJ、New Scientist、Scientific American、The Verge、Tom's Hardware、Phys.org、Unite.AI 同日報導，都強調未經同行審查（[Simon Willison](https://simonwillison.net/2026/Nov/20/levent-alpoge/)；[WSJ](https://news.google.com/rss/articles/CBMitgFBVV95cUxQd2R1UU5HMEVNTGhtYWxQaTNBMjVRZnZxZjJVU0U1MVk0U2dIRHh6akhYNV9tNWxXYjNmeU16UzdqZDM3bUpDS1BxOEd2b3oySzVMako4Z25JMmNFUVd5ZlFWNTZ4WmJ6d2NXT0R5Z1JsNVNGMi04MGowVF9CQkl4dEEtXzJNYWRDeHA3Rk1hV250dEZWQjNRLW5RZHZPQ0ZMMlNLSDdkejFKTklvZW1ZNDZZalFOQQ?oc=5)，2026-11-20）。所用模型版本未見報導。
- **史丹佛競爭草稿（11-21）**：史丹佛研究團隊在聲稱出現數小時後發布完全由人類完成的證明草稿；Guardian、AP、Business Insider 等同日跟進（[The Decoder](https://news.google.com/rss/articles/CBMi2AFBVV95cUxQUGJqSjZWaXNISk8tTE9CM0d4czdubmlPOW4zQjNBTG51X0drbzlBSGl2Mkx4NHdCS0RtWmhNSERHdm4yMkk1bGJZZnhlMzZRMVMzaGZMZTlMekJaVFNQdkpDUDMyUERoQWhhWW9QSVJIQk53eFVUa1EwdUpQUFZTSFVuemIwcWFmWlRyRl8xdm5KUDd6V2Qza3ZPM1IzbHVTRl91TFNDNDNxUnhzdXZXWk1teGcyN2RORU5xTTdHYzJZUkZLaE1ySEpraWljMFlJQV9ZR2JXcDU?oc=5)；[Business Insider](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOMWN0cGwxa2RJY0tiMk5sdjNWeHZzbXhfbEVGamdHaDdaT3diaWhpdlBYd2dzQThqVXpKZlg2VjZWOWlYNUlwS2NPRjBtbjEwXzYzTVVsUktBcmtfbXBqYkJ4OEh1cFJNSWdjb3hLUWlOT29zd1hYV1B3VFhnTGVwTDVvN2kwaHF5XzRycTNEM2JkNHVPQmFTZ3dyNVdWMG01em5BYk1OT1lWZw?oc=5)，2026-11-21）。

## 目前結論

- 兌現狀態：有同行審查結論的 0 項；有第三方登錄或領域專家公開回應的 2 項（rank 紀錄、費馬形式化）；其餘 5 項只有宣稱方自己的說法。
- 官方一手發布且附可查材料（預印本、Lean 程式碼）的，與個人草稿經媒體轉述的，驗證路徑不同：前者別人能查，後者要等審查。
- 這條線的能力聲稱與 Fable 5 產品版是兩回事：多數用內部研究模型，產品版能做到什麼見 [[entities/fable-5]]。

## 懸置中的問題

❓ **待查證**（標 2026-11-24｜查 vp-vnp、formal-math｜複 2026-12-08）｜**VP≠VNP 證明優先權與同行審查狀態**：Anthropic 11-23 先發布，OpenAI 11-24 稱自家證明更早完成；HN 留言比對 GitHub commit 時間戳記（Anthropic 12:04、OpenAI 17:30，同日太平洋時間）結果互有解讀，孰先未有共識，雙方均未見同行審查報導

❓ **待查證**（標 2026-11-20｜查 Alpöge、Riemann hypothesis｜複 2026-12-04｜訊 2026-11-24）｜**黎曼猜想證明是否經同行審查確認**：Levent Alpöge 聲稱與 Claude 合作完成證明，11-21 史丹佛另發表競爭性全人類草稿；11-24 另有標題稱證明達 25 萬頁、一名 Anthropic 數學家稱其「是個笑話」，原文無法讀取，是否為正式撤回或自嘲待查證，雙方截至目前均未經同行審查

❓ **待查證**（標 2026-11-20｜查 Alpöge、Riemann hypothesis｜複 2026-12-04）｜**史丹佛人類草稿與 Alpöge 草稿誰先通過獨立檢驗**：截至 11-21 兩份草稿都尚無同行審查或獨立驗證結果

🔎 **查無官方**（標 2026-09-16｜查 complicated curve、Scientific American｜複 2026-11-30）｜**橢圓曲線 rank 紀錄所用模型版本**（2026-09-16 報導）：官方頁面查無記載；複查 2026-10-31，[anthropic.com/news](https://www.anthropic.com/news) 近期貼文（含 10-27、10-28 科學類）無此紀錄，Scientific American 文章存在（搜尋可見）但本環境 egress 擋該網域、無法讀全文；首查 2026-10-03，[anthropic.com/news](https://www.anthropic.com/news) 與[模型總覽](https://platform.claude.com/docs/en/about-claude/models/overview)均無此紀錄或模型說明，上述歸屬僅媒體稱

## 相關實體

- [[entities/fable-5]]：產品版 Fable 5 系列，本頁多數成果不是它做的
- [[entities/kevin-buzzard]]：費馬形式化工作的長期主導者，公開回應 Anthropic 的結果
- [[entities/mythos]]：同世代的 Mythos 級模型

## 時序

- **2026-11-24**：OpenAI 公開聲稱 VP≠VNP 證明完成時間早於 Anthropic，雙方互貼 GitHub commit 時間戳記；另有媒體標題稱 Anthropic 數學家稱黎曼猜想的 25 萬頁證明「是個笑話」，待查證
- **2026-11-23**：Anthropic 發布 Claude 完成 VP≠VNP 代數複雜度猜想的形式化證明
- **2026-11-21**：史丹佛發布全人類競爭證明草稿，雙方均未經同行審查
- **2026-11-20**：Alpöge 黎曼猜想草稿；黑洞兩題官方部落格補第二項並附兩篇預印本
- **2026-11-19**：黑洞物理兩題首發
- **2026-11-09**：Fable 5.2 發布文提到 prerelease 解開兩個開放數學問題
- **2026-10-03**：橢圓曲線 rank 紀錄查證補述
- **2026-09-16**：Scientific American 報導橢圓曲線 rank 紀錄
- **2026-09-04**：費馬最後定理形式化
- **2026-08-11**：zeta 零點下界紀錄
