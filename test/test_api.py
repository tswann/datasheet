from terminals.api import app
from terminals.models import Terminal
from fastapi.testclient import TestClient
from fastapi import status

client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == {"message": "testing"}


def test_datasheets():
    resp = client.get("/terminals")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == []


def test_create_datasheet():
    data = Terminal(name="test", description="testing", scale=10)
    resp = client.post("/terminals", data=data.json())
    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.json() == data
