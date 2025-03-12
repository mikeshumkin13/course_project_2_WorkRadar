import pytest
from models.vacancy import Vacancy
from utils.filters import filter_by_salary, filter_by_keyword


@pytest.fixture
def sample_vacancies():
    """Создаём тестовые вакансии"""
    return [
        Vacancy("Python Dev", "https://hh.ru/123", 150000, "Опыт от 3 лет"),
        Vacancy("Java Developer", "https://hh.ru/456", 120000, "Опыт от 2 лет"),
        Vacancy("Data Scientist", "https://hh.ru/789", 200000, "Анализ данных"),
        Vacancy("Junior Python", "https://hh.ru/101", 80000, "Python для начинающих")
    ]


def test_filter_by_salary(sample_vacancies):
    """Тестируем фильтрацию по зарплате"""
    filtered = filter_by_salary(sample_vacancies, 130000)
    assert len(filtered) == 2  # Должны остаться только те, у кого salary >= 130000
    assert all(vac.salary >= 130000 for vac in filtered)


def test_filter_by_keyword(sample_vacancies):
    """Тестируем фильтрацию по ключевому слову"""
    filtered = filter_by_keyword(sample_vacancies, "Python")
    assert len(filtered) == 2  # Должны остаться вакансии с "Python" в title или description
    assert all("Python" in vac.title or "Python" in vac.description for vac in filtered)

from utils.sorters import sort_by_salary, sort_by_title


def test_sort_by_salary(sample_vacancies):
    """Тестируем сортировку по зарплате"""
    sorted_vacancies = sort_by_salary(sample_vacancies)
    salaries = [vac.salary for vac in sorted_vacancies]
    assert salaries == sorted(salaries, reverse=True)  # Проверяем, что зарплаты отсортированы по убыванию


def test_sort_by_title(sample_vacancies):
    """Тестируем сортировку по названию вакансии"""
    sorted_vacancies = sort_by_title(sample_vacancies)
    titles = [vac.title for vac in sorted_vacancies]
    assert titles == sorted(titles, key=str.lower)  # Проверяем, что отсортировано по алфавиту

