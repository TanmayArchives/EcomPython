from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_create_product():
    response = client.post(
        "/products/",
        json={"name": "Test Product", "description": "Test Description", "price": 99.99}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 99.99

def test_get_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)