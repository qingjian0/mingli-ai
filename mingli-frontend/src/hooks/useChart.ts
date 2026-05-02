import { useState, useCallback } from 'react'
import { chartsApi } from '@/api/charts'
import type { Chart, ChartType, ZiweiChart, BaziChart, QimenChart } from '@/types'

export function useChart(profileId: string, _chartType: ChartType) {
  const [chart, setChart] = useState<Chart | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const generateChart = useCallback(async (type: ChartType) => {
    if (!profileId) {
      setError('请先选择命盘档案')
      return
    }

    setLoading(true)
    setError(null)

    try {
      let data: ZiweiChart | BaziChart | QimenChart

      switch (type) {
        case 'ziwei':
          data = await chartsApi.generateZiwei(profileId)
          break
        case 'bazi':
          data = await chartsApi.generateBazi(profileId)
          break
        case 'qimen':
          data = await chartsApi.generateQimen(profileId)
          break
        default:
          throw new Error('不支持的命盘类型')
      }

      setChart({
        id: `${profileId}-${type}`,
        profileId,
        type,
        data,
        createdAt: new Date().toISOString(),
      })
    } catch (err) {
      setError('生成命盘失败')
    } finally {
      setLoading(false)
    }
  }, [profileId])

  const fetchChart = useCallback(async (type: ChartType) => {
    if (!profileId) return

    setLoading(true)
    setError(null)

    try {
      const data = await chartsApi.getByProfile(profileId, type)
      setChart(data)
    } catch (err) {
      setError('获取命盘失败')
    } finally {
      setLoading(false)
    }
  }, [profileId])

  return {
    chart,
    loading,
    error,
    generateChart,
    fetchChart,
  }
}
