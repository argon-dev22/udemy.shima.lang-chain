import langchain
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
from init import init

langchain.verbose = True

def main():
    loader = DirectoryLoader("../docs/", glob="**/*.md")
    index = VectorstoreIndexCreator().from_loaders([loader])
    chat = ChatOpenAI(model_name="gpt-4o", temperature=0.0)
    result = index.query("LangChainのエコシステムについて1文で説明してください。", llm=chat)
    print(result)

if __name__ == "__main__":  
    init()
    main()
