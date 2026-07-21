import { ChevronDown, ChevronRight, Search } from 'lucide-react'
import { useMemo, useState } from 'react'
import { UI_LABELS, withBasePath } from '../config/site'
import type { NavigationNode } from '../content/types'

interface SidebarNavigationProps {
  nodes: NavigationNode[]
  currentRoute: string
  title?: string
  onSearch?: () => void
  searchHref?: string
}

function containsRoute(node: NavigationNode, route: string): boolean {
  if (node.route === route) return true
  return node.children.some((child) => containsRoute(child, route))
}

interface NavigationBranchProps {
  node: NavigationNode
  currentRoute: string
  depth: number
}

function NavigationBranch({ node, currentRoute, depth }: NavigationBranchProps) {
  const hasChildren = node.children.length > 0
  const branchActive = containsRoute(node, currentRoute)
  const [expanded, setExpanded] = useState(branchActive || depth === 0)
  const isCurrent = node.route === currentRoute

  return (
    <li className="sidebar-nav__item" data-depth={depth}>
      <div className="sidebar-nav__row">
        {hasChildren ? (
          <button
            type="button"
            aria-expanded={expanded}
            aria-label={`${expanded ? 'ยุบ' : 'ขยาย'} ${node.label}`}
            onClick={() => setExpanded((value) => !value)}
          >
            {expanded ? <ChevronDown aria-hidden="true" /> : <ChevronRight aria-hidden="true" />}
          </button>
        ) : (
          <span className="sidebar-nav__spacer" aria-hidden="true" />
        )}
        {node.route ? (
          <a href={withBasePath(node.route)} aria-current={isCurrent ? 'page' : undefined}>
            {node.label}
          </a>
        ) : (
          <button className="sidebar-nav__branch-label" type="button" onClick={() => setExpanded((value) => !value)}>
            {node.label}
          </button>
        )}
      </div>
      {hasChildren && expanded ? (
        <ul>
          {node.children.map((child) => (
            <NavigationBranch key={child.id} node={child} currentRoute={currentRoute} depth={depth + 1} />
          ))}
        </ul>
      ) : null}
    </li>
  )
}

export function SidebarNavigation({
  nodes,
  currentRoute,
  title = 'เนื้อหารายวิชา',
  onSearch,
  searchHref,
}: SidebarNavigationProps) {
  const visibleNodes = useMemo(() => nodes.filter((node) => node.label.trim()), [nodes])

  return (
    <aside className="reader-sidebar" aria-label="เมนูเนื้อหา" data-pagefind-ignore="all">
      <div className="reader-sidebar__sticky">
        <div className="reader-sidebar__heading">
          <strong>{title}</strong>
        </div>
        {onSearch ? (
          <button className="sidebar-search" type="button" onClick={onSearch}>
            <Search aria-hidden="true" size={17} />
            <span>{UI_LABELS.openSearch}</span>
            <kbd>⌘K</kbd>
          </button>
        ) : searchHref ? (
          <a className="sidebar-search" href={searchHref}>
            <Search aria-hidden="true" size={17} />
            <span>{UI_LABELS.openSearch}</span>
            <kbd>⌘K</kbd>
          </a>
        ) : null}
        <nav className="sidebar-nav">
          <ul>
            {visibleNodes.map((node) => (
              <NavigationBranch key={node.id} node={node} currentRoute={currentRoute} depth={0} />
            ))}
          </ul>
        </nav>
      </div>
    </aside>
  )
}
