
import os
from DocumentProcessor.docProcessor import DocumentProcessor
from dotenv import load_dotenv

# Defining main function
def main():
    
    # create the vectorDB instance
    # get the database instance
    # upsert the documents 
        
    load_dotenv()
    temp_url_path = ["https://raw.githubusercontent.com/ModelEarth/feed/main/README.md"]
    doc_processor = DocumentProcessor( embedding_model_name='openai',db_name='pinecone')
    doc_list = doc_processor.process_web_links(temp_url_path)
    doc_processor.add_documents(doc_list)
    print("The documents are loaded into data base")
    
    
# Using the special variable 
# __name__
if __name__=="__main__":
    main()