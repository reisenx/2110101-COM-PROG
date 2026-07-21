import { useEffect, useState } from 'react'
import { UI_LABELS } from '../config/site'
import type { SiteFrameProps } from '../config/types'
import { SearchDialog } from './SearchDialog'
import { SiteFooter } from './SiteFooter'
import { SiteHeader } from './SiteHeader'

export function SiteFrame({
  activeSection,
  navigation,
  search,
  children,
  className,
  hideFooter = false,
}: SiteFrameProps) {
  const [searchOpen, setSearchOpen] = useState(false)

  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k') {
        event.preventDefault()
        setSearchOpen(true)
      }
    }
    window.addEventListener('keydown', onKeyDown)
    return () => window.removeEventListener('keydown', onKeyDown)
  }, [])

  return (
    <div className={['site', className].filter(Boolean).join(' ')}>
      <a className="skip-link" href="#main-content">{UI_LABELS.skipToContent}</a>
      <SiteHeader
        activeSection={activeSection}
        navigation={navigation}
        onSearch={() => setSearchOpen(true)}
      />
      {children}
      {hideFooter ? null : <SiteFooter />}
      <SearchDialog open={searchOpen} onClose={() => setSearchOpen(false)} search={search} />
    </div>
  )
}
