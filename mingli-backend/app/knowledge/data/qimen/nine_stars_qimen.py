"""
九星含义
奇门遁甲九星的详细解释

九星：天蓬、天芮、天冲、天辅、天禽、天心、天柱、天任、天英
"""

QIMEN_STARS = [
    {
        "id": "qstar_001",
        "term": "天蓬星",
        "pinyin": "tiānpéngxīng",
        "wuxing": "水",
        "position": "坎一宫",
        "category": "nine_stars",
        "system": "qimen",
        "nature": "大凶星",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "九星总论",
            "page": 60
        },
        "original_content": "天蓬星，北方玄一之水，司盗贼之事。",
        "interpretation": "天蓬星代表盗匪和破耗，象征危险和损失。",
        "general_meaning": {
            "fortune": "易有破耗，须防盗贼",
            "career": "多变动，不宜投资",
            "health": "注意肾水方面疾病"
        },
        "favorable": {
            "activities": ["安防", "捉贼", "潜水", "航海"],
            "directions": ["北方"]
        },
        "unfavorable": {
            "activities": ["开业", "嫁娶", "远行"],
            "note": "易有盗难和破财"
        },
        "keywords": ["盗匪", "破耗", "危险", "北方"],
        "combinations": {
            "with_door": "与死门：大凶，易有死亡",
            "with_god": "与玄武：防盗防盗"
        },
        "warning": "天蓬为凶星，用事宜谨慎",
        "verification_status": "verified"
    },
    {
        "id": "qstar_002",
        "term": "天芮星",
        "pinyin": "tiānruìxīng",
        "wuxing": "土",
        "position": "坤二宫",
        "category": "nine_stars",
        "system": "qimen",
        "nature": "凶星",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "九星总论",
            "page": 63
        },
        "original_content": "天芮星，西南二之土，司疾病之事。",
        "interpretation": "天芮星代表疾病和学业，象征疾病和困惑。",
        "general_meaning": {
            "fortune": "易有疾病，健康不佳",
            "career": "学习运佳，适合求学",
            "relationships": "人际关系复杂"
        },
        "favorable": {
            "activities": ["求学", "拜师", "养生", "医疗"],
            "directions": ["西南方"]
        },
        "unfavorable": {
            "activities": ["开业", "婚嫁", "动土"],
            "note": "易有病患"
        },
        "keywords": ["疾病", "学业", "困惑", "西南"],
        "combinations": {
            "with_door": "与死门：大凶，防重病",
            "with_god": "与白虎：疾病缠身"
        },
        "warning": "天芮为凶星，须注意健康",
        "verification_status": "verified"
    },
    {
        "id": "qstar_003",
        "term": "天冲星",
        "pinyin": "tiānchōngxīng",
        "wuxing": "木",
        "position": "震三宫",
        "category": "nine_stars",
        "system": "qimen",
        "nature": "次凶星",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "九星总论",
            "page": 66
        },
        "original_content": "天冲星，东方三之木，司冲突争斗之事。",
        "interpretation": "天冲星代表冲动和冲突，象征突破和冲击。",
        "general_meaning": {
            "fortune": "多变动，易有冲突",
            "career": "利于突破，不宜守成",
            "relationships": "易起争执"
        },
        "favorable": {
            "activities": ["出征", "冲突", "竞争", "突破"],
            "directions": ["东方"]
        },
        "unfavorable": {
            "activities": ["和谈", "嫁娶", "开业"],
            "note": "易有冲撞"
        },
        "keywords": ["冲突", "冲动", "突破", "东方"],
        "combinations": {
            "with_door": "与伤门：争斗激烈",
            "with_god": "与九天：冲突更大"
        },
        "warning": "天冲为次凶星，用事需谨慎",
        "verification_status": "verified"
    },
    {
        "id": "qstar_004",
        "term": "天辅星",
        "pinyin": "tiānfǔxīng",
        "wuxing": "木",
        "position": "巽四宫",
        "category": "nine_stars",
        "system": "qimen",
        "nature": "大吉星",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "九星总论",
            "page": 69
        },
        "original_content": "天辅星，东南四之木，司辅弼之事。",
        "interpretation": "天辅星代表辅助和贵人多助，象征帮助和扶持。",
        "general_meaning": {
            "fortune": "贵人相助，办事顺利",
            "career": "利于升迁，得上司赏识",
            "relationships": "人缘佳，得众人帮助"
        },
        "favorable": {
            "activities": ["求学", "求职", "升迁", "合作"],
            "directions": ["东南方"]
        },
        "unfavorable": {
            "activities": ["安葬", "破坏"],
            "note": "不忌"
        },
        "keywords": ["辅助", "贵人多助", "升迁", "东南"],
        "combinations": {
            "with_door": "与生门：大吉，利财",
            "with_god": "与六合：贵人相助"
        },
        "verification_status": "verified"
    },
    {
        "id": "qstar_005",
        "term": "天禽星",
        "pinyin": "tiānqínxīng",
        "wuxing": "土",
        "position": "中五宫",
        "category": "nine_stars",
        "system": "qimen",
        "nature": "吉星",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "九星总论",
            "page": 72
        },
        "original_content": "天禽星，中宫五之土，司诚信中正之事。",
        "interpretation": "天禽星代表中正和诚信，象征公正和稳重。",
        "general_meaning": {
            "fortune": "中正平和，办事稳妥",
            "career": "诚信经营，得众人信任",
            "relationships": "为人正直，人际关系好"
        },
        "favorable": {
            "activities": ["求职", "合作", "签约", "求学"],
            "directions": ["中宫"]
        },
        "unfavorable": {
            "activities": ["安葬", "动土"],
            "note": "不忌"
        },
        "keywords": ["中正", "诚信", "稳重", "中宫"],
        "combinations": {
            "with_door": "与开门：大吉，利事业",
            "with_god": "与值符：大吉，利升迁"
        },
        "verification_status": "verified"
    },
    {
        "id": "qstar_006",
        "term": "天心星",
        "pinyin": "tiānxīnxīng",
        "wuxing": "金",
        "position": "乾六宫",
        "category": "nine_stars",
        "system": "qimen",
        "nature": "吉星",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "九星总论",
            "page": 75
        },
        "original_content": "天心星，西北六之金，司刚毅决断之事。",
        "interpretation": "天心星代表决断和智慧，象征领导能力和决策力。",
        "general_meaning": {
            "fortune": "决策英明，办事果断",
            "career": "领导能力强，利于管理",
            "relationships": "有主见，但略显固执"
        },
        "favorable": {
            "activities": ["决策", "管理", "医疗", "卜筮"],
            "directions": ["西北方"]
        },
        "unfavorable": {
            "activities": ["和谈", "合作"],
            "note": "过于果断可能影响合作"
        },
        "keywords": ["决断", "智慧", "领导", "西北"],
        "combinations": {
            "with_door": "与开门：大吉，利事业",
            "with_god": "与九天：决策果断"
        },
        "verification_status": "verified"
    },
    {
        "id": "qstar_007",
        "term": "天柱星",
        "pinyin": "tiānzhùxīng",
        "wuxing": "金",
        "position": "兑七宫",
        "category": "nine_stars",
        "system": "qimen",
        "nature": "凶星",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "九星总论",
            "page": 78
        },
        "original_content": "天柱星，正西七之金，司破败争斗之事。",
        "interpretation": "天柱星代表破坏和争斗，象征破败和口舌。",
        "general_meaning": {
            "fortune": "易有破败，须防损失",
            "career": "竞争激烈，不宜冒进",
            "relationships": "易起口舌争执"
        },
        "favorable": {
            "activities": ["拆卸", "破坏", "诉讼", "谈判"],
            "directions": ["西方"]
        },
        "unfavorable": {
            "activities": ["嫁娶", "开业", "动土"],
            "note": "易有破败"
        },
        "keywords": ["破败", "争斗", "口舌", "西方"],
        "combinations": {
            "with_door": "与惊门：口舌是非",
            "with_god": "与白虎：破败更大"
        },
        "warning": "天柱为凶星，用事宜谨慎",
        "verification_status": "verified"
    },
    {
        "id": "qstar_008",
        "term": "天任星",
        "pinyin": "tiānrènxīng",
        "wuxing": "土",
        "position": "艮八宫",
        "category": "nine_stars",
        "system": "qimen",
        "nature": "吉星",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "九星总论",
            "page": 81
        },
        "original_content": "天任星，东北八之土，司争讼田土之事。",
        "interpretation": "天任星代表争讼和产业，象征勤劳和固执。",
        "general_meaning": {
            "fortune": "勤劳致富，但有争执",
            "career": "脚踏实地，但有阻碍",
            "relationships": "固执己见，易起争执"
        },
        "favorable": {
            "activities": ["务农", "建筑", "置业", "求职"],
            "directions": ["东北方"]
        },
        "unfavorable": {
            "activities": ["诉讼", "官司"],
            "note": "易有田土纠纷"
        },
        "keywords": ["争讼", "田土", "勤劳", "东北"],
        "combinations": {
            "with_door": "与生门：利求财",
            "with_god": "与九地：稳重保守"
        },
        "verification_status": "verified"
    },
    {
        "id": "qstar_009",
        "term": "天英星",
        "pinyin": "tiānyīngxīng",
        "wuxing": "火",
        "position": "离九宫",
        "category": "nine_stars",
        "system": "qimen",
        "nature": "次吉星",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "九星总论",
            "page": 84
        },
        "original_content": "天英星，正南九之火，司文章声名之事。",
        "interpretation": "天英星代表文章和名声，象征才华和声誉。",
        "general_meaning": {
            "fortune": "名声显露，文采出众",
            "career": "利于演艺、文职、宣传",
            "relationships": "言语犀利，易得罪人"
        },
        "favorable": {
            "activities": ["写作", "演艺", "宣传", "考试"],
            "directions": ["南方"]
        },
        "unfavorable": {
            "activities": ["谈判", "签约"],
            "note": "言语过激可能影响合作"
        },
        "keywords": ["文章", "名声", "才华", "南方"],
        "combinations": {
            "with_door": "与景门：文章大吉",
            "with_god": "与螣蛇：文书纠纷"
        },
        "verification_status": "verified"
    }
]

STAR_RANKINGS = {
    "best": ["天辅星", "天心星"],
    "good": ["天禽星", "天任星", "天英星"],
    "average": [],
    "bad": ["天冲星", "天柱星"],
    "worst": ["天蓬星", "天芮星"]
}
