import { ReasoningStep } from '@/types'
import clsx from 'clsx'

interface ReasoningFlowProps {
  steps: ReasoningStep[]
  currentStep?: number
  onStepClick?: (step: number) => void
}

export function ReasoningFlow({ steps, currentStep, onStepClick }: ReasoningFlowProps) {
  return (
    <div className="w-full">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">推理流程</h3>

      <div className="relative">
        <div className="absolute left-6 top-0 bottom-0 w-0.5 bg-gradient-to-b from-primary-500 via-gold-500 to-primary-500" />

        <div className="space-y-6">
          {steps.map((step, index) => {
            const isActive = currentStep === index
            const isCompleted = currentStep !== undefined && currentStep > index
            const isPending = currentStep !== undefined && currentStep < index

            return (
              <div
                key={step.step}
                className={clsx(
                  'relative pl-14 transition-all duration-300',
                  isPending && 'opacity-50'
                )}
                onClick={() => onStepClick?.(index)}
              >
                <div
                  className={clsx(
                    'absolute left-3 w-6 h-6 rounded-full flex items-center justify-center text-sm font-bold transition-all',
                    isActive
                      ? 'bg-primary-600 text-white ring-4 ring-primary-100'
                      : isCompleted
                      ? 'bg-green-500 text-white'
                      : 'bg-gray-200 text-gray-600'
                  )}
                >
                  {isCompleted ? '✓' : step.step}
                </div>

                <div
                  className={clsx(
                    'bg-white border-2 rounded-xl p-4 transition-all cursor-pointer hover:shadow-md',
                    isActive
                      ? 'border-primary-300 shadow-md'
                      : isCompleted
                      ? 'border-green-200'
                      : 'border-gray-200'
                  )}
                >
                  <div className="flex items-center justify-between mb-2">
                    <h4 className="font-semibold text-gray-900">{step.title}</h4>
                    <span className="text-xs text-gray-500">步骤 {step.step}</span>
                  </div>

                  <p className="text-sm text-gray-600 mb-3">{step.description}</p>

                  {step.factors.length > 0 && (
                    <div className="mb-3">
                      <div className="text-xs font-medium text-gray-500 mb-1">关键因素</div>
                      <div className="flex flex-wrap gap-1">
                        {step.factors.map((factor, i) => (
                          <span
                            key={i}
                            className={clsx(
                              'px-2 py-0.5 rounded text-xs',
                              isActive ? 'bg-primary-100 text-primary-700' : 'bg-gray-100 text-gray-600'
                            )}
                          >
                            {factor}
                          </span>
                        ))}
                      </div>
                    </div>
                  )}

                  <div className="pt-3 border-t border-gray-100">
                    <div className="text-xs font-medium text-gray-500 mb-1">结论</div>
                    <p className="text-sm text-gray-800 font-medium">{step.conclusion}</p>
                  </div>
                </div>
              </div>
            )
          })}
        </div>
      </div>
    </div>
  )
}
