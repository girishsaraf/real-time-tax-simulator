from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from app.main import Base
from pydantic import BaseModel
from typing import Optional

class TaxLiability(Base):
    __tablename__ = "tax_liabilities"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    quarter = Column(String(10))
    federal_tax = Column(Numeric(12,2))
    state_tax = Column(Numeric(12,2))

class TaxLiabilityResponse(BaseModel):
    id: int
    user_id: int
    quarter: str
    federal_tax: float
    state_tax: float
    class Config:
        orm_mode = True 