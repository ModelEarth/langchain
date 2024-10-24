
from app.llms.openAILLM import OpenAILLM

class SelectLLM:
    def __init__(self):
        return
    
    
    def get_llm(self , model_name):
        if model_name == 'openai':
            llm =  OpenAILLM(temperature=0.3).get()
            return llm
        if model_name == 'llama':
            # TODO : Try llama's BPE embedding model
            return
        if model_name == 'anthropic':
            # TODO : Try anthropic/claude embedding model 
            return
