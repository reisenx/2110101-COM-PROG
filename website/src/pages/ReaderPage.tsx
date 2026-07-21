import { Download, ExternalLink, FileCode2, GitFork } from 'lucide-react'
import { Breadcrumbs } from '../components/Breadcrumbs'
import { MarkdownArticle } from '../components/MarkdownArticle'
import { MobileCourseNavigation } from '../components/MobileCourseNavigation'
import { PageNavigation } from '../components/PageNavigation'
import { SidebarNavigation } from '../components/SidebarNavigation'
import { SiteFrame } from '../components/SiteFrame'
import { TableOfContents } from '../components/TableOfContents'
import { SITE, UI_LABELS } from '../config/site'
import type { ReaderPageModel, SearchProvider } from '../config/types'

interface ReaderPageProps {
  model: ReaderPageModel
  search?: SearchProvider
}

export function ReaderPage({ model, search }: ReaderPageProps) {
  const { document } = model
  const difficulty = document.difficulty?.trim()

  return (
    <SiteFrame
      activeSection={document.kind === 'lesson' || document.kind === 'lecture' || document.kind === 'unit' ? 'lessons' : 'problems'}
      search={search}
    >
      <main id="main-content" className="reader-layout">
        <SidebarNavigation
          nodes={model.sidebar}
          currentRoute={document.route}
          searchHref={`${SITE.basePath}search/`}
        />
        <div className="reader-main">
          <div className="reader-main__inner" data-pagefind-body>
            <MobileCourseNavigation nodes={model.sidebar} currentRoute={document.route} />
            <Breadcrumbs items={model.breadcrumbs} />

            <header className="reader-heading">
              <div className="reader-heading__meta">
                {document.code ? <code data-pagefind-meta="code">{document.code}</code> : null}
                {difficulty ? <span className="reader-difficulty" aria-label={`ระดับความยาก ${difficulty}`}>{difficulty}</span> : null}
              </div>
              <h1 data-pagefind-meta="title">{document.title}</h1>
              <div className="reader-actions">
                {model.solutionHref ? (
                  <a className="button button--primary button--small" href={model.solutionHref}>
                    <Download aria-hidden="true" size={16} /> {UI_LABELS.solution}
                  </a>
                ) : null}
                {model.sourceHref ? (
                  <a className="button button--ghost button--small" href={model.sourceHref} target="_blank" rel="noreferrer">
                    <FileCode2 aria-hidden="true" size={16} /> {UI_LABELS.source}
                    <ExternalLink aria-hidden="true" size={13} />
                  </a>
                ) : null}
                {model.repositoryHref ? (
                  <a className="button button--ghost button--small" href={model.repositoryHref} target="_blank" rel="noreferrer">
                    <GitFork aria-hidden="true" size={16} /> {UI_LABELS.repository}
                  </a>
                ) : null}
              </div>
            </header>

            <div className="reader-content-grid">
              <MarkdownArticle html={document.html} />
              <TableOfContents headings={document.headings} />
            </div>

            <PageNavigation
              previous={model.previous ? { label: model.previous.title, href: model.previous.route } : undefined}
              next={model.next ? { label: model.next.title, href: model.next.route } : undefined}
            />
          </div>
        </div>
      </main>
    </SiteFrame>
  )
}
