from dataclasses import dataclass

@dataclass(order=True)
class Vacancy:
    title: str
    url: str
    salary: int
    description: str

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        return False


    def __post_init__(self):
        """Вызываем методы валидации после инициализации атрибутов"""
        self._validate_title()
        self._validate_url()
        self._validate_salary()
        self._validate_description()

    def _validate_title(self):
        """Проверка корректности названия вакансии"""
        if not self.title or not isinstance(self.title, str):
            raise ValueError("Название вакансии должно быть строкой и не пустым")

    def _validate_url(self):
        """Проверка корректности URL"""
        if not self.url.startswith("http"):
            raise ValueError("URL вакансии должен начинаться с http")

    def _validate_salary(self):
        """Проверка корректности зарплаты"""
        if self.salary is None:
            self.salary = 0  # Если зарплата не указана, ставим 0
        if not isinstance(self.salary, int) or self.salary < 0:
            raise ValueError("Зарплата должна быть положительным числом")

    def _validate_description(self):
        """Проверка корректности описания вакансии"""
        if not self.description or not isinstance(self.description, str):
            self.description = "Описание отсутствует"


