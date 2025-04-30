import pytest
from models.vacancy import Vacancy


def test_create_vacancy():
    """Проверяем создание вакансии с корректными данными"""
    vacancy = Vacancy("Python Dev", "https://hh.ru/123", 150000, "Опыт от 3 лет")

    assert vacancy.title == "Python Dev"
    assert vacancy.url == "https://hh.ru/123"
    assert vacancy.salary == 150000
    assert vacancy.description == "Опыт от 3 лет"


def test_create_vacancy_default_description():
    """Проверяем создание вакансии без описания (должно быть 'Описание отсутствует')"""
    vacancy = Vacancy("Python Dev", "https://hh.ru/123", 150000, "")

    assert vacancy.description == "Описание отсутствует"


def test_create_vacancy_invalid_title():
    """Проверяем валидацию: пустое название вакансии"""
    with pytest.raises(ValueError, match="Название вакансии должно быть строкой и не пустым"):
        Vacancy("", "https://hh.ru/123", 150000, "Опыт от 3 лет")



def test_create_vacancy_invalid_url():
    """Проверяем валидацию: некорректный URL"""
    with pytest.raises(ValueError, match="URL вакансии должен начинаться с http"):
        Vacancy("Python Dev", "hh.ru/123", 150000, "Опыт от 3 лет")



def test_create_vacancy_negative_salary():
    """Проверяем валидацию: отрицательная зарплата"""
    with pytest.raises(ValueError, match="Зарплата должна быть положительным числом"):
        Vacancy("Python Dev", "https://hh.ru/123", -50000, "Опыт от 3 лет")



def test_vacancy_comparison():
    """Проверяем сравнение вакансий по зарплате"""
    v1 = Vacancy("Senior Dev", "https://hh.ru/001", 200000, "Senior")
    v2 = Vacancy("Middle Dev", "https://hh.ru/002", 150000, "Middle")
    v3 = Vacancy("Junior Dev", "https://hh.ru/003", 80000, "Junior")

    assert v1 > v2  # 200000 > 150000
    assert v2 > v3  # 150000 > 80000
    assert v1 != v3  # 200000 != 80000


def test_vacancy_equality():
    """Проверяем равенство вакансий по зарплате"""
    v1 = Vacancy("Dev A", "https://hh.ru/111", 120000, "Desc A")
    v2 = Vacancy("Dev B", "https://hh.ru/222", 120000, "Desc B")

    assert v1 == v2  # 120000 == 120000
