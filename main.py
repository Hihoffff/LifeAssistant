from Assistant.AssistantCore import AssistantCore
from UserData.UserDataManager import UserDataManager


class Main:
    def __init__(self):
        print("Launching of AI assistant...")
        print("Loading modules...")
        self.userDataManager = UserDataManager(self)
        from Assistant.LLM.LLMEngine import LLMModel
        self.assistantCore=AssistantCore(LLMModel.NOUS_HERMES,self)
        from Assistant.Requests.RequestManager import RequestManager
        self.requestManager = RequestManager(self)
        from ConsoleManager import ConsoleManager
        self.consoleManager=ConsoleManager(self.requestManager)
        from Assistant.Requests.RequestProcessor import RequestProcessor
        self.requestProcessor = RequestProcessor(self.requestManager)

    def getUserDataManager(self):
        return self.userDataManager
    def getAssistantCore(self):
        return self.assistantCore
    def run(self):
        print("Launching threads...")
        self.requestProcessor.start()
        self.consoleManager.runOutputThread()

        print("Launching console...")
        self.consoleManager.runInput()



def main():
    mainC = Main()
    mainC.run()
    print("Program closed!")


if __name__ == "__main__":
    main()

