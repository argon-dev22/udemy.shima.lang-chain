import requests
import json
from init import init

def chat_model(OPENAI_API_KEY):
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


def completions_model(OPENAI_API_KEY):
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
    OPENAI_API_KEY = init()
    # completions_model(OPENAI_API_KEY)
    chat_model(OPENAI_API_KEY)

if __name__ == "__main__":
    main()
