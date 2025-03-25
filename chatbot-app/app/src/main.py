import gradio as gr
import src.lib.python_dotenv.init
from src.interface import convert_to_history
from src.chatbot_engine import chat

def respond(message, chat_history):
    history = convert_to_history(chat_history)

    bot_message = chat(message, history)
    chat_history.append((message, bot_message))
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")
