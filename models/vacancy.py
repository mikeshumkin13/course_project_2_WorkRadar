from dataclasses import dataclass


@dataclass
class Vacancy:
    """Класс вакансии, содержащий основные данные"""

    title: str  # Название вакансии
    url: str  # Ссылка на вакансию
    salary: int  # Зарплата
    description: str  # Описание вакансии

    __slots__ = ("title", "url", "salary", "description")

    def __post_init__(self):
        """Валидация данных после инициализации"""
        if not self.title:
            raise ValueError("Название вакансии не может быть пустым")
        if not self.url.startswith("http"):
            raise ValueError("Некорректный URL вакансии")
        if self.salary is None:
            self.salary = 0  # Если зарплата не указана, ставим 0
        if self.salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        if not self.description:
            self.description = "Описание отсутствует"

    def __lt__(self, other):
        """Сравнение вакансий по зарплате (меньше)"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __gt__(self, other):
        """Сравнение вакансий по зарплате (больше)"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary

    def __eq__(self, other):
        """Сравнение вакансий по зарплате (равенство)"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary == other.salary
