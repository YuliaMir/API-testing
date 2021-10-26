import pytest
import requests

#https://jsonplaceholder.typicode.com/posts/dddd
@pytest.mark.parametrize("symbols", ["dddd", "&%$#", "0"])
def test_search_by_wrong_id(base_url, symbols):
    response = requests.get(
        base_url + f"/posts/{symbols}",
    ).json()
    assert response == {}

#https://jsonplaceholder.typicode.com/posts/11
@pytest.mark.parametrize("id", [1, 5, 10, 11])
def test_search_by_id(base_url, id):
    response = requests.get(
        base_url + f"/posts/{id}",
    ).json()
    assert response['id'] == id

#https://jsonplaceholder.typicode.com/posts?userId=1
@pytest.mark.parametrize("userId", [1, 3, 5])
def test_all_post_from_user(base_url, userId):
    response = requests.get(
    base_url + f"/posts?userId={userId}",
    ).json()
    assert len(response) > 9

#https://jsonplaceholder.typicode.com/posts/5
@pytest.mark.parametrize("num", [5, 7, 9])
def test_delete_posts(base_url, num):
    response = requests.delete(
    base_url + f"/posts/{num}",
    ).json()
    assert response == {}

#https://jsonplaceholder.typicode.com/posts/1
@pytest.mark.parametrize("num", [9, 12, 15])
def test_update(base_url, num):
    response = requests.put(
    base_url + f"/posts/{num}"
    ).json()
    assert response != {}




