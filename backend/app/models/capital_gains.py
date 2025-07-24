from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from app.main import Base
from pydantic import BaseModel
from typing import Optional

class CapitalGains(Base):
    __tablename__ = "transactions"  # Shared with Income
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(String(50))  # e.g., 'income', 'capital_gain'
    amount = Column(Numeric(12,2))
    date = Column(Date)

class CapitalGainsCreate(BaseModel):
    user_id: int
    type: str
    amount: float
    date: str

class CapitalGainsResponse(BaseModel):
    id: int
    user_id: int
    type: str
    amount: float
    date: str
    class Config:
        orm_mode = True 