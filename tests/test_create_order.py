import allure

from data import ORDER_WITHOUT_INGREDIENTS, ORDER_WITH_INVALID_HASH
from helpers import create_order, create_order_with_auth

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.story("Создание заказа с авторизацией")
    @allure.title("Создать заказ с авторизацией")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order_with_auth(self, user_token, ingredient_ids):
        response = create_order_with_auth({"ingredients": ingredient_ids}, user_token)
        assert response.status_code == 200

    @allure.story("Создание заказа без авторизации")
    @allure.title("Создать заказ без авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order_without_auth(self, ingredient_ids):
        response = create_order({"ingredients": ingredient_ids})
        assert response.status_code == 200

    @allure.story("Создание заказа с ингредиентами")
    @allure.title("При создании заказа с ингредиентами возвращается номер заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_order_with_ingredients(self, ingredient_ids):
        response = create_order({"ingredients": ingredient_ids})
        assert "number" in response.json()["order"]

    @allure.story("Создание заказа без ингредиентов")
    @allure.title("Нельзя создать заказ без ингредиентов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_order_without_ingredients(self):
        response = create_order(ORDER_WITHOUT_INGREDIENTS)
        assert response.status_code == 400

    @allure.story("Создание заказа с неверным хешем")
    @allure.title("Нельзя создать заказ с неверным хешем ингредиента")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_order_with_invalid_hash(self):
        response = create_order(ORDER_WITH_INVALID_HASH)
        assert response.status_code == 400