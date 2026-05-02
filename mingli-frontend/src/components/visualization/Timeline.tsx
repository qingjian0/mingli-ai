import { TimelineEvent } from '@/types'
import clsx from 'clsx'

interface TimelineProps {
  events: TimelineEvent[]
  currentYear?: string
  onEventClick?: (event: TimelineEvent) => void
}

export function Timeline({ events, currentYear, onEventClick }: TimelineProps) {
  return (
    <div className="w-full">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">人生轨迹</h3>

      <div className="relative">
        <div className="absolute left-4 top-0 bottom-0 w-0.5 bg-gradient-to-b from-primary-400 via-gold-400 to-gray-300" />

        <div className="space-y-4">
          {events.map((event, index) => {
            const isActive = currentYear === event.year
            const isPast = currentYear !== undefined && parseInt(event.year) < parseInt(currentYear)

            return (
              <div
                key={index}
                className={clsx(
                  'relative pl-12 transition-all',
                  isPast && 'opacity-60'
                )}
                onClick={() => onEventClick?.(event)}
              >
                <div
                  className={clsx(
                    'absolute left-0 w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold transition-all',
                    isActive
                      ? 'bg-primary-600 text-white ring-4 ring-primary-100'
                      : isPast
                      ? 'bg-green-500 text-white'
                      : 'bg-white border-2 border-gray-300 text-gray-600'
                  )}
                >
                  {isPast ? '✓' : index + 1}
                </div>

                <div
                  className={clsx(
                    'bg-white border rounded-xl p-4 transition-all cursor-pointer hover:shadow-md',
                    isActive
                      ? 'border-primary-300 shadow-md'
                      : 'border-gray-200'
                  )}
                >
                  <div className="flex items-center justify-between mb-2">
                    <div className="flex items-center space-x-3">
                      <span className="text-lg font-bold text-gray-900">{event.year}年</span>
                      <span className="px-2 py-0.5 bg-primary-100 text-primary-700 rounded text-xs">
                        {event.age}岁
                      </span>
                    </div>
                    {isActive && (
                      <span className="px-2 py-0.5 bg-gold-100 text-gold-700 rounded text-xs font-medium">
                        当前
                      </span>
                    )}
                  </div>

                  <h4 className="font-semibold text-gray-800 mb-2">{event.event}</h4>

                  <div className="bg-gray-50 rounded-lg p-3">
                    <div className="text-xs font-medium text-gray-500 mb-1">命理分析</div>
                    <p className="text-sm text-gray-700">{event.analysis}</p>
                  </div>
                </div>
              </div>
            )
          })}
        </div>
      </div>
    </div>
  )
}
