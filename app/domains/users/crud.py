from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_users(db: Session):
    return db.query(models.User).all()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    # 이메일 중복 체크
    if get_user_by_email(db, user.email):
        raise ValueError("이미 등록된 이메일입니다.")
    
    # 사용자명 중복 체크
    if get_user_by_username(db, user.username):
        raise ValueError("이미 사용 중인 사용자명입니다.")
    
    # 비밀번호 해싱
    hashed_password = pwd_context.hash(user.password)
    
    # 사용자 생성
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
