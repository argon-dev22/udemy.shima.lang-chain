init_dict = {}

def load_env():
    from os import getenv
    from dotenv import load_dotenv
    load_dotenv()
    return getenv("OPENAI_API_KEY")

def init():
    init_dict["OPENAI_API_KEY"] = load_env()
    return init_dict