import logging
import os

# Создаём папку для логов, если её нет
os.makedirs("logs", exist_ok=True)

# Настройка логирования
logging.basicConfig(
    filename="logs/api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)  # Экспортируем логгер


