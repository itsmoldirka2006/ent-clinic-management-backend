from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class PatientBase(BaseModel):
    full_name: str
    birth_date: date
    phone_number: str
    gender: str


class PatientCreate(PatientBase):
    pass


class PatientResponse(PatientBase):
    id: int

    class Config:
        from_attributes = True


class DoctorBase(BaseModel):
    full_name: str
    specialization: str
    phone_number: str


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: datetime
    status: str = "scheduled"


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentStatusUpdate(BaseModel):
    status: str


class AppointmentResponse(AppointmentBase):
    id: int

    class Config:
        from_attributes = True


class VisitRecordBase(BaseModel):
    patient_id: int
    doctor_id: int
    diagnosis: str
    treatment: str
    notes: Optional[str] = None


class VisitRecordCreate(VisitRecordBase):
    pass


class VisitRecordResponse(VisitRecordBase):
    id: int

    class Config:
        from_attributes = True


class ClinicStatsResponse(BaseModel):
    total_patients: int
    total_doctors: int
    total_appointments: int
    scheduled_appointments: int
    completed_appointments: int
    cancelled_appointments: int
    total_visit_records: int