
from chatbot.chatbot import Chatbot
import os
from dotenv import load_dotenv

# Defining main function
def main():
    
    load_dotenv()
    chatbot = Chatbot(llm_model_name='openai' , embedding_model_name='openai',db_name='pinecone')
    print(chatbot.query("what is the purpose of feed player"))

# Using the special variable 
# __name__
if __name__=="__main__":
    main()