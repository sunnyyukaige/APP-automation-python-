__author__ = 'sunny.yu2'
from Browser.BrowserManage import BrowserManage
from WebElement.By import By
from Utilitys.Utils import Utils

class BasePage():

  def __init__(self,plateform='Android'):
    browserManage= BrowserManage()
    self.browser = browserManage.setBrowser(plateform)

  def title(self):
     self.browser.get_title()

  def getSource(self,plateform=None):
     if(plateform=='ios'):
         Utils.wait_for(self.browser.find_element(By.XPATH,'//UIANavigationBar[1]').is_displayed)
     return self.browser.get_pageSource()

