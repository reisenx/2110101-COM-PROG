import { ArrowRight } from 'lucide-react'
import type { LearningUnit } from '../config/types'

interface LearningRailProps {
  units: LearningUnit[]
}

export function LearningRail({ units }: LearningRailProps) {
  return (
    <div className="learning-rail" role="list" aria-label="ลำดับบทเรียน">
      {units.map((unit, index) => (
        <a
          key={`${unit.code}-${unit.href}`}
          className="learning-unit"
          data-state={unit.state ?? 'available'}
          href={unit.href}
          role="listitem"
        >
          <span className="learning-unit__index">{String(index + 1).padStart(2, '0')}</span>
          <span className="learning-unit__code">{unit.code}</span>
          <strong>{unit.title}</strong>
          <p>{unit.description}</p>
          <span className="learning-unit__footer">
            <span>{unit.lessonCount ? `${unit.lessonCount} หัวข้อ` : 'เปิดบทเรียน'}</span>
            <ArrowRight aria-hidden="true" size={18} />
          </span>
        </a>
      ))}
    </div>
  )
}
