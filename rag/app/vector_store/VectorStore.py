from abc import ABC, abstractmethod

class VectorStore(ABC):

    @abstractmethod
    def __init__(self, embedding=None, path=None):
        pass

    @abstractmethod
    def load_and_get_model(self, file = None):
        pass

    @abstractmethod
    def save_model(self):
        pass

    @abstractmethod
    def update_model(self, documents):
        pass

    @abstractmethod
    def get_retriever(self, filter, k):
        pass


