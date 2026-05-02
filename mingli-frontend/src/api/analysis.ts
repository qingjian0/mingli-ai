import apiClient from './client'
import type { AnalysisRequest, AnalysisResult, ApiResponse } from '@/types'

export const analysisApi = {
  create: async (request: AnalysisRequest): Promise<AnalysisResult> => {
    const { data } = await apiClient.post<ApiResponse<AnalysisResult>>('/analysis', request)
    return data.data
  },

  getById: async (id: string): Promise<AnalysisResult> => {
    const { data } = await apiClient.get<ApiResponse<AnalysisResult>>(`/analysis/${id}`)
    return data.data
  },

  getByProfile: async (profileId: string): Promise<AnalysisResult[]> => {
    const { data } = await apiClient.get<ApiResponse<AnalysisResult[]>>(`/analysis/profile/${profileId}`)
    return data.data
  },

  delete: async (id: string): Promise<void> => {
    await apiClient.delete(`/analysis/${id}`)
  },
}
