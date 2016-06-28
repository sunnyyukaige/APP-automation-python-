__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By

class LoginManagerPage(BasePage):

    def InputUserName(self,value):
        self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/login_username').send_keys(value)


    def InputPassWord(self,value):
        self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/login_password').send_keys(value)

    def Submit(self):
        self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/login_confirm').click()
        self.browser.get_screenshot_as_file("f:\\sunnytestit.png")
