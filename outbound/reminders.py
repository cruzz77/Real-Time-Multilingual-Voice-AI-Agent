from memory.schemas import (
    SessionLocal,
    Appointment
)

from voice.tts import (
    text_to_speech
)

from agent.chains import (
    generate_response
)


db = SessionLocal()


async def send_reminders():

    appointments = db.query(
        Appointment
    ).filter(
        Appointment.status == "booked"
    ).all()

    for appointment in appointments:

        reminder_prompt = f"""
        Generate a friendly appointment reminder.

        Patient:
        {appointment.patient_name}

        Doctor:
        {appointment.doctor_name}

        Slot:
        {appointment.slot}
        """

        response = await generate_response(
            prompt=reminder_prompt,
            language="English"
        )

        audio_path = await text_to_speech(
            response,
            "English"
        )

        print("\n")
        print("OUTBOUND REMINDER")
        print("------------------")
        print(response)
        print(audio_path)