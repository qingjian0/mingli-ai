from typing import Dict, List, Optional, Any
from datetime import datetime


class ZiweiClassics:
    """紫微斗数古籍库"""

    CLASSICS_METADATA = {
        "紫微斗数全书": {
            "author": "明·徐子平",
            "dynasty": "明代",
            "category": "ziwei",
            "chapters": [
                "卷一·星曜垣局",
                "卷二·星曜庙陷",
                "卷三·命宫诸曜",
                "卷四·身宫诸曜",
                "卷五·大限论",
                "卷六·小限论",
                "卷七·流年论",
                "卷八·命盘格式",
                "卷九·格局论",
                "卷十·杂论"
            ],
            "key_concepts": [
                "十四正曜", "四化星", "六吉六凶", "庙陷利害",
                "格局高低", "命宫身宫", "大限小限", "流年推演"
            ]
        },
        "紫微斗数星曜全书": {
            "author": "清·任铁樵",
            "dynasty": "清代",
            "category": "ziwei",
            "chapters": [
                "星曜总论",
                "甲级星详解",
                "乙级星详解",
                "丙级星详解",
                "丁级星详解",
                "戊级星详解",
                "星曜组合",
                "星曜与宫位"
            ],
            "key_concepts": [
                "星曜等级", "星曜性质", "星曜亮度", "星曜组合",
                "星曜与会照", "星曜同宫", "星曜对照"
            ]
        },
        "斗数宣微": {
            "author": "清·张九仪",
            "dynasty": "清代",
            "category": "ziwei",
            "chapters": [
                "基础论",
                "排盘论",
                "星情论",
                "宫位论",
                "四化论",
                "格局论",
                "实例分析"
            ],
            "key_concepts": [
                "四化飞星", "生年四化", "自化", "飞化",
                "忌星运用", "科权禄破", "紫府同宫"
            ]
        },
        "中州派紫微斗数": {
            "author": "传统中州派",
            "dynasty": "近代",
            "category": "ziwei",
            "chapters": [
                "中州派源流",
                "排盘方法",
                "星曜体系",
                "宫位系统",
                "四化系统",
                "格局分析",
                "实例详解"
            ],
            "key_concepts": [
                "中州派传承", "星曜系统", "四化系统", "宫位系统",
                "命局分析", "运限分析", "流年分析"
            ]
        }
    }

    STAR_INTERPRETATIONS = {
        "紫微星": {
            "nature": "帝王之星",
            "keywords": ["尊贵", "权力", "领导", "傲慢"],
            "attributes": {
                "五行": "土",
                "阴阳": "阳",
                "庙陷": {
                    "庙": ["子", "午", "卯", "酉"],
                    "旺": ["寅", "申"],
                    "得": ["辰", "戌", "丑", "未"],
                    "陷": ["巳", "亥"]
                }
            },
            "personality": "具有领导才能，追求完美，略带孤僻",
            "career": "适合管理、行政、政治、企业"
        },
        "天机星": {
            "nature": "智慧之星",
            "keywords": ["智慧", "机谋", "变动", "善良"],
            "attributes": {
                "五行": "木",
                "阴阳": "阳",
                "庙陷": {
                    "庙": ["寅", "卯", "午", "未", "亥"],
                    "旺": ["子", "丑"],
                    "得": ["巳", "申"],
                    "陷": ["辰", "戌", "酉"]
                }
            },
            "personality": "聪明好动，足智多谋，善于策划",
            "career": "适合策划、智库、学术、教育"
        },
        "太阳星": {
            "nature": "光明之星",
            "keywords": ["光明", "博爱", "热情", "慷慨"],
            "attributes": {
                "五行": "火",
                "阴阳": "阳",
                "庙陷": {
                    "庙": ["卯", "辰", "巳", "午", "未"],
                    "旺": ["子", "丑", "寅"],
                    "得": ["申", "酉"],
                    "陷": ["亥", "戌"]
                }
            },
            "personality": "热情大方，正直无私，乐于助人",
            "career": "适合政治、公共关系、传媒、教育"
        },
        "武曲星": {
            "nature": "财帛之星",
            "keywords": ["刚毅", "果决", "财运", "义气"],
            "attributes": {
                "五行": "金",
                "阴阳": "阳",
                "庙陷": {
                    "庙": ["子", "午", "卯", "酉"],
                    "旺": ["丑", "未", "戌"],
                    "得": ["寅", "申"],
                    "陷": ["辰", "巳", "亥"]
                }
            },
            "personality": "刚强果断，讲求实际，重视财利",
            "career": "适合金融、商业、军警、武职"
        },
        "天同星": {
            "nature": "福禄之星",
            "keywords": ["福气", "温和", "享乐", "依赖"],
            "attributes": {
                "五行": "水",
                "阴阳": "阳",
                "庙陷": {
                    "庙": ["卯", "辰", "巳", "午", "未"],
                    "旺": ["子", "寅", "亥"],
                    "得": ["丑", "申"],
                    "陷": ["酉", "戌"]
                }
            },
            "personality": "温和平易，知足常乐，略带懒散",
            "career": "适合服务业、娱乐业、餐饮"
        },
        "廉贞星": {
            "nature": "次桃花",
            "keywords": ["感情", "血气", "叛逆", "才华"],
            "attributes": {
                "五行": "火",
                "阴阳": "阴",
                "庙陷": {
                    "庙": ["寅", "卯", "午", "未", "申"],
                    "旺": ["子", "丑", "辰"],
                    "得": ["巳", "亥"],
                    "陷": ["酉", "戌"]
                }
            },
            "personality": "感情丰富，聪明多才，略带叛逆",
            "career": "适合艺术、娱乐、服务业"
        }
    }

    PALACE_INTERPRETATIONS = {
        "命宫": {
            "description": "先天命运、本身性格",
            "key_points": [
                "主一生基本运势",
                "体现先天禀赋",
                "影响命主性格特质",
                "决定事业基础"
            ],
            "analysis_method": "以命宫为核心，结合三方四正综合判断"
        },
        "兄弟宫": {
            "description": "兄弟姐妹、人际关系",
            "key_points": [
                "代表兄弟姐妹",
                "反映人际往来",
                "体现合作能力",
                "影响社交圈子"
            ]
        },
        "夫妻宫": {
            "description": "婚姻感情、配偶情况",
            "key_points": [
                "主婚姻状况",
                "反映配偶特质",
                "体现感情模式",
                "影响桃花运势"
            ]
        },
        "子女宫": {
            "description": "子女运势、创作能力",
            "key_points": [
                "代表子女缘分",
                "反映创作能力",
                "体现运动运势",
                "影响桃花性质"
            ]
        },
        "财帛宫": {
            "description": "财运状况、理财能力",
            "key_points": [
                "主一生财运",
                "反映理财方式",
                "体现赚钱能力",
                "影响物质生活"
            ]
        },
        "疾厄宫": {
            "description": "健康状况、意外灾厄",
            "key_points": [
                "主身体健康",
                "反映疾病信息",
                "体现意外运势",
                "影响生命安全"
            ]
        },
        "迁移宫": {
            "description": "外出运势、人际表现",
            "key_points": [
                "主外出发展",
                "反映社交表现",
                "体现旅途运势",
                "影响人际关系"
            ]
        },
        "奴仆宫": {
            "description": "下属晚辈、事业伙伴",
            "key_points": [
                "主下属运势",
                "反映合作关系",
                "体现服务态度",
                "影响事业拓展"
            ]
        },
        "官禄宫": {
            "description": "事业运势、学历地位",
            "key_points": [
                "主事业发展",
                "反映学业状况",
                "体现社会地位",
                "影响工作表现"
            ]
        },
        "田宅宫": {
            "description": "房产家业、不动产",
            "key_points": [
                "主固定资产",
                "反映家庭状况",
                "体现居住环境",
                "影响家业运势"
            ]
        },
        "福德宫": {
            "description": "福气德行、精神享受",
            "key_points": [
                "主福气运势",
                "反映精神享受",
                "体现道德品质",
                "影响生活品质"
            ]
        },
        "父母宫": {
            "description": "父母情况、文化传承",
            "key_points": [
                "主父母缘分",
                "反映学业传承",
                "体现文书运势",
                "影响上司关系"
            ]
        }
    }

    TRANSFORMATION_RULES = {
        "化禄": {
            "nature": "禄库",
            "meaning": "财运、享受、缘分、润滑",
            "keywords": ["财禄", "食禄", "福禄", "缘份"]
        },
        "化权": {
            "nature": "权势",
            "meaning": "权力、威严、变动、固执",
            "keywords": ["权力", "权威", "争夺", "变动"]
        },
        "化科": {
            "nature": "科名",
            "meaning": "科名、名誉、文教、善良",
            "keywords": ["功名", "学业", "名誉", "名声"]
        },
        "化忌": {
            "nature": "忌恨",
            "meaning": "灾厄、执著、困扰、伤害",
            "keywords": ["忌讳", "是非", "困扰", "破败"]
        }
    }

    @classmethod
    def get_classics_list(cls) -> List[Dict[str, Any]]:
        """获取古籍列表"""
        return [
            {
                "title": title,
                "author": info["author"],
                "dynasty": info["dynasty"],
                "category": info["category"],
                "chapters_count": len(info["chapters"]),
                "key_concepts": info["key_concepts"]
            }
            for title, info in cls.CLASSICS_METADATA.items()
        ]

    @classmethod
    def get_classic_detail(cls, title: str) -> Optional[Dict[str, Any]]:
        """获取古籍详情"""
        if title in cls.CLASSICS_METADATA:
            return cls.CLASSICS_METADATA[title]
        return None

    @classmethod
    def get_star_interpretation(cls, star_name: str) -> Optional[Dict[str, Any]]:
        """获取星曜解读"""
        return cls.STAR_INTERPRETATIONS.get(star_name)

    @classmethod
    def get_all_stars(cls) -> List[Dict[str, str]]:
        """获取所有星曜列表"""
        return [
            {"name": name, "nature": info["nature"]}
            for name, info in cls.STAR_INTERPRETATIONS.items()
        ]

    @classmethod
    def get_palace_interpretation(cls, palace_name: str) -> Optional[Dict[str, Any]]:
        """获取宫位解读"""
        return cls.PALACE_INTERPRETATIONS.get(palace_name)

    @classmethod
    def get_all_palaces(cls) -> List[Dict[str, str]]:
        """获取所有宫位列表"""
        return [
            {"name": name, "description": info["description"]}
            for name, info in cls.PALACE_INTERPRETATIONS.items()
        ]

    @classmethod
    def get_transformation(cls, trans_name: str) -> Optional[Dict[str, Any]]:
        """获取四化信息"""
        return cls.TRANSFORMATION_RULES.get(trans_name)

    @classmethod
    def get_all_transformations(cls) -> List[Dict[str, str]]:
        """获取所有四化列表"""
        return [
            {"name": name, "nature": info["nature"], "meaning": info["meaning"]}
            for name, info in cls.TRANSFORMATION_RULES.items()
        ]

    @classmethod
    def analyze_star_combination(cls, stars: List[str]) -> Dict[str, Any]:
        """分析星曜组合"""
        if len(stars) < 2:
            return {"error": "需要至少两个星曜"}

        combinations = {}
        for i, star1 in enumerate(stars):
            for star2 in stars[i+1:]:
                key = f"{star1}-{star2}"
                combinations[key] = {
                    "star1": cls.STAR_INTERPRETATIONS.get(star1, {}),
                    "star2": cls.STAR_INTERPRETATIONS.get(star2, {}),
                    "combination_meaning": f"{star1}与{star2}的组合"
                }

        return {
            "stars": stars,
            "combinations": combinations,
            "analysis": "星曜组合分析结果"
        }
