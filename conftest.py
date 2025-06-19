import pytest
import requests
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods
from data import BASE_URL, COURIERS_URL


@pytest.fixture()
def courier():
    courier_data = CourierMethods.generate_courier_data_all_fields()
    response = requests.post(f'{BASE_URL}{COURIERS_URL}', json=courier_data)
    return courier_data


@pytest.fixture()
def courier_id(courier):
    login_payload = {
        "login": courier["login"],
        "password": courier["password"]
    }
    response = requests.post(f'{BASE_URL}{COURIERS_URL}login', json=login_payload)
    return response.json().get("id")  

