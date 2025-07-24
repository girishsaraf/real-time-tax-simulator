from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

from app.api.v1 import users, tax_calculations, scenarios, harvesting

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/taxsimulator")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI(title="Real-Time Tax Simulator API", version="1.0")

# CORS (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(users.router, prefix="/api/v1", tags=["users"])
app.include_router(tax_calculations.router, prefix="/api/v1", tags=["tax"])
app.include_router(scenarios.router, prefix="/api/v1", tags=["scenarios"])
app.include_router(harvesting.router, prefix="/api/v1", tags=["harvesting"])

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 