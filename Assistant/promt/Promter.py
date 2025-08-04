from enum import Enum

from Assistant.LLM.LLMEngine import LLMModel







class Promter:
    class PROMTS(Enum):
        fastAnswers = ("FA","fastAnswers_promt.txt")
        NousHermes_promt = ("NH","NousHermes_promt.txt")
        Llama_promt = ("LLA","Llama_promt.txt")
        def __init__(self, promt_name, fileName):
            self.promt_name = promt_name
            self.fileName = fileName
        def getPromt(self) -> str:
            self.getPromt(self.value)

    def __init__(self, main: "Main"):
        self.Main = main
        self.UserDataManager = main.getUserDataManager()
        self.promts = {}
        for promt in Promter.PROMTS:
            self.promts[promt.promt_name] =self.__loadPromt(promt.fileName)

    def createPromt(self,model: LLMModel,user,request):
        messages = self.UserDataManager.getUserData(user).getMessages()
        messages.clear()
        if model.get_name() == LLMModel.NOUS_HERMES.get_name():
            messages.append({"role": "system", "content": self.getPromt(self.PROMTS.NousHermes_promt)})
            print(messages)
        elif model.get_name() == LLMModel.LLAMA.get_name():
            messages.append({"role": "system", "content": self.getPromt(self.PROMTS.Llama_promt)})
        else:
            print("Invalid modelVar for Promter!")
        messages.append({"role": "user", "content": request})


    def getPromt(self,promt : PROMTS) -> str:
        return self.promts[promt.promt_name]

    def __loadPromt(self,fileName)-> str:
        with open("Assistant/promt/promts/" + fileName, "r", encoding="utf-8") as file:
            return file.read()

