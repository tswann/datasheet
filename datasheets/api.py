from fastapi import FastAPI, status
from datasheets.models import Datasheet

app = FastAPI()


@app.get("/")
def root():
    return {"message": "testing"}


@app.get("/datasheets")
def datasheets():
    return []


@app.post("/datasheets", status_code=status.HTTP_201_CREATED)
def create_datasheet(datasheet: Datasheet):
    return datasheet
