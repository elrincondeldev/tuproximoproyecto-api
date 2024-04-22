from fastapi import APIRouter, Depends
from api.services import gpt as gpt_service
from db.database import get_db
from sqlalchemy.orm import Session
from api.auth import security as verify_token

router = APIRouter()

@router.post("/create-project-gpt", response_model=dict)
async def create_project_gpt_route(db: Session = Depends(get_db), token: dict = Depends(verify_token.verify_token)):
    return await gpt_service.generate_project_idea(db)
