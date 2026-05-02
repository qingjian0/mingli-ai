import { Link } from 'react-router-dom'
import { Card } from '@/components/ui/Card'
import { Button } from '@/components/ui/Button'

export function Home() {
  const features = [
    {
      title: '紫微斗数',
      description: '通过星曜分布解读命运走向',
      icon: '⭐',
      color: 'from-gold-400 to-gold-600',
      href: '/chart/ziwei'
    },
    {
      title: '八字命理',
      description: '天干地支演绎人生起伏',
      icon: '㊀',
      color: 'from-blue-400 to-blue-600',
      href: '/chart/bazi'
    },
    {
      title: '奇门遁甲',
      description: '时空阵法指点迷津',
      icon: '☰',
      color: 'from-green-400 to-green-600',
      href: '/chart/qimen'
    }
  ]

  const stats = [
    { label: '命盘档案', value: '1,234', icon: '📋' },
    { label: '分析报告', value: '5,678', icon: '📊' },
    { label: '用户案例', value: '890', icon: '👤' },
  ]

  return (
    <div className="space-y-8">
      <section className="text-center py-12">
        <div className="max-w-3xl mx-auto">
          <div className="text-6xl mb-4">☯</div>
          <h1 className="text-4xl font-serif font-bold text-gradient mb-4">
            明理 AI命理平台
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            融合传统命理智慧与现代人工智能<br />
            为您揭示命运密码，指引人生方向
          </p>
          <div className="flex justify-center space-x-4">
            <Link to="/profile/new">
              <Button variant="gold" size="lg">
                创建命盘档案
              </Button>
            </Link>
            <Link to="/knowledge">
              <Button variant="secondary" size="lg">
                探索知识库
              </Button>
            </Link>
          </div>
        </div>
      </section>

      <section className="grid grid-cols-3 gap-6">
        {stats.map((stat) => (
          <Card key={stat.label} variant="gradient" className="text-center">
            <div className="text-3xl mb-2">{stat.icon}</div>
            <div className="text-2xl font-bold text-gray-900">{stat.value}</div>
            <div className="text-sm text-gray-500">{stat.label}</div>
          </Card>
        ))}
      </section>

      <section>
        <h2 className="text-2xl font-semibold text-gray-900 mb-6">命盘工具</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {features.map((feature) => (
            <Link key={feature.title} to={feature.href}>
              <Card hover className="h-full">
                <div className={`w-16 h-16 rounded-xl bg-gradient-to-br ${feature.color} flex items-center justify-center text-3xl text-white mb-4 shadow-lg`}>
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold text-gray-900 mb-2">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </Card>
            </Link>
          ))}
        </div>
      </section>

      <section className="bg-gradient-to-r from-primary-50 to-gold-50 rounded-2xl p-8">
        <div className="max-w-2xl mx-auto text-center">
          <h2 className="text-2xl font-semibold text-gray-900 mb-4">开始探索您的命运</h2>
          <p className="text-gray-600 mb-6">
            只需几步，即可获得专属的命盘分析报告。<br />
            AI智能推理，为您解读星曜奥秘。
          </p>
          <div className="flex justify-center space-x-4">
            <Link to="/profile/new">
              <Button variant="primary" size="lg">
                立即开始
              </Button>
            </Link>
            <Link to="/profiles">
              <Button variant="secondary" size="lg">
                查看档案
              </Button>
            </Link>
          </div>
        </div>
      </section>
    </div>
  )
}
