import { ArrowLeft, ArrowRight } from 'lucide-react'
import { UI_LABELS } from '../config/site'

interface NavigationTarget {
  label: string
  href: string
  eyebrow?: string
}

interface PageNavigationProps {
  previous?: NavigationTarget
  next?: NavigationTarget
}

export function PageNavigation({ previous, next }: PageNavigationProps) {
  if (!previous && !next) return null
  return (
    <nav className="page-navigation" aria-label="ไปยังเนื้อหาก่อนหน้าหรือถัดไป">
      {previous ? (
        <a className="page-navigation__item page-navigation__item--previous" href={previous.href}>
          <ArrowLeft aria-hidden="true" />
          <span>
            <small>{previous.eyebrow ?? UI_LABELS.previous}</small>
            <strong>{previous.label}</strong>
          </span>
        </a>
      ) : <span />}
      {next ? (
        <a className="page-navigation__item page-navigation__item--next" href={next.href}>
          <span>
            <small>{next.eyebrow ?? UI_LABELS.next}</small>
            <strong>{next.label}</strong>
          </span>
          <ArrowRight aria-hidden="true" />
        </a>
      ) : null}
    </nav>
  )
}
