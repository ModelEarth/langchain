import os
from langchain_openai import OpenAIEmbeddings
from app.utils.logger import SetUpLogging
from app.embedder.EmbeddingModel import EmbeddingModel
import logging

class OpenaiEmbedding(EmbeddingModel):
    def __init__(self):
        super().__init__()
        self.embeddings = OpenAIEmbeddings(model = self.config['openai']['modelname'] , api_key= os.environ.get('OPENAI_API_KEY'))    
        logging.info("Open AI Embedding model is loaded")
        return 

    def get(self):
        return [self.embeddings , self.config['openai']['dimension']]

    # def embed_query(self,query):
    #     # dense = self.model.encode(query , convert_to_numpy= True )
    #     # return dense
    #     return
    
    # def embed_documents(self, docs):
    #     # dense =  self.model.encode(docs , convert_to_numpy= True)
    #     # return dense
    #     return 