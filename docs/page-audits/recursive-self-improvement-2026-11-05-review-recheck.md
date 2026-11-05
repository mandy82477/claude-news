# 第 26 波評審實作複核：topics/recursive-self-improvement（2026-11-05）

> 這次核的是實作 commit `211952d`（另有 `24ca38a` gen 和 `62abb33` web）。上一輪評審是 `-review.md`，我把它當成自己的上一輪。核到一半，主 session 又推了 `9f95126`（冷讀者複驗修了 4 行）和 `807c423`（web），所以全部閘我在 `807c423` 上重跑了一次。
> 這一輪沒做 git 寫入，也沒動 repo 檔，只寫了這一份。build_web 改到的 `web_reader/index.html`、`sw.js` 已經用 `git show HEAD:` 還原，`git status` 是乾淨的。

## 結論

- 🔴 0 條、🟡 3 條。三條修法都附在下面，可以直接貼上。
- 實作單 0–9 步全部照做，或者偏離得可以接受。主 session 自己報的兩處偏離，我都判定可接受。
- **放行**。🟡A 建議在定稿列寫入以前修掉，因為它會把轉知的接手人導錯節。🟡B、🟡C 可以留到同波收尾，或下次 ingest 再修。

## 逐步表

| 步 | 判定 | 證據 |
|---|---|---|
| 0 原檔未動 | 照做 | `git diff --stat f659da4 211952d^` 只動了 docs 五件，沒有 wiki 或規則檔 |
| 1 備份＋套修法 | 照做 | `D.pre-review` 在；`D/` 的 `newtext.py`、`build.py`、`rules_patch.py` 跟 `review/dc2/` 逐字相同 |
| 2 一鍵重跑 | 照做 | `D/gates_after/*` 時戳 16:08，全部閘 exit 0（`check_cell_limits` 無新增，`build_web` 錨點 WARN 0）；`rebuild_out.txt` 還是 15:07 修法前那一版，沒覆寫（只是紀錄沒更新，不影響結果） |
| 3 肉眼抽驗 | 照做 | 在 `211952d` 上：`時間軸` 0 處；五個 grep 都命中，在 L51、L109、L149、L170、L312；gov 有 2 處；pages.md 有 2 處 |
| 4 重產文件 | 照做 | proposal L22、L102 和 map L31 都改成 424／399／M 377／砍 41／結構 13；L105 是 276；`map_rows.md` 整段都在 map 裡；draft L206–207 兩句手補都在 |
| 5 落地 | 照做 | 三頁跟 `D/out` 比，只差 gen 寫的 frontmatter；`pages.md`、`daily.md` 跟 `D/tmp_after` 逐字相同。當時 `verify.py` 的結果是 OK |
| 6 懸置基線 | 偏離，可接受 | 見偏離 (a) |
| 7 轉知 | 偏離，可接受 | 見偏離 (b)。`pending_handoffs.py list` 列出 H-e16406、H-2a8d8a 兩筆都是 open；anthropic-ipo L82、L171 確實指著 ai-agent-safety |
| 8 repo 全閘 | 照做 | 在 `807c423` 實跑 6 支 check 都 exit 0；懸置 223 筆，基線 223；`build_web` 錨點 WARN 0；`run_tests` exit 0 |
| 9 帳與收尾 | 照做 | ledger L63 寫「實作完成待複驗」、L128–129 是兩條裁決；log 有 Query 條目；`git show --stat 211952d` 共 15 檔，沒有一檔落在 `guard_roles.py` L52–56 的 GATE_FILES |

**偏離 (a)**：我在 `211952d` 的樹上把 msi 換回修改前的版本，模擬第一次 `--rebuild-count`。結果是 224 筆，差集「－3、＋15」，跟主 session 報的一樣。
- ＋15 的組成：
  - 11-02～04 ingest 新開 12 筆
  - msi 的 S-1/A 原筆（它本身也是 11-03 ingest 新開的）
  - TribLive 換到 gov 頁鍵後的新指紋
  - 本頁新開的 S-1/A
- 我上一輪寫「＋16」，是把 msi 那筆同時算進「S-1/A 兩筆」和「13 筆 ingest」，算了兩次。這是我的錯，總數兩邊都是 224。
- 第二次 rebuild 拿掉 msi 原筆，變成 223。對 212 的最終差集是 －3／＋14，`check_pending_markers` 實跑也是 223。
- `pending-marker-count.json` 只存最後一次的 note，第一次的 reason 已經被覆寫；吸收 13 筆的說明現在留在 ledger L63 和 log。這是既有設計，可以接受。

**偏離 (b)**：handoff 3、4、5 的接手人本來就是主編，主 session 同波直接做、不開帳，可以接受。log 的 Query 條目和 ledger L63 都有記到。

## 抽驗

- **結論層 7 條**（L51–57）：每條都對到 verified。
  - #4、#7：06-04「尚未達到」已標「據媒體轉述」，S-1/A 標「原文未核對」。
  - #1–#2：26%、2 月不到 1%、0 完全自主、約 3 萬（只算最常用的內部平台）。
  - #5–#6：METR 10-15、Accenture 09-18。
  - Medium 那條附 08-10 查證。
  - 自錨點 4 個，都有對應的標題：L257、L308，以及兩個 `##`。
- **量化表**（L66–71）：一個口徑一列，共六列。前三列官方一手，附 Institute 頁連結；Reuters 寫 09-17，跟 verified #3 一致。
- **White House Accord**：主頁 L109、gov L329 和 L595 都寫成「官方稿未提暫停」，L595 另寫「協議全文未附」，跟 verified 第四節相符。log L8593 寫「內容為與獨立外部稽核…合作」，比官方稿多說了一步；但 log 只能 append，頁面寫法正確，不修。
- **gov 搬入**：新增 35 個非空行，其中 3 行是 Accord 新寫，32 行是 G。32 行裡 27 行去掉列表記號後跟 P 逐字相同；5 行是節標題加了 `[🏛️]` 這類標籤；1 行是 P373 的「核心主張三→二」，因為 P372 被砍了，accounting 有記「（改）」。TribLive 的 🔎 也跟著搬過去了。
- **commitments 三列**（L49–51）：
  - 「雙方各預期五年投入至少 10 億美元，Anthropic 直接出資」，對 rsi L194 和 verified #6。
  - 日期 09-18、10-15、09-12 都對。
  - Amodei 那列寫「第一步已落地」，沿用上一輪已核可的推論（review L88）。

## 發現

**🟡A msi 指路句指錯節，而且「待查證」三個字被機器當成舊字樣標記**
- msi L521 現在寫「待查證住 `[[topics/recursive-self-improvement#目前結論]]`」，可是那筆 ❓ 實際在 rsi **L85**，也就是技術彙整 S-1/A 節（L78）底下。目前結論 L51 沒有標記。提案 §9 handoff 2 原本寫的也是 `#技術彙整`。
- 我用 `iter_legacy` 實跑：msi 的舊字樣從 0 變 1（L521，word=`待查證`）。全庫舊字樣所以維持 19，沒有照預期降到 18。棘輪不會擋，但等於多了一筆假的懸置。
- H-2a8d8a 的 note 也寫成 L488 要改指 `#目前結論`，接手的記者會照著指錯。
- 修法：
  - msi L521 整行換成：`- RSI 門檻定義與量測方法是否經官方進一步說明：這個缺口的懸置標記住 [[topics/recursive-self-improvement#技術彙整]] 的 S-1/A 節（11-03 起追蹤），本頁只判讀。`。這句我實測過，`iter_legacy` 為 0；換完不用 rebuild，因為新語法筆數不變。
  - 轉知改單：先 `python3 scripts/pending_handoffs.py void H-2a8d8a --result "指錯節，改開新單"`，接著 `open --from 安全政策 --to 投資分析 --page topics/market-signals-ipo --note "第 26 波 recursive-self-improvement：L65「硬度：官方文件」改「媒體轉述（引 S-1/A，原文未核對）」；L488 追蹤列改一句指 [[topics/recursive-self-improvement#技術彙整]] 的 S-1/A 節（原 L521 的 ❓ 已搬到該節、本頁改為指路）"`，先加 `--dry-run` 跑一次。
  - 驗收：`check_pending_markers` 的「舊字樣共 18 筆」，以及「懸置標記 223 筆」。

**🟡B index 鉤子少了「遞歸」**
- 提案 handoff 5 定的字是「AI 遞歸（遞迴）自我改進」，實作的 index L142 只寫「AI 遞迴自我改進」。頁面 H1（L26）用的是「遞歸」，全頁出現 5 次「遞歸」、2 次「遞迴」。只搜「遞歸」的讀者，在 index 這一欄找不到這頁的鉤子。
- 修法：把 index L142 的 `AI 遞迴自我改進：` 改成 `AI 遞歸（遞迴）自我改進：`。

**🟡C 照搬行留著 Accenture 的舊日期**
- rsi L180 寫「09-19 Anthropic 指定 Accenture 為首位內嵌評估者」。這跟 L53 的結論、commitments L49、verified #6 的 09-18 都不一致。09-19 其實是條目的新增日期。
- 這一行是照搬的原字，上一輪我沒抓到。
- 修法：把 `、09-19 Anthropic 指定 Accenture 為首位內嵌評估者` 改成 `、09-18 Anthropic 指定 Accenture 為首位內嵌評估者（09-19 條目）`。

**沒有發現問題，但要知道**：`9f95126` 改了 L57、L82、L173、L354 四行，所以現在拿 `D/verify.py` 去對 repo，結果是「273 行，FAIL」；對 `D/out` 仍然是「276 行，OK」。這四處是冷讀者複驗刻意改的：補「據媒體轉述」、修方位詞、把摘要改成連結。這是設計快照跟現況之間的落差，不是缺陷。`D/verify.py` 往後不能再拿來當 repo 的閘。

## 放行

放行，0 🔴。🟡A 建議在定稿以前修掉，改完跑一次 `check_pending_markers`，驗收是舊字樣 18、懸置 223；🟡B、🟡C 是一行的 Edit。三條都不新增裁決點，所以不用回設計者。修完以後，ledger 第 26 列就可以改成「定稿」。
