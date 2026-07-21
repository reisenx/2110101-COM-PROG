import { ArrowRight, FileSearch, LoaderCircle, Search } from 'lucide-react'
import { useEffect, useState } from 'react'
import { SiteFrame } from '../components/SiteFrame'
import { SITE, UI_LABELS } from '../config/site'
import type { SearchPageModel, SearchProvider, SearchResult } from '../config/types'

interface SearchPageProps {
  model: SearchPageModel
  search?: SearchProvider
}

export function SearchPage({ model, search }: SearchPageProps) {
  const [query, setQuery] = useState(model.initialQuery ?? '')
  const [results, setResults] = useState<SearchResult[]>(model.featured ?? [])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    if (!search || query.trim().length < 2) {
      setResults(model.featured ?? [])
      setLoading(false)
      return
    }
    let cancelled = false
    const timer = window.setTimeout(async () => {
      setLoading(true)
      try {
        const nextResults = await search(query.trim())
        if (!cancelled) setResults(nextResults)
      } catch {
        if (!cancelled) setResults([])
      } finally {
        if (!cancelled) setLoading(false)
      }
    }, 160)

    return () => {
      cancelled = true
      window.clearTimeout(timer)
    }
  }, [model.featured, query, search])

  return (
    <SiteFrame search={search}>
      <main id="main-content" className="standalone-page search-page" data-pagefind-ignore="all">
        <div className="standalone-hero standalone-hero--blue">
          <div className="site-container standalone-hero__inner">
            <h1>ค้นหาเนื้อหารายวิชา</h1>
            <p>ค้นหาบทเรียน โจทย์ฝึกทำ รหัสปัญหา หรือไฟล์ประกอบได้จากจุดเดียว</p>
            <label className="search-field search-field--page">
              <Search aria-hidden="true" size={23} />
              <span className="visually-hidden">{UI_LABELS.openSearch}</span>
              <input
                type="search"
                value={query}
                placeholder={SITE.searchPlaceholder}
                onChange={(event) => setQuery(event.target.value)}
                autoFocus
              />
              {loading ? <LoaderCircle className="spin" aria-label="กำลังค้นหา" /> : null}
            </label>
          </div>
        </div>
        <div className="site-container search-page__results" aria-live="polite">
          <div className="section-heading section-heading--compact">
            <div>
              <h2>{query.trim().length >= 2 ? `ผลการค้นหา “${query.trim()}”` : 'เนื้อหาแนะนำ'}</h2>
            </div>
            <span className="section-heading__count">{results.length} รายการ</span>
          </div>
          {results.length ? (
            <ul className="search-results search-results--page">
              {results.map((result) => (
                <li key={result.id}>
                  <a href={result.href}>
                    <div>
                      <span className="search-result__meta">
                        {result.group ?? result.kind ?? 'เนื้อหา'}
                        {result.code ? ` · ${result.code}` : ''}
                      </span>
                      <strong>{result.title}</strong>
                      <p>{result.excerpt}</p>
                    </div>
                    <ArrowRight aria-hidden="true" />
                  </a>
                </li>
              ))}
            </ul>
          ) : !loading ? (
            <div className="empty-state">
              <FileSearch aria-hidden="true" />
              <h2>{UI_LABELS.noSearchResults}</h2>
              <p>ลองใช้คำที่สั้นลง หรือค้นหาด้วยรหัสโจทย์</p>
            </div>
          ) : null}
        </div>
      </main>
    </SiteFrame>
  )
}
