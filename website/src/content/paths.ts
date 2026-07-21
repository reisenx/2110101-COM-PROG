import path from "node:path";

const EXTERNAL_PROTOCOL = /^[a-z][a-z\d+.-]*:/iu;

export function normalizeBasePath(value: string): string {
  const trimmed = value.trim();
  if (!trimmed || trimmed === "/") return "";
  return `/${trimmed.replace(/^\/+|\/+$/gu, "")}`;
}

/**
 * Resolve a README-authored URL and return a deploy-safe, project-base-aware URL.
 * External URLs, protocol-relative URLs, fragments and data URLs are unchanged.
 */
export function normalizeContentUrl(
  value: string,
  sourcePath: string,
  basePath: string,
): string {
  const original = value.trim();
  if (
    !original ||
    original.startsWith("#") ||
    original.startsWith("//") ||
    EXTERNAL_PROTOCOL.test(original)
  ) {
    return original;
  }

  const { pathname, suffix } = splitUrlSuffix(original);
  const normalizedBase = normalizeBasePath(basePath);
  let repositoryPath: string;

  if (
    normalizedBase &&
    (pathname === normalizedBase || pathname.startsWith(`${normalizedBase}/`))
  ) {
    repositoryPath = pathname.slice(normalizedBase.length).replace(/^\//u, "");
  } else {
    repositoryPath = resolveRepositoryPath(pathname, sourcePath);
  }

  const hadTrailingSlash = pathname.endsWith("/");
  const route = readmePathToRoute(repositoryPath);
  if (route) return withBasePath(route, normalizedBase) + suffix;

  let outputPath = repositoryPath.replace(/^\/+|\/+$/gu, "");
  if (hadTrailingSlash && outputPath) outputPath += "/";
  return withBasePath(`/${encodeRepositoryPath(outputPath)}`, normalizedBase) + suffix;
}

export function resolveRepositoryPath(
  value: string,
  sourcePath: string,
): string {
  const { pathname } = splitUrlSuffix(value.trim());
  if (!pathname) return "";

  if (pathname.startsWith("/")) {
    return path.posix.normalize(pathname).replace(/^\/+|^\.\//gu, "");
  }

  const sourceDirectory = path.posix.dirname(sourcePath.replaceAll("\\", "/"));
  return path.posix
    .normalize(path.posix.join(sourceDirectory === "." ? "" : sourceDirectory, pathname))
    .replace(/^\.\//u, "");
}

export function readmePathToRoute(repositoryPath: string): string | undefined {
  const normalized = repositoryPath.replace(/^\/+|\/+$/gu, "");
  if (!/(?:^|\/)README\.md$/iu.test(normalized)) return undefined;
  if (/^README\.md$/iu.test(normalized)) return "/about/";

  return `/${path.posix.dirname(normalized).replace(/^\/+|\/+$/gu, "")}/`;
}

export function resourceHref(repositoryPath: string, basePath: string): string {
  const normalized = repositoryPath.replace(/^\/+|\/+$/gu, "");
  return withBasePath(`/${encodeRepositoryPath(normalized)}`, normalizeBasePath(basePath));
}

export function siteRouteHref(route: string, basePath: string): string {
  const normalizedRoute = `/${route.replace(/^\/+|\/+$/gu, "")}/`;
  return withBasePath(normalizedRoute, normalizeBasePath(basePath));
}

function splitUrlSuffix(value: string): { pathname: string; suffix: string } {
  const queryIndex = value.indexOf("?");
  const hashIndex = value.indexOf("#");
  const suffixIndex = [queryIndex, hashIndex]
    .filter((index) => index >= 0)
    .sort((left, right) => left - right)[0];

  if (suffixIndex === undefined) return { pathname: value, suffix: "" };
  return {
    pathname: value.slice(0, suffixIndex),
    suffix: value.slice(suffixIndex),
  };
}

function encodeRepositoryPath(value: string): string {
  return value
    .split("/")
    .map((segment) => {
      if (!segment) return segment;
      try {
        return encodeURIComponent(decodeURIComponent(segment));
      } catch {
        return encodeURIComponent(segment);
      }
    })
    .join("/");
}

function withBasePath(route: string, normalizedBase: string): string {
  const normalizedRoute = route.startsWith("/") ? route : `/${route}`;
  return `${normalizedBase}${normalizedRoute}` || "/";
}
