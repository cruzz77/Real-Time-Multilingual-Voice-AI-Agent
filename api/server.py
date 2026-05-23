import base64

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import WebSocket


app = FastAPI()

app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend"
)


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

            from voice.stt import (
                transcribe_audio
            )

            from agent.graph import (
                run_agent
            )

            from voice.tts import (
                generate_tts_audio
            )

            stt_result = (
                await transcribe_audio(
                    audio_bytes
                )
            )

            transcript = (
                stt_result["transcript"]
            )

            language = (
                stt_result["language"]
            )

            ai_response = (
                await run_agent(
                    transcript,
                    language
                )
            )

            audio_response = (
                await generate_tts_audio(
                    ai_response,
                    language
                )
            )

            audio_base64 = (
                base64.b64encode(
                    audio_response
                ).decode("utf-8")
            )

            await websocket.send_json({

                "transcript":
                    transcript,

                "language":
                    language,

                "response":
                    ai_response,

                "audio_base64":
                    audio_base64
            })

    except Exception as e:

        print(
            "WebSocket Error:",
            e
        )