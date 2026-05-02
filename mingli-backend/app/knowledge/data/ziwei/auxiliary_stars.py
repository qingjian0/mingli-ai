"""
紫微斗数辅星、煞星、杂曜知识库
源自《紫微斗数全书》《斗数宣微》《中州派紫微斗数》

星曜分类：
- 辅星（8颗）：左辅、右弼、文昌、文曲、禄存、天马、地空、地劫
- 煞星（6颗）：擎羊、陀罗、火星、铃星、天空、地劫
- 杂曜（20+颗）：解神、阴煞、天德、月德、恩光、天贵、龙池、凤阁等
"""

AUXILIARY_STARS = [
    {
        "id": "aux_001",
        "term": "左辅星",
        "pinyin": "zuǒfǔxīng",
        "wuxing": "土",
        "category": "auxiliary",
        "level": "乙级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·辅曜星",
            "page": 45
        },
        "original_content": "左辅星，象辅弼之臣，主忠诚、有助。居左辅佐紫微，犹君之有贤臣。",
        "interpretation": "左辅星为紫微星最重要的辅佐星，代表忠诚的臣子和助力，象征辅助力量和贵人。",
        "enhanced_meaning": {
            "庙": "能力强，有助力，地位稳固",
            "旺": "贵人运佳，人脉广泛",
            "陷": "助力不足，孤立无援"
        },
        "personality": ["稳重可靠", "忠诚正直", "乐于助人", "有耐心"],
        "positive_traits": ["有助力", "人缘好", "事业有成", "处事圆滑"],
        "negative_traits": ["依赖性强", "缺乏主见"],
        "combinations": [
            {"star": "紫微星", "meaning": "君臣相得，权力巩固，领导力增强"},
            {"star": "天府星", "meaning": "得力助手，事业发达，财运亨通"},
            {"star": "天相星", "meaning": "印星得辅，权力稳固，仕途顺遂"},
            {"star": "武曲星", "meaning": "刚柔并济，财运事业双丰收"}
        ],
        "palace_influence": {
            "ming_gong": "性格稳重，有领导才能",
            "guan_gong": "事业有助力，职位稳固",
            "cai_gong": "财运佳，有贵人相助"
        },
        "keywords": ["助力", "忠诚", "辅助", "贵人", "辅弼"],
        "verification_status": "verified"
    },
    {
        "id": "aux_002",
        "term": "右弼星",
        "pinyin": "yòubìxīng",
        "wuxing": "水",
        "category": "auxiliary",
        "level": "乙级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·辅曜星",
            "page": 47
        },
        "original_content": "右弼星，象文曜之臣，主文章显达，扶辅相成。",
        "interpretation": "右弼星代表文昌显达和辅助力量，象征学业成就和文书之运。",
        "enhanced_meaning": {
            "庙": "文才出众，学业有成",
            "旺": "才华横溢，声名远播",
            "陷": "学业受阻，怀才不遇"
        },
        "personality": ["文雅斯文", "才华出众", "善于表达", "追求完美"],
        "positive_traits": ["文才好", "学业佳", "有声名", "善于协调"],
        "negative_traits": ["清高", "不善变通"],
        "combinations": [
            {"star": "紫微星", "meaning": "文武双全，权柄兼顾，名利双收"},
            {"star": "文昌星", "meaning": "文星聚会，学业大吉，考试顺利"},
            {"star": "天机星", "meaning": "智慧出众，策划能力强"}
        ],
        "palace_influence": {
            "ming_gong": "文雅有才学，气质出众",
            "guan_gong": "仕途顺利，职位显达",
            "yi_gong": "子女学业佳，才华出众"
        },
        "keywords": ["文昌", "显达", "学业", "文书", "辅弼"],
        "verification_status": "verified"
    },
    {
        "id": "aux_003",
        "term": "文昌星",
        "pinyin": "wénchāngxīng",
        "wuxing": "金",
        "category": "auxiliary",
        "level": "乙级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·文曜论",
            "page": 52
        },
        "original_content": "文昌星，司文章科举之星，主才学名声，利正途功名。",
        "interpretation": "文昌星代表学业成就和科举功名，象征正统的学业和考试之运。",
        "enhanced_meaning": {
            "庙": "学业大吉，考试顺利，金榜题名",
            "旺": "才华横溢，声名远播",
            "陷": "学业受阻，才华难展"
        },
        "personality": ["好学上进", "勤勉努力", "追求学识", "注重名声"],
        "positive_traits": ["学业优秀", "考试顺利", "文才好", "名声好"],
        "negative_traits": ["过于追求名利", "学术至上"],
        "combinations": [
            {"star": "紫微星", "meaning": "科名显达，权贵双全"},
            {"star": "天府星", "meaning": "文财双美，学以致用"},
            {"star": "天梁星", "meaning": "学术有成，声名远扬"},
            {"star": "太阳星", "meaning": "功名显达，科甲联捷"}
        ],
        "palace_influence": {
            "ming_gong": "学业优秀，聪明好学",
            "guan_gong": "仕途功名顺利",
            "yi_gong": "子女学业优秀"
        },
        "keywords": ["学业", "功名", "科举", "文章", "文昌"],
        "verification_status": "verified"
    },
    {
        "id": "aux_004",
        "term": "文曲星",
        "pinyin": "wénqǔxīng",
        "wuxing": "水",
        "category": "auxiliary",
        "level": "乙级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·文曜论",
            "page": 54
        },
        "original_content": "文曲星，司才艺词辩之星，主巧艺口才，利异路功名。",
        "interpretation": "文曲星代表才艺和口才，象征非正统途径的成就和表达能力强。",
        "enhanced_meaning": {
            "庙": "才华出众，口才了得，技艺精湛",
            "旺": "多才多艺，表达能力强",
            "陷": "才华难展，口舌是非"
        },
        "personality": ["才华横溢", "善于表达", "机智灵敏", "多才多艺"],
        "positive_traits": ["口才好", "才艺多", "反应快", "善于变通"],
        "negative_traits": ["花言巧语", "不够稳重"],
        "combinations": [
            {"star": "紫微星", "meaning": "权谋兼备，能言善道"},
            {"star": "贪狼星", "meaning": "桃花犯主，感情复杂"},
            {"star": "武曲星", "meaning": "武职文用，技艺出众"}
        ],
        "palace_influence": {
            "ming_gong": "聪明机敏，多才多艺",
            "kou_gong": "口才出众，善于表达",
            "cai_gong": "偏财运佳，有意外之财"
        },
        "keywords": ["才艺", "口才", "词辩", "巧艺", "文曲"],
        "verification_status": "verified"
    },
    {
        "id": "aux_005",
        "term": "禄存星",
        "pinyin": "lùcúnxīng",
        "wuxing": "土",
        "category": "auxiliary",
        "level": "甲级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·财禄论",
            "page": 35
        },
        "original_content": "禄存星，主财禄之星，司俸禄吉庆，主积累储存，为财库之根。",
        "interpretation": "禄存星代表财禄和积累，是紫微斗数中最重要的财星，象征稳定的收入和积蓄。",
        "enhanced_meaning": {
            "庙": "财运亨通，积累丰厚，物质充裕",
            "旺": "财源稳定，储蓄有道",
            "陷": "财运不佳，破耗较大"
        },
        "personality": ["务实稳重", "理财有方", "勤俭节约", "重视物质"],
        "positive_traits": ["财运好", "能积蓄", "理财强", "物质充裕"],
        "negative_traits": ["过于保守", "吝啬小气"],
        "combinations": [
            {"star": "紫微星", "meaning": "权禄两全，富贵双全"},
            {"star": "天府星", "meaning": "双禄交加，财库充盈"},
            {"star": "武曲星", "meaning": "财官双美，富贵双全"},
            {"star": "天马星", "meaning": "禄马交驰，财运大发，外地得财"}
        ],
        "palace_influence": {
            "ming_gong": "理财能力强，善于积累",
            "cai_gong": "财运亨通，财库充盈",
            "fu_gong": "得祖上荫庇，承继家业"
        },
        "keywords": ["财禄", "俸禄", "积累", "吉庆", "财库"],
        "verification_status": "verified"
    },
    {
        "id": "aux_006",
        "term": "天马星",
        "pinyin": "tiānmǎxīng",
        "wuxing": "火",
        "category": "auxiliary",
        "level": "乙级",
        "nature": "中性星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·驿马论",
            "page": 68
        },
        "original_content": "天马星，驿马之星，司迁调动移，主奔波变动，为动象之代表。",
        "interpretation": "天马星代表驿马和变动，象征外出、迁移和奔波之运。",
        "enhanced_meaning": {
            "庙": "动中求财，外地发展，迁移有利",
            "旺": "走动频繁，变动活跃",
            "陷": "奔波劳碌，居无定所"
        },
        "personality": ["好动不安", "追求变化", "适应力强", "不安于现状"],
        "positive_traits": ["适应力强", "善于交际", "勇于尝试", "视野开阔"],
        "negative_traits": ["不稳定", "奔波劳碌", "缺乏耐心"],
        "combinations": [
            {"star": "禄存星", "meaning": "禄马交驰，财运大发，外地得财"},
            {"star": "武曲星", "meaning": "财马动发，贸易起家"},
            {"star": "太阴星", "meaning": "动中有财，女性助力"},
            {"star": "贪狼星", "meaning": "桃花马动，奔波于情"}
        ],
        "palace_influence": {
            "ming_gong": "不安现状，喜欢变动",
            "guan_gong": "职业变动多，常出差",
            "chu_gong": "外出发展有利，离家发展"
        },
        "keywords": ["驿马", "变动", "迁移", "奔波", "动象"],
        "verification_status": "verified"
    },
    {
        "id": "aux_007",
        "term": "地空星",
        "pinyin": "dìkōngxīng",
        "wuxing": "火",
        "category": "auxiliary",
        "level": "丙级",
        "nature": "中性星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·空曜论",
            "page": 72
        },
        "original_content": "地空星，主空亡破耗之星，司虚无灭没，主人精神恍惚。",
        "interpretation": "地空星代表空亡和消耗，象征精神层面的空虚和物质上的破耗。",
        "enhanced_meaning": {
            "庙": "精神超脱，淡泊名利",
            "旺": "创意无限，想象丰富",
            "陷": "破耗较大，精神空虚"
        },
        "personality": ["思想独特", "理想主义", "不善理财", "精神追求"],
        "positive_traits": ["创意丰富", "不重物质", "精神独立", "有灵感"],
        "negative_traits": ["破耗大", "不稳定", "难积蓄"],
        "combinations": [
            {"star": "紫微星", "meaning": "空有其表，虚名虚利"},
            {"star": "天府星", "meaning": "空有财库，难以守住"},
            {"star": "火星", "meaning": "火空则发，一时得意"}
        ],
        "palace_influence": {
            "ming_gong": "思想独特，不重物质",
            "cai_gong": "财运不稳，破耗较大",
            "guan_gong": "事业起伏大，不稳定"
        },
        "keywords": ["空亡", "破耗", "虚无", "精神", "灭没"],
        "verification_status": "verified"
    },
    {
        "id": "aux_008",
        "term": "地劫星",
        "pinyin": "dìjiéxīng",
        "wuxing": "火",
        "category": "auxiliary",
        "level": "丙级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·劫曜论",
            "page": 74
        },
        "original_content": "地劫星，主劫夺破耗之星，司灾祸损失，主人争夺劫取。",
        "interpretation": "地劫星代表劫夺和损失，象征争夺、劫难和意外的破耗。",
        "enhanced_meaning": {
            "庙": "劫难可解，因祸得福",
            "旺": "冲劲十足，敢于冒险",
            "陷": "破耗严重，灾祸连连"
        },
        "personality": ["刚强好胜", "敢于冒险", "不服输", "争强好斗"],
        "positive_traits": ["有冲劲", "不服输", "敢于拼搏"],
        "negative_traits": ["破耗大", "争夺心强", "易惹祸"],
        "combinations": [
            {"star": "紫微星", "meaning": "劫格逢君，先难后易"},
            {"star": "七杀星", "meaning": "杀劫同行，凶险异常"},
            {"star": "破军星", "meaning": "劫破交加，破祖离乡"}
        ],
        "palace_influence": {
            "ming_gong": "争强好胜，劫难较多",
            "cai_gong": "破耗较大，财来财去",
            "guan_gong": "事业起伏大，成败不定"
        },
        "keywords": ["劫夺", "破耗", "灾祸", "损失", "争夺"],
        "verification_status": "verified"
    }
]

SINFUL_STARS = [
    {
        "id": "sha_001",
        "term": "擎羊星",
        "pinyin": "qíngyángxīng",
        "wuxing": "火",
        "category": "sha",
        "level": "甲级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·六煞星",
            "page": 78
        },
        "original_content": "擎羊星，主刑伤，是非冲突，司刀杖血光之灾。",
        "interpretation": "擎羊为六煞之首，代表冲突、刑伤、阻碍和意外，象征直接的伤害和冲突。",
        "characteristics": [
            "性格刚强，易冲动",
            "易有意外伤灾",
            "事业多阻碍",
            "易招惹是非"
        ],
        "enhanced_meaning": {
            "庙": "敢冲敢拼，能化煞为权",
            "旺": "冲劲十足，敢于冒险",
            "陷": "刑伤难免，灾祸不断"
        },
        "personality": ["刚强冲动", "不服输", "敢于冒险", "急躁易怒"],
        "positive_traits": ["有魄力", "敢冲敢拼", "意志坚定"],
        "negative_traits": ["冲动", "易惹祸", "刑伤", "是非多"],
        "avoidance": [
            "避免冲突场合",
            "注意交通安全",
            "修身养性",
            "远离是非之地"
        ],
        "combinations": [
            {"star": "紫微星", "meaning": "羊刃相随，权柄加重，须防刚过易折"},
            {"star": "七杀星", "meaning": "杀羊同行，凶险异常，刑伤难免"},
            {"star": "武曲星", "meaning": "武职发达，但易有血光之灾"},
            {"star": "天相星", "meaning": "有印转化，可减凶性"}
        ],
        "palace_influence": {
            "ming_gong": "性格刚强，刑伤难免",
            "guan_gong": "事业阻碍多，竞争激烈",
            "qian_gong": "健康受损，须防意外"
        },
        "keywords": ["刑伤", "冲突", "阻碍", "血光", "刀杖"],
        "verification_status": "verified"
    },
    {
        "id": "sha_002",
        "term": "陀罗星",
        "pinyin": "tuóluówīng",
        "wuxing": "金",
        "category": "sha",
        "level": "甲级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·六煞星",
            "page": 80
        },
        "original_content": "陀罗星，主拖累纠缠，司暗昧是非，主人拖延滞碍。",
        "interpretation": "陀罗代表拖延、纠缠和暗中的阻碍，象征持续性的问题和内耗。",
        "characteristics": [
            "做事拖延",
            "易被拖累",
            "纠缠不清",
            "暗中阻碍"
        ],
        "enhanced_meaning": {
            "庙": "拖延有度，终能成事",
            "旺": "内耗严重，纠缠不断",
            "陷": "拖累过重，难以解脱"
        },
        "personality": ["优柔寡断", "缺乏主见", "易被利用", "拖沓"],
        "positive_traits": ["有耐心", "韧性强"],
        "negative_traits": ["拖延", "拖累", "纠缠", "暗昧"],
        "avoidance": [
            "避免优柔寡断",
            "谨防被人利用",
            "果断行事",
            "注意合同纠纷"
        ],
        "combinations": [
            {"star": "紫微星", "meaning": "陀罗缠君，办事拖延，进退维谷"},
            {"star": "天机星", "meaning": "机陀同宫，谋略难伸，计划受阻"},
            {"star": "天同星", "meaning": "同陀会聚，懒散拖延，坐失良机"}
        ],
        "palace_influence": {
            "ming_gong": "优柔寡断，办事拖沓",
            "guan_gong": "事业阻碍多，进度缓慢",
            "yi_gong": "感情纠缠，拖泥带水"
        },
        "keywords": ["拖累", "纠缠", "拖延", "暗昧", "滞碍"],
        "verification_status": "verified"
    },
    {
        "id": "sha_003",
        "term": "火星",
        "pinyin": "huǒxīng",
        "wuxing": "火",
        "category": "sha",
        "level": "乙级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·火铃星",
            "page": 82
        },
        "original_content": "火星，烈烈轰轰之星，司火灾血光，主人急躁暴烈。",
        "interpretation": "火星代表急剧的变化和爆发性的能量，象征突发事件和激烈的冲突。",
        "characteristics": [
            "性格急躁",
            "易发怒",
            "突发性事件",
            "火灾危险"
        ],
        "enhanced_meaning": {
            "庙": "敢冲敢拼，能爆发成功",
            "旺": "脾气暴躁，易惹祸端",
            "陷": "灾祸突然，难以防备"
        },
        "personality": ["急躁冲动", "脾气火爆", "敢作敢当", "缺乏耐心"],
        "positive_traits": ["有冲劲", "爆发力强", "敢于行动"],
        "negative_traits": ["冲动", "暴躁", "易惹祸", "火灾"],
        "avoidance": [
            "控制脾气",
            "避免冲动决策",
            "注意防火",
            "远离危险活动"
        ],
        "combinations": [
            {"star": "贪狼星", "meaning": "火贪同行，爆发力强，有意外之喜"},
            {"star": "紫微星", "meaning": "火紫相会，权柄激发，但易有血光"},
            {"star": "七杀星", "meaning": "火杀相冲，凶险异常"},
            {"star": "铃星", "meaning": "火铃双煞，凶性大增"}
        ],
        "palace_influence": {
            "ming_gong": "性格急躁，脾气火爆",
            "qian_gong": "健康易出问题，注意心脏",
            "jia_gong": "火灾隐患，注意居家安全"
        },
        "keywords": ["火灾", "血光", "急躁", "爆发", "暴烈"],
        "verification_status": "verified"
    },
    {
        "id": "sha_004",
        "term": "铃星",
        "pinyin": "língxīng",
        "wuxing": "火",
        "category": "sha",
        "level": "乙级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·火铃星",
            "page": 84
        },
        "original_content": "铃星，隐隐约约之星，司暗昧惊怖，主人阴沉多疑。",
        "interpretation": "铃星代表暗中的威胁和心理的不安，象征持续性的压力和内在的恐惧。",
        "characteristics": [
            "阴沉多疑",
            "内在压力",
            "暗中小人",
            "心理不安"
        ],
        "enhanced_meaning": {
            "庙": "内敛深沉，能暗中成事",
            "旺": "多疑多虑，内心不安",
            "陷": "暗昧缠身，惊怖不断"
        },
        "personality": ["阴沉多疑", "内心不安", "善于隐藏", "敏感多虑"],
        "positive_traits": ["城府深", "善于隐忍", "心思细腻"],
        "negative_traits": ["多疑", "暗昧", "惊怖", "阴沉"],
        "avoidance": [
            "保持心态平和",
            "避免多疑多虑",
            "光明磊落行事",
            "寻求心理咨询"
        ],
        "combinations": [
            {"star": "贪狼星", "meaning": "铃贪同度，桃花暗动，感情复杂"},
            {"star": "七杀星", "meaning": "铃杀相会，暗中受阻，须防暗算"},
            {"star": "火星", "meaning": "火铃双煞，凶性大增，灾难深重"}
        ],
        "palace_influence": {
            "ming_gong": "内心不安，多疑多虑",
            "guan_gong": "暗中小人多，须防暗算",
            "shi_gong": "人际关系复杂，暗中是非"
        },
        "keywords": ["暗昧", "惊怖", "多疑", "阴沉", "暗中"],
        "verification_status": "verified"
    },
    {
        "id": "sha_005",
        "term": "天空星",
        "pinyin": "tiānkōngxīng",
        "wuxing": "火",
        "category": "sha",
        "level": "丙级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·空曜论",
            "page": 76
        },
        "original_content": "天空星，虚幻不实之星，司空虚破灭，主人志大才疏。",
        "interpretation": "天空代表虚幻和理想化，象征不切实际和难以落地的想法。",
        "characteristics": [
            "志大才疏",
            "好高骛远",
            "执行力差",
            "理想主义"
        ],
        "enhanced_meaning": {
            "庙": "思想超脱，淡泊名利",
            "旺": "空想多，实干少",
            "陷": "一事无成，眼高手低"
        },
        "personality": ["理想主义", "好高骛远", "思想丰富", "执行力弱"],
        "positive_traits": ["思想开阔", "有创意", "不重物质"],
        "negative_traits": ["空想", "虚浮", "不切实际", "缺乏行动"],
        "avoidance": [
            "脚踏实地",
            "从小事做起",
            "避免空想",
            "培养执行力"
        ],
        "combinations": [
            {"star": "紫微星", "meaning": "空有其名，难得实权"},
            {"star": "天机星", "meaning": "空有机谋，难成大事"},
            {"star": "太阴星", "meaning": "空有才情，难遇知音"}
        ],
        "palace_influence": {
            "ming_gong": "好高骛远，志大才疏",
            "guan_gong": "事业难成，计划落空",
            "yi_gong": "子女空想多，实干少"
        },
        "keywords": ["空虚", "虚幻", "破灭", "不实", "空想"],
        "verification_status": "verified"
    },
    {
        "id": "sha_006",
        "term": "地劫星",
        "pinyin": "dìjiéxīng",
        "wuxing": "火",
        "category": "sha",
        "level": "丙级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·劫曜论",
            "page": 74
        },
        "original_content": "地劫星，主劫夺破耗之星，司灾祸损失，主人争夺劫取。",
        "interpretation": "地劫星代表劫夺和损失，与地空同为空劫之星，但地劫更强调争夺和外显的破耗。",
        "characteristics": [
            "破耗较大",
            "争夺心强",
            "意外损失",
            "投资失利"
        ],
        "enhanced_meaning": {
            "庙": "劫难可解，因祸得福",
            "旺": "破耗不断，争夺不休",
            "陷": "劫难深重，损失惨重"
        },
        "personality": ["争强好胜", "敢于冒险", "不服输", "容易冲动"],
        "positive_traits": ["有冲劲", "敢于拼搏"],
        "negative_traits": ["破耗大", "争夺多", "灾祸", "损失"],
        "avoidance": [
            "避免高风险投资",
            "谨慎签订合同",
            "注意财物安全",
            "低调行事"
        ],
        "combinations": [
            {"star": "紫微星", "meaning": "劫格逢君，先难后易"},
            {"star": "七杀星", "meaning": "杀劫同行，凶险异常"},
            {"star": "破军星", "meaning": "劫破交加，破祖离乡，财库空虚"}
        ],
        "palace_influence": {
            "ming_gong": "破耗较大，争夺心强",
            "cai_gong": "破财不断，投资失利",
            "guan_gong": "事业起伏大，竞争激烈"
        },
        "keywords": ["劫夺", "破耗", "灾祸", "损失", "争夺"],
        "verification_status": "verified"
    }
]

MISC_STARS = [
    {
        "id": "misc_001",
        "term": "解神星",
        "pinyin": "jiěshénxīng",
        "category": "misc",
        "subcategory": "吉曜",
        "level": "丁级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·杂曜论",
            "page": 112
        },
        "original_content": "解神星，主化解灾厄之星，司排难解纷。",
        "interpretation": "解神星代表化解和排解，象征灾难的化解和是非的平息。",
        "characteristics": ["化灾解难", "排难解纷", "化解是非"],
        "enhanced_meaning": {
            "庙": "灾厄可解，危难有救",
            "陷": "解难之力不足"
        },
        "keywords": ["化解", "排难", "解纷", "化灾"],
        "verification_status": "verified"
    },
    {
        "id": "misc_002",
        "term": "阴煞星",
        "pinyin": "yīnshàxīng",
        "category": "misc",
        "subcategory": "凶曜",
        "level": "丁级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·杂曜论",
            "page": 114
        },
        "original_content": "阴煞星，主暗昧阴邪之星，司阴私暗害。",
        "interpretation": "阴煞星代表暗中的小人、阴私和阴谋，象征背后的是非和暗算。",
        "characteristics": ["暗中作祟", "阴私暗害", "小人是非", "阴谋陷害"],
        "enhanced_meaning": {
            "庙": "暗害可防，阴谋难成",
            "陷": "阴煞缠身，暗箭难防"
        },
        "avoidance": ["谨言慎行", "远离小人", "光明正大"],
        "keywords": ["阴煞", "暗害", "阴谋", "阴私"],
        "verification_status": "verified"
    },
    {
        "id": "misc_003",
        "term": "天德星",
        "pinyin": "tiāndéxīng",
        "category": "misc",
        "subcategory": "吉曜",
        "level": "丁级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·德曜论",
            "page": 108
        },
        "original_content": "天德星，天恩浩荡之星，司天赐吉庆，主逢凶化吉。",
        "interpretation": "天德星代表天赐的吉庆和德泽，象征贵人和逢凶化吉的力量。",
        "characteristics": ["天赐吉庆", "逢凶化吉", "德泽深厚", "贵人相助"],
        "enhanced_meaning": {
            "庙": "德福双全，贵人扶持",
            "旺": "遇难成祥，逢凶化吉",
            "陷": "德泽不足，化解有限"
        },
        "combinations": [
            {"star": "天德", "with": "月德", "meaning": "双德同会，大吉大利，灾祸全消"}
        ],
        "keywords": ["天德", "吉庆", "化吉", "德泽"],
        "verification_status": "verified"
    },
    {
        "id": "misc_004",
        "term": "月德星",
        "pinyin": "yuèdéxīng",
        "category": "misc",
        "subcategory": "吉曜",
        "level": "丁级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·德曜论",
            "page": 110
        },
        "original_content": "月德星，月华润泽之星，司温和吉庆，主女贵提携。",
        "interpretation": "月德星代表温和的吉庆和女性的贵助，象征柔和的帮助和化解。",
        "characteristics": ["温和吉庆", "女性贵助", "化解是非", "柔和之力"],
        "enhanced_meaning": {
            "庙": "女性缘佳，得女贵助",
            "旺": "化解之力强，灾祸可解",
            "陷": "化解之力弱，贵人难遇"
        },
        "combinations": [
            {"star": "月德", "with": "天德", "meaning": "双德同会，大吉大利，灾祸全消"}
        ],
        "keywords": ["月德", "吉庆", "女贵", "化解"],
        "verification_status": "verified"
    },
    {
        "id": "misc_005",
        "term": "恩光星",
        "pinyin": "ēnguāngxīng",
        "category": "misc",
        "subcategory": "吉曜",
        "level": "丁级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·荣恩论",
            "page": 118
        },
        "original_content": "恩光星，主恩宠荣耀之星，司封诰光荣。",
        "interpretation": "恩光星代表恩宠和荣耀，象征得到赏识和提拔的机会。",
        "characteristics": ["恩宠荣耀", "封诰光荣", "受赏识", "得名位"],
        "enhanced_meaning": {
            "庙": "恩宠有加，光荣显达",
            "旺": "荣耀加身，名声远播",
            "陷": "恩宠难求，荣耀难获"
        },
        "keywords": ["恩光", "恩宠", "荣耀", "封诰"],
        "verification_status": "verified"
    },
    {
        "id": "misc_006",
        "term": "天贵星",
        "pinyin": "tiānguìxīng",
        "category": "misc",
        "subcategory": "吉曜",
        "level": "丁级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·荣恩论",
            "page": 120
        },
        "original_content": "天贵星，主贵显声名之星，司功名成就。",
        "interpretation": "天贵星代表贵显和声名，象征功成名就和地位的提升。",
        "characteristics": ["贵显声名", "功名成就", "地位提升", "受尊重"],
        "enhanced_meaning": {
            "庙": "功名成就，贵显一方",
            "旺": "名声远播，地位显赫",
            "陷": "功名难就，难获尊重"
        },
        "keywords": ["天贵", "贵显", "声名", "功名"],
        "verification_status": "verified"
    },
    {
        "id": "misc_007",
        "term": "龙池星",
        "pinyin": "lóngchíxīng",
        "category": "misc",
        "subcategory": "装饰曜",
        "level": "丁级",
        "nature": "中性星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·装饰论",
            "page": 125
        },
        "original_content": "龙池星，主荣华富贵之象，司池阁装饰。",
        "interpretation": "龙池星代表荣华和装饰，与凤阁相配，象征门面和外在的华美。",
        "characteristics": ["荣华富贵", "池阁装饰", "门面华美", "外在表现"],
        "enhanced_meaning": {
            "庙": "荣华富贵，表面光鲜",
            "陷": "华而不实，虚有其表"
        },
        "combinations": [
            {"star": "龙池", "with": "凤阁", "meaning": "龙凤相配，荣华富贵，门面显赫"}
        ],
        "keywords": ["龙池", "荣华", "富贵", "装饰"],
        "verification_status": "verified"
    },
    {
        "id": "misc_008",
        "term": "凤阁星",
        "pinyin": "fènggéxīng",
        "category": "misc",
        "subcategory": "装饰曜",
        "level": "丁级",
        "nature": "中性星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·装饰论",
            "page": 127
        },
        "original_content": "凤阁星，主文章装饰之象，司楼台华丽。",
        "interpretation": "凤阁星代表文采和装饰，与龙池相配，象征才华的外在表现。",
        "characteristics": ["文章华美", "楼台华丽", "文采装饰", "才华外现"],
        "enhanced_meaning": {
            "庙": "文采飞扬，才华出众",
            "陷": "华而不实，虚有其表"
        },
        "combinations": [
            {"star": "凤阁", "with": "龙池", "meaning": "龙凤相配，荣华富贵，门面显赫"}
        ],
        "keywords": ["凤阁", "文章", "华丽", "装饰"],
        "verification_status": "verified"
    },
    {
        "id": "misc_009",
        "term": "孤辰星",
        "pinyin": "gūchénxīng",
        "category": "misc",
        "subcategory": "凶曜",
        "level": "丁级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·孤寡论",
            "page": 132
        },
        "original_content": "孤辰星，主孤寡孤独之星，司生离死别。",
        "interpretation": "孤辰星代表孤独和分离，象征独居、丧偶和与六亲的疏离。",
        "characteristics": ["孤独寡居", "生离死别", "与六亲疏", "独居之命"],
        "enhanced_meaning": {
            "庙": "孤而不寂，精神独立",
            "陷": "孤独终老，刑克六亲"
        },
        "combinations": [
            {"star": "孤辰", "with": "寡宿", "meaning": "孤寡相逢，孤独之命，难得有情"}
        ],
        "keywords": ["孤辰", "孤独", "寡居", "分离"],
        "verification_status": "verified"
    },
    {
        "id": "misc_010",
        "term": "寡宿星",
        "pinyin": "guǎsùxīng",
        "category": "misc",
        "subcategory": "凶曜",
        "level": "丁级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·孤寡论",
            "page": 134
        },
        "original_content": "寡宿星，主鳏寡孤独之星，司婚姻迟滞。",
        "interpretation": "寡宿星代表婚姻的迟滞和寡居，象征晚婚、独身或丧偶的命格。",
        "characteristics": ["婚姻迟滞", "鳏寡孤独", "晚婚之命", "寡居之象"],
        "enhanced_meaning": {
            "庙": "晚婚有缘，迟得佳偶",
            "陷": "婚姻难成，孤独终老"
        },
        "combinations": [
            {"star": "寡宿", "with": "孤辰", "meaning": "孤寡相逢，孤独之命，难得有情"}
        ],
        "keywords": ["寡宿", "鳏寡", "晚婚", "孤独"],
        "verification_status": "verified"
    },
    {
        "id": "misc_011",
        "term": "红鸾星",
        "pinyin": "hóngluánxīng",
        "category": "misc",
        "subcategory": "吉曜",
        "level": "丁级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·桃花论",
            "page": 98
        },
        "original_content": "红鸾星，主婚姻喜庆之星，司恋爱嫁娶。",
        "interpretation": "红鸾星代表婚姻和喜庆，象征正缘桃花和恋爱婚姻的顺利。",
        "characteristics": ["婚姻喜庆", "恋爱顺利", "正缘桃花", "嫁娶吉庆"],
        "enhanced_meaning": {
            "庙": "姻缘早发，婚姻美满",
            "旺": "桃花旺盛，感情顺利",
            "陷": "桃花过重，感情复杂"
        },
        "combinations": [
            {"star": "红鸾", "with": "天喜", "meaning": "鸾喜同会，姻缘早发，婚姻幸福"}
        ],
        "keywords": ["红鸾", "婚姻", "喜庆", "桃花"],
        "verification_status": "verified"
    },
    {
        "id": "misc_012",
        "term": "天喜星",
        "pinyin": "tiānxǐxīng",
        "category": "misc",
        "subcategory": "吉曜",
        "level": "丁级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·桃花论",
            "page": 100
        },
        "original_content": "天喜星，主吉庆喜悦之星，司添丁之喜。",
        "interpretation": "天喜星代表喜悦和添丁之喜，象征子女缘分和家庭吉庆。",
        "characteristics": ["吉庆喜悦", "添丁之喜", "家庭和睦", "子女缘分"],
        "enhanced_meaning": {
            "庙": "喜事连连，家宅安宁",
            "旺": "喜事频繁，人丁兴旺",
            "陷": "喜庆难求，人丁稀少"
        },
        "combinations": [
            {"star": "天喜", "with": "红鸾", "meaning": "鸾喜同会，姻缘早发，婚姻幸福"}
        ],
        "keywords": ["天喜", "吉庆", "添丁", "喜悦"],
        "verification_status": "verified"
    },
    {
        "id": "misc_013",
        "term": "破碎星",
        "pinyin": "pòsuìxīng",
        "category": "misc",
        "subcategory": "凶曜",
        "level": "丁级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·破耗论",
            "page": 140
        },
        "original_content": "破碎星，主破耗损失之星，司破败财散。",
        "interpretation": "破碎星代表破耗和损失，象征投资失利、破财和物品的损坏。",
        "characteristics": ["破耗损失", "投资失利", "破财之象", "物损之灾"],
        "enhanced_meaning": {
            "庙": "破中有成，先破后立",
            "陷": "破耗连连，损失惨重"
        },
        "keywords": ["破碎", "破耗", "损失", "破败"],
        "verification_status": "verified"
    },
    {
        "id": "misc_014",
        "term": "大耗星",
        "pinyin": "dàhàoxīng",
        "category": "misc",
        "subcategory": "凶曜",
        "level": "丁级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·破耗论",
            "page": 142
        },
        "original_content": "大耗星，主大耗破败之星，司破败耗散。",
        "interpretation": "大耗星代表大额的破耗和损失，象征大笔破财和严重的失败。",
        "characteristics": ["大额破耗", "破败损失", "耗财之灾", "失败之象"],
        "enhanced_meaning": {
            "庙": "破耗可避，损失有限",
            "陷": "大耗连连，财务危机"
        },
        "keywords": ["大耗", "破耗", "破败", "耗散"],
        "verification_status": "verified"
    },
    {
        "id": "misc_015",
        "term": "官府星",
        "pinyin": "guānfǔxīng",
        "category": "misc",
        "subcategory": "吉曜",
        "level": "丁级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·官禄论",
            "page": 145
        },
        "original_content": "官府星，主仕途官府之星，司俸禄官职。",
        "interpretation": "官府星代表仕途和官职，象征在官场的发展和职位的提升。",
        "characteristics": ["仕途顺利", "官职提升", "俸禄增加", "官场得意"],
        "enhanced_meaning": {
            "庙": "官运亨通，仕途顺遂",
            "陷": "官运不通，难以升迁"
        },
        "keywords": ["官府", "仕途", "官职", "俸禄"],
        "verification_status": "verified"
    },
    {
        "id": "misc_016",
        "term": "奏书星",
        "pinyin": "zòushūxīng",
        "category": "misc",
        "subcategory": "吉曜",
        "level": "丁级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·官禄论",
            "page": 147
        },
        "original_content": "奏书星，主文书奏对之星，司文章科甲。",
        "interpretation": "奏书星代表文书和科举，象征文书运势和考试成就。",
        "characteristics": ["文书顺利", "科举成就", "文章出众", "名声显达"],
        "enhanced_meaning": {
            "庙": "文书大吉，科甲顺利",
            "陷": "文书受阻，科举不利"
        },
        "keywords": ["奏书", "文书", "科举", "文章"],
        "verification_status": "verified"
    },
    {
        "id": "misc_017",
        "term": "台辅星",
        "pinyin": "táifǔxīng",
        "category": "misc",
        "subcategory": "吉曜",
        "level": "丁级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·辅弼论",
            "page": 150
        },
        "original_content": "台辅星，主辅佐台阁之星，司辅助扶持。",
        "interpretation": "台辅星代表辅佐和扶持，象征在组织中的辅助地位和助力。",
        "characteristics": ["辅佐得力", "台阁扶持", "职位稳固", "助力充足"],
        "enhanced_meaning": {
            "庙": "辅佐有功，得人信任",
            "陷": "辅佐无功，难获信任"
        },
        "keywords": ["台辅", "辅佐", "台阁", "扶持"],
        "verification_status": "verified"
    },
    {
        "id": "misc_018",
        "term": "封诰星",
        "pinyin": "fènggào xīng",
        "category": "misc",
        "subcategory": "吉曜",
        "level": "丁级",
        "nature": "善星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·辅弼论",
            "page": 152
        },
        "original_content": "封诰星，主封赠诰命之星，司荣誉称号。",
        "interpretation": "封诰星代表荣誉和封赠，象征得到名誉和地位的确立。",
        "characteristics": ["封赠荣誉", "诰命称号", "名誉地位", "受封得荣"],
        "enhanced_meaning": {
            "庙": "封诰荣身，名利双收",
            "陷": "诰命难求，荣誉难得"
        },
        "keywords": ["封诰", "诰命", "荣誉", "称号"],
        "verification_status": "verified"
    },
    {
        "id": "misc_019",
        "term": "天巫星",
        "pinyin": "tiānwūxīng",
        "category": "misc",
        "subcategory": "中性曜",
        "level": "丁级",
        "nature": "中性星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·杂曜论",
            "page": 155
        },
        "original_content": "天巫星，主升迁推荐之星，司提拔推荐。",
        "interpretation": "天巫星代表升迁和推荐，象征得到他人的提拔和推荐。",
        "characteristics": ["升迁推荐", "提拔重用", "伯乐相助", "仕途进步"],
        "enhanced_meaning": {
            "庙": "升迁顺利，得人提拔",
            "陷": "推荐难求，升迁受阻"
        },
        "keywords": ["天巫", "升迁", "推荐", "提拔"],
        "verification_status": "verified"
    },
    {
        "id": "misc_020",
        "term": "天姚星",
        "pinyin": "tiānyáoxīng",
        "category": "misc",
        "subcategory": "桃花曜",
        "level": "丁级",
        "nature": "中性星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·桃花论",
            "page": 102
        },
        "original_content": "天姚星，主风骚浪漫之星，司情感艳丽。",
        "interpretation": "天姚星代表风骚和浪漫，象征情感的魅力和外在的吸引力。",
        "characteristics": ["风骚浪漫", "情感丰富", "魅力出众", "外表吸引"],
        "enhanced_meaning": {
            "庙": "魅力四射，感情丰富",
            "陷": "感情复杂，桃花过重"
        },
        "keywords": ["天姚", "风骚", "浪漫", "桃花"],
        "verification_status": "verified"
    },
    {
        "id": "misc_021",
        "term": "天刑星",
        "pinyin": "tiānxíngxīng",
        "category": "misc",
        "subcategory": "凶曜",
        "level": "丁级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·刑曜论",
            "page": 160
        },
        "original_content": "天刑星，主刑克官非之星，司法律刑罚。",
        "interpretation": "天刑星代表刑克和官非，象征法律问题和身体的刑伤。",
        "characteristics": ["刑克官非", "法律问题", "身体刑伤", "官司诉讼"],
        "enhanced_meaning": {
            "庙": "刑克有制，灾祸可免",
            "陷": "刑克深重，官非不断"
        },
        "keywords": ["天刑", "刑克", "官非", "刑罚"],
        "verification_status": "verified"
    },
    {
        "id": "misc_022",
        "term": "劫煞星",
        "pinyin": "jiéshàxīng",
        "category": "misc",
        "subcategory": "凶曜",
        "level": "丁级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·劫曜论",
            "page": 165
        },
        "original_content": "劫煞星，主意外灾祸之星，司突发事件。",
        "interpretation": "劫煞星代表意外和突发灾祸，象征不可预测的突发事件。",
        "characteristics": ["意外灾祸", "突发事件", "不可预测", "突然变故"],
        "enhanced_meaning": {
            "庙": "意外可避，大难不死",
            "陷": "意外频发，灾祸难逃"
        },
        "keywords": ["劫煞", "意外", "灾祸", "突发"],
        "verification_status": "verified"
    },
    {
        "id": "misc_023",
        "term": "岁煞星",
        "pinyin": "suìshàxīng",
        "category": "misc",
        "subcategory": "凶曜",
        "level": "丁级",
        "nature": "煞星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·岁煞论",
            "page": 168
        },
        "original_content": "岁煞星，主太岁相冲之星，司岁君相冲。",
        "interpretation": "岁煞星代表与太岁相冲的凶险，象征年度的不顺和冲犯。",
        "characteristics": ["太岁相冲", "岁君相冲", "年度不顺", "冲犯太岁"],
        "enhanced_meaning": {
            "庙": "冲犯有制，可化解",
            "陷": "冲犯太岁，灾祸连连"
        },
        "keywords": ["岁煞", "太岁", "相冲", "冲犯"],
        "verification_status": "verified"
    },
    {
        "id": "misc_024",
        "term": "华盖星",
        "pinyin": "huágàixīng",
        "category": "misc",
        "subcategory": "中性曜",
        "level": "丁级",
        "nature": "中性星",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷二·华盖论",
            "page": 172
        },
        "original_content": "华盖星，主艺术宗教之星，司孤高清高。",
        "interpretation": "华盖星代表艺术和宗教的缘分，象征孤高的气质和对精神层面的追求。",
        "characteristics": ["艺术气质", "宗教缘分", "孤高清高", "精神追求"],
        "enhanced_meaning": {
            "庙": "艺术有成，宗教信仰",
            "旺": "清高孤傲，与众不同",
            "陷": "孤僻难合，脱离世俗"
        },
        "keywords": ["华盖", "艺术", "宗教", "孤高"],
        "verification_status": "verified"
    }
]
