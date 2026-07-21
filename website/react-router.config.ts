import fs from "node:fs";
import path from "node:path";

import type { Config } from "@react-router/dev/config";

type GeneratedManifest = {
  pages: Array<{ route: string }>;
  resourceCollections?: Array<{ route: string }>;
};

const basePath = normalizeBasePath(process.env.SITE_BASE_PATH ?? "");
const manifestPath = path.resolve(".generated/content-manifest.json");

function normalizeBasePath(value: string): string {
  if (!value || value === "/") return "";
  return `/${value.replace(/^\/+|\/+$/g, "")}`;
}

function readPrerenderPaths(): string[] {
  if (!fs.existsSync(manifestPath)) {
    throw new Error(
      "Missing generated content manifest. Run `npm run content` before React Router.",
    );
  }

  const manifest = JSON.parse(
    fs.readFileSync(manifestPath, "utf8"),
  ) as GeneratedManifest;
  const paths = new Set<string>(["/", "/search/", "/404/"]);

  for (const page of manifest.pages) paths.add(page.route);
  for (const collection of manifest.resourceCollections ?? []) {
    paths.add(collection.route);
  }

  return [...paths].sort((left, right) => left.localeCompare(right));
}

export default {
  appDirectory: "src",
  // React Router requires the project basename to begin with Vite's trailing-
  // slash base while its preview server performs the prerender requests.
  basename: basePath ? `${basePath}/` : "/",
  buildDirectory: "build",
  routeDiscovery: { mode: "initial" },
  ssr: false,
  prerender: {
    paths: readPrerenderPaths(),
    // Each loader reads the generated manifest; a modest concurrency keeps
    // GitHub-hosted runners reliable while still prerendering quickly.
    concurrency: 4,
  },
} satisfies Config;
