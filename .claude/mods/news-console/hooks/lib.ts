// news-console 的純函式：不碰 $，全部可在 claude plugin test 裡直接單元測試。

export const LIVE_MS = 90 * 60_000 // 與 .claude/hooks/block_foreign_stage.py 的 STALE_MINUTES 同值
export const DEAD_SHIFT_MS = 3 * 3600_000 // 一輪 pipeline 最壞約 2 小時（daily-news-pipeline-cloud 班距註解）

// ── 本機落後 origin ─────────────────────────────────────────────

/** `git rev-list --left-right --count HEAD...origin/master` 的輸出 → { ahead, behind } */
export function parseAheadBehind(stdout: string): { ahead: number; behind: number } | null {
  const m = stdout.trim().match(/^(\d+)\s+(\d+)$/)
  return m ? { ahead: Number(m[1]), behind: Number(m[2]) } : null
}

/**
 * 落後時的那一行說明。本機另有未推的 commit（ahead > 0）時已經分岔，ff-only 不可能成功，
 * 按鈕不該出現——2026-10-04 提示列寫「落後 1 筆」配「拉取（ff-only）」，按了只回一行看不懂的錯。
 */
export function syncSummary(ahead: number, behind: number): { text: string; canFastForward: boolean } {
  if (behind > 0 && ahead > 0) {
    return {
      text: `本機與 origin 分岔：遠端多 ${behind} 筆、本機有 ${ahead} 筆未推。ff-only 拉不了，請請 Claude 合併`,
      canFastForward: false,
    }
  }
  return { text: `本機落後 origin ${behind} 筆`, canFastForward: behind > 0 }
}

/** git pull 失敗時，從 stderr 挑出真正的原因並翻成一句人話（git 第一行常是 hint，不是原因） */
export function explainPullFailure(stderr: string): string {
  if (/would be overwritten by merge|Your local changes/i.test(stderr)) {
    return '工作樹有未 commit 的檔和遠端改到同一批，先 commit 或捨棄那些檔'
  }
  if (/Not possible to fast-forward|divergent|Diverging/i.test(stderr)) {
    return '本機有未推的 commit，和遠端分岔了，ff-only 拉不了'
  }
  if (/untracked working tree files would be/i.test(stderr)) {
    return '有未追蹤的檔和遠端新增的檔同名'
  }
  const line = stderr.split('\n').map((l) => l.trim()).find((l) => /^(fatal|error):/.test(l))
  return line ?? (stderr.split('\n').map((l) => l.trim()).find(Boolean) || '原因不明')
}

/** `git ls-tree --name-only origin/master news/` → 最新日報日期 YYYY-MM-DD */
export function latestDigest(stdout: string): string | null {
  const dates = stdout
    .split('\n')
    .map((l) => l.trim().match(/^news\/(\d{4}-\d{2}-\d{2})\.md$/))
    .filter(Boolean)
    .map((m) => (m as RegExpMatchArray)[1])
    .sort()
  return dates.length ? dates[dates.length - 1] : null
}

// ── 雲端班次 ────────────────────────────────────────────────────

const STARTED = /^\[cloud daily-news-pipeline-cloud STARTED (\d{4}-\d{2}-\d{2})T(\d{2}):(\d{2}):(\d{2})Z\]/

/**
 * 只看 origin/master 上的 task_scheduler.log 與停泊分支，回傳要不要出聲。
 * 設計內的中止不出聲：12Z／17Z 等料中止（抓料晚到是常態）、任何班次的冪等中止。
 */
export function classifyShift(
  logText: string,
  parkedBranches: string[],
  nowMs: number,
): { alert: string | null } {
  if (parkedBranches.length) {
    return { alert: `雲端有 ${parkedBranches.length} 個停泊分支待救回（${parkedBranches[0]}${parkedBranches.length > 1 ? ' 等' : ''}）` }
  }
  const lines = logText.split('\n')
  let start = -1
  for (let i = lines.length - 1; i >= 0; i--) {
    if (STARTED.test(lines[i])) {
      start = i
      break
    }
  }
  if (start < 0) return { alert: null }
  const m = lines[start].match(STARTED) as RegExpMatchArray
  const startedMs = Date.UTC(+m[1].slice(0, 4), +m[1].slice(5, 7) - 1, +m[1].slice(8, 10), +m[2], +m[3], +m[4])
  const hour = Number(m[2])
  const after = lines.slice(start + 1).join('\n')
  const label = `${m[1].slice(5)} ${m[2]}Z 班`
  if (/FAILED/.test(after)) return { alert: `雲端 ${label}失敗：${firstLine(after, /FAILED/)}` }
  if (/Pipeline complete/.test(after)) return { alert: null }
  if (/ABORTED/.test(after)) {
    if (/冪等|already exists/.test(after)) return { alert: null }
    if (/不存在|尚未落地|延遲/.test(after)) {
      return hour >= 22 ? { alert: `雲端 ${label}（最後一班）仍等不到抓料：當日缺報` } : { alert: null }
    }
    return { alert: `雲端 ${label}中止：${firstLine(after, /ABORTED/)}` }
  }
  if (nowMs - startedMs > DEAD_SHIFT_MS) return { alert: `雲端 ${label}開跑後無任何後續（逾 3 小時）：疑似中途死亡` }
  return { alert: null }
}

function firstLine(text: string, re: RegExp): string {
  const line = text.split('\n').find((l) => re.test(l)) ?? ''
  return line.replace(/^\[[^\]]*\]\s*/, '').slice(0, 80)
}

// ── wiki 新鮮度 ─────────────────────────────────────────────────

/** wiki 頁的 frontmatter `last_news_update` 與距今天數；不是 wiki 頁或沒有欄位回 null。 */
export function freshness(text: string, nowMs: number): { date: string; days: number } | null {
  const head = text.slice(0, 4000)
  if (!head.startsWith('---')) return null
  const m = head.match(/^last_news_update:\s*"?(\d{4}-\d{2}-\d{2})"?\s*$/m)
  if (!m) return null
  const [y, mo, d] = m[1].split('-').map(Number)
  const days = Math.floor((nowMs - Date.UTC(y, mo - 1, d)) / 86_400_000)
  return { date: m[1], days }
}

export function isWikiPage(rel: string | null): boolean {
  return !!rel && /^wiki\/.+\.md$/.test(rel)
}

// ── 路徑 ────────────────────────────────────────────────────────

export function relTo(root: string, path: string): string | null {
  const norm = (p: string) => p.replace(/\\/g, '/').replace(/\/+$/, '')
  const r = norm(root)
  let p = norm(path)
  if (!/^([A-Za-z]:)?\//.test(p)) return p.replace(/^\.\//, '')
  const lower = (s: string) => (/^[A-Za-z]:/.test(s) ? s.toLowerCase() : s)
  if (lower(p).startsWith(lower(r) + '/')) return p.slice(r.length + 1)
  return null
}

/** `git status --porcelain -uall` → 髒檔路徑（rename 取新路徑）。 */
export function parsePorcelain(stdout: string): string[] {
  const out: string[] = []
  for (const line of stdout.split('\n')) {
    if (line.length < 4) continue
    let p = line.slice(3)
    const arrow = p.indexOf(' -> ')
    if (arrow >= 0) p = p.slice(arrow + 4)
    out.push(p.replace(/^"|"$/g, ''))
  }
  return out
}

// ── shell 指令裡的 git add／commit ─────────────────────────────

/** 引號感知切段（只認引號外的 ; && || | 換行），再切 token。與 .claude/hooks/_cmdparse.py 同精神、較簡。 */
export function commands(command: string): string[][] {
  const body = command.replace(/<<-?\s*(['"]?)(\w+)\1[^\n]*\n[\s\S]*?\n[ \t]*\2[ \t]*(?=\n|$)/g, '')
  const segs: string[] = []
  let buf = ''
  let q: string | null = null
  for (let i = 0; i < body.length; i++) {
    const c = body[i]
    if (q) {
      buf += c
      if (c === q) q = null
      continue
    }
    if (c === '"' || c === "'") {
      q = c
      buf += c
      continue
    }
    const two = body.slice(i, i + 2)
    if (two === '&&' || two === '||') {
      segs.push(buf)
      buf = ''
      i++
      continue
    }
    if (c === ';' || c === '|' || c === '\n') {
      segs.push(buf)
      buf = ''
      continue
    }
    buf += c
  }
  segs.push(buf)
  return segs.map(tokens).filter((t) => t.length)
}

function tokens(seg: string): string[] {
  const out: string[] = []
  const re = /"([^"]*)"|'([^']*)'|(\S+)/g
  let m: RegExpExecArray | null
  while ((m = re.exec(seg))) out.push(m[1] ?? m[2] ?? m[3])
  return out
}

/**
 * 指令裡每個 git add／commit：{ sub, pathspecs, all }。git 必須是該段的程式名。
 * all：commit 帶 -a／--all（含 -am 這類合寫），會把所有改過的追蹤檔一起 commit。
 */
export function gitStageCalls(command: string): { sub: 'add' | 'commit'; pathspecs: string[]; all: boolean }[] {
  const out: { sub: 'add' | 'commit'; pathspecs: string[]; all: boolean }[] = []
  for (const t of commands(command)) {
    if (!/(^|[\\/])git(\.exe)?$/.test(t[0])) continue
    let i = 1
    while (i < t.length && t[i].startsWith('-')) i += t[i] === '-C' || t[i] === '-c' ? 2 : 1
    const sub = t[i]
    if (sub !== 'add' && sub !== 'stage' && sub !== 'commit') continue
    const rest = t.slice(i + 1)
    const dd = rest.indexOf('--')
    const specs = sub === 'commit'
      ? (dd >= 0 ? rest.slice(dd + 1) : [])
      : rest.filter((a, k) => (dd >= 0 && k > dd) || !a.startsWith('-'))
    const flags = dd >= 0 ? rest.slice(0, dd) : rest
    const all = sub === 'commit' && flags.some((a) => a === '--all' || /^-[A-Za-z]*a/.test(a))
    out.push({ sub: sub === 'commit' ? 'commit' : 'add', pathspecs: specs, all })
  }
  return out
}

export function underSpec(path: string, spec: string): boolean {
  const s = spec.replace(/\\/g, '/').replace(/^\.\//, '').replace(/\/+$/, '')
  if (s === '' || s === '.') return true
  return path === s || path.startsWith(s + '/')
}

/**
 * 這次 add／commit 會納入、屬於別的活著的 session、本 session 沒動過的檔。
 * candidates：會被帶走的 staged（有不點名的 commit 才算）＋ add／commit 點名範圍內的髒檔
 * ＋ commit -a 時的全部髒檔。
 */
export function foreignHits(candidates: string[], mine: Set<string>, foreign: Map<string, Set<string>>) {
  const hits = new Set<string>()
  const sessions = new Set<string>()
  for (const p of candidates) {
    if (mine.has(p)) continue
    for (const [sid, paths] of foreign) {
      if (paths.has(p)) {
        hits.add(p)
        sessions.add(sid)
      }
    }
  }
  return { files: hits.size, sessions: sessions.size }
}
