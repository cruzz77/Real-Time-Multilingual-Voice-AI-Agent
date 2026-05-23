from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "llama-3.1-8b-instant"
)

DB_URL = os.getenv(
    "DB_URL",
    "sqlite:///database/patients.db"
)

FAISS_INDEX_PATH = os.getenv(
    "FAISS_INDEX_PATH",
    "memory/faiss_index"
)


REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")


WHISPER_MODEL = os.getenv(
    "WHISPER_MODEL",
    "small"
)

TTS_VOICE_EN = os.getenv("TTS_VOICE_EN")
TTS_VOICE_HI = os.getenv("TTS_VOICE_HI")
TTS_VOICE_TA = os.getenv("TTS_VOICE_TA")


MAX_RESPONSE_LATENCY_MS = int(
    os.getenv(
        "MAX_RESPONSE_LATENCY_MS",
        450
    )
)