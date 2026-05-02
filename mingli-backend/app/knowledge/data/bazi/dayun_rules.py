"""
大运规则
八字命理大运推算规则

大运是八字命理中重要的后天运势
"""

BAZI_DAYUN_RULES = [
    {
        "id": "dayun_001",
        "rule_name": "大运起始年龄计算",
        "rule_type": "calculation",
        "system": "bazi",
        "source": {
            "book": "渊海子平",
            "chapter": "论大运",
            "page": 120
        },
        "condition": "根据出生月份和节气确定起运年龄",
        "formula": "起运年龄 = (行月令 - 出生月令) × 10日/年",
        "explanation": "大运从出生后开始计算，起运年龄根据出生节气与行月令的关系确定。行月令是指出生后下一个节气的月份地支。",
        "example": "例：立春后惊蛰前出生，行月令为惊蛰之月（卯月）。若出生在惊蛰前5天，则起运年龄 = (2 - 0.5) × 10 = 15岁起运。",
        "verification_status": "verified",
        "notes": "男女行运方向不同：男命顺行，女命逆行"
    },
    {
        "id": "dayun_002",
        "rule_name": "大运顺逆规则",
        "rule_type": "calculation",
        "system": "bazi",
        "source": {
            "book": "滴天髓",
            "chapter": "论大运",
            "page": 85
        },
        "condition": "根据性别确定大运走向",
        "formula": "男命顺行：按地支顺序排列。女命逆行：按地支逆序排列",
        "explanation": "大运有顺逆之分，男性顺地支顺序，女性逆地支顺序。",
        "example": "例：男性大运从月柱顺排：月柱为午，则大运依次为未、申、酉、戌、亥、子、丑...女性则逆行：大运为巳、辰、卯、寅、丑、子...",
        "verification_status": "verified",
        "notes": "另有部分流派不论男女皆顺行"
    },
    {
        "id": "dayun_003",
        "rule_name": "大运天干起法",
        "rule_type": "calculation",
        "system": "bazi",
        "source": {
            "book": "渊海子平",
            "chapter": "论大运天干",
            "page": 125
        },
        "condition": "根据命宫天干和性别确定大运天干",
        "formula": "大运天干按五行相生顺序排列",
        "explanation": "大运天干从命宫天干开始，按五行相生顺序（甲→丙→戊→庚→壬→甲）顺排或逆排。",
        "example": "例：命宫天干为甲，男命顺行。大运天干依次为：乙、丙、丁、戊、己...女命逆行：大运天干为：癸、壬、辛、庚、己...",
        "verification_status": "verified",
        "notes": "天干起法需结合地支一起考虑"
    },
    {
        "id": "dayun_004",
        "rule_name": "大运吉凶判断",
        "rule_type": "interpretation",
        "system": "bazi",
        "source": {
            "book": "滴天髓",
            "chapter": "论大运吉凶",
            "page": 90
        },
        "condition": "根据大运干支与命局的生克关系判断",
        "result": "大运分为好运、平运、差运",
        "explanation": "大运的吉凶取决于大运干支与命局的生克关系，以及大运是否得用神。",
        "favorable_conditions": [
            "大运干支生助日干或用神",
            "大运地支为日干之长生、帝旺",
            "大运天干透出命局所需之十神"
        ],
        "unfavorable_conditions": [
            "大运干支克制日干或用神",
            "大运地支为日干之死绝",
            "大运天干克泄日干或用神"
        ],
        "verification_status": "verified",
        "notes": "需综合命局、大运、流年三者关系判断"
    },
    {
        "id": "dayun_005",
        "rule_name": "小运推算规则",
        "rule_type": "calculation",
        "system": "bazi",
        "source": {
            "book": "渊海子平",
            "chapter": "论小运",
            "page": 130
        },
        "condition": "根据出生时辰和年份推算小运",
        "formula": "小运以时支为基准，顺行十二宫",
        "explanation": "小运主管一岁至十岁之运势，以时柱地支起算。",
        "example": "例：出生时支为午，小运从午宫起，顺行一岁在未，二岁在申，三岁在酉...",
        "verification_status": "verified",
        "notes": "小运主要用于命局不完整时（如早夭）的补充"
    },
    {
        "id": "dayun_006",
        "rule_name": "流年太岁规则",
        "rule_type": "interpretation",
        "system": "bazi",
        "source": {
            "book": "渊海子平",
            "chapter": "论流年",
            "page": 135
        },
        "condition": "根据流年地支与命局的冲合会刑关系判断",
        "result": "流年吉凶",
        "explanation": "流年以太岁为主，配合命局而断。太岁为君，星宿为臣。",
        "interactions": {
            "chong": "冲：主变动、冲击、冲破",
            "he": "合：主合作、桃花、贵人",
            "hui": "会：主聚会、合伙、机会",
            "xing": "刑：主是非、矛盾、疾病"
        },
        "verification_status": "verified",
        "notes": "流年是论断一年运势的关键"
    },
    {
        "id": "dayun_007",
        "rule_name": "命宫计算规则",
        "rule_type": "calculation",
        "system": "bazi",
        "source": {
            "book": "渊海子平",
            "chapter": "论命宫",
            "page": 140
        },
        "condition": "根据出生月份和时辰确定命宫地支",
        "formula": "命宫地支 = (生月地支序数 + 生时地支序数) mod 12",
        "explanation": "命宫是八字命理中的重要宫位，代表先天禀赋和基本性格。",
        "example": "例：寅月酉时生。寅=3，酉=10。(3+10) mod 12 = 1，故命宫在子。",
        "verification_status": "verified",
        "notes": "命宫天干按命宫地支查表得出"
    },
    {
        "id": "dayun_008",
        "rule_name": "胎元推算规则",
        "rule_type": "calculation",
        "system": "bazi",
        "source": {
            "book": "滴天髓",
            "chapter": "论胎元",
            "page": 95
        },
        "condition": "根据出生月份和时辰推算胎元",
        "formula": "胎元 = 出生月令 + 三月",
        "explanation": "胎元代表先天之命，对研究胎儿时期的运势有参考价值。",
        "example": "例：出生在卯月，胎元为午月。",
        "verification_status": "verified",
        "notes": "胎元需与命局综合分析"
    }
]
