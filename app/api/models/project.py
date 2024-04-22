from sqlalchemy import String, Boolean, Integer, Column, text, TIMESTAMP
from db.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    votes = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    type = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("now()"))