__author__ = 'sunny.yu2'
from BaseCase import BaseCase
from PageModel.LoginPage import LoginPage
from PageModel.LoginManagerPage import LoginManagerPage
from PageModel.BasePage import BasePage


class LoginManager(BaseCase):

   def loginManager(self,name,psw,plateform):
       loginManagerpage = LoginManagerPage()
       loginManagerpage.Login(name,psw,plateform)

   def testRun(self):
       loginPage=LoginPage()
       loginPage.GotoManagerLogin()
       self.loginManager('harryning','test','ios')
       basePage=BasePage()
       self.assertNotEqual(-1,basePage.getSource().find('Hi'))