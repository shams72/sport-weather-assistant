import os
import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from rag.rag import search

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

mcp = FastMCP("weather")


@mcp.tool()
def get_weather(city: str) -> dict:
    """Get the current weather for a city using OpenWeather."""

    if not API_KEY:
        raise ValueError("OPENWEATHER_API_KEY is not set")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature_c": data["main"]["temp"],
        "feels_like_c": data["main"]["feels_like"],
        "humidity_percent": data["main"]["humidity"],
        "wind_speed_mps": data["wind"]["speed"],
        "weather": data["weather"][0]["main"],
        "description": data["weather"][0]["description"]
    }

@mcp.tool()
def search_rag(query: str) -> list:
    """Search the sports knowledge base for information about
    which sports are suitable for different weather conditions."""
    return search(query)

if __name__ == "__main__":
    mcp.run()