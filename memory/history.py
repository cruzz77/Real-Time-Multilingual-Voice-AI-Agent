from memory.vector_store import (
    vector_store
)

from config import (
    FAISS_INDEX_PATH
)


def save_conversation_memory(
    patient_name: str,
    transcript: str,
    response: str
):

    memory_text = f"""
    Patient: {patient_name}

    User said:
    {transcript}

    Assistant replied:
    {response}
    """

    vector_store.add_texts([
        memory_text
    ])

    vector_store.save_local(
        FAISS_INDEX_PATH
    )