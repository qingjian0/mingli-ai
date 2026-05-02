import { BaziChart as BaziChartType } from '@/types'
import clsx from 'clsx'

interface BaziChartProps {
  data: BaziChartType
}

const elementColors: Record<string, string> = {
  '木': 'bg-green-100 text-green-800 border-green-300',
  '火': 'bg-red-100 text-red-800 border-red-300',
  '土': 'bg-yellow-100 text-yellow-800 border-yellow-300',
  '金': 'bg-gray-100 text-gray-800 border-gray-300',
  '水': 'bg-blue-100 text-blue-800 border-blue-300',
}

export function BaziChart({ data }: BaziChartProps) {
  const { pillars, dayMaster, fiveElements } = data

  const renderPillar = (pillar: { stem: string; branch: string; element: string }, label: string) => {
    const stemColor = elementColors[data.pillars.year.stem[0]] || elementColors[pillar.element]
    const branchColor = elementColors[pillar.element]

    return (
      <div className="flex flex-col items-center">
        <div className={clsx(
          'w-16 h-12 flex items-center justify-center border-2 rounded-lg font-bold text-lg',
          stemColor
        )}>
          {pillar.stem}
        </div>
        <div className="my-1 text-gray-400 text-xs">{label}</div>
        <div className={clsx(
          'w-16 h-12 flex items-center justify-center border-2 rounded-lg text-sm',
          branchColor
        )}>
          <span>{pillar.branch}</span>
        </div>
      </div>
    )
  }

  return (
    <div className="w-full">
      <div className="mb-6 flex items-center justify-between">
        <h3 className="text-lg font-semibold text-gray-900">八字命盘</h3>
        <div className="flex items-center space-x-2">
          <span className="text-sm text-gray-500">日主:</span>
          <span className={clsx(
            'px-3 py-1 rounded-full font-semibold text-sm',
            elementColors[dayMaster]
          )}>
            {dayMaster}
          </span>
        </div>
      </div>

      <div className="bg-gradient-to-br from-amber-50 to-orange-50 border-2 border-amber-200 rounded-xl p-6">
        <div className="flex justify-center space-x-4 mb-6">
          {renderPillar(pillars.year, '年柱')}
          {renderPillar(pillars.month, '月柱')}
          {renderPillar(pillars.day, '日柱')}
          {renderPillar(pillars.hour, '时柱')}
        </div>

        <div className="border-t border-amber-200 pt-4">
          <h4 className="text-sm font-medium text-gray-700 mb-3 text-center">五行分布</h4>
          <div className="grid grid-cols-5 gap-2">
            {Object.entries(fiveElements).map(([element, count]) => (
              <div key={element} className="text-center">
                <div className={clsx(
                  'w-12 h-12 mx-auto rounded-full flex items-center justify-center text-xl font-bold border-2',
                  elementColors[element]
                )}>
                  {element}
                </div>
                <div className="text-lg font-semibold text-gray-800 mt-1">{count}</div>
                <div className="text-xs text-gray-500">个</div>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="mt-4 grid grid-cols-2 gap-4 text-sm">
        <div className="bg-white border rounded-lg p-3">
          <div className="text-gray-500 mb-1">天干</div>
          <div className="font-medium text-gray-800">
            {pillars.year.stem} {pillars.month.stem} {pillars.day.stem} {pillars.hour.stem}
          </div>
        </div>
        <div className="bg-white border rounded-lg p-3">
          <div className="text-gray-500 mb-1">地支</div>
          <div className="font-medium text-gray-800">
            {pillars.year.branch} {pillars.month.branch} {pillars.day.branch} {pillars.hour.branch}
          </div>
        </div>
      </div>
    </div>
  )
}
