
from configparser import ConfigParser

__author__ = 'Fox'

class Config(object):
    instance = None

    @staticmethod
    def get_instance():
        if Config.instance is None:
            Config.instance = ConfigParser()
            return Config.instance
        else:
            return Config.instance

    @staticmethod
    def get_new_instance():
        return ConfigParser()