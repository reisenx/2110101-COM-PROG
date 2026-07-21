import { BookOpen, Braces } from 'lucide-react'
import { Breadcrumbs } from '../components/Breadcrumbs'
import { PageNavigation } from '../components/PageNavigation'
import { SidebarNavigation } from '../components/SidebarNavigation'
import { SiteFrame } from '../components/SiteFrame'
import { ExerciseTable, LectureList } from '../components/UnitContents'
import { SITE } from '../config/site'
import type { SearchProvider, UnitPageModel } from '../config/types'

interface UnitPageProps {
  model: UnitPageModel
  search?: SearchProvider
}

export function UnitPage({ model, search }: UnitPageProps) {
  return (
    <SiteFrame activeSection="lessons" search={search}>
      <main id="main-content" className="course-layout">
        {model.sidebar?.length ? (
          <SidebarNavigation
            nodes={model.sidebar}
            currentRoute={model.currentRoute ?? ''}
            searchHref={`${SITE.basePath}search/`}
          />
        ) : null}
        <div className="course-main">
          <div className="course-main__inner" data-pagefind-body>
            <Breadcrumbs items={model.breadcrumbs} />
            <header className="unit-hero">
              <span className="unit-hero__code">{model.code}</span>
              <div>
                <h1 data-pagefind-meta="title">{model.title}</h1>
                {model.description ? <p>{model.description}</p> : null}
              </div>
              <div className="unit-hero__geometry" aria-hidden="true">
                <span /><span /><Braces />
              </div>
            </header>

            <section className="content-section" aria-labelledby="lectures-heading">
              <div className="content-section__heading">
                <span className="content-section__icon"><BookOpen aria-hidden="true" /></span>
                <div>
                  <h2 id="lectures-heading">บทเรียน</h2>
                </div>
                <span className="content-section__count">{model.lectures.length} หัวข้อ</span>
              </div>
              <LectureList items={model.lectures} />
            </section>

            <section className="content-section" aria-labelledby="exercises-heading">
              <div className="content-section__heading">
                <span className="content-section__icon content-section__icon--yellow"><Braces aria-hidden="true" /></span>
                <div>
                  <h2 id="exercises-heading">แบบฝึกหัด</h2>
                </div>
                <span className="content-section__count">{model.exercises.length} ข้อ</span>
              </div>
              <ExerciseTable items={model.exercises} />
            </section>

            <PageNavigation previous={model.previous} next={model.next} />
          </div>
        </div>
      </main>
    </SiteFrame>
  )
}
