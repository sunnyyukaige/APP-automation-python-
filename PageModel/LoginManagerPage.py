__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By

class LoginManagerPage(BasePage):


    def InputUserName(self,value,plateform=None):
        if(plateform=='ios'):
            element=self.browser.find_element(By.XPATH,'//UIACollectionCell[2]/UIATextField[1]')
            element.click()
            element.send_keys(value)
        else:
            self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/login_username').send_keys(value)



    def InputPassWord(self,value,plateform=None):
        if(plateform=='ios'):

            element=self.browser.find_element(By.XPATH,'//UIACollectionCell[2]/UIASecureTextField[1]')
            element.click
            element.send_keys(value)
        else:
            self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/login_password').send_keys(value)

    def Submit(self,plateform=None):
        if(plateform=='ios'):
            self.browser.find_element(By.XPATH, '//UIACollectionCell[2]/UIAButton[1]').click()
        else:
            self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/login_confirm').click()
            self.browser.get_screenshot_as_file("f:\\sunnytestit.png")

    def Login(self,name,psw,plateform=None):
         self.InputUserName(name,plateform)
         self.InputPassWord(psw,plateform)
         self.Submit(plateform)

