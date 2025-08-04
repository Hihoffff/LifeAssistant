from llama_cpp import Llama
from Assistant.LLM.LLMEngine import LLMBase


class NousHermes(LLMBase):
    def load(self):
        self.llm = Llama(
            model_path="models/Nous-Hermes-2-Mistral-7B-DPO.Q4_K_M.gguf",
            n_ctx=16000,  # 4096 default
            n_threads=8,
            n_gpu_layers=40,  # 40 или 0 если только CPU
            chat_format="chatml"
        )
    def unload(self):
        del self.llm
        import gc
        gc.collect()
    def response(self,messages):
        response = self.llm.create_chat_completion(
            messages=messages,
            max_tokens=1024,
            temperature=1
        )
        reply = response["choices"][0]["message"]["content"]
        return reply

    def get_name(self):
        return "nous_hermes_7B"