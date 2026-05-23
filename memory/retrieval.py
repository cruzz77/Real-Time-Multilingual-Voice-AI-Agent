from memory.vector_store import (
    vector_store
)

from utils.latency import (
    LatencyTracker
)


def retrieve_memories(query: str):

    tracker = LatencyTracker()

    tracker.start("memory_retrieval")

    docs = vector_store.similarity_search(
        query,
        k=3
    )

    tracker.stop("memory_retrieval")

    memories = [
        doc.page_content
        for doc in docs
    ]

    return memories, tracker.report()