import os
import yaml
from abc import ABC, abstractmethod
from app.configuration.Constants import Constants

class VectorStore(ABC):

    # @abstractmethod
    # def __init__(self, embedding=None, path=None):
    #     pass
    # TODO : Pranoy says to load config at the start of service
    def __init__(self, embedding=None, path=None):
        self.default_config = Constants.DATABASE_CONFIG_PATH
        self.get_database_config()

    def get_database_config(self):
        path = self.default_config
        if os.path.exists(path):
            with open(path, 'rt') as f:
                self.config = yaml.safe_load(f.read())
        else: 
            self.config = {}

    @abstractmethod
    def load_and_get_store(self, file = None):
        pass

    @abstractmethod
    def save_store(self):
        pass

    @abstractmethod
    def update_store(self, documents):
        pass

    @abstractmethod
    def get_retriever(self, filter, k):
        pass


