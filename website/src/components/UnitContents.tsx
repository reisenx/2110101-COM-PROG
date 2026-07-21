import { ArrowRight, CheckCircle2, FileText } from 'lucide-react'
import { UI_LABELS } from '../config/site'
import type { ExerciseItem, LectureItem } from '../config/types'

interface LectureListProps {
  items: LectureItem[]
}

export function LectureList({ items }: LectureListProps) {
  if (items.length === 0) return <EmptySection />
  return (
    <ol className="lecture-list">
      {items.map((item) => (
        <li key={`${item.number}-${item.href}`}>
          <a href={item.href}>
            <span className="lecture-list__number">{item.number}</span>
            <span className="lecture-list__icon"><FileText aria-hidden="true" size={20} /></span>
            <span className="lecture-list__copy">
              <strong>{item.title}</strong>
              {item.description ? <span>{item.description}</span> : null}
            </span>
            {item.meta ? <span className="lecture-list__meta">{item.meta}</span> : null}
            <ArrowRight aria-hidden="true" size={19} />
          </a>
        </li>
      ))}
    </ol>
  )
}

function Difficulty({ value = 0 }: { value?: number }) {
  const clamped = Math.max(0, Math.min(5, value))
  return (
    <span className="difficulty" aria-label={`${UI_LABELS.difficulty} ${clamped} จาก 5`}>
      {Array.from({ length: 5 }, (_, index) => (
        <span key={index} data-filled={index < clamped || undefined} aria-hidden="true">★</span>
      ))}
    </span>
  )
}

interface ExerciseTableProps {
  items: ExerciseItem[]
}

export function ExerciseTable({ items }: ExerciseTableProps) {
  if (items.length === 0) return <EmptySection />
  return (
    <div className="exercise-table-wrap">
      <table className="exercise-table">
        <thead>
          <tr>
            <th scope="col">รหัส</th>
            <th scope="col">ชื่อโจทย์</th>
            <th scope="col">ความยาก</th>
            <th scope="col"><span className="visually-hidden">เปิดโจทย์</span></th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <tr key={`${item.code}-${item.href}`}>
              <td><code>{item.code}</code></td>
              <td>
                <a href={item.href}>
                  <strong>{item.title}</strong>
                </a>
                {item.solutionHref ? (
                  <a className="solution-badge" href={item.solutionHref}>
                    <CheckCircle2 aria-hidden="true" size={14} /> มีเฉลย
                  </a>
                ) : null}
              </td>
              <td><Difficulty value={item.difficulty} /></td>
              <td><a className="table-arrow" href={item.href} aria-label={`เปิดโจทย์ ${item.title}`}><ArrowRight aria-hidden="true" /></a></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export function EmptySection() {
  return (
    <div className="empty-section">
      <FileText aria-hidden="true" />
      <p>{UI_LABELS.emptySection}</p>
    </div>
  )
}
