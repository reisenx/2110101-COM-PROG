import { fileURLToPath } from "node:url";
import path from "node:path";

import { buildContent } from "../src/content/pipeline";

const websiteRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const repoRoot = path.resolve(websiteRoot, "..");
const basePath =
  process.env.SITE_BASE_PATH ?? process.env.PAGES_BASE_PATH ?? "";

try {
  const result = await buildContent({
    repoRoot,
    websiteRoot,
    basePath,
    copyAssets: process.env.CONTENT_SKIP_ASSETS !== "1",
  });

  const readmePages = result.manifest.pages.filter(
    (page) => page.sourcePath !== null,
  ).length;
  const generatedPages = result.manifest.pages.length - readmePages;
  console.log(
    `Generated ${readmePages} README pages and ${generatedPages} resource indexes.`,
  );
  console.log(
    `Copied ${result.copiedAssetCount} visitor assets (${formatMegabytes(result.copiedAssetBytes)} MB).`,
  );
  console.log(`Content output: ${result.generatedDir}`);

  if (result.manifest.warnings.length > 0) {
    console.warn(`Content warnings (${result.manifest.warnings.length}):`);
    for (const warning of result.manifest.warnings) console.warn(`- ${warning}`);
  }
} catch (error) {
  console.error(error instanceof Error ? error.stack ?? error.message : error);
  process.exitCode = 1;
}

function formatMegabytes(bytes: number): string {
  return (bytes / (1024 * 1024)).toFixed(1);
}
