import { describe, expect, it } from "vitest";

import {
  buildNavigation,
  extractOrderedReadmeTargets,
  isCourseReadme,
  isVisitorAsset,
} from "../../src/content/pipeline";
import type { ContentPageSummary } from "../../src/content/types";

describe("content discovery", () => {
  it("accepts course READMEs and excludes website or hidden documentation", () => {
    expect(isCourseReadme("README.md")).toBe(true);
    expect(isCourseReadme("00-Python-Intro/README.md")).toBe(true);
    expect(isCourseReadme("website/README.md")).toBe(false);
    expect(isCourseReadme(".github/README.md")).toBe(false);
    expect(isCourseReadme("notes.md")).toBe(false);
  });

  it("extracts collection table order using repository-relative resolution", () => {
    const markdown = `
| No. | Solution |
| --- | --- |
| 1 | [B](./B/README.md) |
| 2 | [A](/Unit/A/README.md#solution) |

[Back](../README.md)
`;
    expect(extractOrderedReadmeTargets(markdown, "Unit/README.md")).toEqual([
      "Unit/B/README.md",
      "Unit/A/README.md",
    ]);
  });

  it("builds a naturally sorted hierarchy with route-bearing pages", () => {
    const pages = [
      summary("/10-Tuple-Set-Dict/", "10 Tuple Set Dict"),
      summary("/02-Basic-String-and-List/", "02 Basic String and List"),
      summary("/02-Basic-String-and-List/02_StrList_01/", "Add Strings"),
    ];
    const navigation = buildNavigation(pages);

    expect(navigation.map((node) => node.route)).toEqual([
      "/02-Basic-String-and-List/",
      "/10-Tuple-Set-Dict/",
    ]);
    expect(navigation[0].children[0]).toMatchObject({
      label: "Add Strings",
      route: "/02-Basic-String-and-List/02_StrList_01/",
    });
  });

  it("copies visitor formats but excludes PSD files and tooling", () => {
    expect(isVisitorAsset("SM-Study-Materials/guide.pdf")).toBe(true);
    expect(isVisitorAsset("00-Python-Intro/example.py")).toBe(true);
    expect(isVisitorAsset("Z99-OTHERS/banner.png")).toBe(true);
    expect(isVisitorAsset("Z99-OTHERS/banner.psd")).toBe(false);
    expect(isVisitorAsset("PL-Problem-List/table-generate.py")).toBe(false);
    expect(isVisitorAsset("website/public/logo.png")).toBe(false);
  });
});

function summary(route: string, title: string): ContentPageSummary {
  return {
    id: route,
    sourcePath: `${route.slice(1)}README.md`,
    route,
    title,
    kind: "unit",
    group: route.split("/").filter(Boolean)[0],
    headings: [],
    documentPath: "pages/example.json",
  };
}
