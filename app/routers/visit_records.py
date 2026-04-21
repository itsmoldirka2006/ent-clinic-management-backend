from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/visit-records", tags=["Visit Records"])


@router.post("/", response_model=schemas.VisitRecordResponse)
def create_visit_record(
    visit_record: schemas.VisitRecordCreate,
    db: Session = Depends(get_db)
):
    return crud.create_visit_record(db, visit_record)


@router.get("/", response_model=List[schemas.VisitRecordResponse])
def read_visit_records(db: Session = Depends(get_db)):
    return crud.get_visit_records(db)


@router.get("/patient/{patient_id}", response_model=List[schemas.VisitRecordResponse])
def read_patient_visit_records(patient_id: int, db: Session = Depends(get_db)):
    return crud.get_patient_visit_records(db, patient_id)