// newsroom-pets：主編與記者每做一種 wiki 操作，就在 prompt 上方的提示列做對應的小動作；
// 平常主編縮成 2 行睡覺，Claude 在想事情時醒著坐在角落。
//
// 只觀察、不干預：agent.spawn 與 tool.call 一律回傳 next(e) 的結果，不改派工、不改輸入、
// 不擋任何呼叫。只在 CLAUDE_NEWS 樹上作用。動作對照見 actions.ts 與 README。

import { actionOf, actionPixels, outcomeOf, thinkingPixels, VERB } from './actions.ts'
import type { Action } from './actions.ts'
import { EDITOR, FRAME_MS, HELPER, LINGER_MS, onStage, reporterOf, SLEEP_FRAME_MS, sleepingPixels, SPRITE_W, toRows, toSvg } from './lib.ts'
import type { Px } from './lib.ts'
import type { Desk, Who } from './lib.ts'

type Stage = Desk & { action: Action }

let active = false
let root = ''
const agents = new Map<string, Who>() // agentId → 記者
const desks = new Map<string, Stage>() // who.id → 正在做什麼
let tick = 0
let timer: { cancel(): void } | null = null
let speed = 0
const PX_SIZE = 8 // 桌面版 SVG 每像素幾個 CSS px，約與終端機半格方塊同大

function whoFor(agentId: string | undefined): Who {
  if (!agentId) return EDITOR
  return agents.get(agentId) ?? HELPER
}

function relOf(path: unknown): string | null {
  if (typeof path !== 'string' || !path) return null
  const norm = (p: string) => p.replace(/\\/g, '/').replace(/\/+$/, '')
  const p = norm(path)
  const r = norm(root)
  if (!/^([A-Za-z]:)?\//.test(p)) return p.replace(/^\.\//, '')
  return p.toLowerCase().startsWith(r.toLowerCase() + '/') ? p.slice(r.length + 1) : null
}

// 一支計時器、兩種速度：有人在台上用 FRAME_MS，沒人就降到 SLEEP_FRAME_MS
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

export function register(on: any) {
  on('session.start', async ($: any, e: any, next: any) => {
    try {
      root = await $.session.root()
      active = (await $.fs.exists(root + '/scripts/ingest_gate.py')) && (await $.fs.exists(root + '/wiki/log.md'))
      if (active) startClock($, SLEEP_FRAME_MS)
    } catch {
      active = false
    }
    return next(e)
  })

  // 派工時記下哪個 agentId 是哪類記者（只讀 agent 類型與 prompt，不改）
  on('agent.spawn', async ($: any, e: any, next: any) => {
    const result = await next(e)
    const who = active ? reporterOf(String(e.prompt ?? ''), e.subagentType) : null
    if (who && result?.agentId) agents.set(result.agentId, who)
    return result
  })

  // 每一次工具呼叫：開始時上台做動作，結束後依結果（被擋、閘紅綠）換成結果動作再停留一下
  on('tool.call', async ($: any, e: any, next: any) => {
    if (!active) return next(e)
    const who = whoFor(e.agentId)
    let start: { action: Action; label: string }
    try {
      start = actionOf(String(e.tool ?? ''), e, relOf(e.file_path ?? e.notebook_path))
    } catch {
      return next(e)
    }
    desks.set(who.id, { who, file: start.label, until: 0, writing: true, action: start.action })
    $.ui.invalidate('ui.render')
    startClock($, FRAME_MS)
    let result: any
    try {
      result = await next(e)
      return result
    } finally {
      try {
        const after = outcomeOf(start.action, result)
        const now = await $.clock.now()
        const cur = desks.get(who.id)
        // 同一角色可能已開始下一個動作；只收尾自己這一個
        if (cur && cur.action === start.action && cur.file === start.label) {
          desks.set(who.id, { ...cur, writing: false, until: now + LINGER_MS, action: after ?? start.action })
        }
        $.ui.invalidate('ui.render')
      } catch {
        // 動畫收尾失敗不影響工具結果
      }
    }
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($: any, e: any, next: any) => {
    if (!active || e.props.hasSurvey) return next(e)
    const stage = onStage(desks, await $.clock.now()) as Stage[]
    const els = $.ui.resolve(e)
    const { Box, Text } = els
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
    // 終端機以外的介面（桌面版等）沒有等寬字格，半格方塊字會一列列錯開：整張像素圖畫成一張 SVG。
    // 用 surface 判斷而非 els.Svg：終端機的元件表也給 Svg，但畫出來是空的
    const sprite = (px: Px[][], key: string, alt: string) =>
      e.surface !== 'terminal' && els.Svg
        ? Box({ key, children: [els.Svg({ source: toSvg(px, PX_SIZE), alt })] })
        : Box({ key, flexDirection: 'column', children: toRows(px).map(line) })
    const theirs = await next(e)
    const withTheirs = (mine: any) => Box({ flexDirection: 'column', children: theirs ? [mine, theirs] : [mine] })

    if (!stage.length) {
      // 沒人在做事：Claude 在工作就醒著想事情，否則睡覺。都只佔 2 行、靠右
      const thinking = !!e.props.isWorking
      const px = thinking ? thinkingPixels(EDITOR, tick) : sleepingPixels(EDITOR, tick)
      return withTheirs(Box({
        key: 'nap',
        flexDirection: 'row',
        justifyContent: 'flex-end',
        alignItems: 'flex-end',
        columnGap: 1,
        children: [
          Text({ dimColor: true, children: [EDITOR.name + (thinking ? ' …' : ' zZ')] }),
          sprite(px, 'nap-px', EDITOR.name + (thinking ? '在想事情' : '在睡覺')),
        ],
      }))
    }

    const width = SPRITE_W + 2
    const fit = Math.max(1, Math.floor((e.props.bodyColumns ?? 80) / width))
    const cards = stage.slice(0, fit).map((d) =>
      Box({
        key: 'desk-' + d.who.id,
        flexDirection: 'column',
        width,
        children: [
          sprite(actionPixels(d.who, d.action, tick), 'px-' + d.who.id, d.who.name + ' ' + VERB[d.action]),
          Text({ bold: true, wrap: 'truncate-end', children: [d.who.badge + ' ' + d.who.name] }),
          Text({ dimColor: true, wrap: 'truncate-end', children: [VERB[d.action] + (d.file ? ' ' + d.file : '')] }),
        ],
      }),
    )
    const more = stage.length - cards.length
    return withTheirs(Box({
      key: 'newsroom',
      flexDirection: 'row',
      children: more > 0 ? [...cards, Text({ dimColor: true, children: [`…還有 ${more} 位`] })] : cards,
    }))
  })
}
