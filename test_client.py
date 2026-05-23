import asyncio
import websockets
import json
import base64


async def test():

    uri = "ws://localhost:8000/ws"

    async with websockets.connect(uri) as websocket:

        with open("sample.wav", "rb") as audio_file:

            audio_bytes = audio_file.read()

            await websocket.send(audio_bytes)

            response = await websocket.recv()

            data = json.loads(response)

            print(data["transcript"])

            print(data["language"])

            print(data["response"])

            audio_data = base64.b64decode(
                data["audio_base64"]
            )

            with open(
                "response.mp3",
                "wb"
            ) as output_audio:

                output_audio.write(
                    audio_data
                )

            print(
                "Audio response saved as response.mp3"
            )


asyncio.run(test())