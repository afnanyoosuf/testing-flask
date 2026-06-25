from app import app
import pytest

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client


def test_valid_adult(client):
    response = client.post("/predict", json={"age": 22})
    assert response.status_code == 200
    assert response.json["prediction"] == "adult"


def test_valid_child(client):
    response = client.post("/predict", json={"age": 5})
    assert response.status_code == 200
    assert response.json["prediction"] == "child"


def test_missing_age(client):
    response = client.post("/predict", json={})
    assert response.status_code == 400
    assert response.json["error"] == "Age is required"


def test_invalid_type(client):
    response = client.post("/predict", json={"age": "aabc"})
    assert response.status_code == 400
    assert response.json["error"] == "Age must be a number"


def test_invalid_range(client):
    response = client.post("/predict", json={"age": -5})
    assert response.status_code == 400
    assert response.json["error"] == "Age must be between 0 and 100"


def test_no_json_data(client):
    response = client.post("/predict")
    assert response.status_code == 400
    assert response.json["error"] == "No JSON data provided"