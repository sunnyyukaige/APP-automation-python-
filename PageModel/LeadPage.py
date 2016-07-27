__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By
import time

class LeadPage(BasePage):

  # def __init__(self):
  #     super(self).__init__()

    def StudentName(self,name,plateform=None):
        if(plateform=='ios'):
            time.sleep(3)
            self.browser.find_element(By.XPATH,'//UIATableCell[1]/UIATextField[1]').set_value(name)
        else:
            self.browser.set_wait_element_timeout(60000000)
            self.browser.find_element(By.ID,'com.ef.hugin.dev:id/lead_child_name').set_value(name)

    def StudentAge(self,age,plateform=None):
        if(plateform=='ios'):
            time.sleep(3)
            self.browser.find_element(By.XPATH,'//UIATableCell[2]/UIATextField[1]').click()
            self.browser.find_element(By.XPATH,'//UIATableCell[2]/UIATextField[1]').send_keys(age)
        else:
            self.browser.find_element(By.ID,'com.ef.hugin.dev:id/lead_child_birth_age').send_keys(age)



    def PhoneNumber(self,number,plateform=None):
        if(plateform=='ios'):
            time.sleep(3)
            self.browser.find_element(By.XPATH,'//UIATableCell[3]/UIATextField[1]').click()
            self.browser.find_element(By.XPATH,'//UIATableCell[3]/UIATextField[1]').send_keys(number)
        else:
            self.browser.find_element(By.ID,'com.ef.hugin.dev:id/lead_child_phone').send_keys(number)


    def Submit(self,plateform=None):
        if(plateform=='ios'):
            time.sleep(3)
            self.browser.find_element(By.XPATH,'//UIATableCell[7]/UIAButton[1]').click()
        else:
            self.browser.find_element(By.ID,'com.ef.hugin.dev:id/lead_submit').click()

    def Scroll_down(self):
        self.browser.scroll_down()

    def Alert(self,plateform=None):
       if(plateform=='ios'):
            self.browser.find_element(By.XPATH,'//UIAWindow[1]/UIAButton[2]').click()
       else:
            self.browser.is_alert_present()
            self.browser.find_element(By.ID,'android:id/button1').click()
