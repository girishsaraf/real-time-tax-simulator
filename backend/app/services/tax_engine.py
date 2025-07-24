def calculate_tax(income: float, state: str = None) -> dict:
    # Dummy progressive tax: 10% up to 10k, 20% up to 50k, 30% above
    if income <= 10000:
        federal = income * 0.10
    elif income <= 50000:
        federal = 1000 + (income - 10000) * 0.20
    else:
        federal = 9000 + (income - 50000) * 0.30
    # Dummy state tax: 5%
    state_tax = income * 0.05 if state else 0
    return {"federal": round(federal, 2), "state": round(state_tax, 2)} 