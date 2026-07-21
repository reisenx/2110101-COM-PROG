import path from "node:path";

import type { ContentKind } from "./types";

export interface ExtractedMetadata {
  route: string;
  title: string;
  code?: string;
  difficulty?: string;
  kind: ContentKind;
  group: string;
}

const GENERIC_HEADINGS = [
  /^contents(?:\s*\(.*\))?$/i,
  /^solution(?:\s+\d+)?$/i,
  /^แบบฝึกหัด$/i,
  /^เฉลย$/i,
];

export function routeFromReadme(sourcePath: string): string {
  const normalized = toPosixPath(sourcePath);
  if (normalized === "README.md") return "/about/";

  const directory = path.posix.dirname(normalized);
  return `/${directory.replace(/^\/+|\/+$/g, "")}/`;
}

export function extractMetadata(
  sourcePath: string,
  markdown: string,
): ExtractedMetadata {
  const normalized = toPosixPath(sourcePath);
  const directory = path.posix.dirname(normalized);
  const segments = directory === "." ? [] : directory.split("/");
  const leaf = segments.at(-1) ?? "";
  const group = segments[0] ?? "about";
  const kind = inferContentKind(normalized, markdown);
  const rawHeading = firstHtmlH1(markdown);
  const markdownHeading = firstMeaningfulMarkdownH1(markdown);

  let code = rawHeading?.code;
  let difficulty = rawHeading?.difficulty;
  let title = rawHeading?.title;

  if (kind === "about") {
    title = markdownHeading ?? "2110101 Computer Programming";
  } else if (kind === "lecture") {
    const parent = segments.at(-2) ?? group;
    title = `${humanizeSegment(parent)} · Lecture`;
  } else if (kind === "unit" || kind === "collection") {
    title = humanizeSegment(leaf || group);
  } else {
    title ||= markdownHeading ?? humanizeSegment(leaf);
  }

  if (kind === "lesson" && !code && looksLikeProblemCode(leaf)) {
    code = leaf;
  }

  if (!difficulty) {
    difficulty = findDifficultyNearTitle(markdown, code);
  }

  return {
    route: routeFromReadme(normalized),
    title: normalizeWhitespace(title || humanizeSegment(leaf || group)),
    code,
    difficulty,
    kind,
    group,
  };
}

export function inferContentKind(
  sourcePath: string,
  markdown: string,
): ContentKind {
  const normalized = toPosixPath(sourcePath);
  if (normalized === "README.md") return "about";

  const directory = path.posix.dirname(normalized);
  const segments = directory.split("/");
  const leaf = segments.at(-1) ?? "";

  if (leaf.toLowerCase() === "lecture") return "lecture";
  if (segments.length === 1 && /^\d{2}-/.test(leaf)) return "unit";
  if (segments.length === 1) return "collection";
  if (firstHtmlH1(markdown)?.code || looksLikeProblemCode(leaf)) return "lesson";
  return "document";
}

export function humanizeSegment(segment: string): string {
  return decodeURIComponent(segment)
    .replace(/[_-]+/g, " ")
    .replace(/\b([a-z])/g, (letter) => letter.toUpperCase())
    .replace(/\s+/g, " ")
    .trim();
}

function firstHtmlH1(
  markdown: string,
): { title: string; code?: string; difficulty?: string } | undefined {
  const match = markdown.match(/<h1\b[^>]*>([\s\S]*?)<\/h1\s*>/i);
  if (!match) return undefined;

  const source = match[1];
  const codeMatch = source.match(/<code\b[^>]*>([\s\S]*?)<\/code\s*>/i);
  const code = codeMatch ? cleanInlineHtml(codeMatch[1]) : undefined;
  const fullText = cleanInlineHtml(source);
  const difficulty = fullText.match(/[★☆]{1,5}/u)?.[0];
  let title = fullText;

  if (code) {
    title = title.replace(
      new RegExp(`\\(\\s*${escapeRegExp(code)}\\s*\\)`, "iu"),
      "",
    );
    title = title.replace(code, "");
  }
  if (difficulty) title = title.replace(difficulty, "");
  title = title.replace(/[()]+\s*$/u, "").trim();

  return { title, code, difficulty };
}

function firstMeaningfulMarkdownH1(markdown: string): string | undefined {
  const withoutCode = stripFencedCode(markdown);
  for (const line of withoutCode.split(/\r?\n/u)) {
    const match = line.match(/^\s*#\s+(.+?)\s*#*\s*$/u);
    if (!match) continue;

    const candidate = cleanMarkdownInline(match[1]);
    if (!candidate || GENERIC_HEADINGS.some((pattern) => pattern.test(candidate))) {
      continue;
    }
    return candidate;
  }
  return undefined;
}

function findDifficultyNearTitle(
  markdown: string,
  code?: string,
): string | undefined {
  if (!code) return undefined;
  const codeIndex = markdown.indexOf(code);
  if (codeIndex < 0) return undefined;
  const nearby = markdown.slice(Math.max(0, codeIndex - 120), codeIndex + 240);
  return nearby.match(/[★☆]{1,5}/u)?.[0];
}

function stripFencedCode(markdown: string): string {
  const output: string[] = [];
  let fence: string | undefined;

  for (const line of markdown.split(/\r?\n/u)) {
    const opening = line.match(/^\s*(`{3,}|~{3,})/u)?.[1];
    if (!fence && opening) {
      fence = opening[0];
      continue;
    }
    if (fence && new RegExp(`^\\s*${escapeRegExp(fence)}{3,}`).test(line)) {
      fence = undefined;
      continue;
    }
    if (!fence) output.push(line);
  }

  return output.join("\n");
}

function cleanMarkdownInline(value: string): string {
  return normalizeWhitespace(
    decodeHtmlEntities(
      value
        .replace(/!\[([^\]]*)\]\([^)]*\)/gu, "$1")
        .replace(/\[([^\]]+)\]\([^)]*\)/gu, "$1")
        .replace(/[*_~`]/gu, "")
        .replace(/<[^>]+>/gu, ""),
    ),
  );
}

function cleanInlineHtml(value: string): string {
  return normalizeWhitespace(decodeHtmlEntities(value.replace(/<[^>]+>/gu, " ")));
}

function normalizeWhitespace(value: string): string {
  return value.replace(/\s+/gu, " ").trim();
}

function looksLikeProblemCode(segment: string): boolean {
  return /^(?:\d{2,4}|P\d|G\d)_[A-Za-z0-9_-]+$/u.test(segment);
}

function decodeHtmlEntities(value: string): string {
  const named: Record<string, string> = {
    amp: "&",
    apos: "'",
    gt: ">",
    lt: "<",
    nbsp: " ",
    quot: '"',
  };

  return value.replace(
    /&(#x?[\da-f]+|[a-z]+);/giu,
    (entity, name: string) => {
      if (name[0] === "#") {
        const hex = name[1]?.toLowerCase() === "x";
        const parsed = Number.parseInt(name.slice(hex ? 2 : 1), hex ? 16 : 10);
        return Number.isFinite(parsed) ? String.fromCodePoint(parsed) : entity;
      }
      return named[name.toLowerCase()] ?? entity;
    },
  );
}

function escapeRegExp(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/gu, "\\$&");
}

function toPosixPath(value: string): string {
  return value.replaceAll(path.sep, "/").replace(/^\.\//u, "");
}
