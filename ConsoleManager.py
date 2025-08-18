import threading

class ConsoleInput:
    from Assistant.Requests.RequestManager import RequestManager
    def __init__(self, request_manager: RequestManager):
        self.RequestManager = request_manager
        self.running = True
    def stop(self):
        self.running = False
    def run(self):
        from Assistant.Requests.RequestManager import LLMRequest, LLMRequestHandler
        print("Input request (or 'exit' for exit):")
        while self.running:
            user_input = input("\n👤 You: ")
            if user_input.strip().lower() in ["exit", "quit", "выход"]:
                print("Exiting...")
                self.stop()
            else:
                self.RequestManager.sendRequest(LLMRequest("console", LLMRequestHandler.BASE, user_input))
                print("Request sent successfully.")


class ConsoleOutput(threading.Thread):
    from Assistant.Requests.RequestManager import RequestManager
    def __init__(self, request_manager: RequestManager):
        super().__init__(daemon=True)  # daemon=True поток завершится вместе с программой
        self.RequestManager = request_manager
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        from Assistant.Requests.RequestManager import LLMResponse
        while self.running:
            if not self.RequestManager.isResponsesEmpty():
                response: LLMResponse = self.RequestManager.getLastResponse()
                print(response.response)


class ConsoleManager:
    from Assistant.Requests.RequestManager import RequestManager
    def __init__(self,request_manager: RequestManager):
        self.request_manager = request_manager
        self.consoleOutput = ConsoleOutput(request_manager)
        self.consoleInput = ConsoleInput(request_manager)
    def runOutputThread(self):
        self.consoleOutput.start()
    def runInput(self):
        self.consoleInput.run()
