from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.tax_liability import TaxLiability, TaxLiabilityResponse
from app.main import get_db

router = APIRouter()

@router.get("/tax/current", response_model=TaxLiabilityResponse)
def get_current_tax(user_id: int = 1, db: Session = Depends(get_db)):
    # In production, get user_id from auth
    tax = db.query(TaxLiability).filter(TaxLiability.user_id == user_id).order_by(TaxLiability.id.desc()).first()
    if not tax:
        raise HTTPException(status_code=404, detail="No tax liability found for user")
    return tax 