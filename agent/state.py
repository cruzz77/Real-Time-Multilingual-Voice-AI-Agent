from typing import TypedDict
from typing import List
from typing import Optional


class AgentState(TypedDict):

    transcript: str

    response: str

    language: str

    messages: List[dict]

    intent: Optional[str]

    patient_name: Optional[str]

    doctor_name: Optional[str]

    specialization: Optional[str]

    slot: Optional[str]

    tool_result: Optional[dict]

    retrieved_memories: List[str]

    retrieval_latency: Optional[dict]

    llm_latency: Optional[dict]