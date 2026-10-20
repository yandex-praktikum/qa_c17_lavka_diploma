from playwright.sync_api import Page

from ui import locators


class CatalogPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("/")
        self.page.wait_for_load_state("networkidle")

    def open_drinks(self):
        self.page.locator(locators.CATEGORY).click()
        self.page.wait_for_load_state("networkidle")

    def open_product(self):
        self.page.locator(locators.PRODUCT).click()
        self.page.wait_for_load_state("networkidle")

    def add_product_to_cart(self):
        self.page.locator(locators.ADD_TO_CART).click()


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.locator(locators.CART).click()
        self.page.wait_for_load_state("networkidle")

    def checkout(self):
        self.page.locator(locators.CHECKOUT).click()
        self.page.wait_for_load_state("networkidle")


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def is_open(self):
        return self.page.locator(
            locators.CHECKOUT_PAGE_TITLE
        ).filter(
            has_text="Оформление заказа"
        ).is_visible()