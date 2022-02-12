from datasheets.api import app
from datasheets.models import Datasheet
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "testing"}


def test_datasheets():
    resp = client.get("/datasheets")
    assert resp.status_code == 200
    assert resp.json() == []


def test_create_datasheet():
    data = Datasheet(name="test", description="testing")
    resp = client.post("/datasheets", data=data.json())
    assert resp.status_code == 200
    assert resp.json() == { "data": data.json() }
