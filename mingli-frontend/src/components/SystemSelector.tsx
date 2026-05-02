import React, { useState, useEffect } from 'react'
import { Star, Check, X, Info, Heart, Compare } from 'lucide-react'
import { ChartType, SystemRating } from '../types'

interface SystemSelectorProps {
  onSelectSystem: (system: ChartType) => void
  onCompare: (sys1: ChartType, sys2: ChartType) => void
}

const SYSTEM_NAMES: Record<ChartType, string> = {
  ziwei: '紫微斗数',
  bazi: '子平八字',
  qimen: '奇门遁甲',
  qizheng_siyu: '七政四余',
  shaozi_yishu: '邵子易数',
  huangji_shu: '皇极数',
  daliu_ren: '大六壬',
  meihua_yishu: '梅花易数',
  liuyao: '六爻',
  xiaocheng_tu: '小成图',
  dayan_shifa: '大衍筮法',
  shenyi_shu: '神易术',
  dading_shu: '大定数',
  cegui_shu: '策轨数',
  heluo_shu: '河洛数',
  yuzi_shu: '愚子数',
  fanwei_shu: '范围数',
  suanpan_shu: '算盘数',
  yelv_shu: '耶律数'
}

const DIMENSION_NAMES: Record<string, string> = {
  theoryCompleteness: '理论完善度',
  practicalAccuracy: '实用准确性',
  learningDifficulty: '学习难易度',
  popularity: '普及程度',
  historicalHeritage: '历史传承',
  architectureCompleteness: '架构完善度',
  computationComplexity: '计算复杂度',
  flexibility: '灵活适用性',
  evidenceBased: '实证支持度'
}

// 模拟评分数据
const MOCK_RATINGS: SystemRating[] = [
  {
    systemId: 'ziwei',
    systemName: '紫微斗数',
    systemNameCn: '紫微斗数',
    overallScore: 9.2,
    dimensionScores: {
      theoryCompleteness: 9.5,
      practicalAccuracy: 8.8,
      learningDifficulty: 7.0,
      popularity: 9.0,
      historicalHeritage: 9.3,
      architectureCompleteness: 9.5,
      computationComplexity: 7.5,
      flexibility: 8.2,
      evidenceBased: 7.8
    },
    strengths: ['理论体系完善', '星曜搭配严谨', '千年历史验证'],
    weaknesses: ['入门门槛高', '学习曲线陡峭'],
    recommendedScenarios: ['深度命运分析', '职业规划', '长期人生规划'],
    lastUpdated: '2026-05-02'
  },
  {
    systemId: 'bazi',
    systemName: '子平八字',
    systemNameCn: '子平八字',
    overallScore: 9.0,
    dimensionScores: {
      theoryCompleteness: 9.3,
      practicalAccuracy: 8.5,
      learningDifficulty: 7.5,
      popularity: 9.5,
      historicalHeritage: 9.4,
      architectureCompleteness: 9.2,
      computationComplexity: 6.5,
      flexibility: 8.8,
      evidenceBased: 8.0
    },
    strengths: ['理论极其完善', '普及度最高', '五行生克理论深厚'],
    weaknesses: ['深入需大量实践', '同一命盘可能有不同解读'],
    recommendedScenarios: ['快速命理分析', '五行能量平衡', '初学者入门'],
    lastUpdated: '2026-05-02'
  },
  {
    systemId: 'qimen',
    systemName: '奇门遁甲',
    systemNameCn: '奇门遁甲',
    overallScore: 8.8,
    dimensionScores: {
      theoryCompleteness: 9.0,
      practicalAccuracy: 8.2,
      learningDifficulty: 6.0,
      popularity: 7.8,
      historicalHeritage: 9.1,
      architectureCompleteness: 8.9,
      computationComplexity: 7.8,
      flexibility: 8.5,
      evidenceBased: 7.5
    },
    strengths: ['时空模型精妙', '适合事件分析', '古代兵家智慧'],
    weaknesses: ['学习难度大', '需要较多实践经验'],
    recommendedScenarios: ['重要决策时机', '方位布局', '事件预测'],
    lastUpdated: '2026-05-02'
  },
  {
    systemId: 'meihua_yishu',
    systemName: '梅花易数',
    systemNameCn: '梅花易数',
    overallScore: 8.5,
    dimensionScores: {
      theoryCompleteness: 8.0,
      practicalAccuracy: 8.3,
      learningDifficulty: 8.5,
      popularity: 8.8,
      historicalHeritage: 8.2,
      architectureCompleteness: 7.8,
      computationComplexity: 9.0,
      flexibility: 9.2,
      evidenceBased: 7.2
    },
    strengths: ['最易入门', '灵活多变', '计算简单'],
    weaknesses: ['理论深度相对不足', '依赖占卜者感悟'],
    recommendedScenarios: ['日常小事占卜', '初学者快速入门', '趣味学习'],
    lastUpdated: '2026-05-02'
  },
  {
    systemId: 'liuyao',
    systemName: '六爻纳甲',
    systemNameCn: '六爻纳甲',
    overallScore: 8.3,
    dimensionScores: {
      theoryCompleteness: 8.5,
      practicalAccuracy: 8.0,
      learningDifficulty: 7.8,
      popularity: 8.2,
      historicalHeritage: 8.8,
      architectureCompleteness: 8.3,
      computationComplexity: 8.5,
      flexibility: 8.0,
      evidenceBased: 7.0
    },
    strengths: ['与易经结合紧密', '完整六亲体系', '适合事件占卜'],
    weaknesses: ['解卦需较多经验', '不同流派差异明显'],
    recommendedScenarios: ['具体事件预测', '易经研究', '传统占卜'],
    lastUpdated: '2026-05-02'
  },
  {
    systemId: 'daliu_ren',
    systemName: '大六壬',
    systemNameCn: '大六壬',
    overallScore: 8.7,
    dimensionScores: {
      theoryCompleteness: 8.8,
      practicalAccuracy: 8.3,
      learningDifficulty: 5.5,
      popularity: 6.5,
      historicalHeritage: 8.9,
      architectureCompleteness: 8.7,
      computationComplexity: 7.0,
      flexibility: 8.2,
      evidenceBased: 7.3
    },
    strengths: ['三式之首', '天盘地盘系统精妙', '古代高层决策工具'],
    weaknesses: ['学习难度极大', '需要极高专业水平', '现代传承少'],
    recommendedScenarios: ['专业命理研究', '传统学术探讨'],
    lastUpdated: '2026-05-02'
  },
  {
    systemId: 'heluo_shu',
    systemName: '河洛数',
    systemNameCn: '河洛数',
    overallScore: 7.5,
    dimensionScores: {
      theoryCompleteness: 8.5,
      practicalAccuracy: 6.8,
      learningDifficulty: 7.2,
      popularity: 5.8,
      historicalHeritage: 9.0,
      architectureCompleteness: 7.8,
      computationComplexity: 8.8,
      flexibility: 7.0,
      evidenceBased: 6.0
    },
    strengths: ['中华文明源头', '数理思想深刻', '哲学价值高'],
    weaknesses: ['直接应用较少', '多作为理论基础'],
    recommendedScenarios: ['数理研究', '文化探讨', '学术研究'],
    lastUpdated: '2026-05-02'
  }
]

const StarRating = ({ score, max = 10 }: { score: number; max?: number }) => {
  const stars = Math.round((score / max) * 5)
  return (
    <div className="flex items-center gap-1">
      {[1, 2, 3, 4, 5].map((i) => (
        <Star
          key={i}
          size={14}
          className={`${i <= stars ? 'text-yellow-400 fill-yellow-400' : 'text-gray-300'}`}
        />
      ))}
      <span className="ml-1 text-sm text-gray-600">{score.toFixed(1)}</span>
    </div>
  )
}

const RatingBar = ({ score, label }: { score: number; label: string }) => {
  const percentage = (score / 10) * 100
  let color = 'bg-red-500'
  if (score >= 8) color = 'bg-green-500'
  else if (score >= 6) color = 'bg-yellow-500'
  else if (score >= 4) color = 'bg-orange-500'
  
  return (
    <div className="mb-2">
      <div className="flex justify-between text-xs text-gray-600 mb-1">
        <span>{label}</span>
        <span>{score.toFixed(1)}</span>
      </div>
      <div className="h-2 bg-gray-200 rounded-full overflow-hidden">
        <div 
          className={`h-full ${color} transition-all duration-500`}
          style={{ width: `${percentage}%` }}
        />
      </div>
    </div>
  )
}

const SystemCard = ({
  rating,
  selected,
  onSelect,
  onToggleFavorite
}: {
  rating: SystemRating
  selected: boolean
  onSelect: () => void
  onToggleFavorite: () => void
}) => {
  return (
    <div 
      className={`border rounded-xl p-4 transition-all cursor-pointer hover:shadow-md ${
        selected ? 'border-blue-500 bg-blue-50' : 'border-gray-200 bg-white'
      }`}
      onClick={onSelect}
    >
      <div className="flex justify-between items-start mb-3">
        <div>
          <h3 className="font-bold text-lg text-gray-800">{rating.systemNameCn}</h3>
          <p className="text-sm text-gray-500">{rating.systemName}</p>
        </div>
        <button 
          onClick={(e) => {
            e.stopPropagation()
            onToggleFavorite()
          }}
          className="p-1 hover:bg-gray-100 rounded"
        >
          <Heart size={18} className="text-gray-400 hover:text-red-500" />
        </button>
      </div>
      
      <div className="flex items-center gap-2 mb-3">
        <div className="text-2xl font-bold text-blue-600">{rating.overallScore.toFixed(1)}</div>
        <StarRating score={rating.overallScore} />
      </div>
      
      <div className="space-y-1 mb-3">
        <RatingBar score={rating.dimensionScores.theoryCompleteness} label="理论" />
        <RatingBar score={rating.dimensionScores.practicalAccuracy} label="实用" />
        <RatingBar score={rating.dimensionScores.learningDifficulty} label="易上手" />
      </div>
      
      <div className="flex gap-2 flex-wrap mb-3">
        {rating.strengths.slice(0, 3).map((s, i) => (
          <span 
            key={i}
            className="text-xs px-2 py-1 bg-green-100 text-green-700 rounded-full"
          >
            {s}
          </span>
        ))}
      </div>
      
      <button 
        className="w-full py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition"
        onClick={(e) => {
          e.stopPropagation()
          onSelect()
        }}
      >
        使用此系统
      </button>
    </div>
  )
}

const SystemDetailModal = ({
  rating,
  onClose,
  onUse
}: {
  rating: SystemRating
  onClose: () => void
  onUse: () => void
}) => {
  if (!rating) return null
  
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto">
        <div className="sticky top-0 bg-white border-b p-4 flex justify-between items-center">
          <div>
            <h2 className="text-xl font-bold text-gray-800">{rating.systemNameCn}</h2>
            <p className="text-sm text-gray-500">综合评分: {rating.overallScore.toFixed(1)}</p>
          </div>
          <button onClick={onClose} className="p-2 hover:bg-gray-100 rounded-full">
            <X size={20} />
          </button>
        </div>
        
        <div className="p-6">
          <div className="grid grid-cols-2 gap-4 mb-6">
            {Object.entries(rating.dimensionScores).map(([key, value]) => (
              <div key={key}>
                <RatingBar score={value} label={DIMENSION_NAMES[key] || key} />
              </div>
            ))}
          </div>
          
          <div className="mb-6">
            <h3 className="font-semibold text-gray-800 mb-2 flex items-center gap-2">
              <Check size={16} className="text-green-500" />
              优势
            </h3>
            <div className="flex flex-wrap gap-2">
              {rating.strengths.map((s, i) => (
                <span key={i} className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm">
                  {s}
                </span>
              ))}
            </div>
          </div>
          
          <div className="mb-6">
            <h3 className="font-semibold text-gray-800 mb-2 flex items-center gap-2">
              <X size={16} className="text-orange-500" />
              不足
            </h3>
            <div className="flex flex-wrap gap-2">
              {rating.weaknesses.map((s, i) => (
                <span key={i} className="px-3 py-1 bg-orange-100 text-orange-700 rounded-full text-sm">
                  {s}
                </span>
              ))}
            </div>
          </div>
          
          <div className="mb-6">
            <h3 className="font-semibold text-gray-800 mb-2 flex items-center gap-2">
              <Info size={16} className="text-blue-500" />
              推荐场景
            </h3>
            <div className="flex flex-wrap gap-2">
              {rating.recommendedScenarios.map((s, i) => (
                <span key={i} className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">
                  {s}
                </span>
              ))}
            </div>
          </div>
          
          <button 
            onClick={onUse}
            className="w-full py-3 bg-blue-500 text-white rounded-xl font-medium hover:bg-blue-600 transition"
          >
            开始使用此系统
          </button>
        </div>
      </div>
    </div>
  )
}

const SystemSelector: React.FC<SystemSelectorProps> = ({
  onSelectSystem,
  onCompare
}) => {
  const [viewMode, setViewMode] = useState<'grid' | 'list'>('grid')
  const [sortBy, setSortBy] = useState<'overall' | 'difficulty' | 'popularity'>('overall')
  const [selectedDetail, setSelectedDetail] = useState<SystemRating | null>(null)
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
                  <option value="difficulty">易上手度</option>
                  <option value="popularity">普及程度</option>
                </select>
              </div>
              
              <div className="flex items-center gap-2">
                <button 
                  onClick={() => setViewMode('grid')}
                  className={`p-2 rounded ${viewMode === 'grid' ? 'bg-blue-100 text-blue-600' : 'text-gray-400'}`}
                >
                  网格
                </button>
                <button 
                  onClick={() => setViewMode('list')}
                  className={`p-2 rounded ${viewMode === 'list' ? 'bg-blue-100 text-blue-600' : 'text-gray-400'}`}
                >
                  列表
                </button>
              </div>
            </div>
            
            {comparing.length > 0 && (
              <button 
                onClick={doCompare}
                disabled={comparing.length < 2}
                className="flex items-center gap-2 px-4 py-2 bg-purple-500 text-white rounded-lg hover:bg-purple-600 disabled:bg-gray-300"
              >
                <Compare size={16} />
                对比 ({comparing.length}/2)
              </button>
            )}
          </div>
        </div>
        
        <div className={`grid gap-6 ${
          viewMode === 'grid' 
            ? 'grid-cols-1 md:grid-cols-2 lg:grid-cols-3'
            : 'grid-cols-1'
        }`}>
          {sortedRatings.map((rating) => (
            <SystemCard
              key={rating.systemId}
              rating={rating}
              selected={comparing.includes(rating.systemId as ChartType)}
              onSelect={() => setSelectedDetail(rating)}
              onToggleFavorite={() => toggleFavorite(rating.systemId)}
            />
          ))}
        </div>
        
        {selectedDetail && (
          <SystemDetailModal
            rating={selectedDetail}
            onClose={() => setSelectedDetail(null)}
            onUse={() => {
              onSelectSystem(selectedDetail.systemId as ChartType)
              setSelectedDetail(null)
            }}
          />
        )}
      </div>
    </div>
  )
}

export default SystemSelector
