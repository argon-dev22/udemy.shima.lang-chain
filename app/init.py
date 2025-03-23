from os import getenv
from dotenv import load_dotenv

def init():
    load_dotenv()
    OPENAI_API_KEY = getenv("OPENAI_API_KEY")
    return OPENAI_API_KEY