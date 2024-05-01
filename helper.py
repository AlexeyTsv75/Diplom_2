import random
import allure
import requests

import data


@allure.step("Создаем случайный емейл")
def get_random_email():
    email = f'{random.choice(['alex', 'john', 'kean'])}.{random.randint(100, 999)}@mail.{random.choice(['net', 'com',
                                                                                                        'ru'])}'
    return email


@allure.step("Создаем случайны набор данных")
def get_random_user_payload():
    email = get_random_email()
    password = f'{random.randint(100000, 999999)}'
    name = f'{random.choice(['alex', 'john', 'kean'])}'
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload


@allure.step("Регистрация нового пользователя")
def new_user_creation():
    payload = get_random_user_payload()
    response = requests.post(data.MAIN_PAGE+data.REGISTRATION, data=payload)
    payload["code"] = response.status_code
    payload["token"] = response.json()["accessToken"]
    payload["retoken"] = response.json()["refreshToken"]
    return payload


@allure.step("Удаление пользователя")
def delete_user(token):
    requests.delete(data.MAIN_PAGE+data.USER, headers={'Authorization': token})


@allure.step("Авторизация пользователя")
def new_user_login():
    payload = new_user_creation()
    response = requests.post(data.MAIN_PAGE+data.LOGIN, data=payload)
    payload["token"] = response.json()["accessToken"]
    payload["retoken"] = response.json()["refreshToken"]
    return payload


@allure.step("Создние списка ингредиентов")
def creation_list_of_ingredients():
    response = requests.get(data.MAIN_PAGE+data.INGREDIENTS)
    list_ingredients = response.json()["data"]
    list_hash_ingredients = []
    for ingredient in list_ingredients:
        list_hash_ingredients.append(ingredient["_id"])
    return list_hash_ingredients


@allure.step("Создаем заказ для авторизованного пользователя")
def creation_order_authorized_user(token):
    ingredients = creation_list_of_ingredients()
    list_of_ingredient = [ingredients[0], ingredients[1], ingredients[2]]
    payload_order = {"ingredients": list_of_ingredient}
    requests.post(data.MAIN_PAGE + data.ORDER,
                  data=payload_order,
                  headers={'Authorization': token})
