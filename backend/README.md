

## Backend

All backend-related code and configuration should live inside the this folder.

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


## Environment Variables

Setup a `.env` file and set the api keys for gemini and the open weather in the `.env` file.

```env
GEMINI_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

## Getting Started

Install the backend dependencies:

```bash
pip install -r requirements.txt
```

Configure the required environment variables in `.env`.

Then start the backend using the project's configured entry point, for example:

```bash
 python -m uvicorn main:app --reload
```

The exact startup command should match the backend entry-point file in this project.


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
