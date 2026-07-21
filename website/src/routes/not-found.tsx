import { useMemo } from "react";

import { SITE } from "../config/site";
import { loadContentManifest } from "../content/server";
import type { ContentManifest } from "../content/types";
import { NotFoundPage } from "../pages/NotFoundPage";
import { createSearchProvider } from "../search/site-search";

export async function loader(): Promise<{ manifest: ContentManifest }> {
  return { manifest: await loadContentManifest() };
}

export function meta() {
  return [{ title: `ไม่พบหน้า · ${SITE.name}` }];
}

export default function NotFoundRoute({
  loaderData,
}: {
  loaderData: { manifest: ContentManifest };
}) {
  const search = useMemo(
    () => createSearchProvider(loaderData.manifest.pages),
    [loaderData.manifest.pages],
  );
  return <NotFoundPage search={search} />;
}
