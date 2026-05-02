from typing import Dict, List, Optional, Any
from datetime import datetime


class BaziClassics:
    """八字命理古籍库"""

    CLASSICS_METADATA = {
        "渊海子平": {
            "author": "宋·徐子升",
            "dynasty": "宋代",
            "category": "bazi",
            "chapters": [
                "论五行生成",
                "论天干阴阳",
                "论地支阴阳",
                "论十干十二支",
                "论五行生克",
                "论十神之名称",
                "论正官",
                "论偏官",
                "论正财",
                "论偏财",
                "论正印",
                "论偏印",
                "论食神",
                "论伤官",
                "论比肩",
                "论劫财",
                "论格局",
                "论大运",
                "论流年",
                "论命宫"
            ],
            "key_concepts": [
                "五行生克", "十神体系", "格局论命", "大运流年",
                "用神取法", "调候用神", "通关用神", "扶抑用神"
            ]
        },
        "滴天髓": {
            "author": "宋·京图",
            "dynasty": "宋代",
            "category": "bazi",
            "chapters": [
                "天道",
                "地道",
                "人道",
                "知命",
                "理气",
                "配合",
                "天干",
                "地支",
                "干支总论",
                "五行",
                "六亲",
                "女命",
                "小儿",
                "性情",
                "疾病",
                "出身",
                "地位",
                "贫富",
                "寿夭",
                "事业"
            ],
            "key_concepts": [
                "滴天髓原文", "旺衰判断", "用神体系", "命局分析",
                "气势流通", "五行平衡", "寒暖燥湿", "十神心性"
            ]
        },
        "穷通宝鉴": {
            "author": "明·余春台",
            "dynasty": "明代",
            "category": "bazi",
            "chapters": [
                "调候总论",
                "甲木调候",
                "乙木调候",
                "丙火调候",
                "丁火调候",
                "戊土调候",
                "己土调候",
                "庚金调候",
                "辛金调候",
                "壬水调候",
                "癸水调候",
                "五行总论",
                "四季调候"
            ],
            "key_concepts": [
                "调候用神", "寒暖燥湿", "春夏秋冬", "五行喜忌",
                "甲木喜庚", "乙木喜丙", "丙火喜壬", "丁火喜甲"
            ]
        },
        "神峰通考": {
            "author": "明·张楠",
            "dynasty": "明代",
            "category": "bazi",
            "chapters": [
                "定格局",
                "论用神",
                "论病药",
                "论何知章",
                "女命百例",
                "六甲日时断",
                "六乙日时断",
                "六丙日时断",
                "六丁日时断",
                "六戊日时断",
                "六己日时断",
                "六庚日时断",
                "六辛日时断",
                "六壬日时断",
                "六癸日时断"
            ],
            "key_concepts": [
                "病药说", "盖头说", "六甲日时断", "格局专论",
                "用神真假", "秀气", "清气", "浊气"
            ]
        },
        "子平真诠": {
            "author": "清·沈孝瞻",
            "dynasty": "清代",
            "category": "bazi",
            "chapters": [
                "论十干十二支",
                "论阴阳生克",
                "论五行生克",
                "论四时节气",
                "论十干合",
                "论十干配合性情",
                "论干支异同",
                "论五行相克",
                "论天干宜忌",
                "论地支",
                "论三合",
                "论生化",
                "论刑冲会合",
                "论神煞",
                "论格局",
                "论用神",
                "论用神成败救应",
                "论用神变化",
                "论杂气",
                "论墓库",
                "论小运",
                "论大运",
                "论流年"
            ],
            "key_concepts": [
                "格局论命", "用神体系", "相神", "喜神", "忌神",
                "八格", "外格", "用神变化", "格局成败"
            ]
        },
        "三命通会": {
            "author": "明·万民英",
            "dynasty": "明代",
            "category": "bazi",
            "chapters": [
                "论天干",
                "论地支",
                "论五行",
                "论六十甲子",
                "论纳音",
                "论十神",
                "论格局",
                "论大运",
                "论小运",
                "论流年",
                "论神煞",
                "论女命",
                "论小儿",
                "论六亲",
                "论性情",
                "论疾病",
                "论贫富",
                "论贵贱",
                "论寿夭"
            ],
            "key_concepts": [
                "纳音五行", "神煞体系", "六亲论法", "性情论断",
                "贫富贵贱", "寿夭判断", "格局配合", "行运得失"
            ]
        }
    }

    STEM_INTERPRETATIONS = {
        "甲": {
            "nature": "阳木",
            "keywords": ["栋梁", "仁义", "正直", "出头"],
            "personality": "仁慈博爱，刚毅果断，有领导才能",
            "career": "适合领导、管理、建筑、林木业",
            "combinations": {
                "乙": "甲木逢乙，藤萝系甲，可外而内",
                "丙": "甲木逢丙，阳光暖照，秀气发越",
                "丁": "甲木逢丁，丁火柔中，暗烛光辉"
            }
        },
        "乙": {
            "nature": "阴木",
            "keywords": ["花草", "柔顺", "敏感", "婉转"],
            "personality": "温柔婉顺，敏感细腻，善于变通",
            "career": "适合艺术、教育、服务、柔性行业",
            "combinations": {
                "甲": "乙木逢甲，枝多根多，曲折有情",
                "丙": "乙木逢丙，艳丽大方，秀气流通",
                "丁": "乙木逢丁，艺文之星，才华出众"
            }
        },
        "丙": {
            "nature": "阳火",
            "keywords": ["太阳", "热情", "光明", "礼让"],
            "personality": "热情豪爽，正直明快，有同理心",
            "career": "适合政治、传媒、教育、表演",
            "combinations": {
                "丁": "丙火逢丁，星光闪烁，秀气文章",
                "戊": "丙火逢戊，厚重持重，光明磊落"
            }
        },
        "丁": {
            "nature": "阴火",
            "keywords": ["灯烛", "文明", "细腻", "神秘"],
            "personality": "内敛细腻，聪明敏锐，有艺术气质",
            "career": "适合艺术、文化、宗教、学术",
            "combinations": {
                "丙": "丁火逢丙，星光灿烂，文明之象",
                "戊": "丁火逢戊，灯烛照夜，暗中发光"
            }
        },
        "戊": {
            "nature": "阳土",
            "keywords": ["高山", "稳重", "诚信", "包容"],
            "personality": "稳重厚道，诚实守信，有责任心",
            "career": "适合农业、建筑、房地产、仓储",
            "combinations": {
                "己": "戊土逢己，田园湿润，养育万物"
            }
        },
        "己": {
            "nature": "阴土",
            "keywords": ["田园", "柔顺", "细腻", "务实"],
            "personality": "温柔细腻，脚踏实地，善于规划",
            "career": "适合财务、设计、农业、服务",
            "combinations": {
                "戊": "己土逢戊，厚重有力，可成大器"
            }
        },
        "庚": {
            "nature": "阳金",
            "keywords": ["刀剑", "刚强", "义气", "决断"],
            "personality": "刚强果决，义气豪爽，善于交际",
            "career": "适合金融、法律、军警、金属加工",
            "combinations": {
                "辛": "庚金逢辛，器具精美，工艺之象"
            }
        },
        "辛": {
            "nature": "阴金",
            "keywords": ["珠玉", "细腻", "精致", "柔韧"],
            "personality": "精致细腻，敏感自尊，善于表达",
            "career": "适合艺术、设计、珠宝、金融",
            "combinations": {
                "庚": "辛金逢庚，金属光泽，锐利无比"
            }
        },
        "壬": {
            "nature": "阳水",
            "keywords": ["江河", "智慧", "流动", "变通"],
            "personality": "聪明智慧，灵活变通，善于交际",
            "career": "适合贸易、物流、水利、流动行业",
            "combinations": {
                "癸": "壬水逢癸，雨露滋润，智慧流通"
            }
        },
        "癸": {
            "nature": "阴水",
            "keywords": ["雨露", "柔情", "机智", "内敛"],
            "personality": "柔情内敛，聪明机智，有韧性",
            "career": "适合学术、策划、宗教、服务",
            "combinations": {
                "壬": "癸水逢壬，水势浩荡，智慧如海"
            }
        }
    }

    BRANCH_INTERPRETATIONS = {
        "子": {
            "nature": "阳水",
            "keywords": ["墨池", "智谋", "流动", "变化"],
            "animal": "鼠",
            "season": "冬季"
        },
        "丑": {
            "nature": "阴土",
            "keywords": ["柳岸", "蓄藏", "忍耐", "务实"],
            "animal": "牛",
            "season": "冬季"
        },
        "寅": {
            "nature": "阳木",
            "keywords": ["广谷", "生发", "仁义", "希望"],
            "animal": "虎",
            "season": "春季"
        },
        "卯": {
            "nature": "阴木",
            "keywords": ["琼枝", "柔弱", "细腻", "艺术"],
            "animal": "兔",
            "season": "春季"
        },
        "辰": {
            "nature": "阳土",
            "keywords": ["草泽", "蕴藏", "包容", "变动"],
            "animal": "龙",
            "season": "春季"
        },
        "巳": {
            "nature": "阴火",
            "keywords": ["大驿", "文明", "变化", "礼仪"],
            "animal": "蛇",
            "season": "夏季"
        },
        "午": {
            "nature": "阳火",
            "keywords": ["烽堠", "热烈", "豪爽", "冲动"],
            "animal": "马",
            "season": "夏季"
        },
        "未": {
            "nature": "阴土",
            "keywords": ["花园", "温润", "养育", "礼仪"],
            "animal": "羊",
            "season": "夏季"
        },
        "申": {
            "nature": "阳金",
            "keywords": ["名都", "刚健", "决断", "义气"],
            "animal": "猴",
            "season": "秋季"
        },
        "酉": {
            "nature": "阴金",
            "keywords": ["寺钟", "细腻", "精致", "审美"],
            "animal": "鸡",
            "season": "秋季"
        },
        "戌": {
            "nature": "阳土",
            "keywords": ["原野", "厚重", "忠诚", "积蓄"],
            "animal": "狗",
            "season": "秋季"
        },
        "亥": {
            "nature": "阴水",
            "keywords": ["悬河", "智慧", "变动", "流动"],
            "animal": "猪",
            "season": "冬季"
        }
    }

    TEN_GODS = {
        "比肩": {
            "nature": "同我者",
            "keywords": ["自立", "刚健", "竞争", "合作"],
            "meaning": "代表兄弟姐妹、同事、朋友、合作伙伴"
        },
        "劫财": {
            "nature": "助我者",
            "keywords": ["义气", "争夺", "损耗", "投机"],
            "meaning": "代表异性兄弟姐妹、竞争者、合伙人"
        },
        "食神": {
            "nature": "泄我者",
            "keywords": ["福气", "才华", "表达", "寿元"],
            "meaning": "代表福气、才华、表达、子女"
        },
        "伤官": {
            "nature": "泄我者",
            "keywords": ["才华", "叛逆", "创新", "是非"],
            "meaning": "代表才华、创意、叛逆、口舌"
        },
        "正财": {
            "nature": "克我者",
            "keywords": ["正当", "稳定", "理财", "勤俭"],
            "meaning": "代表正当收入、财产、妻子（男命）"
        },
        "偏财": {
            "nature": "克我者",
            "keywords": ["流动", "投机", "慷慨", "风流"],
            "meaning": "代表流动资产、意外之财、父亲"
        },
        "正印": {
            "nature": "生我者",
            "keywords": ["权贵", "学业", "慈悲", "名誉"],
            "meaning": "代表权贵、学业、母亲、房产"
        },
        "偏印": {
            "nature": "生我者",
            "keywords": ["权谋", "领悟", "孤独", "偏业"],
            "meaning": "代表偏门、领悟、继母、偏业"
        },
        "正官": {
            "nature": "克我者",
            "keywords": ["规矩", "责任", "地位", "压力"],
            "meaning": "代表规矩、地位、压力、丈夫（女命）"
        },
        "七杀": {
            "nature": "克我者",
            "keywords": ["压力", "刚强", "权威", "灾祸"],
            "meaning": "代表压力、权威、挑战、灾祸"
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
        return cls.CLASSICS_METADATA.get(title)

    @classmethod
    def get_stem_interpretation(cls, stem: str) -> Optional[Dict[str, Any]]:
        """获取天干解读"""
        return cls.STEM_INTERPRETATIONS.get(stem)

    @classmethod
    def get_all_stems(cls) -> List[Dict[str, str]]:
        """获取所有天干"""
        return [
            {"name": stem, "nature": info["nature"]}
            for stem, info in cls.STEM_INTERPRETATIONS.items()
        ]

    @classmethod
    def get_branch_interpretation(cls, branch: str) -> Optional[Dict[str, Any]]:
        """获取地支解读"""
        return cls.BRANCH_INTERPRETATIONS.get(branch)

    @classmethod
    def get_all_branches(cls) -> List[Dict[str, Any]]:
        """获取所有地支"""
        return [
            {"name": branch, **info}
            for branch, info in cls.BRANCH_INTERPRETATIONS.items()
        ]

    @classmethod
    def get_ten_god(cls, god_name: str) -> Optional[Dict[str, Any]]:
        """获取十神信息"""
        return cls.TEN_GODS.get(god_name)

    @classmethod
    def get_all_ten_gods(cls) -> List[Dict[str, Any]]:
        """获取所有十神"""
        return [
            {"name": name, **info}
            for name, info in cls.TEN_GODS.items()
        ]

    @classmethod
    def calculate_stem_branch_nature(cls, stem: str, branch: str) -> Dict[str, Any]:
        """计算干支组合特性"""
        stem_info = cls.STEM_INTERPRETATIONS.get(stem, {})
        branch_info = cls.BRANCH_INTERPRETATIONS.get(branch, {})

        return {
            "stem": stem,
            "branch": branch,
            "combination": f"{stem}{branch}",
            "stem_nature": stem_info.get("nature"),
            "branch_nature": branch_info.get("nature"),
            "analysis": f"{stem}木{branch}支的组合特性分析"
        }

    @classmethod
    def analyze_stem_combination(cls, stems: List[str]) -> Dict[str, Any]:
        """分析天干组合"""
        result = {"stems": stems, "analysis": []}

        for i, stem1 in enumerate(stems):
            for stem2 in stems[i+1:]:
                stem1_info = cls.STEM_INTERPRETATIONS.get(stem1, {})
                stem2_info = cls.STEM_INTERPRETATIONS.get(stem2, {})
                result["analysis"].append({
                    "combination": f"{stem1}{stem2}",
                    "stem1": stem1_info.get("nature"),
                    "stem2": stem2_info.get("nature")
                })

        return result
