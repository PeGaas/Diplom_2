import allure
import pytest
import requests

from data_static import MAIN_URL, CREATE_UNIQUE_USER, EMAIL, PASSWORD, NAME, DELETE_USER


class TestCreateUser:
    @allure.title('Создать нового уникального пользователя')
    def test_create_unique_user_true(self, get_payload):
        # Создать нового пользователя
        response = requests.post(f'{MAIN_URL}{CREATE_UNIQUE_USER}', data=get_payload)

        assert response.status_code == 200 and response.json()['success'] == True

        # Удалить пользователя
        requests.delete(f'{MAIN_URL}{DELETE_USER}', headers={'Authorization': response.json()['accessToken']})

    @allure.title('Создать пользователя, который уже существует')
    def test_create_user_is_already_registered(self, get_payload):
        # Создать нового пользователя
        response_create_user = requests.post(f'{MAIN_URL}{CREATE_UNIQUE_USER}', data=get_payload)

        # Создать пользователя, который уже существует
        payload = {"email": response_create_user.json()['user']['email'], "password": PASSWORD,
                   "name": response_create_user.json()['user']['name']}
        response = requests.post(f'{MAIN_URL}{CREATE_UNIQUE_USER}', data=payload)

        assert response.status_code == 403 and response.json()['success'] == False and response.json()[
            'message'] == 'User already exists'

        # Удалить пользователя
        requests.delete(f'{MAIN_URL}{DELETE_USER}',
                        headers={'Authorization': response_create_user.json()['accessToken']})

    @allure.title('Создать пользователя и не заполнить одно из обязательных полей')
    @pytest.mark.parametrize('email, password, name',
                             [['', PASSWORD, NAME], [EMAIL, '', NAME], [EMAIL, PASSWORD, '']])
    def test_create_user_and_not_fill_in_one_required_fields(self, email, password, name):
        # Создать нового пользователя
        payload = {"email": email, "password": password, "name": name}
        response = requests.post(f'{MAIN_URL}{CREATE_UNIQUE_USER}', data=payload)
        print(response.json())

        assert response.status_code == 403 and response.json()['success'] == False and response.json()[
            'message'] == 'Email, password and name are required fields'
