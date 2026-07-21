import { ExternalLink, GitFork, RefreshCw } from 'lucide-react'
import { Breadcrumbs } from '../components/Breadcrumbs'
import { MarkdownArticle } from '../components/MarkdownArticle'
import { SiteFrame } from '../components/SiteFrame'
import type { AboutPageModel, SearchProvider } from '../config/types'

interface AboutPageProps {
  model: AboutPageModel
  search?: SearchProvider
}

export function AboutPage({ model, search }: AboutPageProps) {
  return (
    <SiteFrame activeSection="about" search={search}>
      <main id="main-content" className="standalone-page about-page">
        <div className="site-container standalone-content standalone-content--narrow" data-pagefind-body>
          <Breadcrumbs items={model.breadcrumbs} />
          <header className="about-hero">
            <h1 data-pagefind-meta="title">{model.title}</h1>
            {model.description ? <p>{model.description}</p> : null}
            <a className="button button--primary" href={model.repositoryHref} target="_blank" rel="noreferrer">
              <GitFork aria-hidden="true" size={18} /> เปิดรีโพซิทอรี
              <ExternalLink aria-hidden="true" size={14} />
            </a>
          </header>
          <aside className="sync-notice">
            <RefreshCw aria-hidden="true" />
            <div>
              <strong>เนื้อหาอัปเดตอัตโนมัติจาก README.md</strong>
              <p>เมื่อมีการเปลี่ยนแปลงไฟล์ในสาขาที่เผยแพร่ ระบบจะสร้างเว็บไซต์ใหม่โดยไม่ต้องคัดลอกเนื้อหา</p>
            </div>
          </aside>
          <MarkdownArticle html={model.html} className="about-content" />
        </div>
      </main>
    </SiteFrame>
  )
}
