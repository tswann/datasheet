from fastapi import FastAPI
from datasheets.models import Datasheet

app = FastAPI()


@app.get("/")
def root():
    return {"message": "testing"}


@app.get("/datasheets")
def datasheets():
    return []


@app.post("/datasheets")
def create_datasheet(datasheet: Datasheet):
    return {"data": datasheet.json()}
