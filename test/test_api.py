from datasheets.api import app
from datasheets.models import Datasheet
from fastapi.testclient import TestClient
from fastapi import status

client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == {"message": "testing"}


def test_datasheets():
    resp = client.get("/datasheets")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == []


def test_create_datasheet():
    data = Datasheet(name="test", description="testing")
    resp = client.post("/datasheets", data=data.json())
    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.json() == data
