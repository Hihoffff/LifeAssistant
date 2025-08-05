
import threading

class RequestProcessor(threading.Thread):
    from Assistant.Requests.RequestManager import RequestManager
    def __init__(self, request_manager:RequestManager):
        super().__init__(daemon=True)
        self.RequestManager = request_manager
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        from Assistant.Requests.RequestManager import LLMRequest
        import queue
        while self.running:
            try:
                # Получаем запрос (блокирует поток, пока нет запроса)
                request: LLMRequest = self.RequestManager.requests.get(timeout=1)
            except queue.Empty:
                continue
            print("(RequestProcessor) Processing request type: {}".format(request.type) + "from user {}".format(request.user))

