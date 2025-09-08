from fastapi import APIRouter, Depends, HTTPException, status
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

@router.post("/", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    새로운 사용자를 등록합니다.
    """
    try:
        return crud.create_user(db=db, user=user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
