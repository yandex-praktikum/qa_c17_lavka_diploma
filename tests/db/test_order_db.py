import csv
import io

import allure


@allure.title("DB-check: заказ записан в order_model")
def test_order_is_saved_in_db(api, user, product_id):
    # TODO: получите order_model и проверьте созданный заказ
    raise NotImplementedError
