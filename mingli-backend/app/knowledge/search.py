from typing import List, Optional, Tuple, Dict, Any
import hashlib
import json
from datetime import datetime, timedelta
import numpy as np
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from app.models.knowledge import KnowledgeEntry, ClassicText, ClassicSection
from app.schemas.knowledge import (
    KnowledgeSearchRequest, KnowledgeSearchResult, KnowledgeSearchResponse,
    KnowledgeCategoryEnum, KnowledgeTypeEnum
)
from app.config import settings


class SemanticSearch:
    """语义搜索服务"""

    def __init__(self, db: AsyncSession):
        self.db = db
        self.cache: Dict[str, Tuple[List[KnowledgeSearchResult], datetime]] = {}
        self.cache_ttl = timedelta(hours=1)

    def _get_cache_key(self, request: KnowledgeSearchRequest) -> str:
        """生成缓存键"""
        cache_data = {
            "query": request.query,
            "category": request.category.value if request.category else None,
            "knowledge_type": request.knowledge_type.value if request.knowledge_type else None,
            "tags": sorted(request.tags) if request.tags else None,
            "verification_level": request.verification_level,
            "limit": request.limit,
            "offset": request.offset
        }
        cache_str = json.dumps(cache_data, sort_keys=True)
        return hashlib.md5(cache_str.encode()).hexdigest()

    def _get_from_cache(self, cache_key: str) -> Optional[List[KnowledgeSearchResult]]:
        """从缓存获取"""
        if cache_key in self.cache:
            results, timestamp = self.cache[cache_key]
            if datetime.now() - timestamp < self.cache_ttl:
                return results
            else:
                del self.cache[cache_key]
        return None

    def _set_cache(self, cache_key: str, results: List[KnowledgeSearchResult]) -> None:
        """设置缓存"""
        if len(self.cache) > 1000:
            oldest_key = min(self.cache.keys(), key=lambda k: self.cache[k][1])
            del self.cache[oldest_key]
        self.cache[cache_key] = (results, datetime.now())

    def _tokenize(self, text: str) -> List[str]:
        """简单分词"""
        stop_words = {'的', '了', '和', '是', '在', '有', '与', '及', '等', '为', '以', '于'}
        chars = list(text.lower())
        tokens = []
        current_token = ""

        for char in chars:
            if '\u4e00' <= char <= '\u9fff':
                if current_token:
                    if current_token not in stop_words:
                        tokens.append(current_token)
                    current_token = ""
                tokens.append(char)
            elif char.isalnum():
                current_token += char
            else:
                if current_token:
                    if current_token not in stop_words:
                        tokens.append(current_token)
                    current_token = ""

        if current_token and current_token not in stop_words:
            tokens.append(current_token)

        return tokens

    def _calculate_similarity(self, query_tokens: List[str], text_tokens: List[str]) -> float:
        """计算文本相似度"""
        if not query_tokens or not text_tokens:
            return 0.0

        query_set = set(query_tokens)
        text_set = set(text_tokens)

        intersection = query_set & text_set
        union = query_set | text_set

        if not union:
            return 0.0

        jaccard = len(intersection) / len(union)

        query_tf = sum(1 for t in query_tokens if t in text_tokens) / len(query_tokens)

        position_score = 0.0
        if text_tokens:
            first_match_idx = next((i for i, t in enumerate(text_tokens) if t in query_set), len(text_tokens))
            position_score = 1.0 - (first_match_idx / len(text_tokens))

        return (jaccard * 0.4 + query_tf * 0.3 + position_score * 0.3)

    def _generate_highlights(self, content: str, query_tokens: List[str], max_length: int = 200) -> List[str]:
        """生成高亮片段"""
        highlights = []
        content_lower = content.lower()
        query_lower_set = {t.lower() for t in query_tokens}

        for token in query_lower_set:
            idx = content_lower.find(token)
            if idx != -1:
                start = max(0, idx - 50)
                end = min(len(content), idx + len(token) + 50)
                highlight = content[start:end]
                if start > 0:
                    highlight = "..." + highlight
                if end < len(content):
                    highlight = highlight + "..."
                highlights.append(highlight)
                if len(highlights) >= 3:
                    break

        return highlights[:3]

    async def search(
        self,
        request: KnowledgeSearchRequest
    ) -> KnowledgeSearchResponse:
        """执行语义搜索"""
        cache_key = self._get_cache_key(request)
        cached_results = self._get_from_cache(cache_key)

        if cached_results is not None:
            return KnowledgeSearchResponse(
                results=cached_results[request.offset:request.offset + request.limit],
                total=len(cached_results),
                query=request.query
            )

        query_tokens = self._tokenize(request.query)

        conditions = [KnowledgeEntry.is_published == True]

        if request.category:
            conditions.append(KnowledgeEntry.category == request.category.value)
        if request.knowledge_type:
            conditions.append(KnowledgeEntry.knowledge_type == request.knowledge_type.value)
        if request.verification_level:
            conditions.append(KnowledgeEntry.verification_level == request.verification_level.value)
        if request.tags:
            for tag in request.tags:
                conditions.append(KnowledgeEntry.tags.contains([tag]))

        result = await self.db.execute(
            select(KnowledgeEntry).where(and_(*conditions))
        )
        all_entries = result.scalars().all()

        scored_entries = []
        for entry in all_entries:
            search_text = f"{entry.title} {entry.content} {' '.join(entry.tags or [])}"
            text_tokens = self._tokenize(search_text)
            score = self._calculate_similarity(query_tokens, text_tokens)

            if score > 0.1:
                highlights = self._generate_highlights(entry.content, query_tokens)

                scored_entries.append((
                    KnowledgeSearchResult(
                        entry=entry,
                        score=round(score, 4),
                        highlights=highlights
                    ),
                    score
                ))

        scored_entries.sort(key=lambda x: x[1], reverse=True)

        all_results = [item[0] for item in scored_entries]
        self._set_cache(cache_key, all_results)

        total = len(all_results)
        paginated_results = all_results[request.offset:request.offset + request.limit]

        return KnowledgeSearchResponse(
            results=paginated_results,
            total=total,
            query=request.query
        )

    async def search_classics(
        self,
        query: str,
        category: Optional[str] = None,
        limit: int = 20
    ) -> List[Tuple[ClassicText, float]]:
        """搜索古籍"""
        query_tokens = self._tokenize(query)

        conditions = []
        if category:
            conditions.append(ClassicText.category == category)

        result = await self.db.execute(
            select(ClassicText).where(and_(*conditions)) if conditions else select(ClassicText)
        )
        texts = result.scalars().all()

        scored_texts = []
        for text in texts:
            search_text = f"{text.title} {text.author or ''} {text.description or ''}"
            text_tokens = self._tokenize(search_text)
            score = self._calculate_similarity(query_tokens, text_tokens)

            if score > 0.1:
                scored_texts.append((text, round(score, 4)))

        scored_texts.sort(key=lambda x: x[1], reverse=True)
        return scored_texts[:limit]

    async def search_sections(
        self,
        query: str,
        text_id: Optional[int] = None,
        limit: int = 20
    ) -> List[Tuple[ClassicSection, float]]:
        """搜索古籍章节"""
        query_tokens = self._tokenize(query)

        conditions = []
        if text_id:
            conditions.append(ClassicSection.text_id == text_id)

        result = await self.db.execute(
            select(ClassicSection).where(and_(*conditions)) if conditions else select(ClassicSection)
        )
        sections = result.scalars().all()

        scored_sections = []
        for section in sections:
            search_text = f"{section.chapter} {section.section or ''} {section.content}"
            text_tokens = self._tokenize(search_text)
            score = self._calculate_similarity(query_tokens, text_tokens)

            if score > 0.05:
                scored_sections.append((section, round(score, 4)))

        scored_sections.sort(key=lambda x: x[1], reverse=True)
        return scored_sections[:limit]


class EmbeddingService:
    """向量嵌入服务（预留接口）"""

    def __init__(self):
        self.model = None
        self.dimension = 1536

    async def generate_embedding(self, text: str) -> List[float]:
        """生成文本向量"""
        return [0.0] * self.dimension

    async def generate_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """批量生成文本向量"""
        return [[0.0] * self.dimension for _ in texts]

    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """计算余弦相似度"""
        if not vec1 or not vec2:
            return 0.0

        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = sum(a * a for a in vec1) ** 0.5
        norm2 = sum(b * b for b in vec2) ** 0.5

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return dot_product / (norm1 * norm2)
