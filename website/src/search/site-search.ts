import { SITE, withBasePath } from "../config/site";
import type { SearchProvider, SearchResult } from "../config/types";
import type { ContentPageSummary } from "../content/types";

type PagefindData = {
  url: string;
  excerpt: string;
  meta: Record<string, string>;
};

type PagefindResult = {
  id: string;
  data: () => Promise<PagefindData>;
};

type PagefindModule = {
  options: (options: { baseUrl: string }) => Promise<void>;
  search: (query: string) => Promise<{ results: PagefindResult[] }>;
};

let pagefindPromise: Promise<PagefindModule> | undefined;

function plainText(value: string): string {
  return value
    .replace(/<[^>]+>/g, " ")
    .replace(/&hellip;/g, "…")
    .replace(/&(?:nbsp|#160);/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

async function loadPagefind(): Promise<PagefindModule> {
  if (!pagefindPromise) {
    const bundleUrl = withBasePath("pagefind/pagefind.js");
    pagefindPromise = import(/* @vite-ignore */ bundleUrl).then(
      async (module: PagefindModule) => {
        await module.options({ baseUrl: SITE.basePath });
        return module;
      },
    );
  }
  return pagefindPromise;
}

function fallbackSearch(
  pages: ContentPageSummary[],
  query: string,
): SearchResult[] {
  const normalized = query.trim().toLocaleLowerCase("th");
  if (!normalized) return [];

  return pages
    .flatMap((page) => {
      const headingText = page.headings.map((heading) => heading.text).join(" ");
      const searchable = [page.title, page.code, page.group, headingText]
        .filter(Boolean)
        .join(" ")
        .toLocaleLowerCase("th");

      if (!searchable.includes(normalized)) return [];
      return [
        {
          id: page.id,
          title: page.title,
          excerpt: headingText || `เนื้อหาจาก ${page.group}`,
          href: withBasePath(page.route),
          group: page.group,
          code: page.code,
          kind: page.kind,
        } satisfies SearchResult,
      ];
    })
    .slice(0, 12);
}

export function createSearchProvider(
  pages: ContentPageSummary[],
): SearchProvider {
  return async (query) => {
    try {
      const pagefind = await loadPagefind();
      const response = await pagefind.search(query);
      const data = await Promise.all(
        response.results.slice(0, 12).map(async (result) => ({
          id: result.id,
          data: await result.data(),
        })),
      );

      return data.map(({ id, data }) => ({
        id,
        title: data.meta.title || "ไม่มีชื่อ",
        excerpt: plainText(data.excerpt),
        href: data.url,
        group: data.meta.group,
        code: data.meta.code,
        kind: data.meta.kind,
      }));
    } catch {
      return fallbackSearch(pages, query);
    }
  };
}
