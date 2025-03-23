from langchain.prompts import PromptTemplate

def main():
    template = """
    次のコマンドの概要を説明してください。

    コマンド: {command}
    """
    prompt = PromptTemplate(
        input_variables=["command"],
        template=template
    )
    result = prompt.format(command="ls -l")
    print(result)

if __name__ == "__main__":
    main()
