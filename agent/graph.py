from memory.retrieval import (
    retrieve_memories
)

from agent.chains import (
    generate_response
)


async def run_agent(
    transcript: str,
    language: str
):

    memories = retrieve_memories(
        transcript
    )

    response = await generate_response(
        transcript,
        language,
        memories
    )

    return response