from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.schemas import proposedProject
from api.services import proposedProject as proposed_project_service
from db.database import get_db
from api.auth import token

router = APIRouter()

@router.post("/propose-project", response_model=proposedProject.ProjectBase)
async def propose_project(project: proposedProject.ProjectBase, db: Session = Depends(get_db), token: dict = Depends(token.authenticate)):
    return proposed_project_service.propose_project(db, project)