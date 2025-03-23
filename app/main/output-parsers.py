import langchain
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field, validator
from typing import List
from init import init

langchain.verbose = True

class Recipe(BaseModel):
    ingredients: List[str] = Field(description="ingredients of the dish")
    steps: List[str] = Field(description="steps to make the dish")

def main():
    # チャットモデルを作成
    chat = ChatOpenAI(model_name="gpt-4o", temperature=0.0)

    # プロンプトテンプレートを作成
    template = """
    料理のレシピを教えてください。

    {format_instructions}

    料理名: {dish}
    """

    # 出力パーサーを作成
    parser = PydanticOutputParser(pydantic_object=Recipe)

    prompt = PromptTemplate(
        template=template,
        input_variables=["dish"],
        partial_variables={"format_instructions": parser.get_format_instructions()}
    )

    # チェーンを作成
    chain = LLMChain(llm=chat, prompt=prompt)

    # チェーンを実行
    result = chain.run({"dish": "カレー"})
    # print(result)

    # 出力結果をPythonのオブジェクトにマッピング
    recipe = parser.parse(result)
    # print(type(recipe))
    # print(recipe)

if __name__ == "__main__":
    init()
    main()