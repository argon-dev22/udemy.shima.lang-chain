from langchain.memory import ChatMessageHistory

def convert_to_langchain_history(bot_user_id: str, conversations_history) -> ChatMessageHistory:
    history = ChatMessageHistory()
    for message in reversed(conversations_history["messages"]):
        text = message["text"]
        if message["user"] == bot_user_id:
            history.add_ai_message(text)
        else:
            history.add_user_message(text)
    return history