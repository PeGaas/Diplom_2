import allure
import requests

from data_static import MAIN_URL, EMAIL, PASSWORD, NAME, GET_USER


class TestChangeDataUser:
    @allure.title('Обновить информацию о пользователи с авторизацией')
    def test_change_user_data_with_authorization_true(self, create_user):
        # Обновить информацию о пользователи с авторизацией
        payload = {"email": EMAIL, "password": PASSWORD,
                   "name": NAME}
        response = requests.patch(f'{MAIN_URL}{GET_USER}', data=payload,
                                  headers={'Authorization': create_user.json()['accessToken']})

        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Обновить информацию о пользователи без авторизации')
    def test_change_user_data_without_authorization_false(self, create_user):
        # Обновить информацию о пользователи без авторизации
        payload = {"email": EMAIL, "password": PASSWORD,
                   "name": NAME}
        response = requests.patch(f'{MAIN_URL}{GET_USER}', data=payload)

        assert response.status_code == 401 and response.json()['success'] == False and response.json()[
            'message'] == 'You should be authorised'
