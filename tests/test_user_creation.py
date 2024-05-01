import allure
import pytest
import requests
import helper
import data


class TestUserCreation:
    @allure.title(
        "Проверяем успешное создание нового пользователя")
    def test_new_user_creation_success(self):
        payload = helper.get_random_user_payload()
        response = requests.post(data.MAIN_PAGE + data.REGISTRATION, data=payload)
        code = response.status_code
        token = response.json()["accessToken"]
        helper.delete_user(token)
        assert code == 200 and token is not None

    @allure.title(
        "Проверяем невозможность создания двух одинаковых пользователей")
    def test_creation_two_similar_users_impossible(self):
        payload = helper.get_random_user_payload()
        payload_first = payload
        response_first = requests.post(data.MAIN_PAGE + data.REGISTRATION, data=payload_first)
        token = response_first.json()["accessToken"]
        payload_second = payload
        response_second = requests.post(data.MAIN_PAGE + data.REGISTRATION, data=payload_second)
        code_second = response_second.status_code
        message_second = response_second.json()["message"]
        helper.delete_user(token)
        assert code_second == 403 and message_second == "User already exists"

    @allure.title(
        "Проверяем невозможность создание нового пользователя без необходимых полей")
    @pytest.mark.parametrize('empty_field', ["email", "password", "name"])
    def test_create_user_without_needed_field_impossible(self, empty_field):
        payload = helper.get_random_user_payload()
        payload[empty_field] = ""
        response = requests.post(data.MAIN_PAGE + data.REGISTRATION, data=payload)
        assert response.status_code == 403 and response.json()["message"] == ("Email, password and name are "
                                                                              "required fields")



