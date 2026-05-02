export interface Profile {
  id: string
  name: string
  gender: 'male' | 'female'
  birthDate: string
  birthTime: string
  birthLocation: string
  createdAt: string
  updatedAt: string
}

export interface ProfileFormData {
  name: string
  gender: 'male' | 'female'
  birthDate: string
  birthTime: string
  birthLocation: string
}

export type ChartType = 'ziwei' | 'bazi' | 'qimen' | 'qizheng_siyu' | 'shaozi_yishu' | 'huangji_shu' | 'daliu_ren' | 'meihua_yishu' | 'liuyao' | 'xiaocheng_tu' | 'dayan_shifa' | 'shenyi_shu' | 'dading_shu' | 'cegui_shu' | 'heluo_shu' | 'yuzi_shu' | 'fanwei_shu' | 'suanpan_shu' | 'yelv_shu'

export interface SystemRating {
  systemId: string
  systemName: string
  systemNameCn: string
  overallScore: number
  dimensionScores: {
    theoryCompleteness: number
    practicalAccuracy: number
    learningDifficulty: number
    popularity: number
    historicalHeritage: number
    architectureCompleteness: number
    computationComplexity: number
    flexibility: number
    evidenceBased: number
  }
  strengths: string[]
  weaknesses: string[]
  recommendedScenarios: string[]
  lastUpdated: string
}

export interface SystemSelection {
  selectedSystems: ChartType[]
  favoriteSystems: ChartType[]
  comparisonHistory: {
    system1: ChartType
    system2: ChartType
    comparison: any
  }[]
}

export interface ZiweiStar {
  name: string
  palace: string
  brightness: 'bright' | 'normal' | 'dim'
  attributes: string[]
}

export interface ZiweiPalace {
  name: string
  stars: ZiweiStar[]
  sign: string
  mutable: boolean
}

export interface ZiweiChart {
  profileId: string
  dateRange: string
  mainPalace: string
  palaces: ZiweiPalace[]
}

export interface BaziPillar {
  year: BaziStemBranch
  month: BaziStemBranch
  day: BaziStemBranch
  hour: BaziStemBranch
}

export interface BaziStemBranch {
  stem: string
  branch: string
  element: string
}

export interface BaziChart {
  profileId: string
  pillars: BaziPillar
  dayMaster: string
  fiveElements: Record<string, number>
}

export interface QimenDoor {
  name: string
  nature: string
}

export interface QimenChart {
  profileId: string
  qiMenType: string
  gongWei: string
  men: QimenDoor
  xiu: string[]
  shen: string[]
}

export interface Chart {
  id: string
  profileId: string
  type: ChartType
  data: ZiweiChart | BaziChart | QimenChart
  createdAt: string
}

export interface AnalysisRequest {
  profileId: string
  chartType: ChartType
  query: string
}

export interface AnalysisResult {
  id: string
  profileId: string
  chartType: ChartType
  query: string
  summary: string
  reasoning: ReasoningStep[]
  insights: Insight[]
  recommendations: string[]
  createdAt: string
}

export interface ReasoningStep {
  step: number
  title: string
  description: string
  factors: string[]
  conclusion: string
}

export interface Insight {
  category: string
  title: string
  content: string
  confidence: number
}

export interface KnowledgeItem {
  id: string
  term: string
  pinyin: string
  category: string
  description: string
  relatedStars?: string[]
  relatedPalaces?: string[]
}

export interface TimelineEvent {
  year: string
  age: string
  event: string
  analysis: string
}

export interface ApiResponse<T> {
  success: boolean
  data: T
  message?: string
}

export interface PaginatedResponse<T> {
  items: T[]
  total: number
  page: number
  pageSize: number
}
