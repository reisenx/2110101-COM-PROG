import { spawn } from "node:child_process";
import { createReadStream } from "node:fs";
import { stat } from "node:fs/promises";
import { createServer } from "node:http";
import path from "node:path";

const args = process.argv.slice(2);
const noBuild = args.includes("--no-build");
const host = argumentValue("--host") ?? "127.0.0.1";
const port = Number(argumentValue("--port") ?? "4173");
const basePath = normalizeBasePath(
  argumentValue("--base") ?? process.env.SITE_BASE_PATH ?? "/2110101-COMP-PROG",
);
const clientDir = path.resolve(process.cwd(), "build", "client");

if (!Number.isInteger(port) || port < 1 || port > 65_535) {
  throw new Error(`Invalid preview port: ${port}`);
}

if (!noBuild) {
  const exitCode = await runBuild(basePath);
  if (exitCode !== 0) process.exit(exitCode ?? 1);
}

if (!(await isFile(path.join(clientDir, "index.html")))) {
  throw new Error(
    "Missing build/client/index.html. Run without --no-build or run npm run build first.",
  );
}

const server = createServer(async (request, response) => {
  try {
    const requestUrl = new URL(request.url ?? "/", `http://${request.headers.host ?? host}`);
    const pathname = requestUrl.pathname;

    if (basePath && pathname === basePath) {
      response.writeHead(308, { location: `${basePath}/${requestUrl.search}` });
      response.end();
      return;
    }
    if (basePath && !pathname.startsWith(`${basePath}/`)) {
      await sendNotFound(response, request.method);
      return;
    }

    const sitePath = basePath ? pathname.slice(basePath.length) || "/" : pathname;
    const file = await resolveStaticFile(sitePath);
    if (!file) {
      await sendNotFound(response, request.method);
      return;
    }

    response.writeHead(200, {
      "content-type": contentType(file),
      "cache-control": "no-store",
    });
    if (request.method === "HEAD") response.end();
    else createReadStream(file).pipe(response);
  } catch (error) {
    response.writeHead(500, { "content-type": "text/plain; charset=utf-8" });
    response.end(error instanceof Error ? error.message : "Preview server error");
  }
});

server.listen(port, host, () => {
  const url = `http://${host}:${port}${basePath}/`;
  console.log(`GitHub Pages preview: ${url}`);
  console.log("The server uses strict static routes; missing deep pages return 404.");
});

for (const signal of ["SIGINT", "SIGTERM"] as const) {
  process.on(signal, () => server.close(() => process.exit(0)));
}

async function runBuild(base: string): Promise<number | null> {
  const command = process.platform === "win32" ? "npm.cmd" : "npm";
  return new Promise((resolve, reject) => {
    const child = spawn(command, ["run", "build"], {
      cwd: process.cwd(),
      env: { ...process.env, SITE_BASE_PATH: base },
      stdio: "inherit",
    });
    child.once("error", reject);
    child.once("exit", (code) => resolve(code));
  });
}

async function resolveStaticFile(requestPath: string): Promise<string | undefined> {
  let decoded: string;
  try {
    decoded = decodeURIComponent(requestPath);
  } catch {
    return undefined;
  }
  if (decoded.includes("\0")) return undefined;

  const relative = path.posix.normalize(`/${decoded}`).replace(/^\/+/, "");
  const direct = path.resolve(clientDir, relative);
  if (!direct.startsWith(`${clientDir}${path.sep}`) && direct !== clientDir) {
    return undefined;
  }

  const candidates = requestPath.endsWith("/") || !relative
    ? [path.join(direct, "index.html")]
    : path.extname(relative)
      ? [direct]
      : [direct, `${direct}.html`, path.join(direct, "index.html")];

  for (const candidate of candidates) {
    if (await isFile(candidate)) return candidate;
  }
  return undefined;
}

async function sendNotFound(
  response: import("node:http").ServerResponse,
  method?: string,
): Promise<void> {
  const notFound = path.join(clientDir, "404.html");
  response.writeHead(404, {
    "content-type": "text/html; charset=utf-8",
    "cache-control": "no-store",
  });
  if (method === "HEAD") {
    response.end();
  } else if (await isFile(notFound)) {
    createReadStream(notFound).pipe(response);
  } else {
    response.end("Not found");
  }
}

async function isFile(file: string): Promise<boolean> {
  try {
    return (await stat(file)).isFile();
  } catch {
    return false;
  }
}

function argumentValue(name: string): string | undefined {
  const index = args.indexOf(name);
  return index >= 0 ? args[index + 1] : undefined;
}

function normalizeBasePath(value: string): string {
  if (!value || value === "/") return "";
  return `/${value.replace(/^\/+|\/+$/gu, "")}`;
}

function contentType(file: string): string {
  const extension = path.extname(file).toLowerCase();
  const types: Record<string, string> = {
    ".avif": "image/avif",
    ".css": "text/css; charset=utf-8",
    ".csv": "text/csv; charset=utf-8",
    ".gif": "image/gif",
    ".html": "text/html; charset=utf-8",
    ".ico": "image/x-icon",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".js": "text/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".mjs": "text/javascript; charset=utf-8",
    ".pdf": "application/pdf",
    ".png": "image/png",
    ".py": "text/plain; charset=utf-8",
    ".svg": "image/svg+xml",
    ".txt": "text/plain; charset=utf-8",
    ".webp": "image/webp",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".woff": "font/woff",
    ".woff2": "font/woff2",
  };
  return types[extension] ?? "application/octet-stream";
}
