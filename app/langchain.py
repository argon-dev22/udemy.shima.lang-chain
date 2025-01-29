import os
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.0)

result = llm.predict("自己紹介してください")
print(result)
