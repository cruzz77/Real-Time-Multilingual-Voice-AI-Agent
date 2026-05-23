from langchain_community.vectorstores import FAISS

from memory.embeddings import (
    embedding_model
)

from config import (
    FAISS_INDEX_PATH
)

import os


def load_vector_store():

    if os.path.exists(FAISS_INDEX_PATH):

        return FAISS.load_local(
            FAISS_INDEX_PATH,
            embedding_model,
            allow_dangerous_deserialization=True
        )

    return FAISS.from_texts(
        ["initial memory"],
        embedding_model
    )


vector_store = load_vector_store()