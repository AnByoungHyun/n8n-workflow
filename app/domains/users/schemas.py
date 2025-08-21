from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    class Config:
        from_attributes = True

from sqlalchemy.orm import Session
from . import models

def get_users(db: Session):
    return db.query(models.User).all()
