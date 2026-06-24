import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    """Create test client"""
    from main import app
    return TestClient(app)

def test_health_status(client):
    """Test health status endpoint"""
    response = client.get("/api/health/status")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_ping(client):
    """Test ping endpoint"""
    response = client.get("/api/health/ping")
    assert response.status_code == 200
    assert response.json()["message"] == "pong"