from fastapi import WebSocket
from voice.stt import transcribe_audio


class ConnectionManager:

    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):

        if websocket in self.active_connections:
            self.active_connections.remove(websocket)


manager = ConnectionManager()


async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:

        while True:

            audio_bytes = await websocket.receive_bytes()

            transcript = await transcribe_audio(
                audio_bytes
            )

            await websocket.send_json({
                "transcript": transcript
            })

    except Exception as e:

        print(e)

        manager.disconnect(websocket)