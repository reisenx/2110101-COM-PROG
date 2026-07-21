import { Menu, Search, X } from 'lucide-react'
import { useEffect, useId, useState } from 'react'
import { SITE, SITE_NAVIGATION, UI_LABELS } from '../config/site'
import type { SiteNavItem } from '../config/types'

interface SiteHeaderProps {
  activeSection?: string
  navigation?: SiteNavItem[]
  onSearch: () => void
}

export function SiteHeader({
  activeSection,
  navigation = SITE_NAVIGATION,
  onSearch,
}: SiteHeaderProps) {
  const [menuOpen, setMenuOpen] = useState(false)
  const menuId = useId()

  useEffect(() => {
    if (!menuOpen) return
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setMenuOpen(false)
    }
    window.addEventListener('keydown', onKeyDown)
    return () => window.removeEventListener('keydown', onKeyDown)
  }, [menuOpen])

  return (
    <header className="site-header" data-pagefind-ignore="all">
      <div className="site-header__inner site-container">
        <a className="site-brand" href={SITE.basePath} aria-label={`${SITE.name} หน้าแรก`}>
          <span className="site-brand__mark" aria-hidden="true">
            <span>&lt;/&gt;</span>
          </span>
          <span className="site-brand__name">
            <strong>2110101</strong>
            <span>COMP PROG</span>
          </span>
        </a>

        <nav className="site-nav" aria-label="เมนูหลัก">
          {navigation.map((item) => (
            <a
              key={item.section}
              className="site-nav__link"
              data-active={activeSection === item.section || undefined}
              href={item.href}
              target={item.external ? '_blank' : undefined}
              rel={item.external ? 'noreferrer' : undefined}
            >
              {item.label}
            </a>
          ))}
        </nav>

        <div className="site-header__actions">
          <button
            className="icon-button site-search-button"
            type="button"
            aria-label={UI_LABELS.openSearch}
            onClick={onSearch}
          >
            <Search aria-hidden="true" size={19} strokeWidth={2} />
            <span>{UI_LABELS.openSearch}</span>
            <kbd aria-hidden="true">⌘ K</kbd>
          </button>
          <button
            className="icon-button site-menu-button"
            type="button"
            aria-expanded={menuOpen}
            aria-controls={menuId}
            aria-label={menuOpen ? UI_LABELS.closeMenu : UI_LABELS.openMenu}
            onClick={() => setMenuOpen((isOpen) => !isOpen)}
          >
            {menuOpen ? <X aria-hidden="true" /> : <Menu aria-hidden="true" />}
          </button>
        </div>
      </div>

      <div id={menuId} className="mobile-nav" data-open={menuOpen || undefined}>
        <nav className="mobile-nav__inner site-container" aria-label="เมนูหลักบนมือถือ">
          {navigation.map((item) => (
            <a
              key={item.section}
              className="mobile-nav__link"
              data-active={activeSection === item.section || undefined}
              href={item.href}
              onClick={() => setMenuOpen(false)}
            >
              {item.label}
            </a>
          ))}
          <button
            className="mobile-nav__search"
            type="button"
            onClick={() => {
              setMenuOpen(false)
              onSearch()
            }}
          >
            <Search aria-hidden="true" size={18} />
            {UI_LABELS.openSearch}
          </button>
        </nav>
      </div>
    </header>
  )
}
