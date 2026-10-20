import requests


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def request(self, method, path, **kwargs):
        return self.session.request(
            method,
            f"{self.base_url}{path}",
            timeout=20,
            **kwargs,
        )

    def create_user(self, data):
        # TODO: реализуйте POST /api/v1/users
        raise NotImplementedError

    def create_order(self, products, delivery_time=None, token=None):
        # TODO: реализуйте POST /api/v1/orders
        raise NotImplementedError

    # TODO: реализовать остальные методы клиента
    def _not_implemented(self):
        body = {"productsList": products}
        if delivery_time is not None:
            body["deliveryTime"] = delivery_time
        return self.request(
            "POST",
            "/api/v1/orders",
            json=body,
            headers=self.auth_headers(token),
        )

    def add_products(self, order_id, products, token):
        return self.request(
            "PUT",
            f"/api/v1/orders/{order_id}",
            json={"productsList": products},
            headers=self.auth_headers(token),
        )

    def get_cart(self, order_id, token):
        return self.request(
            "GET",
            f"/api/v1/orders/{order_id}",
            headers=self.auth_headers(token),
        )

    def complete_order(self, order_id, token):
        return self.request(
            "PUT",
            f"/api/v1/orders/{order_id}/complete",
            headers=self.auth_headers(token),
        )

    def get_user_orders(self, token):
        return self.request(
            "GET",
            "/api/v1/orders",
            headers=self.auth_headers(token),
        )

    def get_db_table(self, table_name):
        return self.request(
            "GET",
            f"/api/db/resources/{table_name}.csv",
        )

    @staticmethod
    def auth_headers(token):
        return {"Authorization": f"Bearer {token}"} if token else {}
