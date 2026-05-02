from enum import Enum
from typing import Dict, List, Optional


class ErrorType(Enum):
    """错误类型"""
    SOURCE_ERROR = "source_error"
    MISUNDERSTANDING = "misunderstanding"
    PROPAGATION_ERROR = "propagation_error"
    TRANSLATION_ERROR = "translation_error"
    OUT_OF_CONTEXT = "out_of_context"


class ErrorDetector:
    """错误检测器"""

    COMMON_ERRORS = {
        "紫微斗数": [
            "误区：紫微星永远吉利",
            "正解：紫微星需看庙陷及其他星曜配合",
            "来源：《紫微斗数全书》卷一"
        ],
        "八字用神": [
            "误区：用神就是缺什么补什么",
            "正解：用神是平衡八字五行最需要的字",
            "来源：《渊海子平》《穷通宝鉴》"
        ],
        "五行相生": [
            "误区：相生关系越多越好",
            "正解：相生需适度，过犹不及",
            "来源：《滴天髓》"
        ],
        "日主强弱": [
            "误区：日主越旺越好",
            "正解：日主需与命局平衡",
            "来源：《子平真诠》"
        ]
    }

    def detect_common_errors(self, content: str) -> List[Dict]:
        """检测常见错误"""
        detected_errors = []

        for topic, error_info in self.COMMON_ERRORS.items():
            if topic in content:
                for error_pattern in error_info:
                    if error_pattern.startswith("误区："):
                        if error_pattern[3:] in content:
                            detected_errors.append({
                                "error_type": ErrorType.MISUNDERSTANDING,
                                "topic": topic,
                                "error_content": error_pattern[3:],
                                "suggestion": error_info[1],
                                "source": error_info[2]
                            })

        return detected_errors

    def detect_out_of_context(self, quote: str, original: str) -> bool:
        """检测断章取义"""
        if len(quote) > len(original) * 0.8:
            return False

        if "..." not in quote and len(quote) < len(original) * 0.5:
            return True

        return False

    def detect_source_errors(self, source: Dict) -> List[Dict]:
        """检测来源错误"""
        errors = []

        if not source.get("book"):
            errors.append({
                "error_type": ErrorType.SOURCE_ERROR,
                "description": "缺少典籍名称",
                "severity": "high"
            })

        if source.get("dynasty"):
            dynasty = source["dynasty"]
            if dynasty not in ["夏", "商", "周", "春秋", "战国", "秦", "汉", "三国", "晋", "南北朝",
                               "隋", "唐", "五代", "宋", "元", "明", "清", "近代", "现代"]:
                errors.append({
                    "error_type": ErrorType.SOURCE_ERROR,
                    "description": f"朝代 '{dynasty}' 格式不规范",
                    "severity": "medium"
                })

        return errors

    def detect_propagation_errors(self, content: str, trusted_sources: List[str]) -> List[Dict]:
        """检测传播错误"""
        errors = []

        for trusted in trusted_sources:
            if trusted in content:
                if "民间传说" in content or "据说" in content:
                    errors.append({
                        "error_type": ErrorType.PROPAGATION_ERROR,
                        "description": f"引用 '{trusted}' 时混入了未经证实的说法",
                        "severity": "high"
                    })

        return errors

    def detect_translation_errors(self, original: str, translated: str) -> List[Dict]:
        """检测翻译错误"""
        errors = []

        key_terms = ["吉", "凶", "旺", "衰", "生", "克", "制", "化"]
        original_count = sum(1 for term in key_terms if term in original)
        translated_count = sum(1 for term in key_terms if term in translated)

        if original_count > 0 and translated_count == 0:
            errors.append({
                "error_type": ErrorType.TRANSLATION_ERROR,
                "description": "关键术语在翻译后丢失",
                "severity": "high"
            })

        return errors

    def classify_error_severity(self, error: Dict) -> str:
        """分类错误严重程度"""
        severity_markers = {
            "high": ["错误", "谬误", "完全", "绝对"],
            "medium": ["可能", "一般", "通常"],
            "low": ["建议", "参考"]
        }

        content = str(error)

        for level, markers in severity_markers.items():
            if any(marker in content for marker in markers):
                return level

        return "medium"

    def get_correction_suggestion(self, error_type: ErrorType, context: str) -> Optional[str]:
        """获取纠错建议"""
        suggestions = {
            ErrorType.SOURCE_ERROR: "请核实来源信息的准确性",
            ErrorType.MISUNDERSTANDING: "建议参考权威典籍原典",
            ErrorType.PROPAGATION_ERROR: "请追查原始文献",
            ErrorType.TRANSLATION_ERROR: "请核对原文含义",
            ErrorType.OUT_OF_CONTEXT: "请引用完整上下文"
        }

        return suggestions.get(error_type)
