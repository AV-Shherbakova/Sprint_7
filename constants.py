#URLS
URL_CREATE_COURIER = "https://qa-scooter.praktikum-services.ru/api/v1/courier"
URL_LOGIN_COURIER = "https://qa-scooter.praktikum-services.ru/api/v1/courier/login"
URL_ORDER_CREATE = "https://qa-scooter.praktikum-services.ru/api/v1/orders"
URL_GET_ORDER_LIST = 'https://qa-scooter.praktikum-services.ru/api/v1/orders?limit=10&page=0&nearestStation=["110"]'
URL_DELETE_COURIER = f"https://qa-scooter.praktikum-services.ru/api/v1/courier/"

#USER DATA
COURIER_LOGIN = "Vladislavv"
COURIER_PASSWORD = "6666"
USER_DATA = {
            "login": "Vladislavv",
            "password": "6666"
        }
NO_EXIST_USER_DATA = {
            "login": "Rihanna",
            "password": "9876"
        }

#CUSTOMER_DATA
CUSTOMER_DATA = {
    "firstName": "Elon",
    "lastName": "Musk",
    "address": "Lenina, 85",
    "metroStation": 4,
    "phone": "+7 999 555 35 35"
}

#ORDER_DATA
ORDER_DATA = {
    "rentTime": "2",
    "deliveryDate": "2025-01-31",
    "comment": "Say hello for my little friend"
}

#RESPONSE BODY
USER_EXIST_BODY = {
    "code": 409,
    "message": "Этот логин уже используется. Попробуйте другой."
}
NO_FIELD_TO_CREATE_BODY = {
    "code": 400,
    "message": "Недостаточно данных для создания учетной записи"
}
NO_FIELD_TO_LOGIN_BODY = {
    "code": 400,
    "message": "Недостаточно данных для входа"
}
ACCOUNT_NOT_FOUND_BODY = {
    "code": 404,
    "message": "Учетная запись не найдена"
}
