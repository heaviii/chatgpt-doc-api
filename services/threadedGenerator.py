from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import queue

class ThreadedGenerator:
    def __init__(self):
        self.queue = queue.Queue()

    def __iter__(self):
        return self

    def __next__(self):
        item = self.queue.get()
        if item is StopIteration: raise item
        return item

    def send(self, data):
        self.queue.put(data)

    def close(self):
        self.queue.put(StopIteration)
    
    def encode(self, data):
        self.queue.put(data)
        print('encode:-------------------')
        print(data)
        return data

class ChainStreamHandler(StreamingStdOutCallbackHandler):
    def __init__(self, gen):
        super().__init__()
        self.gen = gen

    def on_llm_new_token(self, token: str, **kwargs):
        self.gen.send(token)

    def on_llm_new_token(self, token: str, **kwargs):
        self.gen.send(token)