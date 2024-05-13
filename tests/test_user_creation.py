import allure
import pytest
import requests
import helper
from data import UrlData
from data import DataAnswerMessage


class TestUserCreation:
    @allure.title(
        "Проверяем успешное создание нового пользователя")
    def test_new_user_creation_success(self):
        payload = helper.get_random_user_payload()
        response = requests.post(UrlData.MAIN_PAGE + UrlData.REGISTRATION, data=payload)
        code = response.status_code
        token = response.json()["accessToken"]
        helper.delete_user(token)
        assert code == 200 and token is not None

    @allure.title(
        "Проверяем невозможность создания двух одинаковых пользователей")
    def test_creation_two_similar_users_impossible(self):
        payload = helper.get_random_user_payload()
        response_first = requests.post(UrlData.MAIN_PAGE + UrlData.REGISTRATION, data=payload)
        token = response_first.json()["accessToken"]
        response_second = requests.post(UrlData.MAIN_PAGE + UrlData.REGISTRATION, data=payload)
        code_second = response_second.status_code
        message_second = response_second.json()["message"]
        helper.delete_user(token)
        assert code_second == 403 and message_second == DataAnswerMessage.existed_user

    @allure.title(
        "Проверяем невозможность создание нового пользователя без необходимых полей")
    @pytest.mark.parametrize('empty_field', ["email", "password", "name"])
    def test_create_user_without_needed_field_impossible(self, empty_field):
        payload = helper.get_random_user_payload()
        payload[empty_field] = ""
        response = requests.post(UrlData.MAIN_PAGE + UrlData.REGISTRATION, data=payload)
        assert response.status_code == 403 and response.json()["message"] == DataAnswerMessage.required_fields
