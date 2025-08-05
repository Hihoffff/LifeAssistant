import queue
from enum import Enum

class LLMRequestType(Enum):
    BASE=0,
    SPLITER=1,
    FUNCTION=2,

class LLMRequest:
    user: str
    type: LLMRequestType
    request: str



class RequestManager:
    from main import Main

    def __init__(self, main : Main):
        self.requests = queue.Queue()
        self.responses = queue.Queue()
        self.main = main
    def sendRequest(self, request:LLMRequest):
        self.requests.put(request)
    def getLastResponse(self) -> LLMRequest:
        return self.responses.get()



