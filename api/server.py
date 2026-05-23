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

            await websocket.receive_bytes()

            await websocket.send_json({
                "transcript": "Audio received successfully",
                "response": "WebSocket working correctly on Render",
                "audio_base64": ""
            })

    except Exception as e:

        print(e)