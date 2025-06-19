import allure
import pytest
import random
from methods.order_methods import OrderMethods
from methods.courier_methods import CourierMethods
from data import ORDER_DATA_1, ORDER_DATA_2, ORDER_DATA_3, ORDER_DATA_4


class TestOrder:

    @allure.title("Создание заказа")
    @pytest.mark.parametrize(
        'order_data',
        [
            ORDER_DATA_1,
            ORDER_DATA_2,
            ORDER_DATA_3,
            ORDER_DATA_4
        ]
    )

    def test_create_order(self, order_data):
        order = OrderMethods()
        response, status_code, order_track = order.create_order(order_data)
        assert status_code == 201 and order_track is not None


    @allure.title("Получение списка заказов")
    def test_get_list_of_orders(self):
        order = OrderMethods()
        response, status_code = order.get_orders_list()
        assert status_code == 200 and isinstance(response, dict) and len(response) > 0


    @allure.title("Получение заказа по трекинговому номеру")
    def test_get_order_with_correct_track(self):
        order = OrderMethods()
        #response, status_code, order_track = order.create_order(ORDER_DATA_1)
        order_track = order.create_order(ORDER_DATA_1)[2]
        response, status_code, order_id = order.get_order_with_some_track(order_track)
        expected_result = {
            "firstName": "Sakura",
            "lastName": "Haruno",
            "address": "Tokyo, Shibuya 10-5",
            "metroStation": 12,
            "phone": "+7 900 123 45 67",
            "rentTime": 3,
            "deliveryDate": "2023-11-01",
            "comment": "Please deliver between 9am and 12pm",
            "color": [
                "BLACK"
            ]
        }
        assert status_code == 200 and ORDER_DATA_1 == expected_result

    
    @allure.title("Получение заказа без трекингового номера")
    def test_get_order_without_track(self):
        order = OrderMethods()
        response, status_code = order.get_order_without_track()
        assert status_code == 400 and response == {"code": 400, "message": "Недостаточно данных для поиска"}

    
    @allure.title("Получение заказа с некорректным трекинговым номером")
    def test_get_order_with_incorrect_track(self):
        order = OrderMethods()
        track = random.randint(10_0000, 99_9999)
        response, status_code = order.get_order_with_incorrect_track(track)
        assert status_code == 404 and response == {"code": 404, "message": "Заказ не найден"}


    @allure.title("Принять заказ используя корректные Id курьера и Id заказа")
    def test_get_order_correct_ids_courier_and_order(self, courier_id):
        id_courier = courier_id
        params = {
            "courierId": id_courier
        }
   
        order = OrderMethods()
        order_track = order.create_order(ORDER_DATA_1)[2]
        id_order = order.get_order_with_some_track(order_track)[2]
        response, status_code = order.accept_order(id_order, params)

        assert status_code == 200 and response == {"ok": True}


    @allure.title("Принять заказ используя корректный Id заказа и без Id курьера")
    def test_get_order_correct_id_order_and_no_id_courier(self):
        params = {
            "courierId": ""
        }
   
        order = OrderMethods()
        order_track = order.create_order(ORDER_DATA_1)[2]
        id_order = order.get_order_with_some_track(order_track)[2]
        response, status_code = order.accept_order(id_order, params)

        assert status_code == 400 and response == {"code": 400, "message": "Недостаточно данных для поиска"}


    @allure.title("Принять заказ используя некорректный Id курьера и корректный Id заказа")
    def test_get_order_incorrect_id_courier_and_correct_id_order(self):
        params = {
            "courierId": "1234554"
        }
   
        order = OrderMethods()
        order_track = order.create_order(ORDER_DATA_1)[2]
        id_order = order.get_order_with_some_track(order_track)[2]
        response, status_code = order.accept_order(id_order, params)

        assert status_code == 404 and response == {"code": 404, "message": "Курьера с таким id не существует"}


    @allure.title("Принять заказ используя корректные Id курьера и без Id заказа")
    def test_get_order_correct_id_courier_and_no_id_order(self, courier_id):
        id_courier = courier_id
        params = {
            "courierId": id_courier
        }
   
        order = OrderMethods()
        id_order = ''
        response, status_code = order.accept_order(id_order, params)

        assert status_code == 404 and response ==  {"code": 404, "message": "Not Found."}

    @allure.title("Принять заказ используя корректный Id курьера и некорректный Id заказа")
    def test_get_order_correct_id_courier_and_incorrect_id_order(self, courier_id):
        id_courier = courier_id
        params = {
            "courierId": id_courier
        }
   
        order = OrderMethods()
        id_order = 53456
        response, status_code = order.accept_order(id_order, params)

        assert status_code == 404 and response == {"code": 404, "message": "Заказа с таким id не существует"}
