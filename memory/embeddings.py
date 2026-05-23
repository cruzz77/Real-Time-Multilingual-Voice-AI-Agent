from langchain_huggingface import (
    HuggingFaceEmbeddings
)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"
)