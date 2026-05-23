import tempfile

from faster_whisper import WhisperModel

from config import (
    WHISPER_MODEL
)


model = None


def get_model():

    global model

    if model is None:

        model = WhisperModel(
            WHISPER_MODEL,
            device="cpu",
            compute_type="int8"
        )

    return model


async def transcribe_audio(
    audio_bytes: bytes
):

    whisper_model = get_model()

    with tempfile.NamedTemporaryFile(
        suffix=".webm"
    ) as temp_audio:

        temp_audio.write(
            audio_bytes
        )

        temp_audio.flush()

        segments, info = (
            whisper_model.transcribe(
                temp_audio.name,
                beam_size=1
            )
        )

        transcript = " ".join([
            segment.text
            for segment in segments
        ])

    return {

        "transcript":
            transcript.strip(),

        "language":
            info.language
    }