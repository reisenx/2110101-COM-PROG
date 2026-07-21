import { useEffect, useRef } from 'react'
import { UI_LABELS } from '../config/site'

interface MarkdownArticleProps {
  html: string
  className?: string
}

export function MarkdownArticle({ html, className }: MarkdownArticleProps) {
  const articleRef = useRef<HTMLElement>(null)

  useEffect(() => {
    const article = articleRef.current
    if (!article) return
    const blocks = article.querySelectorAll('pre')
    blocks.forEach((block, index) => {
      block.dataset.codeBlock = String(index)
      block.tabIndex = 0
      if (block.querySelector('.code-copy-button')) return

      const button = document.createElement('button')
      button.type = 'button'
      button.className = 'code-copy-button'
      button.setAttribute('aria-label', UI_LABELS.copyCode)
      button.innerHTML = `<span aria-hidden="true">⧉</span><span>${UI_LABELS.copyCode}</span>`
      button.addEventListener('click', async () => {
        const source = block.querySelector('code')?.textContent ?? block.textContent ?? ''
        try {
          await navigator.clipboard.writeText(source)
          button.dataset.copied = 'true'
          button.lastElementChild!.textContent = UI_LABELS.copied
          window.setTimeout(() => {
            button.dataset.copied = 'false'
            button.lastElementChild!.textContent = UI_LABELS.copyCode
          }, 1800)
        } catch {
          button.dataset.copied = 'false'
        }
      })
      block.append(button)
    })

    return () => article.querySelectorAll('.code-copy-button').forEach((button) => button.remove())
  }, [html])

  return (
    <article
      ref={articleRef}
      className={['markdown-body', className].filter(Boolean).join(' ')}
    >
      <div dangerouslySetInnerHTML={{ __html: html }} />
    </article>
  )
}
