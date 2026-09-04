import os
import asyncio

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY was not found")

print("Gemini API key found")


client = MultiServerMCPClient(
    {
        "weather": {
            "transport": "stdio",
            "command": "python",
            "args": ["server.py"],
        }
    }
)


agent = None

async def get_agent():

    global agent

    if agent is None:

        print("\nStarting MCP server...")

        tools = await client.get_tools()

        print("\nMCP tools available:")

        for tool in tools:
            print("-", tool.name)

        model = ChatGoogleGenerativeAI(
            model="gemini-3.5-flash-lite",
            google_api_key=api_key,
        )

        agent = create_agent(
            model,
            tools,

            system_prompt="""
You are a sports and weather assistant.

You can ONLY answer questions about sports and weather.

==================================================
TOOLS
==================================================

For current weather:
Use get_weather.

For sports information:
Use search_rag.

You must use the tools when the required information
is not already available in the conversation.

==================================================
WEATHER
==================================================

Before calling get_weather:

1. Check the conversation history.
2. Check whether weather for the relevant city is
   already available.
3. If the required weather information is already
   available and the user is asking a follow-up question,
   reuse that information.
4. If the user explicitly asks for current, latest,
   updated, or new weather, call get_weather again.

==================================================
CITY MEMORY
==================================================

Remember cities mentioned in THIS conversation.

If the user says:

"there"
"it"
"that city"
"there today"

use the relevant city from the conversation when
the meaning is clear.

If multiple cities have been discussed and it is
unclear which city the user means:

ASK the user to specify the city.

Never guess.

==================================================
SPORTS
==================================================

Use search_rag for sports information.

If the user asks something such as:

"Can I run there?"
"Can I play tennis there?"
"Is football okay there?"

then:

1. Determine the relevant city from the conversation.
2. Use the weather information already available
   for that city when possible.
3. Use search_rag for the sports information.
4. Base the answer ONLY on the available weather
   and RAG information.

==================================================
STRICT DATA RULE
==================================================

Do NOT use your own general knowledge.

Do NOT guess.

Do NOT make up facts.

Do NOT add information that is not present in:

- tool results
- conversation history

If the required information is unavailable, say:

"Sorry, I don't have that information in my available data."

==================================================
OUTSIDE DOMAIN
==================================================

If the user asks about coding, programming, politics,
entertainment, mathematics, or anything unrelated
to sports and weather, say:

"Sorry, I can only answer sports and weather-related questions."
"""
        )

    return agent

conversations = {}

async def process_message(
    user_id: str,
    user_message: str
):

    if user_id not in conversations:
        conversations[user_id] = []

    messages = conversations[user_id]

    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    agent_instance = await get_agent()

    result = await agent_instance.ainvoke(
        {
            "messages": messages
        }
    )

    conversations[user_id] = result["messages"]

    final_message = result["messages"][-1]

    print("\nTOOLS USED:")

    for message in result["messages"]:

        if hasattr(message, "tool_calls") and message.tool_calls:

            for tool_call in message.tool_calls:

                print(
                    "Tool:",
                    tool_call["name"],
                    "| Arguments:",
                    tool_call["args"]
                )

    print("\nAGENT:")
    print(final_message.content)


    return final_message.content


async def main():

    user_id = input("Enter your user ID: ")

    print("\nType your questions.")
    print("Type 'exit' to quit.\n")

    while True:

        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("\nGoodbye!")
            break

        if not user_message.strip():
            continue

        await process_message(
            user_id=user_id,
            user_message=user_message
        )

if __name__ == "__main__":
    asyncio.run(main())