__author__ = 'sunny.yu2'
from Browser.BrowserManage import BrowserManage
from WebElement.By import By
from Utilitys.Utils import Utils

class BasePage():

  def __init__(self):
    browserManage= BrowserManage()
    self.browser = browserManage.setBrowser("ios")

  def title(self):
     self.browser.get_title()

  def getSource(self):
     Utils.wait_for(self.browser.find_element(By.XPATH,'//UIANavigationBar[1]').is_displayed)
     return self.browser.get_pageSource()

