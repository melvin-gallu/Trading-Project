from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

#to run it, use python -m pytest

def test_read_main():
    response = client.get("/", headers={"X-Token": "fake-secret-token"})
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_item_bad_token():
    response = client.get("/", headers={"X-Token": "hailhydra"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}