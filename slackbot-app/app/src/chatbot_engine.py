import os
from typing import List
import langchain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain.schema import HumanMessage
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.agents import initialize_agent, AgentType
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)
from langchain.memory import ConversationBufferMemory
from langchain.tools import BaseTool

langchain.verbose = True

def create_index():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    src_path = os.path.join(base_path, "src")
    loader = DirectoryLoader(src_path, glob="**/*.py", loader_cls=TextLoader)
    return VectorstoreIndexCreator().from_loaders([loader])

def create_tools(index: VectorStoreIndexWrapper, llm: ChatOpenAI) -> List[BaseTool]:
    vectorstore_info = VectorStoreInfo(
        name="project source code",
        description="A collection of the project source code",
        vectorstore=index.vectorstore
    )
    toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info, llm=llm)
    return toolkit.get_tools()

def chat(message: str, history: ChatMessageHistory, index: VectorStoreIndexWrapper) -> str:
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
    tools = create_tools(index, llm)
    memory = ConversationBufferMemory(chat_memory=history, memory_key="chat_history", return_messages=True)
    agent_chain = initialize_agent(
        tools,
        llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory
    )
    return agent_chain.run(input=message)
