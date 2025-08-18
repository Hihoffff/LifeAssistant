
from enum import Enum

class LLMRequestHandler(Enum):
    BASE=0, #отправляем запрос на быстрый ответ пользователю
    SPLITER=1, #отправляем запрос на разбиение текста
    FUNCTION=2, #отправляем запрос на создание запроса на вызов функций


class LLMRequest:
    def __init__(self, user:str, type:LLMRequestHandler, request:str):
        self.request=request
        self.user = user
        self.type = type

    user: str
    type: LLMRequestHandler
    request: str

class LLMResponse:
    def __init__(self, user:str, source:LLMRequestHandler, request:str):
        self.request=request
        self.user = user
        self.type = type

    user: str
    source: LLMRequestHandler
    response: str
class RequestManager:
    from main import Main


    def __init__(self, main : Main):
        import queue
        self.requests = queue.Queue()
        self.responses = queue.Queue()
        self.main = main
    def sendRequest(self, request:LLMRequest):
        self.requests.put(request)
    def getLastRequest(self) -> LLMRequest:
        return self.requests.get()
    def getLastResponse(self) -> LLMResponse:
        return self.responses.get()
    def sendResponse(self, response:LLMResponse):
        self.responses.put(response)
    def isResponsesEmpty(self) -> bool:
        return self.responses.empty()
    def isRequestsEmpty(self) -> bool:
        return self.requests.empty()


