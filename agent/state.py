from typing import TypedDict, List


class AgentState(TypedDict):

    transcript: str

    response: str

    language: str

    messages: List[dict]