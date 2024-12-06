from app.embedder.openaiEmbedding import OpenaiEmbedding


class SelectEmbeddingModel:
    def __init__(self):
        return

    @staticmethod
    def get_embedding_model(embedding_model_name):
        if embedding_model_name == 'openai':
            embedding_model, dimension = OpenaiEmbedding().get() 
            return embedding_model , dimension
        if embedding_model_name == 'allmini':
            # TODO :  try other embedding models
            return
        if embedding_model_name == 'voyage':
            # TODO : try other embedding models
            return
