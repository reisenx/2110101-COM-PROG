import { ArrowLeft, Compass } from 'lucide-react'
import { SiteFrame } from '../components/SiteFrame'
import { SITE } from '../config/site'
import type { SearchProvider } from '../config/types'

interface NotFoundPageProps {
  search?: SearchProvider
}

export function NotFoundPage({ search }: NotFoundPageProps) {
  return (
    <SiteFrame search={search}>
      <main id="main-content" className="not-found-page">
        <div className="not-found-page__grid" aria-hidden="true" />
        <div className="not-found-page__content">
          <span className="not-found-page__icon"><Compass aria-hidden="true" /></span>
          <span className="eyebrow">ERROR 404</span>
          <h1>ไม่พบหน้าที่คุณกำลังค้นหา</h1>
          <p>ลิงก์อาจถูกย้ายหรือเปลี่ยนชื่อ ลองกลับไปหน้าแรกแล้วค้นหาเนื้อหาอีกครั้ง</p>
          <a className="button button--primary" href={SITE.basePath}>
            <ArrowLeft aria-hidden="true" /> กลับหน้าแรก
          </a>
        </div>
      </main>
    </SiteFrame>
  )
}
