from pydantic import BaseModel

class NewsletterBase(BaseModel):
    email: str