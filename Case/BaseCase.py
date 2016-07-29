__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
import unittest
import time
from string import Formatter
from Browser.BrowserManage import BrowserManage
from Configs.Config import Config
import os

class BaseCase(unittest.TestCase):

    config=Config.get_instance()

    def setUp(self):
      self.load_config_file()
      self.basePage = BasePage()

    def tearDown(self):
      if(self.defaultTestResult().failures):
         fileName = Formatter().format("{0}{1}.jpg", "f:\\",time.time().__str__())
         self.basePage.browser.get_screenshot_as_file(fileName)
      self.basePage.browser.close_App()
      browserManage= BrowserManage()
      self.browser = browserManage.clearBrowser()

    def load_config_file(self):
        config_file = self.get_relative_path("../Configs", "Configs.ini")
        self.config.read(config_file)

    def get_relative_path(self, path, file_name):
        return os.path.join(os.path.dirname(__file__), path, file_name)
