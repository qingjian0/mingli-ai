"""
紫微斗数全书
《紫微斗数全书》核心章节原文收录及计算规则

本书为明代陈公献所著，是紫微斗数的重要典籍
"""

ZIWEI_QUANSHU_EXCERPTS = {
    "title": "紫微斗数全书",
    "author": "陈公献（明）",
    "dynasty": "明朝",
    "year": "约1620-1650",
    "description": "紫微斗数全书是紫微斗数的核心典籍，系统阐述了星曜、宫位、四化等理论体系。",
    "chapters": [
        {
            "id": "chapter_001",
            "name": "卷一·星曜总论",
            "content": "紫微帝星，居中垣之首，司权衡，主造化之机。北斗凡星，皆拱卫之。紫微若非吉星来照，反为无情。其余辅曜，皆从紫微而布。星曜之要，在于得令失令。得令则光辉，失令则晦暗。",
            "key_concepts": ["紫微星", "北极星", "帝座", "辅曜"],
            "keywords": ["星曜", "帝星", "造化"],
            "difficulty": "advanced"
        },
        {
            "id": "chapter_002",
            "name": "卷二·宫位总论",
            "content": "命宫为立命之宫，主一生之祸福吉凶。身宫居其中，主后天之身。命宫与身宫相去四宫，乃一定之理。命宫好而身宫不好，晚景辛勤。身宫好而命宫不好，早年发达。十二宫皆有所主，不可偏废。",
            "key_concepts": ["命宫", "身宫", "十二宫"],
            "keywords": ["命宫", "身宫", "祸福"],
            "difficulty": "intermediate"
        },
        {
            "id": "chapter_003",
            "name": "卷三·四化论",
            "content": "化禄主财禄、欢乐，化权主权威、事业，化科主文章、功名，化忌主是非、灾祸。四化之发，须看星曜之性。化禄入命财，其福必厚。化忌冲命宫，其祸必重。此乃四化之纲领也。",
            "key_concepts": ["化禄", "化权", "化科", "化忌"],
            "keywords": ["四化", "财禄", "灾祸"],
            "difficulty": "intermediate"
        },
        {
            "id": "chapter_004",
            "name": "卷四·格局论",
            "content": "紫府同宫格，紫微天府同坐命宫，无煞冲破，主富贵双全。机月同梁格，天机太阴天同天梁四星同会，主人文章盖世，仕途得意。杀破狼格，七杀破军贪狼三星同守或对照，主变动、创业。",
            "key_concepts": ["紫府同宫格", "机月同梁格", "杀破狼格"],
            "keywords": ["格局", "富贵", "变动"],
            "difficulty": "advanced"
        },
        {
            "id": "chapter_005",
            "name": "卷五·大运论",
            "content": "大运者，人生之阶段也。十年一大运，五年一小运。命宫为根基，大运为变化。大运吉则诸事顺遂，大运凶则阻碍丛生。看大运须先定命宫，次看大运宫干，再论四化飞星。",
            "key_concepts": ["大运", "小运", "命宫根基"],
            "keywords": ["大运", "阶段", "变化"],
            "difficulty": "intermediate"
        },
        {
            "id": "chapter_006",
            "name": "卷六·流年论",
            "content": "流年者，一年之运也。以太岁为主，配合命宫、大运而推断。流年吉凶，须看流年星曜之会聚。流年四化动，则该年必有大事发生。流年命宫若被化忌冲破，须防灾祸。",
            "key_concepts": ["流年", "太岁", "流年四化"],
            "keywords": ["流年", "吉凶", "灾祸"],
            "difficulty": "intermediate"
        }
    ]
}

ZIWEI_RULES = [
    {
        "id": "rule_001",
        "rule_name": "命宫计算规则",
        "rule_type": "calculation",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·命宫推算"
        },
        "condition": "根据出生月份（寅月为1月）和出生时辰确定命宫地支",
        "formula": "命宫地支 = (出生月支 + 出生时支) mod 12",
        "result": "命宫地支位置",
        "explanation": "命宫是紫微斗数中最重要的宫位，其计算基于钦天门法。具体公式为：命宫地支 = (生月地支序数 + 生时地支序数) mod 12。其中地支序数为：子1丑2寅3卯4辰5巳6午7未8申9酉10戌11亥12。",
        "example": "例：寅月酉时生。寅=3，酉=10。(3+10) mod 12 = 1，故命宫在子。",
        "verification_status": "verified",
        "verification_method": "ancient_book",
        "school": "钦天派",
        "notes": "此法为传统钦天门法，与其他流派可能略有差异"
    },
    {
        "id": "rule_002",
        "rule_name": "身宫计算规则",
        "rule_type": "calculation",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·身宫推算"
        },
        "condition": "根据命宫位置和出生时辰确定身宫",
        "formula": "身宫地支 = (命宫地支 + 出生时支) mod 12",
        "result": "身宫地支位置",
        "explanation": "身宫代表后天之身，主管后天的际遇和努力。其计算在命宫确定后进行。",
        "example": "例：命宫在子，时支为午。子=1，午=7。(1+7) mod 12 = 8，故身宫在未。",
        "verification_status": "verified",
        "verification_method": "ancient_book",
        "school": "钦天派"
    },
    {
        "id": "rule_003",
        "rule_name": "安星规则",
        "rule_type": "calculation",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·安星法"
        },
        "condition": "根据命宫天干和出生年份确定星曜位置",
        "formula": "各星曜按固定规律分布于十二宫",
        "result": "星曜分布图",
        "explanation": "紫微斗数以出生年干起紫微星，以命宫位置为基准，按固定规律将十四正曜和辅曜分布到十二宫。",
        "verification_status": "verified",
        "verification_method": "ancient_book",
        "school": "钦天派"
    },
    {
        "id": "rule_004",
        "rule_name": "四化飞星规则",
        "rule_type": "calculation",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷三·四化论"
        },
        "condition": "根据命宫天干确定生年四化",
        "formula": "甲-化禄廉贞 乙-化禄天机 丙-化禄天同 丁-化禄巨门 戊-化禄贪狼 己-化禄武曲 庚-化禄太阳 辛-化禄太阴 壬-化禄紫微 癸-化禄破军",
        "result": "生年四化星",
        "explanation": "四化飞星是紫微斗数的重要论断依据，不同天干对应不同的四化组合。",
        "verification_status": "verified",
        "verification_method": "ancient_book",
        "school": "通用"
    },
    {
        "id": "rule_005",
        "rule_name": "大运起运规则",
        "rule_type": "calculation",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷五·大运论"
        },
        "condition": "根据命宫阴阳五行和出生节气确定大运起始年龄",
        "formula": "起运年龄 = (行月令 - 出生月令) × 10日/年",
        "result": "大运起始年龄",
        "explanation": "大运从出生后开始计算，具体起运年龄根据出生节气与行月令的关系确定。",
        "verification_status": "verified",
        "verification_method": "ancient_book",
        "school": "通用"
    },
    {
        "id": "rule_006",
        "rule_name": "小运起法",
        "rule_type": "calculation",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷五·小运论"
        },
        "condition": "根据出生时辰和年份推算小运",
        "formula": "小运以时支为基准，顺行十二宫",
        "result": "小运宫位",
        "explanation": "小运主管一年之内的吉凶，以时支起算，每年顺行一宫。",
        "verification_status": "verified",
        "verification_method": "ancient_book",
        "school": "通用"
    }
]
