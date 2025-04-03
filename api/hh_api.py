import requests
from api.base_api import BaseAPI
from utils.logger import logger


class HeadHunterAPI(BaseAPI):
    """Класс для работы с API hh.ru"""

    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        """Инициализация приватных атрибутов"""
        self._session = requests.Session()  # Приватный атрибут
        self._headers = {"User-Agent": "WorkRadar"}  # Приватный атрибут

    def _connect(self, url: str, params: dict):
        """Подключение к API hh.ru с обработкой ошибок"""
        try:
            response = self._session.get(url, params=params, headers=self._headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при запросе к API: {e}")
            return None  # Важно: API вернет None при ошибке

    def get_vacancies(self, search_query: str, area: int = None, salary: int = None, employment: str = None):
        """Получает вакансии по ключевому слову и дополнительным параметрам"""
        params = {"text": search_query, "per_page": 20}
        if area:
            params["area"] = area
        if salary:
            params["salary"] = salary
        if employment:
            params["employment"] = employment

        data = self._connect(self.BASE_URL, params)
        if not data:  # Если `None`, вернуть пустой список
            logger.warning(f"Ошибка при запросе, возвращаем пустой список. Запрос: {params}")
            return []

        vacancies = data.get("items", [])
        logger.info(f"Запрос: {params} | Найдено вакансий: {len(vacancies)}")
        return vacancies

