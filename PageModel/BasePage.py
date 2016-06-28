__author__ = 'sunny.yu2'
from Browser.BrowserManage import BrowserManage


class BasePage():

  def __init__(self):
    browserManage= BrowserManage()
    self.browser = browserManage.setBrowser()

  def title(self):
     self.browser.get_title()

  def getSource(self):
     return self.browser.get_pageSource()

