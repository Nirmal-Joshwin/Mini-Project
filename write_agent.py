from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

@tool
def write_file(content: str) -> str:
    """Write text content to file.text."""
    with open("file.text", "w", encoding="utf-8") as f:
        f.write(content)
    return "Content successfully written to file.text"

agent = create_agent(ChatGoogleGenerativeAI(model="gemini-flash-lite-latest"), [write_file])
if __name__ == "__main__":
    response = agent.invoke({"messages": [{"role": "user", "content": "Write this note to file.text: Meeting is scheduled at 3 PM about AI architecture."}]})
    print(response["messages"][-1].text)

