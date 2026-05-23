from agent.chains import generate_response
from agent.tools import (
    book_appointment,
    cancel_appointment
)


async def chatbot_node(state):

    transcript = state["transcript"]

    lower_text = transcript.lower()

    tool_result = None

    if "book" in lower_text:

        tool_result = book_appointment(
            patient_name="Aditya",
            doctor_name="Dr Sharma",
            slot="tomorrow 5pm"
        )

    elif "cancel" in lower_text:

        tool_result = cancel_appointment(
            patient_name="Aditya"
        )

    response = await generate_response(
        f"""
        User said:
        {transcript}

        Tool result:
        {tool_result}
        """
    )

    state["response"] = response

    return state