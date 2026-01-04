import pytest
from loguru import logger
import sys


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Настройка логирования для всех тестов"""
    # Удаляем стандартный обработчик
    logger.remove()

    # Добавляем обработчик для вывода в консоль
    logger.add(
        sys.stdout,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="DEBUG",
        colorize=True
    )

    # Добавляем обработчик для записи в файл
    logger.add(
        "test_results.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level="INFO",
        rotation="50 MB",
        retention="10 days"
    )

    yield
    logger.info("Все тесты завершены")