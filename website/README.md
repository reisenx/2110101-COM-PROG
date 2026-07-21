# 2110101 COMP PROG learning portal

This folder contains the custom static website for the course repository. The
site is Thai-first, responsive, and generated from the course's existing
`README.md` files. It does not require a backend, database, or CMS.

## How README synchronization works

The website does not store copies of course READMEs. Before every development
or production build, the content generator discovers the Git-tracked
`README.md` files outside `website/`, parses their metadata and Markdown, and
creates temporary data under `website/.generated/`. That directory and the
production output are ignored by Git.

As a result, a README addition, edit, rename, or removal on the branch being
built is reflected automatically the next time the site builds. A README change
is not uploaded immediately: the public site updates only after the Pages
workflow builds and deploys a push to `main`.

The generator keeps the existing clean directory routes. For example:

```text
00-Python-Intro/00_Intro_01/README.md
    -> /2110101-COMP-PROG/00-Python-Intro/00_Intro_01/
```

README-authored links and asset paths are normalized in generated output. The
source README files themselves are never rewritten.

## Local development and preview

Node.js 24 or newer is required. Run commands from this folder:

```bash
cd website
npm ci
npm run dev
```

The development command prints its local URL and watches application files.
Restart it after adding, renaming, or removing README files so the content
manifest is regenerated.

For a production-equivalent preview, including static README routes and the
Pagefind search index, run:

```bash
npm run preview:pages
```

Open the URL printed by the command (normally
`http://127.0.0.1:4173/2110101-COMP-PROG/`). This preview is entirely local: it
does not merge a branch, change repository settings, or replace the live site.

Useful verification commands are:

```bash
npm run test
npm run typecheck
npm run build
npx playwright install chromium
npm run test:e2e
npm run check
```

`npm run test:e2e` starts the production preview automatically and checks the
desktop, tablet, and mobile layouts. Playwright screenshots, traces, and videos
are written to the operating system's temporary directory rather than tracked
repository paths.

To test another GitHub Pages prefix locally, set `SITE_BASE_PATH` for both the
build and preview:

```bash
SITE_BASE_PATH=/another-project npm run preview:pages
```

## Customization map

| Customize | Location |
| --- | --- |
| Site name, Thai labels, main navigation, repository URL | `src/config/site.ts` |
| Configuration and content types | `src/config/types.ts`, `src/content/types.ts` |
| Colors, fonts, spacing, responsive breakpoints | `src/styles/theme.css`, `src/styles/site.css` |
| Header, mobile menu, sidebar, search, breadcrumbs, TOC | `src/components/` |
| Homepage sections and featured links | `src/pages/HomePage.tsx` |
| README and generated collection layouts | `src/pages/ReaderPage.tsx`, `src/pages/UnitPage.tsx`, `src/pages/MaterialsPage.tsx` |
| README discovery, metadata overrides, link normalization | `scripts/` and `src/content/` |

Prefer configuration overrides and resilient extraction fallbacks over editing
course READMEs solely for presentation. This keeps teaching-content branches
independent of the website implementation.

## GitHub Pages workflow and branch safety

The workflow at `.github/workflows/website-pages.yml` validates pushes to
`feat/website` and `main`, pull requests, and manual runs. Every trigger installs
dependencies, runs tests and type checking, builds all discovered README routes,
and executes responsive browser smoke tests.

Deployment has two independent guards: the ref must be `refs/heads/main`, and
the event must be a push. Therefore, pushing or manually running the workflow
from `feat/website` cannot deploy or replace the live Pages site. Manual runs
validate the website but never deploy it.
The implementation is intentionally confined to `website/**` plus that one new
workflow, so it does not overlap branches that only edit course READMEs.

After the feature is reviewed and separately merged, enable the new deployment
once in **Repository Settings → Pages → Build and deployment → Source → GitHub
Actions**. Until that setting is changed, the existing branch-published site
remains active. Do not change the setting merely to preview this feature branch;
use `npm run preview:pages` instead.

## Hosting cost

For this public repository, GitHub Pages hosting remains available on GitHub
Free, so an expired GitHub Pro subscription does not add a Pages hosting charge
or take down the site. Standard GitHub-hosted Actions usage for public
repositories is also free. A separately purchased custom domain, a larger
Actions runner, or making the repository private can introduce different plan
or billing requirements.

- [GitHub Pages availability](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
- [Using custom workflows with GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
