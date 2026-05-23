from agent.chains import (
    generate_response
)

from voice.tts import (
    text_to_speech
)


async def send_followup():

    prompt = """
    Generate a polite healthcare follow-up
    asking how the patient feels after
    their recent appointment.
    """

    response = await generate_response(
        prompt=prompt,
        language="English"
    )

    audio_path = await text_to_speech(
        response,
        "English"
    )

    print("\n")
    print("FOLLOWUP CAMPAIGN")
    print("------------------")
    print(response)
    print(audio_path)