__author__ = 'sunny.yu2'
from PageModel.HomePage import HomePage
from PageModel.LeadPage import LeadPage
from PageModel.LoginPage import LoginPage
from Case.BaseCaseIOS import BaseCaseIOS

class Submit(BaseCaseIOS):

    def testRun(self):
        loginPage=LoginPage()
        loginPage.NotificationAcc()
        loginPage.Login(BaseCaseIOS.userName,BaseCaseIOS.password,'ios')
        self.homePage=HomePage()
        self.homePage.SelectMarketingPlace('ios')
        self.homePage.AddLead('ios')
        self.leadPage=LeadPage()
        self.leadPage.StudentName('APPautomation','ios')
        self.leadPage.StudentAge('10','ios')
        self.leadPage.PhoneNumber('13671556095','ios')
        self.leadPage.Scroll_down()
        self.leadPage.Submit('ios')
        self.leadPage.Alert('ios')
        self.assertEqual(self.homePage.LeadsNumber(),"1")


