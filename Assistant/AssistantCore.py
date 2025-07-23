from Assistant.LLM.LLMEngine import LLMEngine
from Assistant.promt.Promter import Promter

class AssistantCore:
    def __init__(self,main: "Main"):
        self.Main = main
        self.LLMengine = LLMEngine(0)
        self.promter = Promter(main)

    def createTxtRequest(self,user,input):
        self.promter.createPromt(0,user,input)
        userData = self.Main.getUserDataManager().getUserData(user)
        reply = self.LLMengine.generate(userData.messages)
        userData.messages.append({"role": "assistant", "content": reply})
        return reply
