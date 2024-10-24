import os
import yaml
import logging
from app.utils.logger import SetUpLogging
from app.configuration.Constants import Constants

class LLM:
    def __init__(self):
        self.default_config = Constants.LLM_CONFIG
        SetUpLogging().setup_logging()
        self.get_llm_config()
        logging.info("LLM config has been parsed")

    def get_llm_config(self):
        path = self.default_config
        # print("LLM config Path: ", path)
        if os.path.exists(path):
            print("Inside path")
            with open(path, 'rt') as f:
                self.config = yaml.safe_load(f.read())
        # print(self.config)
                
if __name__ == "__main__":
    e = LLM()