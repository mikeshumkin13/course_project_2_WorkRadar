import pytest
import requests
from api.hh_api import HeadHunterAPI


@pytest.fixture
def hh_api():
    """Фикстура для создания экземпляра API hh.ru"""
    return HeadHunterAPI()


def test_get_vacancies_success(mocker, hh_api):
    """Тестируем успешное получение вакансий"""
    mock_response = {
        "items": [
            {"name": "Python Developer", "alternate_url": "https://hh.ru/vacancy/123"},
            {"name": "Backend Developer", "alternate_url": "https://hh.ru/vacancy/456"},
        ]
    }

    mocker.patch("api.hh_api.requests.get", return_value=mocker.Mock(status_code=200, json=lambda: mock_response))

    vacancies = hh_api.get_vacancies("Python")
    assert len(vacancies) == 2
    assert vacancies[0]["name"] == "Python Developer"
    assert vacancies[1]["name"] == "Backend Developer"


def test_get_vacancies_fail(mocker, hh_api):
    """Тестируем обработку ошибки API"""
    mock_response = mocker.Mock(status_code=500, text="Internal Server Error")
    mock_response.json.return_value = {}  # Добавляем мок для json()

    mocker.patch("api.hh_api.requests.get", return_value=mock_response)

    vacancies = hh_api.get_vacancies("Python")
    assert vacancies == []  # Ожидаем пустой список при ошибке API


def test_get_vacancies_http_error(mocker, hh_api):
    """Тестируем обработку ошибки 404"""
    mocker.patch("api.hh_api.requests.get", side_effect=requests.exceptions.HTTPError("404 Not Found"))

    vacancies = hh_api.get_vacancies("Python")
    assert vacancies == []  # Ожидаем пустой список при ошибке API


def test_get_vacancies_timeout(mocker, hh_api):
    """Тестируем обработку ошибки сети (таймаут)"""
    mocker.patch("api.hh_api.requests.get", side_effect=requests.exceptions.Timeout)

    vacancies = hh_api.get_vacancies("Python")
    assert vacancies == []  # Ожидаем пустой список при таймауте

