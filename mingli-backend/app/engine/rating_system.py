"""
命理系统评分模块
基于求是思想的多维度评分系统
"""

from enum import Enum
from typing import Dict, List, Any
from pydantic import BaseModel, Field
from ..engine.base import ChartType


class RatingDimension(str, Enum):
    """评分维度"""
    THEORY_COMPLETENESS = "theory_completeness"  # 理论完善度
    PRACTICAL_ACCURACY = "practical_accuracy"    # 实用准确性
    LEARNING_DIFFICULTY = "learning_difficulty"  # 学习难易度
    POPULARITY = "popularity"                    # 普及程度
    HISTORICAL_HERITAGE = "historical_heritage"  # 历史传承
    ARCHITECTURE_COMPLETENESS = "architecture_completeness"  # 架构完善度
    COMPUTATION_COMPLEXITY = "computation_complexity"  # 计算复杂度
    FLEXIBILITY = "flexibility"                  # 灵活适用性
    EVIDENCE_BASED = "evidence_based"            # 实证支持度


class RatingLevel(str, Enum):
    """评分等级"""
    EXCELLENT = "excellent"    # 优秀 (5星)
    GOOD = "good"              # 良好 (4星)
    MEDIUM = "medium"          # 中等 (3星)
    FAIR = "fair"              # 一般 (2星)
    NEEDS_IMPROVEMENT = "needs_improvement"  # 需改进 (1星)


class SystemRating(BaseModel):
    """命理系统评分"""
    system_id: str
    system_name: str
    system_name_cn: str
    overall_score: float  # 综合评分 0-10
    
    # 各维度评分
    dimension_scores: Dict[RatingDimension, float]  # 各维度 0-10分
    dimension_levels: Dict[RatingDimension, RatingLevel]
    
    # 评分说明
    strengths: List[str]  # 优势
    weaknesses: List[str]  # 不足
    recommended_scenarios: List[str]  # 推荐场景
    
    # 元数据
    last_updated: str
    reference_count: int = 0
    
    def get_level(self, score: float) -> RatingLevel:
        """将分数转换为等级"""
        if score >= 9:
            return RatingLevel.EXCELLENT
        elif score >= 7.5:
            return RatingLevel.GOOD
        elif score >= 5.5:
            return RatingLevel.MEDIUM
        elif score >= 3.5:
            return RatingLevel.FAIR
        else:
            return RatingLevel.NEEDS_IMPROVEMENT


class RatingSystem:
    """命理系统评分系统"""
    
    def __init__(self):
        self.ratings: Dict[ChartType, SystemRating] = {}
        self._init_ratings()
    
    def _init_ratings(self):
        """初始化各系统评分"""
        
        # ==================== 紫微斗数 ====================
        self.ratings[ChartType.ZIWEI] = SystemRating(
            system_id="ziwei",
            system_name="紫微斗数",
            system_name_cn="紫微斗数",
            overall_score=9.2,
            dimension_scores={
                RatingDimension.THEORY_COMPLETENESS: 9.5,
                RatingDimension.PRACTICAL_ACCURACY: 8.8,
                RatingDimension.LEARNING_DIFFICULTY: 7.0,
                RatingDimension.POPULARITY: 9.0,
                RatingDimension.HISTORICAL_HERITAGE: 9.3,
                RatingDimension.ARCHITECTURE_COMPLETENESS: 9.5,
                RatingDimension.COMPUTATION_COMPLEXITY: 7.5,
                RatingDimension.FLEXIBILITY: 8.2,
                RatingDimension.EVIDENCE_BASED: 7.8
            },
            dimension_levels={},
            strengths=[
                "理论体系完善，星曜搭配严谨",
                "经千年历史验证，传承有序",
                "涵盖人生各维度的分析框架",
                "专业化程度高，适合深度研究",
                "钦天监等官方机构采用"
            ],
            weaknesses=[
                "入门门槛较高，学习曲线陡峭",
                "不同流派差异较大",
                "计算过程相对复杂"
            ],
            recommended_scenarios=[
                "深度个人命运分析",
                "职业规划与发展",
                "长期人生规划参考",
                "专业命理研究与实践"
            ],
            last_updated="2026-05-02"
        )
        
        # ==================== 子平八字 ====================
        self.ratings[ChartType.BAZI] = SystemRating(
            system_id="bazi",
            system_name="子平八字",
            system_name_cn="子平八字",
            overall_score=9.0,
            dimension_scores={
                RatingDimension.THEORY_COMPLETENESS: 9.3,
                RatingDimension.PRACTICAL_ACCURACY: 8.5,
                RatingDimension.LEARNING_DIFFICULTY: 7.5,
                RatingDimension.POPULARITY: 9.5,
                RatingDimension.HISTORICAL_HERITAGE: 9.4,
                RatingDimension.ARCHITECTURE_COMPLETENESS: 9.2,
                RatingDimension.COMPUTATION_COMPLEXITY: 6.5,
                RatingDimension.FLEXIBILITY: 8.8,
                RatingDimension.EVIDENCE_BASED: 8.0
            },
            dimension_levels={},
            strengths=[
                "理论体系极其完善，核心逻辑清晰",
                "普及度最高，受众广泛",
                "五行生克理论根基深厚",
                "计算相对简单，易于上手",
                "经典著作丰富，传承完整"
            ],
            weaknesses=[
                "深入研究仍需大量实践",
                "同一命盘可能有不同解读",
                "需要一定的中医、天文知识"
            ],
            recommended_scenarios=[
                "快速命理分析与诊断",
                "五行能量平衡建议",
                "初学者入门学习",
                "日常决策参考"
            ],
            last_updated="2026-05-02"
        )
        
        # ==================== 奇门遁甲 ====================
        self.ratings[ChartType.QIMEN] = SystemRating(
            system_id="qimen",
            system_name="奇门遁甲",
            system_name_cn="奇门遁甲",
            overall_score=8.8,
            dimension_scores={
                RatingDimension.THEORY_COMPLETENESS: 9.0,
                RatingDimension.PRACTICAL_ACCURACY: 8.2,
                RatingDimension.LEARNING_DIFFICULTY: 6.0,
                RatingDimension.POPULARITY: 7.8,
                RatingDimension.HISTORICAL_HERITAGE: 9.1,
                RatingDimension.ARCHITECTURE_COMPLETENESS: 8.9,
                RatingDimension.COMPUTATION_COMPLEXITY: 7.8,
                RatingDimension.FLEXIBILITY: 8.5,
                RatingDimension.EVIDENCE_BASED: 7.5
            },
            dimension_levels={},
            strengths=[
                "时空模型精妙，结合方位与时间",
                "适合具体事件分析",
                "古代兵家与决策智慧",
                "有完整的时间盘局系统",
                "应用场景广泛"
            ],
            weaknesses=[
                "学习难度较大",
                "需要较多实践经验",
                "过于复杂易致迷惑"
            ],
            recommended_scenarios=[
                "重要决策时机选择",
                "方位布局与优化",
                "事件发展预测",
                "商战与竞争分析"
            ],
            last_updated="2026-05-02"
        )
        
        # ==================== 梅花易数 ====================
        self.ratings[ChartType.MEIHUA_YISHU] = SystemRating(
            system_id="meihua_yishu",
            system_name="梅花易数",
            system_name_cn="梅花易数",
            overall_score=8.5,
            dimension_scores={
                RatingDimension.THEORY_COMPLETENESS: 8.0,
                RatingDimension.PRACTICAL_ACCURACY: 8.3,
                RatingDimension.LEARNING_DIFFICULTY: 8.5,
                RatingDimension.POPULARITY: 8.8,
                RatingDimension.HISTORICAL_HERITAGE: 8.2,
                RatingDimension.ARCHITECTURE_COMPLETENESS: 7.8,
                RatingDimension.COMPUTATION_COMPLEXITY: 9.0,
                RatingDimension.FLEXIBILITY: 9.2,
                RatingDimension.EVIDENCE_BASED: 7.2
            },
            dimension_levels={},
            strengths=[
                "最易入门，上手极快",
                "灵活多变，随机而应",
                "计算简单，随时可测",
                "易与现代场景结合",
                "趣味性强，适合大众"
            ],
            weaknesses=[
                "理论深度相对不足",
                "依赖占卜者的感悟",
                "系统化程度较低"
            ],
            recommended_scenarios=[
                "日常小事快速占卜",
                "初学者快速入门",
                "生活灵感启发",
                "趣味学习与交流"
            ],
            last_updated="2026-05-02"
        )
        
        # ==================== 六爻 ====================
        self.ratings[ChartType.LIUYAO] = SystemRating(
            system_id="liuyao",
            system_name="六爻纳甲",
            system_name_cn="六爻纳甲",
            overall_score=8.3,
            dimension_scores={
                RatingDimension.THEORY_COMPLETENESS: 8.5,
                RatingDimension.PRACTICAL_ACCURACY: 8.0,
                RatingDimension.LEARNING_DIFFICULTY: 7.8,
                RatingDimension.POPULARITY: 8.2,
                RatingDimension.HISTORICAL_HERITAGE: 8.8,
                RatingDimension.ARCHITECTURE_COMPLETENESS: 8.3,
                RatingDimension.COMPUTATION_COMPLEXITY: 8.5,
                RatingDimension.FLEXIBILITY: 8.0,
                RatingDimension.EVIDENCE_BASED: 7.0
            },
            dimension_levels={},
            strengths=[
                "与易经结合紧密",
                "有完整的六亲体系",
                "适合具体事件占卜",
                "纳甲法严谨规范",
                "历史上应用广泛"
            ],
            weaknesses=[
                "解卦需要较多经验",
                "信息密度高，不易掌握",
                "不同流派差异明显"
            ],
            recommended_scenarios=[
                "具体事件预测",
                "易经研究与应用",
                "传统占卜实践",
                "深度决策分析"
            ],
            last_updated="2026-05-02"
        )
        
        # ==================== 大六壬 ====================
        self.ratings[ChartType.DALIU_REN] = SystemRating(
            system_id="daliu_ren",
            system_name="大六壬",
            system_name_cn="大六壬",
            overall_score=8.7,
            dimension_scores={
                RatingDimension.THEORY_COMPLETENESS: 8.8,
                RatingDimension.PRACTICAL_ACCURACY: 8.3,
                RatingDimension.LEARNING_DIFFICULTY: 5.5,
                RatingDimension.POPULARITY: 6.5,
                RatingDimension.HISTORICAL_HERITAGE: 8.9,
                RatingDimension.ARCHITECTURE_COMPLETENESS: 8.7,
                RatingDimension.COMPUTATION_COMPLEXITY: 7.0,
                RatingDimension.FLEXIBILITY: 8.2,
                RatingDimension.EVIDENCE_BASED: 7.3
            },
            dimension_levels={},
            strengths=[
                "三式之首，体系完备",
                "天盘地盘系统精妙",
                "四课三传逻辑严谨",
                "古代高层决策工具",
                "时空信息密度极高"
            ],
            weaknesses=[
                "学习难度极大",
                "需要极高专业水平",
                "现代传承相对较少",
                "过于复杂难以普及"
            ],
            recommended_scenarios=[
                "专业命理研究",
                "传统学术探讨",
                "复杂问题分析",
                "资深爱好者深度研究"
            ],
            last_updated="2026-05-02"
        )
        
        # ==================== 邵子易数 ====================
        self.ratings[ChartType.SHAOZI_YISHU] = SystemRating(
            system_id="shaozi_yishu",
            system_name="邵子易数",
            system_name_cn="邵子易数",
            overall_score=7.8,
            dimension_scores={
                RatingDimension.THEORY_COMPLETENESS: 7.5,
                RatingDimension.PRACTICAL_ACCURACY: 7.2,
                RatingDimension.LEARNING_DIFFICULTY: 8.2,
                RatingDimension.POPULARITY: 6.0,
                RatingDimension.HISTORICAL_HERITAGE: 8.5,
                RatingDimension.ARCHITECTURE_COMPLETENESS: 7.3,
                RatingDimension.COMPUTATION_COMPLEXITY: 8.8,
                RatingDimension.FLEXIBILITY: 7.5,
                RatingDimension.EVIDENCE_BASED: 6.5
            },
            dimension_levels={},
            strengths=[
                "邵雍易学思想精髓",
                "数理结合巧妙",
                "传承宋儒理学思想",
                "计算相对简单",
                "哲学价值高"
            ],
            weaknesses=[
                "现代传承较少",
                "实践应用相对有限",
                "需要一定的易理基础"
            ],
            recommended_scenarios=[
                "易理研究",
                "宋明理学探讨",
                "学术研究",
                "文化传承学习"
            ],
            last_updated="2026-05-02"
        )
        
        # ==================== 皇极数 ====================
        self.ratings[ChartType.HUANGJI_SHU] = SystemRating(
            system_id="huangji_shu",
            system_name="皇极数",
            system_name_cn="皇极数",
            overall_score=7.5,
            dimension_scores={
                RatingDimension.THEORY_COMPLETENESS: 7.2,
                RatingDimension.PRACTICAL_ACCURACY: 7.0,
                RatingDimension.LEARNING_DIFFICULTY: 8.5,
                RatingDimension.POPULARITY: 5.5,
                RatingDimension.HISTORICAL_HERITAGE: 8.0,
                RatingDimension.ARCHITECTURE_COMPLETENESS: 7.0,
                RatingDimension.COMPUTATION_COMPLEXITY: 9.0,
                RatingDimension.FLEXIBILITY: 7.2,
                RatingDimension.EVIDENCE_BASED: 6.0
            },
            dimension_levels={},
            strengths=[
                "皇极经世思想",
                "历史与易理结合",
                "大尺度时间观",
                "有独特视角",
                "哲学深度高"
            ],
            weaknesses=[
                "现代应用较少",
                "理论相对晦涩",
                "验证困难"
            ],
            recommended_scenarios=[
                "历史研究",
                "易学哲学探讨",
                "学术研究",
                "特殊领域应用"
            ],
            last_updated="2026-05-02"
        )
        
        # ==================== 小成图 ====================
        self.ratings[ChartType.XIAOCHENG_TU] = SystemRating(
            system_id="xiaocheng_tu",
            system_name="小成图",
            system_name_cn="小成图",
            overall_score=7.2,
            dimension_scores={
                RatingDimension.THEORY_COMPLETENESS: 7.0,
                RatingDimension.PRACTICAL_ACCURACY: 6.8,
                RatingDimension.LEARNING_DIFFICULTY: 8.0,
                RatingDimension.POPULARITY: 5.0,
                RatingDimension.HISTORICAL_HERITAGE: 7.5,
                RatingDimension.ARCHITECTURE_COMPLETENESS: 6.8,
                RatingDimension.COMPUTATION_COMPLEXITY: 8.5,
                RatingDimension.FLEXIBILITY: 7.0,
                RatingDimension.EVIDENCE_BASED: 5.8
            },
            dimension_levels={},
            strengths=[
                "简洁巧妙",
                "小而精的架构",
                "易于理解",
                "有独到之处"
            ],
            weaknesses=[
                "应用较少",
                "资料相对缺乏",
                "需要更多验证"
            ],
            recommended_scenarios=[
                "简易占卜",
                "易学研究补充",
                "特殊需求应用"
            ],
            last_updated="2026-05-02"
        )
        
        # ==================== 大衍筮法 ====================
        self.ratings[ChartType.DAYAN_SHIFA] = SystemRating(
            system_id="dayan_shifa",
            system_name="大衍筮法",
            system_name_cn="大衍筮法",
            overall_score=8.0,
            dimension_scores={
                RatingDimension.THEORY_COMPLETENESS: 9.0,
                RatingDimension.PRACTICAL_ACCURACY: 7.5,
                RatingDimension.LEARNING_DIFFICULTY: 7.8,
                RatingDimension.POPULARITY: 7.0,
                RatingDimension.HISTORICAL_HERITAGE: 9.5,
                RatingDimension.ARCHITECTURE_COMPLETENESS: 8.5,
                RatingDimension.COMPUTATION_COMPLEXITY: 8.0,
                RatingDimension.FLEXIBILITY: 7.5,
                RatingDimension.EVIDENCE_BASED: 7.0
            },
            dimension_levels={},
            strengths=[
                "易经原典传承",
                "最正统的占卜方法",
                "历史最悠久",
                "仪式感强",
                "经典价值高"
            ],
            weaknesses=[
                "过程较繁琐",
                "现代简化版本较多",
                "解卦依赖易理基础"
            ],
            recommended_scenarios=[
                "易经学习",
                "传统占卜",
                "重要事情决策",
                "文化体验"
            ],
            last_updated="2026-05-02"
        )
        
        # ==================== 河洛数 ====================
        self.ratings[ChartType.HELUO_SHU] = SystemRating(
            system_id="heluo_shu",
            system_name="河洛数",
            system_name_cn="河洛数",
            overall_score=7.5,
            dimension_scores={
                RatingDimension.THEORY_COMPLETENESS: 8.5,
                RatingDimension.PRACTICAL_ACCURACY: 6.8,
                RatingDimension.LEARNING_DIFFICULTY: 7.2,
                RatingDimension.POPULARITY: 5.8,
                RatingDimension.HISTORICAL_HERITAGE: 9.0,
                RatingDimension.ARCHITECTURE_COMPLETENESS: 7.8,
                RatingDimension.COMPUTATION_COMPLEXITY: 8.8,
                RatingDimension.FLEXIBILITY: 7.0,
                RatingDimension.EVIDENCE_BASED: 6.0
            },
            dimension_levels={},
            strengths=[
                "河图洛书，中华文明源头",
                "数理思想深刻",
                "哲学价值极高",
                "是众多数术的基础",
                "文化内涵丰富"
            ],
            weaknesses=[
                "直接应用较少",
                "多作为理论基础",
                "需要深厚文化底蕴"
            ],
            recommended_scenarios=[
                "数理研究",
                "文化探讨",
                "学术研究",
                "哲学思考"
            ],
            last_updated="2026-05-02"
        )
        
        # ==================== 其他数术 ====================
        # 神易术、大定数、策轨数、愚子数、范围数、算盘数、耶律数
        other_systems = [
            ("shenyi_shu", "神易术", 6.5),
            ("dading_shu", "大定数", 6.2),
            ("cegui_shu", "策轨数", 6.0),
            ("yuzi_shu", "愚子数", 5.8),
            ("fanwei_shu", "范围数", 6.0),
            ("suanpan_shu", "算盘数", 5.5),
            ("yelv_shu", "耶律数", 5.7)
        ]
        
        for sys_id, sys_name, score in other_systems:
            self.ratings[ChartType(sys_id)] = SystemRating(
                system_id=sys_id,
                system_name=sys_name,
                system_name_cn=sys_name,
                overall_score=score,
                dimension_scores={
                    RatingDimension.THEORY_COMPLETENESS: 6.0,
                    RatingDimension.PRACTICAL_ACCURACY: 5.5,
                    RatingDimension.LEARNING_DIFFICULTY: 7.0,
                    RatingDimension.POPULARITY: 4.0,
                    RatingDimension.HISTORICAL_HERITAGE: 7.0,
                    RatingDimension.ARCHITECTURE_COMPLETENESS: 5.8,
                    RatingDimension.COMPUTATION_COMPLEXITY: 8.0,
                    RatingDimension.FLEXIBILITY: 6.0,
                    RatingDimension.EVIDENCE_BASED: 5.0
                },
                dimension_levels={},
                strengths=["有一定历史传承", "有独特视角"],
                weaknesses=["资料较少", "应用有限", "需要更多验证"],
                recommended_scenarios=["学术研究", "文化探索", "特殊应用"],
                last_updated="2026-05-02"
            )
        
        # 计算等级
        for rating in self.ratings.values():
            for dim, score in rating.dimension_scores.items():
                rating.dimension_levels[dim] = rating.get_level(score)
    
    def get_rating(self, chart_type: ChartType) -> SystemRating:
        """获取单个系统评分"""
        return self.ratings.get(chart_type)
    
    def get_all_ratings(self) -> List[SystemRating]:
        """获取所有系统评分"""
        return list(self.ratings.values())
    
    def get_top_systems(self, n: int = 5) -> List[SystemRating]:
        """获取排名前n的系统"""
        sorted_systems = sorted(
            self.ratings.values(),
            key=lambda x: x.overall_score,
            reverse=True
        )
        return sorted_systems[:n]
    
    def get_systems_by_dimension(
        self, dimension: RatingDimension, n: int = 5
    ) -> List[SystemRating]:
        """按维度获取排序"""
        sorted_systems = sorted(
            self.ratings.values(),
            key=lambda x: x.dimension_scores.get(dimension, 0),
            reverse=True
        )
        return sorted_systems[:n]
    
    def recommend_system(
        self, 
        scenario: str, 
        user_level: str = "beginner"
    ) -> List[SystemRating]:
        """推荐适合的系统"""
        # 根据场景和用户水平推荐
        if user_level == "beginner":
            # 初学者优先推荐易上手的
            filtered = [
                s for s in self.ratings.values()
                if s.dimension_scores[RatingDimension.LEARNING_DIFFICULTY] >= 8.0
            ]
        else:
            filtered = list(self.ratings.values())
        
        return sorted(
            filtered,
            key=lambda x: x.overall_score,
            reverse=True
        )[:5]
    
    def compare_systems(
        self, 
        system1: ChartType, 
        system2: ChartType
    ) -> Dict[str, Any]:
        """对比两个系统"""
        r1 = self.ratings.get(system1)
        r2 = self.ratings.get(system2)
        
        if not r1 or not r2:
            return {"error": "System not found"}
        
        comparison = {
            "system1": r1.system_name,
            "system2": r2.system_name,
            "overall_comparison": {
                "winner": r1.system_name if r1.overall_score > r2.overall_score else r2.system_name,
                "difference": abs(r1.overall_score - r2.overall_score)
            },
            "dimension_comparison": {}
        }
        
        for dim in RatingDimension:
            s1 = r1.dimension_scores.get(dim, 0)
            s2 = r2.dimension_scores.get(dim, 0)
            comparison["dimension_comparison"][dim] = {
                "system1_score": s1,
                "system2_score": s2,
                "winner": r1.system_name if s1 > s2 else r2.system_name if s2 > s1 else "equal"
            }
        
        return comparison


__all__ = [
    "RatingDimension",
    "RatingLevel",
    "SystemRating",
    "RatingSystem"
]
