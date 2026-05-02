"""
八字神煞知识库
源自《三命通会》《渊海子平》《星平会海》

神煞分类：
- 吉神：天乙贵人、文昌、驿马、桃花、天德、月德等
- 凶煞：羊刃、亡神、劫煞、孤辰寡宿等
- 中性神煞：需结合全局判断吉凶
"""

LUCKY_SHAS = [
    {
        "id": "ls_001",
        "name": "天乙贵人",
        "pinyin": "tiān yǐ guì rén",
        "category": "贵人星",
        "nature": "吉",
        "calculations": [
            "甲戊兼牛羊（甲日、戊日出生者见牛、羊）",
            "乙己鼠猴乡（乙日、己日出生者见鼠、猴）",
            "丙丁猪鸡位（丙日、丁日出生者见猪、鸡）",
            "壬癸兔蛇藏（壬日、癸日出生者见兔、蛇）",
            "庚辛逢马虎（庚日、辛日出生者见马、虎）"
        ],
        "calculation_formula": {
            "甲日": ["丑", "未"],
            "戊日": ["丑", "未"],
            "乙日": ["子", "申"],
            "己日": ["子", "申"],
            "丙日": ["亥", "酉"],
            "丁日": ["亥", "酉"],
            "庚日": ["午", "寅"],
            "辛日": ["午", "寅"],
            "壬日": ["卯", "巳"],
            "癸日": ["卯", "巳"]
        },
        "meaning": "一生逢凶化吉，得贵人扶持",
        "effects": {
            "personality": "人缘好，易得他人帮助",
            "career": "事业发展顺利，易获提拔",
            "relationships": "得贵人相助，人际和谐"
        },
        "best_positions": ["年支", "日支"],
        "source": {"book": "三命通会", "chapter": "论天乙贵人"},
        "verification_status": "verified"
    },
    {
        "id": "ls_002",
        "name": "文昌贵人",
        "pinyin": "wén chāng guì rén",
        "category": "文昌星",
        "nature": "吉",
        "calculations": [
            "甲乙见申子（甲日、乙日见申、子）",
            "丙丁见酉亥（丙日、丁日见酉、亥）",
            "戊己见午申（戊日、己日见午、申）",
            "庚辛见戌子（庚日、辛日见戌、子）",
            "壬癸见丑卯（壬日、癸日见丑、卯）"
        ],
        "calculation_formula": {
            "甲日": ["申", "子"],
            "乙日": ["申", "子"],
            "丙日": ["酉", "亥"],
            "丁日": ["酉", "亥"],
            "戊日": ["午", "申"],
            "己日": ["午", "申"],
            "庚日": ["戌", "子"],
            "辛日": ["戌", "子"],
            "壬日": ["丑", "卯"],
            "癸日": ["丑", "卯"]
        },
        "meaning": "利于学业考试，文采出众",
        "effects": {
            "scholarship": "学业优秀，考试顺利",
            "career": "利于文职、教育类工作",
            "talent": "才华出众，表达能力强"
        },
        "best_positions": ["年支", "时支"],
        "source": {"book": "三命通会", "chapter": "论文昌贵人"},
        "verification_status": "verified"
    },
    {
        "id": "ls_003",
        "name": "驿马",
        "pinyin": "yì mǎ",
        "category": "迁移星",
        "nature": "中性偏吉",
        "calculations": [
            "申子辰马在寅（申月、子月、辰日见寅为驿马）",
            "寅午戌马在申（寅月、午月、戌日见申为驿马）",
            "巳酉丑马在亥（巳月、酉月、丑日见亥为驿马）",
            "亥卯未见巳（亥月、卯月、未日见巳为驿马）"
        ],
        "calculation_formula": {
            "申": ["寅"],
            "子": ["寅"],
            "辰": ["寅"],
            "寅": ["申"],
            "午": ["申"],
            "戌": ["申"],
            "巳": ["亥"],
            "酉": ["亥"],
            "丑": ["亥"],
            "亥": ["巳"],
            "卯": ["巳"],
            "未": ["巳"]
        },
        "meaning": "走动奔波，利于外出发展",
        "effects": {
            "travel": "多走动出差，利于外派",
            "career": "利于外出发展的行业",
            "mind": "思维活跃，不安于现状"
        },
        "notes": "驿马逢冲则动更甚，驿马被合则动少",
        "best_positions": ["时支"],
        "source": {"book": "渊海子平", "chapter": "论驿马"},
        "verification_status": "verified"
    },
    {
        "id": "ls_004",
        "name": "桃花",
        "pinyin": "táo huā",
        "category": "桃花星",
        "nature": "中性",
        "calculations": [
            "申子辰见酉（申月、子月、辰日见酉为桃花）",
            "寅午戌见卯（寅月、午月、戌日见卯为桃花）",
            "巳酉丑见午（巳月、酉月、丑日见午为桃花）",
            "亥卯未见子（亥月、卯月、未日见子为桃花）"
        ],
        "calculation_formula": {
            "申": ["酉"],
            "子": ["酉"],
            "辰": ["酉"],
            "寅": ["卯"],
            "午": ["卯"],
            "戌": ["卯"],
            "巳": ["午"],
            "酉": ["午"],
            "丑": ["午"],
            "亥": ["子"],
            "卯": ["子"],
            "未": ["子"]
        },
        "meaning": "异性缘佳，利于感情",
        "effects": {
            "relationships": "异性缘好，感情丰富",
            "social": "人缘佳，善于交际",
            "talent": "艺术气质，表达能力佳"
        },
        "types": [
            {"name": "墙内桃花", "position": "年支、月支", "meaning": "利感情婚姻"},
            {"name": "墙外桃花", "position": "日支、时支", "meaning": "易有感情纠葛"}
        ],
        "notes": "桃花逢冲或带官杀则易有感情问题",
        "source": {"book": "三命通会", "chapter": "论桃花"},
        "verification_status": "verified"
    },
    {
        "id": "ls_005",
        "name": "天德贵人",
        "pinyin": "tiān dé guì rén",
        "category": "天德星",
        "nature": "吉",
        "calculations": [
            "正月生者见丁",
            "二月生者见申",
            "三月生者见壬",
            "四月生者见辛",
            "五月生者见亥",
            "六月生者见甲",
            "七月生者见癸",
            "八月生者见寅",
            "九月生者见丙",
            "十月生者见乙",
            "十一月生者见辰",
            "十二月生者见庚"
        ],
        "calculation_formula": {
            "正月": "丁", "二月": "申", "三月": "壬", "四月": "辛",
            "五月": "亥", "六月": "甲", "七月": "癸", "八月": "寅",
            "九月": "丙", "十月": "乙", "十一月": "辰", "十二月": "庚"
        },
        "meaning": "化解灾厄，带来吉祥",
        "effects": {
            "fortune": "逢凶化吉，灾厄化解",
            "health": "身体健康，少有病痛",
            "career": "事业发展顺利"
        },
        "best_positions": ["月支"],
        "source": {"book": "星平会海", "chapter": "论天德"},
        "verification_status": "verified"
    },
    {
        "id": "ls_006",
        "name": "月德贵人",
        "pinyin": "yuè dé guì rén",
        "category": "月德星",
        "nature": "吉",
        "calculations": [
            "寅午戌月丙（寅月、午月、戌月见丙为月德）",
            "申子辰月壬（申月、子月、辰月见壬为月德）",
            "亥卯未月甲（亥月、卯月、未月见甲为月德）",
            "巳酉丑月庚（巳月、酉月、丑月见庚为月德）"
        ],
        "calculation_formula": {
            "寅月": "丙", "午月": "丙", "戌月": "丙",
            "申月": "壬", "子月": "壬", "辰月": "壬",
            "亥月": "甲", "卯月": "甲", "未月": "甲",
            "巳月": "庚", "酉月": "庚", "丑月": "庚"
        },
        "meaning": "逢凶化吉，利于事业",
        "effects": {
            "fortune": "灾厄化解，平安吉祥",
            "relationships": "人际关系和谐",
            "career": "事业发展顺利"
        },
        "notes": "天德月德并临，化解之力最强",
        "source": {"book": "星平会海", "chapter": "论月德"},
        "verification_status": "verified"
    },
    {
        "id": "ls_007",
        "name": "天厨贵人",
        "pinyin": "tiān chú guì rén",
        "category": "福禄星",
        "nature": "吉",
        "calculations": [
            "甲日见巳，乙日见午",
            "丙日见酉，丁日见戌",
            "戊日见子，己日见丑",
            "庚日见寅，辛日见卯",
            "壬日见午，癸日见未"
        ],
        "calculation_formula": {
            "甲日": "巳", "乙日": "午", "丙日": "酉", "丁日": "戌",
            "戊日": "子", "己日": "丑", "庚日": "寅", "辛日": "卯",
            "壬日": "午", "癸日": "未"
        },
        "meaning": "丰衣足食，衣禄无忧",
        "effects": {
            "food": "饮食无忧，有口福",
            "fortune": "生活富足，衣禄充足"
        },
        "source": {"book": "三命通会", "chapter": "论天厨贵人"},
        "verification_status": "verified"
    },
    {
        "id": "ls_008",
        "name": "福星贵人",
        "pinyin": "fú xīng guì rén",
        "category": "福禄星",
        "nature": "吉",
        "calculations": [
            "甲日见寅子，乙日见卯丑",
            "丙日见寅子，丁日见卯丑",
            "戊日见申辰，己日见酉巳",
            "庚日见午戌，辛日见巳未",
            "壬日见午戌，癸日见巳未"
        ],
        "meaning": "一生福禄，平安吉祥",
        "effects": {
            "fortune": "福气深厚，一生平安",
            "career": "事业平稳，少有波折"
        },
        "source": {"book": "三命通会", "chapter": "论福星贵人"},
        "verification_status": "verified"
    },
    {
        "id": "ls_009",
        "name": "国印贵人",
        "pinyin": "guó yìn guì rén",
        "category": "贵印星",
        "nature": "吉",
        "calculations": [
            "甲日见戌，乙日见亥",
            "丙日见丑，丁日见寅",
            "戊日见卯，己日见辰",
            "庚日见巳，辛日见午",
            "壬日见未，癸日见申"
        ],
        "calculation_formula": {
            "甲日": "戌", "乙日": "亥", "丙日": "丑", "丁日": "寅",
            "戊日": "卯", "己日": "辰", "庚日": "巳", "辛日": "午",
            "壬日": "未", "癸日": "申"
        },
        "meaning": "利于仕途，有掌印之权",
        "effects": {
            "career": "利于从政，有印绶之权",
            "status": "地位稳固，易获升迁"
        },
        "source": {"book": "渊海子平", "chapter": "论国印贵人"},
        "verification_status": "verified"
    },
    {
        "id": "ls_010",
        "name": "天赦贵人",
        "pinyin": "tiān shè guì rén",
        "category": "赦免星",
        "nature": "吉",
        "calculations": [
            "春戊寅（春季寅月见戊日为天赦）",
            "夏甲午（夏季午月见甲日为天赦）",
            "秋戊申（秋季申月见戊日为天赦）",
            "冬甲子（冬季子月见甲子为天赦）"
        ],
        "calculation_formula": {
            "寅月": "戊", "卯月": "戊", "辰月": "戊",
            "巳月": "甲", "午月": "甲", "未月": "甲",
            "申月": "戊", "酉月": "戊", "戌月": "戊",
            "亥月": "甲子", "子月": "甲子", "丑月": "甲子"
        },
        "meaning": "灾厄赦免，化险为夷",
        "effects": {
            "fortune": "灾厄得以赦免",
            "legal": "减少官讼是非"
        },
        "source": {"book": "三命通会", "chapter": "论天赦"},
        "verification_status": "verified"
    },
    {
        "id": "ls_011",
        "name": "金舆贵人",
        "pinyin": "jīn yú guì rén",
        "category": "车马星",
        "nature": "吉",
        "calculations": [
            "甲日见辰，乙日见巳",
            "丙日见未，丁日见申",
            "戊日见戌，己日见酉",
            "庚日见子，辛日见午",
            "壬日见寅，癸日见卯"
        ],
        "calculation_formula": {
            "甲日": "辰", "乙日": "巳", "丙日": "未", "丁日": "申",
            "戊日": "戌", "己日": "酉", "庚日": "子", "辛日": "午",
            "壬日": "寅", "癸日": "卯"
        },
        "meaning": "出行顺利，有车马之缘",
        "effects": {
            "travel": "出行顺利，有车有房",
            "career": "利于经商或贸易"
        },
        "source": {"book": "三命通会", "chapter": "论金舆"},
        "verification_status": "verified"
    },
    {
        "id": "ls_012",
        "name": "太极贵人",
        "pinyin": "tài jí guì rén",
        "category": "智慧星",
        "nature": "吉",
        "calculations": [
            "甲日见子子，乙日见午子",
            "丙日见卯酉，丁日见卯酉",
            "戊日见午酉，己日见午酉",
            "庚日见子亥，辛日见午亥",
            "壬日见卯寅，癸日见卯寅"
        ],
        "meaning": "聪明好学，有特异功能",
        "effects": {
            "wisdom": "聪明过人，有悟性",
            "spirituality": "有灵性，对神秘事物感兴趣"
        },
        "source": {"book": "三命通会", "chapter": "论太极贵人"},
        "verification_status": "verified"
    },
    {
        "id": "ls_013",
        "name": "学堂词馆",
        "pinyin": "xué táng cí guǎn",
        "category": "文昌星",
        "nature": "吉",
        "calculations": [
            "甲日见亥子，乙日见寅卯",
            "丙日见寅卯，丁日见巳午",
            "戊日见巳午，己日见申酉",
            "庚日见申酉，辛日见亥子",
            "壬日见申酉，癸日见寅卯"
        ],
        "meaning": "利于学业功名",
        "effects": {
            "scholarship": "学业进步，考试顺利",
            "career": "利于文职"
        },
        "source": {"book": "渊海子平", "chapter": "论学堂词馆"},
        "verification_status": "verified"
    },
    {
        "id": "ls_014",
        "name": "天官贵人",
        "pinyin": "tiān guān guì rén",
        "category": "贵官星",
        "nature": "吉",
        "calculations": [
            "甲日见未，乙日见申",
            "丙日见酉，丁日见亥",
            "戊日见子，己日见丑",
            "庚日见寅，辛日见卯",
            "壬日见辰，癸日见巳"
        ],
        "meaning": "利于仕途发展",
        "effects": {
            "career": "利于官场发展",
            "status": "地位提升"
        },
        "source": {"book": "三命通会", "chapter": "论天官贵人"},
        "verification_status": "verified"
    },
    {
        "id": "ls_015",
        "name": "将星",
        "pinyin": "jiāng xīng",
        "category": "权力星",
        "nature": "吉",
        "calculations": [
            "申子辰见子（申月、子月、辰日见子为将星）",
            "寅午戌见午（寅月、午月、戌日见午为将星）",
            "巳酉丑见酉（巳月、酉月、丑日见酉为将星）",
            "亥卯未见卯（亥月、卯月、未日见卯为将星）"
        ],
        "calculation_formula": {
            "申": "子", "子": "子", "辰": "子",
            "寅": "午", "午": "午", "戌": "午",
            "巳": "酉", "酉": "酉", "丑": "酉",
            "亥": "卯", "卯": "卯", "未": "卯"
        },
        "meaning": "有权有势，掌兵权",
        "effects": {
            "authority": "领导力强，有权力",
            "career": "利于管理层"
        },
        "source": {"book": "渊海子平", "chapter": "论将星"},
        "verification_status": "verified"
    }
]

UNLUCKY_SHAS = [
    {
        "id": "us_001",
        "name": "羊刃",
        "pinyin": "yáng rèn",
        "category": "刚暴星",
        "nature": "凶",
        "calculations": [
            "甲刃在卯，乙刃在寅",
            "丙刃在午，戊刃在午",
            "己刃在巳，庚刃在酉",
            "辛刃在申，壬刃在子",
            "癸刃在亥"
        ],
        "calculation_formula": {
            "甲": "卯", "乙": "寅", "丙": "午", "丁": "午",
            "戊": "午", "己": "巳", "庚": "酉", "辛": "申",
            "壬": "子", "癸": "亥"
        },
        "meaning": "刚暴易怒，易有血光",
        "effects": {
            "personality": "刚强暴躁，容易冲动",
            "health": "易有血光之灾或手术",
            "relationships": "人际冲突，刀刃之灾"
        },
        "avoidance": "修身养性，避免冲突，谨言慎行",
        "good_combination": "羊刃驾杀、羊刃配印",
        "bad_combination": "羊刃逢冲、羊刃无制",
        "source": {"book": "渊海子平", "chapter": "论羊刃"},
        "verification_status": "verified"
    },
    {
        "id": "us_002",
        "name": "亡神",
        "pinyin": "wáng shén",
        "category": "凶煞星",
        "nature": "凶",
        "calculations": [
            "申子辰见亥（申月、子月、辰日见亥为亡神）",
            "寅午戌见巳（寅月、午月、戌日见巳为亡神）",
            "巳酉丑见申（巳月、酉月、丑日见申为亡神）",
            "亥卯未见寅（亥月、卯月、未日见寅为亡神）"
        ],
        "calculation_formula": {
            "申": "亥", "子": "亥", "辰": "亥",
            "寅": "巳", "午": "巳", "戌": "巳",
            "巳": "申", "酉": "申", "丑": "申",
            "亥": "寅", "卯": "寅", "未": "寅"
        },
        "meaning": "心神不宁，易有官非",
        "effects": {
            "mind": "心神不宁，易有烦恼",
            "legal": "易有官讼是非",
            "relationships": "易与人发生争执"
        },
        "notes": "亡神见官杀则凶，见贵人则解",
        "source": {"book": "三命通会", "chapter": "论亡神"},
        "verification_status": "verified"
    },
    {
        "id": "us_003",
        "name": "劫煞",
        "pinyin": "jié shà",
        "category": "凶煞星",
        "nature": "凶",
        "calculations": [
            "申子辰见巳（申月、子月、辰日见巳为劫煞）",
            "寅午戌见亥（寅月、午月、戌日见亥为劫煞）",
            "巳酉丑见寅（巳月、酉月、丑日见寅为劫煞）",
            "亥卯未见申（亥月、卯月、未日见申为劫煞）"
        ],
        "calculation_formula": {
            "申": "巳", "子": "巳", "辰": "巳",
            "寅": "亥", "午": "亥", "戌": "亥",
            "巳": "寅", "酉": "寅", "丑": "寅",
            "亥": "申", "卯": "申", "未": "申"
        },
        "meaning": "易遭劫难破财",
        "effects": {
            "fortune": "易破财遭劫",
            "career": "事业多阻滞",
            "relationships": "易被欺骗背叛"
        },
        "notes": "劫煞见财则破财，见官则官灾",
        "source": {"book": "渊海子平", "chapter": "论劫煞"},
        "verification_status": "verified"
    },
    {
        "id": "us_004",
        "name": "孤辰寡宿",
        "pinyin": "gū chén guǎ sù",
        "category": "孤独星",
        "nature": "凶",
        "calculations": {
            "孤辰": [
                "亥子丑见寅（亥月、子月、丑月见寅为孤辰）",
                "寅卯辰见巳（寅月、卯月、辰月见巳为孤辰）",
                "巳午未见申（巳月、午月、未月见申为孤辰）",
                "申酉戌见亥（申月、酉月、戌月见亥为孤辰）"
            ],
            "寡宿": [
                "亥子丑见戌（亥月、子月、丑月见戌为寡宿）",
                "寅卯辰见未（寅月、卯月、辰月见未为寡宿）",
                "巳午未见辰（巳月、午月、未月见辰为寡宿）",
                "申酉戌见丑（申月、酉月、戌月见丑为寡宿）"
            ]
        },
        "calculation_formula": {
            "孤辰": {
                "亥": "寅", "子": "寅", "丑": "寅",
                "寅": "巳", "卯": "巳", "辰": "巳",
                "巳": "申", "午": "申", "未": "申",
                "申": "亥", "酉": "亥", "戌": "亥"
            },
            "寡宿": {
                "亥": "戌", "子": "戌", "丑": "戌",
                "寅": "未", "卯": "未", "辰": "未",
                "巳": "辰", "午": "辰", "未": "辰",
                "申": "丑", "酉": "丑", "戌": "丑"
            }
        },
        "meaning": "性格孤独，人际欠佳",
        "effects": {
            "personality": "性格内向，孤独感强",
            "relationships": "人际关系差，婚恋不顺",
            "family": "与六亲缘薄"
        },
        "notes": "孤辰寡宿同现更凶，易孤独终老",
        "source": {"book": "三命通会", "chapter": "论孤辰寡宿"},
        "verification_status": "verified"
    },
    {
        "id": "us_005",
        "name": "元辰",
        "pinyin": "yuán chén",
        "category": "大耗星",
        "nature": "凶",
        "calculations": [
            "阳男阴女：子年见未，丑年见午",
            "阴男阳女：子年见巳，丑年见辰"
        ],
        "meaning": "大耗钱财，易有灾祸",
        "effects": {
            "fortune": "破耗严重，财来财去",
            "accident": "易有意外灾祸"
        },
        "source": {"book": "三命通会", "chapter": "论元辰"},
        "verification_status": "verified"
    },
    {
        "id": "us_006",
        "name": "阴差阳错",
        "pinyin": "yīn chā yáng cuò",
        "category": "婚姻星",
        "nature": "凶",
        "calculations": [
            "丙子、丙午见辛卯辛酉",
            "丁丑、丁未见壬申壬寅",
            "戊寅、戊申见癸亥癸巳",
            "己卯、己酉见甲午甲辰",
            "庚午见甲辰甲戌",
            "辛巳见乙未乙丑",
            "壬辰、壬戌见丙子丙午",
            "癸未、癸丑见丁巳丁亥"
        ],
        "meaning": "婚姻不顺，感情纠葛",
        "effects": {
            "marriage": "婚姻感情多波折",
            "relationships": "与异性缘分不佳"
        },
        "notes": "阴差阳错日出生者，婚姻多有不顺",
        "source": {"book": "滴天髓", "chapter": "论阴差阳错"},
        "verification_status": "verified"
    },
    {
        "id": "us_007",
        "name": "十恶大败",
        "pinyin": "shí è dà bài",
        "category": "破败星",
        "nature": "凶",
        "calculations": [
            "甲辰、乙巳、丙申、丁亥、戊戌",
            "己卯、庚寅、辛酉、壬子、癸丑"
        ],
        "meaning": "财运不佳，办事难成",
        "effects": {
            "fortune": "财运不佳，开销大",
            "career": "事业阻碍，办事不顺"
        },
        "notes": "十恶大败日出生者，理财能力差",
        "source": {"book": "渊海子平", "chapter": "论十恶大败"},
        "verification_status": "verified"
    },
    {
        "id": "us_008",
        "name": "魁罡",
        "pinyin": "kuí gāng",
        "category": "刚强星",
        "nature": "中性偏凶",
        "calculations": [
            "庚辰、壬辰、戊戌、庚戌"
        ],
        "meaning": "刚强果断，不利女命",
        "effects": {
            "personality": "性格刚强，行事果断",
            "caution": "女命魁罡多婚姻问题"
        },
        "notes": "魁罡加临财官印，格局反而为吉",
        "source": {"book": "滴天髓", "chapter": "论魁罡"},
        "verification_status": "verified"
    },
    {
        "id": "us_009",
        "name": "红艳煞",
        "pinyin": "hóng yàn shà",
        "category": "桃花煞",
        "nature": "凶",
        "calculations": [
            "甲见午、乙见午、丙见寅",
            "丁见戌、戊见辰、己见辰",
            "庚见戌、辛见酉、壬见子",
            "癸见申"
        ],
        "meaning": "感情外露，易有桃花",
        "effects": {
            "relationships": "感情丰富，易有外遇",
            "reputation": "易有感情风波影响名声"
        },
        "notes": "红艳煞加桃花更凶",
        "source": {"book": "三命通会", "chapter": "论红艳煞"},
        "verification_status": "verified"
    },
    {
        "id": "us_010",
        "name": "寡宿",
        "pinyin": "guǎ sù",
        "category": "孤独星",
        "nature": "凶",
        "calculations": [
            "亥子丑见戌（亥月、子月、丑月见戌为寡宿）",
            "寅卯辰见未（寅月、卯月、辰月见未为寡宿）",
            "巳午未见辰（巳月、午月、未月见辰为寡宿）",
            "申酉戌见丑（申月、酉月、戌月见丑为寡宿）"
        ],
        "calculation_formula": {
            "亥": "戌", "子": "戌", "丑": "戌",
            "寅": "未", "卯": "未", "辰": "未",
            "巳": "辰", "午": "辰", "未": "辰",
            "申": "丑", "酉": "丑", "戌": "丑"
        },
        "meaning": "孤独寡居，婚姻难成",
        "effects": {
            "marriage": "婚姻难成或丧偶",
            "relationships": "与配偶缘薄"
        },
        "source": {"book": "渊海子平", "chapter": "论寡宿"},
        "verification_status": "verified"
    },
    {
        "id": "us_011",
        "name": "勾绞",
        "pinyin": "gōu jiǎo",
        "category": "凶煞星",
        "nature": "凶",
        "calculations": [
            "阳男阴女：见卯、戌、酉、午",
            "阴男阳女：见辰、巳、申、丑"
        ],
        "meaning": "易有牵连纠葛",
        "effects": {
            "legal": "易有官讼牵连",
            "relationships": "易与人发生纠纷"
        },
        "source": {"book": "三命通会", "chapter": "论勾绞"},
        "verification_status": "verified"
    },
    {
        "id": "us_012",
        "name": "埋儿杀",
        "pinyin": "mái ér shā",
        "category": "子嗣星",
        "nature": "凶",
        "calculations": [
            "子午卯酉见申，申子辰见卯",
            "寅午戌见亥，亥卯未见午",
            "巳酉丑见寅，寅申巳见酉",
            "辰戌丑未见子，丑未辰见戌"
        ],
        "meaning": "不利子嗣，难以生育",
        "effects": {
            "children": "不利子嗣或难孕",
            "family": "与子女缘分浅"
        },
        "source": {"book": "渊海子平", "chapter": "论埋儿杀"},
        "verification_status": "verified"
    },
    {
        "id": "us_013",
        "name": "流霞",
        "pinyin": "liú xiá",
        "category": "灾祸星",
        "nature": "凶",
        "calculations": [
            "甲日见酉，乙日见戌",
            "丙日见未，丁日见申",
            "戊日见巳，己日见午",
            "庚日见辰，辛日见卯",
            "壬日见寅，癸日见丑"
        ],
        "meaning": "易有血光之灾",
        "effects": {
            "health": "易有血光灾祸",
            "accident": "易有意外事故"
        },
        "source": {"book": "三命通会", "chapter": "论流霞"},
        "verification_status": "verified"
    },
    {
        "id": "us_014",
        "name": "咸池",
        "pinyin": "xián chí",
        "category": "桃花煞",
        "nature": "凶",
        "calculations": [
            "申子辰见酉，寅午戌见卯",
            "巳酉丑见午，亥卯未见子"
        ],
        "calculation_formula": {
            "申": "酉", "子": "酉", "辰": "酉",
            "寅": "卯", "午": "卯", "戌": "卯",
            "巳": "午", "酉": "午", "丑": "午",
            "亥": "子", "卯": "子", "未": "子"
        },
        "meaning": "桃花煞，易有感情问题",
        "effects": {
            "relationships": "感情纠纷多",
            "reputation": "易有桃花风波"
        },
        "notes": "咸池即桃花，但性质更凶",
        "source": {"book": "星平会海", "chapter": "论咸池"},
        "verification_status": "verified"
    },
    {
        "id": "us_015",
        "name": "天罗地网",
        "pinyin": "tiān luó dì wǎng",
        "category": "困厄星",
        "nature": "凶",
        "calculations": [
            "辰为天罗，戌为地网",
            "男怕天罗，女怕地网",
            "亥子辰巳午未寅午戌见辰为天罗",
            "亥子辰巳午未申酉丑见戌为地网"
        ],
        "meaning": "阻碍重重，运势不佳",
        "effects": {
            "career": "事业阻碍，仕途不顺",
            "fortune": "运势低迷，困难重重"
        },
        "notes": "天罗地网逢冲可解",
        "source": {"book": "渊海子平", "chapter": "论天罗地网"},
        "verification_status": "verified"
    }
]

NEUTRAL_SHAS = [
    {
        "id": "ns_001",
        "name": "三奇贵人",
        "pinyin": "sān qí guì rén",
        "category": "贵奇星",
        "nature": "中性",
        "calculations": [
            "天上三奇：甲戊庚",
            "地下三奇：乙丙丁",
            "人中三奇：壬癸辛"
        ],
        "meaning": "才学出众，命运非凡",
        "effects": {
            "wisdom": "聪明过人",
            "fortune": "命运奇特"
        },
        "notes": "三奇需顺序不乱方验",
        "source": {"book": "渊海子平", "chapter": "论三奇"},
        "verification_status": "verified"
    },
    {
        "id": "ns_002",
        "name": "金神",
        "pinyin": "jīn shén",
        "category": "刚强星",
        "nature": "中性",
        "calculations": [
            "乙日见巳丑，丙日见寅子",
            "丁日见卯亥，戊日见午寅",
            "己日见酉申，庚日见辰午",
            "辛日见未戌，壬日见申丑",
            "癸日见卯辰"
        ],
        "meaning": "刚强果敢，利于武职",
        "effects": {
            "personality": "性格刚强",
            "career": "利于武职"
        },
        "notes": "金神入火乡为贵",
        "source": {"book": "滴天髓", "chapter": "论金神"},
        "verification_status": "verified"
    },
    {
        "id": "ns_003",
        "name": "华盖",
        "pinyin": "huá gài",
        "category": "艺术星",
        "nature": "中性",
        "calculations": [
            "寅午戌见戌，申子辰见辰",
            "巳酉丑见丑，亥卯未见未"
        ],
        "calculation_formula": {
            "寅": "戌", "午": "戌", "戌": "戌",
            "申": "辰", "子": "辰", "辰": "辰",
            "巳": "丑", "酉": "丑", "丑": "丑",
            "亥": "未", "卯": "未", "未": "未"
        },
        "meaning": "聪明有才，孤独清高",
        "effects": {
            "talent": "聪明有才华",
            "personality": "性格孤僻，清高"
        },
        "notes": "华盖临印学业好，临桃花感情丰",
        "source": {"book": "三命通会", "chapter": "论华盖"},
        "verification_status": "verified"
    },
    {
        "id": "ns_004",
        "name": "空亡",
        "pinyin": "kōng wáng",
        "category": "空缺星",
        "nature": "中性",
        "calculations": [
            "甲子旬见戌亥，甲戌旬见申酉",
            "甲申旬见午未，甲午旬见辰巳",
            "甲辰旬见寅卯，甲寅旬见子丑"
        ],
        "meaning": "事事落空，缺而不全",
        "effects": {
            "fortune": "财运不佳",
            "career": "事业难成"
        },
        "notes": "空亡可被填实或逢冲",
        "source": {"book": "渊海子平", "chapter": "论空亡"},
        "verification_status": "verified"
    }
]

ALL_SHAS = {
    "lucky_shens": LUCKY_SHAS,
    "unlucky_shens": UNLUCKY_SHAS,
    "neutral_shens": NEUTRAL_SHAS
}
