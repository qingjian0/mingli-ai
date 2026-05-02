import { useState, useEffect } from 'react'
import { useParams, useSearchParams } from 'react-router-dom'
import { Button } from '@/components/ui/Button'
import { Card } from '@/components/ui/Card'
import { Modal } from '@/components/ui/Modal'
import { ZiweiChart } from '@/components/charts/ZiweiChart'
import { BaziChart } from '@/components/charts/BaziChart'
import { QimenChart } from '@/components/charts/QimenChart'
import { PalaceDiagram } from '@/components/visualization/PalaceDiagram'
import { useChart } from '@/hooks/useChart'
import { useProfile } from '@/hooks/useProfile'
import type { ChartType, ZiweiPalace, ZiweiChart as ZiweiChartType } from '@/types'

export function Chart() {
  const { type, id } = useParams<{ type: ChartType; id: string }>()
  const [searchParams] = useSearchParams()
  const profileId = searchParams.get('profile') || id

  const { profile, loading: profileLoading } = useProfile(profileId)
  const { chart, loading: chartLoading, generateChart, error } = useChart(profileId || '', type || 'ziwei')
  const [selectedPalace, setSelectedPalace] = useState<ZiweiPalace | null>(null)

  useEffect(() => {
    if (profileId && type) {
      generateChart(type)
    }
  }, [profileId, type])

  const handleGenerate = () => {
    if (type) {
      generateChart(type)
    }
  }

  if (profileLoading || chartLoading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-4 border-primary-500 border-t-transparent mx-auto mb-4"></div>
          <p className="text-gray-500">命盘生成中...</p>
        </div>
      </div>
    )
  }

  const renderChart = () => {
    if (!chart) {
      return (
        <Card className="text-center py-12">
          <p className="text-gray-500 mb-4">暂无命盘数据</p>
          <Button onClick={handleGenerate}>生成命盘</Button>
        </Card>
      )
    }

    switch (type) {
      case 'ziwei':
        const ziweiData = chart.data as ZiweiChartType
        return (
          <div className="space-y-6">
            <ZiweiChart
              data={ziweiData}
              onPalaceClick={(palace) => setSelectedPalace(palace)}
            />
            <PalaceDiagram
              mainPalace={ziweiData.mainPalace}
              palaces={ziweiData.palaces.map(p => p.name)}
              onPalaceClick={(palace) => {
                const p = ziweiData.palaces.find(pal => pal.name === palace)
                if (p) setSelectedPalace(p)
              }}
            />
          </div>
        )
      case 'bazi':
        return <BaziChart data={chart.data as any} />
      case 'qimen':
        return <QimenChart data={chart.data as any} />
      default:
        return <Card>不支持的命盘类型</Card>
    }
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">
            {type === 'ziwei' ? '紫微斗数' : type === 'bazi' ? '八字命理' : '奇门遁甲'} 命盘
          </h1>
          {profile && (
            <p className="text-gray-500 mt-1">
              {profile.name} · {profile.birthDate} {profile.birthTime}
            </p>
          )}
        </div>
        <Button onClick={handleGenerate}>重新生成</Button>
      </div>

      {error && (
        <Card className="bg-red-50 border-red-200">
          <p className="text-red-600">{error}</p>
        </Card>
      )}

      {renderChart()}

      <Modal
        isOpen={!!selectedPalace}
        onClose={() => setSelectedPalace(null)}
        title={selectedPalace?.name || ''}
        size="lg"
      >
        {selectedPalace && (
          <div className="space-y-4">
            <div>
              <div className="text-sm text-gray-500 mb-1">宫位</div>
              <div className="font-medium">{selectedPalace.name}</div>
            </div>
            <div>
              <div className="text-sm text-gray-500 mb-1">星曜</div>
              <div className="flex flex-wrap gap-2">
                {selectedPalace.stars.map((star, i) => (
                  <span
                    key={i}
                    className="px-3 py-1 bg-primary-100 text-primary-700 rounded-full text-sm"
                  >
                    {star.name}
                  </span>
                ))}
              </div>
            </div>
            <div>
              <div className="text-sm text-gray-500 mb-1">宫位特点</div>
              <p className="text-gray-700">
                {selectedPalace.sign && `属相: ${selectedPalace.sign}`}
                {selectedPalace.mutable && ' · 变宫'}
              </p>
            </div>
          </div>
        )}
      </Modal>
    </div>
  )
}
