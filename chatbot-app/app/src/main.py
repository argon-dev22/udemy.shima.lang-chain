import os
import gradio as gr
import src.lib.python_dotenv.init
from src.interface import convert_to_langchain_history
from src.chatbot_engine import chat, create_index

def respond(message, chat_history):
    history = convert_to_langchain_history(chat_history)

    bot_message = chat(message, history, index)
    chat_history.append((message, bot_message))
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)


if __name__ == "__main__":
    app_env = os.environ.get("APP_ENV", "production")
    if app_env == "production":
        username = os.environ.get("USERNAME")
        password = os.environ.get("PASSWORD")
        auth = (username, password)
    else:
        auth = None

    index = create_index()

    demo.launch(server_name="0.0.0.0", auth=auth)
