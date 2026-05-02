import { useState } from 'react'
import { Input } from '@/components/ui/Input'
import { Card } from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'
import type { KnowledgeItem } from '@/types'

const mockKnowledgeItems: KnowledgeItem[] = [
  {
    id: '1',
    term: '紫微星',
    pinyin: 'zǐ wēi xīng',
    category: '主星',
    description: '紫微星是紫微斗数中的帝星，象征尊贵、权力和领导能力。',
    relatedStars: ['天机星', '太阳星'],
  },
  {
    id: '2',
    term: '天机星',
    pinyin: 'tiān jī xīng',
    category: '主星',
    description: '天机星代表智慧、谋略和创新思维。',
    relatedStars: ['紫微星', '太阴星'],
  },
  {
    id: '3',
    term: '太阳星',
    pinyin: 'tài yáng xīng',
    category: '主星',
    description: '太阳星象征光明、正义和事业成就。',
    relatedStars: ['紫微星', '巨门星'],
  },
  {
    id: '4',
    term: '命宫',
    pinyin: 'mìng gōng',
    category: '十二宫',
    description: '命宫是紫微斗数中最重要的宫位，代表一个人的基本性格和命运走向。',
    relatedPalaces: ['兄弟宫', '夫妻宫', '子女宫'],
  },
  {
    id: '5',
    term: '财帛宫',
    pinyin: 'cái bó gōng',
    category: '十二宫',
    description: '财帛宫掌管一个人的财运和理财能力。',
    relatedPalaces: ['命宫', '福德宫'],
  },
  {
    id: '6',
    term: '官禄宫',
    pinyin: 'guān lù gōng',
    category: '十二宫',
    description: '官禄宫代表事业运势和职业发展。',
    relatedPalaces: ['命宫', '迁移宫'],
  },
]

const categories = ['全部', '主星', '辅星', '煞星', '十二宫', '神煞']

export function Knowledge() {
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedCategory, setSelectedCategory] = useState('全部')

  const filteredItems = mockKnowledgeItems.filter((item) => {
    const matchesSearch = item.term.includes(searchTerm) ||
      item.description.includes(searchTerm)
    const matchesCategory = selectedCategory === '全部' ||
      item.category === selectedCategory
    return matchesSearch && matchesCategory
  })

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">命理知识库</h1>
        <p className="text-gray-500 mt-1">探索紫微斗数术语和概念</p>
      </div>

      <Card>
        <div className="flex flex-col md:flex-row space-y-4 md:space-y-0 md:space-x-4">
          <Input
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="搜索术语..."
            className="flex-1"
          />
          <div className="flex space-x-2 overflow-x-auto">
            {categories.map((cat) => (
              <Button
                key={cat}
                variant={selectedCategory === cat ? 'primary' : 'secondary'}
                size="sm"
                onClick={() => setSelectedCategory(cat)}
              >
                {cat}
              </Button>
            ))}
          </div>
        </div>
      </Card>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {filteredItems.map((item) => (
          <Card key={item.id} hover className="cursor-pointer">
            <div className="flex items-start justify-between mb-2">
              <div>
                <h3 className="font-semibold text-gray-900">{item.term}</h3>
                <p className="text-sm text-gray-500">{item.pinyin}</p>
              </div>
              <span className="px-2 py-0.5 bg-primary-100 text-primary-700 rounded text-xs">
                {item.category}
              </span>
            </div>
            <p className="text-sm text-gray-600 mb-3 line-clamp-2">{item.description}</p>
            {(item.relatedStars?.length || item.relatedPalaces?.length) && (
              <div className="flex flex-wrap gap-1">
                {item.relatedStars?.map((star) => (
                  <span key={star} className="px-2 py-0.5 bg-gold-100 text-gold-700 rounded text-xs">
                    {star}
                  </span>
                ))}
                {item.relatedPalaces?.map((palace) => (
                  <span key={palace} className="px-2 py-0.5 bg-green-100 text-green-700 rounded text-xs">
                    {palace}
                  </span>
                ))}
              </div>
            )}
          </Card>
        ))}
      </div>

      {filteredItems.length === 0 && (
        <Card className="text-center py-12">
          <p className="text-gray-500">未找到相关术语</p>
          <Button
            variant="secondary"
            className="mt-4"
            onClick={() => {
              setSearchTerm('')
              setSelectedCategory('全部')
            }}
          >
            清除筛选
          </Button>
        </Card>
      )}
    </div>
  )
}
