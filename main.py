from Assistant.AssistantCore import AssistantCore
from UserData.UserDataManager import UserDataManager

class Main:
    def __init__(self):
        print("Launching of AI assistant...")
        print("Loading modules...")
        self.userDataManager = UserDataManager(self)
        from Assistant.LLM.LLMEngine import LLMModel
        self.assistantCore=AssistantCore(LLMModel.NOUS_HERMES,self)

    def getUserDataManager(self):
        return self.userDataManager
    def getAssistantCore(self):
        return self.assistantCore
    def run(self):
        print("💬 Готово! Введи сообщение (или 'exit' для выхода):")
        from Assistant.LLM.LLMEngine import LLMModel
        while True:
            user_input = input("\n👤 Ты: ")
            if user_input.strip().lower() in ["exit", "quit", "выход"]:
                print("👋 Завершаю...")
                break
            reply = self.getAssistantCore().createTxtRequest(LLMModel.NOUS_HERMES,"console",user_input)
            print(f"🤖 Ассистент: {reply}")


def main():
    mainC = Main()
    mainC.run()
    print("Program closed!")



if __name__ == "__main__":
    main()