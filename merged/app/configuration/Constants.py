import os

class Constants:

    MODEL_DIRECTORY = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    CONFIG_PATH =  os.path.join(os.path.dirname(__file__), 'config.ini')
    DATABASE_CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'database_config.yaml')
    EMBEDDING_CONFIG = os.path.join(os.path.dirname(__file__), 'embedding_config.yaml')
    LLM_CONFIG  = os.path.join(os.path.dirname(__file__), 'llm_config.yaml')
    LOGGING_CONFIG = os.path.join(os.path.dirname(__file__), 'logging_config.yaml')