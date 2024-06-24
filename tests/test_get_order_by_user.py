import allure
import requests

from data_static import MAIN_URL, CREATE_ORDER, GET_ORDERS


class TestGetOrderByUser:
    @allure.title('Получить заказы авторизованного пользователя')
    def test_get_order_by_authorization_user_true(self, authorization_user, get_ingredients):
        # Создать заказ
        payload = {"ingredients": get_ingredients}
        requests.post(f'{MAIN_URL}{CREATE_ORDER}', data=payload,
                      headers={'Authorization': authorization_user.json()['accessToken']})

        # Получить заказы авторизованного пользователя
        response = requests.get(f'{MAIN_URL}{GET_ORDERS}',
                                headers={'Authorization': authorization_user.json()['accessToken']})

        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Получить заказы не авторизованного пользователя')
    def test_get_order_without_authorization_user_false(self, get_ingredients):
        # Создать заказ
        payload = {"ingredients": get_ingredients}
        requests.post(f'{MAIN_URL}{CREATE_ORDER}', data=payload)

        # Получить заказы авторизованного пользователя
        response = requests.get(f'{MAIN_URL}{GET_ORDERS}')

        assert response.status_code == 401 and response.json()['success'] == False and response.json()[
            'message'] == 'You should be authorised'
