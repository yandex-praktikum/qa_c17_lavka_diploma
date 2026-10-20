import os
import uuid

import pytest
from dotenv import load_dotenv

from api.client import ApiClient

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "").rstrip("/")


@pytest.fixture(scope="session")
def api_url():
    return os.getenv("API_URL", "").rstrip("/") or base_url


@pytest.fixture(scope="session")
def product_id():
    return int(os.getenv("PRODUCT_ID", "1"))


@pytest.fixture
def api(api_url):
    return ApiClient(api_url)


@pytest.fixture
def user_data():
    suffix = uuid.uuid4().hex[:8]

    return {
        "firstName": "TestUser",
        "phone": f"+7999{uuid.uuid4().int % 10_000_000:07d}",
        "address": "г. Москва, ул. Пушкина, д. 10",
        "email": f"test_{suffix}@example.com",
        "password": f"Password{suffix}123",
    }


@pytest.fixture
def user(api, user_data):
    response = api.create_user(user_data)

    assert response.status_code == 201, response.text

    body = response.json()

    return {
        "token": body["authToken"],
        "data": user_data,
    }


@pytest.fixture
def browser_context(playwright, base_url, user):
    browser = playwright.chromium.launch()

    context = browser.new_context(
        base_url=base_url,
    )

    context.add_init_script(
        script=f"""
        localStorage.setItem("authToken", "{user["token"]}");
        """
    )

    yield context

    context.close()
    browser.close()