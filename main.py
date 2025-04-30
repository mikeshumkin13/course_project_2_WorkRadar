from api.hh_api import HeadHunterAPI
from storage.json_storage import JSONStorage
from utils.filters import filter_by_salary, filter_by_keyword
from utils.sorters import sort_by_salary
from models.vacancy import Vacancy


def main():
    """Главное меню программы"""
    api = HeadHunterAPI()
    storage = JSONStorage()

    while True:
        print("\n===== Меню =====")
        print("1. Поиск вакансий по ключевому слову")
        print("2. Показать сохранённые вакансии")
        print("3. Показать топ-N вакансий по зарплате")
        print("4. Фильтровать вакансии по ключевому слову")
        print("5. Удалить вакансию")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            search_vacancies(api, storage)
        elif choice == "2":
            show_saved_vacancies(storage)
        elif choice == "3":
            show_top_vacancies(storage)
        elif choice == "4":
            filter_vacancies(storage)
        elif choice == "5":
            delete_vacancy(storage)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: выберите корректный пункт меню.")


def search_vacancies(api, storage):
    """Запрашивает вакансии из API и сохраняет их"""
    query = input("Введите ключевое слово для поиска: ")
    vacancies = api.get_vacancies(query)

    if not vacancies:
        print("Вакансии не найдены.")
        return

    print(f"Найдено {len(vacancies)} вакансий. Сохраняем их в JSON-файл.")
    for vacancy_data in vacancies:
        vacancy = Vacancy(
            vacancy_data["name"],
            vacancy_data["alternate_url"],
            vacancy_data["salary"]["from"] if vacancy_data.get("salary") and vacancy_data["salary"].get("from") else 0,
            vacancy_data.get("snippet", {}).get("requirement", "Описание отсутствует"),
        )
        storage.add_vacancy(vacancy)


    print("Вакансии сохранены!")


def show_saved_vacancies(storage):
    """Выводит сохранённые вакансии"""
    vacancies = storage.get_vacancies()
    if not vacancies:
        print("Сохранённых вакансий нет.")
        return

    for idx, vacancy in enumerate(vacancies, 1):
        print(f"{idx}. {vacancy.title} - {vacancy.salary} руб. ({vacancy.url})")


def show_top_vacancies(storage):
    """Выводит топ-N вакансий по зарплате"""
    try:
        n = int(input("Введите количество вакансий для вывода: "))
    except ValueError:
        print("Ошибка: введите число.")
        return

    vacancies = sort_by_salary(storage.get_vacancies())[:n]
    if not vacancies:
        print("Вакансий нет.")
        return

    for idx, vacancy in enumerate(vacancies, 1):
        print(f"{idx}. {vacancy.title} - {vacancy.salary} руб. ({vacancy.url})")


def filter_vacancies(storage):
    """Фильтрует вакансии по ключевому слову"""
    keyword = input("Введите ключевое слово для фильтрации: ")
    vacancies = filter_by_keyword(storage.get_vacancies(), keyword)

    if not vacancies:
        print("Нет вакансий с таким ключевым словом.")
        return

    for idx, vacancy in enumerate(vacancies, 1):
        print(f"{idx}. {vacancy.title} - {vacancy.salary} руб. ({vacancy.url})")


def delete_vacancy(storage):
    """Удаляет вакансию из хранилища"""
    show_saved_vacancies(storage)

    try:
        idx = int(input("Введите номер вакансии для удаления: ")) - 1
    except ValueError:
        print("Ошибка: введите число.")
        return

    vacancies = storage.get_vacancies()
    if idx < 0 or idx >= len(vacancies):
        print("Ошибка: неверный номер вакансии.")
        return

    storage.delete_vacancy(vacancies[idx])
    print("Вакансия удалена.")


if __name__ == "__main__":
    main()

