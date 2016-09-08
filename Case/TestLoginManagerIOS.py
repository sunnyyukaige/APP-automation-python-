__author__ = 'sunny.yu2'
from Case.BaseCaseIOS import BaseCaseIOS
from PageModel.LoginPage import LoginPage
from PageModel.LoginManagerPage import LoginManagerPage
from PageModel.BasePage import BasePage


class LoginManager(BaseCaseIOS):

   def loginManager(self,name,psw,plateform):
       loginManagerpage = LoginManagerPage()
       loginManagerpage.Login(name,psw,plateform)

   def testRun(self):
       loginPage=LoginPage()
       loginPage.NotificationAcc()
       loginPage.GotoManagerLogin('ios')
       self.loginManager(BaseCaseIOS.managerName,BaseCaseIOS.managerPSW,'ios')
       basePage=BasePage()
       self.assertNotEqual(-1,basePage.getSource().find('Hi'))