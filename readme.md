# 基于自有数据文件的chatgpt

## 使用技术

langchain+chatgpt+fastapi

## Usage

1.Install requirements

    ```
    pip3 install -r requirements.txt

    ```
2.copy `config-dev.py to` `config-py`

3.add openai key to `OPENAI_API_KEY`

DATA_PATH = './data'
./data 源数据文件

INDEX_JSON_PATH = './index.json'
向量存本地json文件，删除后自动重新加载data目录文件，到json文件

VECTOR_STORE_PATH = './vector_store'
chroma本地向量数据库的文件路径，删除后自动重新加载data目录文件，到向量数据库

## 启动命令

uvicorn main:app --reload

## 相关接口

默认使用Chorma向量数据库

- [问答文相关信息]

```
curl -X POST -H "content-type:application/json" 'http://127.0.0.1:8000/llm/chat'  -d '{"content": "我家的花园叫什么"}'
```

- [stream流式问答文相关信息]

```
curl -X POST -H "content-type:application/json" 'http://127.0.0.1:8000/llm/chatStream'  -d '{"content": "我家的花园叫什么"}'

```

## 向量数据库

### 本地向量文件

index.json

### Chorma

本地向量数据库

### Pinecone

Pinecone 是一个在线的向量数据库。所以，我可以第一步依旧是注册，然后拿到对应的 api key。<https://app.pinecone.io/>

免费版如果索引14天不使用会被自动清除。

然后创建我们的数据库：

Index Name：这个随意

Dimensions：OpenAI 的 text-embedding-ada-002 模型为 OUTPUT DIMENSIONS 为 1536，所以我们这里填 1536

Metric：可以默认为 cosine
