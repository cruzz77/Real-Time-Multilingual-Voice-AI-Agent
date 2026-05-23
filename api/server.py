from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import WebSocket

from api.websocket import (
    websocket_endpoint
)


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
async def websocket_route(
    websocket: WebSocket
):

    await websocket_endpoint(
        websocket
    )