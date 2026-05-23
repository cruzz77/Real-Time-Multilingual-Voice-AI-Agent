from agent.chains import (
    extract_intent,
    generate_response
)

from agent.tools import (
    book_appointment,
    cancel_appointment,
    get_doctor_by_specialization
)

from memory.retrieval import (
    retrieve_memories
)

from memory.history import (
    save_conversation_memory
)


async def chatbot_node(state):

    transcript = state["transcript"]

    memories = retrieve_memories(
        transcript
    )

    extracted = await extract_intent(
        transcript
    )

    intent = extracted.get("intent")

    specialization = extracted.get(
        "specialization"
    )

    slot = extracted.get("slot")

    doctor_name = extracted.get(
        "doctor_name"
    )

    tool_result = None

    if specialization and not doctor_name:

        doctor = get_doctor_by_specialization(
            specialization
        )

        if doctor:
            doctor_name = doctor.name

    if intent == "book":

        tool_result = book_appointment(
            patient_name="Aditya",
            doctor_name=doctor_name,
            slot=slot
        )

    elif intent == "cancel":

        tool_result = cancel_appointment(
            patient_name="Aditya"
        )

    response = await generate_response(
        f"""
        User transcript:
        {transcript}

        Retrieved memories:
        {memories}

        Extracted information:
        {extracted}

        Tool result:
        {tool_result}

        Generate a natural conversational response.
        """
    )

    save_conversation_memory(
        patient_name="Aditya",
        transcript=transcript,
        response=response
    )

    state["response"] = response

    state["intent"] = intent

    state["doctor_name"] = doctor_name

    state["specialization"] = specialization

    state["slot"] = slot

    state["tool_result"] = tool_result

    state["retrieved_memories"] = memories

    return state