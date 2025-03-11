import json
from models.vacancy import Vacancy
from storage.base_storage import BaseStorage
from typing import List


class JSONStorage(BaseStorage):
    """Класс для хранения вакансий в JSON-файле"""

    def __init__(self, filename: str = "vacancies.json"):
        """Инициализирует хранилище JSON, задавая имя файла"""
        self.filename = filename

    def add_vacancy(self, vacancy: Vacancy):
        """Добавляет вакансию в JSON-файл"""
        vacancies = self.get_vacancies()  # Загружаем существующие вакансии
        vacancies.append(vacancy)  # Добавляем новую вакансию
        self._save_to_file(vacancies)  # Перезаписываем файл

    def get_vacancies(self, filter_str: str = None) -> List[Vacancy]:
        """Загружает вакансии из JSON-файла и фильтрует их по ключевому слову"""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                vacancies_data = json.load(f)  # Загружаем JSON
                vacancies = [
                    Vacancy(**v) for v in vacancies_data
                ]  # Конвертируем в объекты Vacancy
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies = []  # Если файла нет или он повреждён, возвращаем пустой список

        if filter_str:
            vacancies = [
                vac
                for vac in vacancies
                if filter_str.lower() in vac.title.lower()
                or filter_str.lower() in vac.description.lower()
            ]

        return vacancies

    def delete_vacancy(self, vacancy: Vacancy):
        """Удаляет вакансию из JSON-файла по URL"""
        vacancies = self.get_vacancies()  # Загружаем вакансии
        vacancies = [v for v in vacancies if v.url != vacancy.url]  # Удаляем нужную
        self._save_to_file(vacancies)  # Обновляем файл

    def _save_to_file(self, vacancies: List[Vacancy]):
        """Сохраняет список вакансий в JSON"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(
                [self._vacancy_to_dict(v) for v in vacancies],
                f,
                ensure_ascii=False,
                indent=4
            )

    def _vacancy_to_dict(self, vacancy: Vacancy) -> dict:
        """Преобразует объект Vacancy в словарь"""
        return {
            "title": vacancy.title,
            "url": vacancy.url,
            "salary": vacancy.salary,
            "description": vacancy.description
        }


