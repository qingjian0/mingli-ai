import { create } from 'zustand'
import type { Profile, AnalysisResult, ChartType } from '@/types'

interface AppState {
  currentProfile: Profile | null
  setCurrentProfile: (profile: Profile | null) => void

  currentAnalysis: AnalysisResult | null
  setCurrentAnalysis: (analysis: AnalysisResult | null) => void

  activeChartType: ChartType
  setActiveChartType: (type: ChartType) => void

  sidebarExpanded: boolean
  toggleSidebar: () => void

  theme: 'light' | 'dark'
  toggleTheme: () => void
}

export const useStore = create<AppState>((set) => ({
  currentProfile: null,
  setCurrentProfile: (profile) => set({ currentProfile: profile }),

  currentAnalysis: null,
  setCurrentAnalysis: (analysis) => set({ currentAnalysis: analysis }),

  activeChartType: 'ziwei',
  setActiveChartType: (type) => set({ activeChartType: type }),

  sidebarExpanded: true,
  toggleSidebar: () => set((state) => ({ sidebarExpanded: !state.sidebarExpanded })),

  theme: 'light',
  toggleTheme: () => set((state) => ({ theme: state.theme === 'light' ? 'dark' : 'light' })),
}))
