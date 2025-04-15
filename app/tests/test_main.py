from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_filter_json_valid():
    test_data = {
        "data": {
            "user": {
                "name": "John",
                "email": "john@example.com",
                "address": {
                    "street": "123 Main St",
                    "city": "Boston"
                }
            }
        },
        "filter": {
            "user": ["name", "email"]
        }
    }
    
    response = client.post("/filter", json=test_data)
    assert response.status_code == 200
    filtered_data = response.json()
    assert "user" in filtered_data
    assert "name" in filtered_data["user"]
    assert "email" in filtered_data["user"]
    assert "address" not in filtered_data["user"]

def test_filter_json_empty_data():
    test_data = {
        "data": {},
        "filter": {}
    }
    
    response = client.post("/filter", json=test_data)
    assert response.status_code == 200
    assert response.json() == {}

def test_filter_json_missing_fields():
    test_data = {
        "data": {}
    }
    
    response = client.post("/filter", json=test_data)
    assert response.status_code == 422

def test_filter_json_invalid_format():
    test_data = {
        "data": "invalid",
        "filter": ["invalid"]
    }
    
    response = client.post("/filter", json=test_data)
    assert response.status_code == 422

def test_filter_json_complex_data():
    test_data = {
        "data": {
            "users": [
                {
                    "id": 1,
                    "name": "John",
                    "details": {
                        "age": 30,
                        "email": "john@example.com"
                    }
                },
                {
                    "id": 2,
                    "name": "Jane",
                    "details": {
                        "age": 25,
                        "email": "jane@example.com"
                    }
                }
            ]
        },
        "filter": {
            "users": ["id", "name"]
        }
    }
    
    response = client.post("/filter", json=test_data)
    assert response.status_code == 200
    filtered_data = response.json()
    assert "users" in filtered_data
    assert len(filtered_data["users"]) == 2
    assert all("details" not in user for user in filtered_data["users"])
    assert all("id" in user and "name" in user for user in filtered_data["users"])