# Course Project 2 - WorkRadar

# WorkRadar – Поиск и фильтрация вакансий

## 📌 Описание проекта
WorkRadar – это консольное приложение на Python для поиска вакансий с hh.ru.  
Позволяет **искать, фильтровать, сортировать и удалять вакансии**.

## 🚀 Функциональность
✅ Поиск вакансий через API hh.ru  
✅ Сохранение вакансий в JSON  
✅ Вывод сохранённых вакансий  
✅ Топ-N вакансий по зарплате  
✅ Фильтрация по ключевым словам  
✅ Удаление вакансий  

## 🛠️ Установка и запуск
1. **Клонируем репозиторий**:
   
   git clone git@github.com:mikeshumkin13/course_project_2_WorkRadar.git
   cd course_project_2_WorkRadar

2. **Создаём виртуальное окружение:**
poetry install
3. **Запускаем приложение:**
python3 main.py


🔍 Пример работы:

===== Меню =====
1. Поиск вакансий по ключевому слову
2. Показать сохранённые вакансии
3. Показать топ-N вакансий по зарплате
4. Фильтровать вакансии по ключевому слову
5. Удалить вакансию
6. Выйти
Выберите действие: 


Структура проекта

.
├── README.md
├── api
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── base_api.cpython-312.pyc
│   │   └── hh_api.cpython-312.pyc
│   ├── base_api.py
│   └── hh_api.py
├── logs
│   └── api.log
├── main.py
├── models
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   └── vacancy.cpython-312.pyc
│   └── vacancy.py
├── poetry.lock
├── pyproject.toml
├── storage
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── base_storage.cpython-312.pyc
│   │   └── json_storage.cpython-312.pyc
│   ├── base_storage.py
│   └── json_storage.py
├── tests
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── test_api.cpython-312-pytest-8.3.5.pyc
│   │   ├── test_json_storage.cpython-312-pytest-8.3.5.pyc
│   │   ├── test_storage.cpython-312-pytest-8.3.5.pyc
│   │   ├── test_utils.cpython-312-pytest-8.3.5.pyc
│   │   └── test_vacancy.cpython-312-pytest-8.3.5.pyc
│   ├── test_api.py
│   ├── test_json_storage.py
│   ├── test_utils.py
│   └── test_vacancy.py
├── utils
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── filters.cpython-312.pyc
│   │   └── sorters.cpython-312.pyc
│   ├── filters.py
│   └── sorters.py
└── vacancies.json

12 directories, 39 files


Тестирование
pytest tests/

🤝 Авторы:
mikeshumkin13
https://github.com/mikeshumkin13


