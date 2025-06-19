import requests
import allure
from data import BASE_URL, ORDERS_URL, TRACK_URL, ACCEPT_URL


class OrderMethods():

    @allure.step("Создание заказа")
    def create_order(sels, params):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=params)
        return response.json(), response.status_code, response.json().get('track')
    
    @allure.step("Получение списка заказов")
    def get_orders_list(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response.json(), response.status_code
    
    @allure.step("Получение заказа с использованием трекингового номера")
    def get_order_with_some_track(self, track):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}{TRACK_URL}', params={'t': track})
        return response.json(), response.status_code, response.json()['order']['id']
    
    @allure.step("Получение заказа без использования трекингового номера")
    def get_order_without_track(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}{TRACK_URL}', params={'t': ''})
        return response.json(), response.status_code
    
    @allure.step("Получение заказа с некорректным трекинговым номером")
    def get_order_with_incorrect_track(self, track):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}{TRACK_URL}', params={'t': track})
        return response.json(), response.status_code

    @allure.step("Принять заказ")
    def accept_order(self, id_order, params):
        response = requests.put(f'{BASE_URL}{ORDERS_URL}{ACCEPT_URL}{id_order}', params=params)
        return response.json(), response.status_code