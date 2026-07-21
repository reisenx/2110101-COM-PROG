import { ExternalLink, GitFork } from 'lucide-react'
import { SITE, SITE_NAVIGATION } from '../config/site'

export function SiteFooter() {
  return (
    <footer className="site-footer" data-pagefind-ignore="all">
      <div className="site-container site-footer__grid">
        <div>
          <a className="site-brand site-brand--footer" href={SITE.basePath}>
            <span className="site-brand__mark" aria-hidden="true">&lt;/&gt;</span>
            <span className="site-brand__name">
              <strong>2110101</strong>
              <span>COMP PROG</span>
            </span>
          </a>
          <p>{SITE.description}</p>
        </div>
        <nav className="site-footer__links" aria-label="ลิงก์ท้ายเว็บไซต์">
          {SITE_NAVIGATION.slice(0, 5).map((item) => (
            <a key={item.section} href={item.href}>{item.label}</a>
          ))}
        </nav>
        <div className="site-footer__external">
          <a href={SITE.repositoryUrl} target="_blank" rel="noreferrer">
            <GitFork aria-hidden="true" size={18} /> GitHub
            <ExternalLink aria-hidden="true" size={13} />
          </a>
          <p>เนื้อหาทั้งหมดซิงก์จากไฟล์ README.md ในรีโพซิทอรี</p>
        </div>
      </div>
      <div className="site-container site-footer__legal">
        <span>จัดทำเพื่อการเรียนรู้รายวิชา 2110101 Computer Programming</span>
        <span>Built from open course materials</span>
      </div>
    </footer>
  )
}
