from terminals.api import app
from terminals.models import ScaleName, Scale, Terminal
from fastapi.testclient import TestClient
from fastapi import status

client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == {"message": "testing"}


def test_terminals():
    resp = client.get("/terminals")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == []


def test_create_terminal():
    data = Terminal(
        name="test", 
        description="testing", 
        scale=Scale(name=ScaleName.grandis, value=6),
        base_points=180)
    resp = client.post("/terminals", data=data.json())
    assert resp.status_code == status.HTTP_201_CREATED
    assert resp.json() == data
