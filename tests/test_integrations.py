import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    """Create test client"""
    from main import app
    return TestClient(app)

def test_integration_status(client):
    """Test integration status endpoint"""
    response = client.get("/api/integrations/status")
    assert response.status_code == 200
    data = response.json()
    assert "integrations" in data
    assert len(data["integrations"]) > 0