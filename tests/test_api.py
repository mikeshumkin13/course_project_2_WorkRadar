import pytest
import requests
from api.hh_api import HeadHunterAPI


@pytest.fixture
def hh_api():
    """Фикстура для создания экземпляра API hh.ru"""
    return HeadHunterAPI()


def test_get_vacancies_success(mocker, hh_api):
    """Тест успешного получения вакансий"""
    mock_response = {"items": [{"name": "Python Dev", "alternate_url": "https://hh.ru/vacancy/123"}]}

    # Мокаем `self._session.get`, а не `requests.get`
    mock_get = mocker.patch.object(hh_api._session, "get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    vacancies = hh_api.get_vacancies("Python")
    assert len(vacancies) == 1, f"Ожидали 1 вакансию, но получили {len(vacancies)}"


def test_get_vacancies_fail(mocker, hh_api):
    """Тест обработки ошибки API"""
    mock_get = mocker.patch.object(hh_api._session, "get")
    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = {}  # API возвращает пустой словарь

    vacancies = hh_api.get_vacancies("Python")
    assert vacancies == [], f"Ожидался пустой список, но получили {vacancies}"


def test_get_vacancies_http_error(mocker, hh_api):
    """Тест обработки ошибки 404"""
    mocker.patch.object(hh_api._session, "get", side_effect=requests.exceptions.HTTPError("404 Not Found"))

    vacancies = hh_api.get_vacancies("Python")
    assert vacancies == [], f"Ожидался пустой список при HTTP 404, но получили {vacancies}"


def test_get_vacancies_timeout(mocker, hh_api):
    """Тест обработки таймаута"""
    mocker.patch.object(hh_api._session, "get", side_effect=requests.exceptions.Timeout)

    vacancies = hh_api.get_vacancies("Python")
    assert vacancies == [], f"Ожидался пустой список при таймауте, но получили {vacancies}"
