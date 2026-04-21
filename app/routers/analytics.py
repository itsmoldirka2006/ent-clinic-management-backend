from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/stats", response_model=schemas.ClinicStatsResponse)
def read_clinic_stats(db: Session = Depends(get_db)):
    return crud.get_clinic_stats(db)