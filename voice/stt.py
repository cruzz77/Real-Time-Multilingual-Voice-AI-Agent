import tempfile

from faster_whisper import WhisperModel

from config import (
    WHISPER_MODEL
)

from voice.language import (
    normalize_language
)

from utils.latency import (
    LatencyTracker
)


model = WhisperModel(
    WHISPER_MODEL,
    device="cpu",
    compute_type="int8"
)


async def transcribe_audio(
    audio_bytes: bytes
):

    tracker = LatencyTracker()

    tracker.start("stt")

    with tempfile.NamedTemporaryFile(
        suffix=".wav"
    ) as temp_audio:

        temp_audio.write(audio_bytes)

        temp_audio.flush()

        segments, info = model.transcribe(
            temp_audio.name,
            beam_size=1
        )

        transcript = " ".join([
            segment.text
            for segment in segments
        ])

        detected_language = normalize_language(
            info.language
        )

    tracker.stop("stt")

    return {
        "transcript": transcript.strip(),
        "language": detected_language,
        "latency": tracker.report()
    }