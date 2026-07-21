import { ChevronDown, List } from 'lucide-react'
import type { ContentHeading } from '../content/types'
import { UI_LABELS } from '../config/site'

interface TableOfContentsProps {
  headings: ContentHeading[]
}

function TocLinks({ headings }: TableOfContentsProps) {
  return (
    <ol>
      {headings.map((heading) => (
        <li key={heading.id} data-depth={heading.depth}>
          <a href={`#${heading.id}`}>{heading.text}</a>
        </li>
      ))}
    </ol>
  )
}

export function TableOfContents({ headings }: TableOfContentsProps) {
  if (headings.length === 0) return null

  return (
    <>
      <aside className="page-toc" aria-label={UI_LABELS.onThisPage} data-pagefind-ignore="all">
        <div className="page-toc__title">
          <List aria-hidden="true" size={17} />
          <strong>{UI_LABELS.onThisPage}</strong>
        </div>
        <TocLinks headings={headings} />
      </aside>
      <details className="mobile-toc" data-pagefind-ignore="all">
        <summary>
          <span><List aria-hidden="true" size={17} /> {UI_LABELS.onThisPage}</span>
          <ChevronDown aria-hidden="true" size={18} />
        </summary>
        <TocLinks headings={headings} />
      </details>
    </>
  )
}
