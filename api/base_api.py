from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Абстрактный класс для работы с API вакансий"""

    @abstractmethod
    def get_vacancies(self, search_query: str):
        """Метод для получения вакансий по ключевому слову"""
        pass

