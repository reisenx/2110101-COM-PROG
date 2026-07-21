import { ChevronRight, Home } from 'lucide-react'
import { SITE } from '../config/site'
import type { BreadcrumbItem } from '../config/types'

interface BreadcrumbsProps {
  items: BreadcrumbItem[]
}

export function Breadcrumbs({ items }: BreadcrumbsProps) {
  const visibleItems = items[0]?.label === 'หน้าแรก' ? items.slice(1) : items
  return (
    <nav className="breadcrumbs" aria-label="เส้นทางนำทาง">
      <ol>
        <li>
          <a href={SITE.basePath} aria-label="หน้าแรก">
            <Home aria-hidden="true" size={15} />
          </a>
        </li>
        {visibleItems.map((item, index) => {
          const current = index === visibleItems.length - 1
          return (
            <li key={`${item.label}-${index}`}>
              <ChevronRight aria-hidden="true" size={14} />
              {item.href && !current ? (
                <a href={item.href}>{item.label}</a>
              ) : (
                <span aria-current={current ? 'page' : undefined}>{item.label}</span>
              )}
            </li>
          )
        })}
      </ol>
    </nav>
  )
}
