import { useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import clsx from 'clsx'

interface NavItem {
  name: string
  href: string
  icon: string
  description?: string
}

const mainNav: NavItem[] = [
  { name: '首页', href: '/', icon: '🏠', description: '回到首页' },
  { name: '命盘档案', href: '/profiles', icon: '📋', description: '管理命盘' },
]

const toolsNav: NavItem[] = [
  { name: '知识库', href: '/knowledge', icon: '📚', description: '术语查询' },
]

const chartTypes = [
  { name: '紫微斗数', href: '/chart/ziwei', icon: '⭐', color: 'text-gold-600' },
  { name: '八字命理', href: '/chart/bazi', icon: '㊀', color: 'text-blue-600' },
  { name: '奇门遁甲', href: '/chart/qimen', icon: '☰', color: 'text-green-600' },
]

export function Sidebar() {
  const location = useLocation()
  const [expandedSection, setExpandedSection] = useState<string | null>('tools')

  const toggleSection = (section: string) => {
    setExpandedSection(expandedSection === section ? null : section)
  }

  return (
    <aside className="w-64 bg-white border-r border-gray-100 min-h-screen sticky top-16 hidden lg:block">
      <div className="p-4 space-y-6">
        <div>
          <h3 className="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">
            导航
          </h3>
          <nav className="space-y-1">
            {mainNav.map((item) => {
              const isActive = location.pathname === item.href
              return (
                <Link
                  key={item.name}
                  to={item.href}
                  className={clsx(
                    'flex items-center px-3 py-2 rounded-lg text-sm font-medium transition-colors',
                    isActive
                      ? 'bg-primary-50 text-primary-700'
                      : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
                  )}
                >
                  <span className="mr-3 text-lg">{item.icon}</span>
                  {item.name}
                </Link>
              )
            })}
          </nav>
        </div>

        <div>
          <button
            onClick={() => toggleSection('charts')}
            className="flex items-center justify-between w-full px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2 hover:text-gray-700"
          >
            <span>命盘工具</span>
            <svg
              className={clsx(
                'w-4 h-4 transition-transform',
                expandedSection === 'charts' && 'rotate-180'
              )}
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          {expandedSection === 'charts' && (
            <nav className="space-y-1 pl-2">
              {chartTypes.map((chart) => (
                <Link
                  key={chart.name}
                  to={chart.href}
                  className={clsx(
                    'flex items-center px-3 py-2 rounded-lg text-sm transition-colors',
                    location.pathname.includes(chart.href)
                      ? 'bg-primary-50 text-primary-700'
                      : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
                  )}
                >
                  <span className={clsx('mr-3', chart.color)}>{chart.icon}</span>
                  {chart.name}
                </Link>
              ))}
            </nav>
          )}
        </div>

        <div>
          <h3 className="px-3 text-xs font-semibold text-gray-500 uppercase tracking-wider mb-2">
            工具
          </h3>
          <nav className="space-y-1">
            {toolsNav.map((item) => {
              const isActive = location.pathname === item.href
              return (
                <Link
                  key={item.name}
                  to={item.href}
                  className={clsx(
                    'flex items-center px-3 py-2 rounded-lg text-sm font-medium transition-colors',
                    isActive
                      ? 'bg-primary-50 text-primary-700'
                      : 'text-gray-600 hover:bg-gray-50 hover:text-gray-900'
                  )}
                >
                  <span className="mr-3 text-lg">{item.icon}</span>
                  {item.name}
                </Link>
              )
            })}
          </nav>
        </div>
      </div>
    </aside>
  )
}
