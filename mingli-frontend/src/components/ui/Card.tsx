import { HTMLAttributes, forwardRef } from 'react'
import clsx from 'clsx'

interface CardProps extends HTMLAttributes<HTMLDivElement> {
  variant?: 'default' | 'gradient' | 'bordered'
  hover?: boolean
  padding?: 'none' | 'sm' | 'md' | 'lg'
}

export const Card = forwardRef<HTMLDivElement, CardProps>(
  ({ className, variant = 'default', hover = false, padding = 'md', children, ...props }, ref) => {
    const baseStyles = 'rounded-xl transition-all duration-300'

    const variantStyles = {
      default: 'bg-white border border-gray-100 shadow-sm',
      gradient: 'bg-gradient-to-br from-white to-gray-50 border border-gray-200',
      bordered: 'bg-white border-2 border-gray-200',
    }

    const hoverStyles = hover ? 'hover:shadow-lg hover:-translate-y-0.5 cursor-pointer' : ''

    const paddingStyles = {
      none: '',
      sm: 'p-3',
      md: 'p-4',
      lg: 'p-6',
    }

    return (
      <div
        ref={ref}
        className={clsx(baseStyles, variantStyles[variant], hoverStyles, paddingStyles[padding], className)}
        {...props}
      >
        {children}
      </div>
    )
  }
)

Card.displayName = 'Card'
