"""
生のOpenAI APIを使ってChatモデルを呼び出す。
LangChainとは無関係。
"""

import os
import requests
import json
from init import init

def chat_model():
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    data = {
        "model": "gpt-4o",
        "messages": [
            {"role": "user", "content": "Hello!"}
        ],
        "temperature": 0.0,
    }

    response = requests.post(url=url, headers=headers, json=data)
    print(json.dumps(response.json(), indent=2))

def completions_model():
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    data = {
        "model": "gpt-3.5-turbo-instruct",
        "prompt": "Hello!",
        "temperature": 0.0,
    }

    response = requests.post(url=url, headers=headers, json=data)
    print(json.dumps(response.json(), indent=2))

def main():
    # completions_model()
    chat_model()

if __name__ == "__main__":
    init()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    main()
