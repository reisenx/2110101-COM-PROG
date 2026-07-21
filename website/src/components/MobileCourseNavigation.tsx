import { ChevronDown, Library } from 'lucide-react'
import type { NavigationNode } from '../content/types'
import { withBasePath } from '../config/site'

interface MobileCourseNavigationProps {
  nodes: NavigationNode[]
  currentRoute: string
}

function flattenNavigation(nodes: NavigationNode[]): NavigationNode[] {
  return nodes.flatMap((node) => [node, ...flattenNavigation(node.children)])
}

export function MobileCourseNavigation({ nodes, currentRoute }: MobileCourseNavigationProps) {
  const links = flattenNavigation(nodes).filter((node) => node.route)
  const current = links.find((node) => node.route === currentRoute)

  return (
    <details className="mobile-course-nav" data-pagefind-ignore="all">
      <summary>
        <span><Library aria-hidden="true" size={17} /> {current?.label ?? 'เลือกเนื้อหา'}</span>
        <ChevronDown aria-hidden="true" size={18} />
      </summary>
      <nav aria-label="เลือกเนื้อหารายวิชา">
        {links.map((node) => (
          <a key={node.id} href={withBasePath(node.route!)} aria-current={node.route === currentRoute ? 'page' : undefined}>
            {node.label}
          </a>
        ))}
      </nav>
    </details>
  )
}
