import os
import logging
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

from app.vector_store.VectorStore import VectorStore
from app.utils.logger import SetUpLogging
from app.vector_store.pineconeDB import PineconeDB


class PineconeStore(VectorStore):
    def __init__(self , embedding , dimensions  ):
        self.db = PineconeDB(dimensions=dimensions)
        self.vectorstore = PineconeVectorStore(index_name=self.db.index_name, embedding=embedding , pinecone_api_key= os.environ.get('PINECONE_ACCESS_TOKEN'))
    
    def load_and_get_store(self, file = None):
        return self.vectorstore

    def save_store(self):
        pass

    def update_store(self, documents):
        self.vectorstore.add_documents(documents)
        logging.info("Document are added into the vector store")

    def get_retriever(self, filter , k = 10):
        return self.vectorstore.as_retriever(filter = filter , k = k)

    def similarity_search(self, query , filter): # can be called in the upper layers as well
        self.vectorstore.similarity_search(query, filter=filter)

