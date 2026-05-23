import edge_tts
import tempfile

from config import (
    TTS_VOICE_EN,
    TTS_VOICE_HI,
    TTS_VOICE_TA
)

from utils.latency import (
    LatencyTracker
)


VOICE_MAP = {
    "English": TTS_VOICE_EN,
    "Hindi": TTS_VOICE_HI,
    "Tamil": TTS_VOICE_TA
}


async def generate_tts_audio(
    text: str,
    language: str
):

    tracker = LatencyTracker()

    tracker.start("tts")

    voice = VOICE_MAP.get(
        language,
        TTS_VOICE_EN
    )

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice
    )

    with tempfile.NamedTemporaryFile(
        suffix=".mp3"
    ) as temp_audio:

        await communicate.save(
            temp_audio.name
        )

        temp_audio.seek(0)

        audio_bytes = (
            temp_audio.read()
        )

    tracker.stop("tts")

    return audio_bytes