from sqlalchemy.orm import Session
from app.models.income import Income

def get_total_income(db: Session, user_id: int) -> float:
    total = db.query(Income).filter(Income.user_id == user_id, Income.type == 'income').with_entities(Income.amount).all()
    return float(sum([row.amount for row in total])) if total else 0.0 