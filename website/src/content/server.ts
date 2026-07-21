import { readFile } from "node:fs/promises";
import path from "node:path";

import { normalizeBasePath, readmePathToRoute } from "./paths";
import type {
  ContentManifest,
  ContentPageDocument,
  ContentPageSummary,
} from "./types";

export async function loadContentManifest(
  generatedDir = resolveGeneratedDirectory(),
): Promise<ContentManifest> {
  return readJson<ContentManifest>(path.join(generatedDir, "content-manifest.json"));
}

export async function loadContentPageById(
  id: string,
  generatedDir = resolveGeneratedDirectory(),
): Promise<ContentPageDocument> {
  if (!/^[a-f\d]{12}$/u.test(id)) {
    throw new Error(`Invalid generated content page id: ${id}`);
  }
  return readJson<ContentPageDocument>(path.join(generatedDir, "pages", `${id}.json`));
}

export async function loadContentPageByRoute(
  route: string,
  generatedDir = resolveGeneratedDirectory(),
): Promise<ContentPageDocument | undefined> {
  const manifest = await loadContentManifest(generatedDir);
  const normalizedRoute = normalizeRequestedRoute(route, manifest.basePath);
  const summary = manifest.pages.find((page) => page.route === normalizedRoute);
  if (!summary) return undefined;
  return readJson<ContentPageDocument>(path.join(generatedDir, summary.documentPath));
}

export async function getPrerenderRoutes(
  generatedDir = resolveGeneratedDirectory(),
): Promise<string[]> {
  const manifest = await loadContentManifest(generatedDir);
  return manifest.pages.map((page) => page.route);
}

export async function getContentPageSummary(
  route: string,
  generatedDir = resolveGeneratedDirectory(),
): Promise<ContentPageSummary | undefined> {
  const manifest = await loadContentManifest(generatedDir);
  const normalizedRoute = normalizeRequestedRoute(route, manifest.basePath);
  return manifest.pages.find((page) => page.route === normalizedRoute);
}

export function resolveGeneratedDirectory(): string {
  if (process.env.CONTENT_GENERATED_DIR) {
    return path.resolve(process.env.CONTENT_GENERATED_DIR);
  }

  const cwd = process.cwd();
  return path.basename(cwd) === "website"
    ? path.join(cwd, ".generated")
    : path.join(cwd, "website", ".generated");
}

function normalizeRequestedRoute(route: string, basePath: string): string {
  let pathname = route.split(/[?#]/u, 1)[0] || "/";
  try {
    pathname = decodeURI(pathname);
  } catch {
    // Keep the original text; a malformed escape simply will not match a page.
  }

  const base = normalizeBasePath(basePath);
  if (base && (pathname === base || pathname.startsWith(`${base}/`))) {
    pathname = pathname.slice(base.length) || "/";
  }

  const legacyRoute = readmePathToRoute(pathname);
  if (legacyRoute) return legacyRoute;

  const normalized = `/${pathname.replace(/^\/+|\/+$/gu, "")}`;
  return normalized === "/" ? "/" : `${normalized}/`;
}

async function readJson<T>(file: string): Promise<T> {
  try {
    return JSON.parse(await readFile(file, "utf8")) as T;
  } catch (error) {
    const reason = error instanceof Error ? error.message : String(error);
    throw new Error(`Unable to read generated content ${file}: ${reason}`, {
      cause: error,
    });
  }
}
