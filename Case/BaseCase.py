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
    userName=''
    password=''
    managerName=''
    managerPSW=''
    def setUp(self):
      cf=self.load_config_file()
      self.basePage = BasePage()
      BaseCase.userName=cf.get("configuration","username")
      BaseCase.password=cf.get("configuration","password")
      BaseCase.managerName=cf.get("configuration","managername")
      BaseCase.managerPSW=cf.get("configuration","managerpassword")

    def tearDown(self):
      if(self.defaultTestResult().failures):
         fileName = Formatter().format("{0}{1}.jpg", "f:\\",time.time().__str__())
         self.basePage.browser.get_screenshot_as_file(fileName)
      self.basePage.browser.close_App()
      browserManage= BrowserManage()
      self.browser = browserManage.clearBrowser()

    def load_config_file(self):
        config_file = self.get_relative_path("Configs", "Configs.ini")
        self.config.read(config_file)
        return self.config

    def get_relative_path(self, path, file_name):
        prepath=os.getcwd()
        return os.path.join(prepath, path, file_name)
