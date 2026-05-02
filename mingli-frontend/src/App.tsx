import React, { useState } from 'react'
import SystemSelector from './components/SystemSelector'
import SystemComparison from './components/SystemComparison'
import { ChartType, SystemRating } from './types'

const MOCK_RATINGS: Record<string, SystemRating> = {
  ziwei: {
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
    strengths: ['理论体系完善', '星曜搭配严谨', '千年历史验证', '专业程度高'],
    weaknesses: ['入门门槛较高', '学习曲线陡峭', '流派差异较大'],
    recommendedScenarios: ['深度命运分析', '职业规划', '长期人生规划', '专业研究'],
    lastUpdated: '2026-05-02'
  },
  bazi: {
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
  qimen: {
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
  meihua_yishu: {
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
    strengths: ['最易入门', '灵活多变', '计算简单', '趣味性强'],
    weaknesses: ['理论深度相对不足', '依赖占卜者感悟'],
    recommendedScenarios: ['日常小事占卜', '初学者快速入门', '趣味学习'],
    lastUpdated: '2026-05-02'
  }
}

type ViewMode = 'selector' | 'comparison' | 'using'

const App: React.FC = () => {
  const [viewMode, setViewMode] = useState<ViewMode>('selector')
  const [selectedSystem, setSelectedSystem] = useState<ChartType | null>(null)
  const [comparingSystems, setComparingSystems] = useState<ChartType[]>([])
  
  const handleSelectSystem = (system: ChartType) => {
    setSelectedSystem(system)
    setViewMode('using')
    console.log('Selected system:', system)
  }
  
  const handleCompare = (sys1: ChartType, sys2: ChartType) => {
    setComparingSystems([sys1, sys2])
    setViewMode('comparison')
  }
  
  const handleBackToSelector = () => {
    setViewMode('selector')
    setComparingSystems([])
  }
  
  const renderUsingSystem = () => (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50 flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-xl p-8 max-w-md w-full text-center">
        <div className="w-20 h-20 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center mx-auto mb-6">
          <div className="text-4xl text-white">✨</div>
        </div>
        <h2 className="text-2xl font-bold text-gray-800 mb-2">
          已选择 {MOCK_RATINGS[selectedSystem!]?.systemNameCn}
        </h2>
        <p className="text-gray-600 mb-6">
          正在加载命盘系统...
        </p>
        <button
          onClick={handleBackToSelector}
          className="px-6 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition"
        >
          返回选择
        </button>
      </div>
    </div>
  )
  
  return (
    <div>
      {viewMode === 'selector' && (
        <SystemSelector
          onSelectSystem={handleSelectSystem}
          onCompare={handleCompare}
        />
      )}
      {viewMode === 'comparison' && (
        <SystemComparison
          system1={MOCK_RATINGS[comparingSystems[0]]}
          system2={MOCK_RATINGS[comparingSystems[1]]}
          onBack={handleBackToSelector}
          onSelectSystem={handleSelectSystem}
        />
      )}
      {viewMode === 'using' && selectedSystem && renderUsingSystem()}
    </div>
  )
}

export default App
