from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.main import get_db
from sqlalchemy import insert

router = APIRouter()

class ScenarioRequest(BaseModel):
    user_id: int
    scenario_json: dict

class ScenarioResponse(BaseModel):
    id: int
    user_id: int
    scenario_json: dict
    result_json: dict

@router.post("/tax/scenario", response_model=ScenarioResponse)
def run_scenario(scenario: ScenarioRequest, db: Session = Depends(get_db)):
    # Dummy result for now
    result = {"estimated_tax_impact": 1234.56}
    # Insert into scenarios table
    sql = """
        INSERT INTO scenarios (user_id, scenario_json, result_json)
        VALUES (:user_id, :scenario_json, :result_json)
        RETURNING id, user_id, scenario_json, result_json
    """
    row = db.execute(sql, {
        "user_id": scenario.user_id,
        "scenario_json": scenario.scenario_json,
        "result_json": result
    }).fetchone()
    db.commit()
    return ScenarioResponse(
        id=row.id,
        user_id=row.user_id,
        scenario_json=row.scenario_json,
        result_json=row.result_json
    ) 