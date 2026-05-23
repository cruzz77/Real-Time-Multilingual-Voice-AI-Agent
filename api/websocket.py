from fastapi import WebSocket

import base64
import tempfile
import os
import uuid

from voice.stt import (
    transcribe_audio
)

from voice.tts import (
    text_to_speech
)

from voice.buffer import (
    audio_buffers
)

from agent.session import (
    active_requests
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

    connection_id = str(uuid.uuid4())

    audio_buffers[
        connection_id
    ] = bytearray()

    active_requests[
        connection_id
    ] = 0

    try:

        while True:

            audio_chunk = (
                await websocket.receive_bytes()
            )

            active_requests[
                connection_id
            ] += 1

            current_request = (
                active_requests[
                    connection_id
                ]
            )

            audio_buffers[
                connection_id
            ].extend(audio_chunk)

            if len(
                audio_buffers[
                    connection_id
                ]
            ) < 50000:

                continue

            with tempfile.NamedTemporaryFile(
                suffix=".webm",
                delete=False
            ) as temp_audio:

                temp_audio.write(
                    audio_buffers[
                        connection_id
                    ]
                )

                temp_audio.flush()

                with open(
                    temp_audio.name,
                    "rb"
                ) as audio_file:

                    stt_result = (
                        await transcribe_audio(
                            audio_file.read()
                        )
                    )

            transcript = stt_result[
                "transcript"
            ]

            language = stt_result[
                "language"
            ]

            await websocket.send_json({
                "transcript": transcript
            })

            if len(
                transcript.strip()
            ) < 15:

                continue

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

            if current_request != active_requests[
                connection_id
            ]:
                continue

            response_text = result[
                "response"
            ]

            audio_path = await text_to_speech(
                response_text,
                language
            )

            if current_request != active_requests[
                connection_id
            ]:
                continue

            with open(
                audio_path,
                "rb"
            ) as audio_file:

                encoded_audio = (
                    base64.b64encode(
                        audio_file.read()
                    ).decode("utf-8")
                )

            await websocket.send_json({
                "transcript": transcript,
                "language": language,
                "response": response_text,
                "audio_base64": encoded_audio
            })

            audio_buffers[
                connection_id
            ] = bytearray()

            os.remove(
                temp_audio.name
            )

    except Exception as e:

        print(e)

        manager.disconnect(
            websocket
        )

        if connection_id in audio_buffers:

            del audio_buffers[
                connection_id
            ]

        if connection_id in active_requests:

            del active_requests[
                connection_id
            ]