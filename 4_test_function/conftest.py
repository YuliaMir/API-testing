import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
    )


    parser.addoption(
        "--code",
        default="200",
        choices=["200", "300", "400", "404", "500", "502"],
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_method(request):
    return requests.get

@pytest.fixture
def basic_code(request):
    return request.config.getoption("--code")