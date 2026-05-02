"""
格局汇总
紫微斗数重要格局详解

格局是紫微斗数论命的重要依据，代表命盘中星曜的特殊组合
"""

ZIWEI_PATTERNS = [
    {
        "id": "pattern_001",
        "name": "紫府同宫格",
        "pinyin": "zǐfǔ tónggōng gé",
        "pattern_type": "noble_pattern",
        "quality": "上格",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷四·格局论",
            "page": 78
        },
        "formation": "紫微星与天府星同坐命宫",
        "original_content": "紫府同宫格，紫微天府同坐命宫，无煞冲破，主富贵双全。",
        "interpretation": "紫微天府双星同宫，象征帝王与储君同位，代表极高的地位和富贵。",
        "characteristics": {
            "personality": "领导力强，有王者风范",
            "career": "事业发达，位高权重",
            "wealth": "财运亨通，富贵双全",
            "relationships": "人际关系好，得众人拥戴"
        },
        "conditions": {
            "required": ["紫微天府同宫", "命宫无煞星"],
            "forbidden": ["破军", "七杀", "化忌"]
        },
        "favorable_combinations": ["禄存星", "左辅星", "右弼星"],
        "keywords": ["富贵", "双全", "领导", "权力"],
        "verification_status": "verified"
    },
    {
        "id": "pattern_002",
        "name": "机月同梁格",
        "pinyin": "jīyuè tóngliáng gé",
        "pattern_type": "scholar_pattern",
        "quality": "上格",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷四·格局论",
            "page": 80
        },
        "formation": "天机、太阴、天同、天梁四星同会于命宫或官禄宫",
        "original_content": "机月同梁格，天机太阴天同天梁四星同会，主人文章盖世，仕途得意。",
        "interpretation": "四星汇聚，象征智谋与福泽并存，主学业和仕途得意。",
        "characteristics": {
            "personality": "聪明睿智，学识渊博",
            "career": "仕途得意，官运亨通",
            "scholarship": "文章出众，学业优异",
            "relationships": "人缘好，得贵人相助"
        },
        "conditions": {
            "required": ["天机太阴同宫", "天同天梁同宫"],
            "optional": ["化科", "文昌", "文曲"]
        },
        "favorable_combinations": ["化科", "文昌星", "文曲星"],
        "keywords": ["文章", "仕途", "学业", "智慧"],
        "verification_status": "verified"
    },
    {
        "id": "pattern_003",
        "name": "杀破狼格",
        "pinyin": "shāpòláng gé",
        "pattern_type": "change_pattern",
        "quality": "中格",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷四·格局论",
            "page": 82
        },
        "formation": "七杀、破军、贪狼三星同守或对照于命宫",
        "original_content": "杀破狼格，七杀破军贪狼三星同守或对照，主变动、创业。",
        "interpretation": "三星聚守，象征激烈的变动和创业冲动，命运起伏较大。",
        "characteristics": {
            "personality": "敢闯敢拼，不甘平凡",
            "career": "创业有成，但起伏大",
            "change": "命运多变动，变化频繁",
            "risk": "敢于冒险，魄力十足"
        },
        "conditions": {
            "required": ["七杀破军贪狼同宫或对照"],
            "note": "此格之人一生多变动，成败不定"
        },
        "favorable_combinations": ["紫微星", "天府星", "化禄"],
        "unfavorable_combinations": ["化忌", "擎羊", "陀罗"],
        "keywords": ["变动", "创业", "魄力", "起伏"],
        "warning": "此格之人人生大起大落，需谨慎理财和决策",
        "verification_status": "verified"
    },
    {
        "id": "pattern_004",
        "name": "紫微七杀格",
        "pinyin": "zǐwēi qīshā gé",
        "pattern_type": "power_pattern",
        "quality": "上格",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷四·格局论",
            "page": 84
        },
        "formation": "紫微星与七杀星同坐命宫或对宫",
        "original_content": "紫微七杀同宫或对冲，威命无伤，大富大贵。",
        "interpretation": "帝星与将星相会，象征权力与武力的结合，主大富大贵。",
        "characteristics": {
            "personality": "威严果断，有领导魅力",
            "career": "事业有成，适合军政",
            "wealth": "财运佳，可积累财富",
            "authority": "权力欲强，适合管理"
        },
        "conditions": {
            "required": ["紫微七杀同宫"],
            "forbidden": ["破军", "化忌冲破"]
        },
        "favorable_combinations": ["天府星", "天相星", "禄存星"],
        "keywords": ["威权", "富贵", "武职", "领导"],
        "verification_status": "verified"
    },
    {
        "id": "pattern_005",
        "name": "武曲七杀格",
        "pinyin": "wǔqū qīshā gé",
        "pattern_type": "military_pattern",
        "quality": "中格",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷四·格局论",
            "page": 86
        },
        "formation": "武曲星与七杀星同坐命宫",
        "original_content": "武曲七杀同宫，掌兵权，权威出众。",
        "interpretation": "财星与将星相会，象征财运与武职的结合。",
        "characteristics": {
            "personality": "刚毅果断，行动力强",
            "career": "适合武职或金融",
            "wealth": "财运佳，能积累财富",
            "authority": "有权威，适合管理"
        },
        "conditions": {
            "required": ["武曲七杀同宫命宫"],
            "favorable": ["紫微星", "天府星"]
        },
        "keywords": ["兵权", "武职", "财运", "果断"],
        "verification_status": "verified"
    },
    {
        "id": "pattern_006",
        "name": "贪武同行格",
        "pinyin": "tānwǔ tóngxíng gé",
        "pattern_type": "wealth_pattern",
        "quality": "上格",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷四·格局论",
            "page": 88
        },
        "formation": "贪狼星与武曲星同坐命宫或迁移宫",
        "original_content": "贪武同行，三十岁后方可创业，财运丰厚。",
        "interpretation": "欲望与决断同宫，早年财运不利，中年后财源广进。",
        "characteristics": {
            "personality": "野心大，敢于冒险",
            "career": "创业型，适合投资",
            "wealth": "财运丰厚，能积累财富",
            "timing": "早年多波折，三十岁后转佳"
        },
        "conditions": {
            "required": ["贪狼武曲同宫"],
            "note": "需三十岁后方能成就"
        },
        "favorable_combinations": ["化禄", "禄存星"],
        "unfavorable_combinations": ["化忌", "擎羊", "陀罗"],
        "keywords": ["财运", "创业", "投资", "三十岁后"],
        "verification_status": "verified"
    },
    {
        "id": "pattern_007",
        "name": "府相朝垣格",
        "pinyin": "fǔxiāng cháoyuán gé",
        "pattern_type": "noble_pattern",
        "quality": "上格",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷四·格局论",
            "page": 90
        },
        "formation": "天府星、天相星分别位于命宫的三方四正",
        "original_content": "府相朝垣格，天府天相来朝命宫，主大富大贵。",
        "interpretation": "财库与印星相辅，象征富贵双全之命。",
        "characteristics": {
            "personality": "稳重可靠，有责任感",
            "career": "事业稳定，适合从政",
            "wealth": "财运稳定，积累丰厚",
            "status": "地位稳固，受人尊敬"
        },
        "conditions": {
            "required": ["天府天相在三方四正"],
            "note": "命宫星曜需完整无破"
        },
        "favorable_combinations": ["紫微星", "化禄", "禄存星"],
        "keywords": ["富贵", "双全", "稳定", "朝垣"],
        "verification_status": "verified"
    },
    {
        "id": "pattern_008",
        "name": "火贪格",
        "pinyin": "huǒtān gé",
        "pattern_type": "change_pattern",
        "quality": "中格",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷四·格局论",
            "page": 92
        },
        "formation": "贪狼星与火星或铃星同坐命宫",
        "original_content": "火贪同行，暴富暴贵，多得意外之财。",
        "interpretation": "欲望之星遇火，象征突然的财富和地位提升。",
        "characteristics": {
            "personality": "敢于冒险，爆发力强",
            "career": "多变动，可能一夜暴富",
            "wealth": "可能有意外之财",
            "timing": "机遇来临时能抓住"
        },
        "conditions": {
            "required": ["贪狼火星同宫或贪狼铃星同宫"],
            "note": "需抓住机遇，否则易暴富暴贫"
        },
        "favorable_combinations": ["化禄", "禄存星"],
        "warning": "此格之人财运不稳定，须谨慎理财",
        "keywords": ["暴富", "意外之财", "机遇", "变动"],
        "verification_status": "verified"
    },
    {
        "id": "pattern_009",
        "name": "铃贪格",
        "pinyin": "língtān gé",
        "pattern_type": "change_pattern",
        "quality": "中格",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷四·格局论",
            "page": 94
        },
        "formation": "贪狼星与铃星同坐命宫",
        "original_content": "铃贪同行，亦主暴富，但较火贪稍逊。",
        "interpretation": "欲望之星遇铃，财富来得较慢但更稳定。",
        "characteristics": {
            "personality": "隐忍有谋，不张扬",
            "career": "稳步发展，终有成就",
            "wealth": "财运渐进而稳定",
            "timing": "成就较慢但更稳固"
        },
        "conditions": {
            "required": ["贪狼铃星同宫"],
            "comparison": "火贪格主暴富，铃贪格主渐富"
        },
        "favorable_combinations": ["化禄", "禄存星"],
        "keywords": ["渐富", "稳步", "隐忍", "有谋"],
        "verification_status": "verified"
    },
    {
        "id": "pattern_010",
        "name": "马头带剑格",
        "pinyin": "mǎtóu dàijiàn gé",
        "pattern_type": "military_pattern",
        "quality": "中格",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷四·格局论",
            "page": 96
        },
        "formation": "擎羊星与天马星同坐命宫",
        "original_content": "马头带剑，，威权出众，掌兵符。",
        "interpretation": "驿马遇煞，象征奔波和武职成就。",
        "characteristics": {
            "personality": "刚毅果断，不畏艰难",
            "career": "适合军警或外务",
            "movement": "多外出，多变动",
            "authority": "有威严，能掌权"
        },
        "conditions": {
            "required": ["擎羊天马同宫命宫"],
            "note": "适合武职或外务工作"
        },
        "keywords": ["兵权", "武职", "奔波", "威权"],
        "verification_status": "verified"
    }
]
