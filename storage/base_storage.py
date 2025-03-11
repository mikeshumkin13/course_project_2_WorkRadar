from abc import ABC, abstractmethod
from models.vacancy import Vacancy
from typing import List


class BaseStorage(ABC):
    """Абстрактный класс для хранения вакансий"""

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy):
        """Добавить вакансию в хранилище"""
        pass

    @abstractmethod
    def get_vacancies(self, filter_str: str = None) -> List[Vacancy]:
        """Получить список вакансий (с фильтром по ключевому слову)"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy):
        """Удалить вакансию из хранилища"""
        pass
