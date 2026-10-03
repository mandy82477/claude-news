// newsroom-pets 的純函式：角色辨識、像素圖與畫格，全部可直接單元測試。

export const LINGER_MS = 3500 // 做完後角色多留一下，連續呼叫之間才不會一閃一閃
export const FRAME_MS = 320
export const SLEEP_FRAME_MS = 900 // 睡覺時 zZ 慢慢飄，重畫少

export type HatId =
  | 'fedora' | 'hardhat' | 'antenna' | 'tophat' | 'police' | 'cap' | 'newsboy' | 'visor' | 'beanie' | 'deerstalker' | 'band'

export type Who = { id: string; name: string; badge: string; color: string; hat: HatId; hatColor: string }

// 顏色取自 Claude 介面色票的 400 階；主編用陶土橘加深色紳士帽
export const EDITOR: Who = { id: 'editor', name: '主編', badge: '🖋️', color: '#D85A30', hat: 'fedora', hatColor: '#2C2C2A' }
export const HELPER: Who = { id: 'helper', name: '小幫手', badge: '🧰', color: '#888780', hat: 'band', hatColor: '#B4B2A9' }

// 派工 prompt 的類別名 → 徽章、身體色、帽子（領域 emoji 取自 wiki/index.md 的領域欄）
const CAST: Record<string, { badge: string; color: string; hat: HatId; hatColor: string }> = {
  功能: { badge: '🛠️', color: '#378ADD', hat: 'hardhat', hatColor: '#EF9F27' },
  模型: { badge: '🤖', color: '#7F77DD', hat: 'antenna', hatColor: '#E24B4A' },
  商業: { badge: '💼', color: '#BA7517', hat: 'tophat', hatColor: '#2C2C2A' },
  安全政策: { badge: '🏛️', color: '#1D9E75', hat: 'police', hatColor: '#0C447C' },
  社群: { badge: '🌐', color: '#D4537E', hat: 'cap', hatColor: '#ED93B1' },
  人物: { badge: '👤', color: '#639922', hat: 'newsboy', hatColor: '#3B6D11' },
  投資分析: { badge: '💰', color: '#EF9F27', hat: 'visor', hatColor: '#97C459' },
  開發實務: { badge: '📓', color: '#5F5E5A', hat: 'beanie', hatColor: '#B4B2A9' },
  分類複核: { badge: '🔍', color: '#993556', hat: 'deerstalker', hatColor: '#854F0B' },
}

/**
 * 從派工 prompt 認出記者。派工範本（wiki-ingest/references/dispatch.md）的開頭是
 * 「你是 CLAUDE_NEWS wiki 的「功能」記者」或「…的分類複核記者」；認不出回 null。
 */
export function reporterOf(prompt: string): Who | null {
  const m = prompt.match(/你是 CLAUDE_NEWS wiki 的(?:「([^」]+)」|(分類複核))記者/)
  if (!m) return null
  const raw = (m[1] ?? m[2]).replace(/（.*?）/g, '').trim()
  const key = Object.keys(CAST).find((k) => raw.startsWith(k)) ?? raw
  const c = CAST[key] ?? { badge: '📰', color: '#888780', hat: 'band' as HatId, hatColor: '#B4B2A9' }
  return { id: 'reporter:' + key, name: key + '記者', ...c }
}

export function basename(path: string): string {
  return path.replace(/\\/g, '/').split('/').filter(Boolean).pop() ?? path
}

// ── 像素圖 ──────────────────────────────────────────────────────

export type Px = string | null

export const BODY_W = 10 // 角色（含帽子、雙手）
export const PROP_W = 8 // 右邊的道具區
export const SPRITE_W = BODY_W + PROP_W
export const SPRITE_H = 8 // 像素列；畫成 4 行半格方塊字

/** 字元圖的調色盤。C＝角色身體色、H＝帽子色，其餘固定。 */
export const PALETTE: Record<string, string> = {
  E: '#2C2C2A', k: '#2C2C2A', K: '#444441', W: '#F1EFE8', g: '#B4B2A9', D: '#888780', S: '#5F5E5A',
  B: '#378ADD', b: '#0C447C', P: '#185FA5', R: '#E24B4A', G: '#639922', L: '#97C459', Y: '#EF9F27',
  O: '#854F0B', o: '#BA7517', p: '#D4537E', q: '#ED93B1',
}

/** 字元圖 → 像素列。'.'＝透明；不在調色盤的字母從 extra 找。 */
export function art(rows: string[], extra: Record<string, string> = {}): Px[][] {
  return rows.map((r) => [...r].map((ch) => (ch === '.' ? null : extra[ch] ?? PALETTE[ch] ?? null)))
}

// 帽子：2 列 × 10 格。H＝該角色的帽子色
const HATS: Record<HatId, string[]> = {
  fedora: ['...HHHH...', '.HHHHHHHH.'],
  hardhat: ['...HWHH...', '.HHHHHHHH.'],
  antenna: ['....H.....', '....K.....'],
  tophat: ['..HHHHHH..', 'HHHRRRRHHH'],
  police: ['...HYHH...', '.kkkkkkkk.'],
  cap: ['....HHHH..', 'HHHHHHHH..'],
  newsboy: ['..HHHHH.Y.', '.HHHHHHHH.'],
  visor: ['........Y.', 'HHHHHHHH..'],
  beanie: ['....R.....', '..HHHHHH..'],
  deerstalker: ['...HkHH...', 'HHHHHHHHHH'],
  band: ['..........', '..HHHHHH..'],
}

/**
 * 角色本體：10×8 像素。上兩列帽子，下面頭、眼睛、身體、揮動的雙手、腳。
 * wave 時雙手上下交替；blink 由 tick 決定（每 9 格眨一次）。
 */
export function bodyPixels(who: Who, tick: number, wave: boolean, eyesClosed = false): Px[][] {
  const up = wave && tick % 2 === 0
  const eye = eyesClosed || tick % 9 === 0 ? 'C' : 'E'
  const rows = [
    ...HATS[who.hat],
    '.CCCCCCCC.',
    `.C${eye}CCC${eye}CC.`,
    '.CCCCCCCC.',
    `${up ? 'C' : '.'}CCCCCCCC${up ? '.' : 'C'}`,
    `${up ? '.' : 'C'}CCCCCCCC${up ? 'C' : '.'}`,
    '.C.C..C.C.',
  ]
  return art(rows, { C: who.color, H: who.hatColor })
}

/** 本體＋空道具區的 18×8 像素（給沒有道具的場合與測試用）。 */
export function pixels(who: Who, tick: number, writing: boolean): Px[][] {
  return bodyPixels(who, tick, writing, !writing).map((row) => [...row, ...Array(PROP_W).fill(null)])
}

const ZZZ = '#B4B2A9'

/** 平常的睡姿：10×4 像素（2 行半格方塊字），蜷著、戴帽子，頭頂 z 一上一下飄。 */
export function sleepingPixels(who: Who, tick: number): Px[][] {
  const _ = null
  const C = who.color
  const H = who.hatColor
  const DESK = PALETTE.D
  const g: Px[][] = [
    [_, _, _, _, _, _, _, _, _, _],
    [_, _, H, H, H, H, _, _, _, _],
    [_, C, C, C, C, C, C, _, _, _],
    [DESK, C, C, C, C, C, C, C, DESK, _],
  ]
  const k = tick % 6
  if (k < 3) g[0][7 + (k % 2)] = ZZZ
  else g[1][8 + (k % 2)] = ZZZ
  return g
}

export type Seg = { text: string; color?: string; backgroundColor?: string }

/**
 * 像素格 → 每行一串文字片段（半格方塊：上半像素是字色、下半是底色），
 * 同樣式的相鄰字合併成一段，讓 Text 元素數量少。
 */
export function toRows(g: Px[][]): Seg[][] {
  const rows: Seg[][] = []
  for (let r = 0; r < g.length; r += 2) {
    const segs: Seg[] = []
    for (let x = 0; x < g[r].length; x++) {
      const top = g[r][x]
      const bot = g[r + 1]?.[x] ?? null
      let seg: Seg
      if (!top && !bot) seg = { text: ' ' }
      else if (top && bot) seg = { text: '▀', color: top, backgroundColor: bot }
      else if (top) seg = { text: '▀', color: top }
      else seg = { text: '▄', color: bot as string }
      const last = segs[segs.length - 1]
      if (last && last.color === seg.color && last.backgroundColor === seg.backgroundColor && (last.text[0] === seg.text[0])) {
        last.text += seg.text
      } else {
        segs.push(seg)
      }
    }
    rows.push(segs)
  }
  return rows
}

export type Desk = { who: Who; file: string; until: number; writing: boolean }

/** 還在畫面上的角色（做到一半，或做完還在停留期），主編排第一。 */
export function onStage(desks: Map<string, Desk>, now: number): Desk[] {
  return [...desks.values()]
    .filter((d) => d.writing || d.until > now)
    .sort((a, b) => (a.who.id === 'editor' ? -1 : b.who.id === 'editor' ? 1 : a.who.name.localeCompare(b.who.name)))
}
