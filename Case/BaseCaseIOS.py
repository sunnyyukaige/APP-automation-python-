__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
import unittest
import time
from string import Formatter
from Browser.BrowserManage import BrowserManage
from Configs.Config import Config

class BaseCase(unittest.TestCase):

    config=Config.get_instance()

    def setUp(self):
      self.basePage = BasePage("ios")

    def tearDown(self):
      if(self.defaultTestResult().failures):
         fileName = Formatter().format("{0}{1}.jpg", "f:\\",time.time().__str__())
         self.basePage.browser.get_screenshot_as_file(fileName)
      self.basePage.browser.close_App()
      browserManage= BrowserManage()
      self.browser = browserManage.clearBrowser()


