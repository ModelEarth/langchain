import os
import yaml
import logging
from utils.logger import SetUpLogging

class LLM:
    def __init__(self):
        self.default_config = os.path.join(os.path.dirname(
            os.path.abspath('__file__')), "config\llm_config.yaml")
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