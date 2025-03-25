import langchain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain.schema import HumanMessage

langchain.verbose = True

def chat(message: str, history: ChatMessageHistory) -> str:
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

    messages = history.messages
    messages.append(HumanMessage(content=message))

    return llm(messages).content
