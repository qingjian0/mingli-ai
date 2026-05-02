import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Button } from '@/components/ui/Button'
import { Card } from '@/components/ui/Card'
import { Modal } from '@/components/ui/Modal'
import { Input } from '@/components/ui/Input'
import { useProfile } from '@/hooks/useProfile'
import type { Profile } from '@/types'

export function ProfileList() {
  const { profiles, loading, error, fetchProfiles, deleteProfile } = useProfile()
  const [deleteModal, setDeleteModal] = useState<Profile | null>(null)
  const [searchTerm, setSearchTerm] = useState('')

  useEffect(() => {
    fetchProfiles()
  }, [])

  const filteredProfiles = profiles.filter((p) =>
    p.name.includes(searchTerm) ||
    p.birthLocation.includes(searchTerm)
  )

  const handleDelete = async () => {
    if (deleteModal) {
      await deleteProfile(deleteModal.id)
      setDeleteModal(null)
    }
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center py-12">
        <div className="animate-spin rounded-full h-12 w-12 border-4 border-primary-500 border-t-transparent"></div>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">命盘档案</h1>
          <p className="text-gray-500 mt-1">管理您的命盘档案</p>
        </div>
        <Link to="/profile/new">
          <Button variant="gold">新建档案</Button>
        </Link>
      </div>

      {error && (
        <Card className="bg-red-50 border-red-200">
          <p className="text-red-600">{error}</p>
        </Card>
      )}

      <Card>
        <Input
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="搜索档案..."
        />
      </Card>

      {filteredProfiles.length === 0 ? (
        <Card className="text-center py-12">
          <p className="text-gray-500 mb-4">暂无命盘档案</p>
          <Link to="/profile/new">
            <Button>创建第一个档案</Button>
          </Link>
        </Card>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {filteredProfiles.map((profile) => (
            <Card key={profile.id} hover>
              <div className="flex items-start justify-between mb-3">
                <div>
                  <h3 className="font-semibold text-gray-900">{profile.name}</h3>
                  <p className="text-sm text-gray-500">
                    {profile.gender === 'male' ? '男' : '女'}
                  </p>
                </div>
                <span className="text-2xl">{profile.gender === 'male' ? '👨' : '👩'}</span>
              </div>

              <div className="space-y-1 text-sm text-gray-600 mb-4">
                <p>出生: {profile.birthDate} {profile.birthTime}</p>
                <p>地点: {profile.birthLocation}</p>
              </div>

              <div className="flex space-x-2">
                <Link to={`/profile/${profile.id}`} className="flex-1">
                  <Button variant="secondary" className="w-full">
                    查看
                  </Button>
                </Link>
                <Link to={`/analysis/${profile.id}`} className="flex-1">
                  <Button className="w-full">分析</Button>
                </Link>
              </div>

              <button
                onClick={(e) => {
                  e.preventDefault()
                  setDeleteModal(profile)
                }}
                className="absolute top-2 right-2 p-1 text-gray-400 hover:text-red-500"
              >
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
              </button>
            </Card>
          ))}
        </div>
      )}

      <Modal
        isOpen={!!deleteModal}
        onClose={() => setDeleteModal(null)}
        title="确认删除"
        size="sm"
      >
        <p className="text-gray-600 mb-4">
          确定要删除 {deleteModal?.name} 的档案吗？此操作无法撤销。
        </p>
        <div className="flex justify-end space-x-3">
          <Button variant="secondary" onClick={() => setDeleteModal(null)}>
            取消
          </Button>
          <Button onClick={handleDelete}>确认删除</Button>
        </div>
      </Modal>
    </div>
  )
}
