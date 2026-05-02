import { ZiweiChart as ZiweiChartType, ZiweiPalace } from '@/types'
import clsx from 'clsx'

interface ZiweiChartProps {
  data: ZiweiChartType
  onPalaceClick?: (palace: ZiweiPalace) => void
}

const palaceOrder = ['命宫', '兄弟宫', '夫妻宫', '子女宫', '财帛宫', '疾厄宫', '迁移宫', '奴仆宫', '官禄宫', '田宅宫', '福德宫', '父母宫']

const palaceColors: Record<string, string> = {
  '命宫': 'bg-red-50 border-red-200',
  '兄弟宫': 'bg-orange-50 border-orange-200',
  '夫妻宫': 'bg-pink-50 border-pink-200',
  '子女宫': 'bg-purple-50 border-purple-200',
  '财帛宫': 'bg-blue-50 border-blue-200',
  '疾厄宫': 'bg-green-50 border-green-200',
  '迁移宫': 'bg-teal-50 border-teal-200',
  '奴仆宫': 'bg-cyan-50 border-cyan-200',
  '官禄宫': 'bg-indigo-50 border-indigo-200',
  '田宅宫': 'bg-violet-50 border-violet-200',
  '福德宫': 'bg-amber-50 border-amber-200',
  '父母宫': 'bg-gray-50 border-gray-200',
}

export function ZiweiChart({ data, onPalaceClick }: ZiweiChartProps) {
  const getPalaceData = (palaceName: string) => {
    return data.palaces.find(p => p.name === palaceName) || {
      name: palaceName,
      stars: [],
      sign: '',
      mutable: false
    }
  }

  const renderPalace = (palaceName: string, _index: number) => {
    const palace = getPalaceData(palaceName)
    const colorClass = palaceColors[palaceName] || 'bg-gray-50 border-gray-200'

    return (
      <div
        key={palaceName}
        className={clsx(
          'relative border rounded-lg p-3 min-h-[140px] cursor-pointer transition-all hover:shadow-md',
          colorClass,
          palaceName === data.mainPalace && 'ring-2 ring-gold-400 ring-offset-2'
        )}
        onClick={() => onPalaceClick?.(palace)}
      >
        <div className="text-xs font-semibold text-gray-700 mb-1 flex items-center justify-between">
          <span>{palaceName}</span>
          {palaceName === data.mainPalace && (
            <span className="text-gold-600 text-[10px] bg-gold-100 px-1 rounded">主</span>
          )}
        </div>
        <div className="text-[10px] text-gray-500 mb-1">{palace.sign}</div>

        <div className="space-y-0.5">
          {palace.stars.slice(0, 5).map((star, i) => (
            <div key={i} className="flex items-center text-[11px]">
              <span className={clsx(
                'w-1.5 h-1.5 rounded-full mr-1.5',
                star.brightness === 'bright' ? 'bg-red-500' :
                star.brightness === 'dim' ? 'bg-gray-400' : 'bg-yellow-500'
              )} />
              <span className="text-gray-700">{star.name}</span>
            </div>
          ))}
          {palace.stars.length > 5 && (
            <div className="text-[10px] text-gray-400 pl-3">+{palace.stars.length - 5}星</div>
          )}
        </div>
      </div>
    )
  }

  return (
    <div className="w-full">
      <div className="mb-4 flex items-center justify-between">
        <h3 className="text-lg font-semibold text-gray-900">紫微斗数命盘</h3>
        <span className="text-sm text-gray-500">{data.dateRange}</span>
      </div>

      <div className="grid grid-cols-4 gap-1">
        {renderPalace(palaceOrder[0], 0)}
        {renderPalace(palaceOrder[1], 1)}
        {renderPalace(palaceOrder[2], 2)}

        <div className="row-span-2 flex items-center justify-center bg-gradient-to-br from-gold-50 to-gold-100 border border-gold-200 rounded-lg">
          <div className="text-center transform -rotate-90 whitespace-nowrap">
            <div className="text-2xl text-gold-600">☽</div>
            <div className="text-xs text-gold-700">明理</div>
          </div>
        </div>

        {renderPalace(palaceOrder[11], 11)}
        {renderPalace(palaceOrder[10], 10)}
        {renderPalace(palaceOrder[9], 9)}

        <div className="col-span-3 row-span-2 flex items-center justify-center bg-gradient-to-br from-gray-100 to-gray-50 border border-gray-200 rounded-lg">
          <div className="text-center">
            <div className="text-4xl text-gray-400 mb-2">☯</div>
            <div className="text-sm text-gray-600">十二宫位</div>
            <div className="text-xs text-gray-400 mt-1">流转不息</div>
          </div>
        </div>

        <div className="col-span-3 grid grid-cols-3 gap-1">
          {renderPalace(palaceOrder[8], 8)}
          {renderPalace(palaceOrder[7], 7)}
          {renderPalace(palaceOrder[6], 6)}
          {renderPalace(palaceOrder[5], 5)}
          {renderPalace(palaceOrder[4], 4)}
          {renderPalace(palaceOrder[3], 3)}
        </div>
      </div>
    </div>
  )
}
