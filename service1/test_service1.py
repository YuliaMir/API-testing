import pytest
import requests

@pytest.mark.parametrize("count", [5, 7])
def test_api_count(base_url, count):
    response = requests.get(
    base_url + f"/breeds/image/random/{count}",
    ).json()
    assert len(response['message']) == count

@pytest.mark.parametrize("breed", ["Borzoi", "Eskimo", "Husky"])
def test_api_breed_presence(base_url, breed):
    response = requests.get(
        base_url + "/breed/" +
        f"{breed}/images/random",
    ).json()
    assert len(response['message']) > 0

@pytest.mark.parametrize("breed_identifier", ["xxxx", "1111", "!@*&"])
def test_api_breed_unknown(base_url, breed_identifier):
    response = requests.get(
        base_url + f"/breed/{breed_identifier}/list",
        ).json()
    assert response['code'] == 404

#https://dog.ceo/api/breeds/list/all
def test_list_all_breeds(base_url):
    response = requests.get(
        base_url + "/breeds/list/all",
        ).json()
    assert len(response) > 1

#https://dog.ceo/api/breed/greyhound/afghan/images
def test_wrong_breed_subbreed(base_url):
    response = requests.get(
        base_url + "/breed/greyhound/afghan/images",
    ).json()
    assert response['status'] == 'error'




