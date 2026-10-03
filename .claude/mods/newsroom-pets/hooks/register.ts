// newsroom-pets：主編或記者用 Edit／Write 寫檔時，在 prompt 上方的提示列畫一隻打字的小角色。
//
// 只觀察、不干預：agent.spawn 與 tool.call 一律 next(e) 原樣放行並回傳 next 的結果，
// 不改派工、不改輸入、不擋任何呼叫。只在 CLAUDE_NEWS 樹上作用。

import { basename, EDITOR, FRAME_MS, HELPER, LINGER_MS, onStage, pixels, reporterOf, SLEEP_FRAME_MS, sleepingPixels, SPRITE_W, toRows } from './lib.ts'
import type { Desk, Who } from './lib.ts'

let active = false
const agents = new Map<string, Who>() // agentId → 記者
const desks = new Map<string, Desk>() // who.id → 桌上在寫什麼
let tick = 0
let timer: { cancel(): void } | null = null

function whoFor(agentId: string | undefined): Who {
  if (!agentId) return EDITOR
  return agents.get(agentId) ?? HELPER
}

// 一支計時器、兩種速度：有人在寫用 FRAME_MS 打字，沒人在寫就降到 SLEEP_FRAME_MS 讓主編睡覺
let speed = 0

function startClock($: any, ms: number) {
  if (timer && speed === ms) return
  timer?.cancel()
  speed = ms
  timer = $.clock.every(ms, async () => {
    tick += 1
    $.ui.invalidate('ui.render')
    if (speed === FRAME_MS && !onStage(desks, await $.clock.now()).length) startClock($, SLEEP_FRAME_MS)
  })
}

async function animate($: any) {
  startClock($, FRAME_MS)
}

export function register(on: any) {
  on('session.start', async ($: any, e: any, next: any) => {
    try {
      const root = await $.session.root()
      active = (await $.fs.exists(root + '/scripts/ingest_gate.py')) && (await $.fs.exists(root + '/wiki/log.md'))
      if (active) startClock($, SLEEP_FRAME_MS)
    } catch {
      active = false
    }
    return next(e)
  })

  // 派工時記下哪個 agentId 是哪類記者（只讀 prompt，不改）
  on('agent.spawn', async ($: any, e: any, next: any) => {
    const result = await next(e)
    const who = active ? reporterOf(String(e.prompt ?? '')) : null
    if (who && result?.agentId) agents.set(result.agentId, who)
    return result
  })

  on('tool.call', { tool: ['Edit', 'Write', 'NotebookEdit', 'MultiEdit'] }, async ($: any, e: any, next: any) => {
    if (!active) return next(e)
    const who = whoFor(e.agentId)
    desks.set(who.id, { who, file: basename(String(e.file_path ?? e.notebook_path ?? '')), until: 0, writing: true })
    $.ui.invalidate('ui.render')
    await animate($)
    try {
      return await next(e)
    } finally {
      const desk = desks.get(who.id)
      if (desk) desks.set(who.id, { ...desk, writing: false, until: (await $.clock.now()) + LINGER_MS })
      $.ui.invalidate('ui.render')
    }
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($: any, e: any, next: any) => {
    if (!active || e.props.hasSurvey) return next(e)
    const stage = onStage(desks, await $.clock.now())
    const { Box, Text } = $.ui.resolve(e)
    const width = SPRITE_W + 2
    const fit = Math.max(1, Math.floor((e.props.bodyColumns ?? 80) / width))
    // 一行半格方塊字＝一串 Text 片段；undefined 的顏色欄不放進 props（多餘的鍵會讓整張圖被退回）
    const line = (segs: { text: string; color?: string; backgroundColor?: string }[], k: number) =>
      Box({
        key: 'px-' + k,
        flexDirection: 'row',
        children: segs.map((s) => {
          const props: Record<string, unknown> = { children: [s.text] }
          if (s.color) props.color = s.color
          if (s.backgroundColor) props.backgroundColor = s.backgroundColor
          return Text(props)
        }),
      })
    if (!stage.length) {
      // 平常：主編縮成 2 行蜷在右下角睡覺
      const nap = Box({
        key: 'nap',
        flexDirection: 'row',
        justifyContent: 'flex-end',
        alignItems: 'flex-end',
        columnGap: 1,
        children: [
          Text({ dimColor: true, children: [EDITOR.name + ' zZ'] }),
          Box({ key: 'nap-px', flexDirection: 'column', children: toRows(sleepingPixels(EDITOR, tick)).map(line) }),
        ],
      })
      const theirs = await next(e)
      return Box({ flexDirection: 'column', children: theirs ? [nap, theirs] : [nap] })
    }
    const cards = stage.slice(0, fit).map((d) =>
      Box({
        key: 'desk-' + d.who.id,
        flexDirection: 'column',
        width,
        children: [
          ...toRows(pixels(d.who, tick, d.writing)).map(line),
          Text({ bold: true, wrap: 'truncate-end', children: [d.who.badge + ' ' + d.who.name] }),
          Text({ dimColor: true, wrap: 'truncate-end', children: [d.writing ? '✎ ' + d.file : '寫好了'] }),
        ],
      }),
    )
    const more = stage.length - cards.length
    const room = Box({
      key: 'newsroom',
      flexDirection: 'row',
      children: more > 0 ? [...cards, Text({ dimColor: true, children: [`…還有 ${more} 位`] })] : cards,
    })
    // 提示列是所有 mod 共用的：把排在後面的 mod 畫的東西一起放進來，不蓋掉它們
    const theirs = await next(e)
    return Box({ flexDirection: 'column', children: theirs ? [room, theirs] : [room] })
  })
}
