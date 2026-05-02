"""
八字合冲刑害模块
定义地支之间的各种关系组合
"""

from typing import Dict, List, Set, Tuple
from .stems import STEM_INDICES
from .branches import BRANCH_INDICES, BRANCH_ORDER


class RelationType(str):
    """关系类型"""
    HE = "合"
    CHONG = "冲"
    XING = "刑"
    HAI = "害"
    SHENG = "生"
    KE = "克"


BRANCH_HE = {
    ("子", "丑"): "子丑合土",
    ("寅", "亥"): "寅亥合木",
    ("卯", "戌"): "卯戌合火",
    ("辰", "酉"): "辰酉合金",
    ("巳", "申"): "巳申合水",
    ("午", "未"): "午未合火土"
}

BRANCH_HE_STEMS = {
    ("子", "丑"): ["戊", "癸"],
    ("寅", "亥"): ["甲", "壬"],
    ("卯", "戌"): ["乙", "丁"],
    ("辰", "酉"): ["戊", "辛"],
    ("巳", "申"): ["丙", "庚"],
    ("午", "未"): ["丁", "己"]
}

BRANCH_CHONG = {
    ("子", "午"): "子午冲",
    ("丑", "未"): "丑未冲",
    ("寅", "申"): "寅申冲",
    ("卯", "酉"): "卯酉冲",
    ("辰", "戌"): "辰戌冲",
    ("巳", "亥"): "巳亥冲"
}

BRANCH_XING = {
    ("寅", "巳", "申"): "寅巳申三刑",
    ("丑", "戌", "未"): "丑戌未三刑",
    ("子", "卯"): "子卯相刑",
    ("辰", "辰"): "辰自刑",
    ("午", "午"): "午自刑",
    ("酉", "酉"): "酉自刑",
    ("亥", "亥"): "亥自刑",
    ("戌", "丑"): "丑戌互刑",
    ("未", "戌"): "戌未互刑"
}

BRANCH_HAI = {
    ("子", "未"): "子未相害",
    ("丑", "午"): "丑午相害",
    ("寅", "巳"): "寅巳相害",
    ("卯", "辰"): "卯辰相害",
    ("申", "亥"): "申亥相害",
    ("酉", "戌"): "酉戌相害"
}

def check_branch_he(branch1: str, branch2: str) -> Tuple[bool, str]:
    """检查地支六合"""
    key = (branch1, branch2)
    reverse_key = (branch2, branch1)
    if key in BRANCH_HE:
        return True, BRANCH_HE[key]
    if reverse_key in BRANCH_HE:
        return True, BRANCH_HE[reverse_key]
    return False, ""

def check_branch_chong(branch1: str, branch2: str) -> Tuple[bool, str]:
    """检查地支六冲"""
    key = (branch1, branch2)
    reverse_key = (branch2, branch1)
    if key in BRANCH_CHONG:
        return True, BRANCH_CHONG[key]
    if reverse_key in BRANCH_CHONG:
        return True, BRANCH_CHONG[reverse_key]
    return False, ""

def check_branch_xing(branch1: str, branch2: str, branch3: str = None) -> Tuple[bool, str]:
    """检查地支三刑"""
    if branch3:
        combo = tuple(sorted([branch1, branch2, branch3]))
        if combo == ("寅", "巳", "申"):
            return True, "寅巳申三刑"
        if combo == ("丑", "未", "戌"):
            return True, "丑戌未三刑"
    else:
        key = (branch1, branch2)
        reverse_key = (branch2, branch1)
        if key in BRANCH_XING:
            return True, BRANCH_XING[key]
        if reverse_key in BRANCH_XING:
            return True, BRANCH_XING[reverse_key]
        if branch1 == branch2 and branch1 in ["辰", "午", "酉", "亥"]:
            return True, f"{branch1}自刑"
    return False, ""

def check_branch_hai(branch1: str, branch2: str) -> Tuple[bool, str]:
    """检查地支相害"""
    key = (branch1, branch2)
    reverse_key = (branch2, branch1)
    if key in BRANCH_HAI:
        return True, BRANCH_HAI[key]
    if reverse_key in BRANCH_HAI:
        return True, BRANCH_HAI[reverse_key]
    return False, ""

def analyze_pillar_relations(pillars: Dict[str, Dict[str, str]]) -> List[Dict]:
    """分析四柱之间的所有关系"""
    relations = []
    items = [
        ("年柱", pillars.get("year", {})),
        ("月柱", pillars.get("month", {})),
        ("日柱", pillars.get("day", {})),
        ("时柱", pillars.get("hour", {}))
    ]

    checked_pairs = set()
    for i, (name1, pillar1) in enumerate(items):
        for j, (name2, pillar2) in enumerate(items):
            if i >= j:
                continue

            pair_key = frozenset([name1, name2])
            if pair_key in checked_pairs:
                continue
            checked_pairs.add(pair_key)

            branch1 = pillar1.get("branch", "")
            branch2 = pillar2.get("branch", "")
            stem1 = pillar1.get("stem", "")
            stem2 = pillar2.get("stem", "")

            rels = []

            he_ok, he_desc = check_branch_he(branch1, branch2)
            if he_ok:
                rels.append({"type": "六合", "desc": he_desc})

            chong_ok, chong_desc = check_branch_chong(branch1, branch2)
            if chong_ok:
                rels.append({"type": "六冲", "desc": chong_desc})

            hai_ok, hai_desc = check_branch_hai(branch1, branch2)
            if hai_ok:
                rels.append({"type": "相害", "desc": hai_desc})

            for s1, s2 in [(stem1, stem2), (stem2, stem1)]:
                from .stems import stems_combination, stems_clash
                he = stems_combination(s1, s2)
                if he:
                    rels.append({"type": "天干五合", "desc": he})
                if stems_clash(s1, s2):
                    rels.append({"type": "天干相冲", "desc": f"{s1}庚{s2}冲"})

            if rels:
                relations.append({
                    "pillars": [name1, name2],
                    "details": rels
                })

    return relations
