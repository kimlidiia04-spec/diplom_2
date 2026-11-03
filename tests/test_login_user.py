import allure

from data import WRONG_EMAIL, WRONG_PASSWORD
from helpers import login_user

@allure.feature("Авторизация пользователя")
class TestLoginUser:

    @allure.story("Успешная авторизация")
    @allure.title("Пользователь может авторизоваться")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_user(self, user_data):
        payload = {"email": user_data["email"], "password": user_data["password"]}
        response = login_user(payload)
        assert response.status_code == 200

    @allure.story("Успешная авторизация")
    @allure.title("При успешной авторизации возвращается accessToken")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_user_returns_access_token(self, user_data):
        payload = {"email": user_data["email"], "password": user_data["password"]}
        response = login_user(payload)
        assert "accessToken" in response.json()

    @allure.story("Неверный пароль")
    @allure.title("Нельзя авторизоваться с неверным паролем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_user_with_wrong_password(self, user_data):
        payload = {"email": user_data["email"], "password": WRONG_PASSWORD}
        response = login_user(payload)
        assert response.status_code == 401

    @allure.story("Неверный email")
    @allure.title("Нельзя авторизоваться с неверным email")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_user_with_wrong_email(self, user_data):
        payload = {"email": WRONG_EMAIL, "password": user_data["password"]}
        response = login_user(payload)
        assert response.status_code == 401

    @allure.story("Неверный email и пароль")
    @allure.title("Нельзя авторизоваться с неверным email и паролем")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_user_with_wrong_email_and_password(self):
        payload = {"email": WRONG_EMAIL, "password": WRONG_PASSWORD}
        response = login_user(payload)
        assert response.status_code == 401