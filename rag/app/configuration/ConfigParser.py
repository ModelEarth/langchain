import configparser

from app.configuration.Constants import Constants


class ConfigParser:

    config = configparser.ConfigParser()
    config.read(Constants.CONFIG_PATH)

    # handle other cases
    @staticmethod
    def get_key_value(key):
        return ConfigParser.config['keys'][key]
