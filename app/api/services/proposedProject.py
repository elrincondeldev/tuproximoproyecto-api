from sqlalchemy.orm import Session
from api.models.proposedProject import Project
from api.schemas.proposedProject import ProjectBase
from typing import List

def propose_project(db: Session, project: ProjectBase):
    db_project = Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project