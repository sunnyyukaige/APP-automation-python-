__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By
import time

class HomePage(BasePage):

  # def __init__(self):
  #     super(self).__init__()

    def SelectMarketingPlace(self,plateform=None):
        if(plateform=='ios'):
            self.browser.set_wait_element_timeout(600000)
            time.sleep(3)
            self.browser.find_element(By.XPATH,'//UIATableCell[5]/UIATextField[1]').click()
            self.browser.find_element(By.XPATH,'//UIATableView[1]/UIATableCell[2]').click()
        else:
            self.browser.set_wait_element_timeout(600000)
            self.browser.find_element(By.ID,'com.ef.hugin.dev:id/home_marketing_place').click()
            self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/select_dialog_list_item_text').click()

    def AddLead(self,plateform=None):
        if(plateform=='ios'):
            self.browser.find_element(By.XPATH,'//UIAWindow[1]/UIAButton[3]').click()
        else:
            self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/home_add_lead').click()
            self.browser.get_screenshot_as_file("f:\\sunnytestit.png")

    def LeadsNumber(self,plateform=None):
        if(plateform=='ios'):
            return self.browser.find_element(By.XPATH,'//UIATableGroup[1]/UIAStaticText[2]').text
        else:
            return self.browser.find_element(By.ID,'com.ef.hugin.dev:id/dashboard_total').text