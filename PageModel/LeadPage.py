__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By

class LeadPage(BasePage):

  # def __init__(self):
  #     super(self).__init__()

    def StudentName(self,name):
        self.browser.set_wait_element_timeout(60000000)
        self.browser.find_element(By.ID,'com.ef.hugin.dev:id/lead_child_name').send_keys(name)

    def StudentAge(self,age):

        self.browser.find_element(By.ID,'com.ef.hugin.dev:id/lead_child_birth_age').send_keys(age)



    def PhoneNumber(self,number):

        self.browser.find_element(By.ID,'com.ef.hugin.dev:id/lead_child_phone').send_keys(number)


    def Submit(self):

        self.browser.find_element(By.ID,'com.ef.hugin.dev:id/lead_submit').click()

    def Scroll_down(self):
        self.browser.scroll_down()

    def Alert(self):
        self.browser.is_alert_present()
        self.browser.find_element(By.ID,'android:id/button1').click()
