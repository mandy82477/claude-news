import { expect, mock, test } from 'claude-code/testing'
import { basename, onStage, pixels, reporterOf, sleepingPixels, toRows, EDITOR, LINGER_MS, SPRITE_H, SPRITE_W } from '../hooks/lib.ts'

const ROOT = '/work/claude-news'
const BAND = {
  plugin: 'newsroom-pets', component: 'AbovePrompt', requestId: 'above', surface: 'desktop',
  viewport: { columns: 100, rows: 30 },
  props: { hasSurvey: false, isWorking: true, maxRows: 10, bodyColumns: 90, scroll: { offset: 0, bodyRows: 10 }, view: {} },
} as const

// 派工範本原文（.claude/skills/wiki-ingest/references/dispatch.md）
const FEATURES = '你是 CLAUDE_NEWS wiki 的「功能」記者。開工前先 Read `.claude/agents/wiki-reporter-features.md`'
const DEVPRACTICE = '你是 CLAUDE_NEWS wiki 的「開發實務（devpractice）」記者。開工前先 Read'
const CLASSIFY = '你是 CLAUDE_NEWS wiki 的分類複核記者。開工前先 Read'

test('reporters are recognised from the real dispatch preambles', async () => {
  expect(reporterOf(FEATURES)).toEqual({ id: 'reporter:功能', name: '功能記者', badge: '🛠️', color: '#378ADD' })
  expect(reporterOf(DEVPRACTICE)?.name).toBe('開發實務記者')
  expect(reporterOf(CLASSIFY)?.badge).toBe('🔍')
  expect(reporterOf('找出所有 hook 檔')).toBe(null)
  expect(basename('C:\\repo\\wiki\\entities\\claude-code.md')).toBe('claude-code.md')
})

test('pixel sprites: right size, animate while writing, half-block rows join cleanly', async () => {
  const who = reporterOf(FEATURES)!
  const g = pixels(who, 0, true)
  expect(g.length).toBe(SPRITE_H)
  for (const row of g) expect(row.length).toBe(SPRITE_W)
  expect(JSON.stringify(pixels(who, 0, true))).not.toBe(JSON.stringify(pixels(who, 1, true)))
  const rows = toRows(g)
  expect(rows.length).toBe(SPRITE_H / 2)
  for (const segs of rows) expect(segs.map((x) => x.text).join('').length).toBe(SPRITE_W)
  expect(rows.flat().some((x) => x.color === '#378ADD')).toBe(true)
  const desks = new Map([
    ['reporter:社群', { who: { id: 'reporter:社群', name: '社群記者', badge: '🌐' }, file: 'a.md', until: 0, writing: true }],
    ['editor', { who: EDITOR, file: 'log.md', until: 5000, writing: false }],
  ])
  expect(onStage(desks, 1000).map((d) => d.who.id)).toEqual(['editor', 'reporter:社群'])
  expect(onStage(desks, 9000).map((d) => d.who.id)).toEqual(['reporter:社群'])
})

function stubs(on: any) {
  on('session.start', () => ({ cwd: ROOT }))
  on('session.root', () => ({ value: ROOT }))
  // e.path 由 engine 轉成絕對路徑，Windows 上是反斜線
  on('fs.exists', ($: any, e: any) => ({ value: /ingest_gate\.py$|wiki[\\/]log\.md$/.test(e.path) }))
  on('agent.spawn', () => ({ model: 'sonnet', agentId: 'agent-features' }))
  on('tool.call', () => ({ result: 'ok' }))
  on('ui.render', () => ({ type: 'Text', props: {}, children: ['other mods'] }))
}

test('a reporter writing shows up, keeps other mods, and leaves after lingering', async ($, on) => {
  const clock = mock.clock(on, { now: 1000 })
  stubs(on)
  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: ROOT })

  const spawned: any = await $.agent.spawn({ tool_use_id: 't1', prompt: FEATURES, description: '功能記者', subagentType: 'general-purpose' })
  expect(spawned.agentId).toBe('agent-features')
  await $.tool.call({ tool: 'Edit', agentId: 'agent-features', file_path: ROOT + '/wiki/entities/claude-code.md', old_string: 'a', new_string: 'b' })

  const ui = await $.ui.mount(BAND)
  expect(await ui.find({ type: 'Text', text: '🛠️ 功能記者' })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: '寫好了' })).toBeDefined()
  expect(await ui.find({ type: 'Text', text: 'other mods' })).toBeDefined()
  await ui.unmount()

  // 色碼要能通過兩種畫面的繪圖驗證：不合法的 prop 會讓整張圖被退回成 engine 自己的版本
  for (const surface of ['terminal', 'desktop'] as const) {
    const u = await $.ui.mount({ ...BAND, surface })
    const px: any = await u.find({ type: 'Text', text: /^▀+$/ })
    expect(px).toBeDefined()
    expect(String(px.props.color)).toMatch(/^#[0-9A-F]{6}$/)
    await u.unmount()
  }

  await clock.advance(LINGER_MS + 1000)
  const later = await $.ui.mount(BAND)
  expect(await later.find({ type: 'Text', text: '🛠️ 功能記者' })).toBeUndefined()
})

test('the main session writing is the editor', async ($, on) => {
  mock.clock(on, { now: 1000 })
  stubs(on)
  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: ROOT })
  await $.tool.call({ tool: 'Write', file_path: ROOT + '/wiki/log.md', content: 'x' })
  const ui = await $.ui.mount(BAND)
  expect(await ui.find({ type: 'Text', text: '🖋️ 主編' })).toBeDefined()
})

test('passes tool calls through untouched', async ($, on) => {
  mock.clock(on, { now: 1000 })
  stubs(on)
  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: ROOT })
  const r = await $.tool.call({ tool: 'Edit', file_path: ROOT + '/x.md', old_string: 'a', new_string: 'b' })
  expect(r).toEqual({ result: 'ok' })
})

test('idle: the editor naps in two rows, and wakes up full size when writing', async ($, on) => {
  mock.clock(on, { now: 1000 })
  stubs(on)
  await $.session.start({ surface: 'desktop', isInteractive: true, cwd: ROOT })
  const idle = await $.ui.mount(BAND)
  expect(await idle.find({ type: 'Text', text: '主編 zZ' })).toBeDefined()
  expect(await idle.find({ type: 'Text', text: 'other mods' })).toBeDefined()
  await idle.unmount()

  await $.tool.call({ tool: 'Write', file_path: ROOT + '/wiki/log.md', content: 'x' })
  const awake = await $.ui.mount(BAND)
  expect(await awake.find({ type: 'Text', text: '主編 zZ' })).toBeUndefined()
  expect(await awake.find({ type: 'Text', text: '🖋️ 主編' })).toBeDefined()
})

test('sleeping sprite is 2 text rows wide enough to stay out of the way', async () => {
  const rows = toRows(sleepingPixels(EDITOR, 0))
  expect(rows.length).toBe(2)
  expect(JSON.stringify(sleepingPixels(EDITOR, 0))).not.toBe(JSON.stringify(sleepingPixels(EDITOR, 3)))
})
