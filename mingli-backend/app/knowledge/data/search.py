"""
知识数据检索工具
提供便捷的数据查询接口
"""

from typing import List, Dict, Optional, Any
from .ziwei import (
    ZIWEI_STARS, ZIWEI_PALACES, ZIWEI_TRANSFORMS,
    ZIWEI_PATTERNS, ZIWEI_QUANSHU_EXCERPTS
)
from .bazi import (
    BAZI_TEN_GODS, BAZI_YUANHAI_EXCERPTS,
    BAZI_DITIAN_EXCERPTS, BAZI_QIONGTONG_EXCERPTS, BAZI_DAYUN_RULES
)
from .qimen import (
    QIMEN_DOORS, QIMEN_STARS, QIMEN_SPIRITS, QIMEN_QUANSHU_EXCERPTS
)
from .yijing import HEXAGRAM_MEANINGS, YAO_MEANINGS


class KnowledgeSearcher:
    def __init__(self):
        self.stars = ZIWEI_STARS
        self.palaces = ZIWEI_PALACES
        self.transforms = ZIWEI_TRANSFORMS
        self.patterns = ZIWEI_PATTERNS
        self.ten_gods = BAZI_TEN_GODS
        self.qimen_doors = QIMEN_DOORS
        self.qimen_stars = QIMEN_STARS
        self.qimen_spirits = QIMEN_SPIRITS
        self.hexagrams = HEXAGRAM_MEANINGS
        self.yaos = YAO_MEANINGS

    def search_stars(self, keyword: str) -> List[Dict[str, Any]]:
        results = []
        for star in self.stars:
            if keyword in star.get('term', '') or \
               keyword in star.get('pinyin', '') or \
               keyword in ' '.join(star.get('keywords', [])):
                results.append(star)
        return results

    def search_palaces(self, keyword: str) -> List[Dict[str, Any]]:
        results = []
        for palace in self.palaces:
            if keyword in palace.get('term', '') or \
               keyword in palace.get('pinyin', '') or \
               keyword in ' '.join(palace.get('keywords', [])):
                results.append(palace)
        return results

    def search_ten_gods(self, keyword: str) -> List[Dict[str, Any]]:
        results = []
        for god in self.ten_gods:
            if keyword in god.get('term', '') or \
               keyword in god.get('pinyin', '') or \
               keyword in ' '.join(god.get('keywords', [])):
                results.append(god)
        return results

    def search_qimen_doors(self, keyword: str) -> List[Dict[str, Any]]:
        results = []
        for door in self.qimen_doors:
            if keyword in door.get('term', '') or \
               keyword in door.get('pinyin', '') or \
               keyword in ' '.join(door.get('keywords', [])):
                results.append(door)
        return results

    def search_hexagrams(self, keyword: str) -> List[Dict[str, Any]]:
        results = []
        for hex in self.hexagrams:
            if keyword in hex.get('name', '') or \
               keyword in ' '.join(hex.get('keywords', [])):
                results.append(hex)
        return results

    def get_star_by_id(self, star_id: str) -> Optional[Dict[str, Any]]:
        for star in self.stars:
            if star.get('id') == star_id:
                return star
        return None

    def get_palace_by_id(self, palace_id: str) -> Optional[Dict[str, Any]]:
        for palace in self.palaces:
            if palace.get('id') == palace_id:
                return palace
        return None

    def get_hexagram_by_id(self, hex_id: str) -> Optional[Dict[str, Any]]:
        for hex in self.hexagrams:
            if hex.get('id') == hex_id:
                return hex
        return None


searcher = KnowledgeSearcher()

__all__ = [
    'KnowledgeSearcher',
    'searcher',
    'ZIWEI_STARS', 'ZIWEI_PALACES', 'ZIWEI_TRANSFORMS', 'ZIWEI_PATTERNS',
    'BAZI_TEN_GODS', 'BAZI_DAYUN_RULES',
    'QIMEN_DOORS', 'QIMEN_STARS', 'QIMEN_SPIRITS',
    'HEXAGRAM_MEANINGS', 'YAO_MEANINGS'
]
