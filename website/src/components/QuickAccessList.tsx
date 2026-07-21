import {
  ArrowUpRight,
  BookOpen,
  Braces,
  ClipboardCheck,
  FileText,
  FolderOpen,
  GraduationCap,
  Layers,
  Library,
  Terminal,
} from 'lucide-react'
import type { IconName, QuickAccessItem } from '../config/types'

const ICONS = {
  'book-open': BookOpen,
  braces: Braces,
  'clipboard-check': ClipboardCheck,
  'file-text': FileText,
  'folder-open': FolderOpen,
  'graduation-cap': GraduationCap,
  layers: Layers,
  library: Library,
  terminal: Terminal,
} satisfies Record<IconName, typeof BookOpen>

interface QuickAccessListProps {
  items: QuickAccessItem[]
}

export function QuickAccessList({ items }: QuickAccessListProps) {
  return (
    <div className="quick-access-list">
      {items.map((item) => {
        const Icon = ICONS[item.icon]
        return (
          <a key={`${item.eyebrow}-${item.href}`} className="quick-access-item" data-tone={item.tone ?? 'blue'} href={item.href}>
            <span className="quick-access-item__icon"><Icon aria-hidden="true" /></span>
            <span className="quick-access-item__copy">
              <span className="eyebrow">{item.eyebrow}</span>
              <strong>{item.title}</strong>
              <p>{item.description}</p>
            </span>
            {item.meta ? <span className="quick-access-item__meta">{item.meta}</span> : null}
            <ArrowUpRight className="quick-access-item__arrow" aria-hidden="true" />
          </a>
        )
      })}
    </div>
  )
}
