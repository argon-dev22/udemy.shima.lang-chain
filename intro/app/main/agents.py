import langchain
from langchain.agents import load_tools, AgentType
from langchain.agents.initialize import initialize_agent
from langchain.chat_models import ChatOpenAI
from init import init

langchain.verbose = True

def main():
    chat = ChatOpenAI(model_name="gpt-4o", temperature=0.0)
    tools = load_tools(["terminal"], llm=chat)
    agent_chain = initialize_agent(tools, chat, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
    result = agent_chain.run("What is current directory?")
    print(result)

if __name__ == "__main__":
    init()
    main()
