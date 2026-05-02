"""
爻辞
易经六爻详解

包含各卦六爻的爻辞、爻象、小象传等完整信息
"""

YAO_MEANINGS = {
    "乾": [
        {
            "position": 1,
            "name": "初九",
            "yaoci": "潜龙勿用",
            "xiaoxiang": "潜龙勿用，阳在下也",
            "interpretation": "龙潜深渊，时机未到，宜静待时机。",
            "keywords": ["潜伏", "静待", "潜藏", "勿用"],
            "fortune": "宜守不宜动，积蓄力量"
        },
        {
            "position": 2,
            "name": "九二",
            "yaoci": "见龙在田，利见大人",
            "xiaoxiang": "见龙在田，德施普也",
            "interpretation": "龙现于田，贵人出现，宜积极进取。",
            "keywords": ["显现", "贵人", "田地", "利见"],
            "fortune": "得贵人相助，宜把握机会"
        },
        {
            "position": 3,
            "name": "九三",
            "yaoci": "君子终日乾乾，夕惕若厉，无咎",
            "xiaoxiang": "终日乾乾，反复道也",
            "interpretation": "君子勤勉不懈，时刻警惕，可免于咎。",
            "keywords": ["勤勉", "警惕", "谨慎", "无咎"],
            "fortune": "勤勉谨慎，自强不息"
        },
        {
            "position": 4,
            "name": "九四",
            "yaoci": "或跃在渊，无咎",
            "xiaoxiang": "或跃在渊，进无咎也",
            "interpretation": "龙跃深渊，进退有据，可无咎害。",
            "keywords": ["跳跃", "进退", "深渊", "或跃"],
            "fortune": "进退有度，审时度势"
        },
        {
            "position": 5,
            "name": "九五",
            "yaoci": "飞龙在天，利见大人",
            "xiaoxiang": "飞龙在天，大人造也",
            "interpretation": "龙飞于天，大人成就功业，顶峰之象。",
            "keywords": ["飞腾", "在天", "大人", "造化"],
            "fortune": "功成名就，登峰造极"
        },
        {
            "position": 6,
            "name": "上九",
            "yaoci": "亢龙有悔",
            "xiaoxiang": "亢龙有悔，盈不可久也",
            "interpretation": "龙飞过高则有悔，知进退之理。",
            "keywords": ["亢进", "有悔", "盈满", "不可久"],
            "fortune": "物极必反，宜退不宜进"
        },
        {
            "position": 7,
            "name": "用九",
            "yaoci": "见群龙无首，吉",
            "xiaoxiang": "用九，天德不可为首也",
            "interpretation": "群龙无首而能协同，则吉。",
            "keywords": ["群龙", "无首", "协同", "天德"],
            "fortune": "刚柔并济，吉祥如意"
        }
    ],
    "坤": [
        {
            "position": 1,
            "name": "初六",
            "yaoci": "履霜，坚冰至",
            "xiaoxiang": "履霜坚冰，阴始凝也。驯致其道，至坚冰也",
            "interpretation": "脚下踩到霜，寒冬将至，预兆事物的渐进变化。",
            "keywords": ["履霜", "坚冰", "阴凝", "驯致"],
            "fortune": "见微知著，防患未然"
        },
        {
            "position": 2,
            "name": "六二",
            "yaoci": "直方大，不习无不利",
            "xiaoxiang": "六二之动，直以方也。不习无不利，地道光也",
            "interpretation": "正直端方，行为大方，不学也无不利。",
            "keywords": ["正直", "端方", "大方", "地道"],
            "fortune": "品性纯正，自然有利"
        },
        {
            "position": 3,
            "name": "六三",
            "yaoci": "含章可贞。或从王事，无成有终",
            "xiaoxiang": "含章可贞，以时发也。或从王事，知光大也",
            "interpretation": "内含美德可以守正，若从事王事，虽无成就却有好的结果。",
            "keywords": ["含章", "可贞", "王事", "有终"],
            "fortune": "内敛含蓄，功成不居"
        },
        {
            "position": 4,
            "name": "六四",
            "yaoci": "括囊，无咎无誉",
            "xiaoxiang": "括囊无咎，慎不害也",
            "interpretation": "扎紧口袋，谨慎不言，可免咎害。",
            "keywords": ["括囊", "缄默", "谨慎", "无害"],
            "fortune": "守口如瓶，明哲保身"
        },
        {
            "position": 5,
            "name": "六五",
            "yaoci": "黄裳，元吉",
            "xiaoxiang": "黄裳元吉，文在中也",
            "interpretation": "黄色下裳，大为吉祥，美德在中。",
            "keywords": ["黄裳", "元吉", "文明", "中道"],
            "fortune": "居中守正，大吉之象"
        },
        {
            "position": 6,
            "name": "上六",
            "yaoci": "龙战于野，其血玄黄",
            "xiaoxiang": "龙战于野，其道穷也",
            "interpretation": "龙战于野，其道穷尽，阴阳交战。",
            "keywords": ["龙战", "玄黄", "道穷", "阴阳"],
            "fortune": "穷则生变，防微杜渐"
        },
        {
            "position": 7,
            "name": "用六",
            "yaoci": "利永贞",
            "xiaoxiang": "用六永贞，以大终也",
            "interpretation": "利于永久守正，方有好的结局。",
            "keywords": ["永贞", "大终", "地道"],
            "fortune": "持之以恒，善始善终"
        }
    ],
    "屯": [
        {
            "position": 1,
            "name": "初九",
            "yaoci": "磐桓，利居贞，利建侯",
            "xiaoxiang": "虽磐桓，志行正也。以贵下贱，大得民也",
            "interpretation": "徘徊不进，利于守正，利于建立功业。",
            "keywords": ["磐桓", "居贞", "建侯", "下贱"],
            "fortune": "艰难中求进，稳扎稳打"
        },
        {
            "position": 2,
            "name": "六二",
            "yaoci": "屯如邅如，乘马班如。匪寇婚媾，女子贞不字，十年乃字",
            "xiaoxiang": "六二之难，乘刚也。十年乃字，反常也",
            "interpretation": "艰难辗转，乘马盘旋，非寇是婚，女贞不嫁，十年方嫁。",
            "keywords": ["屯如", "邅如", "班如", "婚媾"],
            "fortune": "时机未到，耐心等待"
        },
        {
            "position": 3,
            "name": "六三",
            "yaoci": "即鹿无虞，惟入于林中，君子几不如舍，往吝",
            "xiaoxiang": "即鹿无虞，以从禽也。君子几不如舍，往吝穷也",
            "interpretation": "逐鹿无向导，入于林中，君子见机不如舍弃，前往则有难。",
            "keywords": ["即鹿", "无虞", "几", "不如舍"],
            "fortune": "盲目冒进必有所失"
        },
        {
            "position": 4,
            "name": "六四",
            "yaoci": "乘马班如，求婚媾，往吉，无不利",
            "xiaoxiang": "求而往，明也",
            "interpretation": "乘马盘旋，前往求婚，前往则吉，无所不利。",
            "keywords": ["班如", "婚媾", "前往", "无不利"],
            "fortune": "主动求婚，得偿所愿"
        },
        {
            "position": 5,
            "name": "九五",
            "yaoci": "屯其膏，小贞吉，大贞凶",
            "xiaoxiang": "屯其膏，施未光也",
            "interpretation": "囤积膏泽，小事守正则吉，大事守正则凶。",
            "keywords": ["屯膏", "小贞", "大贞", "施未光"],
            "fortune": "资源有限，当审慎使用"
        },
        {
            "position": 6,
            "name": "上六",
            "yaoci": "乘马班如，泣血涟如",
            "xiaoxiang": "泣血涟如，何可长也",
            "interpretation": "乘马盘旋，泣血涟涟，忧伤何可长久。",
            "keywords": ["泣血", "涟如", "忧伤", "不长"],
            "fortune": "忧患之中，难以持久"
        }
    ],
    "蒙": [
        {
            "position": 1,
            "name": "初六",
            "yaoci": "发蒙，利用刑人，用说桎梏以往，吝",
            "xiaoxiang": "利用刑人，以正法也",
            "interpretation": "启发蒙昧，利于惩治犯人，解脱刑具则有过失。",
            "keywords": ["发蒙", "刑人", "桎梏", "以往"],
            "fortune": "教育需有度，过严则失"
        },
        {
            "position": 2,
            "name": "九二",
            "yaoci": "包蒙吉，纳妇吉，子克家",
            "xiaoxiang": "子克家，刚柔节也",
            "interpretation": "包容蒙昧则吉，纳妇则吉，子孙能兴家。",
            "keywords": ["包蒙", "纳妇", "克家", "刚柔"],
            "fortune": "包容教化，子孙有成"
        },
        {
            "position": 3,
            "name": "六三",
            "yaoci": "勿用取女，见金夫，不有躬，无攸利",
            "xiaoxiang": "勿用取女，行不顺也",
            "interpretation": "不可娶此女，见美男则失身，无所利。",
            "keywords": ["取女", "金夫", "不有躬", "不顺"],
            "fortune": "女子失贞，婚事不吉"
        },
        {
            "position": 4,
            "name": "六四",
            "yaoci": "困蒙，吝",
            "xiaoxiang": "困蒙之吝，独远实也",
            "interpretation": "困于蒙昧，有所憾惜。",
            "keywords": ["困蒙", "吝", "独远"],
            "fortune": "困于蒙昧，需勤学好问"
        },
        {
            "position": 5,
            "name": "六五",
            "yaoci": "童蒙，吉",
            "xiaoxiang": "童蒙之吉，顺以巽也",
            "interpretation": "童蒙则吉，柔顺而谦逊。",
            "keywords": ["童蒙", "吉", "顺巽"],
            "fortune": "纯朴求知，大吉之象"
        },
        {
            "position": 6,
            "name": "上九",
            "yaoci": "击蒙，不利为寇，利御寇",
            "xiaoxiang": "利用御寇，上下顺也",
            "interpretation": "击打蒙昧，利于防御盗贼，不利于主动攻击。",
            "keywords": ["击蒙", "御寇", "上下顺"],
            "fortune": "以刚克蒙，防御为上"
        }
    ],
    "需": [
        {
            "position": 1,
            "name": "初九",
            "yaoci": "需于郊，利用恒，无咎",
            "xiaoxiang": "需于郊，不犯难行也。利用恒，无咎，未失常也",
            "interpretation": "在郊外等待，利于恒心守正，可无咎害。",
            "keywords": ["需于郊", "利用恒", "无咎", "未失常"],
            "fortune": "耐心等待，不失常态"
        },
        {
            "position": 2,
            "name": "九二",
            "yaoci": "需于沙，小有言，终吉",
            "xiaoxiang": "需于沙，衍在中也。虽小有言，以吉终也",
            "interpretation": "在沙地等待，稍有言语责难，终则吉。",
            "keywords": ["需于沙", "小有言", "终吉"],
            "fortune": "虽有波折，终获吉祥"
        },
        {
            "position": 3,
            "name": "九三",
            "yaoci": "需于泥，致寇至",
            "xiaoxiang": "需于泥，灾在外也。自我致寇，敬慎不败也",
            "interpretation": "在泥中等待，招致贼寇，自我招祸，谨慎可不败。",
            "keywords": ["需于泥", "致寇", "敬慎"],
            "fortune": "自我招祸，谨慎可解"
        },
        {
            "position": 4,
            "name": "六四",
            "yaoci": "需于血，出自穴",
            "xiaoxiang": "需于血，顺以听也",
            "interpretation": "在血泊中等待，从洞穴中脱出。",
            "keywords": ["需于血", "出自穴", "顺听"],
            "fortune": "历经艰险，终可脱困"
        },
        {
            "position": 5,
            "name": "九五",
            "yaoci": "需于酒食，贞吉",
            "xiaoxiang": "酒食贞吉，以中正也",
            "interpretation": "在酒食中等待，守正则吉。",
            "keywords": ["酒食", "贞吉", "中正"],
            "fortune": "守中持正，大吉之象"
        },
        {
            "position": 6,
            "name": "上六",
            "yaoci": "入于穴，有不速之客三人来，敬之终吉",
            "xiaoxiang": "不速之客来，敬之终吉。虽不当位，未大失也",
            "interpretation": "进入洞穴，有不请自来的客人三人，敬重他们则终吉。",
            "keywords": ["入穴", "不速", "三人", "敬之"],
            "fortune": "意外来客，恭敬待之"
        }
    ],
    "讼": [
        {
            "position": 1,
            "name": "初六",
            "yaoci": "不永所事，小有言，终吉",
            "xiaoxiang": "不永所事，讼不可长也。虽小有言，其辩明也",
            "interpretation": "不永终诉讼，虽有小言，终则吉。",
            "keywords": ["不永", "所事", "小言", "辩明"],
            "fortune": "诉讼不久，辩明则吉"
        },
        {
            "position": 2,
            "name": "九二",
            "yaoci": "不克讼，归而逋，其邑人三百户，无眚",
            "xiaoxiang": "不克讼，归而逋也。自下讼上，患至掇也",
            "interpretation": "诉讼不胜，归来逃避，其邑三百户无忧。",
            "keywords": ["不克", "逋", "三百户", "无眚"],
            "fortune": "讼而不胜，退避可解"
        },
        {
            "position": 3,
            "name": "六三",
            "yaoci": "食旧德，贞厉，终吉，或从王事，无成",
            "xiaoxiang": "食旧德，从上吉也",
            "interpretation": "享受旧日德泽，守正有危，终则吉，或从事王事则无成。",
            "keywords": ["食德", "贞厉", "终吉", "无成"],
            "fortune": "守成有道，终获吉祥"
        },
        {
            "position": 4,
            "name": "九四",
            "yaoci": "不克讼，复即命，渝安贞，吉",
            "xiaoxiang": "复即命，渝安贞，不失也",
            "interpretation": "诉讼不胜，回头顺命，改变守正则吉。",
            "keywords": ["复即", "命渝", "安贞", "吉"],
            "fortune": "改过自新，转危为安"
        },
        {
            "position": 5,
            "name": "九五",
            "yaoci": "讼，元吉",
            "xiaoxiang": "讼元吉，以中正也",
            "interpretation": "诉讼，大为吉祥。",
            "keywords": ["讼", "元吉", "中正"],
            "fortune": "中正诉讼，大吉之象"
        },
        {
            "position": 6,
            "name": "上九",
            "yaoci": "或锡之鞶带，终朝三褫之",
            "xiaoxiang": "以讼受服，亦不足敬也",
            "interpretation": "或赐以官服，终朝三次夺之。",
            "keywords": ["锡鞶", "终朝", "三褫"],
            "fortune": "争来得官，不足为敬"
        }
    ]
}

YAO_POSITION_NAMES = {
    1: "初爻",
    2: "二爻",
    3: "三爻",
    4: "四爻",
    5: "五爻",
    6: "上爻",
    7: "用爻"
}

YAO_YANG_NAMES = ["初九", "九二", "九三", "九四", "九五", "上九", "用九"]
YAO_YIN_NAMES = ["初六", "六二", "六三", "六四", "六五", "上六", "用六"]
