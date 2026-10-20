import allure

from ui.pages import CatalogPage, CartPage, CheckoutPage


@allure.title("UI: добавить товар в корзину")
def test_add_product_to_cart(browser_context):
    page = browser_context.new_page()

    catalog = CatalogPage(page)

    # TODO: реализуйте сценарий:
    # 1. открыть каталог
    # 2. открыть категорию с товаром
    # 3. открыть страницу товара
    # 4. добавить товар в корзину

    raise NotImplementedError


@allure.title("UI: перейти к оформлению заказа")
def test_checkout(browser_context):
    page = browser_context.new_page()

    catalog = CatalogPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # TODO: реализуйте сценарий:
    # 1. открыть каталог
    # 2. открыть категорию с товаром
    # 3. открыть страницу товара
    # 4. добавить товар в корзину
    # 5. открыть корзину
    # 6. перейти к оформлению заказа

    # TODO: добавьте проверку, что открылась страница оформления заказа

    raise NotImplementedError