import { ArrowUpRight, Database, File, FileCode2, FileSpreadsheet, FileText, Image, Library } from 'lucide-react'
import { Breadcrumbs } from '../components/Breadcrumbs'
import { SiteFrame } from '../components/SiteFrame'
import type { ResourceEntry } from '../content/types'
import type { MaterialsPageModel, SearchProvider } from '../config/types'

interface MaterialsPageProps {
  model: MaterialsPageModel
  search?: SearchProvider
}

const RESOURCE_ICONS = {
  pdf: FileText,
  python: FileCode2,
  spreadsheet: FileSpreadsheet,
  data: Database,
  text: FileText,
  image: Image,
  other: File,
} as const

function formatFileSize(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`
  if (bytes < 1024 * 1024) return `${Math.round(bytes / 1024)} KB`
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`
}

function ResourceCard({ resource }: { resource: ResourceEntry }) {
  const Icon = RESOURCE_ICONS[resource.kind]
  return (
    <a className="resource-card" href={resource.href}>
      <span className="resource-card__icon"><Icon aria-hidden="true" /></span>
      <span className="resource-card__copy">
        <strong>{resource.name}</strong>
        <span>{resource.group} · {formatFileSize(resource.size)}</span>
      </span>
      <ArrowUpRight aria-hidden="true" size={18} />
    </a>
  )
}

export function MaterialsPage({ model, search }: MaterialsPageProps) {
  const totalResources = model.collections.reduce((total, collection) => total + collection.entries.length, 0)
  return (
    <SiteFrame activeSection="materials" search={search}>
      <main id="main-content" className="standalone-page materials-page">
        <div className="site-container standalone-content" data-pagefind-body>
          <Breadcrumbs items={model.breadcrumbs} />
          <header className="standalone-heading">
            <span className="standalone-heading__icon"><Library aria-hidden="true" /></span>
            <div>
              <h1 data-pagefind-meta="title">{model.title}</h1>
              {model.description ? <p>{model.description}</p> : null}
            </div>
            <span className="standalone-heading__count">{totalResources} FILES</span>
          </header>

          <div className="resource-collections">
            {model.collections.map((collection) => (
              <section key={collection.id} className="resource-collection">
                <div className="content-section__heading">
                  <span className="content-section__icon"><Library aria-hidden="true" /></span>
                  <div>
                    <h2>{collection.title}</h2>
                  </div>
                  <span className="content-section__count">{collection.entries.length} ไฟล์</span>
                </div>
                <div className="resource-grid">
                  {collection.entries.map((resource) => <ResourceCard key={resource.path} resource={resource} />)}
                </div>
              </section>
            ))}
          </div>
        </div>
      </main>
    </SiteFrame>
  )
}
