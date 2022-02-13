from enum import Enum
from pydantic import BaseModel


class ScaleName(str, Enum):
    grandis = "grandis"
    immensus = "immensus"
    magnificus = "magnificus"


class Scale(BaseModel):
    name: ScaleName
    value: int


class Terminal(BaseModel):
    name: str
    description: str
    scale: Scale
    base_points: int
