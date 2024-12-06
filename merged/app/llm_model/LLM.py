from langchain_openai import ChatOpenAI

class LLMModel:

    def __init__(self, name):
        self.model = ChatOpenAI(model=name)

    def get_model(self):
        return self.model


