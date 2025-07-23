from Assistant.AssistantCore import AssistantCore
from UserData.UserDataManager import UserDataManager

class Main:
    def __init__(self):
        print("Launching of AI assistant...")
        print("Loading modules...")
        self.userDataManager = UserDataManager(self)
        self.assistantCore=AssistantCore(self)

    def getUserDataManager(self):
        return self.userDataManager
    def getAssistantCore(self):
        return self.assistantCore
    def run(self):
        print("💬 Готово! Введи сообщение (или 'exit' для выхода):")

        while True:
            user_input = input("\n👤 Ты: ")
            if user_input.strip().lower() in ["exit", "quit", "выход"]:
                print("👋 Завершаю...")
                break
            reply = self.getAssistantCore().createTxtRequest("console",user_input);
            print(f"🤖 Ассистент: {reply}")


def main():
    mainC = Main()
    mainC.run()
    print("Program closed!")



if __name__ == "__main__":
    main()