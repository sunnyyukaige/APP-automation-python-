__author__ = 'sunny.yu2'
from Case.BaseCaseIOS import BaseCaseIOS
from PageModel.HomePage import HomePage
from PageModel.LoginPage import LoginPage

class SelectMarketing(BaseCaseIOS):

    def testRun(self):
        loginPage=LoginPage()
        loginPage.NotificationAcc()
        loginPage.Login(BaseCaseIOS.userName,BaseCaseIOS.password,'ios')
        self.homePage=HomePage()
        self.homePage.SelectMarketingPlace('ios')
        self.homePage.AddLead('ios')
