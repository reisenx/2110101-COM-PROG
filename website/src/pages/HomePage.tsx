import { ArrowRight, BookOpen, Code2 } from 'lucide-react'
import { LearningRail } from '../components/LearningRail'
import { QuickAccessList } from '../components/QuickAccessList'
import { SiteFrame } from '../components/SiteFrame'
import type { HomePageModel, SearchProvider } from '../config/types'

interface HomePageProps {
  model: HomePageModel
  search?: SearchProvider
}

export function HomePage({ model, search }: HomePageProps) {
  return (
    <SiteFrame activeSection="home" search={search}>
      <main id="main-content" data-pagefind-body>
        <section className="home-hero">
          <div className="home-hero__grid" aria-hidden="true" />
          <div className="site-container home-hero__layout">
            <div className="home-hero__copy">
              <h1 data-pagefind-meta="title">{model.title}</h1>
              <p>{model.description}</p>
              <div className="hero-actions">
                <a className="button button--primary" href={model.primaryAction.href}>
                  <BookOpen aria-hidden="true" size={19} />
                  {model.primaryAction.label}
                  <ArrowRight aria-hidden="true" size={18} />
                </a>
                <a className="button button--secondary" href={model.secondaryAction.href}>
                  {model.secondaryAction.label}
                </a>
              </div>
              {model.stats?.length ? (
                <dl className="hero-stats">
                  {model.stats.map((stat) => (
                    <div key={stat.label}>
                      <dt>{stat.label}</dt>
                      <dd>{stat.value}</dd>
                    </div>
                  ))}
                </dl>
              ) : null}
            </div>

            <div className="hero-visual" aria-label="ตัวอย่างโค้ด Python">
              <span className="hero-orbit hero-orbit--one" aria-hidden="true" />
              <span className="hero-orbit hero-orbit--two" aria-hidden="true" />
              <div className="code-window">
                <div className="code-window__bar">
                  <span /><span /><span />
                  <strong>hello.py</strong>
                  <Code2 aria-hidden="true" size={17} />
                </div>
                <pre aria-label="Python code example"><code><span className="token-purple">course</span> = <span className="token-yellow">&quot;2110101&quot;</span>{'\n'}<span className="token-blue">print</span>(<span className="token-yellow">&quot;Hello, Python!&quot;</span>){'\n\n'}<span className="token-comment"># เริ่มต้นการเขียนโปรแกรม</span>{'\n'}<span className="token-purple">ready</span> = <span className="token-blue">True</span></code></pre>
              </div>
              <div className="hero-badge hero-badge--python">PY</div>
              <div className="hero-badge hero-badge--braces">{'{ }'}</div>
            </div>
          </div>
        </section>

        <section className="section section--units">
          <div className="site-container">
            <div className="section-heading">
              <div>
                <h2>เรียนรู้ทีละขั้น</h2>
                <p>เริ่มจากพื้นฐาน แล้วค่อย ๆ พัฒนาทักษะผ่านบทเรียนและโจทย์ฝึกทำ</p>
              </div>
              <span className="section-heading__count">{model.units.length} UNITS</span>
            </div>
            <LearningRail units={model.units} />
          </div>
        </section>

        <section className="section section--quick">
          <div className="site-container">
            <div className="section-heading">
              <div>
                <h2>ไปยังส่วนที่ต้องการ</h2>
              </div>
            </div>
            <QuickAccessList items={model.quickAccess} />
          </div>
        </section>
      </main>
    </SiteFrame>
  )
}
