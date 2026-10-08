// news-console：CLAUDE_NEWS 本機 mod。三塊——
//   1. 本機落後 origin 的看守（背景 fetch、prompt 上方提示列、只給 Claude 的一行警告、雲端班次真失敗）
//   2. wiki 新鮮度旁註（Read wiki 頁後在 transcript 記一行最後新聞更新日與天數）
//   3. 共用工作樹自動歸屬（記下本 session 動過的檔；git add／commit 掃到別的 session 的檔就拒絕）
//
// 守則（見 README）：對工具呼叫只 next(e) 或 { deny }——回 { result } 會跳過專案的 settings hook；
// 不改寫工具輸入；不用 $.model、不起 agent；不自動 pull；按鈕不用數字熱鍵；預設 fail-open。

import {
  classifyShift, explainPullFailure, foreignHits, freshness, gitStageCalls, isWikiPage, latestDigest,
  LIVE_MS, parseAheadBehind, parsePorcelain, relTo, syncSummary, underSpec,
} from './lib.ts'

type Sync = {
  behind: number
  ahead: number
  subject: string
  digest: string | null
  shiftAlert: string | null
  error: string | null
  checkedAt: number
}

let active = false // 只在 CLAUDE_NEWS 樹上作用；全域載入時其他專案完全不受影響
let root = ''
let sessionId = ''
let sync: Sync | null = null
let pulling = false

async function git($: any, args: string[], timeoutMs = 25_000) {
  try {
    return await $.process.run(['git', ...args], { cwd: root, timeoutMs })
  } catch (err) {
    return { exitCode: -1, stdout: '', stderr: String(err) }
  }
}

// fetch=false：只用本機 refs 重算（不連網、很快）。push／merge／pull 之後與送出 prompt 前用它，
// 否則狀態要等下一次 10 分鐘的背景 fetch 才更新——2026-10-08 本 session 合併並推送後，
// 提示列與給 Claude 的警告還停在「分岔：遠端多 2 筆、本機 1 筆未推」。
async function checkOrigin($: any, fetch = true) {
  const fetched = fetch ? await git($, ['fetch', '--quiet', 'origin']) : null
  const counts = parseAheadBehind((await git($, ['rev-list', '--left-right', '--count', 'HEAD...origin/master'])).stdout)
  const subject = (await git($, ['log', '-1', '--format=%s', 'origin/master'])).stdout.trim()
  const digest = latestDigest((await git($, ['ls-tree', '--name-only', 'origin/master', 'news/'])).stdout)
  const log = (await git($, ['show', 'origin/master:src/logs/task_scheduler.log'])).stdout
  const parked = (await git($, ['branch', '-r', '--list', 'origin/cloud-daily-*'])).stdout
    .split('\n').map((s) => s.trim()).filter(Boolean)
  const now = await $.clock.now()
  sync = {
    behind: counts?.behind ?? 0,
    ahead: counts?.ahead ?? 0,
    subject,
    digest,
    shiftAlert: classifyShift(log.split('\n').slice(-400).join('\n'), parked, now).alert,
    error: fetched ? (fetched.exitCode === 0 ? null : 'git fetch 失敗，落後筆數可能過時') : (sync?.error ?? null),
    checkedAt: now,
  }
  // 狀態列常駐一行：同步時也看得到 mod 活著（提示列與提示行只在出事時顯眼）
  $.ui.status(
    sync.error ? 'news ⚠ ' + sync.error
      : sync.behind > 0 ? 'news ⚠ ' + syncSummary(sync.ahead, sync.behind).text.split('：')[0]
      : sync.shiftAlert ? 'news ⚠ 雲端班次失敗'
      : 'news ✓ 已同步' + (sync.digest ? '　日報 ' + sync.digest.slice(5) : ''),
  )
  $.ui.invalidate('ui.render')
}

async function touchedOf($: any, sid: string, keys?: string[]): Promise<Set<string>> {
  // 舊格式 `touched:<sid>` 陣列照讀（升級前的記錄），新格式一檔一把 `p:<sid>:<path>`
  const v = await $.store.get('touched:' + sid)
  const out = new Set<string>(Array.isArray(v) ? v : [])
  const prefix = 'p:' + sid + ':'
  for (const k of keys ?? (await $.store.keys())) if (k.startsWith(prefix)) out.add(k.slice(prefix.length))
  return out
}

async function addTouched($: any, paths: string[]) {
  if (!paths.length || !sessionId) return
  // 一檔一把 key、只 set 不先 get：同 session 的並行子代理（同一個 sessionId）各自寫入互不覆蓋。
  // 舊做法是整份陣列 get→add→set，五位記者並行時互相蓋掉，本 session 改過的檔從帳上消失，
  // 換成別的 session 的誤記（它 Bash 前後比對時剛好看到這些檔變髒）擋下自己的 commit。
  for (const p of paths) await $.store.set('p:' + sessionId + ':' + p, 1)
  await $.store.set('alive:' + sessionId, await $.clock.now())
}

async function liveForeign($: any): Promise<Map<string, Set<string>>> {
  const now = await $.clock.now()
  const out = new Map<string, Set<string>>()
  const keys = await $.store.keys()
  for (const key of keys) {
    if (!key.startsWith('alive:')) continue
    const sid = key.slice(6)
    if (sid === sessionId) continue
    const at = Number(await $.store.get(key))
    if (now - at > LIVE_MS) continue
    out.set(sid, await touchedOf($, sid, keys))
  }
  return out
}

async function dirty($: any): Promise<string[]> {
  const r = await git($, ['status', '--porcelain', '-uall'], 15_000)
  return r.exitCode === 0 ? parsePorcelain(r.stdout) : []
}

export function register(on: any) {
  on('session.start', async ($: any, e: any, next: any) => {
    try {
      root = await $.session.root()
      active = (await $.fs.exists(root + '/scripts/ingest_gate.py')) && (await $.fs.exists(root + '/wiki/log.md'))
      if (active) {
        sessionId = await $.session.id()
        const now = await $.clock.now()
        await $.store.set('alive:' + sessionId, now)
        // 清掉一天沒心跳的 session，store 上限 4 MiB
        const keys = await $.store.keys()
        const dead = new Set<string>()
        for (const key of keys) {
          if (!key.startsWith('alive:')) continue
          if (now - Number(await $.store.get(key)) > 24 * 3600_000) {
            dead.add(key.slice(6))
            await $.store.delete(key)
            await $.store.delete('touched:' + key.slice(6))
          }
        }
        for (const key of keys) {
          if (key.startsWith('p:') && dead.has(key.slice(2, key.indexOf(':', 2)))) await $.store.delete(key)
        }
        // fetch 不可擋住開場：延後在背景跑，之後每 10 分鐘一次
        $.clock.after(1500, () => checkOrigin($))
        $.clock.every(10 * 60_000, () => checkOrigin($))
      }
    } catch {
      active = false
    }
    return next(e)
  })

  // ── 1. 只給 Claude 的一行警告 ───────────────────────────────
  on('prompt.submit', async ($: any, e: any, next: any) => {
    if (!active || !sync || sync.behind === 0) return next(e)
    // 警告前先用本機 refs 重算：使用者或 Claude 可能剛拉取、合併、推送過
    try {
      await checkOrigin($, false)
    } catch {
      // 重算失敗就沿用上次結果
    }
    if (sync.behind === 0) return next(e)
    const s = syncSummary(sync.ahead, sync.behind)
    const line = s.canFastForward
      ? `⚠️ 本機 clone 落後 origin/master ${sync.behind} 筆（最新：${sync.subject}）。` +
        '回答 wiki／日報的現況前，先請使用者按提示列的「拉取」或自己 git pull --ff-only；否則你讀到的是舊版。'
      : `⚠️ 本機 clone 與 origin/master 分岔（遠端多 ${sync.behind} 筆，最新：${sync.subject}；本機 ${sync.ahead} 筆未推）。` +
        'ff-only 拉不了；回答 wiki／日報的現況前要先合併，否則你讀到的是舊版。'
    return next({ ...e, context: [...(e.context ?? []), line] })
  })

  // ── 1. prompt 上方提示列：只在落後或雲端真失敗時出現 ─────────
  on('ui.render', { component: 'AbovePrompt' }, async ($: any, e: any, next: any) => {
    if (!active || !sync || e.props.hasSurvey) return next(e)
    if (sync.behind === 0 && !sync.shiftAlert) return next(e)
    const { Box, Text, Button } = $.ui.resolve(e)
    const rows: any[] = []
    if (sync.behind > 0) {
      const s = syncSummary(sync.ahead, sync.behind)
      rows.push(Box({
        key: 'behind',
        flexDirection: 'row',
        columnGap: 2,
        children: [
          Text({ color: 'yellow', wrap: 'truncate-end', children: [s.canFastForward ? `${s.text} · ${sync.subject}` : s.text] }),
          s.canFastForward && Button({
            key: 'pull',
            label: pulling ? '拉取中…' : '拉取（ff-only）',
            onPress: async () => {
              if (pulling) return
              pulling = true
              $.ui.invalidate('ui.render')
              const r = await git($, ['pull', '--ff-only', '--quiet'], 120_000)
              pulling = false
              $.ui.toast(r.exitCode === 0 ? '已拉取到最新' : '拉取失敗：' + explainPullFailure(r.stderr || String(r.exitCode)))
              await checkOrigin($)
            },
          }),
        ].filter(Boolean),
      }))
    }
    if (sync.shiftAlert) rows.push(Text({ color: 'red', wrap: 'truncate-end', children: [sync.shiftAlert] }))
    if (sync.error) rows.push(Text({ dimColor: true, children: [sync.error] }))
    // 提示列是所有 mod 共用的：把排在後面的 mod（例如 newsroom-pets）畫的東西一起放進來
    const theirs = await next(e)
    return Box({ flexDirection: 'column', children: theirs ? [...rows, theirs] : rows })
  })

  // ── 1. 平常：提示行尾端一段暗色「已同步　日報 MM-DD」────────
  on('ui.render', { component: 'PromptHint' }, async ($: any, e: any, next: any) => {
    if (!active || !sync || sync.behind > 0 || sync.shiftAlert || !sync.digest) return next(e)
    const tag = '已同步　日報 ' + sync.digest.slice(5)
    return next({ ...e, props: { ...e.props, hint: e.props.hint ? e.props.hint + '　·　' + tag : tag } })
  })

  // ── 2. wiki 新鮮度旁註 ──────────────────────────────────────
  on('tool.call', { tool: 'Read' }, async ($: any, e: any, next: any) => {
    const result = await next(e)
    if (!active || result?.deny || result?.isError) return result
    const rel = relTo(root, e.file_path ?? '')
    if (!isWikiPage(rel)) return result
    try {
      const f = freshness(await $.fs.read(e.file_path), await $.clock.now())
      if (f) $.ui.log(`${rel}：最後新聞更新 ${f.date}（${f.days} 天前）`)
    } catch {
      // 旁註失敗不影響 Read 本身
    }
    return result
  })

  // ── 3. 共用工作樹：Edit／Write 成功後記帳 ────────────────────
  on('tool.call', { tool: ['Edit', 'Write', 'NotebookEdit', 'MultiEdit'] }, async ($: any, e: any, next: any) => {
    const result = await next(e)
    if (!active || result?.deny || result?.isError) return result
    const rel = relTo(root, e.file_path ?? e.notebook_path ?? '')
    if (rel) await addTouched($, [rel])
    return result
  })

  // ── 3. 共用工作樹：Bash／PowerShell 前後比對髒檔，並守 git add／commit ─
  on('tool.call', { tool: ['Bash', 'PowerShell'] }, async ($: any, e: any, next: any) => {
    if (!active) return next(e)
    const command = String(e.command ?? '')
    const before = new Set(await dirty($))

    const calls = gitStageCalls(command)
    if (calls.length) {
      const foreign = await liveForeign($)
      if (foreign.size) {
        // 點名路徑的 commit（`commit -- <路徑>`）只帶走點名的檔，別人放在暫存區的不會跟著進去；
        // 只有不點名的 commit 才會把整個暫存區帶走。commit -a 則帶走所有改過的檔
        const wholeIndex = calls.some((c) => c.sub === 'commit' && !c.pathspecs.length)
        const staged = wholeIndex
          ? (await git($, ['diff', '--cached', '--name-only'])).stdout.split('\n').filter(Boolean)
          : []
        const named = calls.flatMap((c) => c.pathspecs)
        const swept = calls.some((c) => c.all) ? [...before] : [...before].filter((p) => named.some((s) => underSpec(p, s)))
        const candidates = [...new Set([...staged, ...swept])]
        const mine = await touchedOf($, sessionId)
        const hit = foreignHits(candidates, mine, foreign)
        if (hit.files) {
          const own = [...before].filter((p) => mine.has(p)).slice(0, 20)
          $.ui.status(`工作樹：擋下一次 add／commit（${hit.files} 個檔屬另 ${hit.sessions} 個 session）`)
          return {
            deny:
              `這次 add／commit 會納入 ${hit.files} 個別的 session 正在動、你這個 session 沒動過的檔（${hit.sessions} 個 session）。` +
              '只 add 你自己這輪動過的路徑' + (own.length ? '：' + own.join(' ') : '（本 session 尚無記錄的改動）') +
              '。若確定那些檔是你的（例如在本 mod 載入前改的），請使用者自己在終端機 add。',
          }
        }
      }
    }

    const result = await next(e)
    try {
      const fresh = (await dirty($)).filter((p) => !before.has(p))
      await addTouched($, fresh)
    } catch {
      // 歸屬記帳失敗不影響指令結果
    }
    // 會移動 HEAD 或 origin/master 的 git 指令跑完，馬上重算落後／分岔（不 fetch）
    if (sync && /\bgit\b[^\n]*\b(push|pull|merge|rebase|reset|fetch|commit|cherry-pick|checkout|switch)\b/.test(command)) {
      try {
        await checkOrigin($, false)
      } catch {
        // 重算失敗不影響指令結果
      }
    }
    return result
  })
}
