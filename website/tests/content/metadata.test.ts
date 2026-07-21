import { describe, expect, it } from "vitest";

import { extractMetadata, routeFromReadme } from "../../src/content/metadata";

describe("README metadata", () => {
  it("extracts a centered HTML problem title, difficulty and code", () => {
    const markdown = `
<div align="center">
  <h1>Mountain Valley ★★☆ (<a href="#"><code>00_Intro_03</code></a>)</h1>
</div>
# Contents
# Solution
`;
    expect(
      extractMetadata("00-Python-Intro/00_Intro_03/README.md", markdown),
    ).toMatchObject({
      route: "/00-Python-Intro/00_Intro_03/",
      title: "Mountain Valley",
      code: "00_Intro_03",
      difficulty: "★★☆",
      kind: "lesson",
      group: "00-Python-Intro",
    });
  });

  it("uses directory names for unit pages instead of generic headings", () => {
    expect(
      extractMetadata("03-Selection/README.md", "# แบบฝึกหัด\n"),
    ).toMatchObject({ title: "03 Selection", kind: "unit" });
  });

  it("gives lectures a stable fallback title", () => {
    expect(
      extractMetadata(
        "01-Data-Type-and-Expression/Lecture/README.md",
        "# Contents\n# ส่วนที่ 1",
      ),
    ).toMatchObject({
      title: "01 Data Type And Expression · Lecture",
      kind: "lecture",
    });
  });

  it("does not treat headings inside fenced solutions as page titles", () => {
    const markdown = "# Contents\n```python\n# Not a title\n```\n# Solution";
    expect(
      extractMetadata("misc/Guide/README.md", markdown),
    ).toMatchObject({ title: "Guide", kind: "document" });
  });

  it("maps the repository README to About", () => {
    expect(routeFromReadme("README.md")).toBe("/about/");
  });
});
