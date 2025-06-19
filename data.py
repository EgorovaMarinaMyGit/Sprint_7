BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
ORDERS_URL = 'orders/'
COURIERS_URL = 'courier/'
TRACK_URL = 'track/'
ACCEPT_URL = 'accept/'


COURIER_DATA_SUCCESS = {
    "login": "Tutanhamon_account3",
    "password": "qazwsxedcrfv",
    "firstname": "Tutanhamon"
}

COURIER_DATA_NO_LOGIN = {
    "login": "",
    "password": "qwertyuiop",
    "firstname": "Puaro"
}

COURIER_DATA_NO_PASSWORD = {
    "login": "zxcvbnm1",
    "password": "",
    "firstname": "Agata"
}

COURIER_DATA_NO_FIRSTNAME = {
    "login": "zxcvbnmqq1",
    "password": "asdfghjww",
    "firstname": ""
}

COURIER_DATA_INCORRECT_LOGIN = {
    "login": "Tutanhamon_account_incorrect1",
    "password": "qazwsxedcrfv",
    "firstname": "Tutanhamon"
}

COURIER_DATA_INCORRECT_PASSWORD = {
    "login": "Tutanhamon_account1",
    "password": "qazwsxedcrfv_incorrect",
    "firstname": "Tutanhamon"
}

COURIER_DATA_NO_EXIST_ACCOUNT = {
    "login": "no_exist_login12344",
    "password": "no_exist_password",
    "firstname": "no_exist_firsname"
}


ORDER_DATA_1 = {
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

ORDER_DATA_2 = {
    "firstName": "Ivan",
    "lastName": "Petrov",
    "address": "Moscow, Tverskaya 15",
    "metroStation": 7,
    "phone": "+7 495 987 65 43",
    "rentTime": 10,
    "deliveryDate": "2023-12-15",
    "comment": "Leave package at the entrance, please.",
    "color": [
        "GREY"
    ]
}

ORDER_DATA_3 = {
    "firstName": "Johnie",
    "lastName": "Davis",
    "address": "Man, 50",
    "metroStation": 34,
    "phone": "+7 4561 555 441 331",
    "rentTime": 7,
    "deliveryDate": "2024-01-10",
    "comment": "Ring the doorbell twice.",
    "color": [
        "BLACK",
        "GREY"
    ]
}

ORDER_DATA_4 = {
    "firstName": "Alice",
    "lastName": "Smith",
    "address": "New York, 123 Broadway",
    "metroStation": 12,
    "phone": "+1 212 555 7890",
    "rentTime": 5,
    "deliveryDate": "2024-02-15",
    "comment": "Leave at the front desk.",
    "color": [
        "",
        ""
    ]
}