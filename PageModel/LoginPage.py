__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By


class LoginPage(BasePage):

  # def __init__(self):
  #     super(self).__init__()

    def InputUserName(self,value):
        self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/login_username').send_keys(value)


    def InputPassWord(self,value):
        self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/login_password').send_keys(value)

    def Submit(self):
        self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/login_confirm').click()
        self.browser.get_screenshot_as_file("f:\\sunnytestit.png")

    def Login(self,name,psw):
        self.InputUserName(name)
        self.InputPassWord(psw)
        self.Submit()

    def GotoManagerLogin(self):
        self.browser.find_elements(By.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')[1].click()


