#models.py
from pydantic import BaseModel
from datetime import datetime
DateTime = datetime
from typing import List, Optional


class Recipe(BaseModel):
    id: int
    name: str
    description: str
    instructions: str
    ingredients: List[str]
    image64: str

class image64(BaseModel):
    image64: str