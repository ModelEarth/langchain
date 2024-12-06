import os
import yaml
from app.configuration.Constants import Constants

class VectorDataBase:
    def __init__(self ) :
        # self.index_name = index_name
        # self.dimensions  = dimensions
        # self.metric = metric
        self.default_config = Constants.DATABASE_CONFIG_PATH
        self.get_database_config()
        
    def get_database_config(self):
        path = self.default_config
        if os.path.exists(path):
            with open(path, 'rt') as f:
                self.config = yaml.safe_load(f.read())
