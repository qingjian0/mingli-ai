"""
纯净知识库API路由
确保知识源自古籍原典，经过严格筛选和验证
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
import uuid

router = APIRouter(prefix="/api/v1/knowledge", tags=["知识库"])

# ==================== 请求/响应模型 ====================

class SourceReference(BaseModel):
    """来源参考"""
    book: str
    author: Optional[str] = None
    dynasty: Optional[str] = None
    chapter: Optional[str] = None
    page: Optional[int] = None

class KnowledgeEntryResponse(BaseModel):
    """知识条目响应"""
    id: str
    term: str
    pinyin: Optional[str] = None
    category: str
    system: str
    source: SourceReference
    original_content: str
    interpretation: str
    verification_status: str
    source_traceable: bool
    quality_grade: str
    related_entries: List[str] = []
    tags: List[str] = []
    view_count: int = 0
    reference_count: int = 0
    created_at: str
    updated_at: str

class KnowledgeSearchRequest(BaseModel):
    """知识搜索请求"""
    query: Optional[str] = None
    system: Optional[str] = None
    category: Optional[str] = None
    verification_status: Optional[str] = None
    source_book: Optional[str] = None
    page: int = 1
    page_size: int = 20

class KnowledgeSearchResponse(BaseModel):
    """知识搜索响应"""
    items: List[KnowledgeEntryResponse]
    total: int
    page: int
    page_size: int
    quality_distribution: dict

class SourceValidationRequest(BaseModel):
    """来源验证请求"""
    book: str
    author: Optional[str] = None
    dynasty: Optional[str] = None
    chapter: Optional[str] = None
    page: Optional[int] = None

class SourceValidationResponse(BaseModel):
    """来源验证响应"""
    is_valid: bool
    credibility_grade: str
    confidence: float
    issues: List[str] = []
    suggestions: List[str] = []
    matched_book_info: Optional[dict] = None

class QualityReportResponse(BaseModel):
    """质量报告响应"""
    total_entries: int
    verified_entries: int
    pending_entries: int
    disputed_entries: int
    average_quality_score: float
    source_coverage: float
    verification_coverage: float
    common_issues: List[dict]
    recommendations: List[str]

class AncientBookResponse(BaseModel):
    """古籍响应"""
    id: str
    title: str
    author: Optional[str]
    dynasty: str
    category: str
    version: Optional[str]
    source: str
    chapters_summary: List[dict]
    entry_count: int
    creation_date: str

# ==================== 模拟数据存储 ====================

# 已知权威古籍
KNOWN_BOOKS = {
    "紫微斗数全书": {
        "author": "陈公献",
        "dynasty": "明",
        "category": "ziwei",
        "reliability": "A"
    },
    "渊海子平": {
        "author": "徐子平",
        "dynasty": "宋",
        "category": "bazi",
        "reliability": "A"
    },
    "滴天髓": {
        "author": "任铁樵",
        "dynasty": "清",
        "category": "bazi",
        "reliability": "A"
    },
    "穷通宝鉴": {
        "author": "余春台",
        "dynasty": "清",
        "category": "bazi",
        "reliability": "A"
    },
    "子平真诠": {
        "author": "沈孝瞻",
        "dynasty": "清",
        "category": "bazi",
        "reliability": "A"
    },
    "奇门遁甲全书": {
        "author": None,
        "dynasty": "明",
        "category": "qimen",
        "reliability": "A"
    },
    "易经": {
        "author": "孔子",
        "dynasty": "春秋",
        "category": "yijing",
        "reliability": "A"
    }
}

# 知识条目示例
SAMPLE_KNOWLEDGE = [
    {
        "id": "know_001",
        "term": "紫微星",
        "pinyin": "zǐwēixīng",
        "category": "main_star",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "author": "陈公献",
            "dynasty": "明",
            "chapter": "卷一·星曜总论",
            "page": 15
        },
        "original_content": "紫微帝星，居中垣之首，司权衡，主造化之机。",
        "interpretation": "紫微星为紫微斗数诸星之首，象征最高权力和领导力。",
        "verification_status": "verified",
        "source_traceable": True,
        "quality_grade": "A",
        "related_entries": ["天机星", "太阳星", "武曲星"],
        "tags": ["帝王星", "权力", "领导"],
        "view_count": 1250,
        "reference_count": 89
    },
    {
        "id": "know_002",
        "term": "比肩",
        "pinyin": "bǐjiān",
        "category": "ten_god",
        "system": "bazi",
        "source": {
            "book": "渊海子平",
            "author": "徐子平",
            "dynasty": "宋",
            "chapter": "论十神",
            "page": 45
        },
        "original_content": "比肩者，兄弟也。见同类而为比肩。",
        "interpretation": "比肩代表兄弟姐妹、同事、朋友，象征竞争和合作。",
        "verification_status": "verified",
        "source_traceable": True,
        "quality_grade": "A",
        "related_entries": ["劫财", "正官", "七杀"],
        "tags": ["兄弟", "竞争", "合作"],
        "view_count": 980,
        "reference_count": 67
    },
    {
        "id": "know_003",
        "term": "命宫",
        "pinyin": "mìnggōng",
        "category": "palace",
        "system": "ziwei",
        "source": {
            "book": "紫微斗数全书",
            "author": "陈公献",
            "dynasty": "明",
            "chapter": "卷二·宫位总论",
            "page": 28
        },
        "original_content": "命宫为立命之宫，主一生之祸福吉凶。",
        "interpretation": "命宫是紫微斗数中最重要的宫位，代表个人的基本性格和命运走向。",
        "verification_status": "verified",
        "source_traceable": True,
        "quality_grade": "A",
        "related_entries": ["身宫", "迁移宫", "事业宫"],
        "tags": ["性格", "命运", "一生"],
        "view_count": 2340,
        "reference_count": 156
    },
    {
        "id": "know_004",
        "term": "用神",
        "pinyin": "yòngshén",
        "category": "principle",
        "system": "bazi",
        "source": {
            "book": "穷通宝鉴",
            "author": "余春台",
            "dynasty": "清",
            "chapter": "论用神",
            "page": 12
        },
        "original_content": "用神者，八字之枢纽也。能助日元之弱，抑日元之强。",
        "interpretation": "用神是平衡八字五行最需要的字，是八字分析的核心。",
        "verification_status": "verified",
        "source_traceable": True,
        "quality_grade": "A",
        "related_entries": ["日主", "月令", "喜神"],
        "tags": ["用神", "平衡", "核心"],
        "view_count": 3450,
        "reference_count": 234
    },
    {
        "id": "know_005",
        "term": "乾卦",
        "pinyin": "qiánguà",
        "category": "hexagram",
        "system": "yijing",
        "source": {
            "book": "易经",
            "author": "孔子",
            "dynasty": "春秋",
            "chapter": "乾卦第一",
            "page": 1
        },
        "original_content": "乾：元，亨，利，贞。初九：潜龙，勿用。",
        "interpretation": "乾卦象征天，代表刚健有力。卦辞元亨利贞表示大亨通有利。",
        "verification_status": "verified",
        "source_traceable": True,
        "quality_grade": "A",
        "related_entries": ["坤卦", "震卦", "离卦"],
        "tags": ["乾", "天", "刚健"],
        "view_count": 4500,
        "reference_count": 312
    }
]

# ==================== API端点 ====================

@router.get("/", response_model=KnowledgeSearchResponse)
async def search_knowledge(
    query: Optional[str] = Query(None, description="搜索关键词"),
    system: Optional[str] = Query(None, description="所属体系: ziwei/bazi/qimen/yijing"),
    category: Optional[str] = Query(None, description="分类: star/palace/ten_god/hexagram等"),
    verification_status: Optional[str] = Query(None, description="验证状态: verified/pending"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100)
):
    """搜索知识库"""
    # 过滤知识
    filtered = SAMPLE_KNOWLEDGE.copy()
    
    if query:
        filtered = [
            k for k in filtered
            if query.lower() in k["term"].lower() 
            or query.lower() in k["interpretation"].lower()
        ]
    
    if system:
        filtered = [k for k in filtered if k["system"] == system]
    
    if category:
        filtered = [k for k in filtered if k["category"] == category]
    
    if verification_status:
        filtered = [k for k in filtered if k["verification_status"] == verification_status]
    
    # 分页
    total = len(filtered)
    start = (page - 1) * page_size
    end = start + page_size
    items = filtered[start:end]
    
    # 质量分布统计
    quality_dist = {}
    for k in filtered:
        grade = k["quality_grade"]
        quality_dist[grade] = quality_dist.get(grade, 0) + 1
    
    return KnowledgeSearchResponse(
        items=[KnowledgeEntryResponse(**k) for k in items],
        total=total,
        page=page,
        page_size=page_size,
        quality_distribution=quality_dist
    )

@router.get("/{knowledge_id}", response_model=KnowledgeEntryResponse)
async def get_knowledge(knowledge_id: str):
    """获取知识条目详情"""
    for k in SAMPLE_KNOWLEDGE:
        if k["id"] == knowledge_id:
            return KnowledgeEntryResponse(**k)
    raise HTTPException(status_code=404, detail="知识条目不存在")

@router.post("/validate-source", response_model=SourceValidationResponse)
async def validate_source(request: SourceValidationRequest):
    """验证来源可信度"""
    book = request.book
    issues = []
    suggestions = []
    confidence = 1.0
    
    # 检查是否是已知古籍
    if book in KNOWN_BOOKS:
        book_info = KNOWN_BOOKS[book]
        
        # 验证作者
        if request.author and book_info.get("author"):
            if request.author != book_info["author"]:
                issues.append(f"作者 '{request.author}' 与典籍记录不符")
                confidence -= 0.2
        
        # 验证朝代
        if request.dynasty and book_info.get("dynasty"):
            if request.dynasty != book_info["dynasty"]:
                issues.append(f"朝代 '{request.dynasty}' 可能不正确")
                confidence -= 0.1
        
        return SourceValidationResponse(
            is_valid=len(issues) == 0,
            credibility_grade=book_info["reliability"],
            confidence=max(0, confidence),
            issues=issues,
            suggestions=suggestions,
            matched_book_info=book_info
        )
    else:
        issues.append(f"典籍 '{book}' 未在已知权威列表中")
        confidence -= 0.3
        suggestions.append("建议使用权威原典，如《紫微斗数全书》《渊海子平等")
        
        return SourceValidationResponse(
            is_valid=False,
            credibility_grade="C",
            confidence=max(0, confidence),
            issues=issues,
            suggestions=suggestions,
            matched_book_info=None
        )

@router.get("/books/list", response_model=List[AncientBookResponse])
async def list_ancient_books(
    system: Optional[str] = Query(None, description="按体系筛选")
):
    """获取古籍列表"""
    books = []
    for title, info in KNOWN_BOOKS.items():
        if system and info["category"] != system:
            continue
        
        books.append(AncientBookResponse(
            id=f"book_{hash(title) % 10000}",
            title=title,
            author=info.get("author"),
            dynasty=info["dynasty"],
            category=info["category"],
            version="标准版",
            source=info["reliability"],
            chapters_summary=[
                {"name": "卷一", "entry_count": 50},
                {"name": "卷二", "entry_count": 45}
            ],
            entry_count=len([k for k in SAMPLE_KNOWLEDGE if k["source"]["book"] == title]),
            creation_date="2026-01-01"
        ))
    
    return books

@router.get("/quality/report", response_model=QualityReportResponse)
async def get_quality_report():
    """获取知识库质量报告"""
    total = len(SAMPLE_KNOWLEDGE)
    verified = sum(1 for k in SAMPLE_KNOWLEDGE if k["verification_status"] == "verified")
    pending = sum(1 for k in SAMPLE_KNOWLEDGE if k["verification_status"] == "pending")
    disputed = sum(1 for k in SAMPLE_KNOWLEDGE if k["verification_status"] == "disputed")
    
    # 质量分数
    grade_scores = {"A": 95, "B": 80, "C": 65, "D": 50}
    avg_score = sum(
        grade_scores.get(k["quality_grade"], 0) for k in SAMPLE_KNOWLEDGE
    ) / total if total > 0 else 0
    
    # 来源覆盖率
    traceable = sum(1 for k in SAMPLE_KNOWLEDGE if k["source_traceable"])
    source_coverage = (traceable / total * 100) if total > 0 else 0
    
    return QualityReportResponse(
        total_entries=total,
        verified_entries=verified,
        pending_entries=pending,
        disputed_entries=disputed,
        average_quality_score=round(avg_score, 2),
        source_coverage=round(source_coverage, 2),
        verification_coverage=round((verified / total * 100) if total > 0 else 0, 2),
        common_issues=[
            {"issue": "部分知识缺少页码信息", "count": 5},
            {"issue": "某些术语有多个解释", "count": 3}
        ],
        recommendations=[
            "补充所有知识条目的完整来源信息",
            "建立专家审核机制验证存疑内容",
            "定期更新古籍原文引用"
        ]
    )

@router.get("/systems/overview")
async def get_systems_overview():
    """获取各体系知识概览"""
    systems = {}
    
    for k in SAMPLE_KNOWLEDGE:
        system = k["system"]
        if system not in systems:
            systems[system] = {
                "system": system,
                "total_entries": 0,
                "verified_entries": 0,
                "categories": {},
                "top_sources": []
            }
        
        systems[system]["total_entries"] += 1
        if k["verification_status"] == "verified":
            systems[system]["verified_entries"] += 1
        
        cat = k["category"]
        systems[system]["categories"][cat] = systems[system]["categories"].get(cat, 0) + 1
        
        source = k["source"]["book"]
        if source not in systems[system]["top_sources"]:
            systems[system]["top_sources"].append(source)
    
    return {"systems": list(systems.values())}

@router.get("/terms/{term}/details")
async def get_term_details(term: str):
    """获取术语详细信息"""
    for k in SAMPLE_KNOWLEDGE:
        if k["term"] == term or term.lower() in k["term"].lower():
            return {
                "term": k["term"],
                "pinyin": k["pinyin"],
                "system": k["system"],
                "category": k["category"],
                "source": k["source"],
                "original_content": k["original_content"],
                "interpretation": k["interpretation"],
                "related_terms": k["related_entries"],
                "verification": {
                    "status": k["verification_status"],
                    "grade": k["quality_grade"],
                    "source_traceable": k["source_traceable"]
                },
                "usage_stats": {
                    "views": k["view_count"],
                    "references": k["reference_count"]
                }
            }
    
    raise HTTPException(status_code=404, detail="术语不存在")
