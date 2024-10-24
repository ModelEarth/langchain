import os
from langchain_community.document_loaders import GithubFileLoader
from pydantic import BaseModel
import re
from langchain.document_loaders import TextLoader
from langchain.document_loaders.web_base import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from vectorDB.selectVectorDB import SelectVectorDB
from embedder.selectEmbeddingModel import SelectEmbeddingModel

class DocumentProcessor:
    def __init__(self , embedding_model_name , db_name):
        s_embed = SelectEmbeddingModel()
        s_db = SelectVectorDB()
        self.embedding_model,self.dimension = s_embed.get_embedding_model(embedding_model_name=embedding_model_name)
        self.db = s_db.get_db(db_name=db_name , dimension= self.dimension)
        self.db.create_vector_store(self.embedding_model)
        return

    def get_readme (self, repo_name , branch_name , github_token): # not utilized at the moment
        loader = GithubFileLoader(
            repo= repo_name, # Mention the repo we need 
            branch = branch_name ,  # the branch name
            access_token=github_token,
            github_api_url="https://api.github.com",
            file_filter=lambda file_path: file_path.endswith("README.md"), 
        )
        documents = loader.load()
        return documents

    def preprocess_text(self, text): # Not utilized at the moment
        text = re.sub(r'<[^>]+>', '', text)     # remove HTML
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)     # Remove URLs
        text = re.sub(r'!\[.*?\]\(.*?\)', '', text) # Remove image references
        text = re.sub(r'[^\w\s.?!#]', '', text) # Remove emoticons while preserving basic punctuation
        text = re.sub(r'\s+', ' ', text).strip()         # Remove extra whitespace
        return text

    def process_readme_text_from_web(self , weblink):
        # Use WebBaseLoader instead of TextLoader to load content from a URL
        # loader = WebBaseLoader("https://raw.githubusercontent.com/ModelEarth/feed/main/README.md")
        loader = WebBaseLoader(weblink)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(documents)
        for doc in docs:
            url = doc.metadata['source']
            parts = url.split('/')
            doc.metadata = {'source': url , 'owner': parts[3] ,'repo': parts[4] , 'branch': parts[5], 'filename': '/'.join(parts[6:])}
        return docs
    
    def process_web_links(self , links ):
        doc_list = []
        for link in links: 
            doc_list.extend(self.process_readme_text_from_web(link))
        return doc_list

    def add_documents(self , docs ):
        self.db.add_docs(docs)
    


