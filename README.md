# Udemy_Shima_Langchain

## Quick Start

### 1. 環境変数の設定

.env.exampleをコピーして.envファイルを作成し、OpenAIのAPIキーを設定する。

### 2. コンテナの起動 

```
docker compose up -d
```

### 3. コンテナにログイン

```
docker compose exec -it app bash
```

### 4. アプリケーションの実行

```
cd ./main
python3 openai-api.py
```

### 5. コンテナの削除

```
docker compose down
```
