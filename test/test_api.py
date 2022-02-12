
from src.api import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == { "message":"testing"}

def test_datasheets():
    resp = client.get("/datasheets")
    assert resp.status_code == 200
    assert resp.json() == []
