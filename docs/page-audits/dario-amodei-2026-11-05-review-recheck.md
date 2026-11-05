# 第 27 波評審・實作複核：entities/dario-amodei（2026-11-05）

> 對象：實作 commit `c61e9d8`（另有 `06826a0` gen、`56a9f1a` web），對照我上一輪的 `-review.md` 實作單第 0–9 步。原評審 agent 無法續用，本輪由新 agent 接手，把 `-review.md` 當成自己的上一輪來核。
> 我沒有做 git 寫入，也沒改 repo 檔，只寫了本檔。跑 `build_web` 後，`web_reader/index.html`、`sw.js` 已用 `git show HEAD:` 還原。HEAD 全閘是在 `<scratchpad>/w27/recheck/` 的 clone 裡跑的，跑完已刪。

## 結論：放行。0 🔴、3 🟡，都附修法，併進定稿 commit 即可，不必回設計者

本波實作 0–9 步都做了；偏離只有已知的三項，加上 🟡A。🟡C 來自之後的 `66b16e3`，不屬於本波實作。

## 逐步核對

| 步 | 判定 | 證據 |
|---|---|---|
| 0 確認原檔未動 | 照做 | `git diff --stat d6afcdb c61e9d8^ --` 九條路徑，輸出為空 |
| 1 備份並套修法 | 照做 | `design.pre-review` 存在。`newtext.py` 多 7 行；`build.py` 只差 L113–116：黃仁勳 P101 移位並改為 `take(101,"M")` |
| 2 一鍵重跑 | 照做 | `out/` 主頁與我上輪的 `review/d2/out` 位元組相同。`design/rebuild_out.txt`（16:40）是套修法前的舊檔，仍寫 84 行；以 out 的 mtime 16:51 為準 |
| 3 肉眼抽驗 | 照做 | 在 repo 主頁上跑：「主要針對中國」0；四個目標字串 4 行（L79、L81、L82、L99）；「4 倍以上／四倍以上／07-28」0；參考來源 31 條 |
| 4 重產文件 | 照做，有一處偏離 | `make_draft.py` 重產結果與已提交的 draft 位元組相同；`map_rows.md` 71 列都在 map 裡；proposal 的 L20「46→31」、L23「照搬 120／行內改 18」已改。偏離：map L20 改壞了，見 🟡A |
| 5 落地 | 照做，角色檔有偏離 | 五頁＝out 加上 gen 改的 frontmatter。`people/` 兩檔與 `design/tmp_after` 的 diff 為空，`daily.md` sha `ce709297…` 是補丁後的值，`c55b4005…` 是補丁前的鎖。角色檔照已知偏離用「2a.」插入一行（L15），可接受：分節閱讀的指引已在 daily.md L3。`verify.py` 對 repo 印「83 行；2→2」「結論：OK」 |
| 6 懸置 | 照做 | 「懸置標記 223 筆（基線 223）」「舊字樣共 18 筆」；沒跑 `--rebuild-count` |
| 7 轉知 | 照做，有已知偏離 | H-62f578（人物→安全政策，status open）是 pending-handoffs L406。RSI L55 確實寫「09-17 報導」，L371 確實是 `### 2026-09-17`，與單上內容相符；Burry 09-14 有 burry L40、L47、L61 nypost 09/14 佐證。handoff 1（index L72）由主編直接改，log 記明不登帳，`check_log_handoffs` ✅ |
| 8 repo 內全閘 | 照做 | 見下節 |
| 9 ledger 與 commit | 照做，有一處待補 | 總帳第 27 列已寫 🔴1–2、🟡3–6、🟡4 更正、213→175、62→83、223→223。回訪日欄空著，這和第 26 波慣例一致（`211952d` 實作時空，`d6bcfac` 定稿才填），所以不算漏做。commit 範圍：15 檔，含五頁、`pages.md`、`daily.md`、角色檔、四份 docs、ledger、index、log、handoffs |

## 抽驗

- **主張清單 10 列**：L57–66 逐列都附本人原文，或標「僅媒體轉述」並附連結。第 8 列已去掉「針對中國」（L64），原字仍在 archive L52，沒有丟失。
- **批評者表三列新列與「何時」**：Baker「08-16 前」（TechCrunch 08/16，P L156、L198）；Zuckerberg「09-16 前」（NYT 09-16 僅標題，P L145、L188）；川普陣營「09-24 前」（Axios 09/24 獨家，news/2026-09-26 L35）；黃仁勳「09-23 錄製（09-28 報導）」（jensen-huang L74）。其餘四列：Suleyman 09-16（suleyman L51）、Vembu 09-23、Lonsdale 09-25、LeCun 10-01（各頁 L47）。九列依日期排序（L76–84）。
- **安保費句**：callout L43 與 M L146 都寫「底薪 65.4 萬的四倍多、總薪酬約 1,800 萬的 15%」，數字來自 verified 第四節。我重算：2,745,874／654,167＝4.20 倍；2,745,874／17.96M＝15.3%。兩者都成立。
- **open-weights 07-27 三項**：L59 列出出口管制、蒸餾、開源與閉源都強制安全測試三項，附 anthropic.com 連結；L138、L172 寫的都是 07-27。
- **減速文 09-12**：L49、L57 都寫出〈We Must Pace the Frontier〉並附本人網站連結。三鄰頁（burry、vembu、jack-clark）的 `dario-amodei` 相關行都已從 09-13 改成 09-12，全庫 grep「09-13…減速／暫緩」為 0。

## 閘（repo 工作樹；HEAD clone 另跑）

- check_hierarchy ✅（32 母頁）；pending 223／基線 223、舊字樣 18；freshness OK（143 頁）；cell、reader 無新增；build_web 錨點 WARN 0、exit 0
- check_rules／run_tests 在工作樹是 **exit 1**。唯一的失敗是 personal_paths：`wave27-cold-reader-recheck-2026-11-05.md` L3 寫了專案絕對路徑。我跑閘時這個檔還只是暫存，複核途中已由 `66b16e3` 提交，所以**現在的 HEAD 也是紅的**。這不是本波實作的問題：在實作 HEAD（`56a9f1a`）的 clone 上，check_rules ✅、run_tests exit 0。修法見 🟡C
- `git show --stat c61e9d8`、`06826a0`、`56a9f1a`：都沒碰 GATE_FILES（guard_roles L52–56）

## 發現

### 🟡A　map L20「參考來源」那一格改壞了

- **證據**：現在寫「砍 16、新增 1（同事件、同網址、無連結）、改 9…、新 1（減速文章一手）」。新增算了兩次，括號也從「砍」移到了「新增」後面，讀起來像新增 2 條。
- **修法**（Edit map L20 第二格）：
  - 舊：`46→31 條：砍 16、新增 1（同事件、同網址、無連結）、改 9（補連結、標籤、日期）、新 1（減速文章一手）`
  - 新：`46→31 條：砍 16（同事件、同網址、無連結）、改 9（補連結、標籤、日期）、新 1（減速文章一手）`

### 🟡B　archive L58 仍寫 07-28，和主頁的 07-27 矛盾

- **證據**：
  - 健檢卡 V2（`dario-amodei-2026-11-05.md` L118）點名了「L71、L164、archive L58」三處，但 map L23 只處理主頁 L210，提案和我上一輪的評審也都漏了 archive。
  - 現在主頁 L59、L138、L172 寫 07-27，archive L58 寫「2026-07-28：於 Anthropic Blog 發表聲明」。
  - verified #1 依官方頁判定是 07-27。
- **修法**（Edit archive L58）：
  - 舊：`- 2026-07-28：於 Anthropic Blog 發表聲明「Our position on open-weights models」`
  - 新：`- 2026-07-27：於 Anthropic Blog 發表聲明「Our position on open-weights models」`
  - 只改日期，長度不變，不影響 cell 閘。
- **相關但不屬本波（推論）**：`topics/anthropic-government-policy` L439 時序列寫「2026-07-28｜Amodei 官方部落格聲明」，這頁歸安全政策記者，建議定稿時順手開一張轉知（→安全政策，L439 改 07-27），不擋放行。

### 🟡C　`66b16e3` 把個人路徑帶進 HEAD（不屬本波實作，但擋 commit）

- **證據**：`wave27-cold-reader-recheck-2026-11-05.md` L3 有一段反引號包住的專案絕對路徑，指向根目錄 CLAUDE.md，check_rules 檢查 6 抓到這一處。
- **修法**：Edit 該檔 L3，把那段反引號路徑換成 `` `CLAUDE.md`（專案根目錄） ``，再重跑 check_rules 和 run_tests，兩者都應 exit 0。

## 定稿列要補

- 回訪日填 2026-11-12。
- 產物欄加 `-review-recheck`。
- 🔴2 的描述補上「Zuckerberg／川普陣營改寫為『MM-DD 前』」。
- 記一句：🟡A、🟡B、🟡C 在定稿 commit 一起修。
