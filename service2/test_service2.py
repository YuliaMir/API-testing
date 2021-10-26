import pytest
import requests

#https://api.openbrewerydb.org/breweries/search?query=mountain
@pytest.mark.parametrize("search_word", ["barrel", "mountain", "spring"])
def test_search_brewery_by_word(base_url, search_word):
    response = requests.get(
        base_url + f"/breweries/search?query={search_word}",
    ).json()
    assert response != []

#https://api.openbrewerydb.org/breweries?by_city=san_diego
@pytest.mark.parametrize("city", ["san_diego", "miami", "houston"])
def test_brewery_by_city(base_url, city):
    response = requests.get(
        base_url + f"/breweries?by_city={city}",
    ).json()
    assert response != []

#https://api.openbrewerydb.org/breweries?by_state=florida
@pytest.mark.parametrize("state", ['florida', 'california', 'nevada'])
def test_brewery_by_state(base_url, state):
    response = requests.get(
    base_url + f"/breweries?by_state={state}",
    ).json()
    assert response != []

#https://api.openbrewerydb.org/breweries?per_page=7
@pytest.mark.parametrize("amount", [7, 11])
def test_amount_per_page(base_url, amount):
    response = requests.get(
    base_url + f"/breweries?per_page={amount}",
    ).json()
    assert len(response) == amount

#https://api.openbrewerydb.org/breweries?by_type=micro
@pytest.mark.parametrize("type", ['micro', 'nano', 'brewpub', 'large', 'bar'])
def test_brewery_by_type(base_url, type):
    response = requests.get(
    base_url + f"/breweries?by_type={type}",
    ).json()
    assert len(response) >= 1


