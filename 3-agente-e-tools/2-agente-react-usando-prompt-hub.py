from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from dotenv import load_dotenv

load_dotenv()

@tool("web_search_mock")
def web_search_mock(query: str) -> str:
    """Return the capital of a given country if it exists in the mock data."""
    data = {
        "Brazil": "Brasília",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United States": "Washington, D.C."
    }

    for country, capital in data.items():
        if country.lower() in query.lower():
            return f"The capital of {country} is {capital}."
    return "I don't know the capital of that country."

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)
tools = [web_search_mock]

prompt = hub.pull("hwchase17/react")
agent_chain = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent_chain, 
    tools=tools, 
    verbose=True
)

print(agent_executor.invoke({"input": "What is the capital of Iran?"}))