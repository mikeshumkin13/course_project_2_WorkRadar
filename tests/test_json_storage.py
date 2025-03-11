import pytest
import os
from models.vacancy import Vacancy
from storage.json_storage import JSONStorage


@pytest.fixture
def temp_storage():
    """Фикстура для временного JSON-хранилища"""
    filename = "test_vacancies.json"
    storage = JSONStorage(filename)
    yield storage  # Передаём объект хранилища в тесты
    if os.path.exists(filename):  # Удаляем тестовый файл после тестов
        os.remove(filename)


def test_add_vacancy(temp_storage):
    """Тестируем добавление вакансии в JSON"""
    vacancy = Vacancy("Python Dev", "https://hh.ru/123", 150000, "Опыт от 3 лет")
    temp_storage.add_vacancy(vacancy)

    vacancies = temp_storage.get_vacancies()
    assert len(vacancies) == 1
    assert vacancies[0].title == "Python Dev"
    assert vacancies[0].url == "https://hh.ru/123"
    assert vacancies[0].salary == 150000
    assert vacancies[0].description == "Опыт от 3 лет"


def test_get_vacancies_with_filter(temp_storage):
    """Тестируем фильтрацию вакансий по ключевому слову"""
    vacancy1 = Vacancy("Python Dev", "https://hh.ru/123", 150000, "Опыт от 3 лет")
    vacancy2 = Vacancy("Java Developer", "https://hh.ru/456", 120000, "Опыт от 2 лет")
    temp_storage.add_vacancy(vacancy1)
    temp_storage.add_vacancy(vacancy2)

    filtered_vacancies = temp_storage.get_vacancies("Python")
    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0].title == "Python Dev"


def test_delete_vacancy(temp_storage):
    """Тестируем удаление вакансии из JSON"""
    vacancy1 = Vacancy("Python Dev", "https://hh.ru/123", 150000, "Опыт от 3 лет")
    vacancy2 = Vacancy("Java Developer", "https://hh.ru/456", 120000, "Опыт от 2 лет")
    temp_storage.add_vacancy(vacancy1)
    temp_storage.add_vacancy(vacancy2)

    temp_storage.delete_vacancy(vacancy1)
    vacancies = temp_storage.get_vacancies()

    assert len(vacancies) == 1
    assert vacancies[0].title == "Java Developer"


def test_get_vacancies_empty_file(temp_storage):
    """Тестируем чтение вакансий из пустого JSON-файла"""
    vacancies = temp_storage.get_vacancies()
    assert len(vacancies) == 0


