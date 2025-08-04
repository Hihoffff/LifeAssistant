import queue

class RequestManager:
    def __init__(self):
        self.requests = queue.Queue()





class TextRequest:
    user: str
    source: str
    destination: str
    request: str
