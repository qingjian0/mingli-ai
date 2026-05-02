"""
宫位含义
紫微斗数十二宫位的详细解释

十二宫包括：命宫、兄弟宫、夫妻宫、子女宫、财帛宫、疾厄宫、
迁移宫、奴仆宫、官禄宫、田宅宫、福德宫、父母宫
"""

ZIWEI_PALACES = [
    {
        "id": "palace_001",
        "term": "命宫",
        "pinyin": "mìnggōng",
        "position": 1,
        "category": "core_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·宫位总论",
            "page": 28
        },
        "original_content": "命宫为立命之宫，主一生之祸福吉凶。",
        "interpretation": "命宫是紫微斗数中最重要的宫位，代表个人的基本性格、命运走向和人生格局。",
        "scope": "性格特点、命运走向、人生格局、整体运势",
        "aspects": {
            "personality": "基本性格特征和行为模式",
            "destiny": "命运主要发展趋势",
            "overall": "一生整体运势"
        },
        "keywords": ["性格", "命运", "一生", "祸福", "吉凶"],
        "related_palaces": ["身宫", "福德宫", "父母宫"],
        "notes": "命宫好则一生顺遂，命宫差则波折较多",
        "verification_status": "verified"
    },
    {
        "id": "palace_002",
        "term": "兄弟宫",
        "pinyin": "xiōngdìgōng",
        "position": 2,
        "category": "support_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·宫位总论",
            "page": 30
        },
        "original_content": "兄弟宫主兄弟姐妹之缘，及平辈知交之情。",
        "interpretation": "兄弟宫代表与兄弟姐妹的关系，以及平辈朋友、同事间的人际关系。",
        "scope": "兄弟姐妹关系、平辈人际、合作关系",
        "aspects": {
            "siblings": "与兄弟姐妹的关系",
            "peers": "平辈朋友关系",
            "cooperation": "合作关系和助力"
        },
        "keywords": ["兄弟", "姐妹", "平辈", "合作", "人际"],
        "related_palaces": ["命宫", "奴仆宫", "交友宫"],
        "notes": "兄弟宫吉则兄弟姐妹和睦，得兄弟助力",
        "verification_status": "verified"
    },
    {
        "id": "palace_003",
        "term": "夫妻宫",
        "pinyin": "fūqīgōng",
        "position": 3,
        "category": "relationship_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·宫位总论",
            "page": 32
        },
        "original_content": "夫妻宫主婚姻配偶之缘，及异性情缘之事。",
        "interpretation": "夫妻宫代表婚姻和配偶缘分，以及与异性之间的关系。",
        "scope": "婚姻状况、配偶特征、异性缘分、桃花运",
        "aspects": {
            "marriage": "婚姻状况和配偶特征",
            "spouse": "配偶的个性和能力",
            "romance": "异性缘分和桃花运"
        },
        "keywords": ["婚姻", "配偶", "异性", "情缘", "桃花"],
        "related_palaces": ["子女宫", "福德宫", "命宫"],
        "notes": "夫妻宫吉则婚姻美满，夫妻情深",
        "verification_status": "verified"
    },
    {
        "id": "palace_004",
        "term": "子女宫",
        "pinyin": "zǐnǚgōng",
        "position": 4,
        "category": "descendant_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·宫位总论",
            "page": 34
        },
        "original_content": "子女宫主子女之缘，及晚辈后人之情。",
        "interpretation": "子女宫代表与子女的缘分，以及晚辈、学生等人的关系。",
        "scope": "子女缘分、晚辈关系、后代情况",
        "aspects": {
            "children": "子女的数量和缘分",
            "descendants": "后代发展情况",
            "younger": "与晚辈、学生关系"
        },
        "keywords": ["子女", "后代", "晚辈", "缘分"],
        "related_palaces": ["夫妻宫", "田宅宫", "福德宫"],
        "notes": "子女宫吉则儿女成材，晚年有靠",
        "verification_status": "verified"
    },
    {
        "id": "palace_005",
        "term": "财帛宫",
        "pinyin": "cáibógōng",
        "position": 5,
        "category": "wealth_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·宫位总论",
            "page": 36
        },
        "original_content": "财帛宫主财禄之源，及理财之能。",
        "interpretation": "财帛宫代表财运和理财能力，以及收入的来源和方式。",
        "scope": "财运状况、理财能力、收入来源、物质生活",
        "aspects": {
            "fortune": "整体财运状况",
            "money_manage": "理财能力和态度",
            "income": "主要收入来源",
            "material": "物质生活水平"
        },
        "keywords": ["财禄", "财运", "理财", "收入", "物质"],
        "related_palaces": ["命宫", "福德宫", "田宅宫"],
        "notes": "财帛宫吉则财运亨通，善于理财",
        "verification_status": "verified"
    },
    {
        "id": "palace_006",
        "term": "疾厄宫",
        "pinyin": "jí'èrgōng",
        "position": 6,
        "category": "health_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·宫位总论",
            "page": 38
        },
        "original_content": "疾厄宫主疾病灾厄之患，及身体健康之情。",
        "interpretation": "疾厄宫代表健康状况和容易发生的疾病，以及灾厄情况。",
        "scope": "健康状况、疾病倾向、意外灾厄、体质",
        "aspects": {
            "health": "整体健康状况",
            "diseases": "易患疾病类型",
            "accidents": "意外灾厄倾向",
            "constitution": "先天体质"
        },
        "keywords": ["疾病", "灾厄", "健康", "体质", "意外"],
        "related_palaces": ["命宫", "父母宫", "迁移宫"],
        "notes": "疾厄宫须结合星曜综合判断疾病情况",
        "verification_status": "verified"
    },
    {
        "id": "palace_007",
        "term": "迁移宫",
        "pinyin": "qiānyígōng",
        "position": 7,
        "category": "movement_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·宫位总论",
            "page": 40
        },
        "original_content": "迁移宫主迁徒远行之缘，及在外之祸福。",
        "interpretation": "迁移宫代表外出、迁移、远行的情况，以及在外的际遇。",
        "scope": "外出发展、迁移运势、在外际遇、旅行",
        "aspects": {
            "travel": "外出发展和迁移",
            "outside": "在外地的发展情况",
            "fortune": "外出运势",
            "journey": "旅行运"
        },
        "keywords": ["迁移", "远行", "在外", "旅行", "际遇"],
        "related_palaces": ["命宫", "官禄宫", "财帛宫"],
        "notes": "迁移宫吉则外出发展顺利，得贵人相助",
        "verification_status": "verified"
    },
    {
        "id": "palace_008",
        "term": "奴仆宫",
        "pinyin": "núpúgōng",
        "position": 8,
        "category": "servant_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·宫位总论",
            "page": 42
        },
        "original_content": "奴仆宫主仆役臣妾之辈，及下属晚辈之情。",
        "interpretation": "奴仆宫代表与下属、员工、仆从的关系，以及与晚辈的缘分。",
        "scope": "下属关系、员工缘分、晚辈关系、仆从",
        "aspects": {
            "subordinates": "与下属员工关系",
            "servants": "仆役缘分",
            "younger_gen": "晚辈关系"
        },
        "keywords": ["奴仆", "下属", "员工", "晚辈"],
        "related_palaces": ["命宫", "兄弟宫", "官禄宫"],
        "notes": "奴仆宫吉则得下属助力，管理有方",
        "verification_status": "verified"
    },
    {
        "id": "palace_009",
        "term": "官禄宫",
        "pinyin": "guānlùgōng",
        "position": 9,
        "category": "career_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·宫位总论",
            "page": 44
        },
        "original_content": "官禄宫主仕途功名之业，及事业成就之事。",
        "interpretation": "官禄宫代表事业、仕途和功名成就，是最重要的职业宫位。",
        "scope": "事业发展、仕途功名、职业选择、工作运势",
        "aspects": {
            "career": "事业发展状况",
            "official": "仕途和官运",
            "achievement": "成就和地位",
            "work": "工作运势"
        },
        "keywords": ["官禄", "仕途", "功名", "事业", "成就"],
        "related_palaces": ["命宫", "财帛宫", "迁移宫"],
        "notes": "官禄宫吉则事业发达，仕途顺遂",
        "verification_status": "verified"
    },
    {
        "id": "palace_010",
        "term": "田宅宫",
        "pinyin": "tiánzhàigōng",
        "position": 10,
        "category": "property_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·宫位总论",
            "page": 46
        },
        "original_content": "田宅宫主田园家宅之业，及不动产业之情。",
        "interpretation": "田宅宫代表房产、土地等不动产，以及家庭和祖业情况。",
        "scope": "房产运势、家宅情况、祖业传承、不动产",
        "aspects": {
            "property": "房产和土地运势",
            "home": "家宅状况",
            "ancestors": "祖业传承情况",
            "estate": "不动产多少"
        },
        "keywords": ["田宅", "房产", "家宅", "祖业", "不动产"],
        "related_palaces": ["命宫", "子女宫", "福德宫"],
        "notes": "田宅宫吉则房产丰富，家宅安宁",
        "verification_status": "verified"
    },
    {
        "id": "palace_011",
        "term": "福德宫",
        "pinyin": "fúdé_gōng",
        "position": 11,
        "category": "fortune_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·宫位总论",
            "page": 48
        },
        "original_content": "福德宫主福禄寿考之德，及精神享受之情。",
        "interpretation": "福德宫代表福气、寿命和精神享受，是反映生活质量的重要宫位。",
        "scope": "福气状况、精神生活、寿命、享受",
        "aspects": {
            "fortune": "福气多少",
            "spirit": "精神生活品质",
            "longevity": "寿命状况",
            "enjoyment": "享受层次"
        },
        "keywords": ["福德", "福气", "寿考", "精神", "享受"],
        "related_palaces": ["命宫", "田宅宫", "财帛宫"],
        "notes": "福德宫吉则福泽深厚，晚年享福",
        "verification_status": "verified"
    },
    {
        "id": "palace_012",
        "term": "父母宫",
        "pinyin": "fùmǔgōng",
        "position": 12,
        "category": "parent_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·宫位总论",
            "page": 50
        },
        "original_content": "父母宫主父母高堂之缘，及上司长辈之情。",
        "interpretation": "父母宫代表与父母的关系，以及与上司、长辈、师长的缘分。",
        "scope": "父母关系、长辈缘分、上司关系、师长",
        "aspects": {
            "parents": "与父母的关系",
            "elders": "与长辈的缘分",
            "superiors": "与上司关系",
            "teachers": "与师长缘分"
        },
        "keywords": ["父母", "长辈", "上司", "师长", "缘份"],
        "related_palaces": ["命宫", "福德宫", "迁移宫"],
        "notes": "父母宫吉则受父母荫庇，得长辈提携",
        "verification_status": "verified"
    }
]

SPECIAL_PALACES = [
    {
        "id": "special_001",
        "term": "身宫",
        "pinyin": "shēngōng",
        "category": "special_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·身宫论",
            "page": 52
        },
        "original_content": "身宫居命宫之对冲，主后天之身及后天的际遇。",
        "interpretation": "身宫代表后天之身，与命宫相距四宫，主管后天的努力和际遇。",
        "scope": "后天际遇、个人努力、行为模式",
        "notes": "身宫与命宫需综合分析，命宫为先天，身宫为后天",
        "verification_status": "verified"
    },
    {
        "id": "special_002",
        "term": "相貌宫",
        "pinyin": "xiàngmàogōng",
        "category": "special_palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·相貌论",
            "page": 54
        },
        "original_content": "相貌宫主相貌之形，父母之遗。",
        "interpretation": "相貌宫代表外在相貌和形体特征，承继于父母。",
        "scope": "相貌特征、体形外貌、遗传特质",
        "notes": "相貌宫与父母宫同宫，相貌受父母遗传影响大",
        "verification_status": "verified"
    }
]
