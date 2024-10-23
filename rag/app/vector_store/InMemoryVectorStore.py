import json
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
import os

from app.vector_store.VectorStore import VectorStore


class InMemoryStore(VectorStore):

    def __init__(self, embedding  = None, path = None):

        if not embedding:
            embedding = OpenAIEmbeddings()

        self.vector_store = InMemoryVectorStore(embedding)
        # reload from the disk
        if  path:
            self.file_path = path
            self.load_and_get_model(self.file_path)



    def load_and_get_model(self, file = None):
        if not file:
            file = self.file_path
        # search file exists and load
        if os.path.exists(file):
            with open(file, 'r') as ip:
                docs = json.load(ip)

            self.vector_store.store.update(docs)
        return self


    def save_model(self):
        with open(self.file_path, 'w') as ip:
            json.dump(self.vector_store.store,ip)


    def update_model(self, documents):
        self.vector_store.add_documents(documents)

        self.save_model()

        print('Model saved')

    def get_retriever(self, filter = {}, k = 10 ):

        # return self.vector_store.as_retriever(search_kwargs={'filter': {'repo': 'ModelEarth/langchain'}, 'k' : k})
        # return self.vector_store.as_retriever(search_kwargs={'k': k})
        return self.vector_store.as_retriever(filter = filter, k = k)











