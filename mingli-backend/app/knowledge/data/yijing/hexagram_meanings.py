"""
六十四卦含义
易经六十四卦详解

包含卦名、卦辞、象传、彖传、卦义等完整信息
"""

HEXAGRAM_MEANINGS = [
    {
        "id": "hex_001",
        "name": "乾为天",
        "guaxiang": "乾",
        "wuxing": "金",
        "sequence": 1,
        "guaci": "元亨利贞",
        "tuanci": "大哉乾元，万物资始，乃统天。云行雨施，品物流形。大明终始，六位时成，时乘六龙以御天。乾道变化，各正性命，保合大和，乃利贞。首出庶物，万国咸宁。",
        "xiang": "天行健，君子以自强不息",
        "interpretation": "乾为纯阳之卦，六爻皆阳，象征天道的刚健。",
        "meaning": {
            "positive": "刚健有力，积极进取，意志坚定",
            "caution": "过于刚强则折，宜刚柔并济"
        },
        "keywords": ["刚健", "进取", "领导", "创造", "天道"],
        "fortune": {
            "career": "事业大吉，适宜开创",
            "wealth": "财运亨通，宜进不宜退",
            "health": "阳气旺盛，健康佳",
            "relationships": "领导力强，宜主动出击"
        }
    },
    {
        "id": "hex_002",
        "name": "坤为地",
        "guaxiang": "坤",
        "wuxing": "土",
        "sequence": 2,
        "guaci": "元亨利牝马之贞。君子有攸往，先迷后得主。利西南得朋，东北丧朋。安贞吉",
        "tuanci": "至哉坤元，万物资生，乃顺承天。坤厚载物，德合无疆。含弘光大，品物咸亨。牝马地类，行地无疆，柔顺利贞。",
        "xiang": "地势坤，君子以厚德载物",
        "interpretation": "坤为纯阴之卦，六爻皆阴，象征地道的柔顺。",
        "meaning": {
            "positive": "柔顺宽厚，包容万物，稳步前进",
            "caution": "过于柔弱则失，宜刚柔相济"
        },
        "keywords": ["柔顺", "包容", "稳重", "厚德", "地道"],
        "fortune": {
            "career": "宜稳不宜急，稳扎稳打",
            "wealth": "财运平稳，宜积累",
            "health": "注意脾胃，健康平稳",
            "relationships": "人缘佳，宜以柔克刚"
        }
    },
    {
        "id": "hex_003",
        "name": "水雷屯",
        "guaxiang": "屯",
        "wuxing": "水",
        "sequence": 3,
        "guaci": "元亨利贞，勿用有攸往，利建侯",
        "tuanci": "屯，刚柔始交而难生，动乎险中，大亨贞。雷雨之动满盈，天造草昧，宜建侯而不宁。",
        "xiang": "云雷屯，君子以经纶",
        "interpretation": "屯为难之意，象征万物初生之艰难。",
        "meaning": {
            "positive": "艰难中求发展，蓄势待发",
            "caution": "万事开头难，宜耐心等待"
        },
        "keywords": ["艰难", "初生", "蓄势", "建侯", "创业"],
        "fortune": {
            "career": "创业初期，宜稳扎稳打",
            "wealth": "积累阶段，不宜冒进",
            "health": "注意调养，蓄势待发",
            "relationships": "结交贤友，建立人脉"
        }
    },
    {
        "id": "hex_004",
        "name": "山水蒙",
        "guaxiang": "蒙",
        "wuxing": "水",
        "sequence": 4,
        "guaci": "亨，匪我求童蒙，童蒙求我。初噬告，再三渎，渎则不告。利贞",
        "tuanci": "蒙，山下有险，险而止，蒙。蒙亨，以亨行时中也。匪我求童蒙，童蒙求我，志应也。",
        "xiang": "山下出泉，蒙。君子以果行育德",
        "interpretation": "蒙为蒙昧之意，象征幼稚和启蒙。",
        "meaning": {
            "positive": "启蒙教育，求知若渴",
            "caution": "蒙昧无知，宜虚心求学"
        },
        "keywords": ["蒙昧", "启蒙", "教育", "求知", "幼稚"],
        "fortune": {
            "career": "学习阶段，宜虚心请教",
            "wealth": "理财初期，宜谨慎",
            "health": "注意养护，成长发育",
            "relationships": "拜师学艺，结交良师"
        }
    },
    {
        "id": "hex_005",
        "name": "水天需",
        "guaxiang": "需",
        "wuxing": "水",
        "sequence": 5,
        "guaci": "有孚，光亨，贞吉。利涉大川",
        "tuanci": "需，须也，险在前也。刚健而不陷，其义不困穷矣。需有孚，光亨贞吉，位乎天位，以正中也。",
        "xiang": "云上于天，需。君子以饮食宴乐",
        "interpretation": "需为等待之意，象征时机未到需耐心等待。",
        "meaning": {
            "positive": "耐心等待时机，光明在前",
            "caution": "时机未到，不可冒进"
        },
        "keywords": ["等待", "耐心", "时机", "诚信", "蓄势"],
        "fortune": {
            "career": "时机未到，宜守待",
            "wealth": "积累准备，不宜冒险",
            "health": "调养身心，等待时机",
            "relationships": "以诚待人，结交知己"
        }
    },
    {
        "id": "hex_006",
        "name": "天水讼",
        "guaxiang": "讼",
        "wuxing": "火",
        "sequence": 6,
        "guaci": "有孚，窒惕，中吉，终凶。利见大人，不利涉大川",
        "tuanci": "讼，上刚下险，险而健，讼。讼有孚，窒惕中吉，刚来而得中也。终凶，讼不可成也。",
        "xiang": "天与水违行，讼。君子以作事谋始",
        "interpretation": "讼为争讼之意，象征与人争执是非。",
        "meaning": {
            "positive": "明辨是非，化解纷争",
            "caution": "争讼有凶，宜和为贵"
        },
        "keywords": ["争讼", "是非", "纷争", "谋始", "辨别"],
        "fortune": {
            "career": "防纠纷，宜协商解决",
            "wealth": "防小人，守住成果",
            "health": "注意肝气，调和情志",
            "relationships": "以和为贵，避免争执"
        }
    },
    {
        "id": "hex_007",
        "name": "地水师",
        "guaxiang": "师",
        "wuxing": "水",
        "sequence": 7,
        "guaci": "贞，丈人吉，无咎",
        "tuanci": "师，众也，贞正也，能以众正，可以王矣。刚中而应，行险而顺，以此毒天下，而民从之，吉又何咎矣。",
        "xiang": "地中有水，师。君子以容民畜众",
        "interpretation": "师为众之意，象征兵众和领导众人。",
        "meaning": {
            "positive": "领导有方，众人归心",
            "caution": "严明纪律，以正治众"
        },
        "keywords": ["兵众", "领导", "纪律", "容民", "畜众"],
        "fortune": {
            "career": "领导有方，宜任要职",
            "wealth": "众人相助，财运渐佳",
            "health": "注意调养，稳健为上",
            "relationships": "得人信任，有凝聚力"
        }
    },
    {
        "id": "hex_008",
        "name": "水地比",
        "guaxiang": "比",
        "wuxing": "水",
        "sequence": 8,
        "guaci": "吉。原筮元永贞，无咎。不宁方来，后夫凶",
        "tuanci": "比，吉也。比，辅也，下顺从也。原筮元永贞，无咎，以刚中也。不宁方来，上下应也。后夫凶，其道穷也。",
        "xiang": "地上有水，比。先王以建万国，亲诸侯",
        "interpretation": "比为亲辅之意，象征亲比和归顺。",
        "meaning": {
            "positive": "亲比和顺，众人归附",
            "caution": "择善而从，勿随波逐流"
        },
        "keywords": ["亲比", "归顺", "辅佐", "和顺", "万国"],
        "fortune": {
            "career": "得贵人相助，事业顺利",
            "wealth": "合作共赢，财运提升",
            "health": "平和稳定，注意调养",
            "relationships": "广结善缘，亲近贤能"
        }
    },
    {
        "id": "hex_009",
        "name": "风天小畜",
        "guaxiang": "小畜",
        "wuxing": "木",
        "sequence": 9,
        "guaci": "亨。密云不雨，自我西郊",
        "tuanci": "小畜，柔得位而上下应之，曰小畜。健而巽，刚中而志行，乃亨。密云不雨，尚往也。自我西郊，施未行也。",
        "xiang": "风行天上，小畜。君子以懿文德",
        "interpretation": "小畜为小有蓄积之意，象征初有成就但尚未充实。",
        "meaning": {
            "positive": "小有积蓄，渐有成就",
            "caution": "力量尚小，不宜大动"
        },
        "keywords": ["蓄积", "小成", "懿文", "密云", "未雨"],
        "fortune": {
            "career": "初有成效，宜稳扎稳打",
            "wealth": "小有积蓄，不宜冒进",
            "health": "调养为主，蓄势待发",
            "relationships": "积累人脉，等待时机"
        }
    },
    {
        "id": "hex_010",
        "name": "天泽履",
        "guaxiang": "履",
        "wuxing": "金",
        "sequence": 10,
        "guaci": "履虎尾，不咥人，亨",
        "tuanci": "履，柔履刚也。说而应乎乾，是以履虎尾，不咥人，亨。刚中正，履帝位而不疚，光明也。",
        "xiang": "上天下泽，履。君子以辨上下，定民志",
        "interpretation": "履为履行之意，象征谨慎行事以避免危险。",
        "meaning": {
            "positive": "谨慎行事，化险为夷",
            "caution": "如履薄冰，小心翼翼"
        },
        "keywords": ["履行", "谨慎", "辨别", "定志", "小心翼翼"],
        "fortune": {
            "career": "谨慎行事，可获成功",
            "wealth": "守成为主，不宜冒险",
            "health": "谨慎调养，防意外",
            "relationships": "以礼待人，和睦相处"
        }
    },
    {
        "id": "hex_011",
        "name": "地天泰",
        "guaxiang": "泰",
        "wuxing": "土",
        "sequence": 11,
        "guaci": "小往大来，吉亨",
        "tuanci": "泰，小往大来，吉亨，则是天地交而万物通也，上下交而其志同也。内阳而外阴，内健而外顺，内君子而外小人，君子道长，小人道消也。",
        "xiang": "天地交，泰。后以财成天地之道，辅相天地之宜，以左右民",
        "interpretation": "泰为通泰之意，象征天地交泰，万事亨通。",
        "meaning": {
            "positive": "通泰顺利，万事亨通",
            "caution": "泰极否来，宜守成"
        },
        "keywords": ["通泰", "亨通", "交泰", "阴阳", "盛世"],
        "fortune": {
            "career": "诸事大吉，宜把握时机",
            "wealth": "财运亨通，收益丰厚",
            "health": "身心舒畅，健康佳",
            "relationships": "关系和谐，众人相助"
        }
    },
    {
        "id": "hex_012",
        "name": "天地否",
        "guaxiang": "否",
        "wuxing": "金",
        "sequence": 12,
        "guaci": "否之匪人，不利君子贞，大往小来",
        "tuanci": "否之匪人，不利君子贞，大往小来，则是天地不交而万物不通也，上下不交而天下无邦也。内阴而外阳，内柔而外刚，内小人而外君子，小人道长，君子道消也。",
        "xiang": "天地不交，否。君子以俭德辟难，不可荣以禄",
        "interpretation": "否为闭塞之意，象征天地不交，万事阻滞。",
        "meaning": {
            "positive": "闭塞中守正，静待转机",
            "caution": "诸事不顺，宜守不宜动"
        },
        "keywords": ["闭塞", "阻滞", "不通", "俭德", "辟难"],
        "fortune": {
            "career": "事业受阻，宜静待时机",
            "wealth": "财运不佳，宜守成",
            "health": "注意调理，防疾病",
            "relationships": "人际关系差，宜低调"
        }
    },
    {
        "id": "hex_013",
        "name": "天火同人",
        "guaxiang": "同人",
        "wuxing": "火",
        "sequence": 13,
        "guaci": "同人于野，亨。利涉大川，利君子贞",
        "tuanci": "同人，柔得位得中，而应乎乾，曰同人。同人曰，同人于野，亨，利涉大川，乾行也。文明以健，中正而应，君子正也。唯君子为能通天下之志。",
        "xiang": "天与火，同人。君子以类族辨物",
        "interpretation": "同人为与人同心之意，象征志同道合。",
        "meaning": {
            "positive": "志同道合，众望所归",
            "caution": "和而不同，勿强求一致"
        },
        "keywords": ["同人", "同心", "志同道合", "类族", "辨物"],
        "fortune": {
            "career": "得同道相助，事业顺利",
            "wealth": "合作有利，财运提升",
            "health": "心情舒畅，健康佳",
            "relationships": "广结同道，人脉广泛"
        }
    },
    {
        "id": "hex_014",
        "name": "火天大有",
        "guaxiang": "大有",
        "wuxing": "火",
        "sequence": 14,
        "guaci": "元亨",
        "tuanci": "大有，柔得尊位，大中而上下应之，曰大有。其德刚健而文明，应乎天而时行，是以元亨。",
        "xiang": "火在天上，大有。君子以遏恶扬善，顺天休命",
        "interpretation": "大有为丰盛众多之意，象征富有和收获。",
        "meaning": {
            "positive": "丰盛富有，诸事大吉",
            "caution": "满则招损，宜谦逊守成"
        },
        "keywords": ["富有", "丰盛", "丰获", "遏恶", "扬善"],
        "fortune": {
            "career": "事业鼎盛，收益丰厚",
            "wealth": "财运极佳，富有吉祥",
            "health": "精力充沛，健康佳",
            "relationships": "众星拱照，人际和谐"
        }
    },
    {
        "id": "hex_015",
        "name": "地山谦",
        "guaxiang": "谦",
        "wuxing": "土",
        "sequence": 15,
        "guaci": "亨，君子有终",
        "tuanci": "谦，亨，天道下济而光明，地道卑而上行。天道亏盈而益谦，地道变盈而流谦，鬼神害盈而福谦，人道恶盈而好谦。谦尊而光，卑而不可逾，君子之终也。",
        "xiang": "地中有山，谦。君子以裒多益寡，称物平施",
        "interpretation": "谦为谦逊之意，象征谦受益满招损。",
        "meaning": {
            "positive": "谦逊有德，终得吉祥",
            "caution": "谦谦君子，卑以自牧"
        },
        "keywords": ["谦逊", "谦让", "裒多", "益寡", "平施"],
        "fortune": {
            "career": "谦逊待人，终得好报",
            "wealth": "低调积累，稳健获利",
            "health": "心平气和，健康佳",
            "relationships": "谦以待人，得人敬重"
        }
    },
    {
        "id": "hex_016",
        "name": "雷地豫",
        "guaxiang": "豫",
        "wuxing": "木",
        "sequence": 16,
        "guaci": "利建侯行师",
        "tuanci": "豫，刚应而志行，顺以动，豫。豫顺以动，故天地如之，而况建侯行师乎？天地以顺动，故日月不过，而四时不忒。圣人以顺动，则刑罚清而民服。豫之时义大矣哉。",
        "xiang": "雷出地奋，豫。先王以作乐崇德，殷荐之上帝，以配祖考",
        "interpretation": "豫为欢乐之意，象征和乐愉悦和顺动。",
        "meaning": {
            "positive": "和乐愉悦，顺时而动",
            "caution": "乐极生悲，宜守中道"
        },
        "keywords": ["欢乐", "豫乐", "顺动", "崇德", "殷荐"],
        "fortune": {
            "career": "诸事顺遂，宜把握时机",
            "wealth": "财运不错，收益增加",
            "health": "心情愉悦，健康佳",
            "relationships": "和乐融融，人际和谐"
        }
    }
]
