"""
八门含义
奇门遁甲八门的详细解释

八门：休门、生门、伤门、杜门、景门、死门、惊门、开门
"""

QIMEN_DOORS = [
    {
        "id": "door_001",
        "term": "休门",
        "pinyin": "xiūmén",
        "wuxing": "水",
        "position": "坎一宫",
        "category": "eight_doors",
        "system": "qimen",
        "nature": "吉门",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八门总论",
            "page": 35
        },
        "original_content": "休门者，休养安息也。属水，旺于冬。",
        "interpretation": "休门代表休养、休息、安宁，象征和谐与平稳。",
        "general_meaning": {
            "fortune": "平稳安宁，适合休息",
            "career": "宜守不宜攻，适合稳定发展",
            "relationships": "人际和谐，利于谈判"
        },
        "favorable": {
            "activities": ["休息", "养生", "和谈", "调解", "休闲"],
            "directions": ["北方", "东北方"]
        },
        "unfavorable": {
            "activities": ["冒险", "创业", "竞争", "动武"],
            "note": "过于保守可能错失良机"
        },
        "keywords": ["休养", "安宁", "和谐", "平稳"],
        "combinations": {
            "with_star": "遇天辅星：大吉，利升迁",
            "with_god": "遇六合：婚姻和合，利嫁娶"
        },
        "verification_status": "verified"
    },
    {
        "id": "door_002",
        "term": "生门",
        "pinyin": "shēngmén",
        "wuxing": "土",
        "position": "艮八宫",
        "category": "eight_doors",
        "system": "qimen",
        "nature": "吉门",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八门总论",
            "page": 38
        },
        "original_content": "生门者，生长万物也。属土，旺于四季。",
        "interpretation": "生门代表生机、生长、财禄，象征生机勃勃和财运。",
        "general_meaning": {
            "fortune": "财运亨通，财源广进",
            "career": "利于创业、投资、洽谈",
            "health": "生机旺盛，健康恢复"
        },
        "favorable": {
            "activities": ["创业", "投资", "求财", "种植", "建筑"],
            "directions": ["东北方", "西南方"]
        },
        "unfavorable": {
            "activities": ["丧事", "埋葬", "破坏"],
            "note": "不宜与死门同宫"
        },
        "keywords": ["生机", "财禄", "生长", "财运"],
        "combinations": {
            "with_star": "遇天辅星：天赐财源，大吉",
            "with_god": "遇九天：利创业，大展宏图"
        },
        "verification_status": "verified"
    },
    {
        "id": "door_003",
        "term": "伤门",
        "pinyin": "shāngmén",
        "wuxing": "木",
        "position": "震三宫",
        "category": "eight_doors",
        "system": "qimen",
        "nature": "凶门",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八门总论",
            "page": 41
        },
        "original_content": "伤门者，伤害损害也。属木，旺于春。",
        "interpretation": "伤门代表伤害、损失、刑伤，象征破坏和伤害。",
        "general_meaning": {
            "fortune": "易有损失，财来财去",
            "career": "竞争激烈，易有阻滞",
            "health": "易有伤病，需注意安全"
        },
        "favorable": {
            "activities": ["讨债", "追债", "抓贼", "狩猎", "竞争"],
            "directions": ["东方", "东南方"],
            "note": "伤门利于讨债、追捕"
        },
        "unfavorable": {
            "activities": ["嫁娶", "移居", "开业", "谈判"],
            "note": "易有伤害和损失"
        },
        "keywords": ["伤害", "损失", "刑伤", "竞争"],
        "combinations": {
            "with_star": "遇天冲星：易出意外",
            "with_god": "遇白虎：大凶，防血光之灾"
        },
        "warning": "伤门为凶门，用事宜谨慎",
        "verification_status": "verified"
    },
    {
        "id": "door_004",
        "term": "杜门",
        "pinyin": "dùmén",
        "wuxing": "木",
        "position": "巽四宫",
        "category": "eight_doors",
        "system": "qimen",
        "nature": "平门",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八门总论",
            "page": 44
        },
        "original_content": "杜门者，堵塞闭塞也。属木，旺于春。",
        "interpretation": "杜门代表堵塞、隐蔽、困难，象征障碍和不通。",
        "general_meaning": {
            "fortune": "阻碍较多，进退两难",
            "career": "进展缓慢，需耐心等待",
            "relationships": "沟通不畅，易有隔阂"
        },
        "favorable": {
            "activities": ["躲藏", "逃亡", "保密", "学习", "修炼"],
            "directions": ["东南", "东南方"],
            "note": "利于躲藏和保密"
        },
        "unfavorable": {
            "activities": ["开业", "谈判", "出行", "搬家"],
            "note": "易有阻碍，不宜冒进"
        },
        "keywords": ["堵塞", "隐蔽", "障碍", "不通"],
        "combinations": {
            "with_star": "遇天辅星：利于学习、进修",
            "with_god": "遇太阴：利于保密、隐藏"
        },
        "verification_status": "verified"
    },
    {
        "id": "door_005",
        "term": "景门",
        "pinyin": "jǐngmén",
        "wuxing": "火",
        "position": "离九宫",
        "category": "eight_doors",
        "system": "qimen",
        "nature": "平门",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八门总论",
            "page": 47
        },
        "original_content": "景门者，光明显现也。属火，旺于夏。",
        "interpretation": "景门代表光明、显现、文采，象征表露和展示。",
        "general_meaning": {
            "fortune": "名声显露，利于展示",
            "career": "利于演说、广告、宣传",
            "relationships": "坦诚相待，利于表达"
        },
        "favorable": {
            "activities": ["演说", "广告", "文书", "考试", "展示"],
            "directions": ["南方", "东南方"],
            "note": "利于文书和表达"
        },
        "unfavorable": {
            "activities": ["阴谋", "隐秘", "暗算"],
            "note": "景门光明，不宜暗事"
        },
        "keywords": ["光明", "显现", "文采", "展示"],
        "combinations": {
            "with_star": "遇天英星：文采飞扬，利考试",
            "with_god": "遇螣蛇：文书纠纷，防假象"
        },
        "verification_status": "verified"
    },
    {
        "id": "door_006",
        "term": "死门",
        "pinyin": "sǐmén",
        "wuxing": "土",
        "position": "坤二宫",
        "category": "eight_doors",
        "system": "qimen",
        "nature": "凶门",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八门总论",
            "page": 50
        },
        "original_content": "死门者，死亡凶恶也。属土，旺于夏末。",
        "interpretation": "死门代表死亡、凶恶、绝望，象征最不吉利的能量。",
        "general_meaning": {
            "fortune": "大凶，诸事不宜",
            "career": "事业停滞，难有发展",
            "health": "健康不佳，须防重病"
        },
        "favorable": {
            "activities": ["丧事", "埋葬", "捕猎", "诛杀"],
            "directions": ["西南方"],
            "note": "仅利于丧葬和捕猎"
        },
        "unfavorable": {
            "activities": ["开业", "嫁娶", "搬家", "出行", "谈判"],
            "note": "大凶，绝对不宜"
        },
        "keywords": ["死亡", "凶恶", "绝望", "大凶"],
        "combinations": {
            "with_star": "遇天芮星：大凶，防重病",
            "with_god": "遇白虎：极凶，血光之灾"
        },
        "warning": "死门为大凶之门，用事宜极为谨慎",
        "verification_status": "verified"
    },
    {
        "id": "door_007",
        "term": "惊门",
        "pinyin": "jīngmén",
        "wuxing": "金",
        "position": "兑七宫",
        "category": "eight_doors",
        "system": "qimen",
        "nature": "凶门",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八门总论",
            "page": 53
        },
        "original_content": "惊门者，惊惶惊恐也。属金，旺于秋。",
        "interpretation": "惊门代表惊恐、纷争、口舌，象征是非和不安。",
        "general_meaning": {
            "fortune": "易有惊吓，是非口舌",
            "career": "易有纷争，须防小人",
            "relationships": "易起争执，沟通困难"
        },
        "favorable": {
            "activities": ["捕捉", "声讨", "举报", "投诉"],
            "directions": ["西方", "西北方"],
            "note": "利于申诉、举报"
        },
        "unfavorable": {
            "activities": ["开业", "嫁娶", "签约", "谈判"],
            "note": "易有惊恐和纠纷"
        },
        "keywords": ["惊恐", "纷争", "口舌", "是非"],
        "combinations": {
            "with_star": "遇天柱星：易出惊恐之事",
            "with_god": "遇螣蛇：惊恐万分，防怪异"
        },
        "warning": "惊门为凶门，利于申诉但诸事不宜",
        "verification_status": "verified"
    },
    {
        "id": "door_008",
        "term": "开门",
        "pinyin": "kāimén",
        "wuxing": "金",
        "position": "乾六宫",
        "category": "eight_doors",
        "system": "qimen",
        "nature": "吉门",
        "source": {
            "book": "奇门遁甲全书",
            "chapter": "八门总论",
            "page": 56
        },
        "original_content": "开门者，通达开放也。属金，旺于秋。",
        "interpretation": "开门代表开放、通达、事业，象征发展和扩张。",
        "general_meaning": {
            "fortune": "诸事大吉，前途光明",
            "career": "利于开业、求职、升迁",
            "relationships": "开放坦诚，利于社交"
        },
        "favorable": {
            "activities": ["开业", "求职", "升迁", "远行", "谈判"],
            "directions": ["西北方", "北方"],
            "note": "开门为最吉之门"
        },
        "unfavorable": {
            "activities": ["密谋", "隐蔽"],
            "note": "过于开放，不宜密谋"
        },
        "keywords": ["开放", "通达", "发展", "事业"],
        "combinations": {
            "with_star": "遇天心星：利于医卜，利决策",
            "with_god": "遇九天：大吉，利远行"
        },
        "verification_status": "verified"
    }
]

DOOR_RANKINGS = {
    "best": ["开门", "生门"],
    "good": ["休门"],
    "average": ["景门", "杜门"],
    "bad": ["伤门", "惊门"],
    "worst": ["死门"]
}
