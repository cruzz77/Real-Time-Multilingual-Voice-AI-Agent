import json

from fastapi import FastAPI
from fastapi import WebSocket
from fastapi.responses import FileResponse

from voice.stt import (
    transcribe_audio
)

from agent.graph import (
    run_agent
)


app = FastAPI()


@app.get("/")
async def root():

    return FileResponse(
        "frontend/index.html"
    )


@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket
):

    await websocket.accept()

    try:

        while True:

            audio_bytes = (
                await websocket.receive_bytes()
            )

            stt_result = (
                await transcribe_audio(
                    audio_bytes
                )
            )

            transcript = (
                stt_result["transcript"]
            )

            if not transcript:

                continue

            language = (
                stt_result["language"]
            )

            ai_response = (
                await run_agent(
                    transcript,
                    language
                )
            )

            await websocket.send_text(

                json.dumps({

                    "transcript":
                        transcript,

                    "language":
                        language,

                    "response":
                        ai_response
                })
            )

    except Exception as e:

        print(
            "WebSocket Error:",
            e
        )