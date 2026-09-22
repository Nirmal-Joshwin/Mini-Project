from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

@tool
def modify_file(old_text: str, new_text: str) -> str:
    """Replace old_text with new_text in file.text."""
    with open("file.text", "r", encoding="utf-8") as f:
        content = f.read()
    with open("file.text", "w", encoding="utf-8") as f:
        f.write(content.replace(old_text, new_text))
    return f"Replaced '{old_text}' with '{new_text}' in file.text"

agent = create_agent(ChatGoogleGenerativeAI(model="gemini-flash-lite-latest"), [modify_file])
if __name__ == "__main__":
    response = agent.invoke({"messages": [{"role": "user", "content": "In file.text, change the meeting time to 5 PM."}]})
    print(response["messages"][-1].text)

