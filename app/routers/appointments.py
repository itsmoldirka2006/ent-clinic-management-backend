from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.post("/", response_model=schemas.AppointmentResponse)
def create_appointment(
    appointment: schemas.AppointmentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_appointment(db, appointment)


@router.get("/", response_model=List[schemas.AppointmentResponse])
def read_appointments(db: Session = Depends(get_db)):
    return crud.get_appointments(db)


@router.patch("/{appointment_id}/status", response_model=schemas.AppointmentResponse)
def update_status(
    appointment_id: int,
    status_data: schemas.AppointmentStatusUpdate,
    db: Session = Depends(get_db)
):
    appointment = crud.update_appointment_status(db, appointment_id, status_data.status)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment