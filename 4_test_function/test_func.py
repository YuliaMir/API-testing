import pytest


def test_url_status(base_url, basic_code, request_method):
    target = base_url + f"/status/{basic_code}"
    response = request_method(url=target)
    print(response)
    assert response.status_code == int(basic_code)

