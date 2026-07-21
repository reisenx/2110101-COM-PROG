import { ArrowRight, FileSearch, LoaderCircle, Search, X } from 'lucide-react'
import { useEffect, useRef, useState } from 'react'
import { SITE, UI_LABELS } from '../config/site'
import type { SearchProvider, SearchResult } from '../config/types'

interface SearchDialogProps {
  open: boolean
  onClose: () => void
  search?: SearchProvider
}

export function SearchDialog({ open, onClose, search }: SearchDialogProps) {
  const dialogRef = useRef<HTMLDialogElement>(null)
  const inputRef = useRef<HTMLInputElement>(null)
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<SearchResult[]>([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    const dialog = dialogRef.current
    if (!dialog) return

    if (open && !dialog.open) {
      dialog.showModal()
      window.requestAnimationFrame(() => inputRef.current?.focus())
    } else if (!open && dialog.open) {
      dialog.close()
    }
  }, [open])

  useEffect(() => {
    if (!open || query.trim().length < 2 || !search) {
      setResults([])
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
    }, 140)

    return () => {
      cancelled = true
      window.clearTimeout(timer)
    }
  }, [open, query, search])

  useEffect(() => {
    if (!open) {
      setQuery('')
      setResults([])
    }
  }, [open])

  return (
    <dialog
      ref={dialogRef}
      className="search-dialog"
      aria-labelledby="site-search-title"
      onCancel={(event) => {
        event.preventDefault()
        onClose()
      }}
      onClose={onClose}
      onClick={(event) => {
        if (event.target === dialogRef.current) onClose()
      }}
    >
      <div className="search-dialog__panel">
        <div className="search-dialog__heading">
          <div>
            <h2 id="site-search-title">{UI_LABELS.searchTitle}</h2>
          </div>
          <button className="icon-button" type="button" onClick={onClose} aria-label={UI_LABELS.closeMenu}>
            <X aria-hidden="true" size={20} />
          </button>
        </div>

        <label className="search-field search-field--large">
          <Search aria-hidden="true" size={21} />
          <span className="visually-hidden">{UI_LABELS.openSearch}</span>
          <input
            ref={inputRef}
            type="search"
            value={query}
            placeholder={SITE.searchPlaceholder}
            onChange={(event) => setQuery(event.target.value)}
            autoComplete="off"
          />
          {loading ? <LoaderCircle className="spin" aria-label="กำลังค้นหา" size={19} /> : null}
        </label>

        <div className="search-dialog__body" aria-live="polite">
          {query.length < 2 ? (
            <div className="search-dialog__empty">
              <FileSearch aria-hidden="true" size={34} />
              <p>{UI_LABELS.searchHint}</p>
            </div>
          ) : results.length > 0 ? (
            <ul className="search-results">
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
                    <ArrowRight aria-hidden="true" size={18} />
                  </a>
                </li>
              ))}
            </ul>
          ) : !loading ? (
            <div className="search-dialog__empty">
              <FileSearch aria-hidden="true" size={34} />
              <p>{UI_LABELS.noSearchResults}</p>
            </div>
          ) : null}
        </div>

        <div className="search-dialog__footer">
          <span><kbd>↑</kbd><kbd>↓</kbd> เลือก</span>
          <span><kbd>Enter</kbd> เปิด</span>
          <span><kbd>Esc</kbd> ปิด</span>
        </div>
      </div>
    </dialog>
  )
}
