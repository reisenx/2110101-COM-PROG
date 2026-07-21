export type ContentKind =
  | "about"
  | "unit"
  | "lesson"
  | "lecture"
  | "collection"
  | "document"
  | "resource-index";

export interface ContentHeading {
  depth: number;
  id: string;
  text: string;
}

export interface ContentNeighbor {
  route: string;
  title: string;
}

export interface ContentPageSummary {
  /** Stable identifier used as the generated document filename. */
  id: string;
  /** Repository-relative README path, or null for a generated resource index. */
  sourcePath: string | null;
  /** Site-relative route. The GitHub Pages project base is intentionally omitted. */
  route: string;
  title: string;
  code?: string;
  difficulty?: string;
  kind: ContentKind;
  /** Top-level repository directory used to group the navigation. */
  group: string;
  headings: ContentHeading[];
  previous?: ContentNeighbor;
  next?: ContentNeighbor;
  /** Path relative to `website/.generated`. */
  documentPath: string;
}

export interface ContentPageDocument extends ContentPageSummary {
  html: string;
}

export interface NavigationNode {
  id: string;
  label: string;
  route?: string;
  kind?: ContentKind;
  children: NavigationNode[];
}

export type ResourceKind =
  | "pdf"
  | "python"
  | "spreadsheet"
  | "data"
  | "text"
  | "image"
  | "other";

export interface ResourceEntry {
  path: string;
  href: string;
  name: string;
  group: string;
  kind: ResourceKind;
  size: number;
}

export interface ResourceCollection {
  id: string;
  title: string;
  route: string;
  rootPath: string;
  entries: ResourceEntry[];
}

export interface ContentManifest {
  schemaVersion: 1;
  generatedAt: string;
  sourceRevision: string;
  basePath: string;
  pages: ContentPageSummary[];
  navigation: NavigationNode[];
  resources: ResourceCollection[];
  warnings: string[];
}
