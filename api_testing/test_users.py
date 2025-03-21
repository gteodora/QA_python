import requests
import pytest

BASE_URL =  "https://jsonplaceholder.typicode.com"

def test_get_users_status_code():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200


@pytest.fixture
def setup_api():
    return "https://jsonplaceholder.typicode.com"

def test_get_users_not_empty(setup_api):
    url = setup_api 
    response = requests.get(f"{url}/users")
    assert len(response.json()) > 0

def test_get_users_structure(setup_api):
    url = setup_api
    response = requests.get(f"{url}/users")
    users = response.json()
    for user in users:
        assert "id" in user
        assert "name" in user
        assert "username" in user
        assert "email" in user
        assert "address" in user
        assert "phone" in user
        assert "website" in user



