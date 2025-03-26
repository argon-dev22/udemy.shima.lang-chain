# Udemy_Shima_Langchain_Slackbot-App

## Quick Start

### 1. 環境変数の設定

`.env.example`をコピーして`.env`ファイルを作成し、OpenAIのAPIキーを設定する。

※ APIキーは[こちら](https://platform.openai.com/settings/organization/api-keys)から確認

### 2. コンテナの起動 

```
docker compose up -d
```
または
```
make up
```

### 3. コンテナにログイン

```
docker compose exec -it app bash
```
または
```
make in
```

### 4. アプリケーションの実行

```
poetry run python src/main.py
```

### 5. コンテナの削除

```
docker compose down
```
または
```
make down
```
