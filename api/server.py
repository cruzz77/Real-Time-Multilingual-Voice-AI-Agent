from fastapi import FastAPI, WebSocket
from api.websocket import websocket_endpoint

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Voice AI Agent Running"
    }


@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)