from typing import Dict, List, Optional, Any
from datetime import datetime


class QimenClassics:
    """奇门遁甲古籍库"""

    CLASSICS_METADATA = {
        "奇门遁甲全书": {
            "author": "传统古籍",
            "dynasty": "古代",
            "category": "qimen",
            "chapters": [
                "阴阳遁",
                "三元遁甲",
                "九宫八卦",
                "八门九星",
                "八神八将",
                "吉凶格局",
                "日家奇门",
                "时家奇门",
                "飞宫奇门",
                "转盘奇门",
                "阳遁阴遁",
                "三元节气"
            ],
            "key_concepts": [
                "三奇六仪", "八门九星", "八神八将", "九宫八卦",
                "阳遁阴遁", "值符值使", "吉凶格局", "旺相休囚"
            ]
        },
        "金函玉镜": {
            "author": "传统古籍",
            "dynasty": "明代",
            "category": "qimen",
            "chapters": [
                "奇门源流",
                "排盘起例",
                "八门详解",
                "九星详论",
                "八神阐述",
                "三奇六仪",
                "吉格凶格",
                "日时选择",
                "方位吉凶",
                "趋避之道"
            ],
            "key_concepts": [
                "八门克应", "九星象意", "八神特性", "三奇妙用",
                "符使运行", "宫门星神", "格局吉凶", "主客动静"
            ]
        },
        "烟波钓叟赋": {
            "author": "唐·赵一本",
            "dynasty": "唐代",
            "category": "qimen",
            "chapters": [
                "烟波钓叟歌",
                "奇门起例",
                "阴阳二遁",
                "三奇六仪",
                "八门九星",
                "八神八将",
                "吉凶格局",
                "占断要诀"
            ],
            "key_concepts": [
                "阴阳二遁", "三奇六仪", "八门九星", "八神八将",
                "值符值使", "飞符飞甲", "三诈五假", "九遁八门"
            ]
        }
    }

    EIGHT_DOORS = {
        "休门": {
            "nature": "休养",
            "keywords": ["休息", "美容", "调和", "贵人"],
            "meaning": "主休息、休养、调理、美容、贵人扶持",
            "position": "北方坎一宫",
            "element": "水",
            "auspicious": True,
            "best_for": ["休养", "美容", "洽谈", "求见贵人"]
        },
        "生门": {
            "nature": "生长",
            "keywords": ["财运", "生机", "投资", "营建"],
            "meaning": "主财运、生意、投资、营建、嫁娶",
            "position": "东北艮八宫",
            "element": "土",
            "auspicious": True,
            "best_for": ["求财", "投资", "开业", "嫁娶", "动土"]
        },
        "伤门": {
            "nature": "损伤",
            "keywords": ["伤害", "争斗", "狩猎", "收敛"],
            "meaning": "主伤害、争斗、狩猎、收敛、讨债",
            "position": "东方震三宫",
            "element": "木",
            "auspicious": False,
            "best_for": ["讨债", "狩猎", "捕捉", "行刑"]
        },
        "杜门": {
            "nature": "堵塞",
            "keywords": ["隐藏", "保密", "安全", "堵塞"],
            "meaning": "主隐藏、保密、堵隔、安全、逃难",
            "position": "东南巽四宫",
            "element": "木",
            "auspicious": False,
            "best_for": ["躲藏", "保密", "逃亡", "捕盗"]
        },
        "景门": {
            "nature": "景仰",
            "keywords": ["文化", "表达", "虚妄", "火光"],
            "meaning": "主文化、表达、虚妄、血光、词讼",
            "position": "南方离九宫",
            "element": "火",
            "auspicious": False,
            "best_for": ["文化活动", "考试", "展示", "酒宴"]
        },
        "死门": {
            "nature": "死亡",
            "keywords": ["死亡", "埋葬", "绝望", "不动"],
            "meaning": "主死亡、埋葬、绝望、官讼、擒捕",
            "position": "西南坤二宫",
            "element": "土",
            "auspicious": False,
            "best_for": ["吊丧", "埋葬", "捕猎", "镇邪"]
        },
        "惊门": {
            "nature": "惊恐",
            "keywords": ["惊恐", "口舌", "讼狱", "破损"],
            "meaning": "主惊恐、口舌、讼狱、破损、怪异",
            "position": "西方兑七宫",
            "element": "金",
            "auspicious": False,
            "best_for": ["捕捉", "讼狱", "斗讼"]
        },
        "开门": {
            "nature": "开创",
            "keywords": ["开创", "事业", "公开", "远行"],
            "meaning": "主开创、事业、公开、远行、贸易",
            "position": "西北乾六宫",
            "element": "金",
            "auspicious": True,
            "best_for": ["开业", "赴任", "远行", "贸易", "求官"]
        }
    }

    NINE_STARS = {
        "天蓬星": {
            "nature": "大凶",
            "keywords": ["破财", "盗贼", "大凶", "大耗"],
            "meaning": "主破财、盗贼、凶灾、风险、大耗",
            "position": "北方坎一宫",
            "element": "水",
            "behavior": "胆大妄为，善于谋略，敢于冒险"
        },
        "天任星": {
            "nature": "大吉",
            "keywords": ["求财", "婚姻", "嫁娶", "远行"],
            "meaning": "主求财、婚姻、嫁娶、远行、经商",
            "position": "东北艮八宫",
            "element": "土",
            "behavior": "忠厚老实，任劳任怨，固执保守"
        },
        "天冲星": {
            "nature": "次凶",
            "keywords": ["出征", "远行", "制造", "冲突"],
            "meaning": "主出征、远行、制造、冲突、变动",
            "position": "东方震三宫",
            "element": "木",
            "behavior": "冲动好斗，雷厉风行，快速行动"
        },
        "天辅星": {
            "nature": "大吉",
            "keywords": ["文化", "教育", "调解", "散忧"],
            "meaning": "主文化、教育、调解、散忧、贵人",
            "position": "东南巽四宫",
            "element": "木",
            "behavior": "文雅温和，有贵人运，善于教化"
        },
        "天禽星": {
            "nature": "大吉",
            "keywords": ["主吉", "中宫", "信诚", "稳重"],
            "meaning": "主吉，中宫得之万事皆吉，信诚稳重",
            "position": "中宫五",
            "element": "土",
            "behavior": "诚实守信，为人稳重，有领导力"
        },
        "天心星": {
            "nature": "大吉",
            "keywords": ["医疗", "领导", "策略", "谋划"],
            "meaning": "主医疗、领导、策略、谋划、阴密",
            "position": "西北乾六宫",
            "element": "金",
            "behavior": "心机深沉，智谋远大，善于策划"
        },
        "天柱星": {
            "nature": "次凶",
            "keywords": ["破财", "毁折", "惊恐", "讼狱"],
            "meaning": "主破财、毁折、惊恐、讼狱、破坏",
            "position": "西方兑七宫",
            "element": "金",
            "behavior": "能言善辩，敢于破坏，善于雄辩"
        },
        "天任星": {
            "nature": "大吉",
            "keywords": ["求财", "婚姻", "嫁娶", "远行"],
            "meaning": "主求财、婚姻、嫁娶、远行、经商",
            "position": "东北艮八宫",
            "element": "土",
            "behavior": "忠厚老实，任劳任怨"
        },
        "天芮星": {
            "nature": "大凶",
            "keywords": ["疾病", "问题", "错误", "学业"],
            "meaning": "主疾病、问题、错误、学业、疑惑",
            "position": "西南坤二宫",
            "element": "土",
            "behavior": "好学上进，但易有问题、疑惑"
        },
        "天英星": {
            "nature": "次凶",
            "keywords": ["血光", "是非", "文化", "文章"],
            "meaning": "主血光、是非、文化、文章、离乱",
            "position": "南方离九宫",
            "element": "火",
            "behavior": "性子急躁，好争是非，善于文学"
        }
    }

    EIGHT_GODS = {
        "值符": {
            "nature": "贵神",
            "keywords": ["贵人", "高档", "核心", "引领"],
            "meaning": "代表贵人、高档、核心、引领之物"
        },
        "螣蛇": {
            "nature": "虚耗",
            "keywords": ["惊恐", "怪异", "虚假", "缠绕"],
            "meaning": "代表惊恐、怪异、虚假、缠绕之事"
        },
        "太阴": {
            "nature": "阴佑",
            "keywords": ["阴私", "庇护", "秘密", "玉女"],
            "meaning": "代表阴私、庇护、秘密、暗中相助"
        },
        "六合": {
            "nature": "和合",
            "keywords": ["合伙", "婚姻", "中介", "调和"],
            "meaning": "代表合伙、婚姻、中介、调和之事"
        },
        "白虎": {
            "nature": "凶煞",
            "keywords": ["凶灾", "血光", "孝服", "争斗"],
            "meaning": "代表凶灾、血光、孝服、争斗之事"
        },
        "玄武": {
            "nature": "盗贼",
            "keywords": ["盗贼", "阴谋", "暗昧", "诡诈"],
            "meaning": "代表盗贼、阴谋、暗昧、诡诈之事"
        },
        "九地": {
            "nature": "坚牢",
            "keywords": ["长久", "稳定", "地下", "柔顺"],
            "meaning": "代表长久、稳定、地下、柔顺之事"
        },
        "九天": {
            "nature": "刚健",
            "keywords": ["高远", "变动", "行动", "张扬"],
            "meaning": "代表高远、变动、行动、张扬之事"
        }
    }

    THREE_ODD = {
        "乙": {
            "name": "日奇",
            "nature": "三奇之一",
            "keywords": ["希望", "花草", "医生", "艺术"],
            "meaning": "代表希望、花草、医生、艺术、谋士"
        },
        "丙": {
            "name": "月奇",
            "nature": "三奇之一",
            "keywords": ["权威", "光明", "文书", "契约"],
            "meaning": "代表权威、光明、文书、契约、票据"
        },
        "丁": {
            "name": "星奇",
            "nature": "三奇之一",
            "keywords": ["希望", "光明", "证件", "少女"],
            "meaning": "代表希望、光明、证件、少女、蜡烛"
        }
    }

    SIX_INSTRUMENTS = {
        "甲子": {"yin_yang": "阳", "wu_xing": "金", "meaning": "遁甲之始，万物之始"},
        "甲戌": {"yin_yang": "阴", "wu_xing": "土", "meaning": "隐于戌土，藏匿之象"},
        "甲申": {"yin_yang": "阴", "wu_xing": "金", "meaning": "隐于申金，锋利之象"},
        "甲午": {"yin_yang": "阳", "wu_xing": "火", "meaning": "隐于午火，文明之象"},
        "甲辰": {"yin_yang": "阳", "wu_xing": "土", "meaning": "隐于辰土，蓄养之象"},
        "甲寅": {"yin_yang": "阴", "wu_xing": "木", "meaning": "隐于寅木，生发之象"}
    }

    @classmethod
    def get_classics_list(cls) -> List[Dict[str, Any]]:
        """获取古籍列表"""
        return [
            {
                "title": title,
                "author": info["author"],
                "dynasty": info["dynasty"],
                "category": "奇门遁甲",
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
    def get_door(cls, door_name: str) -> Optional[Dict[str, Any]]:
        """获取八门信息"""
        return cls.EIGHT_DOORS.get(door_name)

    @classmethod
    def get_all_doors(cls) -> List[Dict[str, Any]]:
        """获取所有八门"""
        return [
            {"name": name, **info}
            for name, info in cls.EIGHT_DOORS.items()
        ]

    @classmethod
    def get_star(cls, star_name: str) -> Optional[Dict[str, Any]]:
        """获取九星信息"""
        return cls.NINE_STARS.get(star_name)

    @classmethod
    def get_all_stars(cls) -> List[Dict[str, Any]]:
        """获取所有九星"""
        return [
            {"name": name, "nature": info["nature"], "keywords": info["keywords"]}
            for name, info in cls.NINE_STARS.items()
        ]

    @classmethod
    def get_god(cls, god_name: str) -> Optional[Dict[str, Any]]:
        """获取八神信息"""
        return cls.EIGHT_GODS.get(god_name)

    @classmethod
    def get_all_gods(cls) -> List[Dict[str, Any]]:
        """获取所有八神"""
        return [
            {"name": name, **info}
            for name, info in cls.EIGHT_GODS.items()
        ]

    @classmethod
    def get_odd(cls, odd_name: str) -> Optional[Dict[str, Any]]:
        """获取三奇信息"""
        return cls.THREE_ODD.get(odd_name)

    @classmethod
    def get_all_odds(cls) -> List[Dict[str, Any]]:
        """获取所有三奇"""
        return [
            {"name": name, **info}
            for name, info in cls.THREE_ODD.items()
        ]

    @classmethod
    def get_instrument(cls, instrument: str) -> Optional[Dict[str, Any]]:
        """获取六仪信息"""
        return cls.SIX_INSTRUMENTS.get(instrument)

    @classmethod
    def get_all_instruments(cls) -> List[Dict[str, Any]]:
        """获取所有六仪"""
        return [
            {"name": name, **info}
            for name, info in cls.SIX_INSTRUMENTS.items()
        ]

    @classmethod
    def analyze_door_star_combination(cls, door: str, star: str) -> Dict[str, Any]:
        """分析门星组合"""
        door_info = cls.EIGHT_DOORS.get(door, {})
        star_info = cls.NINE_STARS.get(star, {})

        door_auspicious = door_info.get("auspicious", False)
        star_nature = star_info.get("nature", "")

        if "吉" in star_nature and door_auspicious:
            overall = "大吉"
        elif "凶" in star_nature and not door_auspicious:
            overall = "大凶"
        else:
            overall = "中等"

        return {
            "door": door,
            "star": star,
            "door_nature": door_info.get("nature"),
            "star_nature": star_nature,
            "overall_assessment": overall,
            "suggestion": "根据门星组合判断行动方向"
        }
