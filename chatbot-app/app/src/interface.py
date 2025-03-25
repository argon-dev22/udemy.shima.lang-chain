from langchain.memory import ChatMessageHistory

def convert_to_history(chat_history: list[tuple[str, str]]) -> ChatMessageHistory:
    history = ChatMessageHistory()
    for [user_message, ai_message] in chat_history:
        history.add_user_message(user_message)
        history.add_ai_message(ai_message)
    return history