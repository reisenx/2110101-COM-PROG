import { defineConfig, devices } from '@playwright/test'
import os from 'node:os'
import path from 'node:path'

function normalizeBasePath(value: string | undefined): string {
  if (!value || value === '/') return ''
  return `/${value.replace(/^\/+|\/+$/g, '')}`
}

const siteBasePath = normalizeBasePath(
  process.env.SITE_BASE_PATH ?? '/2110101-COMP-PROG',
)
const previewOrigin = process.env.PLAYWRIGHT_ORIGIN ?? 'http://127.0.0.1:4173'
const previewUrl = `${previewOrigin}${siteBasePath}/`
const artifactRoot = path.join(os.tmpdir(), 'comp-prog-playwright')

export default defineConfig({
  testDir: './tests/e2e',
  fullyParallel: true,
  forbidOnly: Boolean(process.env.CI),
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 2 : undefined,
  reporter: process.env.CI ? [['github'], ['line']] : [['list']],
  outputDir: path.join(artifactRoot, 'results'),
  use: {
    baseURL: previewUrl,
    screenshot: 'only-on-failure',
    trace: 'retain-on-failure',
    video: 'retain-on-failure',
  },
  expect: {
    timeout: 10_000,
  },
  webServer: {
    command: 'npm run preview:pages -- --no-build',
    env: {
      SITE_BASE_PATH: siteBasePath,
    },
    url: previewUrl,
    reuseExistingServer: !process.env.CI,
    timeout: 300_000,
    stdout: 'pipe',
    stderr: 'pipe',
  },
  projects: [
    {
      name: 'Desktop Chromium',
      use: {
        ...devices['Desktop Chrome'],
        viewport: { width: 1440, height: 900 },
      },
    },
    {
      name: 'Tablet Chromium',
      use: {
        viewport: { width: 834, height: 1112 },
        deviceScaleFactor: 1,
        hasTouch: true,
        isMobile: true,
      },
    },
    {
      name: 'Mobile Chromium',
      use: {
        ...devices['Pixel 7'],
      },
    },
  ],
})
