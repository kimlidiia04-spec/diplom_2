import allure

from helpers import create_user, get_user_payload

@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создать нового пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user(self, delete_user):
        payload = get_user_payload()

        response = create_user(payload)
        delete_user(payload["email"], payload["password"])

        assert response.status_code == 200

    @allure.story("Успешное создание пользователя")
    @allure.title("После создания пользователя возвращается success true")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_returns_success_true(self, delete_user):
        payload = get_user_payload()

        response = create_user(payload)
        delete_user(payload["email"], payload["password"])

        assert response.json()["success"] is True

    @allure.story("Создание дубликата пользователя")
    @allure.title("Нельзя создать пользователя, который уже зарегистрирован")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_duplicate_user(self, registered_user):
        response = create_user(registered_user)

        assert response.status_code == 403

    @allure.story("Создание пользователя без email")
    @allure.title("Нельзя создать пользователя без email")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_without_email(self):
        payload = get_user_payload()
        del payload["email"]

        response = create_user(payload)

        assert response.status_code == 403

    @allure.story("Создание пользователя без пароля")
    @allure.title("Нельзя создать пользователя без пароля")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_without_password(self):
        payload = get_user_payload()
        del payload["password"]

        response = create_user(payload)

        assert response.status_code == 403

    @allure.story("Создание пользователя без имени")
    @allure.title("Нельзя создать пользователя без имени")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_without_name(self):
        payload = get_user_payload()
        del payload["name"]

        response = create_user(payload)

        assert response.status_code == 403