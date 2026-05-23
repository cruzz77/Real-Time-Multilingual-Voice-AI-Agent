import edge_tts
import uuid

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


async def text_to_speech(
    text: str,
    language: str
):

    tracker = LatencyTracker()

    tracker.start("tts")

    voice = VOICE_MAP.get(
        language,
        TTS_VOICE_EN
    )

    filename = f"audio_{uuid.uuid4()}.mp3"

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice
    )

    await communicate.save(filename)

    tracker.stop("tts")

    return filename, tracker.report()