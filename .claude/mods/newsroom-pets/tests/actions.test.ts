import { expect, mock, test } from 'claude-code/testing'
import { actionOf, actionPixels, outcomeOf, thinkingPixels } from '../hooks/actions.ts'
import { EDITOR, SPRITE_H, SPRITE_W, toRows } from '../hooks/lib.ts'

test('every wiki operation maps to its own action', async () => {
  const cases: [string, any, string | null, string][] = [
    ['Edit', {}, 'wiki/entities/claude-code.md', 'write'],
    ['Edit', {}, 'wiki/log.md', 'log'],
    ['Edit', {}, 'wiki/index.md', 'shelf'],
    ['Edit', {}, 'wiki/feature-radar.md', 'radar'],
    ['Write', {}, 'news/2026-10-03.md', 'press'],
    ['Read', {}, 'wiki/topics/x.md', 'read'],
    ['Grep', { pattern: 'Opus 5.5' }, null, 'search'],
    ['Glob', { pattern: 'wiki/**' }, null, 'search'],
    ['WebFetch', { url: 'https://platform.claude.com/pricing' }, null, 'phone'],
    ['WebSearch', { query: 'claude code 2.1.288' }, null, 'phone'],
    ['Agent', { description: '功能記者 ingest' }, null, 'whistle'],
    ['Bash', { command: 'python scripts/run_tests.py > /tmp/rt.txt' }, null, 'check'],
    ['Bash', { command: 'python scripts/ingest_gate.py --date 2026-10-03' }, null, 'check'],
    ['Bash', { command: 'git -C REPO add wiki/ && git -C REPO commit -m "wiki: x"' }, null, 'stamp'],
    ['Bash', { command: 'git push' }, null, 'plane'],
    ['Bash', { command: 'python scripts/build_web.py' }, null, 'press'],
    ['Bash', { command: 'python scripts/wiki_search.py "q"' }, null, 'search'],
    ['Bash', { command: 'python scripts/lint_health.py age' }, null, 'sweep'],
    ['Bash', { command: 'ls data/' }, null, 'busy'],
  ]
  for (const [tool, input, rel, want] of cases) expect(actionOf(tool, input, rel).action).toBe(want)
  expect(actionOf('WebFetch', { url: 'https://platform.claude.com/x' }, null).label).toBe('platform.claude.com')
})

test('outcomes: blocked sweats, red gate says 閘紅, green gate gives a thumbs up', async () => {
  expect(outcomeOf('write', { deny: 'nope' })).toBe('sweat')
  expect(outcomeOf('busy', { isError: true })).toBe('sweat')
  expect(outcomeOf('check', { stdout: 'FAILED: 2 個失敗' })).toBe('red')
  expect(outcomeOf('check', { stdout: 'OK: 1162 個測試案例全數通過' })).toBe('thumbs')
  expect(outcomeOf('write', { stdout: 'FAIL in content' })).toBe(null)
  expect(outcomeOf('check', undefined)).toBe(null)
  // tool.call 的 next(e) 實際回的形狀：工具結果包在 result 裡
  expect(outcomeOf('check', { result: { stdout: 'FAILED: 1 個失敗', stderr: '' } })).toBe('red')
  expect(outcomeOf('check', { result: { stdout: 'OK: 全數通過', stderr: '' } })).toBe('thumbs')
})

test('every action draws a full-size sprite that splits into 4 half-block rows', async () => {
  const all = ['write', 'read', 'search', 'log', 'shelf', 'radar', 'press', 'phone', 'whistle', 'check', 'sweat', 'red', 'thumbs', 'stamp', 'plane', 'sweep', 'busy'] as const
  for (const a of all) {
    for (const t of [0, 1, 2, 3]) {
      const g = actionPixels(EDITOR, a, t)
      expect(g.length).toBe(SPRITE_H)
      for (const row of g) expect(row.length).toBe(SPRITE_W)
      for (const segs of toRows(g)) expect(segs.map((s) => s.text).join('').length).toBe(SPRITE_W)
    }
  }
  expect(toRows(thinkingPixels(EDITOR, 0)).length).toBe(2)
  // 讀書、搜尋時戴眼鏡：眼睛那列（第 3 列）出現淡藍鏡片；寫字時沒有
  expect(actionPixels(EDITOR, 'read', 1)[3]).toContain('#B5D4F4')
  expect(actionPixels(EDITOR, 'search', 1)[3]).toContain('#B5D4F4')
  expect(actionPixels(EDITOR, 'write', 1)[3]).not.toContain('#B5D4F4')
})

const ROOT = '/work/claude-news'
const BAND = {
  plugin: 'newsroom-pets', component: 'AbovePrompt', requestId: 'above', surface: 'terminal',
  viewport: { columns: 100, rows: 30 },
  props: { hasSurvey: false, isWorking: true, maxRows: 10, bodyColumns: 90, scroll: { offset: 0, bodyRows: 10 }, view: {} },
} as const

test('main session running scripts wakes the editor with the right verb', async ($, on) => {
  mock.clock(on, { now: 1000 })
  on('session.start', () => ({ cwd: ROOT }))
  on('session.root', () => ({ value: ROOT }))
  on('fs.exists', ($: any, e: any) => ({ value: /ingest_gate\.py$|wiki[\\/]log\.md$/.test(e.path) }))
  on('tool.call', ($: any, e: any) => ({ result: e.tool === 'Bash' ? { stdout: 'OK: 全數通過', stderr: '' } : 'ok' }))
  on('ui.render', () => ({ type: 'Text', props: {}, children: ['other mods'] }))
  await $.session.start({ surface: 'terminal', isInteractive: true, cwd: ROOT })

  const idle = await $.ui.mount(BAND)
  expect(await idle.find({ type: 'Text', text: '主編 …' })).toBeDefined() // isWorking：醒著想事情
  await idle.unmount()

  await $.tool.call({ tool: 'Bash', command: 'python scripts/ingest_gate.py' })
  const ui = await $.ui.mount(BAND)
  expect(await ui.find({ type: 'Text', text: '🖋️ 主編' })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: '全綠 ingest_gate.py' })).toBeDefined()
  await ui.unmount()

  await $.tool.call({ tool: 'Bash', command: 'git push' })
  const ui2 = await $.ui.mount(BAND)
  expect(await ui2.find({ type: 'Text', text: '送上線 git push' })).toBeDefined()
})
