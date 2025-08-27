from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    class Config:
        from_attributes = True
