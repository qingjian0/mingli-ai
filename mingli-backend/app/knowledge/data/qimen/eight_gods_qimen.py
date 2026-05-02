"""
八神含义
奇门遁甲八神的详细解释

八神：值符、螣蛇、太阴、六合、白虎、玄武、九地、九天
"""

QIMEN_SPIRITS = [
    {
        "id": "spirit_001",
        "term": "值符",
        "pinyin": "zhífú",
        "wuxing": "木",
        "category": "eight_spirits",
        "system": "qimen",
        "nature": "吉神",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八神总论",
            "page": 90
        },
        "original_content": "值符者，诸神之首也。司天之事。",
        "interpretation": "值符是八神之首，代表天乙贵人和领导的能量。",
        "general_meaning": {
            "fortune": "贵人相助，地位稳固",
            "career": "利于领导、管理、决策",
            "relationships": "得贵人相助，人际和谐"
        },
        "keywords": ["天乙", "贵人", "领导", "首脑"],
        "combinations": {
            "with_door": "与开门：吉上加吉",
            "with_star": "与天辅星：大吉"
        },
        "favorable_activities": ["求职", "升迁", "管理", "签约"],
        "verification_status": "verified"
    },
    {
        "id": "spirit_002",
        "term": "螣蛇",
        "pinyin": "téngshé",
        "wuxing": "火",
        "category": "eight_spirits",
        "system": "qimen",
        "nature": "凶神",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八神总论",
            "page": 93
        },
        "original_content": "螣蛇者，惊惶之神也。司惊恐怪异之事。",
        "interpretation": "螣蛇代表惊恐、怪异、虚假，象征不安和迷惑。",
        "general_meaning": {
            "fortune": "易有惊恐，防假象",
            "career": "多变动，需防小人",
            "relationships": "易有欺骗，需谨慎"
        },
        "keywords": ["惊恐", "怪异", "虚假", "迷惑"],
        "combinations": {
            "with_door": "与惊门：惊恐万分",
            "with_star": "与天英星：文书纠纷"
        },
        "warning": "防假象和欺骗",
        "verification_status": "verified"
    },
    {
        "id": "spirit_003",
        "term": "太阴",
        "pinyin": "tàiyīn",
        "wuxing": "金",
        "category": "eight_spirits",
        "system": "qimen",
        "nature": "吉神",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八神总论",
            "page": 96
        },
        "original_content": "太阴者，阴私之神也。司暗昧阴私之事。",
        "interpretation": "太阴代表阴私、秘密、柔顺，象征隐秘的力量。",
        "general_meaning": {
            "fortune": "利于密谋，适合暗中行事",
            "career": "宜保守秘密，不宜张扬",
            "relationships": "利于感情，利于密谈"
        },
        "keywords": ["阴私", "秘密", "柔顺", "隐秘"],
        "combinations": {
            "with_door": "与杜门：保密最佳",
            "with_star": "与天辅星：利于求学"
        },
        "favorable_activities": ["保密", "密谈", "策划", "暗恋"],
        "verification_status": "verified"
    },
    {
        "id": "spirit_004",
        "term": "六合",
        "pinyin": "liùhé",
        "wuxing": "木",
        "category": "eight_spirits",
        "system": "qimen",
        "nature": "吉神",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八神总论",
            "page": 99
        },
        "original_content": "六合者和合之神也。司和合婚姻之事。",
        "interpretation": "六合代表和合、婚姻、合作，象征和谐与团聚。",
        "general_meaning": {
            "fortune": "诸事和合，人际融洽",
            "career": "利于合作、合伙、谈判",
            "relationships": "利于婚姻、恋爱、复合"
        },
        "keywords": ["和合", "婚姻", "合作", "团聚"],
        "combinations": {
            "with_door": "与休门：婚姻和合",
            "with_star": "与天辅星：贵人相助"
        },
        "favorable_activities": ["合作", "签约", "嫁娶", "和谈"],
        "verification_status": "verified"
    },
    {
        "id": "spirit_005",
        "term": "白虎",
        "pinyin": "báihǔ",
        "wuxing": "金",
        "category": "eight_spirits",
        "system": "qimen",
        "nature": "凶神",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八神总论",
            "page": 102
        },
        "original_content": "白虎者，凶暴之神也。司兵戈血光之事。",
        "interpretation": "白虎代表凶暴、血光、兵灾，象征危险和伤害。",
        "general_meaning": {
            "fortune": "诸事不吉，易有凶灾",
            "career": "多阻滞，不宜冒险",
            "health": "防血光之灾，注意安全"
        },
        "keywords": ["凶暴", "血光", "兵灾", "危险"],
        "combinations": {
            "with_door": "与死门：大凶",
            "with_star": "与天蓬星：盗难破财"
        },
        "warning": "白虎为大凶之神，用事宜极为谨慎",
        "verification_status": "verified"
    },
    {
        "id": "spirit_006",
        "term": "玄武",
        "pinyin": "xuánwǔ",
        "wuxing": "水",
        "category": "eight_spirits",
        "system": "qimen",
        "nature": "凶神",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八神总论",
            "page": 105
        },
        "original_content": "玄武者，盗耗之神也。司盗贼暗昧之事。",
        "interpretation": "玄武代表盗耗、欺骗、阴谋，象征暗中的破坏。",
        "general_meaning": {
            "fortune": "易有破耗，防盗防骗",
            "career": "小人多，防暗算",
            "relationships": "易有欺骗，防桃花劫"
        },
        "keywords": ["盗耗", "欺骗", "阴谋", "小人"],
        "combinations": {
            "with_door": "与杜门：阴谋暗算",
            "with_star": "与天蓬星：盗贼破财"
        },
        "warning": "玄武为凶神，防欺骗和破财",
        "verification_status": "verified"
    },
    {
        "id": "spirit_007",
        "term": "九地",
        "pinyin": "jiǔdì",
        "wuxing": "土",
        "category": "eight_spirits",
        "system": "qimen",
        "nature": "吉神",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八神总论",
            "page": 108
        },
        "original_content": "九地者，坚牢之神也。司土地田宅之事。",
        "interpretation": "九地代表坚牢、稳定、土地，象征安稳和持久。",
        "general_meaning": {
            "fortune": "稳重踏实，宜守成",
            "career": "宜稳不宜动，适合长线",
            "relationships": "感情稳定，不宜变动"
        },
        "keywords": ["坚牢", "稳定", "土地", "安稳"],
        "combinations": {
            "with_door": "与生门：稳中求财",
            "with_star": "与天任星：利田产"
        },
        "favorable_activities": ["置业", "长线投资", "守成", "稳固"],
        "verification_status": "verified"
    },
    {
        "id": "spirit_008",
        "term": "九天",
        "pinyin": "jiǔtiān",
        "wuxing": "金",
        "category": "eight_spirits",
        "system": "qimen",
        "nature": "吉神",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八神总论",
            "page": 111
        },
        "original_content": "九天者，高远之神也。司兵戈迁徒之事。",
        "interpretation": "九天代表高远、变动、迁徒，象征发展和扩张。",
        "general_meaning": {
            "fortune": "大展宏图，前途光明",
            "career": "利于扩张、变动、升迁",
            "relationships": "变动较大，不宜稳定"
        },
        "keywords": ["高远", "变动", "迁徒", "发展"],
        "combinations": {
            "with_door": "与开门：大吉，利远行",
            "with_star": "与天心星：决策果断"
        },
        "favorable_activities": ["远行", "扩张", "升迁", "发展"],
        "verification_status": "verified"
    }
]

SPIRIT_RANKINGS = {
    "best": ["值符", "六合", "九天"],
    "good": ["太阴", "九地"],
    "average": [],
    "bad": ["螣蛇", "玄武"],
    "worst": ["白虎"]
}
