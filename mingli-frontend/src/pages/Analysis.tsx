import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { Button } from '@/components/ui/Button'
import { Input } from '@/components/ui/Input'
import { Card } from '@/components/ui/Card'
import { ReasoningFlow } from '@/components/visualization/ReasoningFlow'
import { Timeline } from '@/components/visualization/Timeline'
import { useAnalysis } from '@/hooks/useAnalysis'
import { useProfile } from '@/hooks/useProfile'
import type { ChartType } from '@/types'

export function Analysis() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()

  const [query, setQuery] = useState('')
  const [selectedChartType, setSelectedChartType] = useState<ChartType>('ziwei')
  const [isAnalyzing, setIsAnalyzing] = useState(false)

  const { profile, loading: profileLoading } = useProfile(id)
  const {
    analysis,
    loading: analysisLoading,
    error,
    createAnalysis,
    fetchAnalysis
  } = useAnalysis(id || '')

  useEffect(() => {
    if (id) {
      fetchAnalysis()
    }
  }, [id])

  const handleAnalyze = async () => {
    if (!query.trim()) return
    setIsAnalyzing(true)
    try {
      await createAnalysis({
        profileId: id!,
        chartType: selectedChartType,
        query
      })
      setQuery('')
    } finally {
      setIsAnalyzing(false)
    }
  }

  if (!id) {
    return (
      <Card className="text-center py-12">
        <p className="text-gray-500 mb-4">请先选择一个命盘档案</p>
        <Button onClick={() => navigate('/profiles')}>选择档案</Button>
      </Card>
    )
  }

  if (profileLoading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="animate-spin rounded-full h-12 w-12 border-4 border-primary-500 border-t-transparent"></div>
      </div>
    )
  }

  const chartTypes: { value: ChartType; label: string }[] = [
    { value: 'ziwei', label: '紫微斗数' },
    { value: 'bazi', label: '八字命理' },
    { value: 'qimen', label: '奇门遁甲' },
  ]

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">命盘分析</h1>
        {profile && (
          <p className="text-gray-500 mt-1">{profile.name}</p>
        )}
      </div>

      <Card>
        <h3 className="font-semibold text-gray-900 mb-4">发起分析</h3>
        <div className="space-y-4">
          <div className="flex space-x-4">
            {chartTypes.map((ct) => (
              <label key={ct.value} className="flex items-center">
                <input
                  type="radio"
                  name="chartType"
                  value={ct.value}
                  checked={selectedChartType === ct.value}
                  onChange={(e) => setSelectedChartType(e.target.value as ChartType)}
                  className="mr-2"
                />
                {ct.label}
              </label>
            ))}
          </div>
          <div className="flex space-x-4">
            <Input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="请输入您想了解的问题..."
              className="flex-1"
            />
            <Button
              onClick={handleAnalyze}
              loading={isAnalyzing}
              disabled={!query.trim()}
            >
              开始分析
            </Button>
          </div>
        </div>
      </Card>

      {error && (
        <Card className="bg-red-50 border-red-200">
          <p className="text-red-600">{error}</p>
        </Card>
      )}

      {analysisLoading && (
        <Card className="text-center py-12">
          <div className="animate-spin rounded-full h-12 w-12 border-4 border-primary-500 border-t-transparent mx-auto mb-4"></div>
          <p className="text-gray-500">AI分析中，请稍候...</p>
        </Card>
      )}

      {analysis && (
        <div className="space-y-6">
          <Card variant="gradient">
            <h3 className="font-semibold text-gray-900 mb-4">分析摘要</h3>
            <p className="text-gray-700 leading-relaxed">{analysis.summary}</p>
          </Card>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <Card>
              <ReasoningFlow steps={analysis.reasoning} />
            </Card>

            <Card>
              <Timeline
                events={[
                  {
                    year: '2020',
                    age: '25',
                    event: '事业转折',
                    analysis: '官禄宫星曜变动，预示职业发展机遇'
                  },
                  {
                    year: '2023',
                    age: '28',
                    event: '财运提升',
                    analysis: '财帛宫星曜旺盛，财务状况改善'
                  },
                  {
                    year: '2025',
                    age: '30',
                    event: '感情稳定',
                    analysis: '夫妻宫星曜调和，姻缘运势向好'
                  }
                ]}
              />
            </Card>
          </div>

          <div>
            <h3 className="font-semibold text-gray-900 mb-4">核心洞察</h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {analysis.insights.map((insight, i) => (
                <Card key={i}>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm text-gray-500">{insight.category}</span>
                    <span className="text-xs px-2 py-0.5 bg-primary-100 text-primary-700 rounded">
                      {Math.round(insight.confidence * 100)}%
                    </span>
                  </div>
                  <h4 className="font-medium text-gray-900 mb-2">{insight.title}</h4>
                  <p className="text-sm text-gray-600">{insight.content}</p>
                </Card>
              ))}
            </div>
          </div>

          {analysis.recommendations.length > 0 && (
            <Card>
              <h3 className="font-semibold text-gray-900 mb-4">建议</h3>
              <ul className="space-y-2">
                {analysis.recommendations.map((rec, i) => (
                  <li key={i} className="flex items-start">
                    <span className="w-2 h-2 rounded-full bg-primary-500 mt-2 mr-3 flex-shrink-0"></span>
                    <span className="text-gray-700">{rec}</span>
                  </li>
                ))}
              </ul>
            </Card>
          )}
        </div>
      )}
    </div>
  )
}
