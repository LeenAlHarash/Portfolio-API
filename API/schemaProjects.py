from typing import List
from pydantic import BaseModel

class Project(BaseModel):
    id: int
    name: str
    category: str
    tech: List[str]
    description: str
