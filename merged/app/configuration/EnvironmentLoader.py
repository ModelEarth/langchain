import os
import  dotenv
class EnvironmentLoader():
    def __init__(self):
        pass

    @staticmethod
    def load_variables():
        path = os.path.join(os.path.dirname(__file__), 'api_keys.env')
        dotenv.load_dotenv(path)


