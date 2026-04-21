from sqlalchemy.orm import Session
from sqlalchemy import func

from app import models, schemas


def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def get_patients(db: Session):
    return db.query(models.Patient).all()


def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()


def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(**doctor.model_dump())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def get_doctors(db: Session):
    return db.query(models.Doctor).all()


def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()


def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    db_appointment = models.Appointment(**appointment.model_dump())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def get_appointments(db: Session):
    return db.query(models.Appointment).all()


def get_appointment(db: Session, appointment_id: int):
    return db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()


def update_appointment_status(db: Session, appointment_id: int, status: str):
    appointment = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if not appointment:
        return None
    appointment.status = status
    db.commit()
    db.refresh(appointment)
    return appointment


def create_visit_record(db: Session, visit_record: schemas.VisitRecordCreate):
    db_record = models.VisitRecord(**visit_record.model_dump())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


def get_visit_records(db: Session):
    return db.query(models.VisitRecord).all()


def get_patient_visit_records(db: Session, patient_id: int):
    return (
        db.query(models.VisitRecord)
        .filter(models.VisitRecord.patient_id == patient_id)
        .all()
    )


def get_clinic_stats(db: Session):
    total_patients = db.query(func.count(models.Patient.id)).scalar() or 0
    total_doctors = db.query(func.count(models.Doctor.id)).scalar() or 0
    total_appointments = db.query(func.count(models.Appointment.id)).scalar() or 0
    total_visit_records = db.query(func.count(models.VisitRecord.id)).scalar() or 0

    scheduled_appointments = (
        db.query(func.count(models.Appointment.id))
        .filter(models.Appointment.status == "scheduled")
        .scalar()
        or 0
    )

    completed_appointments = (
        db.query(func.count(models.Appointment.id))
        .filter(models.Appointment.status == "completed")
        .scalar()
        or 0
    )

    cancelled_appointments = (
        db.query(func.count(models.Appointment.id))
        .filter(models.Appointment.status == "cancelled")
        .scalar()
        or 0
    )

    return {
        "total_patients": total_patients,
        "total_doctors": total_doctors,
        "total_appointments": total_appointments,
        "scheduled_appointments": scheduled_appointments,
        "completed_appointments": completed_appointments,
        "cancelled_appointments": cancelled_appointments,
        "total_visit_records": total_visit_records,
    }