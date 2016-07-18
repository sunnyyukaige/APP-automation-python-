__author__ = 'sunny.yu2'
from Case.BaseCase import BaseCase
from PageModel.LoginPage import LoginPage
from PageModel.BasePage import BasePage

class Login(BaseCase):

   def login(self,name,psw,plateform):
       loginPage = LoginPage()
       loginPage.NotificationAcc()
       loginPage.Login(name,psw,plateform)

   def testRun(self):
       self.login('sunny','29394','ios')
       basePage=BasePage()
       self.assertNotEqual(-1,basePage.getSource().find('Hi'))




