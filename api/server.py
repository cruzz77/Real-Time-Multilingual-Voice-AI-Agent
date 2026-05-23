from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import WebSocket

from api.websocket import (
    websocket_endpoint
)

from outbound.campaign import (
    scheduler
)

from outbound.reminders import (
    send_reminders
)

from outbound.followups import (
    send_followup
)


app = FastAPI()

app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend"
)


@app.on_event("startup")
async def startup_event():

    scheduler.add_job(
        send_reminders,
        "interval",
        minutes=2
    )

    scheduler.add_job(
        send_followup,
        "interval",
        minutes=5
    )

    scheduler.start()


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