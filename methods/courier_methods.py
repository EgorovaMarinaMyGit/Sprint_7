import requests
import random
import string
import allure
from data import BASE_URL, COURIERS_URL

class CourierMethods():

    @allure.step("Создание курьера, все поля заполнены")
    def create_courier_success(self, params= None):
        if params is None:
            params = self.generate_courier_data_all_fields()
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=params)
        return response.json(), response.status_code, params['login'], params ['password']
    
    @allure.step("Успешная авторизация курьера")
    def courier_login_success(self, params):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', data=params)
        return response.json(), response.status_code, response.json().get('id')

    @allure.step("Создание курьера без логина")
    def courier_create_no_login(self, params):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=params)
        return response.json(), response.status_code

    @allure.step("Создание курьера без пароля")
    def courier_create_incorrect_login(self, params):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=params)
        return response.json(), response.status_code
    
    @allure.step("Создание курьера без имени")
    def courier_create_without_name(self, params= None):
        if params is None:
            params = self.generate_courier_data_without_name()
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=params)
        return response.json(), response.status_code
    
    @allure.step("Авторизация курьера с некорректным логином")
    def courier_login_incorrect_login(self, params):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', data=params)
        return response.json(), response.status_code

    @allure.step("Авторизация курьера с некорректным паролем")
    def courier_login_incorrect_password(self, params):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', data=params)
        return response.json(), response.status_code

    @allure.step("Авторизация курьера без ввода логина")
    def courier_login_without_login(self, params):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', data=params)
        return response.json(), response.status_code
    
    @allure.step("Авторизация курьера без ввода пароля")
    def courier_login_without_password(self, params):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', data=params)
        return response.json(), response.status_code

    @allure.step("Авторизация несуществующего курьера")
    def courier_login_no_exist_data(self, params):
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', data=params)
        return response.json(), response.status_code

    @allure.step("Удаление курьера")
    def courier_delete(self, id):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}/{id}')
        return response.json(), response.status_code


    def get_courier(self):
        response = requests.get(f'{BASE_URL}{COURIERS_URL}id')
        return response.json(), response.status_code
    

    @staticmethod
    def generate_courier_data_all_fields():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        return {
        "login": login,
        "password": password,
        "first_name": first_name
        }
    

    @staticmethod
    def generate_courier_data_without_name():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        
        # генерируем логин и пароль
        login = generate_random_string(10)
        password = generate_random_string(10)
        return {
        "login": login,
        "password": password,
        }