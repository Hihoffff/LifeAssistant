
class UserDataManager:
    def __init__(self,main: "Main"):
        self.main = main
        self.userDataMap = {}
    def loadUserData(self, user):
        self.userDataMap[user] = userData(user)
    def getUserData(self, user):
        if not(user in self.userDataMap):
            self.loadUserData(user)
        return self.userDataMap[user]




class userData:
    def __init__(self,user):
        self.messages = []
        self.user = user
    def getMessages(self):
        return self.messages
    def getUser(self):
        return self.user
    def addMessage(self, user, message):
        self.messages.append(message)

