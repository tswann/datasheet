from pydantic import BaseModel


class Datasheet(BaseModel):
    name: str
    description: str
