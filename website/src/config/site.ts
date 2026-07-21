import type { SiteNavItem } from './types'

const environmentBasePath = import.meta.env.BASE_URL || '/'
const basePath = `/${environmentBasePath.replace(/^\/+|\/+$/g, '')}/`.replace(/^\/\/$/, '/')

export const SITE = {
  name: '2110101 COMP PROG',
  shortName: 'COMP PROG',
  description: 'แหล่งเรียนรู้รายวิชา Computer Programming สำหรับนิสิตจุฬาลงกรณ์มหาวิทยาลัย',
  repositoryUrl: 'https://github.com/reisenx/2110101-COMP-PROG',
  basePath,
  locale: 'th-TH',
  searchPlaceholder: 'ค้นหาบทเรียน โจทย์ หรือรหัสปัญหา…',
} as const

export const SITE_NAVIGATION: SiteNavItem[] = [
  { label: 'หน้าแรก', href: SITE.basePath, section: 'home' },
  { label: 'บทเรียน', href: `${SITE.basePath}00-Python-Intro/`, section: 'lessons' },
  { label: 'แบบฝึกหัด', href: `${SITE.basePath}PL-Problem-List/`, section: 'problems' },
  { label: 'คลังข้อสอบ', href: `${SITE.basePath}EX-Midterm-Final/`, section: 'exams' },
  { label: 'สื่อการเรียน', href: `${SITE.basePath}SM-Study-Materials/`, section: 'materials' },
  { label: 'เกี่ยวกับรายวิชา', href: `${SITE.basePath}about/`, section: 'about' },
]

export const UI_LABELS = {
  skipToContent: 'ข้ามไปยังเนื้อหา',
  openMenu: 'เปิดเมนู',
  closeMenu: 'ปิดเมนู',
  openSearch: 'ค้นหา',
  searchTitle: 'ค้นหาในเว็บไซต์',
  searchHint: 'ลองค้นหาชื่อบทเรียน รหัสโจทย์ หรือหัวข้อ เช่น loop, list, 00_Intro_01',
  noSearchResults: 'ไม่พบเนื้อหาที่ตรงกับคำค้นนี้',
  onThisPage: 'ในหน้านี้',
  source: 'ดูไฟล์ต้นฉบับ',
  repository: 'เปิดบน GitHub',
  solution: 'ดูเฉลย',
  previous: 'ก่อนหน้า',
  next: 'ถัดไป',
  copyCode: 'คัดลอกโค้ด',
  copied: 'คัดลอกแล้ว',
  lectures: 'บทเรียน',
  exercises: 'แบบฝึกหัด',
  viewAll: 'ดูทั้งหมด',
  difficulty: 'ระดับความยาก',
  emptySection: 'ยังไม่มีเนื้อหาในส่วนนี้',
} as const

export function withBasePath(path: string): string {
  if (/^(?:https?:|mailto:|tel:|#)/.test(path)) return path
  const normalized = path.replace(/^\.\//, '').replace(/^\//, '')
  const baseWithoutSlashes = SITE.basePath.replace(/^\/+|\/+$/g, '')
  if (baseWithoutSlashes && (normalized === baseWithoutSlashes || normalized.startsWith(`${baseWithoutSlashes}/`))) {
    return `/${normalized}`
  }
  return `${SITE.basePath}${normalized}`.replace(/\/{2,}/g, '/')
}
