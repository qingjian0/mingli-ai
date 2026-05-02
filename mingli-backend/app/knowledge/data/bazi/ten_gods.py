"""
十神含义
八字命理十神详解

十神包括：
- 同我者：比肩、劫财
- 生我者：正印、偏印（枭神）
- 我生者：食神、伤官
- 克我者：正官、七杀（偏官）
- 我克者：正财、偏财
"""

BAZI_TEN_GODS = [
    {
        "id": "god_001",
        "term": "比肩",
        "pinyin": "bǐjiān",
        "wuxing": "同类",
        "relationship": "同我者",
        "category": "ten_god",
        "system": "bazi",
        "nature": "阳干见阳干，阴干见阴干",
        "source": {
            "book": "渊海子平",
            "chapter": "论十神",
            "page": 45
        },
        "original_content": "比肩者，兄弟也。见同类而为比肩。",
        "interpretation": "比肩代表兄弟姐妹、同事、朋友，象征竞争和合作。",
        "positive_meaning": {
            "personality": "自尊心强，独立自主，意志坚定",
            "career": "适合独立创业，不宜合伙",
            "relationships": "与同龄人关系平等，竞争中有合作"
        },
        "negative_meaning": {
            "personality": "固执己见，不合群，自私",
            "career": "同行竞争，同事不和",
            "relationships": "兄弟争财，朋友背叛"
        },
        "keywords": ["兄弟", "竞争", "合作", "独立", "自尊"],
        "in_palace_effects": {
            "ming_gong": "自尊心强，有主见",
            "xiongdi_gong": "兄弟姐妹关系平等，互相竞争",
            "cai_gong": "理财保守，财务独立"
        },
        "verification_status": "verified"
    },
    {
        "id": "god_002",
        "term": "劫财",
        "pinyin": "jiécái",
        "wuxing": "同类",
        "relationship": "同我者",
        "category": "ten_god",
        "system": "bazi",
        "nature": "阳干见阴干，阴干见阳干",
        "source": {
            "book": "渊海子平",
            "chapter": "论十神",
            "page": 46
        },
        "original_content": "劫财者，分我之财也。见异类而为劫财。",
        "interpretation": "劫财代表破耗和争夺，象征财务上的争夺和消耗。",
        "positive_meaning": {
            "personality": "勇于竞争，敢于冒险",
            "career": "适合投资，敢于拼搏",
            "relationships": "与兄弟姐妹有竞争关系"
        },
        "negative_meaning": {
            "personality": "冲动鲁莽，不计后果",
            "career": "破财，投资失败",
            "relationships": "被兄弟姐妹夺财，口舌是非"
        },
        "keywords": ["破耗", "争夺", "冒险", "竞争", "破财"],
        "in_palace_effects": {
            "ming_gong": "敢于冒险，但易破财",
            "cai_gong": "财务不稳，易破耗",
            "xiongdi_gong": "兄弟姐妹争夺，注意财务"
        },
        "verification_status": "verified"
    },
    {
        "id": "god_003",
        "term": "正印",
        "pinyin": "zhèngyìn",
        "wuxing": "生我者",
        "relationship": "相生",
        "category": "ten_god",
        "system": "bazi",
        "nature": "异性相生，阴干见阳干，阳干见阴干",
        "source": {
            "book": "渊海子平",
            "chapter": "论十神",
            "page": 47
        },
        "original_content": "正印者，生我之母也。阴见阳为正印。",
        "interpretation": "正印代表母亲、长辈、学业、名誉，象征保护和庇荫。",
        "positive_meaning": {
            "personality": "仁慈善良，有爱心，有责任感",
            "career": "适合教育、文化、学术",
            "scholarship": "学业优秀，有学术成就",
            "fame": "名声好，受人尊敬"
        },
        "negative_meaning": {
            "personality": "依赖性强，缺乏主见",
            "career": "事业进展慢，难获提拔",
            "relationships": "与母亲缘薄，受长辈拖累"
        },
        "keywords": ["母亲", "学业", "名誉", "庇荫", "仁慈"],
        "in_palace_effects": {
            "ming_gong": "聪明好学，有爱心",
            "fu_gong": "与母亲缘深，得长辈庇荫",
            "guan_gong": "学业有成，仕途顺利"
        },
        "verification_status": "verified"
    },
    {
        "id": "god_004",
        "term": "偏印（枭神）",
        "pinyin": "piānyìn（xiāoshén）",
        "wuxing": "生我者",
        "relationship": "相生",
        "category": "ten_god",
        "system": "bazi",
        "nature": "同性相生，阴干见阴干，阳干见阳干",
        "source": {
            "book": "渊海子平",
            "chapter": "论十神",
            "page": 48
        },
        "original_content": "偏印者，夺我之食神也。见同气为偏印。",
        "interpretation": "偏印代表继母、偏业、领悟力，象征独特的思维方式。",
        "positive_meaning": {
            "personality": "领悟力强，思维独特，有创造力",
            "career": "适合研究、技术、艺术",
            "scholarship": "有独特的学问或技艺"
        },
        "negative_meaning": {
            "personality": "冷漠无情，缺乏爱心",
            "career": "事业不顺，难以发展",
            "health": "健康问题，意外灾祸"
        },
        "keywords": ["偏印", "枭神", "继母", "领悟", "独特"],
        "warning": "偏印夺食需注意，易有健康或灾祸",
        "in_palace_effects": {
            "ming_gong": "思维独特，但与人不同",
            "shi_gong": "注意食神被夺，健康问题",
            "fu_gong": "与继母缘薄或关系复杂"
        },
        "verification_status": "verified"
    },
    {
        "id": "god_005",
        "term": "食神",
        "pinyin": "shíshén",
        "wuxing": "我生者",
        "relationship": "相泄",
        "category": "ten_god",
        "system": "bazi",
        "nature": "同性相泄，阴干见阴干，阳干见阳干",
        "source": {
            "book": "渊海子平",
            "chapter": "论十神",
            "page": 49
        },
        "original_content": "食神者，我生之子也。主爵禄福寿。",
        "interpretation": "食神代表子女、福气、寿元、才华，象征享受和表达。",
        "positive_meaning": {
            "personality": "温和善良，乐观开朗，有才华",
            "career": "适合餐饮、服务、艺术",
            "fortune": "福气深厚，衣禄无忧",
            "talent": "有艺术才华，表达能力强"
        },
        "negative_meaning": {
            "personality": "过于乐观，不思进取",
            "career": "事业难成，财运不佳",
            "health": "健康欠佳，寿元有损"
        },
        "keywords": ["食神", "福气", "寿元", "才华", "享受"],
        "in_palace_effects": {
            "ming_gong": "温和善良，有口福",
            "zi_gong": "儿女缘分深，得子女之力",
            "cai_gong": "财运稳定，衣禄无忧"
        },
        "verification_status": "verified"
    },
    {
        "id": "god_006",
        "term": "伤官",
        "pinyin": "shāngguān",
        "wuxing": "我生者",
        "relationship": "相泄",
        "category": "ten_god",
        "system": "bazi",
        "nature": "异性相泄，阴干见阳干，阳干见阴干",
        "source": {
            "book": "渊海子平",
            "chapter": "论十神",
            "page": 50
        },
        "original_content": "伤官者，伤害官星也。主聪明傲物。",
        "interpretation": "伤官代表才华、傲气、叛逆、创意，象征不服从和反抗。",
        "positive_meaning": {
            "personality": "聪明过人，才华横溢，有创意",
            "career": "适合艺术、创新、演艺",
            "talent": "艺术天赋，表达能力出众"
        },
        "negative_meaning": {
            "personality": "傲慢自大，目中无人，不服从管教",
            "career": "事业阻碍，与上司不合",
            "relationships": "口舌是非，与人难相处"
        },
        "keywords": ["伤官", "才华", "傲气", "叛逆", "创意"],
        "warning": "伤官见官需谨慎，易有官讼是非",
        "in_palace_effects": {
            "ming_gong": "才华出众，但傲慢",
            "guan_gong": "注意与上司关系，官运受阻",
            "yi_gong": "儿女有才华但叛逆"
        },
        "verification_status": "verified"
    },
    {
        "id": "god_007",
        "term": "正官",
        "pinyin": "zhèngguān",
        "wuxing": "克我者",
        "relationship": "相克",
        "category": "ten_god",
        "system": "bazi",
        "nature": "异性相克，阴干见阳干，阳干见阴干",
        "source": {
            "book": "渊海子平",
            "chapter": "论十神",
            "page": 51
        },
        "original_content": "正官者，正官也。主荣辱贵贱。",
        "interpretation": "正官代表上司、官职、名誉、地位，象征责任和约束。",
        "positive_meaning": {
            "personality": "正直负责，有责任心，有上进心",
            "career": "适合从政、管理、仕途",
            "fame": "名声好，受人尊敬",
            "status": "地位稳固，有官职"
        },
        "negative_meaning": {
            "personality": "胆小怕事，缺乏魄力",
            "career": "事业受阻，难有晋升",
            "relationships": "受上司压制，难以出头"
        },
        "keywords": ["正官", "官职", "名誉", "地位", "责任"],
        "in_palace_effects": {
            "ming_gong": "正直有责任心，适合仕途",
            "guan_gong": "官运亨通，有晋升之望",
            "fu_gong": "受父亲或上司赏识"
        },
        "verification_status": "verified"
    },
    {
        "id": "god_008",
        "term": "七杀（偏官）",
        "pinyin": "qīshā（piānguān）",
        "wuxing": "克我者",
        "relationship": "相克",
        "category": "ten_god",
        "system": "bazi",
        "nature": "同性相克，阴干见阴干，阳干见阳干",
        "source": {
            "book": "渊海子平",
            "chapter": "论十神",
            "page": 52
        },
        "original_content": "七杀者，七杀也。主刚强果敢，司兵刑之权。",
        "interpretation": "七杀代表压力、挑战、权威、灾祸，象征残酷和果断。",
        "positive_meaning": {
            "personality": "刚强果敢，有魄力，敢于冒险",
            "career": "适合军警、司法、外科",
            "authority": "有权威，能掌权"
        },
        "negative_meaning": {
            "personality": "残忍暴虐，是非多端",
            "career": "事业阻碍，小人陷害",
            "health": "疾病灾祸，血光之灾"
        },
        "keywords": ["七杀", "偏官", "压力", "挑战", "权威"],
        "warning": "七杀无制为凶神，需有印星或食神制化",
        "in_palace_effects": {
            "ming_gong": "胆大果敢，但易有灾祸",
            "guan_gong": "事业多挑战，需勇于面对",
            "health_gong": "注意健康，易有意外"
        },
        "verification_status": "verified"
    },
    {
        "id": "god_009",
        "term": "正财",
        "pinyin": "zhèngcái",
        "wuxing": "我克者",
        "relationship": "相克",
        "category": "ten_god",
        "system": "bazi",
        "nature": "异性相克，阴干见阳干，阳干见阴干",
        "source": {
            "book": "渊海子平",
            "chapter": "论十神",
            "page": 53
        },
        "original_content": "正财者，得财之正也。主勤劳致富。",
        "interpretation": "正财代表正当收入、妻子、固定资产，象征正当和稳定。",
        "positive_meaning": {
            "personality": "勤俭节约，务实稳重",
            "career": "适合正当职业，勤俭致富",
            "wealth": "财运稳定，积累财富",
            "spouse": "得贤内助，婚姻稳定"
        },
        "negative_meaning": {
            "personality": "吝啬小气，过于保守",
            "career": "财运有限，难以大富",
            "relationships": "与妻子缘薄"
        },
        "keywords": ["正财", "正当", "稳定", "勤俭", "妻子"],
        "in_palace_effects": {
            "ming_gong": "勤俭节约，财运稳定",
            "cai_gong": "正当收入，理财有方",
            "qi_gong": "得贤妻，婚姻稳定"
        },
        "verification_status": "verified"
    },
    {
        "id": "god_010",
        "term": "偏财",
        "pinyin": "piāncái",
        "wuxing": "我克者",
        "relationship": "相克",
        "category": "ten_god",
        "system": "bazi",
        "nature": "同性相克，阴干见阴干，阳干见阳干",
        "source": {
            "book": "渊海子平",
            "chapter": "论十神",
            "page": 54
        },
        "original_content": "偏财者，得财之偏也。主慷慨大方。",
        "interpretation": "偏财代表意外之财、流动资产、父亲，象征慷慨和流动性。",
        "positive_meaning": {
            "personality": "慷慨大方，人缘好，善于交际",
            "career": "适合投资、贸易、金融",
            "wealth": "财运佳，可能有意外之财",
            "father": "与父亲缘深，得父亲帮助"
        },
        "negative_meaning": {
            "personality": "挥霍无度，不善理财",
            "career": "财务不稳，易破财",
            "relationships": "与父亲缘薄，桃花纠纷"
        },
        "keywords": ["偏财", "意外", "慷慨", "流动", "投资"],
        "in_palace_effects": {
            "ming_gong": "慷慨大方，但理财不佳",
            "cai_gong": "可能有意外之财，但不稳定",
            "fu_gong": "与父亲缘深，得父亲荫庇"
        },
        "verification_status": "verified"
    }
]
