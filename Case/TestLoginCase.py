__author__ = 'sunny.yu2'
from Case.BaseCase import BaseCase
from PageModel.LoginPage import LoginPage
from PageModel.BasePage import BasePage

class Login(BaseCase):

   def login(self,name,psw):
       loginPage = LoginPage()
       loginPage.Login(name,psw)

   def testRun(self):
       self.login(BaseCase.userName,BaseCase.password)
       basePage=BasePage()
       self.assertNotEqual(-1,basePage.getSource().find('Hi'))




