import { createHash } from "node:crypto";
import { execFileSync } from "node:child_process";
import {
  copyFile,
  mkdir,
  readFile,
  rm,
  stat,
  writeFile,
} from "node:fs/promises";
import path from "node:path";

import { renderMarkdown } from "./markdown";
import { extractMetadata, humanizeSegment } from "./metadata";
import {
  normalizeBasePath,
  resolveRepositoryPath,
  resourceHref,
} from "./paths";
import type {
  ContentHeading,
  ContentManifest,
  ContentPageDocument,
  ContentPageSummary,
  NavigationNode,
  ResourceCollection,
  ResourceEntry,
  ResourceKind,
} from "./types";

export interface BuildContentOptions {
  repoRoot: string;
  websiteRoot?: string;
  generatedDir?: string;
  basePath?: string;
  copyAssets?: boolean;
  concurrency?: number;
}

export interface BuildContentResult {
  manifest: ContentManifest;
  generatedDir: string;
  copiedAssetCount: number;
  copiedAssetBytes: number;
}

interface SourcePage {
  sourcePath: string;
  markdown: string;
  document: ContentPageDocument;
}

interface MutableNavigationNode extends NavigationNode {
  segment: string;
}

const RESOURCE_DEFINITIONS = [
  {
    rootPath: "SM-Study-Materials",
    title: "สื่อการเรียน",
  },
  {
    rootPath: "EX-Midterm-Final",
    title: "ข้อสอบกลางภาคและปลายภาค",
  },
  {
    rootPath: "IC-In-class-Assignment",
    title: "แบบฝึกหัดในชั้นเรียน",
  },
] as const;

const VISITOR_ASSET_EXTENSIONS = new Set([
  ".avif",
  ".c",
  ".cpp",
  ".csv",
  ".gif",
  ".ico",
  ".ipynb",
  ".jpeg",
  ".jpg",
  ".json",
  ".pdf",
  ".png",
  ".py",
  ".svg",
  ".txt",
  ".webp",
  ".xlsx",
]);

const naturalCollator = new Intl.Collator("en", {
  numeric: true,
  sensitivity: "base",
});

export async function buildContent(
  options: BuildContentOptions,
): Promise<BuildContentResult> {
  const repoRoot = path.resolve(options.repoRoot);
  const websiteRoot = path.resolve(options.websiteRoot ?? path.join(repoRoot, "website"));
  const generatedDir = path.resolve(
    options.generatedDir ?? path.join(websiteRoot, ".generated"),
  );
  assertGeneratedDirectoryIsSafe(generatedDir, websiteRoot);

  const basePath = normalizeBasePath(options.basePath ?? "");
  const trackedFiles = gitTrackedFiles(repoRoot);
  const readmePaths = trackedFiles.filter(isCourseReadme).sort(naturalCompare);
  const warnings: string[] = [];

  await rm(generatedDir, { force: true, recursive: true });
  await mkdir(path.join(generatedDir, "pages"), { recursive: true });
  await mkdir(path.join(generatedDir, "public", "__content", "pages"), {
    recursive: true,
  });

  const sourcePages = await mapWithConcurrency(
    readmePaths,
    options.concurrency ?? 4,
    async (sourcePath): Promise<SourcePage> => {
      const markdown = await readFile(path.join(repoRoot, sourcePath), "utf8");
      const metadata = extractMetadata(sourcePath, markdown);
      const rendered = await renderMarkdown(markdown, {
        basePath,
        kind: metadata.kind,
        sourcePath,
        title: metadata.title,
      });
      const id = stableId(metadata.route);

      return {
        sourcePath,
        markdown,
        document: {
          id,
          sourcePath,
          route: metadata.route,
          title: metadata.title,
          code: metadata.code,
          difficulty: metadata.difficulty,
          kind: metadata.kind,
          group: metadata.group,
          headings: rendered.headings,
          documentPath: `pages/${id}.json`,
          html: rendered.html,
        },
      };
    },
  );

  collectMetadataWarnings(sourcePages, warnings);
  assignPreviousAndNext(sourcePages, warnings);

  const resources = await buildResourceCollections(
    repoRoot,
    trackedFiles,
    basePath,
  );
  const sourceRoutes = new Set(sourcePages.map((page) => page.document.route));
  const resourceDocuments = resources
    .filter((collection) => !sourceRoutes.has(collection.route))
    .map(resourceCollectionToDocument);
  const documents = [
    ...sourcePages.map((page) => page.document),
    ...resourceDocuments,
  ].sort((left, right) => naturalCompare(left.route, right.route));
  const pages = documents.map(toSummary);

  const manifest: ContentManifest = {
    schemaVersion: 1,
    generatedAt: new Date().toISOString(),
    sourceRevision: gitSourceRevision(repoRoot),
    basePath,
    pages,
    navigation: buildNavigation(pages),
    resources,
    warnings: [...new Set(warnings)].sort(naturalCompare),
  };

  await Promise.all(
    documents.map(async (document) => {
      const json = serializeJson(document);
      await Promise.all([
        writeFile(path.join(generatedDir, document.documentPath), json, "utf8"),
        writeFile(
          path.join(
            generatedDir,
            "public",
            "__content",
            document.documentPath,
          ),
          json,
          "utf8",
        ),
      ]);
    }),
  );

  const manifestJson = serializeJson(manifest);
  await Promise.all([
    writeFile(path.join(generatedDir, "content-manifest.json"), manifestJson, "utf8"),
    writeFile(
      path.join(generatedDir, "public", "__content", "content-manifest.json"),
      manifestJson,
      "utf8",
    ),
  ]);

  let copiedAssetCount = 0;
  let copiedAssetBytes = 0;
  if (options.copyAssets !== false) {
    const copied = await copyVisitorAssets(repoRoot, generatedDir, trackedFiles);
    copiedAssetCount = copied.count;
    copiedAssetBytes = copied.bytes;
  }

  return {
    manifest,
    generatedDir,
    copiedAssetCount,
    copiedAssetBytes,
  };
}

export function gitTrackedFiles(repoRoot: string): string[] {
  const output = execFileSync("git", ["ls-files", "-z", "--"], {
    cwd: repoRoot,
    encoding: "utf8",
    maxBuffer: 64 * 1024 * 1024,
    stdio: ["ignore", "pipe", "pipe"],
  });

  return output
    .split("\0")
    .filter(Boolean)
    .map((file) => file.replaceAll("\\", "/"));
}

export function isCourseReadme(file: string): boolean {
  const normalized = file.replaceAll("\\", "/").replace(/^\.\//u, "");
  return (
    /(?:^|\/)README\.md$/u.test(normalized) &&
    !normalized.startsWith("website/") &&
    !normalized.startsWith(".github/") &&
    !normalized.split("/").some((segment) => segment.startsWith("."))
  );
}

export function buildNavigation(pages: ContentPageSummary[]): NavigationNode[] {
  const roots: MutableNavigationNode[] = [];
  const byPath = new Map<string, MutableNavigationNode>();

  for (const page of pages) {
    if (page.route === "/about/") {
      roots.push({
        id: "nav-about",
        segment: "about",
        label: page.title,
        route: page.route,
        kind: page.kind,
        children: [],
      });
      continue;
    }

    const segments = page.route.split("/").filter(Boolean);
    let siblings = roots;
    let accumulated = "";
    for (const segment of segments) {
      accumulated += `/${segment}`;
      let node = byPath.get(accumulated);
      if (!node) {
        node = {
          id: `nav-${stableId(accumulated)}`,
          segment,
          label: humanizeSegment(segment),
          children: [],
        };
        siblings.push(node);
        byPath.set(accumulated, node);
      }
      siblings = node.children as MutableNavigationNode[];
    }

    const node = byPath.get(`/${segments.join("/")}`);
    if (node) {
      node.label = page.title;
      node.route = page.route;
      node.kind = page.kind;
    }
  }

  sortNavigation(roots);
  return roots.map(stripNavigationSegment);
}

export function extractOrderedReadmeTargets(
  markdown: string,
  sourcePath: string,
): string[] {
  const targets: string[] = [];
  const seen = new Set<string>();
  const linkPattern = /(?:\]\(|href\s*=\s*["'])([^)"']*README\.md(?:[?#][^)"']*)?)/giu;

  for (const line of markdown.split(/\r?\n/u)) {
    if (!/^\s*\|/u.test(line) || !/README\.md/iu.test(line)) continue;
    for (const match of line.matchAll(linkPattern)) {
      const resolved = resolveRepositoryPath(match[1], sourcePath);
      const target = resolved.replace(/[?#].*$/u, "");
      if (!seen.has(target)) {
        targets.push(target);
        seen.add(target);
      }
    }
  }
  return targets;
}

function assignPreviousAndNext(sourcePages: SourcePage[], warnings: string[]): void {
  const bySourcePath = new Map(sourcePages.map((page) => [page.sourcePath, page]));
  const assigned = new Set<string>();
  const sequences = new Map<string, SourcePage[]>();

  for (const collection of sourcePages) {
    const orderedTargets = extractOrderedReadmeTargets(
      collection.markdown,
      collection.sourcePath,
    );
    const resolvedPages: SourcePage[] = [];

    for (const target of orderedTargets) {
      const page = bySourcePath.get(target);
      if (!page) {
        warnings.push(
          `${collection.sourcePath}: table links to missing tracked README ${target}`,
        );
        continue;
      }
      resolvedPages.push(page);
    }

    if (resolvedPages.length > 0) sequences.set(collection.sourcePath, resolvedPages);
  }

  const lessonsByOwner = new Map<string, SourcePage[]>();
  for (const page of sourcePages) {
    if (page.document.kind !== "lesson") continue;
    const owner = nearestAncestorReadme(page.sourcePath, bySourcePath);
    if (!owner) continue;
    const lessons = lessonsByOwner.get(owner.sourcePath) ?? [];
    lessons.push(page);
    lessonsByOwner.set(owner.sourcePath, lessons);
  }

  for (const [ownerPath, lessons] of lessonsByOwner) {
    const sequence = sequences.get(ownerPath) ?? [];
    const listed = new Set(sequence.map((page) => page.sourcePath));
    const unlisted = lessons
      .filter((page) => !listed.has(page.sourcePath))
      .sort((left, right) => naturalCompare(left.sourcePath, right.sourcePath));

    for (const page of unlisted) {
      warnings.push(
        `${page.sourcePath}: discovered lesson is not listed in ${ownerPath}; appended using natural order`,
      );
    }
    const completeSequence = [...sequence, ...unlisted];
    if (completeSequence.length > 1) assignSequence(completeSequence);
    for (const page of completeSequence) assigned.add(page.sourcePath);
  }

  const fallbackGroups = new Map<string, SourcePage[]>();
  for (const page of sourcePages) {
    if (assigned.has(page.sourcePath) || page.document.kind === "about") continue;
    const parent = path.posix.dirname(page.sourcePath);
    const siblings = fallbackGroups.get(parent) ?? [];
    siblings.push(page);
    fallbackGroups.set(parent, siblings);
  }

  for (const siblings of fallbackGroups.values()) {
    if (siblings.length < 2) continue;
    siblings.sort((left, right) => naturalCompare(left.sourcePath, right.sourcePath));
    assignSequence(siblings);
  }
}

function nearestAncestorReadme(
  sourcePath: string,
  bySourcePath: Map<string, SourcePage>,
): SourcePage | undefined {
  let directory = path.posix.dirname(path.posix.dirname(sourcePath));
  while (directory && directory !== ".") {
    const candidate = bySourcePath.get(`${directory}/README.md`);
    if (candidate) return candidate;
    directory = path.posix.dirname(directory);
  }
  return bySourcePath.get("README.md");
}

function assignSequence(sequence: SourcePage[]): void {
  for (let index = 0; index < sequence.length; index += 1) {
    const current = sequence[index].document;
    const previous = sequence[index - 1]?.document;
    const next = sequence[index + 1]?.document;
    current.previous = previous
      ? { route: previous.route, title: previous.title }
      : undefined;
    current.next = next ? { route: next.route, title: next.title } : undefined;
  }
}

async function buildResourceCollections(
  repoRoot: string,
  trackedFiles: string[],
  basePath: string,
): Promise<ResourceCollection[]> {
  return Promise.all(
    RESOURCE_DEFINITIONS.map(async ({ rootPath, title }) => {
      const candidates = trackedFiles
        .filter((file) => file.startsWith(`${rootPath}/`) && isVisitorAsset(file))
        .sort(naturalCompare);
      const entries: ResourceEntry[] = await Promise.all(
        candidates.map(async (file) => {
          const fileStat = await stat(path.join(repoRoot, file));
          const relative = file.slice(rootPath.length + 1);
          return {
            path: file,
            href: resourceHref(file, basePath),
            name: path.posix.basename(file),
            group: path.posix.dirname(relative) === "."
              ? "ทั่วไป"
              : humanizeSegment(relative.split("/")[0]),
            kind: resourceKind(file),
            size: fileStat.size,
          };
        }),
      );

      return {
        id: stableId(`resource:${rootPath}`),
        title,
        route: `/${rootPath}/`,
        rootPath,
        entries,
      };
    }),
  );
}

function resourceCollectionToDocument(
  collection: ResourceCollection,
): ContentPageDocument {
  const grouped = new Map<string, ResourceEntry[]>();
  for (const entry of collection.entries) {
    const entries = grouped.get(entry.group) ?? [];
    entries.push(entry);
    grouped.set(entry.group, entries);
  }

  const headings: ContentHeading[] = [];
  const sections: string[] = [];
  let index = 0;
  for (const [group, entries] of grouped) {
    const id = `resources-${index}`;
    index += 1;
    headings.push({ depth: 2, id, text: group });
    const links = entries
      .map(
        (entry) =>
          `<li><a href="${escapeHtml(entry.href)}">${escapeHtml(entry.name)}</a>` +
          `<span class="resource-meta">${escapeHtml(resourceKindLabel(entry.kind))} · ${formatBytes(entry.size)}</span></li>`,
      )
      .join("");
    sections.push(
      `<section class="resource-group"><h2 id="${id}">${escapeHtml(group)}</h2><ul class="resource-list">${links}</ul></section>`,
    );
  }

  const id = stableId(collection.route);
  return {
    id,
    sourcePath: null,
    route: collection.route,
    title: collection.title,
    kind: "resource-index",
    group: collection.rootPath,
    headings,
    documentPath: `pages/${id}.json`,
    html:
      sections.join("") ||
      '<p class="content-empty">ยังไม่มีไฟล์ในหมวดนี้</p>',
  };
}

async function copyVisitorAssets(
  repoRoot: string,
  generatedDir: string,
  trackedFiles: string[],
): Promise<{ count: number; bytes: number }> {
  const assets = trackedFiles.filter(isVisitorAsset);
  const sizes = await mapWithConcurrency(assets, 12, async (file) => {
    const source = path.join(repoRoot, file);
    const destination = path.join(generatedDir, "public", file);
    await mkdir(path.dirname(destination), { recursive: true });
    await copyFile(source, destination);
    return (await stat(source)).size;
  });

  return {
    count: assets.length,
    bytes: sizes.reduce((total, size) => total + size, 0),
  };
}

export function isVisitorAsset(file: string): boolean {
  const normalized = file.replaceAll("\\", "/");
  if (
    normalized.startsWith("website/") ||
    normalized.startsWith(".github/") ||
    normalized.startsWith("PL-Problem-List/database/") ||
    normalized.split("/").some((segment) => segment.startsWith("."))
  ) {
    return false;
  }

  const basename = path.posix.basename(normalized).toLowerCase();
  if (/^(?:table-?generate|generate-table|util)\.(?:py|js|ts)$/u.test(basename)) {
    return false;
  }

  return VISITOR_ASSET_EXTENSIONS.has(path.posix.extname(normalized).toLowerCase());
}

function collectMetadataWarnings(sourcePages: SourcePage[], warnings: string[]): void {
  for (const page of sourcePages) {
    if (page.document.kind !== "lesson" || !page.document.code) continue;
    const directoryCode = path.posix.basename(path.posix.dirname(page.sourcePath));
    if (directoryCode !== page.document.code) {
      warnings.push(
        `${page.sourcePath}: authored problem code ${page.document.code} differs from route directory ${directoryCode}; route was preserved`,
      );
    }
  }
}

function toSummary(document: ContentPageDocument): ContentPageSummary {
  const { html: _html, ...summary } = document;
  return summary;
}

function sortNavigation(nodes: MutableNavigationNode[]): void {
  nodes.sort((left, right) => {
    if (left.segment === "about") return -1;
    if (right.segment === "about") return 1;
    return naturalCompare(left.segment, right.segment);
  });
  for (const node of nodes) sortNavigation(node.children as MutableNavigationNode[]);
}

function stripNavigationSegment(node: MutableNavigationNode): NavigationNode {
  return {
    id: node.id,
    label: node.label,
    route: node.route,
    kind: node.kind,
    children: (node.children as MutableNavigationNode[]).map(stripNavigationSegment),
  };
}

function gitSourceRevision(repoRoot: string): string {
  return execFileSync("git", ["rev-parse", "HEAD"], {
    cwd: repoRoot,
    encoding: "utf8",
    stdio: ["ignore", "pipe", "pipe"],
  }).trim();
}

function resourceKind(file: string): ResourceKind {
  const extension = path.posix.extname(file).toLowerCase();
  if (extension === ".pdf") return "pdf";
  if (extension === ".py" || [".c", ".cpp"].includes(extension)) return "python";
  if (extension === ".xlsx") return "spreadsheet";
  if ([".csv", ".json"].includes(extension)) return "data";
  if (extension === ".txt") return "text";
  if ([".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".avif"].includes(extension)) {
    return "image";
  }
  return "other";
}

function resourceKindLabel(kind: ResourceKind): string {
  const labels: Record<ResourceKind, string> = {
    pdf: "PDF",
    python: "Code",
    spreadsheet: "Spreadsheet",
    data: "Data",
    text: "Text",
    image: "Image",
    other: "File",
  };
  return labels[kind];
}

function formatBytes(bytes: number): string {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
}

function stableId(value: string): string {
  return createHash("sha1").update(value).digest("hex").slice(0, 12);
}

function naturalCompare(left: string, right: string): number {
  return naturalCollator.compare(left, right);
}

function serializeJson(value: unknown): string {
  return `${JSON.stringify(value, null, 2)}\n`;
}

function escapeHtml(value: string): string {
  return value.replace(/[&<>"']/gu, (character) => {
    const entities: Record<string, string> = {
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;",
    };
    return entities[character];
  });
}

async function mapWithConcurrency<T, R>(
  values: T[],
  concurrency: number,
  mapper: (value: T, index: number) => Promise<R>,
): Promise<R[]> {
  const output = new Array<R>(values.length);
  let cursor = 0;
  const workers = Array.from(
    { length: Math.max(1, Math.min(concurrency, values.length || 1)) },
    async () => {
      while (cursor < values.length) {
        const index = cursor;
        cursor += 1;
        output[index] = await mapper(values[index], index);
      }
    },
  );
  await Promise.all(workers);
  return output;
}

function assertGeneratedDirectoryIsSafe(
  generatedDir: string,
  websiteRoot: string,
): void {
  const relative = path.relative(websiteRoot, generatedDir);
  if (!relative || relative.startsWith("..") || path.isAbsolute(relative)) {
    throw new Error(
      `Generated directory must be a child of website root: ${generatedDir}`,
    );
  }
}
