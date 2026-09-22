import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    return requests.get(f"https://wttr.in/{city}?format=3", timeout=5).text

agent = create_agent(
    ChatGoogleGenerativeAI(model="gemini-flash-latest"), [get_weather]
)

response = agent.invoke(
    {
        "messages": [{"role": "user", "content": "What is the weather in Banglore?"}]
    }
)

print(response["messages"][-1].text)