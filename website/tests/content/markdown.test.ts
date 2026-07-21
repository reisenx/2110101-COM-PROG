import { describe, expect, it } from "vitest";

import { renderMarkdown } from "../../src/content/markdown";

describe("Markdown rendering", () => {
  it("renders GFM, alerts and highlighted code while removing legacy chrome", async () => {
    const markdown = `
<p><a href="../README.md"><img src="../../Z99-OTHERS/00-common/00-back.png" onerror="alert(1)" style="width:10%"></a></p>
<div align="center"><h1>Hello ☆ (<code>00_Intro_01</code>)</h1></div>

# Contents
- [หัวข้อ](#หัวข้อ)
---
## หัวข้อ
> [!NOTE]
>
> รายละเอียด

| A | B |
| - | - |
| 1 | 2 |

\`\`\`python
print("hello")
\`\`\`
`;
    const rendered = await renderMarkdown(markdown, {
      sourcePath: "00-Python-Intro/00_Intro_01/README.md",
      title: "Hello",
      kind: "lesson",
      basePath: "/2110101-COMP-PROG",
    });

    expect(rendered.html).not.toContain("00-back.png");
    expect(rendered.html).not.toContain(">Contents<");
    expect(rendered.html).toContain("markdown-alert-note");
    expect(rendered.html).toContain("รายละเอียด");
    expect(rendered.html).toContain("<table>");
    expect(rendered.html).toContain("data-rehype-pretty-code-figure");
    expect(rendered.headings).toEqual([
      { depth: 2, id: "หัวข้อ", text: "หัวข้อ" },
    ]);
  });

  it("sanitizes scripts, event handlers and unsafe protocols", async () => {
    const rendered = await renderMarkdown(
      '<script>alert(1)</script><a href="javascript:alert(1)" onclick="alert(2)">bad</a><img src="/safe.png" onload="alert(3)">',
      {
        sourcePath: "README.md",
        title: "About",
        kind: "about",
        basePath: "",
      },
    );

    expect(rendered.html).not.toContain("<script");
    expect(rendered.html).not.toContain("javascript:");
    expect(rendered.html).not.toContain("onclick");
    expect(rendered.html).not.toContain("onload");
    expect(rendered.html).toContain('src="/safe.png"');
  });

  it("rewrites Markdown and raw HTML links using the same rules", async () => {
    const rendered = await renderMarkdown(
      '[Markdown](../README.md#top) <a href="/PL-Problem-List/README.md">HTML</a>',
      {
        sourcePath: "00-Python-Intro/Lecture/README.md",
        title: "Lecture",
        kind: "lecture",
        basePath: "/2110101-COMP-PROG",
      },
    );

    expect(rendered.html).toContain(
      'href="/2110101-COMP-PROG/00-Python-Intro/#top"',
    );
    expect(rendered.html).toContain(
      'href="/2110101-COMP-PROG/PL-Problem-List/"',
    );
  });
});
