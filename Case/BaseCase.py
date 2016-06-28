__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
import unittest
import time
from string import Formatter
from Browser.BrowserManage import BrowserManage

class BaseCase(unittest.TestCase):

    def setUp(self):
      self.basePage = BasePage()

    def tearDown(self):
      if(self.defaultTestResult().failures):
         fileName = Formatter().format("{0}{1}.jpg", "f:\\",time.time().__str__())
         self.basePage.browser.get_screenshot_as_file(fileName)
      self.basePage.browser.close_App()
      browserManage= BrowserManage()
      self.browser = browserManage.clearBrowser()


