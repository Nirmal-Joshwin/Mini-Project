from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from write_agent import agent as write_agent
from read_agent import agent as read_agent
from modify_agent import agent as modify_agent

load_dotenv()

@tool
def call_writer(instruction: str) -> str:
    """Delegate writing or creating tasks on file.text to the Writer Agent."""
    return write_agent.invoke({"messages": [{"role": "user", "content": instruction}]})["messages"][-1].text

@tool
def call_reader(instruction: str) -> str:
    """Delegate reading or summarizing tasks on file.text to the Reader Agent."""
    return read_agent.invoke({"messages": [{"role": "user", "content": instruction}]})["messages"][-1].text

@tool
def call_modifier(instruction: str) -> str:
    """Delegate modifying or editing tasks on file.text to the Modifier Agent."""
    return modify_agent.invoke({"messages": [{"role": "user", "content": instruction}]})["messages"][-1].text

coordinator = create_agent(
    ChatGoogleGenerativeAI(model="gemini-flash-lite-latest"),
    [call_writer, call_reader, call_modifier]
)

response = coordinator.invoke({"messages": [{
    "role": "user",
    "content": "First write to file.text: 'Team sync at 2 PM'. Next modify the time to 4 PM. Then read and summarize file.text."
}]})
print(response["messages"][-1].text)

