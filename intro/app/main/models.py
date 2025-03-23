from langchain.llms import OpenAI
from init import init

def main():
    llm = OpenAI(model_name="gpt-4o", temperature=0.0)

    result = llm.predict("自己紹介してください")
    print(result)

if __name__ == "__main__":
    init()
    main()
