from langchain_groq import ChatGroq
from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)

from config import (
    GROQ_API_KEY,
    MODEL_NAME
)

from agent.prompts import SYSTEM_PROMPT

import json


llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name=MODEL_NAME
)


async def extract_intent(transcript: str):

    extraction_prompt = f"""
    Extract structured appointment information.

    Return ONLY valid JSON.

    Example:
    {{
        "intent": "book",
        "doctor_name": "",
        "specialization": "Dermatologist",
        "slot": "tomorrow evening"
    }}

    User:
    {transcript}
    """

    response = llm.invoke([
        HumanMessage(content=extraction_prompt)
    ])

    content = response.content.strip()

    try:
        return json.loads(content)

    except Exception:

        return {
            "intent": None,
            "doctor_name": None,
            "specialization": None,
            "slot": None
        }


async def generate_response(prompt: str):

    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=prompt)
    ])

    return response.content