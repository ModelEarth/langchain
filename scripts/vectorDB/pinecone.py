from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from vectorDB.vectorDataBase import VectorDataBase
from utils.logger import SetUpLogging
import logging
from langchain_pinecone import PineconeVectorStore
import os

class PineconeDB(VectorDataBase):
    def __init__(self , dimensions):
        super().__init__()
        self.index_name = self.config['pinecone']['pinecone_index_name'] 
        self.dimensions = dimensions
        self.metric =  self.config['pinecone']['pinecone_metric']
        self.api_key = os.environ.get('PINECONE_ACCESS_TOKEN')
        self.pc = Pinecone(api_key=self.api_key)
        SetUpLogging().setup_logging()
        if not self.pc.has_index(self.index_name):
            self.setup()
            logging.info("The PineCone index has not been setup Yet. setup() is called automatically to create the pinecone index")
        else: 
            #TODO:  check if the dimensions passed and pc match , if not raise error
            print("...")
        
        
            
    def setup(self):
        if not self.pc.has_index(self.index_name):
            self.pc.create_index(
                name=self.index_name,
                dimension=self.dimensions, 
                metric=self.metric, 
                spec=ServerlessSpec(
                    cloud="aws", 
                    region="us-east-1"
                ) 
            )
        self.index = self.pc.Index(self.index_name)
        logging.info(f"PineCone index is created with stats: {self.index.describe_index_stats()} ")

    def gets_stats(self):
        self.index = self.pc.Index(self.index_name)
        return self.index.describe_index_stats()
    
    def create_vector_store(self , embeddings):
        self.vectorstore = PineconeVectorStore(index_name=self.index_name, embedding=embeddings , pinecone_api_key= os.environ.get('PINECONE_ACCESS_TOKEN'))
        return self.vectorstore

    def add_docs(self, docs):
        self.vectorstore.add_documents(docs)
        logging.info("Document are added into the vector store")
    
    # def similarity_search(self, query , filter): # can be called in the upper layers as well
    #     self.vectorstore.similarity_search(query, filter=filter)



