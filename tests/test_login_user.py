import allure
import requests

from data_static import MAIN_URL, PASSWORD, NAME, LOGIN_USER


class TestLoginUser:
    @allure.title('Пройти авторизацию для существующего пользователя')
    def test_login_user_true(self, create_user):
        # Авторизация пользователя
        payload = {"email": create_user.json()['user']['email'], "password": PASSWORD,
                   "name": create_user.json()['user']['name']}
        response = requests.post(f'{MAIN_URL}{LOGIN_USER}', data=payload)

        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Пройти авторизацию с неверным логином и паролем')
    def test_login_user_with_invalid_username_and_password(self, create_user):
        # Авторизация пользователя с неверным именем и паролем
        payload = {"email": create_user.json()['user']['email'], "password": 12345,
                   "name": NAME}
        response = requests.post(f'{MAIN_URL}{LOGIN_USER}', data=payload)

        assert response.status_code == 401 and response.json()['success'] == False and response.json()[
            'message'] == 'email or password are incorrect'
