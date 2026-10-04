import { expect, mock, test } from 'claude-code/testing'

const ROOT = '/work/claude-news'

// 一個假的 git：依 argv 回答，讓測試決定落後幾筆、髒檔有哪些
function fakeGit(state: { behind: number; dirty: string[]; staged?: string[]; log?: string }) {
  return ($: any, e: any) => {
    const a = e.argv.slice(1).join(' ')
    const out = (stdout: string) => ({ value: { exitCode: 0, stdout, stderr: '' } })
    if (a.startsWith('fetch')) return out('')
    if (a.startsWith('rev-list')) return out(`0\t${state.behind}\n`)
    if (a.startsWith('log -1')) return out('wiki: auto-ingest 2026-10-02\n')
    if (a.startsWith('ls-tree')) return out('news/2026-10-01.md\nnews/2026-10-02.md\n')
    if (a.startsWith('show')) return out(state.log ?? '')
    if (a.startsWith('branch -r')) return out('')
    if (a.startsWith('status')) return out(state.dirty.map((p) => ' M ' + p).join('\n'))
    if (a.startsWith('diff --cached')) return out((state.staged ?? []).join('\n'))
    if (a.startsWith('pull')) return out('')
    return out('')
  }
}

const statusLines: unknown[] = []

function stubCommon(on: any, saved: Map<string, unknown>, inTree = true) {
  on('session.start', () => ({ cwd: ROOT }))
  on('session.root', () => ({ value: ROOT }))
  on('session.id', () => ({ value: 'me' }))
  // e.path 由 engine 轉成絕對路徑，Windows 上是反斜線
  on('fs.exists', ($: any, e: any) => ({ value: inTree && /ingest_gate\.py$|wiki[\\/]log\.md$/.test(e.path) }))
  on('store.get', ($: any, e: any) => ({ value: saved.get(e.key) }))
  on('store.set', ($: any, e: any) => {
    saved.set(e.key, e.value)
    return { value: undefined }
  })
  on('store.delete', ($: any, e: any) => {
    saved.delete(e.key)
    return { value: undefined }
  })
  on('store.keys', () => ({ value: [...saved.keys()] }))
  on('ui.toast', () => ({ value: undefined }))
  on('ui.status', ($: any, e: any) => {
    statusLines.push(e.text)
    return { value: undefined }
  })
  on('ui.log', () => ({ value: undefined }))
  on('tool.call', () => ({ result: 'ok' }))
}

const BAND = {
  plugin: 'news-console', component: 'AbovePrompt', requestId: 'above', surface: 'desktop',
  viewport: { columns: 100, rows: 30 },
  props: { hasSurvey: false, isWorking: false, maxRows: 10, bodyColumns: 90, scroll: { offset: 0, bodyRows: 10 }, view: {} },
} as const

test('behind origin: band with pull button, and one context line for Claude', async ($, on) => {
  const clock = mock.clock(on, { now: Date.UTC(2026, 9, 3, 9) })
  const saved = new Map<string, unknown>()
  stubCommon(on, saved)
  on('process.run', fakeGit({ behind: 54, dirty: [] }))
  on('prompt.submit', ($: any, e: any) => ({ text: e.text, context: e.context }))
  on('ui.render', () => ({ type: 'Text', props: {}, children: ['engine'] }))

  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: ROOT })
  await clock.advance(2000)

  const ui = await $.ui.mount(BAND)
  expect(await ui.find({ type: 'Text', text: /本機落後 origin 54 筆/ })).toBeDefined()
  expect(await ui.find({ key: 'pull' })).toBeDefined()

  const sent: any = await $.prompt.submit({ text: 'wiki 裡 X 怎麼說' })
  expect(String(sent.context)).toMatch(/落後 origin\/master 54 筆/)
})

test('synced: band draws nothing of its own', async ($, on) => {
  const clock = mock.clock(on, { now: Date.UTC(2026, 9, 3, 9) })
  const saved = new Map<string, unknown>()
  stubCommon(on, saved)
  on('process.run', fakeGit({ behind: 0, dirty: [] }))
  on('ui.render', () => ({ type: 'Text', props: {}, children: ['engine'] }))

  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: ROOT })
  await clock.advance(2000)
  const ui = await $.ui.mount(BAND)
  expect(await ui.find({ type: 'Text', text: 'engine' })).toBeDefined()
  expect(await ui.find({ key: 'pull' })).toBeUndefined()
})

test('git add of another live session\'s file is denied with counts only', async ($, on) => {
  const clock = mock.clock(on, { now: Date.UTC(2026, 9, 3, 9) })
  const saved = new Map<string, unknown>([
    ['alive:other', Date.UTC(2026, 9, 3, 8, 50)],
    ['touched:other', ['wiki/their.md']],
    ['touched:me', ['wiki/mine.md']],
  ])
  stubCommon(on, saved)
  on('process.run', fakeGit({ behind: 0, dirty: ['wiki/their.md', 'wiki/mine.md'] }))

  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: ROOT })
  await clock.advance(10)
  const denied: any = await $.tool.call({ tool: 'Bash', command: 'git add wiki/ && git commit -m x' })
  expect(String(denied.deny)).toMatch(/1 個別的 session/)
  expect(String(denied.deny)).not.toMatch(/their\.md/)
  expect(String(denied.deny)).toMatch(/wiki\/mine\.md/)

  const ok: any = await $.tool.call({ tool: 'Bash', command: 'git add wiki/mine.md && git commit -m x' })
  expect(ok.deny).toBeUndefined()
})

test('a stale session no longer blocks, and edits are recorded as mine', async ($, on) => {
  const clock = mock.clock(on, { now: Date.UTC(2026, 9, 3, 9) })
  const saved = new Map<string, unknown>([
    ['alive:old', Date.UTC(2026, 9, 3, 6)],
    ['touched:old', ['wiki/their.md']],
  ])
  stubCommon(on, saved)
  on('process.run', fakeGit({ behind: 0, dirty: ['wiki/their.md'] }))

  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: ROOT })
  await clock.advance(10)
  const ok: any = await $.tool.call({ tool: 'Bash', command: 'git add wiki/' })
  expect(ok.deny).toBeUndefined()

  await $.tool.call({ tool: 'Edit', file_path: ROOT + '/wiki/new.md', old_string: 'a', new_string: 'b' })
  expect(saved.get('p:me:wiki/new.md')).toBe(1)
})

test('parallel edits in one session are all recorded (no read-modify-write loss)', async ($, on) => {
  const clock = mock.clock(on, { now: Date.UTC(2026, 9, 3, 9) })
  const saved = new Map<string, unknown>([
    ['alive:other', Date.UTC(2026, 9, 3, 8, 50)],
    // 另一個 session 的 Bash 前後比對把本 session 子代理改的檔誤記成它的
    ['touched:other', ['wiki/a.md', 'wiki/b.md', 'wiki/c.md']],
  ])
  stubCommon(on, saved)
  on('process.run', fakeGit({ behind: 0, dirty: ['wiki/a.md', 'wiki/b.md', 'wiki/c.md'] }))

  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: ROOT })
  await clock.advance(10)
  // 三位記者同一時刻各自 Edit（同一個 sessionId）
  await Promise.all(['a', 'b', 'c'].map((n) =>
    $.tool.call({ tool: 'Edit', file_path: ROOT + '/wiki/' + n + '.md', old_string: 'x', new_string: 'y' })))
  const ok: any = await $.tool.call({ tool: 'Bash', command: 'git add wiki/a.md wiki/b.md wiki/c.md && git commit -m x' })
  expect(ok.deny).toBeUndefined()
})

test('per-file keys of a session dead for a day are pruned at start', async ($, on) => {
  mock.clock(on, { now: Date.UTC(2026, 9, 5, 9) })
  const saved = new Map<string, unknown>([
    ['alive:gone', Date.UTC(2026, 9, 3, 9)],
    ['p:gone:wiki/x.md', 1],
  ])
  stubCommon(on, saved)
  on('process.run', fakeGit({ behind: 0, dirty: [] }))
  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: ROOT })
  expect(saved.has('p:gone:wiki/x.md')).toBe(false)
  expect(saved.has('alive:gone')).toBe(false)
})

test('outside the CLAUDE_NEWS tree the mod is inert', async ($, on) => {
  const saved = new Map<string, unknown>()
  stubCommon(on, saved, false)
  on('process.run', () => ({ deny: 'no process should run' }))

  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/other' })
  const r: any = await $.tool.call({ tool: 'Bash', command: 'git add .' })
  expect(r).toEqual({ result: 'ok' })
  expect(saved.size).toBe(0)
})

test('status line always says where sync stands', async ($, on) => {
  const clock = mock.clock(on, { now: Date.UTC(2026, 9, 3, 9) })
  const saved = new Map<string, unknown>()
  stubCommon(on, saved)
  on('process.run', fakeGit({ behind: 0, dirty: [] }))
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: ROOT })
  await clock.advance(2000)
  expect(statusLines.at(-1)).toBe('news ✓ 已同步　日報 10-02')
})
