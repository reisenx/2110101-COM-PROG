import {
  readdir,
  readFile,
  stat,
  writeFile,
} from "node:fs/promises";
import path from "node:path";

import { loadContentManifest } from "../src/content/server";

const websiteRoot = process.cwd();
const clientDir = path.resolve(websiteRoot, "build", "client");
const artifactLimitBytes = 900 * 1024 * 1024;

try {
  const manifest = await loadContentManifest();
  const notFoundTemplate = await readFile(
    path.join(clientDir, "404", "index.html"),
    "utf8",
  );
  await writeFile(
    path.join(clientDir, "404.html"),
    injectLegacyReadmeRedirect(notFoundTemplate, manifest.basePath),
    "utf8",
  );
  await writeFile(path.join(clientDir, ".nojekyll"), "", "utf8");

  const expectedRoutes = [
    "/",
    "/search/",
    "/404/",
    ...manifest.pages.map((page) => page.route),
  ];
  const missingRoutes: string[] = [];
  for (const route of new Set(expectedRoutes)) {
    const output = routeToOutputFile(route, clientDir);
    if (!(await exists(output))) missingRoutes.push(route);
  }
  if (missingRoutes.length > 0) {
    throw new Error(
      `Static build is missing ${missingRoutes.length} prerendered routes:\n${missingRoutes.join("\n")}`,
    );
  }

  const htmlFiles = (await walkFiles(clientDir)).filter((file) => file.endsWith(".html"));
  const brokenReferences = await validateInternalReferences(
    htmlFiles,
    clientDir,
    manifest.basePath,
  );
  if (brokenReferences.length > 0) {
    const preview = brokenReferences.slice(0, 50).join("\n");
    const omitted = Math.max(0, brokenReferences.length - 50);
    throw new Error(
      `Static build contains ${brokenReferences.length} broken internal references:\n${preview}` +
        (omitted ? `\n… and ${omitted} more` : ""),
    );
  }

  const files = await walkFiles(clientDir);
  const sizes = await Promise.all(files.map(async (file) => (await stat(file)).size));
  const artifactBytes = sizes.reduce((total, size) => total + size, 0);
  if (artifactBytes >= artifactLimitBytes) {
    throw new Error(
      `Pages artifact is ${formatMegabytes(artifactBytes)} MB; it must stay below 900 MB.`,
    );
  }

  console.log(
    `Validated ${new Set(expectedRoutes).size} static routes and ${htmlFiles.length} HTML files.`,
  );
  console.log(`Pages artifact: ${formatMegabytes(artifactBytes)} MB.`);
} catch (error) {
  console.error(error instanceof Error ? error.stack ?? error.message : error);
  process.exitCode = 1;
}

async function validateInternalReferences(
  htmlFiles: string[],
  root: string,
  basePath: string,
): Promise<string[]> {
  const broken: string[] = [];
  const normalizedBase = normalizeBasePath(basePath);

  for (const htmlFile of htmlFiles) {
    const html = await readFile(htmlFile, "utf8");
    const documentPath = outputFileToRoute(htmlFile, root);
    const attributePattern = /\b(?:href|src)\s*=\s*["']([^"']+)["']/giu;

    for (const match of html.matchAll(attributePattern)) {
      const authored = decodeHtmlAttribute(match[1]);
      if (isExternalOrFragment(authored)) continue;

      const pathname = authored.replace(/[?#].*$/u, "");
      if (!pathname) continue;
      let sitePath: string;

      if (pathname.startsWith("/")) {
        if (
          normalizedBase &&
          pathname !== normalizedBase &&
          !pathname.startsWith(`${normalizedBase}/`)
        ) {
          broken.push(`${relativeName(htmlFile, root)} -> ${authored} (outside site base)`);
          continue;
        }
        sitePath = normalizedBase ? pathname.slice(normalizedBase.length) || "/" : pathname;
      } else {
        sitePath = path.posix.resolve(path.posix.dirname(documentPath), pathname);
      }

      let decoded: string;
      try {
        decoded = decodeURIComponent(sitePath);
      } catch {
        broken.push(`${relativeName(htmlFile, root)} -> ${authored} (malformed URL)`);
        continue;
      }

      const candidates = referenceCandidates(decoded, root);
      if (!(await anyExists(candidates))) {
        broken.push(`${relativeName(htmlFile, root)} -> ${authored}`);
      }
    }
  }

  return [...new Set(broken)].sort();
}

function referenceCandidates(sitePath: string, root: string): string[] {
  const normalized = path.posix.normalize(`/${sitePath}`).replace(/^\/+/, "");
  const direct = path.resolve(root, normalized);
  if (!direct.startsWith(`${root}${path.sep}`) && direct !== root) return [];

  if (!normalized || sitePath.endsWith("/")) return [path.join(direct, "index.html")];
  if (path.posix.extname(normalized)) return [direct];
  return [direct, `${direct}.html`, path.join(direct, "index.html")];
}

function routeToOutputFile(route: string, root: string): string {
  const normalized = route.replace(/^\/+|\/+$/gu, "");
  return normalized ? path.join(root, normalized, "index.html") : path.join(root, "index.html");
}

function outputFileToRoute(file: string, root: string): string {
  const relative = path.relative(root, file).replaceAll(path.sep, "/");
  if (relative === "index.html") return "/";
  if (relative.endsWith("/index.html")) {
    return `/${relative.slice(0, -"index.html".length)}`;
  }
  return `/${relative}`;
}

async function walkFiles(directory: string): Promise<string[]> {
  const entries = await readdir(directory, { withFileTypes: true });
  const files = await Promise.all(
    entries.map(async (entry) => {
      const target = path.join(directory, entry.name);
      return entry.isDirectory() ? walkFiles(target) : [target];
    }),
  );
  return files.flat();
}

async function anyExists(files: string[]): Promise<boolean> {
  for (const file of files) {
    if (await exists(file)) return true;
  }
  return false;
}

async function exists(file: string): Promise<boolean> {
  try {
    await stat(file);
    return true;
  } catch {
    return false;
  }
}

function isExternalOrFragment(value: string): boolean {
  return (
    !value ||
    value.startsWith("#") ||
    value.startsWith("//") ||
    /^[a-z][a-z\d+.-]*:/iu.test(value)
  );
}

function normalizeBasePath(value: string): string {
  if (!value || value === "/") return "";
  return `/${value.replace(/^\/+|\/+$/gu, "")}`;
}

function decodeHtmlAttribute(value: string): string {
  return value
    .replaceAll("&amp;", "&")
    .replaceAll("&quot;", '"')
    .replaceAll("&#39;", "'");
}

function relativeName(file: string, root: string): string {
  return path.relative(root, file).replaceAll(path.sep, "/");
}

function formatMegabytes(bytes: number): string {
  return (bytes / (1024 * 1024)).toFixed(1);
}

function injectLegacyReadmeRedirect(html: string, basePath: string): string {
  const base = normalizeBasePath(basePath);
  const script = `<script>(function(){var p=location.pathname,b=${JSON.stringify(base)},x=/\\/README(?:\\.md|\\.html)$/i;if(!x.test(p))return;if(b&&!p.startsWith(b+"/"))return;var r=b?p.slice(b.length):p,t=/^\\/README(?:\\.md|\\.html)$/i.test(r)?b+"/about/":b+r.replace(/README(?:\\.md|\\.html)$/i,"");location.replace(t+location.search+location.hash)})()</script>`;
  return html.includes("</head>")
    ? html.replace("</head>", `${script}</head>`)
    : `${script}${html}`;
}
