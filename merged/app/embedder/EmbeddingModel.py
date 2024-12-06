import os
import yaml
import logging
from app.utils.logger import SetUpLogging
from app.configuration.Constants import Constants

class EmbeddingModel:
    def __init__(self):
        self.default_config = Constants.EMBEDDING_CONFIG
        print("CONFIG:" , self.default_config)
        SetUpLogging().setup_logging()
        self.get_embedding_config()
        logging.info("Embedding model config has been parsed")

    def get_embedding_config(self):
        path = self.default_config
        if os.path.exists(path):
            with open(path, 'rt') as f:
                self.config = yaml.safe_load(f.read())
                
if __name__ == "__main__":
    e = EmbeddingModel()