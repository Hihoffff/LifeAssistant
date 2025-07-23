from Assistant.LLM.LLMEngine import LLMEngine,LLMModel
from Assistant.promt.Promter import Promter

class AssistantCore:
    def __init__(self,model:LLMModel,main: "Main"):
        self.Main = main
        self.LLMEngine = LLMEngine()
        self.promter = Promter(main)
        self.LLMEngine.load_model(model)

    def createTxtRequest(self,model:LLMModel,user,input):
        self.promter.createPromt(model,user,input)
        userData = self.Main.getUserDataManager().getUserData(user)
        reply = self.LLMEngine.generate(model, userData.messages)
        userData.messages.append({"role": "assistant", "content": reply})
        return reply
