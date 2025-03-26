import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from chatbot_engine import chat, create_index
from interface import convert_to_langchain_history

load_dotenv()
index = create_index()
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

def fetch_history(channel_id: str):
    bot_user_id = app.client.auth_test()["user_id"]
    conversations_history = app.client.conversations_history(channel=channel_id, limit=3)
    return convert_to_langchain_history(bot_user_id, conversations_history)

@app.event("app_mention")
def handle_mention(event, say):
    channel_id = event["channel"]
    history = fetch_history(channel_id)

    message = event["text"]
    bot_message = chat(message, history, index)
    say(bot_message)

if __name__ == "__main__":
    app_env = os.environ.get("APP_ENV", "production")
    if app_env == "production":
        app.start(port=int(os.environ.get("PORT", 3000)))
    else:
        SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
