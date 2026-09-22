from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

@tool
def read_file() -> str:
    """Read the contents of file.text."""
    with open("file.text", "r", encoding="utf-8") as f:
        return f.read()

agent = create_agent(ChatGoogleGenerativeAI(model="gemini-flash-lite-latest"), [read_file])
if __name__ == "__main__":
    response = agent.invoke({"messages": [{"role": "user", "content": "Read file.text and summarize it."}]})
    print(response["messages"][-1].text)

