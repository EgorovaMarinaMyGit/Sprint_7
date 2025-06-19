import allure
import random
from methods.courier_methods import CourierMethods
from conftest import courier
from data import COURIER_DATA_NO_LOGIN, COURIER_DATA_NO_PASSWORD, COURIER_DATA_INCORRECT_LOGIN, COURIER_DATA_INCORRECT_PASSWORD, COURIER_DATA_NO_EXIST_ACCOUNT


class TestCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_passed(self):
        courier = CourierMethods()  # создаем объект класса
        response, status_code, login, password = courier.create_courier_success()
        assert status_code == 201 and response == {'ok': True}


    @allure.title("Создание двух одинаковых курьеров")
    def test_create_courier_with_the_same_data(self):
        courier = CourierMethods() 
        response, status_code, login, password = courier.create_courier_success()
        params_create = {
            "login": login,
            "password": password
        }
        response, status_code, login, password = courier.create_courier_success(params_create)
        assert status_code == 409 and response == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}


    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login(self):
        courier = CourierMethods()
        response, status_code = courier.courier_create_no_login(COURIER_DATA_NO_LOGIN)
        assert status_code == 400 and  response == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}


    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password(self):
        courier = CourierMethods()
        response, status_code = courier.courier_create_no_login(COURIER_DATA_NO_PASSWORD)
        assert status_code == 400 and response == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}


    @allure.title("Создание курьера без имени")
    def test_create_courier_without(self):
        courier = CourierMethods()
        response, status_code = courier.courier_create_without_name()
        assert status_code == 201 and response == {'ok': True}


    @allure.title("Успешная авторизация курьера")
    def test_autorisation_courier_success(self):
        courier = CourierMethods() 
        response, status_code, login, password = courier.create_courier_success()
        params_create = {
            "login": login,
            "password": password
        }
        response, status_code, courier_id = courier.courier_login_success(params_create)
        assert status_code == 200 and courier_id is not None


    @allure.title("Авторизация с неправильным логином")
    def test_autorisation_courier_incorrect_login(self):
        courier = CourierMethods()
        response, status_code = courier.courier_login_incorrect_login(COURIER_DATA_INCORRECT_LOGIN)
        assert status_code == 404 and response == {"code": 404, "message": "Учетная запись не найдена"}


    @allure.title("Авторизация с неправильным паролем")
    def test_autorisation_courier_incorrect_password(self):
        courier = CourierMethods()
        response, status_code = courier.courier_login_incorrect_password(COURIER_DATA_INCORRECT_PASSWORD)
        assert status_code == 404 and response == {"code": 404, "message": "Учетная запись не найдена"}


    @allure.title("Авторизация без логина")
    def test_autorisation_courier_without_login(self):
        courier = CourierMethods()
        response, status_code = courier.courier_login_without_login(COURIER_DATA_NO_LOGIN)
        assert status_code == 400 and response == {"code": 400, "message": "Недостаточно данных для входа"}


    @allure.title("Авторизация без пароля")
    def test_autorisation_courier_without_password(self):
        courier = CourierMethods()
        response, status_code = courier.courier_login_without_password(COURIER_DATA_NO_PASSWORD)
        assert status_code == 400 and response == {"code": 400, "message": "Недостаточно данных для входа"}


    @allure.title("Авторизация несуществующего пользователя")
    def test_autorisation_no_exist_user(self):
        courier = CourierMethods()
        response, status_code = courier.courier_login_no_exist_data(COURIER_DATA_NO_EXIST_ACCOUNT)
        assert status_code == 404 and response == {"code": 404, "message": "Учетная запись не найдена"}


    @allure.title("Удаление курьера с существующим id")
    def test_delete_courier_id_exist(self):
        courier = CourierMethods() 
        response, status_code, login, password = courier.create_courier_success()
        params_create = {
            "login": login,
            "password": password
        }
        response, status_code, courier_id = courier.courier_login_success(params_create)
        response, status_code = courier.courier_delete(courier_id)
        assert status_code == 200 and response == {'ok': True}


    @allure.title("Удаление курьера с несуществующим id")
    def test_delete_courier_id_not_exist(self):
        courier = CourierMethods() 
        random_id = random.randint(10_000, 99_999)
        response, status_code = courier.courier_delete(random_id)
        assert status_code == 404 and response == {"code": 404, "message": "Курьера с таким id нет."}


    @allure.title("Удаление курьера без id")
    def test_delete_courier_without_id(self):
        courier = CourierMethods()
        id = ""
        response, status_code = courier.courier_delete(id)
        assert status_code == 404 and response == {"code": 404, "message": "Not Found."}

