import { expect, test } from '@playwright/test'

let runtimeErrors: string[]

test.beforeEach(async ({ page }) => {
  runtimeErrors = []
  page.on('pageerror', (error) => runtimeErrors.push(error.message))
  page.on('console', (message) => {
    if (message.type() === 'error') runtimeErrors.push(message.text())
  })
})

test.afterEach(async () => {
  expect(runtimeErrors, 'the page should not report runtime or console errors').toEqual([])
})

test('homepage renders without horizontal overflow at each supported viewport', async ({
  page,
}, testInfo) => {
  await page.goto('./')

  await expect(page).toHaveTitle(/2110101|COMP PROG/i)
  await expect(page.locator('main')).toBeVisible()
  await expect(page.locator('main').getByRole('heading', { level: 1 }).first()).toBeVisible()

  const hasHorizontalOverflow = await page.evaluate(
    () => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
  )
  expect(hasHorizontalOverflow).toBe(false)

  const desktopNavigation = page.getByRole('navigation', { name: 'เมนูหลัก', exact: true })
  const menuButton = page.locator('.site-menu-button')
  if (testInfo.project.name === 'Desktop Chromium') {
    await expect(desktopNavigation).toBeVisible()
    await expect(menuButton).toBeHidden()
  } else {
    await expect(desktopNavigation).toBeHidden()
    await expect(menuButton).toBeVisible()
  }
})

test('a deep README route survives a direct visit and refresh', async ({ page }) => {
  await page.goto('./00-Python-Intro/00_Intro_01/')

  await expect(page).toHaveTitle(/Hello/)
  await expect(page.locator('main')).toBeVisible()
  const heading = page.locator('main').getByRole('heading', { level: 1 }).first()
  await expect(heading).toBeVisible()
  const headingText = await heading.textContent()

  await page.reload()

  await expect(page).toHaveTitle(/Hello/)
  await expect(page.locator('main').getByRole('heading', { level: 1 }).first()).toHaveText(
    headingText ?? '',
  )
  await expect(page).toHaveURL(/\/00-Python-Intro\/00_Intro_01\/$/)

  const codeBlocks = await page.locator('.markdown-body pre').count()
  await expect(page.locator('.markdown-body .code-copy-button')).toHaveCount(codeBlocks)

  const hasHorizontalOverflow = await page.evaluate(
    () => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
  )
  expect(hasHorizontalOverflow).toBe(false)
})

test('the unit index contains its exercise table at every viewport', async ({ page }) => {
  await page.goto('./00-Python-Intro/')

  await expect(page.locator('main').getByRole('heading', { level: 1 }).first()).toBeVisible()
  const metrics = await page.evaluate(() => {
    const wrapper = document.querySelector<HTMLElement>('.exercise-table-wrap')
    return {
      pageOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
      tableContained: wrapper ? wrapper.scrollWidth >= wrapper.clientWidth : false,
    }
  })
  expect(metrics.pageOverflow).toBe(false)
  expect(metrics.tableContained).toBe(true)
})

test('README search opens and returns a navigable result', async ({ page }, testInfo) => {
  test.skip(testInfo.project.name !== 'Desktop Chromium', 'one search smoke test is sufficient')

  await page.goto('./')
  await page.locator('.site-search-button').click()

  const dialog = page.getByRole('dialog', { name: 'ค้นหาในเว็บไซต์' })
  await expect(dialog).toBeVisible()
  await dialog.getByRole('searchbox').fill('Hello')
  const firstResult = dialog.locator('.search-results a').first()
  await expect(firstResult).toBeVisible({ timeout: 15_000 })
  await expect(firstResult).toHaveAttribute('href', /00-Python-Intro|Intro/i)
})

test('mobile menu opens and exposes navigation and search', async ({ page }, testInfo) => {
  test.skip(testInfo.project.name !== 'Mobile Chromium', 'mobile-only interaction')

  await page.goto('./')
  const menuButton = page.locator('.site-menu-button')
  await menuButton.click()

  await expect(menuButton).toHaveAttribute('aria-expanded', 'true')
  const navigation = page.getByRole('navigation', { name: 'เมนูหลักบนมือถือ' })
  await expect(navigation).toBeVisible()
  await expect(navigation.getByRole('link', { name: 'บทเรียน' })).toBeVisible()

  await navigation.getByRole('button', { name: 'ค้นหา' }).click()
  await expect(page.getByRole('dialog', { name: 'ค้นหาในเว็บไซต์' })).toBeVisible()
  await expect(menuButton).toHaveAttribute('aria-expanded', 'false')
})
