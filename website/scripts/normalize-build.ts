import { copyFile, mkdir, readdir, rm, stat } from "node:fs/promises";
import path from "node:path";

const clientDir = path.resolve(process.cwd(), "build", "client");
const basePath = normalizeBasePath(process.env.SITE_BASE_PATH ?? "");

try {
  if (basePath) {
    const nestedOutput = path.resolve(clientDir, basePath.slice(1));
    assertChildDirectory(nestedOutput, clientDir);
    if (!(await isDirectory(nestedOutput))) {
      throw new Error(
        `React Router did not emit the expected project-site directory: ${nestedOutput}`,
      );
    }

    // React Router prerenders beneath its basename, while a GitHub Pages
    // artifact is already mounted at that basename. Merge the prerendered
    // files into the artifact root without disturbing copied course assets.
    await mergePrerenderedOutput(nestedOutput, clientDir);
    await rm(nestedOutput, { recursive: true, force: true });
  }

  // The site uses ordinary anchors so every navigation is a full static-page
  // request. React Router data payloads only duplicate the manifest and README
  // HTML hundreds of times, and are not needed by this deployment.
  await removeRouteDataFiles(clientDir);

  // Every known route is prerendered. Keeping a universal SPA fallback would
  // make missing GitHub Pages paths look successful instead of returning 404.
  await rm(path.join(clientDir, "__spa-fallback.html"), { force: true });
  console.log(
    basePath
      ? `Normalized prerendered output for ${basePath}/.`
      : "Prerendered output already uses the artifact root.",
  );
} catch (error) {
  console.error(error instanceof Error ? error.stack ?? error.message : error);
  process.exitCode = 1;
}

function normalizeBasePath(value: string): string {
  if (!value || value === "/") return "";
  return `/${value.replace(/^\/+|\/+$/gu, "")}`;
}

function assertChildDirectory(target: string, parent: string): void {
  const relative = path.relative(parent, target);
  if (!relative || relative.startsWith("..") || path.isAbsolute(relative)) {
    throw new Error(`Unsafe build normalization target: ${target}`);
  }
}

async function isDirectory(target: string): Promise<boolean> {
  try {
    return (await stat(target)).isDirectory();
  } catch {
    return false;
  }
}

async function mergePrerenderedOutput(
  sourceDirectory: string,
  destinationDirectory: string,
): Promise<void> {
  await mkdir(destinationDirectory, { recursive: true });
  const entries = await readdir(sourceDirectory, { withFileTypes: true });
  await Promise.all(
    entries.map(async (entry) => {
      const source = path.join(sourceDirectory, entry.name);
      const destination = path.join(destinationDirectory, entry.name);
      if (entry.isDirectory()) {
        await mergePrerenderedOutput(source, destination);
      } else if (!entry.name.endsWith(".data")) {
        await copyFile(source, destination);
      }
    }),
  );
}

async function removeRouteDataFiles(directory: string): Promise<void> {
  const entries = await readdir(directory, { withFileTypes: true });
  await Promise.all(
    entries.map(async (entry) => {
      const target = path.join(directory, entry.name);
      if (entry.isDirectory()) await removeRouteDataFiles(target);
      else if (entry.name.endsWith(".data")) await rm(target, { force: true });
    }),
  );
}
