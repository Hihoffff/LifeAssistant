from enum import Enum
from Assistant.LLM.Llama import LLama
from Assistant.LLM.NousHermes import NousHermes



class LLMBase:  #структура каждого llm файла
    def get_name(self):...
    def load(self):...
    def unload(self):...
    def response(self, messages):...

class LLMModel(Enum):   #список доступных моделей
    LLAMA = LLama()
    NOUS_HERMES = NousHermes()
    def get_name(self):
        return self.value.get_name()

class LLMEngine:
    def __init__(self):
        self.models = {}
    def generate(self,model: LLMModel,messages):
        if model.get_name() not in self.models:
            self.load_model(model)
        return model.value.response(messages)
    def load_model(self,model:LLMModel):
        self.unload_model(model)
        model.value.load()
        self.models[model.get_name()] = model
    def unload_model(self, model: LLMModel):
        if model.get_name() in self.models:
            self.models[model.get_name()].unload()
            del self.models[model.get_name()]
