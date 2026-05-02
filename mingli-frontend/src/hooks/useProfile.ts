import { useState, useEffect, useCallback } from 'react'
import { profilesApi } from '@/api/profiles'
import type { Profile, ProfileFormData } from '@/types'

export function useProfile(id?: string) {
  const [profile, setProfile] = useState<Profile | null>(null)
  const [profiles, setProfiles] = useState<Profile[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const fetchProfile = useCallback(async () => {
    if (!id) return
    setLoading(true)
    setError(null)
    try {
      const data = await profilesApi.getById(id)
      setProfile(data)
    } catch (err) {
      setError('获取档案失败')
    } finally {
      setLoading(false)
    }
  }, [id])

  const fetchProfiles = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const response = await profilesApi.getAll()
      setProfiles(response.items)
    } catch (err) {
      setError('获取档案列表失败')
    } finally {
      setLoading(false)
    }
  }, [])

  const createProfile = useCallback(async (data: ProfileFormData): Promise<Profile> => {
    setLoading(true)
    setError(null)
    try {
      const newProfile = await profilesApi.create(data)
      setProfiles(prev => [newProfile, ...prev])
      return newProfile
    } catch (err) {
      setError('创建档案失败')
      throw err
    } finally {
      setLoading(false)
    }
  }, [])

  const updateProfile = useCallback(async (id: string, data: ProfileFormData) => {
    setLoading(true)
    setError(null)
    try {
      const updated = await profilesApi.update(id, data)
      setProfile(updated)
      setProfiles(prev => prev.map(p => p.id === id ? updated : p))
    } catch (err) {
      setError('更新档案失败')
      throw err
    } finally {
      setLoading(false)
    }
  }, [])

  const deleteProfile = useCallback(async (id: string) => {
    setLoading(true)
    setError(null)
    try {
      await profilesApi.delete(id)
      setProfiles(prev => prev.filter(p => p.id !== id))
      if (profile?.id === id) {
        setProfile(null)
      }
    } catch (err) {
      setError('删除档案失败')
      throw err
    } finally {
      setLoading(false)
    }
  }, [profile?.id])

  useEffect(() => {
    if (id) {
      fetchProfile()
    }
  }, [id, fetchProfile])

  return {
    profile,
    profiles,
    loading,
    error,
    fetchProfile,
    fetchProfiles,
    createProfile,
    updateProfile,
    deleteProfile,
  }
}
