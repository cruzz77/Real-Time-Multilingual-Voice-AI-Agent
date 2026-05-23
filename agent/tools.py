from memory.schemas import (
    SessionLocal,
    Appointment,
    Doctor
)


db = SessionLocal()


def get_doctor_by_specialization(
    specialization: str
):

    doctor = db.query(Doctor).filter(
        Doctor.specialization.ilike(
            f"%{specialization}%"
        )
    ).first()

    return doctor


def check_availability(slot: str):

    existing = db.query(Appointment).filter(
        Appointment.slot == slot,
        Appointment.status == "booked"
    ).first()

    return existing is None


def suggest_alternative_slots():

    return [
        "tomorrow 6pm",
        "day after tomorrow 11am",
        "friday 4pm"
    ]


def book_appointment(
    patient_name: str,
    doctor_name: str,
    slot: str
):

    available = check_availability(slot)

    if not available:

        return {
            "success": False,
            "message": "Requested slot unavailable",
            "alternatives": suggest_alternative_slots()
        }

    appointment = Appointment(
        patient_name=patient_name,
        doctor_name=doctor_name,
        slot=slot,
        status="booked"
    )

    db.add(appointment)

    db.commit()

    return {
        "success": True,
        "message": f"Appointment booked with {doctor_name} at {slot}"
    }


def cancel_appointment(
    patient_name: str
):

    appointment = db.query(Appointment).filter(
        Appointment.patient_name == patient_name,
        Appointment.status == "booked"
    ).first()

    if not appointment:

        return {
            "success": False,
            "message": "No active appointment found"
        }

    appointment.status = "cancelled"

    db.commit()

    return {
        "success": True,
        "message": "Appointment cancelled successfully"
    }