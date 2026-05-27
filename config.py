import os

from dotenv import load_dotenv


load_dotenv()


GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)

MODEL_NAME = os.getenv(
    "MODEL_NAME"
)

WHISPER_MODEL = os.getenv(
    "WHISPER_MODEL"
)

TTS_VOICE_EN = os.getenv(
    "TTS_VOICE_EN"
)

TTS_VOICE_HI = os.getenv(
    "TTS_VOICE_HI"
)

TTS_VOICE_TA = os.getenv(
    "TTS_VOICE_TA"
)