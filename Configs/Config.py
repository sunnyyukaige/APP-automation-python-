
from configparser import ConfigParser


class Config(object):
    instance = None

    @staticmethod
    def get_instance():
        if Config.instance is None:
            Config.instance = ConfigParser()
            return Config.instance
        else:
            return Config.instance

