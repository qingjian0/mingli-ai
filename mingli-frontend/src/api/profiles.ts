import apiClient from './client'
import type { Profile, ProfileFormData, ApiResponse, PaginatedResponse } from '@/types'

export const profilesApi = {
  getAll: async (params?: { page?: number; pageSize?: number }): Promise<PaginatedResponse<Profile>> => {
    const { data } = await apiClient.get<PaginatedResponse<Profile>>('/profiles', { params })
    return data
  },

  getById: async (id: string): Promise<Profile> => {
    const { data } = await apiClient.get<ApiResponse<Profile>>(`/profiles/${id}`)
    return data.data
  },

  create: async (profileData: ProfileFormData): Promise<Profile> => {
    const { data } = await apiClient.post<ApiResponse<Profile>>('/profiles', profileData)
    return data.data
  },

  update: async (id: string, profileData: ProfileFormData): Promise<Profile> => {
    const { data } = await apiClient.put<ApiResponse<Profile>>(`/profiles/${id}`, profileData)
    return data.data
  },

  delete: async (id: string): Promise<void> => {
    await apiClient.delete(`/profiles/${id}`)
  },
}
