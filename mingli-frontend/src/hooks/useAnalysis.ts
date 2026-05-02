import { useState, useCallback } from 'react'
import { analysisApi } from '@/api/analysis'
import type { AnalysisResult, AnalysisRequest } from '@/types'

export function useAnalysis(profileId: string) {
  const [analysis, setAnalysis] = useState<AnalysisResult | null>(null)
  const [analyses, setAnalyses] = useState<AnalysisResult[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const createAnalysis = useCallback(async (request: AnalysisRequest): Promise<AnalysisResult> => {
    setLoading(true)
    setError(null)

    try {
      const result = await analysisApi.create(request)
      setAnalysis(result)
      setAnalyses(prev => [result, ...prev])
      return result
    } catch (err) {
      setError('分析请求失败')
      throw err
    } finally {
      setLoading(false)
    }
  }, [])

  const fetchAnalysis = useCallback(async () => {
    if (!profileId) return

    setLoading(true)
    setError(null)

    try {
      const results = await analysisApi.getByProfile(profileId)
      setAnalyses(results)
      if (results.length > 0) {
        setAnalysis(results[0])
      }
    } catch (err) {
      setError('获取分析历史失败')
    } finally {
      setLoading(false)
    }
  }, [profileId])

  const fetchAnalysisById = useCallback(async (id: string) => {
    setLoading(true)
    setError(null)

    try {
      const result = await analysisApi.getById(id)
      setAnalysis(result)
      return result
    } catch (err) {
      setError('获取分析详情失败')
      throw err
    } finally {
      setLoading(false)
    }
  }, [])

  const deleteAnalysis = useCallback(async (id: string) => {
    setLoading(true)
    setError(null)

    try {
      await analysisApi.delete(id)
      setAnalyses(prev => prev.filter(a => a.id !== id))
      if (analysis?.id === id) {
        setAnalysis(null)
      }
    } catch (err) {
      setError('删除分析失败')
      throw err
    } finally {
      setLoading(false)
    }
  }, [analysis?.id])

  return {
    analysis,
    analyses,
    loading,
    error,
    createAnalysis,
    fetchAnalysis,
    fetchAnalysisById,
    deleteAnalysis,
  }
}
