
import threading

class RequestProcessor(threading.Thread):
    from Assistant.Requests.RequestManager import RequestManager
    def __init__(self, request_manager:RequestManager):
        super().__init__(daemon=True) # daemon=True поток завершится вместе с программой
        self.RequestManager = request_manager
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        from Assistant.Requests.RequestManager import LLMRequest
        while self.running:
            if not self.RequestManager.isRequestsEmpty():
                # Получаем запрос (блокирует поток, пока нет запроса)
                request: LLMRequest = self.RequestManager.getLastRequest()
                print("(RequestProcessor) Processing request type: {}".format(request.type) + "from user {}".format(request.user))

