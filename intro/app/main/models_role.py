import langchain
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import openai
from init import init

# langchain.verbose = True
openai.log = "debug"

def no_role_setting():
    chat = ChatOpenAI(model_name="gpt-4o", temperature=0.0, max_tokens=100)
    result = chat.predict("You are a helpful assistant.")
    print(result)
    result = chat.predict("Hi, I'm John Doe. What is your name?")
    print(result)


def role_setting():
    chat = ChatOpenAI(model_name="gpt-4o", temperature=0.0, max_tokens=100)
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="Hi, I'm John Doe. What is your name?"),
    ]
    result = chat(messages)
    print(result)

def main():
    # no_role_setting()
    role_setting()

if __name__ == "__main__":
    init()
    main()
