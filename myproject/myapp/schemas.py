from pydantic import BaseModel
from datetime import datetime


class AddAnimal(BaseModel):
    name: str
    description: str


class ReadAnimal(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
