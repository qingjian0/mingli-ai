import apiClient from './client'
import type { Chart, ChartType, ZiweiChart, BaziChart, QimenChart, ApiResponse } from '@/types'

export const chartsApi = {
  getByProfile: async (profileId: string, chartType: ChartType): Promise<Chart> => {
    const { data } = await apiClient.get<ApiResponse<Chart>>(`/charts/${profileId}/${chartType}`)
    return data.data
  },

  generateZiwei: async (profileId: string): Promise<ZiweiChart> => {
    const { data } = await apiClient.post<ApiResponse<ZiweiChart>>(`/charts/${profileId}/ziwei`)
    return data.data
  },

  generateBazi: async (profileId: string): Promise<BaziChart> => {
    const { data } = await apiClient.post<ApiResponse<BaziChart>>(`/charts/${profileId}/bazi`)
    return data.data
  },

  generateQimen: async (profileId: string): Promise<QimenChart> => {
    const { data } = await apiClient.post<ApiResponse<QimenChart>>(`/charts/${profileId}/qimen`)
    return data.data
  },
}
