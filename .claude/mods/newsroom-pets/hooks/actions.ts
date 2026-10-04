// 每種 wiki 操作的動作：從工具呼叫本身（工具名、碰的檔、指令、結果）認出來，不靠猜。

import { art, basename, bodyPixels, PALETTE } from './lib.ts'
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
    // 只去掉 www.，不截斷：截成 16 字會變成 'platform.claude.'，看不出是哪個站；卡片寬度由 Text 的 truncate-end 處理
    return new URL(String(url)).host.replace(/^www\./, '')
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
  // tool.call 的 next(e) 回 { result: <工具結果> }；Bash 的工具結果是 { stdout, stderr } 物件，要往內拆一層
  const inner = result.result && typeof result.result === 'object' ? result.result : {}
  const text = [result.stdout, result.stderr, inner.stdout, inner.stderr, typeof result.result === 'string' ? result.result : '']
    .filter((x) => typeof x === 'string').join('\n')
  if (/FAIL|❌|FAILED|exit=?1\b/.test(text)) return 'red'
  if (/\bOK\b|✅|全數通過|全綠/.test(text)) return 'thumbs'
  return null
}

// ── 像素 ────────────────────────────────────────────────────────
// 角色本體 10 格寬（lib 的 bodyPixels，含專屬帽子），右邊 8×8 道具區畫清楚的道具，
// 多數 2 格交替動畫。字元對照見 lib 的 PALETTE（'.' 透明、W 紙、g 淺灰、K 深灰、D 桌…）。

type Px = string | null

// 每個道具 1～2 格；'D' 開頭的最後一列是桌面
const PROPS: Partial<Record<Action, string[][]>> = {
  write: [
    ['.DDDDD..', '.DWWWD..', '.DSSWD..', '.DWWWD.P', '.DSSSDP.', '.DDDDD..', '........', 'KKKKKKKK'],
    ['.DDDDD..', '.DWWWD..', '.DSSSD..', '.DWWWD..', '.DSSWD.P', '.DDDDDP.', '........', 'KKKKKKKK'],
  ],
  read: [
    ['DDDDDDD.', 'DWWWWWD.', 'DSSWSSD.', 'DWWWWWD.', 'DSSWSSD.', 'DSSWSSD.', 'DDDDDDD.', '........'],
    ['DDDD....', 'DWWWDDD.', 'DSSWDSD.', 'DWWWDWD.', 'DSSWDSD.', 'DSSWDDD.', 'DDDD....', '........'],
  ],
  search: [
    ['........', '.KKKK...', 'KBBBBK..', 'KBWBBK..', '.KKKK...', '....KK..', '.....KK.', '........'],
    ['........', '...KKKK.', '..KBBBBK', '..KBWBBK', '...KKKK.', '......KK', '.......K', '........'],
  ],
  log: [
    ['.....W..', '....WP..', '...WP...', '..P.....', 'YWWWWWWY', 'YWggWggY', 'YYYYYYYY', 'DDDDDDDD'],
    ['......W.', '.....WP.', '....WP..', '...P....', 'YWWWWWWY', 'YWgWWggY', 'YYYYYYYY', 'DDDDDDDD'],
  ],
  press: [
    ['KKKKKK..', 'KYYYYK..', 'KKKKKK..', 'KK..KK..', '.DDDD...', '.DSSD...', '........', 'KKKKKKKK'],
    ['KKKKKK..', 'KYYYYK..', 'KKKKKK..', 'KK..KK..', '........', '.DDDD...', '.DSSD...', 'KKKKKKKK'],
  ],
  phone: [
    ['KK......', 'KKK..B..', '.KK.B...', '..K..B..', '..KK....', '...KKK..', '....KK..', '........'],
    ['KK....B.', 'KKK..B.B', '.KK.B..B', '..K..B.B', '..KK..B.', '...KKK..', '....KK..', '........'],
  ],
  whistle: [
    ['....Y...', '...YY.S.', 'KYYYY...', 'KYYYY.S.', '...YY...', '....Y...', '........', '........'],
    ['....Y...', '...YY..S', 'KYYYY.S.', 'KYYYY..S', '...YY.S.', '....Y...', '........', '........'],
  ],
  thumbs: [
    ['........', '......GG', '.....GG.', 'GG..GG..', '.GGGG...', '..GG....', '........', '........'],
    ['Y.......', '......GG', '.....GG.', 'GG..GG.Y', '.GGGG...', '..GG....', '.....Y..', '........'],
  ],
  red: [
    ['RR....RR', '.RR..RR.', '..RRRR..', '...RR...', '..RRRR..', '.RR..RR.', 'RR....RR', '........'],
    ['........', '.RR..RR.', '..RRRR..', '...RR...', '..RRRR..', '.RR..RR.', '........', '........'],
  ],
  sweat: [
    ['..RRRR..', '.RRRRRR.', 'RRRRRRRR', 'RWWWWWWR', 'RRRRRRRR', '.RRRRRR.', '..RRRR..', '...KK...'],
    ['..RRRR..', '.RRRRRR.', 'RRRRRRRR', 'RWWWWWWR', 'RRRRRRRR', '.RRRRRR.', '..RRRR..', '...KK...'],
  ],
  stamp: [
    ['..KKKK..', '...KK...', '..RRRR..', '........', '.DDDDDD.', '.DWWWWD.', '.DDDDDD.', 'KKKKKKKK'],
    ['........', '..KKKK..', '...KK...', '..RRRR..', '.DRRRRD.', '.DWWWWD.', '.DDDDDD.', 'KKKKKKKK'],
  ],
  sweep: [
    ['.....O..', '....O...', '...O....', '..O.....', '.YYY....', 'YYYYY.S.', '......SS', 'DDDDDDDD'],
    ['..O.....', '...O....', '....O...', '.....O..', '....YYY.', '.S.YYYYY', 'SS......', 'DDDDDDDD'],
  ],
  busy: [
    ['........', '.KKKKKK.', '.KBBBBK.', '.KBLBBK.', '.KBBBBK.', '.KKKKKK.', 'KKKKKKKK', '........'],
    ['........', '.KKKKKK.', '.KBBBBK.', '.KBBBBK.', '.KBLBBK.', '.KKKKKK.', 'KKKKKKKK', '........'],
  ],
}

// 會隨 tick 變化的道具：用程式算
function generatedProp(action: Action, t: number): string[] | null {
  if (action === 'shelf') {
    // 書架：書一本本排上去
    const colors = 'RBGYpKBR'
    const n = t % 9
    const row = (from: number) => 'O' + [...Array(6)].map((_, i) => (from + i < n ? colors[(from + i) % colors.length] : '.')).join('') + 'O'
    return ['OOOOOOOO', row(0), row(0), 'OOOOOOOO', row(6), row(6), 'OOOOOOOO', '........']
  }
  if (action === 'radar') {
    // 雷達：綠色圓框，掃描線繞圈
    const g = ['..GGGG..', '.G....G.', 'G......G', 'G......G', 'G......G', 'G......G', '.G....G.', '..GGGG..'].map((r) => [...r])
    const sweeps: [number, number][][] = [
      [[3, 4], [2, 4], [1, 4]], [[3, 4], [2, 5], [1, 6]], [[4, 4], [4, 5], [4, 6]], [[4, 4], [5, 5], [6, 6]],
      [[4, 3], [5, 3], [6, 3]], [[4, 3], [5, 2], [6, 1]], [[3, 3], [3, 2], [3, 1]], [[3, 3], [2, 2], [1, 1]],
    ]
    for (const [r, c] of sweeps[t % 8]) g[r][c] = 'L'
    if (t % 3 === 0) g[2][5] = 'Y' // 偵測到新功能的光點
    return g.map((r) => r.join(''))
  }
  if (action === 'check') {
    // 夾板：一項項打勾
    const n = t % 4
    const line = (i: number) => (i < n ? 'OWGWSSWO' : 'OWSWSSWO')
    return ['..KKKK..', 'OOOOOOOO', line(0), 'OWWWWWWO', line(1), 'OWWWWWWO', line(2), 'OOOOOOOO']
  }
  if (action === 'plane') {
    // 紙飛機：由左下往右上飛出
    const pos = t % 6
    const g = [...Array(8)].map(() => [...'........'])
    const x0 = pos, y0 = 6 - pos
    const shape: [number, number][] = [[0, 0], [0, 1], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1]]
    for (const [dy, dx] of shape) {
      const y = y0 + dy - 1, x = x0 + dx
      if (y >= 0 && y < 8 && x >= 0 && x < 8) g[y][x] = 'B'
    }
    if (x0 > 0 && y0 + 1 < 8) g[y0 + 1][Math.max(0, x0 - 1)] = 'S' // 尾跡
    return g.map((r) => r.join(''))
  }
  return null
}

/** 一隻角色做某個動作的第 tick 格（18×8 像素）：左邊本體（揮手或靜坐），右邊道具。 */
export function actionPixels(who: Who, action: Action, tick: number): Px[][] {
  const waving = action !== 'read' && action !== 'search' && action !== 'phone' && action !== 'red' && action !== 'sweat'
  const glasses = action === 'read' || action === 'search'
  const body = bodyPixels(who, tick, waving, false, glasses)
  const frames = PROPS[action]
  const propRows = generatedProp(action, tick) ?? (frames ? frames[tick % frames.length] : Array(8).fill('........'))
  const prop = art(propRows)
  return body.map((row, r) => [...row, ...prop[r]])
}

/** Claude 在工作、但還沒碰到任何工具：主編醒著坐在角落想事情（2 行，與睡姿同大小）。 */
export function thinkingPixels(who: Who, tick: number): Px[][] {
  const _ = null, C = who.color, H = who.hatColor, E = PALETTE.E, D = PALETTE.D, S = PALETTE.g
  const e = tick % 9 === 0 ? C : E
  const g: Px[][] = [
    [_, _, H, H, H, H, _, _, _, _],
    [_, C, e, C, C, e, C, _, _, _],
    [_, C, C, C, C, C, C, _, _, _],
    [D, C, C, C, C, C, C, C, D, _],
  ]
  g[0][7 + (tick % 3)] = S
  return g
}
