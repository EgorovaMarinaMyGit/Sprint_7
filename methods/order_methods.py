import requests
import allure
from data import BASE_URL, ORDERS_URL, TRACK_URL, ACCEPT_URL


class OrderMethods:

    @allure.step("Создание заказа")
    def create_order(sels, params):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=params)
        return response.json(), response.status_code, response.json().get('track')
    
    @allure.step("Получение списка заказов")
    def get_orders_list(self):
        response = requests.get(f'{BASE_URL}{ORDERS_URL}')
        return response.json(), response.status_code
    
    @allure.step("Получение заказа")
    def get_order_with_some_track(self, params):
        response = None
        try:
            response = requests.get(f'{BASE_URL}{ORDERS_URL}{TRACK_URL}', params=params)
            json_response = response.json()
        except requests.RequestException as e:
            # Обработка ошибок сети или запроса
            return {"message": str(e)}, None, None
        except ValueError:
            # Обработка ошибок при парсинге JSON
            return {"message": "Некорректный ответ сервера"}, response.status_code if response else None, None
        # Проверяем наличие ключа 'order'
        order_id = None
        if 'order' in json_response:
            order_id = json_response['order'].get('id')
        return response.json(), response.status_code, order_id
  
    @allure.step("Принять заказ")
    def accept_order(self, id_order, params):
        response = requests.put(f'{BASE_URL}{ORDERS_URL}{ACCEPT_URL}{id_order}', params=params)
        return response.json(), response.status_code