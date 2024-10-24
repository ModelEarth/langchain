from vectorDB.pinecone import  PineconeDB

class SelectVectorDB:

    def __init__(self):
        return
    
    def get_db(self, db_name , dimension):
        if db_name == 'pinecone':
            db = PineconeDB(dimension)
            return db
        if db_name == 'inmemory':
            #TODO : Create In Memory Database
            return

