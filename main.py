from asyncio import sleep
import asyncio
import json
import os
import sys
import threading
import time
from fastapi import FastAPI, Request, Response

from fastapi.responses import StreamingResponse

from loguru import logger
from config import Config

from route.hello import Hello
from route.llm import Llm
from services.chatgpt import Chatgpt
from services.llma import LLma
from services.threadedGenerator import ThreadedGenerator
from pydantic import BaseModel


logger.add('logs/app.log', rotation='500 MB', retention='1 days',
           level='INFO', encoding="utf-8", enqueue=True, compression="tar.gz")
logger.info('server init ')

app = FastAPI()



@app.api_route('/streamTest')
async def streamed_response():
    def generate():
        yield 'Hello asdf'+"\r\n"
        time.sleep(1)
        yield 'asdf'+"\r\n"
        time.sleep(1)
        yield '!'+"\r\n"
    return StreamingResponse(generate(), media_type='text/stream')


@app.api_route('/hello', methods=['GET', 'POST'])
async def hello(request: Request):
    logger.info('This is an info message')
    if request.method == 'POST':
        return Hello.post()
    else:
        return Hello.get()
    
@app.api_route('/chatgpt/chat', methods=['GET', 'POST'])
async def chatgptChat(request: Request):
    
    if request.method == 'POST':
        return Chatgpt.chat(content,1)
    else:
        content = request.query_params["content"]
        return Chatgpt.chat(content,1)


@app.api_route('/chatgpt/chatStream', methods=['GET', 'POST'])
async def chatgptChatStream(request: Request):
    if request.method == 'POST':
        return StreamingResponse(Chatgpt.streamChat(content,1), media_type='text/stream')
    else:
        content = request.query_params["content"]
        return StreamingResponse(Chatgpt.streamChat(content,1), media_type='text/stream')

@app.api_route('/llm/chat', methods=['GET', 'POST'])
async def llmChat(request: Request, q:str=None):
    print("method:",request.method)
    if request.method == 'POST':
        content_type = request.headers["Content-Type"]
        if content_type == "application/json":
            json_body = await request.body()
            print("json_body:", json_body)
            body = json.loads(json_body)
            # 如果参数校验失败，则返回 400 状态码和错误信息
            return Llm.chat(body["content"])
    else:
        content = request.query_params["content"]

        print(content)
        return Llm.chat(content)


@app.api_route('/llm/chatStream', methods=['GET', 'POST'])
async def chatStream(request: Request):
    if request.method == 'POST':
        content_type = request.headers["Content-Type"]
        if content_type == "application/json":
            json_body = await request.body()
            print("json_body:", json_body)
            body = json.loads(json_body)
            return StreamingResponse(Llm.chatStream(body["content"]), media_type="text/event-stream")
    else:
        content = request.query_params["content"]
        return StreamingResponse(Llm.chatStream(content), media_type="text/event-stream")


@app.api_route('/llm/create-index', methods=['GET', 'POST'])
async def llmCreateIndex(request: Request):
    if request.method == 'POST':
        return Llm.createIndox()
    else:
        return Llm.createIndox()

Llm.createIndox()

if __name__ == '__main__':
    logger.info('app RUN')
