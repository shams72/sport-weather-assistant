# MCP RAG Sports & Weather Agent

A **proof of concept (PoC)** for an AI-powered sports and weather assistant built with **LangChain**, **Gemini**, **MCP**, and **RAG**.

The current implementation is **terminal-based** and demonstrates the core agent functionality, including tool selection, weather retrieval, sports knowledge retrieval, and conversation context.

This project is intended as a **foundation for extensive future development and extensions**, including integration with WhatsApp and a web-based assistant.

## Features

* Current weather using OpenWeather
* Sports information using RAG
* MCP-based tools
* Gemini LLM
* Conversation memory per user
* LLM decides which MCP tool to use
* Terminal-based chat interface
* Tool usage and arguments displayed for debugging

## Project Structure

```text
mcp-rag/
│
├── .env
├── agent.py
├── server.py
│
└── rag/
    └── rag.py
```

## MCP Tools

### `get_weather`

Retrieves the current weather for a specified city using OpenWeather.

### `search_rag`

Searches the sports knowledge base for relevant information.

The LLM determines which tool is appropriate based on the user's request.

## Environment Variables

Create a `.env` file:

```text
GOOGLE_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

Do not commit your `.env` file to GitHub.

## Install Dependencies

```bash
pip install langchain langchain-google-genai langchain-mcp-adapters fastmcp python-dotenv requests
```

## Run

Start the proof of concept agent:

```bash
python agent.py
```

The MCP server is started automatically by the agent.

## Example

```text
Enter your user ID: user1

You: What is the weather in Doha?

TOOLS USED:
Tool: get_weather | Arguments: {'city': 'Doha'}

AGENT:
The current weather in Doha is ...
```

Follow-up questions can use the conversation context:

```text
You: Can I go running there?
```

The agent can use the previously retrieved weather information together with the sports RAG data.

## User Memory

Conversation history is maintained separately using the `user_id`.

For example:

```text
user1 → Doha
user2 → Dubai
```

This keeps conversations between different users separate.

## Future Development

This project is currently a **proof of concept** and is intended to be **extensively extended**.

Potential future development includes:

### WhatsApp Assistant

Integrate the agent with WhatsApp so users can interact with the sports and weather assistant through chat messages.

### Web Assistant

Build a web-based interface using:

* **React** for the frontend
* **FastAPI** for the backend
* The existing LangChain agent and MCP tools as the AI layer

### Future Architecture

```text
                 ┌──────────────┐
                 │    React     │
                 │ Web Frontend │
                 └──────┬───────┘
                        │
                 ┌──────▼───────┐
                 │   FastAPI    │
                 │    Backend   │
                 └──────┬───────┘
                        │
                 ┌──────▼───────┐
                 │   LangChain  │
                 │    Agent     │
                 └──────┬───────┘
                        │
                 ┌──────▼───────┐
                 │     MCP      │
                 └──────┬───────┘
                       / \
                      /   \
             ┌────────▼┐ ┌▼─────────┐
             │ Weather │ │    RAG   │
             │  Tool   │ │ Knowledge│
             └─────────┘ └──────────┘
```

The goal is to keep the core agent and tool architecture reusable while adding different interfaces such as the terminal, web, and WhatsApp.

## Project Status

**Current:** Proof of concept, terminal-based sports and weather agent.

**Planned:** Extensive development, including web and WhatsApp interfaces, improved memory, additional MCP tools, and further agent capabilities.

## Technologies

* Python
* LangChain
* Gemini
* MCP
* FastMCP
* OpenWeather API
* RAG
* asyncio
* React (future)
* FastAPI (future)
* WhatsApp integration (future)
