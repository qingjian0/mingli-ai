from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
        extra='ignore'
    )

    app_name: str = "明理AI命理平台"
    app_version: str = "1.0.0"
    app_description: str = "专业的AI命理分析平台"

    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    workers: int = 1

    database_url: str = "sqlite+aiosqlite:///./mingli.db"
    database_url_sync: str = "sqlite:///./mingli.db"
    database_pool_size: int = 5
    database_max_overflow: int = 10
    database_pool_timeout: int = 30
    database_pool_recycle: int = 3600

    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_password: str = ""
    redis_decode_responses: bool = True
    redis_max_connections: int = 10

    secret_key: str = "your-secret-key-here-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    allowed_origins: str = "http://localhost:3000,http://localhost:8080"
    allowed_methods: str = "GET,POST,PUT,DELETE,PATCH"
    allowed_headers: str = "*"

    log_level: str = "INFO"
    log_format: str = "json"
    log_file: str = "/var/log/mingli/app.log"
    log_max_bytes: int = 10485760
    log_backup_count: int = 5

    ai_api_key: str = ""
    ai_api_base_url: str = "https://api.openai.com/v1"
    ai_model: str = "gpt-4"

    cache_enabled: bool = True
    cache_ttl: int = 3600

    @property
    def allowed_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.allowed_origins.split(',')]

    @property
    def allowed_methods_list(self) -> List[str]:
        return [method.strip() for method in self.allowed_methods.split(',')]

    @property
    def allowed_headers_list(self) -> List[str]:
        return [header.strip() for header in self.allowed_headers.split(',')]


settings = Settings()
