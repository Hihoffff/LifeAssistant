class Promter:
    def __init__(self, main: "Main"):
        self.Main = main
        self.UserDataManager = main.getUserDataManager()

        self.NousHermes_promt = {"role": "system", "content":(self.loadPromt("NousHermes_promt.txt"))}
        self.Llama_promt = {"role": "system", "content": (self.loadPromt("Llama_promt.txt"))}
    def createPromt(self,modelVar:int,user,request):
        messages = self.UserDataManager.getUserData(user).getMessages()
        messages.clear()
        if(len(messages) == 0):
            if(modelVar == 0):
                messages.append(self.NousHermes_promt)
            elif(modelVar == 1):
                messages.append(self.Llama_promt)
            else :
                print("Invalid modelVar for Promter!")
        messages.append({"role": "user", "content": request})
    def loadPromt(self,fileName):
        with open("Assistant/promt/promts/"+fileName, "r", encoding="utf-8") as file:
            return file.read()