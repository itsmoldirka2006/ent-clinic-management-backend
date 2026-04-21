from fastapi import FastAPI

from app.database import Base, engine
from app.routers import analytics, appointments, doctors, patients, visit_records

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ENT Clinic Appointment and Visit Tracking System")

app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(appointments.router)
app.include_router(visit_records.router)
app.include_router(analytics.router)


@app.get("/")
def root():
    return {"message": "ENT Clinic API is running"}