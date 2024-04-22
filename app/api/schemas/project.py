from pydantic import BaseModel

class ProjectBase(BaseModel):
    name: str
    description: str = None
    votes: int
    category: str
    type: bool