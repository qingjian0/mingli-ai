import React, { useState } from 'react'
import { Star, Check, Heart, ArrowRight } from 'lucide-react'
import { ChartType, SystemRating } from '../types'

interface SystemSelectorProps {
  onSelectSystem: (system: ChartType) => void
  onCompare: (sys1: ChartType, sys2: ChartType) => void
}

const MOCK_RATINGS: SystemRating[] = [
  {
    systemId: 'ziwei',
    systemName: 'Zi Wei Dou Shu',
    systemNameCn: '紫微斗数',
    overallScore: 9.2,
    dimensionScores: {
      theoryCompleteness: 9.5,
      practicalAccuracy: 9.0,
      learningDifficulty: 6.0,
      popularity: 8.5,
      historicalHeritage: 9.5,
      architectureCompleteness: 9.0,
      computationComplexity: 8.0,
      flexibility: 7.5,
      evidenceBased: 8.0
    },
    strengths: ['完善的星曜体系', '清晰的格局系统', '成熟的经验传承'],
    weaknesses: ['学习曲线陡峭', '需要大量记忆'],
    recommendedScenarios: ['一生运势分析', '人际关系', '事业发展'],
    lastUpdated: '2026-05-02'
  },
  {
    systemId: 'bazi',
    systemName: 'Ba Zi',
    systemNameCn: '子平八字',
    overallScore: 9.0,
    dimensionScores: {
      theoryCompleteness: 9.0,
      practicalAccuracy: 9.2,
      learningDifficulty: 7.5,
      popularity: 9.5,
      historicalHeritage: 9.8,
      architectureCompleteness: 8.5,
      computationComplexity: 6.0,
      flexibility: 8.5,
      evidenceBased: 9.0
    },
    strengths: ['系统简洁明了', '应用范围广泛', '实用性极强的五行逻辑'],
    weaknesses: ['需要综合判断'],
    recommendedScenarios: ['命理分析', '运势预测', '健康建议'],
    lastUpdated: '2026-05-02'
  },
  {
    systemId: 'qimen',
    systemName: 'Qi Men Dun Jia',
    systemNameCn: '奇门遁甲',
    overallScore: 8.8,
    dimensionScores: {
      theoryCompleteness: 8.5,
      practicalAccuracy: 8.8,
      learningDifficulty: 4.5,
      popularity: 7.0,
      historicalHeritage: 9.0,
      architectureCompleteness: 9.5,
      computationComplexity: 9.0,
      flexibility: 8.0,
      evidenceBased: 7.5
    },
    strengths: ['时空全息概念', '灵活起局排盘', '运筹帷幄'],
    weaknesses: ['复杂度最高', '需要深厚功底'],
    recommendedScenarios: ['决策辅助', '事件预测', '方位选择'],
    lastUpdated: '2026-05-02'
  }
]

const SystemSelector: React.FC<SystemSelectorProps> = ({
  onSelectSystem,
  onCompare
}) => {
  const [sortBy, setSortBy] = useState<'overall' | 'difficulty' | 'popularity'>('overall')
  const [favorites, setFavorites] = useState<Set<string>>(new Set())
  const [comparing, setComparing] = useState<ChartType[]>([])

  // 排序逻辑
  const sortedRatings = [...MOCK_RATINGS].sort((a, b) => {
    if (sortBy === 'overall') return b.overallScore - a.overallScore
    if (sortBy === 'difficulty') return b.dimensionScores.learningDifficulty - a.dimensionScores.learningDifficulty
    if (sortBy === 'popularity') return b.dimensionScores.popularity - a.dimensionScores.popularity
    return 0
  })

  const toggleFavorite = (systemId: string) => {
    const newFavorites = new Set(favorites)
    if (newFavorites.has(systemId)) newFavorites.delete(systemId)
    else newFavorites.add(systemId)
    setFavorites(newFavorites)
  }

  const toggleCompare = (systemId: ChartType) => {
    if (comparing.includes(systemId)) {
      setComparing(comparing.filter(s => s !== systemId))
    } else if (comparing.length < 2) {
      setComparing([...comparing, systemId])
    }
  }

  const doCompare = () => {
    if (comparing.length === 2) {
      onCompare(comparing[0], comparing[1])
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-7xl mx-auto">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">选择命理系统</h1>
          <p className="text-gray-600">
            基于多维度评分，选择最适合你的命理系统
          </p>
        </div>

        <div className="bg-white rounded-xl shadow-sm p-4 mb-6">
          <div className="flex flex-wrap gap-4 items-center justify-between">
            <div className="flex gap-4">
              <div className="flex items-center gap-2">
                <label className="text-sm text-gray-600">排序:</label>
                <select 
                  value={sortBy}
                  onChange={(e) => setSortBy(e.target.value as any)}
                  className="px-3 py-2 border rounded-lg text-sm"
                >
                  <option value="overall">综合评分</option>
                  <option value="difficulty">简易度</option>
                  <option value="popularity">普及度</option>
                </select>
              </div>
            </div>

            {comparing.length === 2 && (
              <button
                onClick={doCompare}
                className="flex items-center gap-2 px-4 py-2 bg-purple-500 text-white rounded-lg hover:bg-purple-600"
              >
                <ArrowRight size={16} />
                开始对比
              </button>
            )}
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {sortedRatings.map((rating) => {
            const isFavorite = favorites.has(rating.systemId)
            const isComparing = comparing.includes(rating.systemId as ChartType)

            return (
              <div
                key={rating.systemId}
                className={`bg-white rounded-xl p-6 border-2 shadow-sm ${
                  isComparing ? 'border-purple-500 ring-2 ring-purple-200' : 'border-transparent'
                }`}
              >
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <div className="text-xl font-bold text-gray-800 mb-1">
                      {rating.systemNameCn}
                    </div>
                    <div className="text-sm text-gray-500">
                      {rating.systemName}
                    </div>
                  </div>
                  <div className="flex gap-2">
                    <button
                      onClick={() => toggleFavorite(rating.systemId)}
                      className={`p-1 rounded ${
                        isFavorite ? 'text-red-500' : 'text-gray-400'}`}
                    >
                      <Heart size={18} fill={isFavorite ? 'currentColor' : 'none'} />
                    </button>
                    <button
                      onClick={() => toggleCompare(rating.systemId as ChartType)}
                      className={`p-1 rounded ${
                        isComparing ? 'text-purple-500' : 'text-gray-400'}`}
                    >
                      <Check size={18} fill={isComparing ? 'currentColor' : 'none'} />
                    </button>
                  </div>
                </div>

                <div className="mb-4">
                  <div className="flex items-center gap-2 mb-1">
                    <span className="text-3xl font-bold text-blue-600">{rating.overallScore.toFixed(1)}</span>
                    <div className="flex items-center gap-1">
                      {[1, 2, 3, 4, 5].map(i => (
                        <Star key={i} size={12} className="text-yellow-400" fill="currentColor" />
                      ))}
                    </div>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2 mb-2">
                    <div
                      className="bg-gradient-to-r from-blue-500 to-purple-500 h-2 rounded-full"
                      style={{ width: `${(rating.overallScore * 10)}%` }}
                    />
                  </div>
                </div>

                <div className="space-y-2 mb-4 text-sm">
                  <div className="text-gray-600">优势</div>
                  <div className="space-y-1">
                    {rating.strengths.slice(0, 3).map((str, i) => (
                    <div key={i} className="flex items-center gap-2 text-gray-700">
                      <Check size={12} className="text-green-500" />
                      {str}
                    </div>
                  ))}
                  </div>
                </div>

                <div className="flex gap-2">
                  <button
                    onClick={() => onSelectSystem(rating.systemId as ChartType)}
                    className="flex-1 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 text-sm"
                  >
                    选择系统
                  </button>
                </div>
              </div>
            )
          })}
        </div>

        <div className="mt-8 text-center text-gray-500 text-sm">
          <p>选择完成度高的系统优先显示在左侧，红色为收藏，紫色为选中对比</p>
        </div>
      </div>
    </div>
  )
}

export default SystemSelector
