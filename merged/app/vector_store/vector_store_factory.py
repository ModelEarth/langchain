
from app.vector_store.pinecone_vector_store import PineconeStore
from app.vector_store.InMemoryVectorStore import InMemoryStore
import os
from app.configuration.Constants import Constants
from app.configuration.ConfigParser import ConfigParser

class VectorStoreFactory:
    def __init__(self):
        return
    @staticmethod
    def get_vector_store( vector_store_name , embedding, dimension = None ):
        if vector_store_name == 'pinecone':
            return PineconeStore(embedding , dimension)           
        if vector_store_name == 'inmemory':
            path = os.path.join(Constants.MODEL_DIRECTORY, f'{ConfigParser.get_key_value("model_name")}.json')
            return  InMemoryStore(embedding , path= path)
        
