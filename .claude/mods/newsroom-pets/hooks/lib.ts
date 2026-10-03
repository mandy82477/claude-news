// newsroom-pets 的純函式：角色辨識、像素圖與畫格，全部可直接單元測試。

export const LINGER_MS = 3500 // 寫完後角色多留一下，連續 Edit 之間才不會一閃一閃
export const FRAME_MS = 320
export const SLEEP_FRAME_MS = 900 // 睡覺時 zZ 慢慢飄，重畫少

export type Who = { id: string; name: string; badge: string; color: string; hat?: string }

// 顏色取自 Claude 介面色票的 400 階；主編用陶土橘加深色帽
export const EDITOR: Who = { id: 'editor', name: '主編', badge: '🖋️', color: '#D85A30', hat: '#444441' }
export const HELPER: Who = { id: 'helper', name: '小幫手', badge: '🧰', color: '#888780' }

// 派工 prompt 的類別名 → 徽章與顏色（領域 emoji 取自 wiki/index.md 的領域欄）
const CAST: Record<string, { badge: string; color: string }> = {
  功能: { badge: '🛠️', color: '#378ADD' },
  模型: { badge: '🤖', color: '#7F77DD' },
  商業: { badge: '💼', color: '#BA7517' },
  安全政策: { badge: '🏛️', color: '#1D9E75' },
  社群: { badge: '🌐', color: '#D4537E' },
  人物: { badge: '👤', color: '#639922' },
  投資分析: { badge: '💰', color: '#EF9F27' },
  開發實務: { badge: '📓', color: '#5F5E5A' },
  分類複核: { badge: '🔍', color: '#993556' },
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
  const c = CAST[key] ?? { badge: '📰', color: '#888780' }
  return { id: 'reporter:' + key, name: key + '記者', badge: c.badge, color: c.color }
}

export function basename(path: string): string {
  return path.replace(/\\/g, '/').split('/').filter(Boolean).pop() ?? path
}

// ── 像素圖 ──────────────────────────────────────────────────────

const EYE = '#2C2C2A'
const DESK = '#888780'
const PAPER = '#F1EFE8'
const PEN = '#185FA5'
export const SPRITE_W = 12
export const SPRITE_H = 8 // 像素列；畫成 4 行半格方塊字

type Px = string | null

/** 一隻角色的 12×8 像素格。writing 時揮手打字、冒紙張；否則閉眼、頭上飄 z。 */
export function pixels(who: Who, tick: number, writing: boolean): Px[][] {
  const _ = null
  const C = who.color
  const H = who.hat ?? C
  const blink = !writing || tick % 9 === 0
  const e = blink ? C : EYE
  const up = writing && tick % 2 === 0
  const g: Px[][] = [
    [_, _, H, H, H, H, H, H, _, _, _, _],
    [_, C, C, C, C, C, C, C, C, _, _, _],
    [_, C, e, C, C, C, e, C, C, _, _, _],
    [_, C, C, C, C, C, C, C, C, _, _, _],
    [up ? C : _, C, C, C, C, C, C, C, C, up ? _ : C, _, _],
    [up ? _ : C, C, C, C, C, C, C, C, C, up ? C : _, _, _],
    [_, C, _, C, _, _, C, _, C, _, _, _],
    [DESK, DESK, DESK, DESK, DESK, DESK, DESK, DESK, DESK, DESK, writing && tick % 3 !== 0 ? PAPER : _, _],
  ]
  if (writing) {
    g[0][10] = tick % 3 === 1 ? PAPER : _
    g[1][11] = tick % 3 === 2 ? PAPER : _
    g[6][10] = PEN
  } else {
    g[0][10] = tick % 8 < 4 ? PAPER : _
    g[0][11] = tick % 8 >= 4 ? PAPER : _
  }
  return g
}

const ZZZ = '#B4B2A9'

/** 平常的睡姿：10×4 像素（2 行半格方塊字），蜷著、戴帽子，頭頂 z 一上一下飄。 */
export function sleepingPixels(who: Who, tick: number): Px[][] {
  const _ = null
  const C = who.color
  const H = who.hat ?? C
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

/** 還在畫面上的角色（寫到一半，或寫完還在停留期），主編排第一。 */
export function onStage(desks: Map<string, Desk>, now: number): Desk[] {
  return [...desks.values()]
    .filter((d) => d.writing || d.until > now)
    .sort((a, b) => (a.who.id === 'editor' ? -1 : b.who.id === 'editor' ? 1 : a.who.name.localeCompare(b.who.name)))
}
