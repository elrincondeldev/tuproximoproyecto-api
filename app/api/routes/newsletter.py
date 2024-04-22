from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.schemas import newsletter
from api.services import newsletter as newsletter_service
from db.database import get_db

router = APIRouter()

@router.post("/new-email", response_model=newsletter.NewsletterBase)
def new_email(newsletter: newsletter.NewsletterBase, db: Session = Depends(get_db)):
    return newsletter_service.introduce_email(db, newsletter)

@router.get("/get-last-id", response_model=int)
def get_last_id(db: Session = Depends(get_db)):
    return newsletter_service.get_last_id(db)