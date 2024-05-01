import allure
import requests

import data
import helper


class TestGetUserOrder:
    @allure.title("Проверяем получение заказа у авторизованного пользователя")
    def test_get_order_authorized_user(self):
        payload = helper.new_user_login()
        for i in range(data.quantity_orders):
            helper.creation_order_authorized_user(payload["token"])
        response = requests.get(data.MAIN_PAGE+data.ORDER,
                                headers={'Authorization': payload["token"]})
        code = response.status_code
        orders = response.json()["orders"]
        helper.delete_user(payload["token"])
        assert code == 200 and len(orders) == data.quantity_orders

    @allure.title("Проверяем получение заказа у неавторизованного пользователя")
    def test_get_order_unauthorized_user(self):
        response = requests.get(data.MAIN_PAGE+data.ORDER)
        code = response.status_code
        orders = response.json()["message"]
        assert code == 401 and orders == "You should be authorised"
