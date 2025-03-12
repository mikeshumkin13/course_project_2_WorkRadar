from typing import List
from models.vacancy import Vacancy


def sort_by_salary(vacancies: List[Vacancy], reverse: bool = True) -> List[Vacancy]:
    """Сортирует вакансии по зарплате (по умолчанию от большего к меньшему)"""
    return sorted(vacancies, key=lambda vac: vac.salary, reverse=reverse)


def sort_by_title(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортирует вакансии по названию в алфавитном порядке"""
    return sorted(vacancies, key=lambda vac: vac.title.lower())


