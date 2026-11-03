import pytest
import requests

from data import STELLAR_BURGERS_URL
from helpers import create_user, get_ingredients, get_user_payload, login_user, register_new_user_and_return_email_password


@pytest.fixture
def delete_user():
    user_data = {}

    def set_user_data(email, password):
        user_data["email"] = email
        user_data["password"] = password

    yield set_user_data

    response = requests.post(f"{STELLAR_BURGERS_URL}/api/auth/login", json=user_data)
    token = response.json()["accessToken"]
    requests.delete(f"{STELLAR_BURGERS_URL}/api/auth/user", headers={"Authorization": token})


@pytest.fixture
def user_data(delete_user):
    email, password = register_new_user_and_return_email_password()
    delete_user(email, password)
    return {"email": email, "password": password}

@pytest.fixture
def registered_user(delete_user):
    payload = get_user_payload()
    create_user(payload)
    delete_user(payload["email"], payload["password"])
    return payload

@pytest.fixture
def user_token(user_data):
    payload = {"email": user_data["email"], "password": user_data["password"]}
    return login_user(payload).json()["accessToken"]

@pytest.fixture
def ingredient_ids():
    ingredients = get_ingredients().json()["data"]
    return [ingredients[0]["_id"], ingredients[1]["_id"]]