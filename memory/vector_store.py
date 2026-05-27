from langchain_community.vectorstores import FAISS

from memory.embeddings import (
    embedding_model
)


texts = [
    "User prefers evening appointments",
    "User speaks Hindi",
    "User previously booked dermatologist appointment"
]


vector_store = FAISS.from_texts(
    texts,
    embedding_model
)