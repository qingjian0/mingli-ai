import logging
import logging.handlers
import sys
from pathlib import Path
from app.config import settings


def setup_logging():
    """配置日志系统"""
    log_level = getattr(logging, settings.log_level.upper(), logging.INFO)

    # 创建格式化器
    if settings.log_format == "json":
        formatter = logging.Formatter(
            '{"time":"%(asctime)s","level":"%(levelname)s","name":"%(name)s","message":"%(message)s"}',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    else:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    # 控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)

    # 文件处理器（可选）
    log_file = Path(settings.log_file)
    if log_file.parent.exists() or settings.log_file == "/dev/null":
        try:
            file_handler = logging.handlers.RotatingFileHandler(
                filename=settings.log_file if settings.log_file != "/dev/null" else "/tmp/mingli.log",
                maxBytes=settings.log_max_bytes,
                backupCount=settings.log_backup_count,
                encoding='utf-8'
            )
            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
        except (PermissionError, FileNotFoundError):
            logging.warning(f"无法创建日志文件: {settings.log_file}，仅使用控制台日志")
            file_handler = None
    else:
        file_handler = None

    # 配置根日志记录器
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.handlers.clear()
    root_logger.addHandler(console_handler)
    if file_handler:
        root_logger.addHandler(file_handler)

    # 配置第三方库日志级别
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING if not settings.debug else logging.INFO)

    return root_logger


logger = logging.getLogger("mingli")
