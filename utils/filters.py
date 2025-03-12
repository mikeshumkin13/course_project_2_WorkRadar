from typing import List
from models.vacancy import Vacancy


def filter_by_salary(vacancies: List[Vacancy], min_salary: int) -> List[Vacancy]:
    """Фильтрует вакансии по минимальной зарплате"""
    return [vac for vac in vacancies if vac.salary >= min_salary]


def filter_by_keyword(vacancies: List[Vacancy], keyword: str) -> List[Vacancy]:
    """Фильтрует вакансии по ключевому слову в названии или описании"""
    keyword = keyword.lower()
    return [vac for vac in vacancies if keyword in vac.title.lower() or keyword in vac.description.lower()]

