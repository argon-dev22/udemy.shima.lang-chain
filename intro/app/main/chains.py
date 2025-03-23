import langchain
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from init import init

langchain.verbose = True

# 単一のチェーンを作成
def mono_chain():
    # チャットモデルを作成
    chat = ChatOpenAI(model_name="gpt-4o", temperature=0.0)
    
    # プロンプトテンプレートを作成 
    template = """
    次のコマンドの概要を説明してください。

    コマンド: {command}
    """
    prompt = PromptTemplate(
        input_variables=["command"],
        template=template
    )

    # チェーンを作成
    chain = LLMChain(llm=chat, prompt=prompt)

    # チェーンを実行
    result = chain.run("ls -l")

    # 結果を表示
    print(result)

# チェーンの連結
def simple_sequential_chain():
    from langchain.chains import SimpleSequentialChain

    # チャットモデルを作成
    chat = ChatOpenAI(model_name="gpt-4o", temperature=0.0)

    # チェーン1
    ## プロンプトテンプレートを作成
    cot_template = """
    以下の質問に回答してください。

    ### 質問 ###
    {question}
    ### 質問終了 ###

    ステップバイステップで考えてください。
    """
    cot_prompt = PromptTemplate(
        input_variables=["question"],
        template=cot_template
    )

    ## チェーンの作成
    cot_chain = LLMChain(llm=chat, prompt=cot_prompt)

    # チェーン2
    ## プロンプトテンプレートを作成
    summarize_template = """
    以下の内容を一言に要約してください。

    ### 内容 ###
    {content}
    ### 内容終了 ###
    """

    summarize_prompt = PromptTemplate(
        input_variables=["content"],
        template=summarize_template
    )

    ## チェーンの作成
    summarize_chain = LLMChain(llm=chat, prompt=summarize_prompt)

    # チェーンの作成
    cot_summarize_chain = SimpleSequentialChain(
        chains=[cot_chain, summarize_chain]
    )

    result = cot_summarize_chain.run("私は市場に行って10個のリンゴを買いました。隣人に2つ、修理工に2つ渡しました。それから5つのリンゴを買って1つ食べました。残りは何個ですか？")
    print(result)

def main():
    # mono_chain()
    simple_sequential_chain()

if __name__ == "__main__":
    init()
    main()
