__author__ = 'sunny.yu2'
from BaseCase import BaseCase
from PageModel.LoginPage import LoginPage
from PageModel.LoginManagerPage import LoginManagerPage
from PageModel.BasePage import BasePage


class LoginManager(BaseCase):

   def loginManager(self,name,psw):
       loginManagerpage = LoginManagerPage()
       loginManagerpage.InputUserName(name)
       loginManagerpage.InputPassWord(psw)
       loginManagerpage.Submit()

   def testRun(self):
       loginPage=LoginPage()
       loginPage.GotoManagerLogin()
       self.loginManager(self.config.get("configuration","managername"),self.config.get("configuration","managerpassword"))
       basePage=BasePage()
       self.assertNotEqual(-1,basePage.getSource().find('Hi'))