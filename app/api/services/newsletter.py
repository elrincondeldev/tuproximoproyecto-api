from sqlalchemy.orm import Session
from api.models.newsletter import Newsletter
from api.schemas.newsletter import NewsletterBase
from fastapi import HTTPException
from typing import List
from sqlalchemy import func

def introduce_email(db: Session, newsletter: NewsletterBase):
    try:
        db_newsletter = Newsletter(**newsletter.model_dump())
        db.add(db_newsletter)
        db.commit()
        db.refresh(db_newsletter)
        return {"email": db_newsletter.email, "status_code": 200}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al introducir el email en la base de datos")

def get_last_id(db: Session) -> int:
    last_id = db.query(func.max(Newsletter.id)).scalar()
    return last_id