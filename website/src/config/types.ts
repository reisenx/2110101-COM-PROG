import type {
  ContentPageDocument,
  NavigationNode,
  ResourceCollection,
} from '../content/types'
import type { ReactNode } from 'react'

export type IconName =
  | 'book-open'
  | 'braces'
  | 'clipboard-check'
  | 'file-text'
  | 'folder-open'
  | 'graduation-cap'
  | 'layers'
  | 'library'
  | 'terminal'

export interface SiteNavItem {
  label: string
  href: string
  section: string
  external?: boolean
}

export interface BreadcrumbItem {
  label: string
  href?: string
}

export interface LearningUnit {
  code: string
  title: string
  description: string
  href: string
  lessonCount?: number
  state?: 'available' | 'current' | 'upcoming'
}

export interface QuickAccessItem {
  eyebrow: string
  title: string
  description: string
  href: string
  meta?: string
  icon: IconName
  tone?: 'blue' | 'yellow' | 'navy'
}

export interface SearchResult {
  id: string
  title: string
  excerpt: string
  href: string
  group?: string
  code?: string
  kind?: string
}

export type SearchProvider = (query: string) => Promise<SearchResult[]>

export interface SiteFrameProps {
  activeSection?: string
  navigation?: SiteNavItem[]
  search?: SearchProvider
  children: ReactNode
  className?: string
  hideFooter?: boolean
}

export interface HomePageModel {
  eyebrow?: string
  title: string
  description: string
  primaryAction: { label: string; href: string }
  secondaryAction: { label: string; href: string }
  units: LearningUnit[]
  quickAccess: QuickAccessItem[]
  stats?: Array<{ value: string; label: string }>
}

export interface LectureItem {
  number: string
  title: string
  href: string
  description?: string
  meta?: string
}

export interface ExerciseItem {
  code: string
  title: string
  href: string
  difficulty?: number
  solutionHref?: string
}

export interface UnitPageModel {
  code: string
  title: string
  description?: string
  breadcrumbs: BreadcrumbItem[]
  lectures: LectureItem[]
  exercises: ExerciseItem[]
  sidebar?: NavigationNode[]
  currentRoute?: string
  previous?: { label: string; href: string }
  next?: { label: string; href: string }
}

export interface ReaderPageModel {
  document: ContentPageDocument
  breadcrumbs: BreadcrumbItem[]
  sidebar: NavigationNode[]
  sourceHref?: string
  repositoryHref?: string
  solutionHref?: string
  previous?: { title: string; route: string }
  next?: { title: string; route: string }
}

export interface SearchPageModel {
  initialQuery?: string
  featured?: SearchResult[]
}

export interface MaterialsPageModel {
  title: string
  description?: string
  breadcrumbs: BreadcrumbItem[]
  collections: ResourceCollection[]
}

export interface AboutPageModel {
  title: string
  description?: string
  html: string
  breadcrumbs: BreadcrumbItem[]
  repositoryHref: string
}
