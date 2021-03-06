__author__ = 'sunny.yu2'
from PageModel.BasePage import BasePage
from WebElement.By import By


class LoginPage(BasePage):

  # def __init__(self):
  #     super(self).__init__()

    def InputUserName(self,value,plateform=None):
        if(plateform=='ios'):
            element=self.browser.find_element(By.XPATH,'//UIATextField[1]')
            element.click()
            element.send_keys(value)
        else:
            self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/login_username').send_keys(value)



    def InputPassWord(self,value,plateform=None):
        if(plateform=='ios'):

            element=self.browser.find_element(By.XPATH,'//UIATextField[2]')
            element.click
            element.send_keys(value)
        else:
            self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/login_password').send_keys(value)

    def Submit(self,plateform=None):
        if(plateform=='ios'):
            self.browser.find_element(By.XPATH, '//UIACollectionCell[1]/UIAButton[1]').click()
        else:
            self.browser.find_element(By.ID, 'com.ef.hugin.dev:id/login_confirm').click()
            self.browser.get_screenshot_as_file("f:\\sunnytestit.png")

    def Login(self,name,psw,plateform=None):
        self.InputUserName(name,plateform)
        self.InputPassWord(psw,plateform)
        self.Submit(plateform)

    def GotoManagerLogin(self,plateform=None):
        if(plateform=='ios'):
            self.browser.find_element(By.XPATH,'//UIAScrollView[1]/UIAButton[2]').click()
        else:
            self.browser.find_elements(By.CLASS_NAME, 'android.support.v7.app.ActionBar$Tab')[1].click()

    def NotificationAcc(self):
        self.browser.find_element(By.XPATH,'//UIAAlert[1]/UIACollectionView[1]/UIACollectionCell[2]').click()


