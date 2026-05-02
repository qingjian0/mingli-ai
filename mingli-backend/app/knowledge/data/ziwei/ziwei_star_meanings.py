"""
星曜含义
紫微斗数十四正曜及辅曜的详细解释

星曜分类：
- 十四正曜：紫微、天机、太阳、武曲、天同、廉贞天府、太阴、贪狼、巨门、天相、天梁、七杀、破军
- 甲级主星：十四正曜中最重要者
- 乙级助星：辅助甲级主星
- 丙级杂星：影响较小但仍有作用
"""

ZIWEI_STARS = [
    {
        "id": "star_001",
        "term": "紫微星",
        "pinyin": "zǐwēixīng",
        "wuxing": "土",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阳土",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 15
        },
        "original_content": "紫微帝星，居中垣之首，司权衡，主造化之机。",
        "interpretation": "紫微星为帝王星，是紫微斗数诸星之首，象征最高权力和领导力。",
        "personality": ["领导型", "权威型", "自尊心强", "追求完美"],
        "positive_traits": ["尊贵", "权威", "稳重", "有领导力"],
        "negative_traits": ["高傲", "独断", "固执"],
        "keywords": ["帝王", "权力", "领导", "尊贵", "权威"],
        "combinations": {
            "good": ["天府星", "天相星", "紫微七杀"],
            "bad": ["破军星", "七杀星"]
        },
        "palace_influence": {
            "ming_gong": "有领导才能，地位显赫",
            "cai_gong": "财运亨通，适合投资",
            "shi_gong": "社交广泛，人脉丰富"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_002",
        "term": "天机星",
        "pinyin": "tiānjīxīng",
        "wuxing": "木",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阴木",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 18
        },
        "original_content": "天机星，智多星也，主聪明才智，司谋略机变。",
        "interpretation": "天机星代表智慧、谋略和机变，象征聪明才智和策划能力。",
        "personality": ["智谋型", "策划型", "反应敏捷", "善于思考"],
        "positive_traits": ["聪明", "机智", "善于策划", "有谋略"],
        "negative_traits": ["多疑", "善变", "不稳定"],
        "keywords": ["智慧", "谋略", "机变", "策划", "聪明"],
        "combinations": {
            "good": ["太阴星", "天同星", "天梁星"],
            "bad": ["破军星", "七杀星"]
        },
        "palace_influence": {
            "ming_gong": "聪明有谋，适合从商或策划",
            "cai_gong": "理财有道，财运稳定",
            "guan_gong": "事业心强，适合创业"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_003",
        "term": "太阳星",
        "pinyin": "tàiyángxīng",
        "wuxing": "火",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阳火",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 22
        },
        "original_content": "太阳星，光明之象，司权柄贵显，主文章科甲。",
        "interpretation": "太阳星象征光明和权力，代表名望、地位和文采。",
        "personality": ["热情型", "正义型", "光明磊落", "乐于助人"],
        "positive_traits": ["热情", "正义", "大方", "有爱心"],
        "negative_traits": ["过刚", "冲动", "主观"],
        "keywords": ["光明", "权力", "名望", "文采", "正义"],
        "combinations": {
            "good": ["太阴星", "禄存星", "天梁星"],
            "bad": ["破军星", "七杀星"]
        },
        "palace_influence": {
            "ming_gong": "声名显赫，适合从政或教育",
            "guan_gong": "权力欲强，适合管理岗位",
            "yi_gong": "子女缘分深，得子女之力"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_004",
        "term": "武曲星",
        "pinyin": "wǔqūxīng",
        "wuxing": "金",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阳金",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 25
        },
        "original_content": "武曲星，刚毅之星，司财帛武职，主刚强果断。",
        "interpretation": "武曲星代表刚毅和决断，象征财运和武职成就。",
        "personality": ["刚毅型", "务实型", "果断坚决", "重实际"],
        "positive_traits": ["刚毅", "果断", "务实", "有财运"],
        "negative_traits": ["固执", "冲动", "缺乏柔情"],
        "keywords": ["刚毅", "决断", "财帛", "武职", "务实"],
        "combinations": {
            "good": ["天府星", "紫微星", "天相星"],
            "bad": ["破军星", "七杀星", "贪狼星"]
        },
        "palace_influence": {
            "ming_gong": "性格刚强，适合武职或金融",
            "cai_gong": "财运旺盛，适合投资创业",
            "fu_gong": "得祖业，或创业起家"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_005",
        "term": "天同星",
        "pinyin": "tiāntóngxīng",
        "wuxing": "水",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阳水",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 28
        },
        "original_content": "天同星，福星也，主福禄温和，司享受清闲。",
        "interpretation": "天同星代表福气和享受，象征温和、享乐和福禄。",
        "personality": ["温和型", "享乐型", "知足常乐", "随遇而安"],
        "positive_traits": ["温和", "福气", "乐观", "人缘好"],
        "negative_traits": ["懒散", "缺乏上进", "得过且过"],
        "keywords": ["福气", "享乐", "温和", "清闲", "乐观"],
        "combinations": {
            "good": ["天机星", "太阴星", "天梁星"],
            "bad": ["七杀星", "破军星"]
        },
        "palace_influence": {
            "ming_gong": "性格温和，人缘佳，享福之命",
            "yi_gong": "子女孝顺，享天伦之乐",
            "tian_gong": "田产丰厚，房产运佳"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_006",
        "term": "廉贞星",
        "pinyin": "liánzhēnxīng",
        "wuxing": "火",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阴火",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 31
        },
        "original_content": "廉贞星，邪正之星，主邪正两途，司是非口舌。",
        "interpretation": "廉贞星具有双重性格，既可代表邪恶是非，也可代表清廉贞洁。",
        "personality": ["矛盾型", "复杂型", "感情丰富", "易走极端"],
        "positive_traits": ["感情丰富", "有魅力", "有才华"],
        "negative_traits": ["易惹是非", "固执", "感情纠纷"],
        "keywords": ["廉洁", "贞操", "是非", "邪正", "感情"],
        "combinations": {
            "good": ["天府星", "天相星", "紫微星"],
            "bad": ["破军星", "七杀星", "贪狼星"]
        },
        "palace_influence": {
            "ming_gong": "感情丰富，异性缘佳",
            "qi_gong": "桃花旺盛，须防感情纠纷",
            "guan_gong": "事业起伏大，成败不定"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_007",
        "term": "天府星",
        "pinyin": "tiānfǔxīng",
        "wuxing": "土",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阳土",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 34
        },
        "original_content": "天府星，富贵之星，司财库田宅，主稳定保守。",
        "interpretation": "天府星代表富贵和稳定，象征财库和不动产。",
        "personality": ["保守型", "稳重型", "务实理财", "追求稳定"],
        "positive_traits": ["稳重", "理财有方", "有财库", "保守"],
        "negative_traits": ["保守", "缺乏冲劲", "过度谨慎"],
        "keywords": ["富贵", "财库", "田宅", "稳定", "保守"],
        "combinations": {
            "good": ["紫微星", "武曲星", "天相星"],
            "bad": ["破军星", "七杀星"]
        },
        "palace_influence": {
            "ming_gong": "理财能力强，有积蓄之命",
            "cai_gong": "财运稳定，财库充盈",
            "tian_gong": "房产运佳，不动产丰厚"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_008",
        "term": "太阴星",
        "pinyin": "tàiyīnxīng",
        "wuxing": "水",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阴水",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 37
        },
        "original_content": "太阴星，柔静之象，司财帛田宅，主温柔内敛。",
        "interpretation": "太阴星代表温柔和内敛，象征女性和财运。",
        "personality": ["温柔型", "内敛型", "细腻敏感", "追求安全感"],
        "positive_traits": ["温柔", "细腻", "有财运", "内敛"],
        "negative_traits": ["多愁善感", "优柔寡断", "依赖性强"],
        "keywords": ["温柔", "内敛", "财帛", "女性", "细腻"],
        "combinations": {
            "good": ["太阳星", "天同星", "天机星"],
            "bad": ["破军星", "七杀星"]
        },
        "palace_influence": {
            "ming_gong": "女性温和，男性则内敛细腻",
            "cai_gong": "财运稳定，理财谨慎",
            "yi_gong": "女缘分深，得女性助力"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_009",
        "term": "贪狼星",
        "pinyin": "tānlángxīng",
        "wuxing": "木",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阳木",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 40
        },
        "original_content": "贪狼星，欲望之星，司财禄酒色，主贪欲多情。",
        "interpretation": "贪狼星代表欲望和贪念，象征物欲和情欲。",
        "personality": ["欲望型", "多情型", "野心勃勃", "追求刺激"],
        "positive_traits": ["有野心", "多才多艺", "有魅力", "适应力强"],
        "negative_traits": ["贪婪", "多情", "欲望过强", "易走偏锋"],
        "keywords": ["贪欲", "酒色", "财禄", "多情", "野心"],
        "combinations": {
            "good": ["紫微星", "天相星", "天府星"],
            "bad": ["破军星", "七杀星", "武曲星"]
        },
        "palace_influence": {
            "ming_gong": "野心大，桃花旺，须防物欲横流",
            "qi_gong": "桃花旺盛，感情复杂",
            "guan_gong": "事业心强，敢于冒险"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_010",
        "term": "巨门星",
        "pinyin": "jùménxīng",
        "wuxing": "水",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阴水",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 43
        },
        "original_content": "巨门星，暗曜也，司是非口舌，主疑惑多端。",
        "interpretation": "巨门星代表是非和口舌，象征辩论和暗中的力量。",
        "personality": ["辩论型", "怀疑型", "言辞犀利", "内心多疑"],
        "positive_traits": ["口才好", "分析力强", "观察敏锐", "有学识"],
        "negative_traits": ["多疑", "是非多", "口舌纠纷", "爱挑剔"],
        "keywords": ["是非", "口舌", "疑惑", "暗曜", "辩论"],
        "combinations": {
            "good": ["天机星", "天同星", "太阳星"],
            "bad": ["破军星", "七杀星", "贪狼星"]
        },
        "palace_influence": {
            "ming_gong": "口才好，但易惹是非",
            "kou_gong": "口才出众，适合销售或律师",
            "xiang_gong": "兄弟关系复杂，易生口舌"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_011",
        "term": "天相星",
        "pinyin": "tiānxiàngxīng",
        "wuxing": "水",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阳水",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 46
        },
        "original_content": "天相星，印星也，司权力俸禄，主扶助辅佐。",
        "interpretation": "天相星代表印权和辅佐，象征权力和辅助的力量。",
        "personality": ["辅佐型", "忠诚型", "稳重可靠", "追求权力"],
        "positive_traits": ["忠诚", "稳重", "有责任感", "善于辅佐"],
        "negative_traits": ["缺乏主见", "依赖性强", "过于保守"],
        "keywords": ["印星", "权力", "俸禄", "辅佐", "忠诚"],
        "combinations": {
            "good": ["紫微星", "天府星", "武曲星"],
            "bad": ["破军星", "七杀星"]
        },
        "palace_influence": {
            "ming_gong": "稳重可靠，适合从政或管理",
            "guan_gong": "权力欲强，适合辅佐他人",
            "fu_gong": "得父母之力，或继承家业"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_012",
        "term": "天梁星",
        "pinyin": "tiānliángxīng",
        "wuxing": "土",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阳土",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 49
        },
        "original_content": "天梁星，寿星也，司延寿荫福，主清高正直。",
        "interpretation": "天梁星代表长寿和荫庇，象征清高和正直。",
        "personality": ["清高型", "正直型", "乐于助人", "追求清誉"],
        "positive_traits": ["正直", "清高", "有爱心", "长寿"],
        "negative_traits": ["清高", "固执", "好为人师"],
        "keywords": ["寿星", "荫福", "清高", "正直", "延寿"],
        "combinations": {
            "good": ["太阳星", "天同星", "天机星"],
            "bad": ["破军星", "七杀星"]
        },
        "palace_influence": {
            "ming_gong": "正直清高，有长辈缘",
            "fu_gong": "得父母或长辈荫庇",
            "qian_gong": "健康运佳，有延寿之命"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_013",
        "term": "七杀星",
        "pinyin": "qīshāxīng",
        "wuxing": "金",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阳金",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 52
        },
        "original_content": "七杀星，将星也，司威权勇猛，主冲锋陷阵。",
        "interpretation": "七杀星代表威权和勇猛，象征军事和冒险。",
        "personality": ["刚烈型", "冒险型", "勇猛果敢", "敢作敢当"],
        "positive_traits": ["勇敢", "果断", "有魄力", "敢于冒险"],
        "negative_traits": ["刚烈", "冲动", "暴躁", "易得罪人"],
        "keywords": ["将星", "威权", "勇猛", "军事", "冒险"],
        "combinations": {
            "good": ["紫微星", "天府星", "天相星"],
            "bad": ["天机星", "天同星", "太阴星"]
        },
        "palace_influence": {
            "ming_gong": "胆大敢为，适合创业或武职",
            "guan_gong": "权力欲强，适合管理或军事",
            "chong_gong": "变动大，须防意外"
        },
        "verification_status": "verified"
    },
    {
        "id": "star_014",
        "term": "破军星",
        "pinyin": "pòjūnxīng",
        "wuxing": "水",
        "category": "main_star",
        "level": "甲级",
        "system": "ziwei",
        "nature": "阳水",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·星曜总论",
            "page": 55
        },
        "original_content": "破军星，耗星也，司消耗破败，主先破后成。",
        "interpretation": "破军星代表消耗和破败，象征破旧立新。",
        "personality": ["破坏型", "革新型", "敢冲敢拼", "先破后立"],
        "positive_traits": ["创新", "勇敢", "有魄力", "破旧立新"],
        "negative_traits": ["破坏", "消耗", "不稳定", "败家"],
        "keywords": ["耗星", "破败", "消耗", "革新", "先破后成"],
        "combinations": {
            "good": ["紫微星", "天府星", "天相星"],
            "bad": ["天机星", "天同星", "太阴星", "太阳星"]
        },
        "palace_influence": {
            "ming_gong": "先破后立，大起大落",
            "cai_gong": "财来财去，须防破财",
            "guan_gong": "事业变动大，创业型"
        },
        "verification_status": "verified"
    }
]

ASSISTANT_STARS = [
    {
        "id": "assist_001",
        "term": "禄存星",
        "pinyin": "lùcúnxīng",
        "wuxing": "土",
        "category": "assistant_star",
        "level": "乙级",
        "system": "ziwei",
        "nature": "阳土",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·辅曜论",
            "page": 58
        },
        "original_content": "禄存星，主财禄之星，司俸禄吉庆，主积累储存。",
        "interpretation": "禄存星代表财禄和积累，象征稳定的收入和积蓄。",
        "keywords": ["财禄", "俸禄", "积累", "吉庆"],
        "verification_status": "verified"
    },
    {
        "id": "assist_002",
        "term": "天马星",
        "pinyin": "tiānmǎxīng",
        "wuxing": "火",
        "category": "assistant_star",
        "level": "乙级",
        "system": "ziwei",
        "nature": "阳火",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·辅曜论",
            "page": 60
        },
        "original_content": "天马星，驿马之星，司迁调动移，主奔波变动。",
        "interpretation": "天马星代表驿马和变动，象征外出和迁移。",
        "keywords": ["驿马", "变动", "迁徒", "奔波"],
        "verification_status": "verified"
    },
    {
        "id": "assist_003",
        "term": "左辅星",
        "pinyin": "zuǒfǔxīng",
        "wuxing": "土",
        "category": "assistant_star",
        "level": "乙级",
        "system": "ziwei",
        "nature": "阳土",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·辅曜论",
            "page": 62
        },
        "original_content": "左辅星，辅弼之星，司辅佐帮助，主助力支持。",
        "interpretation": "左辅星代表辅佐和帮助，象征他人的支持。",
        "keywords": ["辅佐", "帮助", "助力", "支持"],
        "verification_status": "verified"
    },
    {
        "id": "assist_004",
        "term": "右弼星",
        "pinyin": "yòubìxīng",
        "wuxing": "水",
        "category": "assistant_star",
        "level": "乙级",
        "system": "ziwei",
        "nature": "阴水",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷一·辅曜论",
            "page": 64
        },
        "original_content": "右弼星，辅弼之星，司辅佐帮助，主文昌显达。",
        "interpretation": "右弼星代表辅佐和文昌，象征事业和学业的成功。",
        "keywords": ["辅弼", "文昌", "显达", "成功"],
        "verification_status": "verified"
    }
]
