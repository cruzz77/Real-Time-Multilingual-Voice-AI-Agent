from agent.chains import generate_response


async def chatbot_node(state):

    transcript = state["transcript"]

    response = await generate_response(
        transcript
    )

    state["response"] = response

    return state