import os
from langchain_openai import ChatOpenAI
from llms.LLM import LLM

class OpenAILLM(LLM):
    def __init__(self , temperature = 0.3) :
        super().__init__()
        self.llm = ChatOpenAI(openai_api_key=os.environ.get('OPENAI_API_KEY'), model_name= self.config['openai']['modelname'],temperature=temperature)
        return

    def get(self):    
        return self.llm
     