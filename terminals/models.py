from pydantic import BaseModel


class Terminal(BaseModel):
    name: str
    description: str
    scale: int
