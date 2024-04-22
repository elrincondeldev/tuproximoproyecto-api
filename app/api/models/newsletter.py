from sqlalchemy import String, Boolean, Integer, Column, text, TIMESTAMP
from db.database import Base

class Newsletter(Base):
    __tablename__ = "newsletters"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("now()"))