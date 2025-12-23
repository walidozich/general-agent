from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="general_assistant",
    model="gemini-2.5-flash",
    description="A general-purpose assistant for everyday questions.",
    instruction=(
        "You are a helpful, general-purpose assistant. "
        "Answer clearly and directly. "
        "If you are uncertain or the question depends on current information, use Google Search."
    ),
    tools=[google_search],  
)
