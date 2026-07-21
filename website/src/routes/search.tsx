import { useMemo } from "react";

import { SITE } from "../config/site";
import { loadContentManifest } from "../content/server";
import type { ContentManifest } from "../content/types";
import { createSearchModel } from "../models/site-models";
import { SearchPage } from "../pages/SearchPage";
import { createSearchProvider } from "../search/site-search";

export async function loader(): Promise<{ manifest: ContentManifest }> {
  return { manifest: await loadContentManifest() };
}

export function meta() {
  return [
    { title: `ค้นหา · ${SITE.name}` },
    { name: "description", content: "ค้นหาบทเรียน โจทย์ และสื่อการเรียน" },
  ];
}

export default function SearchRoute({
  loaderData,
}: {
  loaderData: { manifest: ContentManifest };
}) {
  const { manifest } = loaderData;
  const model = useMemo(() => createSearchModel(manifest), [manifest]);
  const search = useMemo(
    () => createSearchProvider(manifest.pages),
    [manifest.pages],
  );
  return <SearchPage model={model} search={search} />;
}
