import os
import yaml

class VectorDataBase:
    def __init__(self ) :
        # self.index_name = index_name
        # self.dimensions  = dimensions
        # self.metric = metric
        self.default_config = os.path.join(os.path.dirname(
            os.path.abspath('__file__')), "config\database_config.yaml")
        self.get_database_config()
        
    def get_database_config(self):
        path = self.default_config
        if os.path.exists(path):
            with open(path, 'rt') as f:
                self.config = yaml.safe_load(f.read())
