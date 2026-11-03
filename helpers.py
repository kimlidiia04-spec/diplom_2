import allure
import requests

from data import STELLAR_BURGERS_URL, USER_EMAIL, USER_NAME, USER_PASSWORD

@allure.step("Подготовить данные для создания пользователя")
def get_user_payload():
    return {
        "email": USER_EMAIL,
        "password": USER_PASSWORD,
        "name": USER_NAME,
    }

@allure.step("Отправить запрос на создание пользователя")
def create_user(payload):
    return requests.post(f"{STELLAR_BURGERS_URL}/api/auth/register", json=payload)

@allure.step("Создать нового пользователя и получить email и пароль")
def register_new_user_and_return_email_password():
    requests.post(f"{STELLAR_BURGERS_URL}/api/auth/register", json=get_user_payload())
    return USER_EMAIL, USER_PASSWORD

@allure.step("Отправить запрос на авторизацию пользователя")
def login_user(payload):
    return requests.post(f"{STELLAR_BURGERS_URL}/api/auth/login", json=payload)

@allure.step("Отправить запрос на получение списка ингредиентов")
def get_ingredients():
    return requests.get(f"{STELLAR_BURGERS_URL}/api/ingredients")

@allure.step("Отправить запрос на создание заказа без авторизации")
def create_order(payload):
    return requests.post(f"{STELLAR_BURGERS_URL}/api/orders", json=payload)

@allure.step("Отправить запрос на создание заказа с авторизацией")
def create_order_with_auth(payload, token):
    return requests.post(f"{STELLAR_BURGERS_URL}/api/orders", json=payload, headers={"Authorization": token})