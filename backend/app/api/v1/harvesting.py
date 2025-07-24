from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class HarvestingRecommendation(BaseModel):
    ticker: str
    loss_amount: float
    recommendation: str

@router.get("/tax/harvesting", response_model=List[HarvestingRecommendation])
def get_harvesting():
    # Dummy data
    return [
        HarvestingRecommendation(ticker="AAPL", loss_amount=500.0, recommendation="Sell to realize loss"),
        HarvestingRecommendation(ticker="TSLA", loss_amount=300.0, recommendation="Sell to realize loss")
    ] 