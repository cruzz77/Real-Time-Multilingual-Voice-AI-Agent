LANGUAGE_MAP = {
    "en": "English",
    "hi": "Hindi",
    "ta": "Tamil"
}


def normalize_language(code: str):

    return LANGUAGE_MAP.get(
        code,
        "English"
    )