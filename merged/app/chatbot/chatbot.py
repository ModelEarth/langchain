import os
from langchain.chains import RetrievalQA  
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from app.vector_store.vector_store_factory import VectorStoreFactory
from app.llms.selectLLM import SelectLLM
from app.embedder.selectEmbeddingModel import SelectEmbeddingModel

class Chatbot:
    def __init__(self , llm_model_name , embedding_model_name , vector_store):
        #TODO: Suggestion : Chatbot llm and embedding model to be passed as objects , and the selection process to be done outdside 
        
        s_llm = SelectLLM()
        self.llm = s_llm.get_llm(model_name=llm_model_name)
        s_embed = SelectEmbeddingModel()
        self.embedding_model,self.dimension = s_embed.get_embedding_model(embedding_model_name=embedding_model_name)
        self.vector_store = vector_store

    
    def filter_retriever(self , repo_name = None):
        if repo_name:
            retriever =  self.vector_store.get_retriever(filter= repo_name)
        else: 
            retriever =  self.vector_store.as_retriever()
        return retriever
    
    def get_rag_chain(self , retriever):
        prompt = hub.pull("rlm/rag-prompt")
        
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)
        
        rag_chain = (
            {"context": retriever | format_docs, "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        return rag_chain

 
    def answer_query(self , query , filter):
        # TODO: retreiver object has to be updated everytime
        # query1 = """what is the purpose of feed player"""
        rag_chain  = self.get_rag_chain(self.filter_retriever(filter))
        return rag_chain.invoke(query)
        
    







