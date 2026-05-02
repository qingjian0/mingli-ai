"""
四化含义
紫微斗数四化飞星详解

四化包括：化禄（财禄）、化权（权力）、化科（功名）、化忌（灾祸）
四化是紫微斗数论断的核心依据
"""

ZIWEI_TRANSFORMS = [
    {
        "id": "transform_001",
        "term": "化禄",
        "pinyin": "huàlù",
        "element": "土",
        "category": "transform",
        "system": "ziwei",
        "nature": "吉化",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷三·四化论",
            "page": 65
        },
        "original_content": "化禄主财禄、欢乐，化入何宫何曜，皆主该宫该曜有增益之美。",
        "interpretation": "化禄代表财禄和欢乐，是最吉利的四化，象征增益和好运。",
        "general_meaning": {
            "fortune": "财运亨通，财源广进",
            "emotion": "心情愉快，享受生活",
            "luck": "福气增加，机遇增多"
        },
        "palace_effects": {
            "ming_gong": "一生福厚，财运佳",
            "cai_gong": "财运旺盛，理财得利",
            "guan_gong": "事业顺遂，晋升有望",
            "qi_gong": "姻缘美满，桃花运佳",
            "zi_gong": "儿女聪明，得子女之力",
            "fu_gong": "受祖上荫庇，享长辈之福"
        },
        "keywords": ["财禄", "欢乐", "增益", "福气", "好运"],
        "warning": "化禄不宜过多，过多则贪多不精，反成懒惰",
        "verification_status": "verified"
    },
    {
        "id": "transform_002",
        "term": "化权",
        "pinyin": "huàquán",
        "element": "火",
        "category": "transform",
        "system": "ziwei",
        "nature": "吉化",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷三·四化论",
            "page": 67
        },
        "original_content": "化权主权威、事业，化入何宫何曜，皆主该宫该曜有奋发之力。",
        "interpretation": "化权代表权威和事业，是积极的四化，象征权力和成就。",
        "general_meaning": {
            "authority": "权力增长，地位提升",
            "career": "事业进步，业绩突出",
            "determination": "意志坚定，执行力强"
        },
        "palace_effects": {
            "ming_gong": "领导力强，有权威",
            "guan_gong": "事业发达，权力增大",
            "cai_gong": "理财有方，掌控力强",
            "fu_gong": "与上司关系好，得提拔",
            "xiang_gong": "兄弟之间有竞争"
        },
        "keywords": ["权威", "事业", "权力", "成就", "奋发"],
        "warning": "化权过旺则刚愎自用，须防与人冲突",
        "verification_status": "verified"
    },
    {
        "id": "transform_003",
        "term": "化科",
        "pinyin": "huàkē",
        "element": "木",
        "category": "transform",
        "system": "ziwei",
        "nature": "吉化",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷三·四化论",
            "page": 69
        },
        "original_content": "化科主文章、功名，化入何宫何曜，皆主该宫该曜有科名之望。",
        "interpretation": "化科代表文章和功名，是文雅的四化，象征学业和名声。",
        "general_meaning": {
            "scholarship": "学业进步，金榜题名",
            "fame": "名声提升，声名远播",
            "wisdom": "智慧增长，才学出众"
        },
        "palace_effects": {
            "ming_gong": "聪明好学，才华出众",
            "guan_gong": "仕途功名，有晋升之望",
            "fu_gong": "得长辈提携，名声好",
            "yi_gong": "儿女学业好，得子女荣耀",
            "tian_gong": "田宅风水好，家宅安宁"
        },
        "keywords": ["文章", "功名", "学业", "名声", "智慧"],
        "warning": "化科不宜与化忌同宫，易有文人薄命之叹",
        "verification_status": "verified"
    },
    {
        "id": "transform_004",
        "term": "化忌",
        "pinyin": "huàjì",
        "element": "水",
        "category": "transform",
        "system": "ziwei",
        "nature": "凶化",
        "source": {
            "book": "紫微斗数全书",
            "chapter": "卷三·四化论",
            "page": 71
        },
        "original_content": "化忌主是非、灾祸，化入何宫何曜，皆主该宫该曜有阻碍不美。",
        "interpretation": "化忌代表是非和灾祸，是最不利的四化，象征阻碍和困厄。",
        "general_meaning": {
            "obstacle": "阻碍重重，事多不顺",
            "dispute": "是非口舌，易生纷争",
            "loss": "破耗损失，财务问题"
        },
        "palace_effects": {
            "ming_gong": "命运多舛，阻碍多",
            "cai_gong": "财运不佳，破财",
            "guan_gong": "事业受阻，仕途不顺",
            "qi_gong": "姻缘不利，婚恋波折",
            "fu_gong": "与上司关系差或受小人陷害",
            "ji_gong": "健康不佳，易生疾病"
        },
        "keywords": ["是非", "灾祸", "阻碍", "困厄", "波折"],
        "warning": "化忌并非全凶，有时是考验和磨练，应理性看待",
        "verification_status": "verified"
    }
]

TRANSFORM_STAR_MAPPINGS = {
    "甲年": {
        "lian_zhen": "化禄",
        "tian_ji": "化权",
        "wu_qu": "化科",
        "ri_ji": "化忌"
    },
    "乙年": {
        "tian_ji": "化禄",
        "tian_tong": "化权",
        "tai_yin": "化科",
        "yang_ren": "化忌"
    },
    "丙年": {
        "tian_tong": "化禄",
        "tian_liang": "化权",
        "wu_qu": "化科",
        "tai_yang": "化忌"
    },
    "丁年": {
        "ju_men": "化禄",
        "tian_xiang": "化权",
        "tian_ji": "化科",
        "tai_yin": "化忌"
    },
    "戊年": {
        "tan_lang": "化禄",
        "wu_qu": "化权",
        "zi_wei": "化科",
        "tian_ji": "化忌"
    },
    "己年": {
        "wu_qu": "化禄",
        "tan_lang": "化权",
        "tian_xiang": "化科",
        "ji_wu": "化忌"
    },
    "庚年": {
        "tai_yang": "化禄",
        "tai_yin": "化权",
        "tian_ji": "化科",
        "tian_tong": "化忌"
    },
    "辛年": {
        "tai_yin": "化禄",
        "ju_men": "化权",
        "tian_ji": "化科",
        "tan_lang": "化忌"
    },
    "壬年": {
        "po_jun": "化禄",
        "tian_ji": "化权",
        "tian_liang": "化科",
        "wu_qu": "化忌"
    },
    "癸年": {
        "tian_ji": "化禄",
        "lu_cun": "化权",
        "tian_xiang": "化科",
        "po_jun": "化忌"
    }
}
