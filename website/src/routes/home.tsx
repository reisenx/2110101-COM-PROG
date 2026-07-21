import { useMemo } from "react";

import { SITE } from "../config/site";
import { loadContentManifest } from "../content/server";
import type { ContentManifest } from "../content/types";
import { createHomeModel } from "../models/site-models";
import { HomePage } from "../pages/HomePage";
import { createSearchProvider } from "../search/site-search";

export async function loader(): Promise<{ manifest: ContentManifest }> {
  return { manifest: await loadContentManifest() };
}

export function meta() {
  return [
    { title: `${SITE.name} · เรียน Python อย่างเป็นขั้นตอน` },
    { name: "description", content: SITE.description },
  ];
}

export default function HomeRoute({
  loaderData,
}: {
  loaderData: { manifest: ContentManifest };
}) {
  const { manifest } = loaderData;
  const model = useMemo(() => createHomeModel(manifest), [manifest]);
  const search = useMemo(
    () => createSearchProvider(manifest.pages),
    [manifest.pages],
  );
  return <HomePage model={model} search={search} />;
}
