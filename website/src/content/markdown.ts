import rehypePrettyCode from "rehype-pretty-code";
import rehypeRaw from "rehype-raw";
import rehypeSanitize, { defaultSchema } from "rehype-sanitize";
import rehypeSlug from "rehype-slug";
import rehypeStringify from "rehype-stringify";
import remarkGfm from "remark-gfm";
import remarkParse from "remark-parse";
import remarkRehype from "remark-rehype";
import { unified } from "unified";

import { normalizeContentUrl } from "./paths";
import type { ContentHeading, ContentKind } from "./types";

interface HastNode {
  type: string;
  tagName?: string;
  value?: string;
  properties?: Record<string, unknown>;
  children?: HastNode[];
}

interface RenderFileData {
  basePath: string;
  headings?: ContentHeading[];
  kind: ContentKind;
  sourcePath: string;
  title: string;
}

export interface RenderMarkdownOptions {
  basePath: string;
  kind: ContentKind;
  sourcePath: string;
  title: string;
}

export interface RenderedMarkdown {
  html: string;
  headings: ContentHeading[];
}

const sanitizeSchema = {
  ...defaultSchema,
  tagNames: [...new Set([...(defaultSchema.tagNames ?? []), "ins", "figure"])],
  attributes: {
    ...defaultSchema.attributes,
    "*": [
      ...(defaultSchema.attributes?.["*"] ?? []),
      "align",
      "className",
      "dataAlert",
    ],
    a: [
      ...(defaultSchema.attributes?.a ?? []),
      "href",
      "rel",
      "target",
    ],
    code: [
      ...(defaultSchema.attributes?.code ?? []),
      "className",
      "dataLanguage",
    ],
    img: [
      ...(defaultSchema.attributes?.img ?? []),
      "align",
      "alt",
      "height",
      "loading",
      "src",
      "title",
      "width",
    ],
    td: [...(defaultSchema.attributes?.td ?? []), "align", "colSpan", "rowSpan"],
    th: [...(defaultSchema.attributes?.th ?? []), "align", "colSpan", "rowSpan"],
  },
};

const processor = unified()
  .use(remarkParse)
  .use(remarkGfm)
  .use(remarkRehype, { allowDangerousHtml: true })
  .use(rehypeRaw)
  .use(stripLegacyChrome)
  .use(normalizeAndHardenElements)
  .use(convertGithubAlerts)
  .use(rehypeSanitize, sanitizeSchema)
  .use(rehypeSlug)
  .use(collectHeadings)
  .use(rehypePrettyCode, {
    keepBackground: false,
    theme: "github-light",
  })
  .use(rehypeStringify);

export async function renderMarkdown(
  markdown: string,
  options: RenderMarkdownOptions,
): Promise<RenderedMarkdown> {
  const file = await processor.process({
    value: markdown,
    data: {
      basePath: options.basePath,
      kind: options.kind,
      sourcePath: options.sourcePath,
      title: options.title,
    } satisfies RenderFileData,
  });
  const data = file.data as unknown as RenderFileData;

  return {
    html: String(file),
    headings: data.headings ?? [],
  };
}

function stripLegacyChrome() {
  return (tree: HastNode, file: { data: unknown }) => {
    const data = file.data as RenderFileData;
    stripChildren(tree, data);
  };
}

function stripChildren(parent: HastNode, data: RenderFileData): void {
  if (!parent.children) return;

  for (const child of parent.children) stripChildren(child, data);

  parent.children = parent.children.filter((child) => {
    if (isLegacyNavigationBlock(child)) return false;

    if (data.kind === "lesson" && containsAuthoredProblemH1(child)) {
      return false;
    }

    if (
      child.tagName === "h1" &&
      normalizedNodeText(child).toLocaleLowerCase() ===
        data.title.toLocaleLowerCase()
    ) {
      return false;
    }

    return true;
  });

  for (let index = 0; index < parent.children.length; index += 1) {
    const child = parent.children[index];
    if (child.tagName !== "h1" || !/^contents(?:\s*\(.*\))?$/iu.test(nodeText(child))) {
      continue;
    }

    let end = index + 1;
    while (end < parent.children.length) {
      const candidate = parent.children[end];
      end += 1;
      if (candidate.tagName === "hr") break;
      if (/^h[12]$/u.test(candidate.tagName ?? "")) {
        end -= 1;
        break;
      }
    }
    parent.children.splice(index, end - index);
    index -= 1;
  }
}

function normalizeAndHardenElements() {
  return (tree: HastNode, file: { data: unknown }) => {
    const data = file.data as RenderFileData;
    visit(tree, (node) => {
      if (!node.properties) node.properties = {};

      for (const property of Object.keys(node.properties)) {
        if (/^on/iu.test(property)) delete node.properties[property];
      }

      const inlineStyle = stringProperty(node, "style");
      if (inlineStyle) {
        const width = inlineStyle.match(/(?:^|;)\s*width\s*:\s*(\d{1,3})%\s*(?:;|$)/iu);
        if (width && (node.tagName === "img" || node.tagName === "table")) {
          node.properties.width = `${Math.min(100, Number(width[1]))}%`;
        }
        delete node.properties.style;
      }

      for (const attribute of ["href", "src"] as const) {
        const current = stringProperty(node, attribute);
        if (!current) continue;
        node.properties[attribute] = normalizeContentUrl(
          current,
          data.sourcePath,
          data.basePath,
        );
      }

      if (node.tagName === "a") {
        const href = stringProperty(node, "href") ?? "";
        if (/^https?:\/\//iu.test(href)) {
          node.properties.target = "_blank";
          node.properties.rel = ["noopener", "noreferrer"];
        }
      }

      if (node.tagName === "img") node.properties.loading = "lazy";
    });
  };
}

function convertGithubAlerts() {
  return (tree: HastNode) => {
    visit(tree, (node) => {
      if (node.tagName !== "blockquote" || !node.children?.length) return;
      const firstParagraph = node.children.find((child) => child.tagName === "p");
      if (!firstParagraph) return;

      const firstText = findFirstText(firstParagraph);
      const marker = firstText?.value?.match(/^\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*/iu);
      if (!firstText || !marker) return;

      const kind = marker[1].toLowerCase();
      firstText.value = firstText.value?.slice(marker[0].length) ?? "";
      if (!normalizedNodeText(firstParagraph)) {
        node.children = node.children.filter((child) => child !== firstParagraph);
      }
      node.properties = {
        ...(node.properties ?? {}),
        className: ["markdown-alert", `markdown-alert-${kind}`],
        dataAlert: kind,
      };
      node.children.unshift({
        type: "element",
        tagName: "p",
        properties: { className: ["markdown-alert-title"] },
        children: [{ type: "text", value: marker[1].toUpperCase() }],
      });
    });
  };
}

function collectHeadings() {
  return (tree: HastNode, file: { data: unknown }) => {
    const data = file.data as RenderFileData;
    const headings: ContentHeading[] = [];

    visit(tree, (node) => {
      const match = node.tagName?.match(/^h([1-6])$/u);
      const id = stringProperty(node, "id");
      const text = normalizedNodeText(node);
      if (!match || !id || !text) return;
      headings.push({ depth: Number(match[1]), id, text });
    });

    data.headings = headings;
  };
}

function isLegacyNavigationBlock(node: HastNode): boolean {
  if (node.tagName !== "p") return false;
  let legacy = false;
  visit(node, (descendant) => {
    if (descendant.tagName !== "img") return;
    const src = stringProperty(descendant, "src") ?? "";
    if (/Z99-OTHERS\/00-common\/(?:00-back|01-lecture)\.png(?:$|[?#])/iu.test(src)) {
      legacy = true;
    }
  });
  return legacy;
}

function containsAuthoredProblemH1(node: HastNode): boolean {
  if (node.tagName !== "div") return false;
  return Boolean(node.children?.some((child) => child.tagName === "h1"));
}

function visit(node: HastNode, visitor: (node: HastNode) => void): void {
  visitor(node);
  for (const child of node.children ?? []) visit(child, visitor);
}

function findFirstText(node: HastNode): HastNode | undefined {
  if (node.type === "text") return node;
  for (const child of node.children ?? []) {
    const result = findFirstText(child);
    if (result) return result;
  }
  return undefined;
}

function nodeText(node: HastNode): string {
  if (node.type === "text") return node.value ?? "";
  return (node.children ?? []).map(nodeText).join("");
}

function normalizedNodeText(node: HastNode): string {
  return nodeText(node).replace(/\s+/gu, " ").trim();
}

function stringProperty(node: HastNode, name: string): string | undefined {
  const value = node.properties?.[name];
  return typeof value === "string" ? value : undefined;
}
