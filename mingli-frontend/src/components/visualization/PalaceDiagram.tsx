import { useState } from 'react'
import clsx from 'clsx'

interface PalaceRelation {
  from: string
  to: string
  type: '相生' | '相克' | '相合' | '冲'
  strength: number
}

interface PalaceDiagramProps {
  mainPalace: string
  palaces: string[]
  relations?: PalaceRelation[]
  onPalaceClick?: (palace: string) => void
}

const palacePositions: Record<string, { x: number; y: number }> = {
  '命宫': { x: 50, y: 10 },
  '父母宫': { x: 85, y: 20 },
  '田宅宫': { x: 95, y: 50 },
  '福德宫': { x: 85, y: 80 },
  '官禄宫': { x: 50, y: 90 },
  '奴仆宫': { x: 15, y: 80 },
  '迁移宫': { x: 5, y: 50 },
  '疾厄宫': { x: 15, y: 20 },
}

const palaceColors: Record<string, string> = {
  '命宫': 'bg-red-100 border-red-400 text-red-800',
  '兄弟宫': 'bg-orange-100 border-orange-400 text-orange-800',
  '夫妻宫': 'bg-pink-100 border-pink-400 text-pink-800',
  '子女宫': 'bg-purple-100 border-purple-400 text-purple-800',
  '财帛宫': 'bg-blue-100 border-blue-400 text-blue-800',
  '疾厄宫': 'bg-green-100 border-green-400 text-green-800',
  '迁移宫': 'bg-teal-100 border-teal-400 text-teal-800',
  '奴仆宫': 'bg-cyan-100 border-cyan-400 text-cyan-800',
  '官禄宫': 'bg-indigo-100 border-indigo-400 text-indigo-800',
  '田宅宫': 'bg-violet-100 border-violet-400 text-violet-800',
  '福德宫': 'bg-amber-100 border-amber-400 text-amber-800',
  '父母宫': 'bg-gray-100 border-gray-400 text-gray-800',
}

const relationLines: Record<string, { color: string; dash?: string }> = {
  '相生': { color: 'text-green-500' },
  '相克': { color: 'text-red-500' },
  '相合': { color: 'text-blue-500' },
  '冲': { color: 'text-orange-500', dash: '5,5' },
}

export function PalaceDiagram({ mainPalace, palaces, relations = [], onPalaceClick }: PalaceDiagramProps) {
  const [hoveredPalace, setHoveredPalace] = useState<string | null>(null)

  const getPosition = (palace: string) => {
    return palacePositions[palace] || { x: 50, y: 50 }
  }

  const renderConnections = () => {
    return relations.map((rel, i) => {
      const from = getPosition(rel.from)
      const to = getPosition(rel.to)

      return (
        <line
          key={i}
          x1={`${from.x}%`}
          y1={`${from.y}%`}
          x2={`${to.x}%`}
          y2={`${to.y}%`}
          className={relationLines[rel.type]?.color}
          strokeWidth={rel.strength}
          strokeDasharray={relationLines[rel.type]?.dash}
          opacity={0.6}
        />
      )
    })
  }

  return (
    <div className="w-full">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">宫位关系图</h3>

      <div className="relative w-full aspect-square bg-gradient-to-br from-gray-50 to-gray-100 rounded-xl border border-gray-200 overflow-hidden">
        <svg className="absolute inset-0 w-full h-full">
          {renderConnections()}
        </svg>

        {palaces.map((palace) => {
          const pos = getPosition(palace)
          const isMain = palace === mainPalace
          const isHovered = hoveredPalace === palace
          const colorClass = palaceColors[palace] || 'bg-white border-gray-300'

          return (
            <div
              key={palace}
              className={clsx(
                'absolute transform -translate-x-1/2 -translate-y-1/2 transition-all cursor-pointer',
                isMain && 'z-10',
                isHovered && 'z-20 scale-110'
              )}
              style={{ left: `${pos.x}%`, top: `${pos.y}%` }}
              onMouseEnter={() => setHoveredPalace(palace)}
              onMouseLeave={() => setHoveredPalace(null)}
              onClick={() => onPalaceClick?.(palace)}
            >
              <div
                className={clsx(
                  'px-3 py-2 rounded-lg border-2 text-sm font-medium whitespace-nowrap shadow-sm transition-shadow',
                  colorClass,
                  isMain && 'ring-2 ring-gold-400 ring-offset-1',
                  isHovered && 'shadow-lg'
                )}
              >
                {palace}
                {isMain && <span className="ml-1 text-xs text-gold-600">★</span>}
              </div>

              {isHovered && (
                <div className="absolute top-full left-1/2 transform -translate-x-1/2 mt-2 px-3 py-2 bg-white border border-gray-200 rounded-lg shadow-lg text-xs whitespace-nowrap z-30">
                  <div className="font-medium text-gray-900">{palace}</div>
                  {relations
                    .filter(r => r.from === palace || r.to === palace)
                    .map((rel, i) => (
                      <div key={i} className="text-gray-600 mt-1">
                        {rel.from === palace ? '→' : '←'} {rel.to}: {rel.type}
                      </div>
                    ))}
                </div>
              )}
            </div>
          )
        })}
      </div>

      {relations.length > 0 && (
        <div className="mt-4 flex flex-wrap gap-4 justify-center">
          {Object.entries(relationLines).map(([type, { color }]) => (
            <div key={type} className="flex items-center space-x-2">
              <div className={`w-8 h-0.5 ${color}`} />
              <span className="text-sm text-gray-600">{type}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}
