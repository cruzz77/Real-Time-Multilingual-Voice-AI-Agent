from fastapi import WebSocket
import base64

from voice.stt import (
    transcribe_audio
)

from voice.tts import (
    text_to_speech
)

from agent.graph import graph


class ConnectionManager:

    def __init__(self):
        self.active_connections = []

    async def connect(
        self,
        websocket: WebSocket
    ):

        await websocket.accept()

        self.active_connections.append(
            websocket
        )

    def disconnect(
        self,
        websocket: WebSocket
    ):

        if websocket in self.active_connections:

            self.active_connections.remove(
                websocket
            )


manager = ConnectionManager()


async def websocket_endpoint(
    websocket: WebSocket
):

    await manager.connect(websocket)

    try:

        while True:

            audio_bytes = await websocket.receive_bytes()

            stt_result = await transcribe_audio(
                audio_bytes
            )

            transcript = stt_result[
                "transcript"
            ]

            language = stt_result[
                "language"
            ]

            result = await graph.ainvoke({
                "transcript": transcript,
                "response": "",
                "language": language,
                "messages": [],
                "intent": None,
                "patient_name": "Aditya",
                "doctor_name": None,
                "specialization": None,
                "slot": None,
                "tool_result": None,
                "retrieved_memories": []
            })

            response_text = result[
                "response"
            ]

            audio_path = await text_to_speech(
                response_text,
                language
            )

            with open(audio_path, "rb") as audio_file:

                encoded_audio = base64.b64encode(
                    audio_file.read()
                ).decode("utf-8")

            await websocket.send_json({
                "transcript": transcript,
                "language": language,
                "response": response_text,
                "audio_base64": encoded_audio
            })

    except Exception as e:

        print(e)

        manager.disconnect(
            websocket
        )