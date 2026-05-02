"""
测试环境和依赖配置
"""

import os
from datetime import datetime

os.environ.setdefault("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/mingli_test")
os.environ.setdefault("REDIS_URL", "redis://localhost:6379")
os.environ.setdefault("SECRET_KEY", "test-secret-key-for-testing-only")
os.environ.setdefault("ENVIRONMENT", "test")


TEST_BIRTH_INFO = {
    "birth_time": datetime(1990, 5, 15, 14, 30),
    "location": {
        "longitude": 116.4,
        "latitude": 39.9,
        "timezone": 8.0
    },
    "gender": "male"
}


VERIFICATION_DATA = {
    "known_jiazi_day": {
        "date": datetime(2024, 2, 9, 12, 0),
        "expected_stem": "甲",
        "expected_branch": "子"
    },
    "known_year_1984": {
        "year": 1984,
        "expected_stem": "甲",
        "expected_branch": "子"
    }
}
