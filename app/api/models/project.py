from sqlalchemy import String, Boolean, Integer, Column, DATE
from db.database import Base
from datetime import datetime

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    votes = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    type = Column(Boolean, nullable=False)
    created_at = Column(DATE, nullable=False, default=datetime.now().date)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "votes": self.votes,
            "category": self.category,
            "type": self.type,
            "created_at": self.created_at.isoformat()
        }
