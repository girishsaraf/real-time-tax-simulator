from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.main import get_db
from app.models.user import User
from sqlalchemy import insert
from app.models.tax_liability import TaxLiability
from sqlalchemy import JSON
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.main import Base

router = APIRouter()

class ScenarioRequest(BaseModel):
    user_id: int
    scenario_json: dict

class ScenarioResponse(BaseModel):
    id: int
    user_id: int
    scenario_json: dict
    result_json: dict

class Scenario(Base):
    __tablename__ = "scenarios"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    scenario_json = Column(MutableDict.as_mutable(JSON))
    result_json = Column(MutableDict.as_mutable(JSON))

@router.post("/tax/scenario", response_model=ScenarioResponse)
def run_scenario(scenario: ScenarioRequest, db: Session = Depends(get_db)):
    # Dummy result for now
    result = {"estimated_tax_impact": 1234.56}
    db_scenario = Scenario(
        user_id=scenario.user_id,
        scenario_json=scenario.scenario_json,
        result_json=result
    )
    db.add(db_scenario)
    db.commit()
    db.refresh(db_scenario)
    return ScenarioResponse(
        id=db_scenario.id,
        user_id=db_scenario.user_id,
        scenario_json=db_scenario.scenario_json,
        result_json=db_scenario.result_json
    ) 