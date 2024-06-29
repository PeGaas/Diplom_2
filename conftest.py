import pytest
import requests

from data_static import MAIN_URL, EMAIL, PASSWORD, NAME, CREATE_UNIQUE_USER, DELETE_USER, LOGIN_USER, GET_INGREDIENTS, \
    CREATE_ORDER


@pytest.fixture()
def create_user():
    # Создать нового пользователя
    payload = {"email": EMAIL, "password": PASSWORD, "name": NAME}
    response = requests.post(f'{MAIN_URL}{CREATE_UNIQUE_USER}', data=payload)

    yield response

    # Удалить пользователя
    requests.delete(f'{MAIN_URL}{DELETE_USER}', headers={'Authorization': response.json()['accessToken']})


@pytest.fixture()
def authorization_user(create_user):
    # Авторизация пользователя
    payload = {"email": create_user.json()['user']['email'], "password": PASSWORD,
               "name": create_user.json()['user']['name']}
    response = requests.post(f'{MAIN_URL}{LOGIN_USER}', data=payload)

    yield response


@pytest.fixture()
def get_ingredients():
    random_ingredients = []
    # Получить список ингридиентов
    response = requests.get(f'{MAIN_URL}{GET_INGREDIENTS}')

    for i in response.json()['data']:
        random_ingredients.append(i.get('_id'))

    yield random_ingredients


@pytest.fixture()
def create_order(get_ingredients):
    # Создать заказ
    payload = {"ingredients": get_ingredients}
    response = requests.post(f'{MAIN_URL}{CREATE_ORDER}', data=payload)
    yield response


@pytest.fixture()
def get_payload():
    payload = {"email": EMAIL, "password": PASSWORD, "name": NAME}
    yield payload

