import React from 'react'
import { ChartType, SystemRating } from '../types'
import { ArrowLeft, Trophy, Check, X } from 'lucide-react'

interface SystemComparisonProps {
  system1: SystemRating
  system2: SystemRating
  onBack: () => void
  onSelectSystem: (system: ChartType) => void
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

const ComparisonRow = ({
  label,
  score1,
  score2
}: {
  label: string
  score1: number
  score2: number
}) => {
  const winner = score1 > score2 ? 1 : score2 > score1 ? 2 : 0
  
  return (
    <div className="py-4 border-b border-gray-100">
      <div className="text-sm text-gray-500 mb-2">{label}</div>
      <div className="flex items-center gap-4">
        <div className="flex-1">
          <div className="flex justify-between text-sm mb-1">
            <span className={`font-semibold ${winner === 1 ? 'text-green-600' : ''}`}>
              {winner === 1 && <Trophy className="inline mr-1" size={12} />}
              {score1.toFixed(1)}
            </span>
          </div>
          <div className="h-3 bg-gray-200 rounded-full overflow-hidden">
            <div
              className={`h-full transition-all duration-500 ${
                winner === 1 ? 'bg-green-500' : 'bg-blue-400'
              }`}
              style={{ width: `${(score1 / 10) * 100}%` }}
            />
          </div>
        </div>
        
        <div className="w-20 text-center text-gray-400">VS</div>
        
        <div className="flex-1">
          <div className="flex justify-between text-sm mb-1">
            <span className={`font-semibold ${winner === 2 ? 'text-green-600' : ''}`}>
              {winner === 2 && <Trophy className="inline mr-1" size={12} />}
              {score2.toFixed(1)}
            </span>
          </div>
          <div className="h-3 bg-gray-200 rounded-full overflow-hidden">
            <div
              className={`h-full transition-all duration-500 ${
                winner === 2 ? 'bg-green-500' : 'bg-blue-400'
              }`}
              style={{ width: `${(score2 / 10) * 100}%` }}
            />
          </div>
        </div>
      </div>
    </div>
  )
}

const SystemComparison: React.FC<SystemComparisonProps> = ({
  system1,
  system2,
  onBack,
  onSelectSystem
}) => {
  const overallWinner = system1.overallScore > system2.overallScore ? 1 : 2
  const sys1Wins = Object.entries(system1.dimensionScores).filter(
    ([key, val]) => val > (system2.dimensionScores as any)[key]
  ).length
  const sys2Wins = Object.entries(system1.dimensionScores).filter(
    ([key, val]) => val < (system2.dimensionScores as any)[key]
  ).length
  
  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4">
        <button
          onClick={onBack}
          className="flex items-center gap-2 mb-6 text-gray-600 hover:text-gray-800"
        >
          <ArrowLeft size={20} />
          返回选择
        </button>
        
        <div className="bg-white rounded-2xl shadow-sm overflow-hidden">
          <div className="bg-gradient-to-r from-blue-500 to-purple-600 p-6 text-white">
            <h2 className="text-2xl font-bold mb-4">系统对比</h2>
            <div className="grid grid-cols-3 gap-4">
              <div className={`text-center p-4 rounded-xl bg-white bg-opacity-20 ${
                overallWinner === 1 ? 'ring-2 ring-white' : ''
              }`}>
                <div className="text-sm opacity-80">{system1.systemNameCn}</div>
                <div className="text-3xl font-bold">{system1.overallScore.toFixed(1)}</div>
                <div className="text-sm opacity-80">{sys1Wins} 项领先</div>
              </div>
              <div className="flex items-center justify-center">
                <div className="text-4xl">VS</div>
              </div>
              <div className={`text-center p-4 rounded-xl bg-white bg-opacity-20 ${
                overallWinner === 2 ? 'ring-2 ring-white' : ''
              }`}>
                <div className="text-sm opacity-80">{system2.systemNameCn}</div>
                <div className="text-3xl font-bold">{system2.overallScore.toFixed(1)}</div>
                <div className="text-sm opacity-80">{sys2Wins} 项领先</div>
              </div>
            </div>
          </div>
          
          <div className="p-6">
            <div className="grid grid-cols-2 gap-4 mb-6">
              <div className="text-center p-4 bg-blue-50 rounded-xl">
                <div className="font-semibold text-gray-800 mb-2">
                  {system1.systemNameCn}
                </div>
                <div className="text-sm text-gray-600">
                  {system1.systemName}
                </div>
              </div>
              <div className="text-center p-4 bg-purple-50 rounded-xl">
                <div className="font-semibold text-gray-800 mb-2">
                  {system2.systemNameCn}
                </div>
                <div className="text-sm text-gray-600">
                  {system2.systemName}
                </div>
              </div>
            </div>
            
            <div className="mb-6">
              <ComparisonRow 
                label="综合评分"
                score1={system1.overallScore}
                score2={system2.overallScore}
              />
              {Object.entries(system1.dimensionScores).map(([key, score]) => (
                <ComparisonRow 
                  key={key}
                  label={DIMENSION_NAMES[key] || key}
                  score1={score}
                  score2={(system2.dimensionScores as any)[key]}
                />
              ))}
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
              <div>
                <h3 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
                  <Check size={16} className="text-green-500" />
                  {system1.systemNameCn} 优势
                </h3>
                <div className="space-y-2">
                  {system1.strengths.map((s, i) => (
                    <div key={i} className="flex items-start gap-2 text-sm text-gray-600">
                      <Check size={12} className="text-green-500 flex-shrink-0 mt-1" />
                      {s}
                    </div>
                  ))}
                </div>
              </div>
              <div>
                <h3 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
                  <Check size={16} className="text-green-500" />
                  {system2.systemNameCn} 优势
                </h3>
                <div className="space-y-2">
                  {system2.strengths.map((s, i) => (
                    <div key={i} className="flex items-start gap-2 text-sm text-gray-600">
                      <Check size={12} className="text-green-500 flex-shrink-0 mt-1" />
                      {s}
                    </div>
                  ))}
                </div>
              </div>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
              <div>
                <h3 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
                  <X size={16} className="text-orange-500" />
                  {system1.systemNameCn} 注意
                </h3>
                <div className="space-y-2">
                  {system1.weaknesses.map((s, i) => (
                    <div key={i} className="flex items-start gap-2 text-sm text-gray-600">
                      <X size={12} className="text-orange-500 flex-shrink-0 mt-1" />
                      {s}
                    </div>
                  ))}
                </div>
              </div>
              <div>
                <h3 className="font-semibold text-gray-800 mb-3 flex items-center gap-2">
                  <X size={16} className="text-orange-500" />
                  {system2.systemNameCn} 注意
                </h3>
                <div className="space-y-2">
                  {system2.weaknesses.map((s, i) => (
                    <div key={i} className="flex items-start gap-2 text-sm text-gray-600">
                      <X size={12} className="text-orange-500 flex-shrink-0 mt-1" />
                      {s}
                    </div>
                  ))}
                </div>
              </div>
            </div>
            
            <div className="flex gap-4 pt-4 border-t border-gray-100">
              <button
                onClick={() => onSelectSystem(system1.systemId as ChartType)}
                className="flex-1 py-3 bg-blue-500 text-white rounded-xl font-medium hover:bg-blue-600 transition"
              >
                选择 {system1.systemNameCn}
              </button>
              <button
                onClick={() => onSelectSystem(system2.systemId as ChartType)}
                className="flex-1 py-3 bg-purple-500 text-white rounded-xl font-medium hover:bg-purple-600 transition"
              >
                选择 {system2.systemNameCn}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default SystemComparison
