from fastapi import FastAPI, status
from datasheets.models import Terminal

app = FastAPI()


@app.get("/")
def root():
    return {"message": "testing"}


@app.get("/terminals")
def terminals():
    return []


@app.post("/terminals", status_code=status.HTTP_201_CREATED)
def create_terminal(terminal: Terminal):
    return terminal
