"""
八字格局知识库
源自《渊海子平》《滴天髓》《穷通宝鉴》《子平真诠》

格局分类：
- 正格（普通格局）：月支本气透出天干
- 变格（特殊格局）：日主从势或专旺
- 杂格：介于正格与变格之间
"""

ZHENG_GE = [
    {
        "id": "zg_001",
        "name": "正官格",
        "pinyin": "zhèngguān gé",
        "formation": "月支本气为正官，天干透出或旺于月令",
        "conditions": [
            "月令本气为正官星",
            "正官星得令且透出天干",
            "日主身强能任官星",
            "官星无伤官克破"
        ],
        "characteristics": [
            "为人正直有责任心",
            "做事规规矩矩",
            "适合公职、管理工作",
            "名声地位较好"
        ],
        "career_suggestions": [
            "政府机关",
            "企业管理",
            "教育行业"
        ],
        "good_combinations": [
            "财官相生（财星生官）",
            "官印相生（印星护官）",
            "官星清透不杂"
        ],
        "bad_combinations": [
            "伤官见官（伤官克正官）",
            "官多化鬼（官星太重为忌）",
            "日主太弱难以任官"
        ],
        "source": {
            "book": "渊海子平",
            "chapter": "论正官格",
            "original": "正官者，乃甲见辛、乙见庚之类也。甲乙日生，四柱中见辛酉之金则为官星。"
        },
        "interpretation": "正官为十神之首，代表约束、责任、地位。格局纯正者，贵气十足。"
    },
    {
        "id": "zg_002",
        "name": "七杀格",
        "pinyin": "qīshā gé",
        "formation": "月支本气为七杀，天干透出或旺于月令",
        "conditions": [
            "月令本气为七杀星",
            "七杀星得令且透出天干",
            "身强能抗七杀",
            "或有印星、食神制化"
        ],
        "characteristics": [
            "做事果断有魄力",
            "敢于冒险竞争",
            "领导能力强",
            "有开拓精神"
        ],
        "career_suggestions": [
            "军警司法",
            "企业决策",
            "体育竞技"
        ],
        "good_combinations": [
            "杀印相生（印星化杀生身）",
            "羊刃驾杀（羊刃抗杀）",
            "食神制杀（食神克制七杀）",
            "杀旺身强"
        ],
        "bad_combinations": [
            "杀重身轻（无力抗杀）",
            "财杀相生（财星助杀）",
            "杀无制约"
        ],
        "source": {
            "book": "渊海子平",
            "chapter": "论七杀",
            "original": "七杀者，乃甲见庚、乙见辛之类也。其性刚强，主兵刑之权。"
        },
        "interpretation": "七杀为凶神，代表压力、竞争、挑战。制化得宜者，可成大器。"
    },
    {
        "id": "zg_003",
        "name": "正财格",
        "pinyin": "zhèngcái gé",
        "formation": "月支本气为正财，天干透出或旺于月令",
        "conditions": [
            "月令本气为正财星",
            "正财星得令且透出天干",
            "日主身强能任财星",
            "财星无劫财克破"
        ],
        "characteristics": [
            "勤俭节约",
            "务实稳重",
            "理财有方",
            "重视正当收入"
        ],
        "career_suggestions": [
            "财务会计",
            "正当贸易",
            "稳定职业"
        ],
        "good_combinations": [
            "财官相生",
            "身财两停",
            "食伤生财"
        ],
        "bad_combinations": [
            "比劫夺财",
            "身弱财旺",
            "财多身弱"
        ],
        "source": {
            "book": "渊海子平",
            "chapter": "论正财",
            "original": "正财者，甲见乙木为正财，乙木为甲之正财也。"
        },
        "interpretation": "正财代表正当收入和物质享受，格局纯正者，财运稳定。"
    },
    {
        "id": "zg_004",
        "name": "偏财格",
        "pinyin": "piāncái gé",
        "formation": "月支本气为偏财，天干透出或旺于月令",
        "conditions": [
            "月令本气为偏财星",
            "偏财星得令且透出天干",
            "日主身强能任偏财",
            "偏财无劫财克破"
        ],
        "characteristics": [
            "慷慨大方",
            "善于交际",
            "人缘极佳",
            "敢于投资"
        ],
        "career_suggestions": [
            "投资理财",
            "商业贸易",
            "风险投资"
        ],
        "good_combinations": [
            "身财两旺",
            "食伤生财",
            "财旺生官"
        ],
        "bad_combinations": [
            "比劫夺财",
            "身弱财旺",
            "财星无护"
        ],
        "source": {
            "book": "渊海子平",
            "chapter": "论偏财",
            "original": "偏财者，甲见戊土为偏财，戊土为甲之偏财也。"
        },
        "interpretation": "偏财代表流动资产和意外之财，善于经营者可获厚利。"
    },
    {
        "id": "zg_005",
        "name": "正印格",
        "pinyin": "zhèngyìn gé",
        "formation": "月支本气为正印，天干透出或旺于月令",
        "conditions": [
            "月令本气为正印星",
            "正印星得令且透出天干",
            "日主身弱有印扶身",
            "印星无财星克破"
        ],
        "characteristics": [
            "仁慈善良",
            "有爱心耐心",
            "学业优秀",
            "受人尊敬"
        ],
        "career_suggestions": [
            "教育培训",
            "文化学术",
            "医疗福利"
        ],
        "good_combinations": [
            "官印相生",
            "杀印相生",
            "印星清透"
        ],
        "bad_combinations": [
            "财星破印",
            "印多成枭",
            "身强印旺"
        ],
        "source": {
            "book": "渊海子平",
            "chapter": "论正印",
            "original": "正印者，乃甲见癸、乙见壬之类也。印乃护身之母。"
        },
        "interpretation": "正印代表学业、名声、长辈扶助，印星得用者多才多艺。"
    },
    {
        "id": "zg_006",
        "name": "偏印格",
        "pinyin": "piānyìn gé",
        "formation": "月支本气为偏印，天干透出或旺于月令",
        "conditions": [
            "月令本气为偏印星",
            "偏印星得令且透出天干",
            "日主身弱有偏印扶身",
            "偏印无财星克破"
        ],
        "characteristics": [
            "领悟力强",
            "思维独特",
            "有创造力",
            "独立性强"
        ],
        "career_suggestions": [
            "研究技术",
            "艺术创作",
            "特殊技艺"
        ],
        "good_combinations": [
            "杀印相生",
            "偏印化杀",
            "身弱有偏印"
        ],
        "bad_combinations": [
            "偏印夺食（偏印克制食神）",
            "财星破印",
            "印多无制"
        ],
        "source": {
            "book": "渊海子平",
            "chapter": "论偏印",
            "original": "偏印者，又名枭神。甲见壬、乙见癸是也。"
        },
        "interpretation": "偏印代表偏门学术和独特技艺，善用者可成一技之长。"
    },
    {
        "id": "zg_007",
        "name": "食神格",
        "pinyin": "shíshén gé",
        "formation": "月支本气为食神，天干透出或旺于月令",
        "conditions": [
            "月令本气为食神星",
            "食神星得令且透出天干",
            "日主身强能任食神",
            "食神无偏印克破"
        ],
        "characteristics": [
            "温和善良",
            "乐观开朗",
            "有口福福气",
            "才华出众"
        ],
        "career_suggestions": [
            "餐饮服务",
            "艺术表演",
            "教育培训"
        ],
        "good_combinations": [
            "食神生财",
            "食神制杀",
            "食神吐秀"
        ],
        "bad_combinations": [
            "偏印夺食",
            "食多伤身",
            "身弱食旺"
        ],
        "source": {
            "book": "渊海子平",
            "chapter": "论食神",
            "original": "食神者，甲见丙火是也。主爵禄福寿。"
        },
        "interpretation": "食神代表福气、才华、寿元，格局纯正者福寿双全。"
    },
    {
        "id": "zg_008",
        "name": "伤官格",
        "pinyin": "shāngguān gé",
        "formation": "月支本气为伤官，天干透出或旺于月令",
        "conditions": [
            "月令本气为伤官星",
            "伤官星得令且透出天干",
            "日主身强能任伤官",
            "伤官无印星克破"
        ],
        "characteristics": [
            "聪明过人",
            "才华横溢",
            "敢于创新",
            "表现欲强"
        ],
        "career_suggestions": [
            "艺术创作",
            "演艺表演",
            "自由职业"
        ],
        "good_combinations": [
            "伤官配印",
            "伤官生财",
            "伤官驾杀"
        ],
        "bad_combinations": [
            "伤官见官",
            "伤官无制",
            "身弱伤旺"
        ],
        "source": {
            "book": "渊海子平",
            "chapter": "论伤官",
            "original": "伤官者，甲见丁火是也。伤官伤尽最为奇。"
        },
        "interpretation": "伤官代表才华、傲气、叛逆，伤官伤尽者可成大器。"
    }
]

BIAN_GE = [
    {
        "id": "bg_001",
        "name": "从杀格",
        "pinyin": "cóngshā gé",
        "formation": "日主极弱无气，官杀强旺得势",
        "conditions": [
            "日主无根无气",
            "官杀得令且众多",
            "无印比扶身",
            "全局官杀独旺"
        ],
        "characteristics": [
            "事业心重",
            "敢于拼搏",
            "意志坚强",
            "易有成就"
        ],
        "career_suggestions": [
            "军警执法",
            "企业管理",
            "创业发展"
        ],
        "notes": "从杀格从其官杀旺势，在事业上易有突破，但需防压力过大。",
        "source": {
            "book": "子平真诠",
            "chapter": "论从杀格",
            "original": "日主无气，弃命从杀，当看杀之形势。"
        },
        "interpretation": "从杀格者，从其旺势，利于功名事业，但压力亦大。"
    },
    {
        "id": "bg_002",
        "name": "从财格",
        "pinyin": "cóngcái gé",
        "formation": "日主极弱无气，财星强旺得势",
        "conditions": [
            "日主无根无气",
            "财星得令且众多",
            "无印比扶身",
            "全局财星独旺"
        ],
        "characteristics": [
            "财运极佳",
            "善于理财",
            "物质丰富",
            "务实肯干"
        ],
        "career_suggestions": [
            "财务管理",
            "投资贸易",
            "商业经营"
        ],
        "notes": "从财格者财来财去，宜从事财务相关工作或经营商业。",
        "source": {
            "book": "渊海子平",
            "chapter": "论从财",
            "original": "日主无气，弃命从财，财旺者富。"
        },
        "interpretation": "从财格者，善于理财，财运亨通，但需防破耗。"
    },
    {
        "id": "bg_003",
        "name": "从儿格",
        "pinyin": "cóng'ér gé",
        "formation": "日主极弱无气，食伤强旺得势",
        "conditions": [
            "日主无根无气",
            "食伤得令且众多",
            "无印比扶身",
            "全局食伤独旺"
        ],
        "characteristics": [
            "才华横溢",
            "聪明过人",
            "善于表达",
            "艺术天赋"
        ],
        "career_suggestions": [
            "艺术表演",
            "教育培训",
            "创意产业"
        ],
        "notes": "从儿格者伤食泄秀，才华出众，宜从事发挥才华的行业。",
        "source": {
            "book": "子平真诠",
            "chapter": "论从儿格",
            "original": "日主无气，弃命从儿，伤食得势。"
        },
        "interpretation": "从儿格者，才华得以发挥，名利双收。"
    },
    {
        "id": "bg_004",
        "name": "从印格",
        "pinyin": "cóngyìn gé",
        "formation": "日主极弱无气，印星强旺得势",
        "conditions": [
            "日主无根无气",
            "印星得令且众多",
            "无财星克印",
            "全局印星独旺"
        ],
        "characteristics": [
            "学业优秀",
            "名声在外",
            "得长辈助",
            "文化修养高"
        ],
        "career_suggestions": [
            "学术研究",
            "教育培训",
            "文化传播"
        ],
        "notes": "从印格者印星太旺，可能过于依赖长辈或缺乏主见。",
        "source": {
            "book": "滴天髓",
            "chapter": "论从印",
            "original": "从印者，印星太旺，日主无气。"
        },
        "interpretation": "从印格者，学问渊博，但需防印旺伤身。"
    },
    {
        "id": "bg_005",
        "name": "化气格",
        "pinyin": "huàqì gé",
        "formation": "日干与月干或时干相合而化",
        "conditions": [
            "日干与月干或时干相合",
            "化神当令且旺",
            "化神无破",
            "从化之气纯粹"
        ],
        "types": [
            {"name": "甲己化土", "化神": "土", "忌神": "木"},
            {"name": "乙庚化金", "化神": "金", "忌神": "火"},
            {"name": "丙辛化水", "化神": "水", "忌神": "土"},
            {"name": "丁壬化木", "化神": "木", "忌神": "金"},
            {"name": "戊癸化火", "化神": "火", "忌神": "水"}
        ],
        "characteristics": [
            "气质非凡",
            "命运独特",
            "化神特性明显"
        ],
        "notes": "化气格需化神纯粹方为可贵，破化则凶。",
        "source": {
            "book": "滴天髓",
            "chapter": "论化气",
            "original": "化气者，天干五合也。甲己化土，乙庚化金，丙辛化水，丁壬化木，戊癸化火。"
        },
        "interpretation": "化气格者，命运特殊，化神所主之事格外吉顺。"
    },
    {
        "id": "bg_006",
        "name": "专旺格",
        "pinyin": "zhuānwàng gé",
        "formation": "日主五行独旺，其他五行顺从",
        "conditions": [
            "日主得令且强旺",
            "同类五行众多",
            "全局气势归附日主",
            "无冲破"
        ],
        "types": [
            {"name": "曲直格", "日主": "木", "气势": "木旺", "宜": "水木", "忌": "金"},
            {"name": "炎上格", "日主": "火", "气势": "火旺", "宜": "木火", "忌": "水"},
            {"name": "稼穑格", "日主": "土", "气势": "土旺", "宜": "火土", "忌": "木"},
            {"name": "从革格", "日主": "金", "气势": "金旺", "宜": "土金", "忌": "火"},
            {"name": "润下格", "日主": "水", "气势": "水旺", "宜": "金水", "忌": "土"}
        ],
        "characteristics": [
            "气势旺盛",
            "个性鲜明",
            "事业心强"
        ],
        "notes": "专旺格者顺势而行，忌逆势而动。",
        "source": {
            "book": "渊海子平",
            "chapter": "论专旺",
            "original": "专旺者，日主独旺，四柱皆归于一气。"
        },
        "interpretation": "专旺格者，得势不饶人，宜顺势发展。"
    },
    {
        "id": "bg_007",
        "name": "从旺格",
        "pinyin": "cóngwàng gé",
        "formation": "日主无气，比劫众多顺势",
        "conditions": [
            "日主无根无气",
            "比劫众多得势",
            "全局比劫一气",
            "无官杀克逆"
        ],
        "characteristics": [
            "为人豪爽",
            "朋友众多",
            "独立性弱",
            "依赖性强"
        ],
        "notes": "从旺格者以比劫为用，贵在朋友相助。",
        "source": {
            "book": "子平真诠",
            "chapter": "论从旺",
            "original": "从旺者，日主无气，满局比劫。"
        },
        "interpretation": "从旺格者，兄弟姐妹朋友助力大，但易纷争。"
    },
    {
        "id": "bg_008",
        "name": "弃命从财格",
        "pinyin": "qìmìng cóngcái gé",
        "formation": "日主极弱，财星强旺，月令为财",
        "conditions": [
            "日主无根无气",
            "月令本气为财",
            "财星当令得势",
            "无印比援手"
        ],
        "characteristics": [
            "财运极佳",
            "善于经商",
            "物质欲望强",
            "务实肯干"
        ],
        "notes": "从财格之一，唯财是命，为财而忙。",
        "source": {
            "book": "滴天髓",
            "chapter": "论从财",
            "original": "弃命从财，不须印比。"
        },
        "interpretation": "弃命从财者，命中注定为财忙碌，善于理财。"
    },
    {
        "id": "bg_009",
        "name": "两神成象格",
        "pinyin": "liǎngshén chéngxiàng gé",
        "formation": "全局仅有两种五行，且力量相当",
        "conditions": [
            "全局仅两种五行",
            "两种五行力量相当",
            "无其他五行杂入",
            "气势纯粹"
        ],
        "types": [
            {"name": "水木相生", "功用": "文才出众"},
            {"name": "木火相生", "功用": "热情奔放"},
            {"name": "火土相生", "功用": "稳重厚实"},
            {"name": "土金相生", "功用": "信用可靠"},
            {"name": "金水相生", "功用": "聪明灵秀"},
            {"name": "水火既济", "功用": "调和有方"},
            {"name": "木土相克", "功用": "刚柔并济"},
            {"name": "金木相克", "功用": "能文能武"}
        ],
        "characteristics": [
            "性格独特",
            "命运特殊",
            "各具特色"
        ],
        "notes": "两神成象需气势纯粹方为上等。",
        "source": {
            "book": "滴天髓",
            "chapter": "论两神",
            "original": "两神成象，非上即下。"
        },
        "interpretation": "两神成象者，命运独特，非富即贵。"
    },
    {
        "id": "bg_010",
        "name": "三奇真贵格",
        "pinyin": "sānqí zhēnguì gé",
        "formation": "天干见甲戊庚或乙丙丁或丙丁戊（顺序不乱）",
        "conditions": [
            "天干见甲戊庚三奇",
            "三奇顺序不乱",
            "三奇得地",
            "无冲破"
        ],
        "characteristics": [
            "才学出众",
            "命运非凡",
            "多才多艺"
        ],
        "notes": "三奇贵格需排列顺序不乱方验。",
        "source": {
            "book": "渊海子平",
            "chapter": "论三奇",
            "original": "天上三奇甲戊庚，地下三奇乙丙丁，人中三奇壬癸辛。"
        },
        "interpretation": "三奇格者，聪明过人，命运奇特。"
    }
]

COMPOUND_PATTERNS = {
    "good_patterns": [
        {
            "id": "cp_001",
            "name": "杀印相生",
            "pinyin": "shā yìn xiāng shēng",
            "description": "七杀与正印相生相化",
            "formation": "七杀为用，正印化杀生身",
            "meaning": "以印化杀，有勇有谋",
            "interpretation": "七杀配印，文武双全，宜从政或管理",
            "source": {"book": "渊海子平", "chapter": "论杀印相生"},
            "effects": ["聪明果断", "能文能武", "事业有成"]
        },
        {
            "id": "cp_002",
            "name": "羊刃驾杀",
            "pinyin": "yángrèn jià shā",
            "description": "羊刃与七杀同现配合",
            "formation": "羊刃抗杀，杀刃相制",
            "meaning": "以刃抗杀，威权显赫",
            "interpretation": "威权显赫，宜武职或管理",
            "source": {"book": "滴天髓", "chapter": "论羊刃驾杀"},
            "effects": ["威权赫赫", "领导力强", "执行力强"]
        },
        {
            "id": "cp_003",
            "name": "食神制杀",
            "pinyin": "shíshén zhì shā",
            "description": "食神克制七杀",
            "formation": "食神为用，克制七杀",
            "meaning": "以食制杀，聪明智慧",
            "interpretation": "聪明智慧，能以智取胜",
            "source": {"book": "渊海子平", "chapter": "论食神制杀"},
            "effects": ["聪明灵巧", "智谋出众", "化解凶险"]
        },
        {
            "id": "cp_004",
            "name": "伤官配印",
            "pinyin": "shāngguān pèi yìn",
            "description": "伤官与正印相配",
            "formation": "印星制约伤官，伤官吐秀",
            "meaning": "伤官配印，才华横溢",
            "interpretation": "才华得以发挥，富贵可期",
            "source": {"book": "子平真诠", "chapter": "论伤官配印"},
            "effects": ["才华横溢", "学业优秀", "名声远扬"]
        },
        {
            "id": "cp_005",
            "name": "财官相生",
            "pinyin": "cái guān xiāng shēng",
            "description": "财星生官星",
            "formation": "财星生官，官星得用",
            "meaning": "财官双美，富贵可期",
            "interpretation": "财运生官运，富贵两全",
            "source": {"book": "渊海子平", "chapter": "论财官相生"},
            "effects": ["财运亨通", "官运顺遂", "富贵双全"]
        },
        {
            "id": "cp_006",
            "name": "食神生财",
            "pinyin": "shíshén shēng cái",
            "description": "食神生财星",
            "formation": "食神吐秀，生助财星",
            "meaning": "食神生财，财源滚滚",
            "interpretation": "财运亨通，财源稳定",
            "source": {"book": "滴天髓", "chapter": "论食神生财"},
            "effects": ["财运稳定", "生财有道", "衣食无忧"]
        },
        {
            "id": "cp_007",
            "name": "官印相生",
            "pinyin": "guān yìn xiāng shēng",
            "description": "官星生印星",
            "formation": "官星生印，印星扶身",
            "meaning": "官印相生，贵气十足",
            "interpretation": "仕途顺利，地位稳固",
            "source": {"book": "渊海子平", "chapter": "论官印相生"},
            "effects": ["仕途顺利", "地位稳固", "受人尊敬"]
        },
        {
            "id": "cp_008",
            "name": "伤官生财",
            "pinyin": "shāngguān shēng cái",
            "description": "伤官生财星",
            "formation": "伤官吐秀，生助财星",
            "meaning": "伤官生财，财运亨通",
            "interpretation": "以才取财，财运佳",
            "source": {"book": "滴天髓", "chapter": "论伤官生财"},
            "effects": ["才华生财", "财运佳", "物质丰富"]
        }
    ],
    "bad_patterns": [
        {
            "id": "cb_001",
            "name": "伤官见官",
            "pinyin": "shāngguān jiàn guān",
            "description": "伤官与正官相冲",
            "formation": "伤官克制正官",
            "meaning": "易有官非口舌",
            "interpretation": "口舌是非多，宜低调行事",
            "avoidance": "避免与官府争执，谨言慎行",
            "source": {"book": "渊海子平", "chapter": "论伤官见官"},
            "effects": ["官讼是非", "事业阻碍", "人际关系差"]
        },
        {
            "id": "cb_002",
            "name": "官杀混杂",
            "pinyin": "guān shā zá zá",
            "description": "正官七杀同时出现",
            "formation": "正官七杀同透或同藏",
            "meaning": "心性不定，格局不清",
            "interpretation": "心志不定，贵气受损",
            "avoidance": "宜清则贵，清则吉",
            "source": {"book": "子平真诠", "chapter": "论官杀混杂"},
            "effects": ["心性不定", "事业波折", "难有成就"]
        },
        {
            "id": "cb_003",
            "name": "比劫夺财",
            "pinyin": "bǐ jié duó cái",
            "description": "比肩劫财克制财星",
            "formation": "比劫众多，财星受损",
            "meaning": "破财之象",
            "interpretation": "财运受损，宜守不宜攻",
            "avoidance": "避免投资合伙，理财保守",
            "source": {"book": "渊海子平", "chapter": "论比劫夺财"},
            "effects": ["破财之象", "合作不利", "财务纠纷"]
        },
        {
            "id": "cb_004",
            "name": "偏印夺食",
            "pinyin": "piān yìn duó shí",
            "description": "偏印克制食神",
            "formation": "偏印旺而食神弱",
            "meaning": "夺食之象",
            "interpretation": "福气受损，健康欠佳",
            "avoidance": "注意饮食健康，防范意外",
            "source": {"book": "滴天髓", "chapter": "论偏印夺食"},
            "effects": ["健康问题", "福气减少", "口舌是非"]
        },
        {
            "id": "cb_005",
            "name": "财破印",
            "pinyin": "cái pò yìn",
            "description": "财星克制印星",
            "formation": "财星旺而印星弱",
            "meaning": "学业受阻",
            "interpretation": "学业事业受损，宜平衡",
            "avoidance": "注意学业进修，防印星受损",
            "source": {"book": "渊海子平", "chapter": "论财破印"},
            "effects": ["学业受阻", "名声受损", "健康问题"]
        },
        {
            "id": "cb_006",
            "name": "身杀两停",
            "pinyin": "shēn shā liǎng tíng",
            "description": "身杀平衡但无制化",
            "formation": "身杀对等无印食制化",
            "meaning": "压力与能力相当",
            "interpretation": "压力大但能承受，需制化方佳",
            "avoidance": "宜有印星或食神制化",
            "source": {"book": "滴天髓", "chapter": "论身杀停均"},
            "effects": ["压力过大", "身心疲惫", "需印食化解"]
        },
        {
            "id": "cb_007",
            "name": "枭神夺食",
            "pinyin": "xiāo shén duó shí",
            "description": "枭神（偏印）克制食神",
            "formation": "偏印旺而食神弱",
            "meaning": "健康寿元受损",
            "interpretation": "易有疾病灾祸",
            "avoidance": "注意健康，防意外",
            "source": {"book": "渊海子平", "chapter": "论枭神夺食"},
            "effects": ["健康受损", "灾祸易生", "福气减少"]
        }
    ]
}

ALL_PATTERNS = {
    "zheng_ge": ZHENG_GE,
    "bian_ge": BIAN_GE,
    "compound_patterns": COMPOUND_PATTERNS
}
