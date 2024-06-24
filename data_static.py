from data_generator import generate_email, generate_password, generate_first_name

MAIN_URL = 'https://stellarburgers.nomoreparties.site'
CREATE_UNIQUE_USER = '/api/auth/register'
DELETE_USER = '/api/auth/user'
GET_USER = '/api/auth/user'
LOGIN_USER = '/api/auth/login'
CREATE_ORDER = '/api/orders'
GET_INGREDIENTS = '/api/ingredients'
GET_ORDERS = '/api/orders'

EMAIL = generate_email()
PASSWORD = generate_password()
NAME = generate_first_name()
