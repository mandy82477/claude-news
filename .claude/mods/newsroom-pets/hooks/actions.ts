// 每種 wiki 操作的動作：從工具呼叫本身（工具名、碰的檔、指令、結果）認出來，不靠猜。

import { basename, pixels, SPRITE_W } from './lib.ts'
import type { Who } from './lib.ts'

export type Action =
  | 'write' | 'read' | 'search' | 'log' | 'shelf' | 'radar' | 'press'
  | 'phone' | 'whistle' | 'check' | 'sweat' | 'red' | 'thumbs' | 'stamp' | 'plane' | 'sweep' | 'busy'

/** 動作 → 名牌下方那行的動詞（後面接檔名或指令摘要） */
export const VERB: Record<Action, string> = {
  write: '✎', read: '翻閱', search: '搜尋', log: '寫日誌', shelf: '整理書架', radar: '雷達掃描',
  press: '印報', phone: '打電話查證', whistle: '派工', check: '檢查中', sweat: '被擋了', red: '閘紅',
  thumbs: '全綠', stamp: '蓋章', plane: '送上線', sweep: '掃地', busy: '忙',
}

const CHECK_RE = /\b(run_tests|ingest_gate|gate_web_build|check_[a-z_]+)\.py\b/
const PRESS_RE = /\b(build_web|news_aggregator|gen_wiki_frontmatter|enrich_attribution_publisher)\b/
const SWEEP_RE = /\b(lint_health|wiki[-_]lint|lint_wiki)\b/

/** 工具呼叫 → 動作與名牌下方要顯示的標籤。rel 是專案相對路徑（Edit／Write／Read 才有）。 */
export function actionOf(tool: string, input: any, rel: string | null): { action: Action; label: string } {
  const file = rel ? basename(rel) : ''
  switch (tool) {
    case 'Edit': case 'Write': case 'NotebookEdit': case 'MultiEdit':
      if (rel === 'wiki/log.md') return { action: 'log', label: 'log.md' }
      if (rel === 'wiki/index.md') return { action: 'shelf', label: 'index.md' }
      if (rel === 'wiki/feature-radar.md') return { action: 'radar', label: 'feature-radar' }
      if (rel && /^news\//.test(rel)) return { action: 'press', label: file }
      return { action: 'write', label: file }
    case 'Read':
      return { action: 'read', label: file }
    case 'Grep': case 'Glob':
      return { action: 'search', label: String(input?.pattern ?? '').slice(0, 16) }
    case 'WebFetch': case 'WebSearch':
      return { action: 'phone', label: tool === 'WebSearch' ? String(input?.query ?? '').slice(0, 16) : hostOf(input?.url) }
    case 'Agent': case 'Task':
      return { action: 'whistle', label: String(input?.description ?? '').slice(0, 16) }
    case 'Bash': case 'PowerShell': {
      const cmd = String(input?.command ?? '')
      const script = cmd.match(/([\w-]+\.py)\b/)?.[1] ?? ''
      if (/\bgit\b[^;&|\n]*\bpush\b/.test(cmd)) return { action: 'plane', label: 'git push' }
      if (/\bgit\b[^;&|\n]*\bcommit\b/.test(cmd)) return { action: 'stamp', label: 'git commit' }
      if (CHECK_RE.test(cmd)) return { action: 'check', label: cmd.match(CHECK_RE)![0] }
      if (/\bwiki_search\.py\b/.test(cmd)) return { action: 'search', label: 'wiki_search' }
      if (SWEEP_RE.test(cmd)) return { action: 'sweep', label: script || 'lint' }
      if (PRESS_RE.test(cmd)) return { action: 'press', label: script || cmd.match(PRESS_RE)![0] }
      return { action: 'busy', label: script || (cmd.trim().split(/\s+/)[0] ?? '').slice(0, 16) }
    }
    default:
      return { action: 'busy', label: tool }
  }
}

function hostOf(url: unknown): string {
  try {
    return new URL(String(url)).host.slice(0, 16)
  } catch {
    return 'web'
  }
}

/**
 * 呼叫結束後的結果動作：被擋（deny）或出錯 → sweat「被擋了」；檢查腳本輸出看得出紅綠時 → red「閘紅」／thumbs「全綠」。
 * Bash 結果的型別官方未定（types 的 BuiltinToolResults 為空），只讀得到的欄位才用。
 */
export function outcomeOf(action: Action, result: any): Action | null {
  if (!result) return null
  if (result.deny || result.isError) return 'sweat'
  if (action !== 'check') return null
  const text = [result.stdout, result.stderr, typeof result.result === 'string' ? result.result : '']
    .filter((x) => typeof x === 'string').join('\n')
  if (/FAIL|❌|FAILED|exit=?1\b/.test(text)) return 'red'
  if (/\bOK\b|✅|全數通過|全綠/.test(text)) return 'thumbs'
  return null
}

// ── 像素 ────────────────────────────────────────────────────────

type Px = string | null
const W = '#F1EFE8', P = '#185FA5', R = '#E24B4A', G = '#639922', Y = '#EF9F27', S = '#B4B2A9'
const B = '#378ADD', K = '#444441', D = '#888780'

function put(g: Px[][], pts: [number, number][], c: Px) {
  for (const [r, x] of pts) if (g[r] && x >= 0 && x < SPRITE_W) g[r][x] = c
}

/** 一隻角色做某個動作的第 tick 格（12×8 像素）。身體沿用 lib 的 pixels，再疊道具。 */
export function actionPixels(who: Who, action: Action, tick: number): Px[][] {
  const typing = action === 'write' || action === 'log' || action === 'press' || action === 'stamp' || action === 'busy'
  const g = pixels(who, tick, typing || action === 'shelf' || action === 'whistle' || action === 'plane')
  // 預設 pixels 會畫桌子和紙；不需要桌子的動作先清掉最後一列與道具欄
  const clearProps = () => { for (let r = 0; r < 8; r++) for (const x of [10, 11]) g[r][x] = null }
  const t = tick
  switch (action) {
    case 'write': case 'busy':
      break
    case 'read':
      clearProps(); for (let x = 0; x < 10; x++) g[7][x] = null
      put(g, [[4, 9], [4, 10], [5, 9], [5, 10], [6, 9], [6, 10]], W); put(g, [[4 + (t % 3), 11]], t % 2 ? S : W)
      break
    case 'search': {
      clearProps(); for (let x = 0; x < 10; x++) g[7][x] = null
      const x = t % 4 < 2 ? 9 : 10
      put(g, [[3, x], [3, x + 1], [4, x], [4, x + 1]], B); put(g, [[5, Math.min(11, x + 1)]], K)
      break
    }
    case 'log':
      clearProps(); put(g, [[6, 9], [6, 10], [6, 11]], Y); put(g, [[5, 10 + (t % 2)]], P)
      break
    case 'shelf': {
      clearProps(); for (let x = 0; x < 10; x++) g[7][x] = null
      const col = [R, B, G, Y]
      for (let i = 0; i < 4; i++) put(g, [[i <= t % 5 ? 4 : 6, Math.min(11, 8 + i)]], i <= t % 5 ? col[i] : null)
      put(g, [[7, 8], [7, 9], [7, 10], [7, 11]], D)
      break
    }
    case 'radar': {
      clearProps(); for (let x = 0; x < 10; x++) g[7][x] = null
      const ring: [number, number][] = [[0, 10], [0, 11], [1, 11], [2, 11], [2, 10], [1, 10]]
      put(g, [ring[t % 6], [1, 10]], G)
      break
    }
    case 'press':
      clearProps(); put(g, [[3, 10], [3, 11], [4, 10], [4, 11]], K); put(g, [[5 - (t % 3), 11]], W)
      break
    case 'phone':
      clearProps(); for (let x = 0; x < 10; x++) g[7][x] = null
      put(g, [[1, 9], [2, 9], [3, 9]], K); put(g, t % 2 ? [[0, 10], [1, 11]] : [[1, 10], [0, 11]], S)
      break
    case 'whistle':
      clearProps(); for (let x = 0; x < 10; x++) g[7][x] = null
      put(g, [[3, 9], [3, 10]], Y); put(g, [[2 + (t % 2), 11]], S)
      break
    case 'check':
      clearProps(); for (let x = 0; x < 10; x++) g[7][x] = null
      put(g, [[3, 9], [3, 10], [4, 9], [4, 10], [5, 9], [5, 10]], W)
      if (t % 4 > 0) put(g, [[4, 9]], G)
      if (t % 4 > 1) put(g, [[3, 10]], G)
      break
    case 'thumbs':
      clearProps(); for (let x = 0; x < 10; x++) g[7][x] = null
      put(g, [[2, 10], [3, 10], [3, 11], [4, 10], [4, 11]], G)
      break
    case 'sweat': case 'red':
      clearProps(); for (let x = 0; x < 10; x++) g[7][x] = null
      put(g, [[1, 10], [2, 10]], t % 2 ? B : null); put(g, [[3, 10], [3, 11], [4, 10], [4, 11]], R)
      break
    case 'stamp':
      clearProps(); put(g, [[t % 2 ? 4 : 5, 10], [t % 2 ? 4 : 5, 11]], R); put(g, [[6, 10], [6, 11]], W)
      break
    case 'plane':
      clearProps(); for (let x = 0; x < 10; x++) g[7][x] = null
      put(g, [[Math.max(0, 3 - (t % 4)), Math.min(11, 8 + (t % 4))]], W)
      break
    case 'sweep':
      clearProps(); for (let x = 0; x < 10; x++) g[7][x] = null
      put(g, [[4, 9], [5, 10], [6, t % 2 ? 11 : 10]], Y); put(g, [[7, (t % 3) + 8]], S)
      break
  }
  return g
}

/** Claude 在工作、但還沒碰到任何工具：主編醒著坐在角落想事情（2 行，與睡姿同大小）。 */
export function thinkingPixels(who: Who, tick: number): Px[][] {
  const _ = null, C = who.color, H = who.hat ?? C, E = '#2C2C2A'
  const e = tick % 9 === 0 ? C : E
  const g: Px[][] = [
    [_, _, H, H, H, H, _, _, _, _],
    [_, C, e, C, C, e, C, _, _, _],
    [_, C, C, C, C, C, C, _, _, _],
    [D, C, C, C, C, C, C, C, D, _],
  ]
  put(g, [[0, 7 + (tick % 3)]], S)
  return g
}
