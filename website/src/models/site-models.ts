import { SITE, withBasePath } from "../config/site";
import type {
  AboutPageModel,
  BreadcrumbItem,
  HomePageModel,
  LearningUnit,
  MaterialsPageModel,
  ReaderPageModel,
  SearchPageModel,
  UnitPageModel,
} from "../config/types";
import type {
  ContentManifest,
  ContentPageDocument,
  ContentPageSummary,
  NavigationNode,
  ResourceCollection,
} from "../content/types";

const UNIT_DESCRIPTIONS: Record<string, string> = {
  "00": "เริ่มต้นใช้งาน Python และเครื่องมือที่จำเป็น",
  "01": "ชนิดข้อมูล ตัวแปร นิพจน์ และการคำนวณ",
  "02": "ข้อความและลิสต์พื้นฐาน",
  "03": "เงื่อนไขและการเลือกทำงาน",
  "04": "การทำงานซ้ำด้วยลูป",
  "05": "การประมวลผลข้อมูลในลิสต์",
  "06": "ออกแบบและเรียกใช้ฟังก์ชัน",
  "07": "ประมวลผลข้อความและไฟล์",
  "08": "พจนานุกรมและการค้นหาข้อมูล",
  "09": "โครงสร้างข้อมูลแบบซ้อน",
  "10": "ทูเพิล เซต และพจนานุกรม",
  "11": "คำนวณข้อมูลด้วย NumPy",
  "12": "คลาส ออบเจ็กต์ และการออกแบบโปรแกรม",
};

function cleanGroupName(group: string): string {
  return group
    .replace(/^\d{2}-/, "")
    .replace(/^(?:P\d|PL|GE|EX|SM|IC)-/, "")
    .replace(/-/g, " ");
}

function pageForRoute(
  manifest: ContentManifest,
  route: string,
): ContentPageSummary | undefined {
  return manifest.pages.find((page) => page.route === route);
}

function topLevelUnits(manifest: ContentManifest): ContentPageSummary[] {
  return manifest.pages
    .filter(
      (page) =>
        page.sourcePath !== null &&
        /^\d{2}-[^/]+\/README\.md$/.test(page.sourcePath),
    )
    .sort((left, right) => left.group.localeCompare(right.group, "en"));
}

function baseNavigation(nodes: NavigationNode[]): NavigationNode[] {
  return nodes.map((node) => ({
    ...node,
    children: baseNavigation(node.children),
  }));
}

function breadcrumbsFor(
  manifest: ContentManifest,
  page: ContentPageSummary,
): BreadcrumbItem[] {
  const crumbs: BreadcrumbItem[] = [
    { label: "หน้าแรก", href: SITE.basePath },
  ];
  if (page.route === "/about/") {
    crumbs.push({ label: "เกี่ยวกับรายวิชา" });
    return crumbs;
  }

  const segments = page.route.split("/").filter(Boolean);
  let route = "/";
  for (const [index, segment] of segments.entries()) {
    route += `${segment}/`;
    const matchingPage = pageForRoute(manifest, route);
    crumbs.push({
      label:
        matchingPage?.title && matchingPage.title !== "Contents"
          ? matchingPage.title
          : cleanGroupName(segment),
      // Some repository group directories intentionally have no README. Keep
      // their fallback label in the trail, but do not emit a dead directory URL.
      href:
        index === segments.length - 1 || !matchingPage
          ? undefined
          : withBasePath(route),
    });
  }
  return crumbs;
}

function summaryWithBaseRoute(
  page: ContentPageSummary | undefined,
): ContentPageSummary | undefined {
  return page ? { ...page, route: withBasePath(page.route) } : undefined;
}

export function createHomeModel(manifest: ContentManifest): HomePageModel {
  const units: LearningUnit[] = topLevelUnits(manifest).map((page, index) => {
    const code = page.group.slice(0, 2);
    const lessonCount = manifest.pages.filter(
      (candidate) =>
        candidate.group === page.group && candidate.route !== page.route,
    ).length;
    return {
      code,
      title: cleanGroupName(page.group),
      description: UNIT_DESCRIPTIONS[code] ?? "บทเรียนและแบบฝึกหัด",
      href: withBasePath(page.route),
      lessonCount,
      state: index === 0 ? "current" : "available",
    };
  });

  return {
    title: "เรียน Python\nอย่างเป็นขั้นตอน",
    description:
      "สรุปบทเรียน แบบฝึกหัด และเฉลยสำหรับรายวิชา 2110101 COMPUTER PROGRAMMING",
    primaryAction: {
      label: "เริ่มเรียนบทที่ 00",
      href: units[0]?.href ?? withBasePath("/00-Python-Intro/"),
    },
    secondaryAction: {
      label: "ดูแบบฝึกหัดทั้งหมด",
      href: withBasePath("/PL-Problem-List/"),
    },
    units,
    quickAccess: [
      {
        eyebrow: "LECTURE",
        title: "สรุป Lecture",
        description: "สรุปเนื้อหาจากการบรรยายทุกบท",
        href: units[0]?.href ?? withBasePath("/00-Python-Intro/"),
        icon: "file-text",
        tone: "blue",
      },
      {
        eyebrow: "PRACTICE",
        title: "แบบฝึกหัด P1–P3",
        description: "โจทย์และเฉลยสำหรับฝึกทักษะ",
        href: withBasePath("/P1-Grader-01-Practice/"),
        icon: "braces",
        tone: "yellow",
      },
      {
        eyebrow: "EXAM ARCHIVE",
        title: "คลังข้อสอบเก่า",
        description: "ข้อสอบ Grader พร้อมเฉลยย้อนหลัง",
        href: withBasePath("/GE-Grader-Examination/"),
        icon: "book-open",
        tone: "navy",
      },
      {
        eyebrow: "RESOURCES",
        title: "Study Materials",
        description: "เอกสาร สไลด์ และคู่มือประกอบการเรียน",
        href: withBasePath("/SM-Study-Materials/"),
        icon: "library",
        tone: "blue",
      },
    ],
  };
}

export function createUnitModel(
  manifest: ContentManifest,
  document: ContentPageDocument,
): UnitPageModel {
  const units = topLevelUnits(manifest);
  const unitIndex = units.findIndex((unit) => unit.route === document.route);
  const directChildren = manifest.pages.filter((page) => {
    if (!page.sourcePath || page.group !== document.group) return false;
    const parts = page.sourcePath.split("/");
    return parts.length === 3 && page.route !== document.route;
  });
  const code = document.group.slice(0, 2);

  return {
    code,
    title: cleanGroupName(document.group),
    description: UNIT_DESCRIPTIONS[code],
    breadcrumbs: breadcrumbsFor(manifest, document),
    lectures: directChildren
      .filter((page) => /\/Lecture\/README\.md$/.test(page.sourcePath ?? ""))
      .map((page, index) => ({
        number: String(index + 1).padStart(2, "0"),
        title: page.title,
        href: withBasePath(page.route),
        description: page.headings[0]?.text,
      })),
    exercises: directChildren
      .filter((page) => !/\/Lecture\/README\.md$/.test(page.sourcePath ?? ""))
      .map((page) => ({
        code: page.code ?? page.route.split("/").filter(Boolean).at(-1) ?? "",
        title: page.title,
        href: withBasePath(page.route),
        difficulty: page.difficulty
          ? Math.max(0, (page.difficulty.match(/★/g) ?? []).length)
          : undefined,
        solutionHref: withBasePath(page.route),
      })),
    previous:
      unitIndex > 0
        ? {
            label: `${units[unitIndex - 1].group.slice(0, 2)} ${cleanGroupName(units[unitIndex - 1].group)}`,
            href: withBasePath(units[unitIndex - 1].route),
          }
        : { label: "ภาพรวมหลักสูตร", href: SITE.basePath },
    next:
      unitIndex >= 0 && unitIndex < units.length - 1
        ? {
            label: `${units[unitIndex + 1].group.slice(0, 2)} ${cleanGroupName(units[unitIndex + 1].group)}`,
            href: withBasePath(units[unitIndex + 1].route),
          }
        : undefined,
    sidebar: baseNavigation(manifest.navigation),
    currentRoute: document.route,
  };
}

export function createReaderModel(
  manifest: ContentManifest,
  document: ContentPageDocument,
): ReaderPageModel {
  const sourceHref = document.sourcePath
    ? `${SITE.repositoryUrl}/blob/main/${document.sourcePath}`
    : undefined;
  return {
    document,
    breadcrumbs: breadcrumbsFor(manifest, document),
    sidebar: baseNavigation(manifest.navigation),
    sourceHref,
    repositoryHref: document.sourcePath
      ? `${SITE.repositoryUrl}/tree/main/${document.sourcePath.replace(/\/README\.md$/, "")}`
      : SITE.repositoryUrl,
    previous: summaryWithBaseRoute(
      document.previous
        ? pageForRoute(manifest, document.previous.route)
        : undefined,
    ),
    next: summaryWithBaseRoute(
      document.next ? pageForRoute(manifest, document.next.route) : undefined,
    ),
  };
}

export function createAboutModel(
  manifest: ContentManifest,
  document: ContentPageDocument,
): AboutPageModel {
  return {
    title: document.title,
    description: SITE.description,
    html: document.html,
    breadcrumbs: breadcrumbsFor(manifest, document),
    repositoryHref: SITE.repositoryUrl,
  };
}

function splitResourceCollection(
  collection: ResourceCollection,
): ResourceCollection[] {
  const grouped = new Map<string, ResourceCollection["entries"]>();
  for (const entry of collection.entries) {
    const key = entry.group || "เอกสารอื่น ๆ";
    const entries = grouped.get(key) ?? [];
    entries.push(entry);
    grouped.set(key, entries);
  }
  return [...grouped.entries()].map(([group, entries], index) => ({
    ...collection,
    id: `${collection.id}-${index}`,
    title: cleanGroupName(group),
    entries,
  }));
}

export function createMaterialsModel(
  manifest: ContentManifest,
  route: string,
): MaterialsPageModel {
  const matching = manifest.resources.filter(
    (collection) => collection.route === route,
  );
  const collections = matching.flatMap(splitResourceCollection);
  return {
    title:
      route === "/SM-Study-Materials/"
        ? "สื่อการเรียน"
        : cleanGroupName(route.split("/").filter(Boolean)[0] ?? "Resources"),
    description: "เอกสารและไฟล์ประกอบที่สร้างรายการอัตโนมัติจากรีโพซิทอรี",
    breadcrumbs: [
      { label: "หน้าแรก", href: SITE.basePath },
      { label: "สื่อการเรียน" },
    ],
    collections,
  };
}

export function createSearchModel(
  manifest: ContentManifest,
): SearchPageModel {
  return {
    featured: manifest.pages.slice(0, 8).map((page) => ({
      id: page.id,
      title: page.title,
      excerpt: page.headings.map((heading) => heading.text).slice(0, 2).join(" · "),
      href: withBasePath(page.route),
      group: page.group,
      code: page.code,
      kind: page.kind,
    })),
  };
}
