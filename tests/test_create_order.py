import allure
import requests

from data_static import MAIN_URL, CREATE_ORDER


class TestCreateOrder:
    @allure.title('Создать заказ для авторизованного пользователя')
    def test_create_order_with_authorization_true(self, authorization_user, get_ingredients):
        # Создать заказ
        payload = {"ingredients": get_ingredients}
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER}', data=payload,
                                 headers={'Authorization': authorization_user.json()['accessToken']})

        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Создать заказ для не авторизованного пользователя')
    def test_create_order_without_authorization_true(self, get_ingredients):
        # Создать заказ
        payload = {"ingredients": get_ingredients}
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER}', data=payload)

        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Создать заказ с ингридиентами')
    def test_create_order_with_ingredients_true(self, get_ingredients):
        # Создать заказ
        payload = {"ingredients": get_ingredients}
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER}', data=payload)

        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Создать заказ без ингридиентами')
    def test_create_order_without_ingredients_false(self):
        # Создать заказ
        payload = {"ingredients": ''}
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER}', data=payload)

        assert response.status_code == 400 and response.json()['success'] == False and response.json()[
            'message'] == 'Ingredient ids must be provided'

    @allure.title('Создать заказ с неправильными хэшем ингридиентов')
    def test_create_order_with_invalid_hash_ingredients_false(self, get_ingredients):
        # Создать заказ
        payload = {"ingredients": ['61c0c5a71d1f82001bdaaa6p']}
        response = requests.post(f'{MAIN_URL}{CREATE_ORDER}', data=payload)

        assert response.status_code == 500
