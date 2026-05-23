import asyncio
import websockets


async def test():

    uri = "ws://localhost:8000/ws"

    async with websockets.connect(uri) as websocket:

        with open("sample.wav", "rb") as audio_file:

            audio_bytes = audio_file.read()

            await websocket.send(audio_bytes)

            response = await websocket.recv()

            print(response)


asyncio.run(test())