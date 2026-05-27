from memory.vector_store import (
    vector_store
)


def retrieve_memories(
    query: str
):

    docs = vector_store.similarity_search(
        query,
        k=3
    )

    memories = [
        doc.page_content
        for doc in docs
    ]

    return memories