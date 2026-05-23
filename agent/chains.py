from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

from config import (
    GROQ_API_KEY,
    MODEL_NAME
)

from agent.prompts import SYSTEM_PROMPT


llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME
)


async def generate_response(transcript: str):

    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=transcript)
    ])

    return response.content