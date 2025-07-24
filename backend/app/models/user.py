from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.main import Base
from pydantic import BaseModel, EmailStr
from typing import Optional

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    state = Column(String(2))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# Pydantic schemas
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    state: Optional[str]

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    state: Optional[str]
    created_at: Optional[str]

    class Config:
        orm_mode = True 