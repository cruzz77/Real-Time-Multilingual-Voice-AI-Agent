def normalize_language(
    language: str
):

    mapping = {
        "en": "English",
        "hi": "Hindi",
        "ta": "Tamil"
    }

    return mapping.get(
        language,
        "English"
    )