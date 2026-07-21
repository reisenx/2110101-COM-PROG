import { useMemo } from "react";
import type { LoaderFunctionArgs } from "react-router";

import { SITE } from "../config/site";
import {
  loadContentManifest,
  loadContentPageByRoute,
} from "../content/server";
import type {
  ContentManifest,
  ContentPageDocument,
} from "../content/types";
import {
  createAboutModel,
  createMaterialsModel,
  createReaderModel,
  createUnitModel,
} from "../models/site-models";
import { AboutPage } from "../pages/AboutPage";
import { MaterialsPage } from "../pages/MaterialsPage";
import { ReaderPage } from "../pages/ReaderPage";
import { UnitPage } from "../pages/UnitPage";
import { createSearchProvider } from "../search/site-search";

interface ContentLoaderData {
  manifest: ContentManifest;
  document: ContentPageDocument;
}

export async function loader({ params }: LoaderFunctionArgs): Promise<ContentLoaderData> {
  const route = `/${params["*"]?.replace(/^\/+|\/+$/g, "") ?? ""}/`;
  const [manifest, document] = await Promise.all([
    loadContentManifest(),
    loadContentPageByRoute(route),
  ]);
  if (!document) {
    throw new Response("Not Found", { status: 404, statusText: "Not Found" });
  }
  return { manifest, document };
}

export function meta({ loaderData }: { loaderData?: ContentLoaderData }) {
  if (!loaderData) return [{ title: `ไม่พบหน้า · ${SITE.name}` }];
  return [
    { title: `${loaderData.document.title} · ${SITE.name}` },
    {
      name: "description",
      content: `${loaderData.document.title} — เนื้อหารายวิชา 2110101 Computer Programming`,
    },
  ];
}

export default function ContentRoute({
  loaderData,
}: {
  loaderData: ContentLoaderData;
}) {
  const { manifest, document } = loaderData;
  const search = useMemo(
    () => createSearchProvider(manifest.pages),
    [manifest.pages],
  );

  if (document.kind === "about") {
    return (
      <AboutPage
        model={createAboutModel(manifest, document)}
        search={search}
      />
    );
  }
  if (document.kind === "unit") {
    return (
      <UnitPage
        model={createUnitModel(manifest, document)}
        search={search}
      />
    );
  }
  if (document.kind === "resource-index") {
    return (
      <MaterialsPage
        model={createMaterialsModel(manifest, document.route)}
        search={search}
      />
    );
  }
  return (
    <ReaderPage
      model={createReaderModel(manifest, document)}
      search={search}
    />
  );
}
