from pydantic import BaseModel
from datetime import datetime

class ProjectBase(BaseModel):
    name: str
    description: str = None
    votes: int
    category: str
    type: bool
    created_at: datetime

class ProjectBaseGpt(BaseModel):
    name: str
    description: str
    votes: int
    category: str
    type: bool