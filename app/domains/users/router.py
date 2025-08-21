from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from . import crud, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.UserOut])
def read_users(db: Session = Depends(get_db)):
    """
    모든 사용자 목록을 조회합니다.
    """
    return crud.get_users(db)
