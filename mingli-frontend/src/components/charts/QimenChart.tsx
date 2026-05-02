import { QimenChart as QimenChartType } from '@/types'
import clsx from 'clsx'

interface QimenChartProps {
  data: QimenChartType
  onGongClick?: (gong: string) => void
}

const gongColors: Record<string, string> = {
  '休': 'bg-blue-50 border-blue-300',
  '生': 'bg-green-50 border-green-300',
  '伤': 'bg-teal-50 border-teal-300',
  '杜': 'bg-emerald-50 border-emerald-300',
  '景': 'bg-red-50 border-red-300',
  '死': 'bg-orange-50 border-orange-300',
  '惊': 'bg-yellow-50 border-yellow-300',
  '开': 'bg-purple-50 border-purple-300',
}

const gongNames: Record<string, string> = {
  '休': '休门',
  '生': '生门',
  '伤': '伤门',
  '杜': '杜门',
  '景': '景门',
  '死': '死门',
  '惊': '惊门',
  '开': '开门',
}

export function QimenChart({ data, onGongClick }: QimenChartProps) {
  const getGongColor = (gong: string) => {
    return gongColors[gong] || 'bg-gray-50 border-gray-200'
  }

  return (
    <div className="w-full">
      <div className="mb-4 flex items-center justify-between">
        <h3 className="text-lg font-semibold text-gray-900">奇门遁甲</h3>
        <div className="flex items-center space-x-4">
          <span className="text-sm text-gray-500">类型: {data.qiMenType}</span>
          <span className="text-sm text-gray-500">宫位: {data.gongWei}</span>
        </div>
      </div>

      <div className="bg-gradient-to-br from-indigo-50 to-purple-50 border-2 border-indigo-200 rounded-xl p-6">
        <div className="grid grid-cols-5 gap-2">
          <div className="col-start-2 flex justify-center">
            <div className={clsx(
              'w-20 h-16 flex flex-col items-center justify-center border-2 rounded-lg cursor-pointer transition-all hover:shadow-md',
              getGongColor('杜')
            )} onClick={() => onGongClick?.('杜')}>
              <span className="text-lg font-bold text-indigo-700">{gongNames['杜']}</span>
              <span className="text-[10px] text-gray-500">东南</span>
            </div>
          </div>
          <div className="flex justify-center">
            <div className={clsx(
              'w-20 h-16 flex flex-col items-center justify-center border-2 rounded-lg cursor-pointer transition-all hover:shadow-md',
              getGongColor('景')
            )} onClick={() => onGongClick?.('景')}>
              <span className="text-lg font-bold text-red-700">{gongNames['景']}</span>
              <span className="text-[10px] text-gray-500">南</span>
            </div>
          </div>
          <div className="flex justify-center">
            <div className={clsx(
              'w-20 h-16 flex flex-col items-center justify-center border-2 rounded-lg cursor-pointer transition-all hover:shadow-md',
              getGongColor('死')
            )} onClick={() => onGongClick?.('死')}>
              <span className="text-lg font-bold text-orange-700">{gongNames['死']}</span>
              <span className="text-[10px] text-gray-500">西南</span>
            </div>
          </div>

          <div className="flex justify-end items-center">
            <div className={clsx(
              'w-20 h-16 flex flex-col items-center justify-center border-2 rounded-lg cursor-pointer transition-all hover:shadow-md',
              getGongColor('伤')
            )} onClick={() => onGongClick?.('伤')}>
              <span className="text-lg font-bold text-teal-700">{gongNames['伤']}</span>
              <span className="text-[10px] text-gray-500">东</span>
            </div>
          </div>
          <div className="flex items-center justify-center">
            <div className="w-24 h-20 bg-gradient-to-br from-indigo-100 to-purple-100 border-2 border-indigo-300 rounded-lg flex flex-col items-center justify-center">
              <span className="text-3xl">☰</span>
              <span className="text-xs text-indigo-700">九宫</span>
            </div>
          </div>
          <div className="flex items-center justify-start">
            <div className={clsx(
              'w-20 h-16 flex flex-col items-center justify-center border-2 rounded-lg cursor-pointer transition-all hover:shadow-md',
              getGongColor('惊')
            )} onClick={() => onGongClick?.('惊')}>
              <span className="text-lg font-bold text-yellow-700">{gongNames['惊']}</span>
              <span className="text-[10px] text-gray-500">西</span>
            </div>
          </div>

          <div className="col-start-2 flex justify-center">
            <div className={clsx(
              'w-20 h-16 flex flex-col items-center justify-center border-2 rounded-lg cursor-pointer transition-all hover:shadow-md',
              getGongColor('生')
            )} onClick={() => onGongClick?.('生')}>
              <span className="text-lg font-bold text-green-700">{gongNames['生']}</span>
              <span className="text-[10px] text-gray-500">东北</span>
            </div>
          </div>
          <div className="flex justify-center">
            <div className={clsx(
              'w-20 h-16 flex flex-col items-center justify-center border-2 rounded-lg cursor-pointer transition-all hover:shadow-md',
              getGongColor('休')
            )} onClick={() => onGongClick?.('休')}>
              <span className="text-lg font-bold text-blue-700">{gongNames['休']}</span>
              <span className="text-[10px] text-gray-500">北</span>
            </div>
          </div>
          <div className="flex justify-center">
            <div className={clsx(
              'w-20 h-16 flex flex-col items-center justify-center border-2 rounded-lg cursor-pointer transition-all hover:shadow-md',
              getGongColor('开')
            )} onClick={() => onGongClick?.('开')}>
              <span className="text-lg font-bold text-purple-700">{gongNames['开']}</span>
              <span className="text-[10px] text-gray-500">西北</span>
            </div>
          </div>
        </div>

        <div className="mt-6 grid grid-cols-2 gap-4">
          <div className="bg-white/60 rounded-lg p-3">
            <div className="text-sm font-medium text-gray-700 mb-2">门</div>
            <div className="flex items-center space-x-2">
              <span className="text-lg">{data.men.name}</span>
              <span className="text-sm text-gray-500">({data.men.nature})</span>
            </div>
          </div>
          <div className="bg-white/60 rounded-lg p-3">
            <div className="text-sm font-medium text-gray-700 mb-2">相关神煞</div>
            <div className="flex flex-wrap gap-1">
              {data.shen.map((s, i) => (
                <span key={i} className="px-2 py-0.5 bg-indigo-100 text-indigo-700 rounded text-xs">
                  {s}
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
