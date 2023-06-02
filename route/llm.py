# 定义参数解析器
import json
import os
from loguru import logger
from config import Config

from route.response import BaseRoute
from services.llma import LLma


# 定义路由类
class Llm():

    @staticmethod
    def chat(content):
        #json库
        #res = LLma().query_index(content)
        #chroma库
        res = LLma().askQuestionChroma(1,content)
        return res

    def chatStream(content):
        print('chatStream')
        logger.info('chatStream')
        return LLma.query_index_stream(content,1)

    def get():
        return BaseRoute.error('00000', {}, 'error Method')

    def createIndox():
        return LLma().create_index_chromadb()

