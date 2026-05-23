from fastapi import WebSocket

from voice.stt import (
    transcribe_audio
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

            await websocket.send_json({
                "transcript": transcript,
                "language": language,
                "response": result["response"]
            })

    except Exception as e:

        print(e)

        manager.disconnect(
            websocket
        )