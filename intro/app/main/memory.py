import os
import requests
import json
import langchain
from init import init

langchain.verbose = True

def post_chat_completions(content):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "user", "content": content}
        ],
        "temperature": 0.0,
    }

    response = requests.post(url=url, headers=headers, json=data)
    print(json.dumps(response.json(), indent=2))

def post_chat_completions_without_context():
    post_chat_completions("Hi, My name is John.")
    post_chat_completions("Do you know my name?")

def post_chat_completions_with_context():
    post_chat_completions("""
    Human: Hi, My name is John.
    AI: Hi, John.
    Human: Do you know my name?
    AI:
    """
    )

def post_chat_completions_with_memory():
    from langchain.chains import ConversationChain
    from langchain.chat_models import ChatOpenAI
    from langchain.memory import ConversationBufferMemory
    import openai

    openai.log = "debug"

    chat = ChatOpenAI(model_name="gpt-4o", temperature=0.0, max_tokens=100)
    memory = ConversationBufferMemory()
    conversation = ConversationChain(llm=chat, memory=memory)

    while True:
        user_message = input("You: ")
        if user_message == "exit":
            break
        result = conversation.predict(input=user_message)
        print(f"AI: {result}")

def post_chat_completions_with_memory_changing_role():
    from langchain.chains import ConversationChain
    from langchain.chat_models import ChatOpenAI
    from langchain.memory import ConversationBufferMemory
    import openai

    openai.log = "debug"

    chat = ChatOpenAI(model_name="gpt-4o", temperature=0.0, max_tokens=100)
    memory = ConversationBufferMemory()
    conversation = ConversationChain(llm=chat, memory=memory)

    while True:
        user_message = input("You: ")
        if user_message == "exit":
            break
        memory.chat_memory.add_user_message(user_message)
        ai_message = chat(memory.chat_memory.messages)
        memory.chat_memory.add_ai_message(ai_message.content)
        print(f"AI: {ai_message.content}")

def main():
    # post_chat_completions_without_context()
    # post_chat_completions_with_context()
    post_chat_completions_with_memory()
    # post_chat_completions_with_memory_changing_role()

if __name__ == "__main__":
    init()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    main()