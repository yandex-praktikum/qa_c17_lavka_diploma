import allure

from api.models import OrderResponse, UserResponse


@allure.title("API: создание пользователя")
def test_create_user(api, user_data):
    # TODO: отправьте запрос на создание пользователя
    # TODO: проверьте HTTP-статус ответа
    # TODO: проверьте, что в ответе есть authToken

    raise NotImplementedError


@allure.title("API: создание корзины с товаром")
def test_create_order(api, user, product_id):
    # TODO: создайте корзину с одним товаром
    # TODO: передайте токен авторизованного пользователя
    # TODO: проверьте HTTP-статус ответа
    # TODO: проверьте id созданной корзины
    # TODO: проверьте список товаров
    # TODO: проверьте начальный статус корзины

    raise NotImplementedError


@allure.title("API: добавление товара в корзину")
def test_add_products_and_get_cart(api, user, product_id):
    # TODO: сначала создайте корзину
    # TODO: получите id созданной корзины
    # TODO: добавьте товар в корзину
    # TODO: проверьте HTTP-статус ответа
    # TODO: получите содержимое корзины
    # TODO: проверьте HTTP-статус ответа
    # TODO: проверьте, что товар присутствует в корзине
    # TODO: проверьте количество товара

    raise NotImplementedError


@allure.title("API: оформление заказа и получение заказов пользователя")
def test_complete_order(api, user, product_id):
    # TODO: создайте корзину с товаром
    # TODO: получите id созданной корзины
    # TODO: оформите заказ
    # TODO: проверьте HTTP-статус ответа
    # TODO: проверьте значение ok в ответе
    # TODO: получите список заказов пользователя
    # TODO: проверьте HTTP-статус ответа
    # TODO: найдите созданный заказ в списке
    # TODO: проверьте данные найденного заказа с помощью OrderResponse
    # TODO: проверьте id заказа
    # TODO: проверьте его статус

    raise NotImplementedError