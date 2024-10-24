import os
import yaml
import logging
from utils.logger import SetUpLogging

class EmbeddingModel:
    def __init__(self):
        self.default_config = os.path.join(os.path.dirname(
            os.path.abspath('__file__')), "config\embedding_config.yaml")
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