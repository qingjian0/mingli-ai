export function formatDate(date: string | Date, format: 'full' | 'short' | 'time' = 'full'): string {
  const d = typeof date === 'string' ? new Date(date) : date

  if (format === 'time') {
    return d.toLocaleTimeString('zh-CN', { hour: '2-digit', minute: '2-digit' })
  }

  if (format === 'short') {
    return d.toLocaleDateString('zh-CN', { month: 'short', day: 'numeric' })
  }

  return d.toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}

export function formatRelativeTime(date: string | Date): string {
  const d = typeof date === 'string' ? new Date(date) : date
  const now = new Date()
  const diffMs = now.getTime() - d.getTime()
  const diffSecs = Math.floor(diffMs / 1000)
  const diffMins = Math.floor(diffSecs / 60)
  const diffHours = Math.floor(diffMins / 60)
  const diffDays = Math.floor(diffHours / 24)

  if (diffSecs < 60) return '刚刚'
  if (diffMins < 60) return `${diffMins}分钟前`
  if (diffHours < 24) return `${diffHours}小时前`
  if (diffDays < 7) return `${diffDays}天前`
  return formatDate(d, 'short')
}

export function formatChineseDate(dateStr: string): string {
  const match = dateStr.match(/(\d{4})-(\d{2})-(\d{2})/)
  if (!match) return dateStr

  const [, year, month, day] = match
  const lunarMonths = ['正', '二', '三', '四', '五', '六', '七', '八', '九', '十', '冬', '腊']
  const lunarDays = ['初一', '初二', '初三', '初四', '初五', '初六', '初七', '初八', '初九', '初十',
    '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九', '二十',
    '廿一', '廿二', '廿三', '廿四', '廿五', '廿六', '廿七', '廿八', '廿九', '三十']

  return `${year}年${lunarMonths[parseInt(month) - 1]}月${lunarDays[parseInt(day) - 1]}`
}

export function formatTimeRange(time: string): string {
  const hour = parseInt(time.split(':')[0])

  if (hour >= 23 || hour < 1) return '子时 (23:00-01:00)'
  if (hour >= 1 && hour < 3) return '丑时 (01:00-03:00)'
  if (hour >= 3 && hour < 5) return '寅时 (03:00-05:00)'
  if (hour >= 5 && hour < 7) return '卯时 (05:00-07:00)'
  if (hour >= 7 && hour < 9) return '辰时 (07:00-09:00)'
  if (hour >= 9 && hour < 11) return '巳时 (09:00-11:00)'
  if (hour >= 11 && hour < 13) return '午时 (11:00-13:00)'
  if (hour >= 13 && hour < 15) return '未时 (13:00-15:00)'
  if (hour >= 15 && hour < 17) return '申时 (15:00-17:00)'
  if (hour >= 17 && hour < 19) return '酉时 (17:00-19:00)'
  if (hour >= 19 && hour < 21) return '戌时 (19:00-21:00)'
  if (hour >= 21 && hour < 23) return '亥时 (21:00-23:00)'

  return time
}

export function truncateText(text: string, maxLength: number): string {
  if (text.length <= maxLength) return text
  return text.slice(0, maxLength - 3) + '...'
}

export function capitalizeFirst(text: string): string {
  if (!text) return text
  return text.charAt(0).toUpperCase() + text.slice(1)
}

export function getElementEmoji(element: string): string {
  const emojis: Record<string, string> = {
    '木': '🌲',
    '火': '🔥',
    '土': '🏔️',
    '金': '⚔️',
    '水': '💧',
  }
  return emojis[element] || ''
}

export function getGenderEmoji(gender: 'male' | 'female'): string {
  return gender === 'male' ? '👨' : '👩'
}

export function debounce<T extends (...args: any[]) => any>(
  func: T,
  wait: number
): (...args: Parameters<T>) => void {
  let timeout: ReturnType<typeof setTimeout> | null = null

  return (...args: Parameters<T>) => {
    if (timeout) clearTimeout(timeout)
    timeout = setTimeout(() => func(...args), wait)
  }
}

export function throttle<T extends (...args: any[]) => any>(
  func: T,
  limit: number
): (...args: Parameters<T>) => void {
  let inThrottle = false

  return (...args: Parameters<T>) => {
    if (!inThrottle) {
      func(...args)
      inThrottle = true
      setTimeout(() => (inThrottle = false), limit)
    }
  }
}
