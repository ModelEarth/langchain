import os
from langchain.chains import RetrievalQA  
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from vectorDB.selectVectorDB import SelectVectorDB
from llms.selectLLM import  SelectLLM
from embedder.selectEmbeddingModel import SelectEmbeddingModel

class Chatbot:
    def __init__(self , llm_model_name , embedding_model_name , db_name , filter_repo_name = None):
        s_llm = SelectLLM()
        self.llm = s_llm.get_llm(model_name=llm_model_name)
        s_embed = SelectEmbeddingModel()
        self.embedding_model,self.dimension = s_embed.get_embedding_model(embedding_model_name=embedding_model_name)
        s_db = SelectVectorDB()
        self.db = s_db.get_db(db_name=db_name , dimension= self.dimension)

        self.vectorstore = self.db.create_vector_store(self.embedding_model)

        self.retriever = self.filter_retriever(filter_repo_name)
        self.vectorstore.as_retriever(filter={'repo': 'feed'} )
        prompt = hub.pull("rlm/rag-prompt")

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)
        
        self.rag_chain = (
            {"context": self.retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
    
    def filter_retriever(self , repo_name = None):
        if repo_name:
            retriever =  self.vectorstore.as_retriever(filter={'repo': repo_name} )
        else: 
            retriever =  self.vectorstore.as_retriever()
        return retriever
    
    def query(self , query):
        # query1 = """what is the purpose of feed player"""
        return self.rag_chain.invoke(query)
        
    







