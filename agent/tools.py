from memory.schemas import (
    SessionLocal,
    Appointment
)


db = SessionLocal()


def check_availability(slot: str):

    existing = db.query(Appointment).filter(
        Appointment.slot == slot,
        Appointment.status == "booked"
    ).first()

    if existing:
        return False

    return True


def book_appointment(
    patient_name: str,
    doctor_name: str,
    slot: str
):

    available = check_availability(slot)

    if not available:

        return {
            "success": False,
            "message": "Slot already booked"
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
            "message": "No appointment found"
        }

    appointment.status = "cancelled"

    db.commit()

    return {
        "success": True,
        "message": "Appointment cancelled"
    }