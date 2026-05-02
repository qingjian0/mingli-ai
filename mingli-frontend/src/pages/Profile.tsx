import { useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { Button } from '@/components/ui/Button'
import { Input } from '@/components/ui/Input'
import { Card } from '@/components/ui/Card'
import { Modal } from '@/components/ui/Modal'
import { useProfile } from '@/hooks/useProfile'

export function Profile() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const isNewProfile = !id || id === 'new'
  const { profile, loading, error, createProfile, updateProfile, deleteProfile } = useProfile(id)

  const [formData, setFormData] = useState({
    name: profile?.name || '',
    gender: profile?.gender || 'male' as 'male' | 'female',
    birthDate: profile?.birthDate || '',
    birthTime: profile?.birthTime || '',
    birthLocation: profile?.birthLocation || '',
  })

  const [showDeleteModal, setShowDeleteModal] = useState(false)
  const [saving, setSaving] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setSaving(true)
    try {
      if (isNewProfile) {
        const newProfile = await createProfile(formData)
        navigate(`/profile/${newProfile.id}`)
      } else {
        await updateProfile(id!, formData)
      }
    } finally {
      setSaving(false)
    }
  }

  const handleDelete = async () => {
    if (id) {
      await deleteProfile(id)
      navigate('/profiles')
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-4 border-primary-500 border-t-transparent mx-auto mb-4"></div>
          <p className="text-gray-500">加载中...</p>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <Card className="text-center py-8">
        <p className="text-red-600">{error}</p>
        <Button className="mt-4" onClick={() => navigate('/profiles')}>
          返回列表
        </Button>
      </Card>
    )
  }

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold text-gray-900">
          {isNewProfile ? '创建命盘档案' : '编辑命盘档案'}
        </h1>
        {!isNewProfile && (
          <Button variant="ghost" onClick={() => setShowDeleteModal(true)}>
            删除档案
          </Button>
        )}
      </div>

      <Card>
        <form onSubmit={handleSubmit} className="space-y-6">
          <Input
            label="姓名"
            value={formData.name}
            onChange={(e) => setFormData({ ...formData, name: e.target.value })}
            placeholder="请输入姓名"
            required
          />

          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">性别</label>
            <div className="flex space-x-4">
              <label className="flex items-center">
                <input
                  type="radio"
                  name="gender"
                  value="male"
                  checked={formData.gender === 'male'}
                  onChange={(e) => setFormData({ ...formData, gender: e.target.value as 'male' })}
                  className="mr-2"
                />
                男
              </label>
              <label className="flex items-center">
                <input
                  type="radio"
                  name="gender"
                  value="female"
                  checked={formData.gender === 'female'}
                  onChange={(e) => setFormData({ ...formData, gender: e.target.value as 'female' })}
                  className="mr-2"
                />
                女
              </label>
            </div>
          </div>

          <Input
            label="出生日期"
            type="date"
            value={formData.birthDate}
            onChange={(e) => setFormData({ ...formData, birthDate: e.target.value })}
            required
          />

          <Input
            label="出生时辰"
            type="time"
            value={formData.birthTime}
            onChange={(e) => setFormData({ ...formData, birthTime: e.target.value })}
            required
          />

          <Input
            label="出生地点"
            value={formData.birthLocation}
            onChange={(e) => setFormData({ ...formData, birthLocation: e.target.value })}
            placeholder="如：北京市朝阳区"
            required
          />

          <div className="flex space-x-4 pt-4">
            <Button type="submit" loading={saving}>
              {isNewProfile ? '创建档案' : '保存修改'}
            </Button>
            <Button type="button" variant="secondary" onClick={() => navigate('/profiles')}>
              取消
            </Button>
          </div>
        </form>
      </Card>

      <Modal
        isOpen={showDeleteModal}
        onClose={() => setShowDeleteModal(false)}
        title="确认删除"
        size="sm"
      >
        <p className="text-gray-600 mb-4">确定要删除这个命盘档案吗？此操作无法撤销。</p>
        <div className="flex justify-end space-x-3">
          <Button variant="secondary" onClick={() => setShowDeleteModal(false)}>
            取消
          </Button>
          <Button variant="ghost" onClick={handleDelete}>
            删除
          </Button>
        </div>
      </Modal>
    </div>
  )
}
