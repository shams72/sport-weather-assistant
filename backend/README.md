# MCP RAG Sports & Weather Agent

A **proof of concept (PoC)** for an AI-powered sports and weather assistant built with **LangChain**, **Gemini**, **MCP**, and **RAG**.

This project is intended as a foundation for extensive future development and extensions, including integration with **WhatsApp** and a **web-based assistant**.

## Features

* Current weather using OpenWeather
* Sports information using RAG
* MCP-based tools
* Gemini LLM
* Conversation memory per user
* LLM decides which MCP tool to use
* Web/API-based assistant
* Tool usage and arguments displayed for debugging

## Backend

All backend-related code and configuration should live inside the `backend/` folder.

The backend is responsible for:

1. Starting the AI assistant backend.
2. Initializing the Gemini LLM.
3. Connecting to the MCP tools.
4. Loading and querying the RAG knowledge base.
5. Providing current weather information through OpenWeather.
6. Maintaining conversation memory per user.
7. Letting the LLM determine which MCP tool should be called.
8. Exposing the assistant through an API for the frontend or other clients.
9. Displaying selected tools and their arguments for debugging during development.

## Getting Started

From the project root:

```bash
cd backend
```

Install the backend dependencies:

```bash
pip install -r requirements.txt
```

Configure the required environment variables in `.env`.

Then start the backend using the project's configured entry point, for example:

```bash
python main.py
```

The exact startup command should match the backend entry-point file in this project.

## Environment Variables

The backend should load secrets and configuration from environment variables rather than hard-coding them.

Typical variables include:

```env
GEMINI_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

Add any additional MCP, database, RAG, or application configuration required by the implementation.

## Development Direction

The backend is designed as a foundation for future extensions such as:

* Web-based chat interface
* WhatsApp integration
* Additional MCP tools
* More sports data sources
* Expanded RAG knowledge bases
* Persistent conversation history
* Authentication and per-user sessions
* Production deployment
