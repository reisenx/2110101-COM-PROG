import { describe, expect, it } from "vitest";

import {
  normalizeContentUrl,
  readmePathToRoute,
  resourceHref,
} from "../../src/content/paths";

describe("content URL normalization", () => {
  const source = "00-Python-Intro/00_Intro_01/README.md";
  const base = "/2110101-COMP-PROG";

  it("turns repository-root README links into project-scoped routes", () => {
    expect(
      normalizeContentUrl("/01-Data-Type-and-Expression/README.md", source, base),
    ).toBe("/2110101-COMP-PROG/01-Data-Type-and-Expression/");
  });

  it("resolves relative README links and preserves fragments", () => {
    expect(normalizeContentUrl("../README.md#แบบฝึกหัด", source, base)).toBe(
      "/2110101-COMP-PROG/00-Python-Intro/#แบบฝึกหัด",
    );
  });

  it("maps the repository root README to the About route", () => {
    expect(normalizeContentUrl("../../README.md?from=lesson", source, base)).toBe(
      "/2110101-COMP-PROG/about/?from=lesson",
    );
    expect(readmePathToRoute("README.md")).toBe("/about/");
  });

  it("normalizes assets without double-prefixing an existing base", () => {
    expect(
      normalizeContentUrl(
        "/2110101-COMP-PROG/Z99-OTHERS/00-main/hero image.png",
        source,
        base,
      ),
    ).toBe("/2110101-COMP-PROG/Z99-OTHERS/00-main/hero%20image.png");
    expect(resourceHref("SM-Study-Materials/คู่มือ.pdf", base)).toBe(
      "/2110101-COMP-PROG/SM-Study-Materials/%E0%B8%84%E0%B8%B9%E0%B9%88%E0%B8%A1%E0%B8%B7%E0%B8%AD.pdf",
    );
  });

  it("leaves external, protocol-relative, data and fragment URLs unchanged", () => {
    for (const value of [
      "https://example.com/README.md",
      "//cdn.example.com/image.png",
      "data:image/png;base64,abc",
      "#solution",
    ]) {
      expect(normalizeContentUrl(value, source, base)).toBe(value);
    }
  });
});
