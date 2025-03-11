import logging
import requests
from api.base_api import BaseAPI

# Настройка логирования
logging.basicConfig(
    filename="logs/api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class HeadHunterAPI(BaseAPI):
    """Класс для работы с API hh.ru"""

    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(
        self,
        search_query: str,
        area: int = None,
        salary: int = None,
        employment: str = None,
    ):
        """Получает вакансии по ключевому слову и дополнительным параметрам"""
        params = {"text": search_query, "per_page": 20}
        if area:
            params["area"] = area
        if salary:
            params["salary"] = salary
        if employment:
            params["employment"] = employment

        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            vacancies = response.json().get("items", [])

            # Логируем успешный запрос
            logging.info(f"Запрос: {params} | Найдено вакансий: {len(vacancies)}")

            return vacancies

        except requests.exceptions.RequestException as e:
            logging.error(f"Ошибка запроса: {e}")
            return []
